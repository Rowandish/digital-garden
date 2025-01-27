#Dometrain 

## Introduzione

Un potente meccanismo per separare la costruzione degli oggetti dal loro uso è la *Dependency Injection (DI)*: l'idea è che un oggetto non dovrebbe mai assumersi la responsabilità dell'istanziazione delle sue dipendenze, al contrario dovrebbe passare questa responsabilità ad un meccanismo più "autorevole", [[Principi SOLID. Dependency Inversion Principle|invertendo pertanto il controllo]].
Usando la DI una classe non intraprende alcun passo diretto per risolvere le sue dipendenze (non chiama per esempio metodi come `BuildObject` per intenderci) ma è completamente passiva: mette a disposizione dei parametri a costruttore o dei metodi `Setter` e assume che questi parametri vengano popolati dal DI Framework nel modo corretto.
Un nome alternativo ma che significa la stessa cosa è "Inversion of Control Container" o "IoC Container".

### Separazione di Main
Un modo per separare la costruzione dell'architettura dal suo utilizzo consiste semplicemente di trasferire tutti gli aspetti della costruzione degli oggetti in `main` o in moduli richiamati da `main` e nel progettare il resto del sistema supponendo che tutti gli oggetti siano già stati costruiti e collegati tra di loro in modo appropriato.
L'obiettivo è che la funzione `main` costruisce gli oggetti necessari per il sistema  e poi li passa all'applicazione che li utilizza.
In questo modo l'applicazione non ha alcuna conoscenza del `main` o del processo di costruzione degli oggetti.
![[photo_2024-01-29_16-52-19.jpg]]
Ovviamente non tutti gli oggetti possono essere creati subito, in questo caso posso utilizzare il pattern [[Pattern Factory#^458139|Abstract Factory]]  per dare all'applicazione il controllo sul momento in cui costruire gli oggetti che gli servono ma mantenendo tutti i dettagli di tale costruzione separati rispetto al codice dell'applicazione.
![[photo_2024-01-29_16-52-20.jpg]]

## .NET
In .NET esiste il pacchetto nuget ufficiale `Microsoft.Extensions.DependencyInjection` che permette di iniettare automaticamente le dipendenze necessarie alle classi.
Il suo funzionamento base è il seguente:
```csharp
public class Application  
{  
    public Application(IWeatherService weatherService){} 
}

var services = new ServiceCollection();  
  
services.AddSingleton<IWeatherService, OpenWeatherService>();  
  
var serviceProvider = services.BuildServiceProvider();  
  
var application = serviceProvider.GetRequiredService<Application>();
```
Viene creata una `ServiceCollection` che è letteralmente una lista di istruzioni (in particolare `List<ServiceDescriptor>`) che indicano come devono essere risolte le dipendenze dal DI Framework con il suo lifetime (`Transient`, `Scoped`, `Singleton`) e su di essa viene costruito un `ServiceProvider` che, come dice il nome, è un servizio che fornisce le dipendenze a chi le richiede.
La `ServiceCollection` è come un libro di ricette mentre il `ServiceProvider` è il cuoco che le mette insieme per creare la ricetta.

Utilizzando poi i metodi di `ServiceProvider` posso ottenere l'istanza della classe che voglio, nell'esempio sopra `Application`. Se questa ultima ha delle dipendenze a costruttore queste vengono automaticamente iniettate dal DI Framework risolvendole: nell'esempio sopra `Application` ha come dipendenza un `IWeatherService` che risolve in un `OpenWeatherService`: verrà automaticamente iniettato questo ultimo.

### ServiceCollection

#### Lifetime

Ho tre tipologie di `lifetime` degli oggetti che posso creare:
* **Transient**: Ogni volta che richiedo una dipendenza verrà creata una nuova istanza della classe. Tipicamente più sicuro a livello di thread-safety ma più lento di singleton.
* **Singleton**: Una sola istanza in tutta l'applicazione, verrà istanziata la prima volta che serve e poi tale istanza verrà riutilizzata in tutta l'applicazione. Va bene per classi *stateless*. E' l'approccio più veloce ma bisogna stare attenti alla thread safety.
* **Scoped**: l'oggetto rimane sempre lo stesso all'interno dello stesso **scope** il quale può essere definito a mano in caso di una applicazione standalone mentre nel caso di ASP.NET questo è per definizione *dall'inizio alla fine di una richiesta*.

##### Custom Scope
Se sono in una Console Application e voglio creare uno scope custom posso scrivere come segue:
```csharp
var serviceScopeFactory = serviceProvider.GetRequiredService<IServiceScopeFactory>();  
  
using (var serviceScope = serviceScopeFactory.CreateScope())  
{  
    var exampleService1 = serviceScope.ServiceProvider.GetRequiredService<ExampleService>();  
    Console.WriteLine(exampleService1.Id);  
}
```

#### Sintassi

La sintassi `builder.Services.AddTransient|Singleton|Scoped<IService, ConcreteService>();` funziona se tutto l'albero delle dipendenze dei costruttori di `ConcreteService` può essere risolto dalla DI: per esempio se `ConcreteService` dipende da `IHttpClientFactory` significa che deve essere esplicitato come risolvere tale interfaccia nella `ServiceCollection` e così a ritroso ad albero per tutte le dipendenze.
Una sintassi alternativa è `builder.Services.AddTransient<IWeatherService>(provider => new OpenWeatherService(Not_DI_Class));` da utilizzare quando voglio esplicitare io come costruire un oggetto senza delegarlo alla DI: in questo modo non serve che tutte le sue dipendenze siano definite nella DI in quanto le espliciterò nella lambda factory. 

La sintassi da utilizzare è inoltre sempre quella "automatica" (vedi esempio sotto); la sintassi "manuale" è il suo analogo ma fatto a mano dal programmatore, cosa che difficilmente si fa a meno di casi particolari.
Lo scopo dell'esempio sotto è dimostrare un minimo cosa viene fatto dietro le quinte quando viene chiamato un metodo della `ServiceCollection`.

```csharp
// sintassi automatica
builder.Services.AddTransient<IWeatherService, OpenWeatherService>();
// sintassi manuale
builder.Services.AddTransient<IWeatherService>(provider =>
    new OpenWeatherService(provider.GetRequiredService<IHttpClientFactory>()));

// sintassi automatica
builder.Services.AddScoped<LifetimeIndicatorFilter>();
// sintassi manuale
builder.Services.AddScoped(provider =>
{
    // Costruisco con la DI le dipendenze che servono alla classe LifetimeIndicatorFilter
    var idGenerator = provider.GetRequiredService<IdGenerator>();
    var logger = provider.GetRequiredService<ILogger<LifetimeIndicatorFilter>>();

    return new LifetimeIndicatorFilter(idGenerator, logger);
});

```

### ServiceDescriptor
Ogni elemento all'interno di una `ServiceCollection` è un `ServiceDescriptor` che, come dice il nome, è una classe che descrive come un servizio deve essere istanziato.
In particolare quando scrivo, per esempio
```csharp
builder.Services.AddTransient<IWeatherService, OpenWeatherService>();
```
Sto creando un `ServiceDescriptor` così:
```csharp
var openWeatherServiceDescriptor =  
    new ServiceDescriptor(typeof(IWeatherService), typeof(OpenWeatherService), ServiceLifetime.Transient);
builder.Services.Add(openWeatherServiceDescriptor);
```
Questo strumento più a basso livello permette di customizzare l'IoC Container con cose custom fighe come `Interceptors`, `Decorators` e così via.

## Note
### Devo rendere tutto interfaccia?
Anche se uno un DI Framework ciò non significa che devo convertire ogni cosa in una interfaccia: tutti gli oggetti che non possono essere sostituiti *by definition* devono rimanere classi classiche.
Anche se tecnicamente potrei iniettarle tramite interfacce a costruttore questo non ha senso.

## Tips & Tricks

### Testare `ILogger`
L'interfaccia `ILogger` di .NET (vedi [[Logging in .NET]]) è piena di extension methods ed estremamente difficile da testare.
Un trucco è creare una classe Adapter che faccia da proxy alle chiamate al log: tale classe può essere quindi iniettata e testata.
Esempio con solo il metodo `LogInformation`:
```csharp
public interface ILoggerAdapter<TType>  
{  
    void LogInformation(string template, params object[] args);  
}

public class LoggerAdapter<TType> : ILoggerAdapter<TType>  
{  
    private readonly ILogger<LoggerAdapter<TType>> _logger;  
  
    public LoggerAdapter(ILogger<LoggerAdapter<TType>> logger)  
    {        _logger = logger;  
    }  
    public void LogInformation(string template, params object[] args)  
    {        _logger.LogInformation(template, args);  
    }
}
```

### Registrare Open Generics
Dato che non è possibile utilizzare gli Open Generic nei tipi per limiti del linguaggio C# posso utilizzare la seguente sintassi sfruttando il `typeof`.
```csharp
builder.Services.AddTransient(typeof(ILoggerAdapter<>), typeof(LoggerAdapter<>));
```
Il codice sopra indica che tutte le volte che richiedo un'interfaccia di tipo `ILoggerAdapter`, indipendentemente dal suo tipo `<T>` deve essere istanziato un `new LoggerAdapter<T>`.

### Registrare più implementazioni
Se dichiaro più implementazioni della stessa interfaccia **la seconda non sovrascrive la prima** ma, se a costruttore ho `IWeatherService` fornirò sempre la seconda dichiarata (come se fosse sovrascritta), mentre se ho `IEnumerable<IWeatherService>` verranno fornire entrambe.
```csharp
services.AddTransient<IWeatherService, OpenWeatherService>();  
services.AddTransient<IWeatherService, InMemoryWeatherService>();
```
Se invece voglio che, se una interfaccia era già definita non aggiungerne una nuova devo usare il metodo `TryAdd` invece di `Add`.
Quindi se scrivo
```csharp
services.TryAddTransient<IWeatherService, OpenWeatherService>();  
services.TryAddTransient<IWeatherService, InMemoryWeatherService>();
```
Verrà aggiunto solo `OpenWeatherService`.
### Raggruppare le definizioni in extension
Per evitare di avere il `Main` con mille righe di definizioni di dipendenze (`AddSingleton`, `AddSingleton`, `AddTransient`…) è buona norma raggruppare tutte le istruzioni che riguardano lo stesso metodo in un unico `extension method` con nome `AddXXX`.
Per esempio posso creare questa extension:
```csharp
public static IServiceCollection AddEndpointsApiExplorer(this IServiceCollection services)
{
    services.TryAddSingleton<IActionDescriptorCollectionProvider, DefaultActionDescriptorCollectionProvider>();
    services.TryAddSingleton<IApiDescriptionGroupCollectionProvider, ApiDescriptionGroupCollectionProvider>();
    return services;
}
```
che poi verrà chiamata dall'esterno in questo modo:
```csharp
services.AddEndpointsApiExplorer();
```
Inoltre è buona norma (sopratutto per chi fornisce librerie come pacchetti nuget) modificare il namespace di tale classe con
```csharp
// ReSharper disable once CheckNamespace  
namespace Microsoft.Extensions.DependencyInjection;
```
in modo tale che dall'esterno non debbia aggiungere uno `using` dedicato a tale extension.