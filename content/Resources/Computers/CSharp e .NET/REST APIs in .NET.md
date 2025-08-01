---
tags:
  - Dometrain
---
## Introduzione
### Caratteristiche di un sistema REST

#### Uniform Interface
Questa è una delle caratteristiche principali di REST, che garantisce coerenza nelle interazioni tra client e server. Si basa su quattro principi:
- **Identification of resources (Identificazione delle risorse)**: Ogni risorsa è identificata in modo univoco tramite un URL.
- **Manipulation of resources through representations (Manipolazione delle risorse tramite rappresentazioni)**: I client interagiscono con le risorse attraverso rappresentazioni (es. JSON, XML) e possono modificarle tramite operazioni HTTP (GET, POST, PUT, DELETE).
- **Self-descriptive messages (Messaggi auto-descrittivi)**: Ogni richiesta contiene tutte le informazioni necessarie per essere compresa, senza dipendere dallo stato del server.
- **Hypermedia as the engine of application state (HATEOAS - Hypermedia come motore dello stato dell'applicazione)**: Le risposte possono contenere link per guidare il client nelle interazioni successive.
#### Stateless
Ogni richiesta HTTP è indipendente e non dipende dalle richieste precedenti. Il server non memorizza informazioni sullo stato del client tra una richiesta e l’altra.
#### Cacheable

Le risposte possono essere memorizzate nella cache per migliorare le prestazioni e ridurre il carico sul server. Il server può indicare quali risposte possono essere memorizzate e per quanto tempo.
#### Client-Server
L’architettura separa client e server, consentendo l’evoluzione indipendente di entrambe le parti. Il client si occupa dell’interfaccia utente, mentre il server gestisce i dati e la logica dell’applicazione.
#### Layered System
L'architettura può essere composta da più livelli (proxy, gateway, load balancer, ecc.), senza che il client debba conoscere i dettagli interni di ciascun livello.

### HTTP verbs
- **POST - Create**: Utilizzato per creare una nuova risorsa sul server. Esempio: inviare dati per creare un nuovo utente.
- **GET - Retrieve**: Serve per ottenere informazioni su una risorsa esistente senza modificarla. Esempio: ottenere i dettagli di un prodotto.
- **PUT - Complete update**: Aggiorna interamente una risorsa esistente, sostituendola con una nuova versione. Esempio: aggiornare il profilo di un utente.
- **PATCH - Partial update**: Modifica solo alcuni campi di una risorsa, senza sostituirla completamente. Esempio: cambiare solo l'email di un utente. Non usato.
- **DELETE - Delete**: Rimuove una risorsa dal server. Esempio: cancellare un ordine dal sistema.

### Status code
Ad ogni richiesta viene fornito uno status code che dovrebbe essere parlante, vediamo gli standard.
* ***POST**
	- **Single resource (`/items/1`)**: **N/A** → Non si può fare un POST su una risorsa specifica già esistente.
	- **Collection resource (`/items`)**:
	    - **201 (Created)** → Risorsa creata con successo (Location header con il nuovo URL).
	    - **202 (Accepted)** → La richiesta è accettata ma non ancora elaborata.
* ***GET**
	- **Single resource (`/items/1`)**:
	    - **200 (OK)** → Risorsa trovata e restituita.
	    - **404 (Not Found)** → Risorsa non esistente.
	- **Collection resource (`/items`)**:
	    - **200 (OK)** → Lista delle risorse restituita.
* ***PUT**
	- **Single resource (`/items/1`)**:
	    - **200 (OK)** → Risorsa aggiornata con successo.
	    - **204 (No Content)** → Aggiornamento riuscito ma senza risposta nel corpo.
	    - **404 (Not Found)** → Risorsa non esistente.
	- **Collection resource (`/items`)**:
	    - **405 (Method Not Allowed)** → Non è consentito aggiornare l’intera collezione.
* ***DELETE**
	- **Single resource (`/items/1`)**:
	    - **200 (OK)** → Risorsa eliminata con successo e dettagli restituiti.
	    - **404 (Not Found)** → Risorsa inesistente.
	- **Collection resource (`/items`)**:
	    - **405 (Method Not Allowed)** → Non è consentito eliminare un'intera collezione.
### Struttura progetti
Tipicamente una REST API viene strutturata secondo tre progetti distinti (qui prendiamo come esempio `Movies`:
1. `Movies.Api`:
	- È il progetto principale che espone l'API REST.
	- Contiene i **controller** (cartella _Controllers_) che gestiscono le richieste HTTP.
	- Utilizza i file di configurazione **appsettings.json** e **appsettings.Developer.json**.
	- Ha una dipendenza da **Movies.Application**, perché deve chiamare i servizi che contengono la logica di business.
2. `Movies.Application`:
	- Contiene la logica di business e i servizi applicativi.
	- Implementa la logica di gestione dei film, come la validazione, il recupero e la modifica dei dati.
	- Non si occupa direttamente dell'accesso ai dati, ma potrebbe interagire con un altro livello (ad esempio un repository o un database).
	- Non dipende dall'API, perché deve essere indipendente dalla tecnologia di esposizione (può essere riutilizzato in altre interfacce, come console app o gRPC).
	- Dipende da **Movies.Contracts** per i modelli di dati condivisi.
3. `Movies.Contracts`:
	- Contiene le classi **DTO (Data Transfer Object)**, interfacce e modelli di dati utilizzati da tutta l’applicazione.
	- Serve per definire contratti chiari tra le diverse parti del sistema, evitando dipendenze circolari.
	- Non ha dipendenze da nessun altro progetto, perché deve rimanere il più indipendente possibile.

Schema delle dipendenze:
```
Movies.Api (Presentazione) 
   ├──> dipende da Movies.Application (Logica di Business)
   │         ├──> dipende da Movies.Contracts (Modelli e DTO)
   └──> dipende da Movies.Contracts (Modelli e DTO)
```

Questa organizzazione segue il **principio della separazione delle responsabilità (Separation of Concerns - SoC)** per garantire modularità, mantenibilità e scalabilità.
Esistono altre strutture, esempio la [[Clean Architecture]].

## Contracts
Il progetto **Contracts** in un'applicazione **ASP.NET** ha lo scopo di definire i **modelli di scambio dati** tra i diversi componenti del sistema, come API, client e servizi interni.  
Questi modelli tipicamente includono **Request**, **Response**, **DTO (Data Transfer Objects)** e a volte **Enums** o **Common** structures.
Il progetto `Contracts` assicura quindi che i dati trasmessi tra API e client siano strutturati in modo chiaro e coerente.
Il progetto è tipicamente strutturato in questo modo:
```
Project.Contracts/
│
├── Requests/
│   ├── CreateObjectRequest.cs
│   ├── UpdateObjectRequest.cs
│   ├── ... .cs
│
├── Responses/
│   ├── ObjectResponse.cs
│   ├── MultipleObjectsResponse.cs
│   ├── ... .cs
├── DTO/
├── Enums/
├── Common/
│
└── (eventuali altre cartelle o file)
```

### 📂 Requests
Questi oggetti vengono usati nei controller o nei servizi per la validazione e la trasformazione in entità di dominio.
Questa cartella contiene i modelli di richiesta usati dai client per inviare dati all'API.  
Esempio per una api di gestione film:
```csharp
public class CreateMovieRequest
{
    public required string Title { get; init; }

    public required int YearOfRelease { get; init; }

    public required IEnumerable<string> Genres { get; init; } = Enumerable.Empty<string>();
}
public class UpdateMovieRequest
{
    public required string Title { get; init; }

    public required int YearOfRelease { get; init; }

    public required IEnumerable<string> Genres { get; init; } = Enumerable.Empty<string>();
}
```
### 📂 Responses
Questa cartella contiene i modelli di risposta restituiti dalle API.  
Questi oggetti vengono utilizzati per **serializzare** i dati inviati ai client.
Esempio per una api di gestione film:
```csharp
public class MovieResponse
{
    public required Guid Id { get; init; }
    
    public required string Title { get; init; }

    public required int YearOfRelease { get; init; }

    public required IEnumerable<string> Genres { get; init; } = Enumerable.Empty<string>();
}
public class MoviesResponse
{
    public required IEnumerable<MovieResponse> Items { get; init; } = Enumerable.Empty<MovieResponse>();
}
```
### 📂 DTO (Data Transfer Objects)
- Contengono oggetti utilizzati per il **trasporto dati tra livelli dell'applicazione**.
- Simili a `Request` e `Response`, ma possono essere più generici o usati internamente.
### 📂 Enums
Definiscono costanti usate nei contratti per rappresentare valori discreti, es.:
```csharp
public enum MovieGenre
{
	Action,
	Comedy,
	Drama,
	Horror,
	SciFi
}
```

### 📂 Common
Contiene oggetti usati sia in `Requests` che `Responses` come modelli comuni.

## Controller
In un'applicazione **ASP.NET**, un **Controller** è una classe che gestisce le richieste HTTP e determina quale azione eseguire in risposta.
Si occupa di:
- **Ricevere le richieste** HTTP dall'utente.
- **Elaborare i dati** tramite il **Model** (ad esempio, interagendo con un database).
- **Restituire una risposta** alla **View** (nel caso di applicazioni MVC) o un **oggetto JSON/XML** (nel caso di API).

I Controller sono solitamente definiti come classi che ereditano da `Controller` o `ControllerBase` (per API) e contengono **metodi action**, ognuno dei quali gestisce un tipo di richiesta (es. `GET`, `POST`).
Esempio di un controller che riceve in ingresso una `IService` che sarà una classe mapping in `Application` che poi utilizzerà una `IRepository` per la comunicazione con il database o in-memory database. Tale classe inoltre si occuperà della validazione degli oggetti con un `validator` (vedi sotto).
```csharp
[ApiController]
public class SampleController : ControllerBase
{
    private readonly IMovieService _movieService;
      
    public SampleController(IMovieService service)  
    {  
        _movieService = service;  
    }

    [HttpGet(ApiEndpoints.Movies.Get)]
    public async Task<IActionResult> Get([FromRoute] Guid id)
    {
        var obj = await _movieService.GetByIdAsync(id);
        if (obj is null)
        {
            return NotFound();
        }

        var response = obj.MapToResponse();
        return Ok(response);
    }
}
```
Se si utilizza Clean Architecture probabilmente non si utilizzerà un `IMovieService` ma il pattern [[Clean Architecture#^a1115b|mediator]].

### Mapping
Ogni API del controller riceve tipicamente in ingresso un oggetto `Request`, definito nel progetto `Contracts` a cui bisogna poi fare il mapping ad un oggetto del mio modello (definito nel progetto `Appolication`).
Per esempio ricevo dall'api un oggetto di tipo `CreateMovieRequest` e in qualche modo devo convertirlo nell'oggetto `Movie` del mio modello.
Dato che è un'operazione estremamente semplice non servono pacchetti nuget o cose particolari, basta creare una classe `ContractMapping` nel progetto `Api` che crea delle extension delle request come in questo esempio:
```csharp
public static Movie MapToMovie(this CreateMovieRequest request)  
{  
    return new Movie  
    {  
        Id = Guid.NewGuid(),  
        Title = request.Title,  
        YearOfRelease = request.YearOfRelease,  
        Genres = request.Genres.ToList()  
    };
}
public static MovieResponse MapToResponse(this Movie movie)  
{  
    return new MovieResponse  
    {  
        Id = movie.Id,  
        Title = movie.Title,  
        YearOfRelease = movie.YearOfRelease,  
        Genres = movie.Genres  
    };  
}
```
In modo da poter scrivere codice analogo a
```csharp
[HttpPost(ApiEndpoints.Movies.Create)]  
public async Task<IActionResult> Create([FromBody]CreateMovieRequest request) {
	// Conversione all'oggetto del dominio "Movie"
    var movie = request.MapToMovie();  
    await _movieRepository.CreateAsync(movie);
    // Conversione alla response da inviare al mondo esterno  
    var movieResponse = movie.MapToResponse();
    // CreatedAtAction permette di avere il location header corretto
    return CreatedAtAction(nameof(Get), new { id = movie.Id }, movieResponse);  
}
```


## Validation
La validazione degli oggetti a livello di business logic avviene in `Application` usando il pacchetto nuget `fluentValidation` che permette di definire come i nostri modelli devono essere validati ma in modo molto pulito.
Per validare l'oggetto `Movie`, per esempio, basta creare una classe che eredita da `AbstractValidator<Movie>` e usare i metodi `RuleFor` come sotto.
```csharp
public class MovieValidator : AbstractValidator<Movie>  
{  
    private readonly IMovieRepository _movieRepository;  
  
    public MovieValidator(IMovieRepository movieRepository)  
    {        _movieRepository = movieRepository;  
        RuleFor(x => x.Id)  
            .NotEmpty();  
  
        // ...
  
        // Lo slug ha bisogno di una validazione custom  
        RuleFor(x => x.Slug)  
            .MustAsync(ValidateSlug)  
            .WithMessage("This movie already exists in the system");  
    }  
    /// <summary>  
    ///     Dato uno slug devo verificare che questo non esista già nel database, per quello ho bisogno della _movieRepository    /// </summary>    private async Task<bool> ValidateSlug(Movie movie, string slug, CancellationToken token = default)  
    {        var existingMovie = await _movieRepository.GetBySlugAsync(slug);  
  
        // Se esiste deve essere quello che sto validando  
        if (existingMovie is not null)  
            return existingMovie.Id == movie.Id;  
        return existingMovie is null;  
    }}
```
Per inizializzarlo basta usare questo metodo quando inizializzo la DI:
```csharp
services.AddValidatorsFromAssemblyContaining<IApplicationMarker>(ServiceLifetime.Singleton);
```
con l'interfaccia `IApplicationMarker` una interfaccia vuota che serve solo come marker per trovare l'assembly che contiene i validator.
Fatto questo per validare vado nella classe `Service` (che ricordo che è la classe definita in `Application` e usata in `Api` che utilizza la `repository` per fare le query a database); vedi esempio sotto.
```csharp
public class MovieService : IMovieService
{
    private readonly IMovieRepository _movieRepository;
    private readonly IValidator<Movie> _movieValidator;

    public MovieService(IMovieRepository movieRepository, IValidator<Movie> movieValidator)
    {
        _movieRepository = movieRepository;
        _movieValidator = movieValidator;
    }

    public async Task<bool> CreateAsync(Movie movie, CancellationToken token = default)
    {
        await _movieValidator.ValidateAndThrowAsync(movie, cancellationToken: token);
        return await _movieRepository.CreateAsync(movie, token);
    }
}
```
Ultima cosa: dato che la validazione fa un `throw ValidationException` ha molto senso creare un `Middleware` di tutte le richieste che avvengono all'API e wrapparle da questo ultimo.
Il codice seguente è praticamente standard e si può copincollare ovunque.
In `Program.cs`
```csharp
app.UseMiddleware<ValidationMappingMiddleware>();
```
e poi questa è la classe middleware che wrappa con un `catch (ValidationException ex)`.
```csharp
public class ValidationMappingMiddleware
{
    private readonly RequestDelegate _next;

    public ValidationMappingMiddleware(RequestDelegate next)
    {
        _next = next;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        try
        {
            await _next(context);
        }
        catch (ValidationException ex)
        {
            context.Response.StatusCode = 400;
            var validationFailureResponse = new ValidationFailureResponse
            {
                Errors = ex.Errors.Select(x => new ValidationResponse
                {
                    PropertyName = x.PropertyName,
                    Message = x.ErrorMessage
                })
            };

            await context.Response.WriteAsJsonAsync(validationFailureResponse);
        }
    }
}
```

## Cancel request
Ogni richiesta HTTP può essere annullata tramite un comando specifico, ma questo annullamento deve essere correttamente gestito dall'API.
Ogni metodo del `Controller` ammette come secondo parametro un `CancellationToken` che automaticamente viene annullato quando il client annulla la richiesta.
Questo token deve essere passato in tutti i metodi fino ad arrivare, esempio al database.
Se si usa `Dapper` e si vuole cancellare una query è necessario usare `CommandDefinition` in quanto questo ha un `CancellationToken` in ingresso; vedi esempio sotto.
```csharp
public async Task<IEnumerable<Movie>> GetAllAsync(CancellationToken token = default)
{
    using var connection = await _dbConnectionFactory.CreateConnectionAsync(token);
    var result = await connection.QueryAsync(new CommandDefinition("""
        QUERY
        """, cancellationToken: token));
    
    return result.Select(x => new Movie
    {
        Id = x.id,
        Title = x.title,
        YearOfRelease = x.yearofrelease,
        Genres = Enumerable.ToList(x.genres.Split(','))
    });
}
```
## Authentication e Authorization
Ci sono due lavori distinti che una API deve gestire: autenticare un utente, quindi capire chi è, e autorizzarlo, quindi capire cosa questo ultimo può o non può fare.
==Dato che le API sono stateless tutte le informazioni devono essere passate ad ogni singola chiamata, in particolare questo avviene tramite l'invio di un JWT==.
### JWT
Un **JWT (JSON Web Token)** è uno standard aperto (RFC 7519) per la creazione di **token sicuri** e **compatti** che possono essere utilizzati per l'autenticazione e l'autorizzazione tra due parti.
Un JWT è composto da **tre parti**, separate da un punto (`.`):
1. **Header**: contiene informazioni sulla firma e l'algoritmo utilizzato per firmare il token.   
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```
2. **Payload**: contiene le **informazioni** dell'utente (dette **claims**), come ID, ruoli o permessi. Alcune sono standard (esempio `sub`) mentre altre sono custom.    
```json
{
  "sub": "1234567890",
  "name": "Mario Rossi",
  "admin": true,
  "exp": 1710000000
}
```
1. **Signature**: serve a verificare che il token non sia stato alterato. È creata con un algoritmo di hash (es. **HMAC, RSA**) usando una chiave segreta.
### Autenticazione
 L'utente si autentica con **email e password**:
* Il server verifica le credenziali da un server apposito e, se valide, genera un JWT con le informazioni dell'utente.
* Il JWT viene inviato al client e memorizzato e inviato alla API ad ogni richiesta.

Per aggiungere l'autenticazione all'API tramite JWT devo installare il pacchetto nuget `Microsoft.AspNetCore.Authentication.JwtBearer` e in `Program.cs` scrivere qualcosa come il seguente:
```csharp
builder.Services.AddAuthentication(x =>
{
    x.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
    x.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
    x.DefaultScheme = JwtBearerDefaults.AuthenticationScheme;
}).AddJwtBearer(x =>
{
    x.TokenValidationParameters = new TokenValidationParameters
    {
        // In questo caso uso una chiave simmetrica memorizzata in config["Jwt:Key"], nel mondo reale sarà una chiave asimmetrica e di certo non memorizzata in config ma in qualcosa come AWS Secrest Manager.
        IssuerSigningKey = new SymmetricSecurityKey(
            Encoding.UTF8.GetBytes(config["Jwt:Key"]!)),
        // Verifica la firma del JWT (fondamentale)
        ValidateIssuerSigningKey = true,
        // Non ammette token obsoleti
        ValidateLifetime = true,
        // Verifica anche che l'issuer e l'audience del JWT siano corrette
        ValidIssuer = config["Jwt:Issuer"],
        ValidAudience = config["Jwt:Audience"],
        ValidateIssuer = true,
        ValidateAudience = true
    };
});

...

app.UseAuthentication();
```
Una volta fatto per ogni controller posso definire se lo voglio con autenticazione con l'attributo `[Authorize]` alla classe indicando che tutte le API devono essere autorizzate e posso eventualmente escluderne alcune con `[AllowAnonymous]`.
### Autorizzazione
 Il client include il JWT nelle richieste API (es. nell'`Authorization` header come `Bearer <token>`).
    - Il server **verifica la firma** del token e ne controlla la validità (es. scadenza, permessi).
    - Se il token è valido, l'utente può accedere alla risorsa.
Nell'esempio seguente definiamo delle stringhe che identificano dei nomi di determinate policy e di determinati claim
```csharp
public static class AuthConstants
{
    public const string AdminUserPolicyName = "Admin";
    public const string AdminUserClaimName = "admin";
    
    public const string TrustedMemberPolicyName = "Trusted";
    public const string TrustedMemberClaimName = "trusted_member";
}
// .. in Program.cs
builder.Services.AddAuthorization(x =>
{
    // Solo gli utenti con il claim "admin" possono accedere
    x.AddPolicy(AuthConstants.AdminUserPolicyName, 
        p => p.RequireClaim(AuthConstants.AdminUserClaimName, "true"));
    
    // Solo gli utenti con il claim "trusted_member" OR "admin" possono accedere
    x.AddPolicy(AuthConstants.TrustedMemberPolicyName,
        p => p.RequireAssertion(c => 
            c.User.HasClaim(m => m is { Type: AuthConstants.AdminUserClaimName, Value: "true" }) || 
            c.User.HasClaim(m => m is { Type: AuthConstants.TrustedMemberClaimName, Value: "true" })));
});

...

app.UseAuthorization();
```

### Ottenere l'userid
Un trucco per ottenere l'userid chiamante è creare un'`Extension method` di `HttpContext`, per esempio:
```csharp
public static Guid? GetUserId(this HttpContext context)  
{  
    var userId = context.User.Claims.SingleOrDefault(x => x.Type == "userid");  
  
    if (Guid.TryParse(userId?.Value, out var parsedId))  
    {        return parsedId;  
    }  
    return null;  
}
```
In questo modo posso ottenere l'user id facilmente con
```csharp
var userId = HttpContext.GetUserId();
```

## Filtering e sorting
Ammettiamo di voler implementare dei filtraggi nella  richiesta di una API, per esempio nell'API che fornisce tutti i film voglio filtrare per anno di uscita oppure per wildcard con il titolo o entrambi.
Inoltre voglio poter ordinare i risultati secondo una property che passo in ingresso.
Infine voglio poter fornire i risultati paginati.
```
api/movies?title=XXX&year=1980&SortBy=title
```
Per prima cosa creo una classe nel progetto `Contracts` property che descrive quanto può fare l'utente:
```csharp
public class PagedRequest  
{  
    public required int Page { get; init; } = 1;  
    public required int PageSize { get; init; } = 10;  
}

public class GetAllMoviesRequest : PagedRequest  
{  
    public required string? Title { get; init; }  
    public required int? Year { get; init; }  
    public required string? SortBy { get; init; }  
}
```
Questa è un esempio di endpoint sul controller: la classe sopra viene passata con l'attributo `[FromQuery]`.
```csharp
public async Task<IActionResult> GetAll(  
    [FromQuery] GetAllMoviesRequest request, CancellationToken token)  
{  
    var userId = HttpContext.GetUserId();  
    var options = request.MapToOptions()  
        .WithUser(userId);  
    var movies = await _movieService.GetAllAsync(options, token);  
    var movieCount = await _movieService.GetCountAsync(options.Title, options.YearOfRelease, token);  
    var moviesResponse = movies.MapToResponse(request.Page, request.PageSize, movieCount);  
    return Ok(moviesResponse);  
}
```
Viene creato un oggetto `GetAllMoviesOptions` dal mapper che contiene le opzioni fornite dall'utente più altre property aggiuntive.
```csharp
public static GetAllMoviesOptions MapToOptions(this GetAllMoviesRequest request)  
{  
    return new GetAllMoviesOptions  
    {  
        Title = request.Title,  
        YearOfRelease = request.Year,  
        SortField = request.SortBy?.Trim('+', '-'),  
        SortOrder = request.SortBy is null ? SortOrder.Unsorted :  
            request.SortBy.StartsWith('-') ? SortOrder.Descending : SortOrder.Ascending,  
        Page = request.Page,  
        PageSize = request.PageSize  
    };  
}

public class GetAllMoviesOptions  
{  
    public string? Title { get; set; }  
    public int? YearOfRelease { get; set; }  
    public Guid? UserId { get; set; }  
    public string? SortField { get; set; }  
    public SortOrder? SortOrder { get; set; }  
    public int Page { get; set; }  
    public int PageSize { get; set; }  
}  
  
public enum SortOrder  
{  
    Unsorted,  
    Ascending,  
    Descending  
}
```
Ora questo oggetto `GetAllMoviesOptions` viene passato al metodo `GetAllAsync` della classe `Service` il quale effettua delle validazioni e poi rilancia al repository
```csharp
public async Task<IEnumerable<Movie>> GetAllAsync(GetAllMoviesOptions options, CancellationToken token = default)  
{  
    await _optionsValidator.ValidateAndThrowAsync(options, token);  
    return await _movieRepository.GetAllAsync(options, token);  
}
```
Una volta fatta la query devo fornire una response con tutte le info anche sul paging, per farlo creo il seguente metodo nel mapping
```csharp
public static MoviesResponse MapToResponse(this IEnumerable<Movie> movies,  
    int page, int pageSize, int totalCount)  
{  
    return new MoviesResponse  
    {  
        Items = movies.Select(MapToResponse),  
        Page = page,  
        PageSize = pageSize,  
        Total = totalCount  
    };
}
public static MovieResponse MapToResponse(this Movie movie)  
{  
    return new MovieResponse  
    {  
        Id = movie.Id,  
        Title = movie.Title,  
        Slug = movie.Slug,  
        Rating = movie.Rating,  
        UserRating = movie.UserRating,  
        YearOfRelease = movie.YearOfRelease,  
        Genres = movie.Genres  
    };  
}
```
Creando la seguente classe `MoviesResponse`:
```csharp
public class MoviesResponse : PagedResponse<MovieResponse>{};
public class PagedResponse<TResponse>  
{  
    public required IEnumerable<TResponse> Items { get; init; } = Enumerable.Empty<TResponse>();  
    public required int PageSize { get; init; }  
    public required int Page { get; init; }  
    public required int Total { get; init; }  
    public bool HasNextPage => Total > (Page * PageSize);  
}
```

## Swagger
Swagger permette di generare una pagina di documentazione automatica per le API con la possibilità sia di vederle che di interagirvi stile postman.
### Autenticazione
Per le API autenticate posso dire a Swagger di creare un pulsante per inserire il token JWT da usare per l'autenticazione, per farlo scrivere il seguente codice:
```csharp
public class ConfigureSwaggerOptions : IConfigureOptions<SwaggerGenOptions>
{
    private readonly IApiVersionDescriptionProvider _provider;
    private readonly IHostEnvironment _environment;

    public ConfigureSwaggerOptions(IApiVersionDescriptionProvider provider, IHostEnvironment environment)
    {
        _provider = provider;
        _environment = environment;
    }

    public void Configure(SwaggerGenOptions options)
    {
        options.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
        {
            In = ParameterLocation.Header,
            Description = "Please provide a valid token",
            Name = "Authorization",
            Type = SecuritySchemeType.Http,
            BearerFormat = "JWT",
            Scheme = "Bearer"
        });

        options.AddSecurityRequirement(new OpenApiSecurityRequirement
        {
            {
                new OpenApiSecurityScheme
                {
                    Reference = new OpenApiReference
                    {
                        Type = ReferenceType.SecurityScheme,
                        Id = "Bearer"
                    }
                },
                Array.Empty<string>()
            }
        });
    }
}
```
e poi in `Program.cs` usare la DI per inizializzare la classe `ConfigureSwaggerOptions`:
```csharp
builder.Services.AddTransient<IConfigureOptions<SwaggerGenOptions>, ConfigureSwaggerOptions>();  
builder.Services.AddSwaggerGen(x => x.OperationFilter<SwaggerDefaultValues>());
...
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}
```

### Descrivere gli status code
Swagger di default non scrive esplicitamente i vari status code che fornisce la mia API ma è necessario esplicitarli tramite l'attributo `ProducesResponseType`.
Esempio:
```csharp
[Authorize(AuthConstants.TrustedMemberPolicyName)]
[HttpPut(ApiEndpoints.Movies.Update)]
[ProducesResponseType(typeof(MovieResponse), StatusCodes.Status200OK)]
[ProducesResponseType(StatusCodes.Status404NotFound)]
[ProducesResponseType(typeof(ValidationFailureResponse), StatusCodes.Status400BadRequest)]
public async Task<IActionResult> Update([FromRoute]Guid id,
    [FromBody]UpdateMovieRequest request,
    CancellationToken token)
{
    // ...
    return Ok(response);
}
```

## Health checks
Ogni REST API dovrebbe esporre un'API dedicata per la verifica della "salute" del servizio, questa API non viene chiamata dal dominio dell'applicazione ma da altri servizi esterni: per esempio se ho un load balancer posso evitare di chiamare tutte le API che non sono healthy.
Per farlo basta aggiungere queste righe nel `Program.cs` che indicano che la chiamata all'api `/_health` porta alla chiamata del metodo in `DatabaseHealthCheck` che verifica che il database sia ok.
```csharp
builder.Services.AddHealthChecks()  
    .AddCheck<DatabaseHealthCheck>(DatabaseHealthCheck.Name);
...
app.MapHealthChecks("_health");
```
E' buona norma verificare la salute di tutte le dipendenze che la mia API utilizza e sono in salute se tutte sono in salute.
```csharp
public class DatabaseHealthCheck : IHealthCheck
{
    public const string Name = "Database";
    
    private readonly IDbConnectionFactory _dbConnectionFactory;
    private readonly ILogger<DatabaseHealthCheck> _logger;

    public DatabaseHealthCheck(IDbConnectionFactory dbConnectionFactory, ILogger<DatabaseHealthCheck> logger)
    {
        _dbConnectionFactory = dbConnectionFactory;
        _logger = logger;
    }

    public async Task<HealthCheckResult> CheckHealthAsync(
        HealthCheckContext context, CancellationToken cancellationToken = new())
    {
        try
        {
            _ = await _dbConnectionFactory.CreateConnectionAsync(cancellationToken);
            return HealthCheckResult.Healthy();
        }
        catch (Exception e)
        {
            const string errorMessage = "Database is unhealthy";
            _logger.LogError(errorMessage, e);
            return HealthCheckResult.Unhealthy(errorMessage, e);
        }
    }
}
```

## Response caching
L'idea alla base della cache è evitare di ricalcolare il risultato di una chiamata API ogni volta, restituendo sempre lo stesso risultato per richieste identiche. Questo obiettivo può essere raggiunto:
- **Client-side**, tramite gli header HTTP (ma dipende dalla fiducia nel client).
- **Server-side**, tramite **output caching**, che garantisce il caching al 100% gestito dal server.
### Client side Response Caching
Per abilitare la cache lato client, si utilizza il middleware `ResponseCaching` in **ASP.NET Core**.
```csharp
builder.Services.AddResponseCaching();
...
app.UseResponseCaching();
```
e nel controller
```csharp
[HttpGet(ApiEndpoints.Movies.GetAll)]
[ResponseCache(Duration = 30, VaryByQueryKeys = new []{"title", "year", "sortBy", "page", "pageSize"}, VaryByHeader = "Accept, Accept-Encoding", Location = ResponseCacheLocation.Any)]
public async Task<IActionResult> GetAll(
    [FromQuery] GetAllMoviesRequest request, CancellationToken token)
{
    // ...
    return Ok(moviesResponse);
}
```
- **`Duration = 30`**: Il risultato viene memorizzato per **30 secondi**.
- **`VaryByQueryKeys`**: La cache è distinta in base ai valori delle query (`title`, `year`, ecc.).
- **`VaryByHeader`**: La cache cambia in base agli header `Accept` e `Accept-Encoding`.
- **`ResponseCacheLocation.Any`**: Indica che la cache può essere condivisa tra client e proxy intermediari.
### Server-Side Output Caching
L'**output caching** è una soluzione più sicura e flessibile, gestita interamente dal server.
```csharp
builder.Services.AddOutputCache(x =>
{
    x.AddBasePolicy(c => c.Cache());
    x.AddPolicy("MovieCache", c => 
        c.Cache()
        .Expire(TimeSpan.FromMinutes(1))
        .SetVaryByQuery(new[] { "title", "year", "sortBy", "page", "pageSize" })
        .Tag("movies"));
});
...
app.UseOutputCache();
```
e nel controller
```csharp
[HttpGet(ApiEndpoints.Movies.GetAll)]
[OutputCache(PolicyName = "MovieCache")]
public async Task<IActionResult> GetAll(
    [FromQuery] GetAllMoviesRequest request, CancellationToken token)
{
    // ...
    return Ok(moviesResponse);
}
```
**Spiegazione**:
- **`Expire(TimeSpan.FromMinutes(1))`**: La cache scade dopo **1 minuto**.
- **`SetVaryByQuery`**: La cache varia in base ai parametri della query (`title`, `year`, ecc.).
- **`Tag("movies")`**: Assegna un tag per permettere invalidazioni mirate.
Per esempio posso invalidare la cache dell'API che fornisce la lista dei film quando viene aggiunto/modificato/eliminato un film, in tramite il metodo `EvictByTagAsync` della classe `IOutputCacheStore` in questo modo:
```csharp
[ApiController]
public class MoviesController : ControllerBase
{
    private readonly IMovieService _movieService;
    private readonly IOutputCacheStore _outputCacheStore;

    public MoviesController(IMovieService movieService, IOutputCacheStore outputCacheStore)
    {
        _movieService = movieService;
        _outputCacheStore = outputCacheStore;
    }
    //...
}

[Authorize(AuthConstants.TrustedMemberPolicyName)]
[HttpPost(ApiEndpoints.Movies.Create)]
public async Task<IActionResult> Create([FromBody]CreateMovieRequest request,
    CancellationToken token)
{
    var movie = request.MapToMovie();
    await _movieService.CreateAsync(movie, token);
    await _outputCacheStore.EvictByTagAsync("movies", token);
    var movieResponse = movie.MapToResponse();
    return CreatedAtAction(nameof(GetV1), new { idOrSlug = movie.Id }, movieResponse);
}
```

## Tips & Tricks
### ApiEndpoints
Non è il massimo avere delle stringhe che identificano le varie API che voglio creare nei vari controller, in quanto non sono aggregate in un unico punto e scomode.
Invece ha molto senso creare una classe statica `ApiEndpoints` (sempre nel progetto `Api`) con all'interno delle sottoclassi sempre statiche una per ogni controller che forniscono le stringhe per le API. Esempio di implementazione:
```csharp
public static class ApiEndpoints  
{  
    private const string ApiBase = "api";  
    public static class Movies  
    {  
        private const string Base = $"{ApiBase}/movies";  
  
        public const string Create = Base;  
        public const string Get = $"{Base}/{{id:guid}}";  
        public const string GetAll = Base;  
        public const string Update = $"{Base}/{{id:guid}}";  
        public const string Delete = $"{Base}/{{id:guid}}";  
    }
}
```
### Non usare PATCH
Il partial update non viene usato in quanto macchinoso: tipicamente il client richiede un oggetto, lo modifica a piacere e poi utilizza l'update totale con `PUT`.

### Connettersi ad un db vero
Tipicamente si registra la factory della connection al DBMS che mi interessa come Singleton nella DI come nell'esempio sotto.
```csharp
services.AddSingleton<IDbConnectionFactory>(_ => new NpgsqlConnectionFactory(connectionString));

public interface IDbConnectionFactory
{
    Task<IDbConnection> CreateConnectionAsync(CancellationToken token = default);
}

public class NpgsqlConnectionFactory : IDbConnectionFactory
{
    private readonly string _connectionString;

    public NpgsqlConnectionFactory(string connectionString)
    {
        _connectionString = connectionString;
    }

    public async Task<IDbConnection> CreateConnectionAsync(CancellationToken token = default)
    {
        var connection = new NpgsqlConnection(_connectionString);
        await connection.OpenAsync(token);
        return connection;
    }
}
```
In seguito si implementa la classe `MovieRepository`
```csharp
public class MovieRepository : IMovieRepository
{
    private readonly IDbConnectionFactory _dbConnectionFactory;

    public MovieRepository(IDbConnectionFactory dbConnectionFactory)
    {
        _dbConnectionFactory = dbConnectionFactory;
    }

    public async Task<IEnumerable<Movie>> GetAllAsync(CancellationToken token = default)
    {
        using var connection = await _dbConnectionFactory.CreateConnectionAsync(token);
        var result = await connection.QueryAsync(new CommandDefinition("QUERY", token));
        
        // Conversione manuale dagli oggetti del db agli oggetti nel mio dominio, esempio Movie
        return result.Select(x => new Movie
        {
            Id = x.id,
            Title = x.title,
            YearOfRelease = x.yearofrelease,
            Genres = Enumerable.ToList(x.genres.Split(','))
        });
    }
}
```