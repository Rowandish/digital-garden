---
tags:
  - Dometrain
---
Questa nota riguarda come scrivere e strutturare al meglio gli [[Tipologie di test|integration test]] in ASP.NET.
Spesso vi è la necessità di testare non solo una singola unit of code indipendentemente da tutto ma l'intero flusso della mia applicazione, in particolare può essere una chiamata dal mondo esterno (esempio HTTP) che si riflette poi in una scrittura nel mondo esterno (esempio database).
Il problema è che il mondo esterno è lento e instabile e esce dallo scope del test in se: l'idea è che un test non dovrebbe essere influenzato o influire sul mondo esterno ma dovrebbe essere tutto self contained.
Per questo motivo sono necessari degli *Adapter* che sono delle classi che mascherano il mondo esterno comportandosi come questo ultimo.
![[Pasted image 20250131123108.png]]

## Step di esecuzione
1. **Setup**  
    Preparazione iniziale dell’ambiente di test:    
    - Seed del database (inserimento di dati iniziali)
    - Configurazione delle variabili di ambiente o file temporanei
2. **Dependency Mocking / Simulation**    
    - In un integration test **non si usano mock classici**, ma si evita comunque di chiamare **servizi esterni reali**.
    - Si possono usare **servizi finti** (stub o API locali che replicano il comportamento delle API esterne), in modo da mantenere il test **autonomo e controllabile**.
3. **Execution**    
    - I test vengono eseguiti con gli **stessi framework/tool degli unit test**, ma operano a un livello più alto (sull’intera applicazione o più componenti insieme).
4. **Assertion**    
    - Si verificano i risultati attesi:
        - Risposte HTTP
        - Stato del database
        - Contenuto di file, messaggi di log o eventi emessi
        - Coerenza del comportamento rispetto al flusso previsto
5. **Cleanup**    
    - Pulizia finale per non lasciare **residui nel database, file system o altri servizi**.
    - Fondamentale per evitare che un test influenzi i successivi o sporchi l’ambiente.

## Naming
Il progetto di test avrà nome `MyProject.Tests.Integration` e i metodi seguiranno lo stile  `HttpMethod_ReturnsXXX_WhenYYY`. Vedi [[Naming nei test]]
## Database
Per fare test su un database è una buona idea utilizzare [[Docker#^02a678|Docker]]: in questo modo divento agnostico dal PC su cui stanno girando i test utilizzando una sandbox dedicata ai test.
## `WebApplicationFactory<T>
Per testare una Minimal API, è buona pratica **avviare l'applicazione in modo controllato e isolato**, simulando un ambiente reale.  
La classe `WebApplicationFactory<T>` (dal pacchetto nuget `Microsoft.AspNetCore.Mvc.Testing`) serve a **creare un'app ASP.NET in memoria**, utile per:
- simulare vere richieste HTTP (con `HttpClient`)
- testare API end-to-end
- isolare l’ambiente di test dal progetto principale
- `T` rappresenta un tipo marker, usato per individuare l’assembly (di solito `Program` o un’interfaccia vuota come `IApiMarker`).
Il metodo fondamentale è `CreateClient()` che permette di creare un client HTTP virtuale che può chiamare vari metodi della API, esempio con metodi come `PostAsJsonAsync` e così via.
Per funzionare è necessario creare un'interfaccia *AssemblyMarker* nel progetto che contiene la REST API da testare in modo che il pacchetto sappia dove si trova il metodo `Program.cs` da lanciare automaticamente.

### Esempio base
Nell'esempio seguente ho il codice minimo possibile per ottenere un HttpClient e fare una richiesta GET alla mia API.
```csharp
public class GetCustomerControllerTests : IClassFixture<WebApplicationFactory<IApiMarker>>
{
    private readonly HttpClient _httpClient;

    public GetCustomerControllerTests(WebApplicationFactory<IApiMarker> appFactory)
    {
        _httpClient = appFactory.CreateClient();
    }
    
    [Fact]
    public async Task Get_ReturnsNotFound_WhenCustomerDoesNotExist()
    {
        // Act
        var response = await _httpClient.GetAsync($"customers/{Guid.NewGuid()}");
        
        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.NotFound);
        var problem = await response.Content.ReadFromJsonAsync<ValidationProblemDetails>();
        problem!.Title.Should().Be("Not Found");
        problem.Status.Should().Be(404);
    }
}
```
Questa classe poi viene utilizzata in questo modo:
```csharp
public class BookTests : IClassFixture<LibraryApiFactory>
{
    private readonly HttpClient _client;

    public BookTests(LibraryApiFactory factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task CreateBook_Returns201()
    {
        var book = new { Isbn = "1234567890123", Title = "Test Book" };
        var response = await _client.PostAsJsonAsync("/books", book);

        response.EnsureSuccessStatusCode();
        Assert.Equal(HttpStatusCode.Created, response.StatusCode);
    }
}
```
### Esempio completo
```csharp
/// <summary>
///     Factory per l'avvio e la configurazione dell'API durante i test di integrazione.
///     Estende WebApplicationFactory per permettere test realistici dell'intera applicazione.
///     IApiMarker è un'assembly marker. Serve per identificare l'assembly principale dell'applicazione.
/// </summary>
public class CustomerApiFactory : WebApplicationFactory<IApiMarker>, IAsyncLifetime
{
    // Utenti di test simulati per il mock server GitHub
    public const string ValidGithubUser = "validuser";
    public const string ThrottledUser = "throttle";

    // Container PostgreSQL tramite Testcontainers, per usare un DB reale isolato per i test. Il modo più moderno è usare PostgreSqlContainer invece di TestcontainerDatabase
    private readonly TestcontainerDatabase _dbContainer =
        new TestcontainersBuilder<PostgreSqlTestcontainer>()
            .WithDatabase(new PostgreSqlTestcontainerConfiguration
            {
                Database = "db",
                Username = "course",
                Password = "whatever"
            }).Build();

    // Server HTTP mock che simula le GitHub API
    private readonly GitHubApiServer _gitHubApiServer = new();

    /// <summary>
    ///     Metodo di inizializzazione asincrona, eseguito prima dei test.
    ///     Avvia i container e il server mock.
    /// </summary>
    public async Task InitializeAsync()
    {
        // Avvia il mock server GitHub
        _gitHubApiServer.Start();

        // Prepara utenti simulati nel mock server
        _gitHubApiServer.SetupUser(ValidGithubUser);
        _gitHubApiServer.SetupThrottledUser(ThrottledUser);

        // Avvia il container PostgreSQL
        await _dbContainer.StartAsync();
    }

    /// <summary>
    ///     Metodo di pulizia finale dopo i test.
    ///     Ferma i container e rilascia le risorse.
    /// </summary>
    public new async Task DisposeAsync()
    {
        await _dbContainer.DisposeAsync(); // Ferma e rimuove il container DB
        _gitHubApiServer.Dispose(); // Ferma il mock server GitHub
    }

    /// <summary>
    ///     Configura il WebHost (app ASP.NET) prima dell'avvio, sovrascrivendo servizi e client HTTP.
    /// </summary>
    protected override void ConfigureWebHost(IWebHostBuilder builder)
    {
        // Rimuove tutti i provider di log per evitare output nei test
        builder.ConfigureLogging(logging => { logging.ClearProviders(); });

        // Configura i servizi da usare **solo durante i test**
        builder.ConfigureTestServices(services =>
        {
            // Rimuove eventuali HostedService attivi (es. background jobs) che tipicamente non vogliamo che siano attivi durante i test
            services.RemoveAll(typeof(IHostedService));

            // Sostituisce la factory della connessione al DB con quella che punta al container PostgreSQL
            services.RemoveAll(typeof(IDbConnectionFactory));
            services.AddSingleton<IDbConnectionFactory>(_ =>
                new NpgsqlConnectionFactory(_dbContainer.ConnectionString));

            // Configura il client HTTP per GitHub in modo che punti al server finto invece che al GitHub reale
            services.AddHttpClient("GitHub", httpClient =>
            {
                httpClient.BaseAddress = new Uri(_gitHubApiServer.Url);
                httpClient.DefaultRequestHeaders.Add(
                    HeaderNames.Accept, "application/vnd.github.v3+json");
                httpClient.DefaultRequestHeaders.Add(
                    HeaderNames.UserAgent, $"Course-{Environment.MachineName}");
            });
        });
    }
}
```
Invece di PostgreSQL posso usare un db sqlite in memoria in questo modo
```csharp
// Rimuove la factory del database registrata nell'app
collection.RemoveAll(typeof(IDbConnectionFactory));

// Usa un database SQLite in memoria per i test
collection.AddSingleton<IDbConnectionFactory>(_ =>
	new SqliteConnectionFactory("DataSource=file:inmem?mode=memory&cache=shared"));
```

## Testare API esterne
Nell'integration testing non utilizzo mock per quanto riguarda db, file system o API ma utilizzo oggetti "veri". Cosa succede però se il mio sistema deve utilizzare API esterne che non dipendono da me? Per esempio devo chiamare le API di GitHub.
Le API esterne hanno vari problemi con i test in quanto:
* Potrebbero essere a pagamento
* Necessitano autenticazioni complesse
* Potrebbero essere down in qualsiasi momento
Ovviamente non voglio che i miei test soffrano dei punti sopra, conseguentemente in questo caso è ==necessario costruire una API "finta" che si comporta come quella vera==.
Quindi una API con autenticazione come GitHub, che risponde con un JSON analogo a quello di GitHub però in locale: in questo modo posso scrivere tutti gli integration test senza temere di pagare ogni chiamata o essere dipendente dal fatto che tale API esterna potrebbe andare down in qualsiasi momento.
Un comodo pacchetto nuget per far girare dei server api mockati è `WireMock`.
Per esempio nel codice della mia applicazione ho la chiamata alle api di github in questo modo:
```csharp
builder.Services.AddHttpClient("GitHub", httpClient =>
{
    httpClient.BaseAddress = new Uri(config.GetValue<string>("GitHub:ApiBaseUrl"));
    httpClient.DefaultRequestHeaders.Add(
        HeaderNames.Accept, "application/vnd.github.v3+json");
    httpClient.DefaultRequestHeaders.Add(
        HeaderNames.UserAgent, $"Course-{Environment.MachineName}");
});
```
utilizzata così:
```csharp
var client = _httpClientFactory.CreateClient("GitHub");
var response = await client.GetAsync($"/users/{username}");
```
Ora voglio usare wiremock nei test: per farlo devo creare una classe che utilizza wiremock per creare un'api che si comporta come github, esempio:
```csharp
public class GitHubApiServer : IDisposable
{
    private WireMockServer _server;

    public string Url => _server.Url!;

    public void Start()
    {
        _server = WireMockServer.Start();
    }

    public void SetupUser(string username)
    {
        _server.Given(Request.Create()
            .WithPath($"/users/{username}")
            .UsingGet())
            .RespondWith(Response.Create()
                .WithBody(GenerateGitHubUserResponseBody(username))
                .WithHeader("content-type", "application/json; charset=utf-8")
                .WithStatusCode(200));
    }

    public void SetupThrottledUser(string username)
    {
        _server.Given(Request.Create()
                .WithPath($"/users/{username}")
                .UsingGet())
            .RespondWith(Response.Create()
                .WithBody(@"{
    ""message"": ""API rate limit exceeded for 127.0.0.1. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)"",
    ""documentation_url"": ""https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting""
}")
                .WithHeader("content-type", "application/json; charset=utf-8")
                .WithStatusCode(403));
    }

    public void Dispose()
    {
        _server.Stop();
        _server.Dispose();
    }

    private static string GenerateGitHubUserResponseBody(string username)
    {
        return $@"{{
  ""login"": ""{username}"",
  ""id"": 67104228,
  //...
}}";
    }
}
```
e poi sovrascrivere la DI in modo che come url github utilizzi quello di wiremock in questo modo:
```csharp
public class CustomerApiFactory : WebApplicationFactory<IApiMarker>, IAsyncLifetime
{
    // Server HTTP mock che simula le GitHub API
    private readonly GitHubApiServer _gitHubApiServer = new();

    public async Task InitializeAsync()
    {
        // Avvia il mock server GitHub
        _gitHubApiServer.Start();

        // Prepara utenti simulati nel mock server
        _gitHubApiServer.SetupUser(ValidGithubUser);
        _gitHubApiServer.SetupThrottledUser(ThrottledUser);
    }

    /// <summary>
    ///     Metodo di pulizia finale dopo i test.
    ///     Ferma i container e rilascia le risorse.
    /// </summary>
    public new async Task DisposeAsync()
    {
        _gitHubApiServer.Dispose(); // Ferma il mock server GitHub
    }

    /// <summary>
    ///     Configura il WebHost (app ASP.NET) prima dell'avvio, sovrascrivendo servizi e client HTTP.
    /// </summary>
    protected override void ConfigureWebHost(IWebHostBuilder builder)
    {
        // Configura i servizi da usare **solo durante i test**
        builder.ConfigureTestServices(services =>
        {
            // Configura il client HTTP per GitHub in modo che punti al server finto invece che al GitHub reale
            services.AddHttpClient("GitHub", httpClient =>
            {
                httpClient.BaseAddress = new Uri(_gitHubApiServer.Url);
                httpClient.DefaultRequestHeaders.Add(
                    HeaderNames.Accept, "application/vnd.github.v3+json");
                httpClient.DefaultRequestHeaders.Add(
                    HeaderNames.UserAgent, $"Course-{Environment.MachineName}");
            });
        });
    }
}
```

## Testare con dati realistici
**[Bogus](https://github.com/bchavez/Bogus)** è un **pacchetto NuGet per generare dati finti (fake data)** in modo semplice, realistico e personalizzabile. È utile per simulare utenti, oggetti, liste di entità per testare la logica dell'applicazione
Va benissimo per test **ripetibili ma non statici**, con combinazioni diverse a ogni run
### Esempio
In questo caso Bogus viene usato per **generare dinamicamente un oggetto `CustomerRequest`** con valori realistici e casuali.
```csharp
private readonly Faker<CustomerRequest> _customerGenerator =
    new Faker<CustomerRequest>()
        .RuleFor(x => x.FullName, faker => faker.Person.FullName)
        .RuleFor(x => x.Email, faker => faker.Person.Email)
        .RuleFor(x => x.GitHubUsername, "nickchapsas") // valore fisso
        .RuleFor(x => x.DateOfBirth, faker => faker.Person.DateOfBirth.Date);
```
Qui stai dicendo: *"Ogni volta che genero un `CustomerRequest`, voglio che i campi abbiano questi valori:"*
- `FullName`: nome completo realistico
- `Email`: email realistica
- `GitHubUsername`: sempre `"nickchapsas"` (hardcoded)
- `DateOfBirth`: data di nascita realistica
```csharp
[Fact]
public async Task Create_ReturnsCreated_WhenCustomerIsCreated()
{
    // Arrange
    var customer = _customerGenerator.Generate();

    // Act
    var response = await _httpClient.PostAsJsonAsync("customers", customer);

    // Assert
    // ...
}
```

## UI Testing
L’UI testing con Playwright consiste nel testare un'applicazione simulando il comportamento reale di un utente all’interno di un browser.
Playwright apre una vera finestra del browser (o headless), naviga nelle pagine, clicca sui pulsanti, compila form, attende caricamenti e verifica che l’interfaccia risponda correttamente.
Questo approccio permette di validare l’esperienza utente end-to-end, assicurandosi che tutto il flusso visivo e interattivo dell’app funzioni come previsto, comprese le integrazioni con backend e database reali.

### Perché non si può usare WebApplicationFactory con Playwright
Nel contesto dei test end-to-end con Playwright su una webapp ASP.NET, `WebApplicationFactory` non è adatto perché l'app viene eseguita in-process e non è esposta su HTTP/HTTPS, mentre Playwright simula un utente reale che interagisce tramite browser e ha quindi bisogno di un'app realmente avviata e raggiungibile su una porta HTTP.
Per questo motivo è necessario avviare l’intera applicazione dentro un container Docker, insieme a un database reale.
E' necessario quindi creare un file `docker-compose` che costruisce l'app direttamente dal codice sorgente, la espone sulle porte 80 e 443, e la configura tramite variabili di ambiente. Queste variabili vengono poi mappate nel `Program.cs` con `config.AddEnvironmentVariables("CustomersWebApp_")`, che consente l’override dei valori presenti in `appsettings.json` usando la sintassi degli underscore. Gli underscore vengono convertiti internamente in due punti, quindi `CustomersWebApp_Database__ConnectionString` corrisponde a `Database:ConnectionString`, permettendo di sovrascrivere in modo semplice configurazioni come la connection string del database o URL di servizi esterni.
```yml
version: '3.9' # Versione del file docker-compose

services:

  # Servizio dell'applicazione ASP.NET
  test-app:
    build: ../../src/Customers.WebApp  # Costruisce l'immagine Docker partendo dal progetto ASP.NET
    ports:
      - "7780:443"  # Espone HTTPS sulla porta 7780 del host
      - "7779:80"   # Espone HTTP sulla porta 7779 del host
    environment:
      # Configura l'app ASP.NET per ascoltare su entrambe le porte
      - ASPNETCORE_URLS=https://+:443;http://+:80
      
      # Imposta il certificato HTTPS per Kestrel
      - ASPNETCORE_Kestrel__Certificates__Default__Password=Test1234!
      - ASPNETCORE_Kestrel__Certificates__Default__Path=/https/cert.pfx

      # Ambiente di esecuzione dell'app (Production simula l'ambiente reale)
      - ASPNETCORE_Environment=Production

      # Override delle configurazioni dell'app tramite variabili di ambiente
      # Queste corrispondono a: Database:ConnectionString e GitHub:ApiBaseUrl
      - CustomersWebApp_Database__ConnectionString=Server=test-db;Port=5432;Database=mydb;User ID=course;Password=changeme;
      - CustomersWebApp_GitHub__ApiBaseUrl=http://localhost:9850

    # Fa partire l'app solo dopo che il DB è pronto
    depends_on:
      test-db:
        condition: service_healthy

  # Servizio del database PostgreSQL
  test-db:
    image: postgres:latest  # Usa l'immagine ufficiale più aggiornata di PostgreSQL
    restart: always         # Riavvia il container in caso di crash
    environment:
      - POSTGRES_USER=course         # Utente del database
      - POSTGRES_PASSWORD=changeme   # Password dell'utente
      - POSTGRES_DB=mydb             # Nome del database da creare al primo avvio
    ports:
      - '5435:5432'  # Espone la porta del database sulla macchina host (utile per debugging locale)

    # Controlla che il database sia pronto prima di far partire l'app
    healthcheck:
      test: [ "CMD-SHELL", "pg_isready" ]  # Verifica se il DB è raggiungibile
      interval: 2s                         # Frequenza del controllo
      timeout: 5s                          # Timeout per ciascun tentativo
      retries: 10                          # Numero massimo di tentativi prima di segnare il container come unhealthy
```

### `FluentDocker`
`FluentDocker` è una libreria .NET che permette di controllare Docker (container, immagini, compose) direttamente dal codice, in modo fluido e dichiarativo.
Posso utilizzarla per **avviare automaticamente l’ambiente Docker Compose** all’interno del contesto di test, senza doverlo eseguire manualmente da terminale prima di lanciare i test.
In pratica, **integri l’infrastruttura di test direttamente nel codice**, così quando parte il test:
- Docker Compose viene lanciato.
- I container vengono creati e avviati.
- L'app è raggiungibile su `https://localhost:7780`.
- Il test Playwright può iniziare a interagire con la UI reale.
Questo approccio è perfetto per test end-to-end come quelli che fai con Playwright, perché crea un ciclo completo e ripetibile: ogni volta che fai partire i test, l’ambiente Docker viene costruito da zero, incluso il database e l'app, con le giuste configurazioni. Non serve nulla di esterno né passaggi manuali. Hai isolamento, coerenza e un ambiente realistico.

#### Esempio
Nel costruttore `_dockerService` usi `new Builder()` per definire in modo fluido il comportamento desiderato:
```csharp
private readonly ICompositeService _dockerService = new Builder()
    .UseContainer()                         // Avvia un ambiente containerizzato
    .UseCompose()                           // Usa un file docker-compose
    .FromFile(DockerComposeFile)            // Specifica il file docker-compose da usare
    .RemoveOrphans()                        // Rimuove eventuali container orfani non più necessari
    .WaitForHttp("test-app", AppUrl)        // Aspetta che il servizio test-app risponda su AppUrl
    .Build();
```
In questo modo, al momento dell’invocazione di `_dockerService.Start();` all’interno del metodo `InitializeAsync`, `FluentDocker` lancia effettivamente Docker Compose con tutte le configurazioni che hai definito, attende che l’app sia disponibile via HTTP(S) e rende l’ambiente pronto per l’esecuzione dei test Playwright.
Alla fine, nel `DisposeAsync`, `_dockerService.Dispose()` ferma e pulisce tutto in automatico, evitando che i container restino attivi dopo i test.
