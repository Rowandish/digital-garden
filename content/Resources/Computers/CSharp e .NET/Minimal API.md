---
tags:
  - Dometrain
---
Le **Minimal APIs** in ASP.NET rappresentano un approccio più leggero e semplificato per creare API REST rispetto al tradizionale [[REST APIs in .NET|ASP.NET Web API]].
Introdotte con **ASP.NET Core 6**, le Minimal APIs eliminano molte delle configurazioni e del codice boilerplate richiesto dalle API tradizionali, offrendo un modo più conciso e diretto per definire gli endpoint.
Microsoft non ha intenzione di deprecare la modalità tradizionale con in controller in quanto esistono degli scenari complessi dove può ancora funzionare bene ma l'idea è poter fare il 90% delle API possibili in modalità minimal.
## Differenze tra Minimal API e API tradizionali

|**Caratteristica**|**Minimal API**|**API tradizionali**|
|---|---|---|
|**Struttura del codice**|Più semplice e concisa|Più strutturata e verbosa|
|**Controller**|Non richiede controller|Usa controller e action|
|**Configurazione**|Minima, senza bisogno di attributi `[Route]` o `[HttpGet]`|Necessita di configurazioni più dettagliate|
|**Performance**|Più veloce, meno overhead|Leggermente più pesante per via del framework MVC|
|**Middleware**|Definito direttamente in `Program.cs`|Basato su un'architettura con più classi e dipendenze|
## Esempio
```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello, Minimal API!");

app.MapGet("/users", () =>
{
    return new List<string> { "Alice", "Bob", "Charlie" };
});

app.Run();
```
- Non usa **controller** né **action**.
- Gli endpoint sono definiti direttamente nella pipeline dell'applicazione.
- Utilizza `app.MapGet()` per definire i metodi HTTP senza bisogno di `[HttpGet]`.
- Il codice è più compatto e leggibile.

## DI Service Registration

La registrazione dei servizi per la [[Dependency Injection Framework|DI]] avviene prima della creazione dell’app con `builder.Build()`, cioè **tra `CreateBuilder` e `Build()`**.
```csharp
var builder = WebApplication.CreateBuilder(args);

// 👉 Service registration qui
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddSingleton<GuidGenerator>();
builder.Services.AddSingleton<PeopleService>();
// 👈 Fine service registration

var app = builder.Build();
```

## Middleware

### Registration
La **registrazione dei middleware** avviene **dopo `builder.Build()`**, quindi **sul risultato di `var app = builder.Build();`**.  
È il punto in cui si configura **il comportamento della pipeline HTTP**.
```csharp
var builder = WebApplication.CreateBuilder(args);
// Service registration
builder.Services.AddControllers();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// 👉 Middleware registration qui
app.UseSwagger();
app.UseSwaggerUI();

app.UseHttpsRedirection();
app.UseAuthorization();
// 👈 Fine middleware registration

// Routing
app.MapControllers();
```

## Parametri

### Passare parametri

I parametri possono essere passati ad un metodo in **5 modi diversi**, vediamoli tutti.
#### Route
I **route parameters** permettono di estrarre valori direttamente dall’URL. Ecco alcune possibilità:

1. **Tipizzazione**:  
    `"{age:int}"` → il parametro `age` deve essere un intero.  
    ➝ Viene automaticamente convertito in `int age` nel metodo handler.
2. **Espressione Regolare**:  
    `"{carId:regex(^[a-z0-9]+$)}"` → `carId` deve rispettare il pattern regex (solo lettere minuscole e numeri).  
    ➝ Se il valore non rispetta la regex, la route non viene attivata.
3. **Lunghezza Fissa**:  
    `"{isbn:length(13)}"` → `isbn` deve avere esattamente 13 caratteri.

#### Query string
I parametri possono essere passati tramite la **query string** dell’URL (es. `?query=123`).  
Per leggerli, si usa l’attributo `[FromQuery]`.  
```csharp
[FromQuery(Name = "query")] int queryParam
```

Il nome può essere specificato esplicitamente con `Name = "..."`, utile se diverso dal nome della variabile.
#### DI Container
È possibile ricevere oggetti o servizi direttamente dal **Dependency Injection container**, semplicemente dichiarandoli nei parametri del metodo.  
ASP.NET li inietta automaticamente se sono registrati nel container.
```csharp
GuidGenerator guidGenerator
```
Qui `GuidGenerator` è un servizio risolto tramite DI, senza bisogno di alcun attributo.
#### Header
È possibile leggere valori direttamente dagli **header HTTP** tramite `[FromHeader]`.  
Utile per accedere a metadati della richiesta.
```csharp
[FromHeader(Name = "Accept-Encoding")] string encoding
```
Il valore viene estratto dall’header `Accept-Encoding`.
#### Body (JSON)
È possibile ricevere oggetti complessi inviati nel **corpo della richiesta (body)**, ad esempio in formato JSON.  
Si usa l’attributo `[FromBody]`, anche se è implicito per i tipi complessi.
```csharp
app.MapPost("/create", ([FromBody] Product product) =>
{
    return $"Received product: {product.Name}";
});
```
Se il tipo `Product` è una classe con proprietà come `Name`, `Price`, ecc., queste verranno automaticamente deserializzate dal JSON nel body della richiesta.

### Parametri speciali
ASP.NET Minimal API permette anche di accedere a **oggetti speciali del framework**, che forniscono informazioni avanzate sulla richiesta o sul contesto di esecuzione. Questi parametri vengono riconosciuti automaticamente dal runtime, senza bisogno di attributi.
#### HttpContext
Fornisce accesso completo a tutti gli elementi della richiesta e della risposta HTTP.
```csharp
app.MapGet("httpcontext", (HttpContext context) =>
{
    return Results.Ok($"Request path: {context.Request.Path}");
});
```
#### HttpRequest / HttpResponse
È possibile accedere direttamente solo alla richiesta o alla risposta.
```csharp
app.MapGet("http", (HttpRequest request, HttpResponse response) =>
{
    var queries = request.QueryString.Value;
    return response.WriteAsync($"Query string: {queries}");
});
```

#### ClaimsPrincipal (utente corrente)
Permette di accedere all’utente autenticato e ai suoi claim.
```csharp
app.MapGet("claims", (ClaimsPrincipal user) =>
{
    var name = user.Identity?.Name;
    return Results.Ok($"User: {name}");
});
```

#### CancellationToken
Consente di gestire l’annullamento della richiesta, ad esempio se il client chiude la connessione.
```csharp
app.MapGet("cancel", (CancellationToken token) =>
{
    // Può essere usato per interrompere operazioni lunghe
    return Results.Ok("CancellationToken received");
});
```

### Custom parameter binding
È un meccanismo che consente di **personalizzare il modo in cui Minimal API converte i dati della richiesta** (route, query, body, ecc.) in oggetti da passare come parametri all’handler.
Per esempio voglio passare un `MapPoint` in un metodo `POST`
```csharp
public class MapPoint
{
    public double Latitude { get; set; }
    public double Longitude { get; set; }
    
    public static bool TryParse(string? value, out MapPoint? point) { ... }

    public static async ValueTask<MapPoint?> BindAsync(HttpContext context, ParameterInfo parameterInfo) { ... }
}

//...

app.MapPost("/map", (MapPoint point) =>
{
    return Results.Ok($"Lat: {point.Latitude}, Lng: {point.Longitude}");
});
```

ASP.NET cerca automaticamente uno dei seguenti metodi statici:
1. `public static bool TryParse(string, out T)`
2. `public static ValueTask<T?> BindAsync(HttpContext, ParameterInfo)`
#### 1. TryParse → binding da route o query string
```csharp
public static bool TryParse(string? value, out MapPoint? point)
```
- Permette il binding da **route** o **query** quando il parametro arriva come stringa (`lat,lng`).
- Il framework usa `TryParse()` per convertire il valore in un oggetto `MapPoint`.
- **Esempio URL:** `/location/45.0,9.0` 
- ASP.NET userà `MapPoint.TryParse("45.0,9.0", out var point)`.
#### 2. BindAsync → binding personalizzato da body o contesto
```csharp
public static async ValueTask<MapPoint?> BindAsync(HttpContext context, ParameterInfo parameterInfo)
```
- Viene usato se il framework **non trova un `TryParse` adatto** oppure se il tipo è passato tramite **body**, **header**, o da **altre fonti personalizzate**.
- In questo esempio, legge il body della richiesta (es. `"45.0,9.0"`) e lo trasforma in un `MapPoint`.
- **Esempio body HTTP:** `45.0,9.0` 
- ASP.NET chiamerà `MapPoint.BindAsync(...)`.

## Swagger
Swagger permette di avere una visualizzazione carina delle API nel browser.
E' possibile aggiungere delle extension alle API in modo da migliorare l'output di Swagger, vediamo quali.
### `Accepts<T>()`
```csharp
.Accepts<Book>("application/json")
```
- Specifica **il tipo di contenuto accettato dal client** (nel body della richiesta).
- Serve principalmente a generare **documentazione Swagger/OpenAPI corretta**.
- In questo caso, Swagger capisce che il client deve inviare un oggetto `Book` nel formato `application/json`.
### `Produces<T>(statusCode)`
```csharp
.Produces<Book>(201)
.Produces<IEnumerable<ValidationFailure>>(400)
```
- Indica **i possibili tipi di risposta e i relativi codici HTTP** restituiti dall’endpoint.
- Anche queste estensioni sono usate **solo per Swagger/OpenAPI**, non influenzano l’esecuzione dell’API.
- Aiutano a documentare in modo esplicito:
    - **Che tipo di oggetto verrà restituito**
    - **Con quale codice di stato**
### Riassunto

| Estensione                     | Scopo                                                                                       | Esempio                              |
| ------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------ |
| `.Accepts<T>(mediaType)`       | Specifica il tipo accettato nel body della richiesta e il media type (es. application/json) | `.Accepts<Book>("application/json")` |
| `.Produces<T>(statusCode)`     | Documenta il tipo restituito nella risposta insieme al codice HTTP                          | `.Produces<Book>(201)`               |
| `.Produces(statusCode)`        | Documenta solo il codice di stato restituito, senza specificare il tipo                     | `.Produces(204)`                     |
| `.ProducesProblem(statusCode)` | Documenta che l’endpoint può restituire una ProblemDetails (errori standard RFC 7807)       | `.ProducesProblem(400)`              |
| `.WithName(name)`              | Assegna un nome all’endpoint per routing e Swagger                                          | `.WithName("CreateBook")`            |
| `.WithTags(tags)`              | Raggruppa l’endpoint sotto uno o più tag nella documentazione Swagger                       | `.WithTags("Books")`                 |
| `.ExcludeFromDescription()`    | Esclude l’endpoint dalla documentazione Swagger/OpenAPI                                     | `.ExcludeFromDescription()`          |
## CORS
**CORS (Cross-Origin Resource Sharing)** è un meccanismo di sicurezza dei browser che **regola le richieste HTTP tra origini diverse** (es. un frontend su `http://localhost:3000` che chiama un'API su `http://localhost:5000`).
**Di default**, i browser **bloccano queste richieste cross-origin**, a meno che il server non consenta esplicitamente l’accesso.
### Come abilitare CORS in Minimal API

#### 1. Registrazione della policy CORS nei servizi
Nel `Program.cs`, nella parte di **service registration**:
```csharp
builder.Services.AddCors(options =>
{
    options.AddPolicy("AnyOrigin", policy =>
        policy.AllowAnyOrigin() // Consente tutte le origini
              .AllowAnyHeader()
              .AllowAnyMethod());
});
```
#### 2. Abilitare CORS nella pipeline middleware
Nel **blocco middleware**, dopo `app.Build()`:
```csharp
app.UseCors(); // usa la policy di default
```
Oppure per **usare una policy specifica**:
```csharp
app.UseCors("AnyOrigin");
```
#### 3. Associare CORS ad un singolo endpoint (opzionale)
Se vuoi **applicare CORS solo a certe API**, puoi farlo direttamente nell’endpoint:
```csharp
app.MapGet("status", [EnableCors("AnyOrigin")] () =>
{
    return Results.Ok("Status ok");
});
```
Oppure:
```csharp
app.MapPost("books", (...) => { ... })
   .RequireCors("AnyOrigin");
```

## Struttura file
In un'app Minimal API, è facile che il file `Program.cs` diventi troppo lungo e disordinato.  
Per risolvere questo problema, puoi **organizzare gli endpoint in classi dedicate**, grazie a un approccio modulare basato su:
- un'interfaccia comune (`IEndpoints`)
- una classe per ogni gruppo di endpoint (es. `LibraryEndpoints`)
- due metodi di estensione: `AddEndpoints` e `UseEndpoints`
### 1. Interfaccia `IEndpoints`
Definisce un contratto standard per ogni classe di endpoint:
```csharp
public interface IEndpoints
{
    static abstract void DefineEndpoints(IEndpointRouteBuilder app);
    static abstract void AddServices(IServiceCollection services, IConfiguration configuration);
}
```
- `DefineEndpoints` → mappa le API.
- `AddServices` → registra i servizi usati dagli endpoint (es. `IBookService`).
### 2. Implementazione in `LibraryEndpoints`
Qui vengono definiti gli endpoint e i servizi specifici della libreria:
```csharp
public class LibraryEndpoints : IEndpoints
{
    public static void DefineEndpoints(IEndpointRouteBuilder app) { ... }
    public static void AddServices(IServiceCollection services, IConfiguration configuration) { ... }
}
```
- Tutte le API (`GET`, `POST`, `PUT`, `DELETE`) sono mappate in `DefineEndpoints`.
- I servizi richiesti (es. `IBookService`) sono registrati in `AddServices`.

#### Esempio completo
```csharp
public class LibraryEndpoints : IEndpoints
{
    private const string ContentType = "application/json";
    private const string Tag = "Books";
    private const string BaseRoute = "books";

    public static void DefineEndpoints(IEndpointRouteBuilder app)
    {
        app.MapPost(BaseRoute, CreateBookAsync)
            .WithName("CreateBook")
            .Accepts<Book>(ContentType)
            .Produces<Book>(201).Produces<IEnumerable<ValidationFailure>>(400)
            .WithTags(Tag);

        app.MapGet(BaseRoute, GetAllBooksAsync)
            .WithName("GetBooks")
            .Produces<IEnumerable<Book>>(200)
            .WithTags(Tag);

        app.MapGet($"{BaseRoute}/{{isbn}}", GetBookByIsbnAsync)
            .WithName("GetBook")
            .Produces<Book>(200).Produces(404)
            .WithTags(Tag);

        app.MapPut($"{BaseRoute}/{{isbn}}", UpdateBookAsync)
            .WithName("UpdateBook")
            .Accepts<Book>(ContentType)
            .Produces<Book>(200).Produces<IEnumerable<ValidationFailure>>(400)
            .WithTags(Tag);

        app.MapDelete($"{BaseRoute}/{{isbn}}", DeleteBookAsync)
            .WithName("DeleteBook")
            .Produces(204).Produces(404)
            .WithTags(Tag);
    }

    internal static async Task<IResult> CreateBookAsync(
        Book book, IBookService bookService, IValidator<Book> validator)
    {
        var validationResult = await validator.ValidateAsync(book);
        if (!validationResult.IsValid)
        {
            return Results.BadRequest(validationResult.Errors);
        }

        var created = await bookService.CreateAsync(book);
        if (!created)
        {
            return Results.BadRequest(new List<ValidationFailure>
            {
                new("Isbn", "A book with this ISBN-13 already exists")
            });
        }

        return Results.Created($"/{BaseRoute}/{book.Isbn}", book);
    }

    internal static async Task<IResult> GetAllBooksAsync(
        IBookService bookService, string? searchTerm)
    {
        if (searchTerm is not null && !string.IsNullOrWhiteSpace(searchTerm))
        {
            var matchedBooks = await bookService.SearchByTitleAsync(searchTerm);
            return Results.Ok(matchedBooks);
        }

        var books = await bookService.GetAllAsync();
        return Results.Ok(books);
    }

    internal static async Task<IResult> GetBookByIsbnAsync(
        string isbn, IBookService bookService)
    {
        var book = await bookService.GetByIsbnAsync(isbn);
        return book is not null ? Results.Ok(book) : Results.NotFound();
    }

    internal static async Task<IResult> UpdateBookAsync(
        string isbn, Book book, IBookService bookService,
        IValidator<Book> validator)
    {
        book.Isbn = isbn;
        var validationResult = await validator.ValidateAsync(book);
        if (!validationResult.IsValid)
        {
            return Results.BadRequest(validationResult.Errors);
        }

        var updated = await bookService.UpdateAsync(book);
        return updated ? Results.Ok(book) : Results.NotFound();
    }

    internal static async Task<IResult> DeleteBookAsync(
        string isbn, IBookService bookService)
    {
        var deleted = await bookService.DeleteAsync(isbn);
        return deleted ? Results.NoContent() : Results.NotFound();
    }

    public static void AddServices(IServiceCollection services, IConfiguration configuration)
    {
        services.AddSingleton<IBookService, BookService>();
    }
}
```
### 3. Estensioni `AddEndpoints` e `UseEndpoints`
Queste extension methods permettono di **richiamare automaticamente tutti gli endpoint registrati** nel progetto:
```csharp
builder.Services.AddEndpoints<Program>(builder.Configuration); // Service registration
app.UseEndpoints<Program>(); // Endpoint registration
```
- Usa `typeof(TMarker)` per cercare automaticamente tutte le classi che implementano `IEndpoints` nell'assembly.
- Esegue internamente i metodi `AddServices` e `DefineEndpoints` di ciascuna classe.


