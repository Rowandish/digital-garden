---
tags:
  - CSharp
  - DotNET
---
L'interfaccia `ILogger` è il cuore del sistema di logging in .NET ed essa fornisce i metodi fondamentali per registrare i messaggi di log.

## Creazione del logger

### Console Application

Le applicazioni console di solito configurano il logging in `Program.cs` usando `LoggerFactory`. La configurazione è semplice e diretta:

```csharp
using var loggerFactory = LoggerFactory.Create(builder =>
{
    builder.SetMinimumLevel(LogLevel.Information).AddConsole();  
});

var logger = loggerFactory.CreateLogger<Program>();
logger.LogInformation("Console application started");
```

### Web Application
In questo caso il logger viene creato nel builder

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Logging...
```


## Il messaggio di log

Quando si logga un messaggio in .NET utilizzando l'interfaccia `ILogger`, il messaggio di log contiene diversi componenti chiave che forniscono informazioni contestuali e dettagliate. Ecco una descrizione approfondita di ciascuno di questi componenti:

### 1. Category

La categoria è un identificatore associato a un logger specifico e **tipicamente rappresenta il nome completo (incluso il namespace) della classe o del componente che genera il log**.
La categoria aiuta a organizzare i log in base alle aree funzionali dell'applicazione e consente di filtrare i messaggi di log per categoria.
Come category del log è convenzione usare la classe che sta utilizzando il log. Nelle minimal Api o WebApi quello che è automaticamente registrato nella DI nelle API è sempre `Ilogger<NomeClasse>` mentre invece la classe pura `ILogger` non viene registrata.

```csharp
public class MyService
{
    public MyService(ILogger<MyService> logger)
    {
    }
}
```

In questo esempio, la categoria sarà `MyService`.

### 2. Event ID

L'`EventId` è una struttura opzionale che rappresenta un identificatore univoco per un evento di log specifico.
Consente di associare i log a eventi specifici, facilitando la ricerca e il tracciamento di particolari occorrenze all'interno del sistema.
Può includere un numero intero e una stringa descrittiva:

```csharp
var eventId = new EventId(1001, "WorkStarted");
_logger.LogInformation(eventId, "Doing work");
// OR
_logger.LogInformation(1001, "Doing work");
```

### 3. Severity (LogLevel)

Il `LogLevel` indica la gravità del messaggio di log. I livelli di log predefiniti in .NET sono:

- `Trace`: Dettagli molto dettagliati. Utilizzato per diagnosticare problemi specifici.
- `Debug`: Informazioni dettagliate utili per il debugging. Non viene normalmente abilitato in ambienti di produzione.
- `Information`: Informazioni generali sul flusso dell'applicazione. Utilizzato per tracciare l'esecuzione di operazioni regolari.
- `Warning`: Indicazioni di potenziali problemi o situazioni inaspettate che non interrompono il flusso dell'applicazione.
- `Error`: Errori che impediscono il completamento di una specifica operazione.
- `Critical`: Errori critici che richiedono un'attenzione immediata. Indicano problemi che potrebbero causare l'interruzione dell'applicazione.

### 4. Message

Il `Message` è la stringa di testo che descrive l'evento di log. Questo messaggio può includere informazioni dinamiche formattate tramite parametri:

```csharp
public void DoWork(string taskName)
{
    _logger.LogInformation("Starting task {TaskName}", taskName);
}
```

Se voglio formattare le stringhe le formattazioni vanno nei parametri del template 
```csharp
logger.logInformation("{Name:S} just turned: {Age:d}", Name, Age)
```

Attenzione che quando voglio passare dei parametri ai log **non devo usare la string interpolation o lo string format** altrimenti perdo l'informazione sui parametri che passo.
Per esempio fare questo è sbagliato in quanto perdo l'informazione sulla variabile "30" che ho passato:
```csharp
var name = "Nick"
var age = 30;
logger.logInformation($"{name} just turned: {age}")
```
L'idea è che non voglio scrivere solo stringhe semplici ma stringhe con metadati, per esempio nel caso sopra voglio sia la stringa che il valore di "30" in modo che possa poi farci delle query o similari.
Il modo corretto è
```csharp
var name = "Nick"
var age = 30;
logger.logInformation("{Name} just turned: {Age}", name, age)
```
Notare che la stringa `{Name}` non è necessario che si chiami come la variabile, quello che conta è l'ordine.
Questo concetto è utilissimo non nel `ConsoleProvider` ma in altri provider più complessi, come il json.


### 5. Exception

L'`Exception` è un oggetto opzionale che rappresenta un'eccezione associata al messaggio di log. Viene utilizzato per registrare informazioni dettagliate sugli errori che si verificano nell'applicazione:

```csharp
try
{
    // Simulate work
}
catch (Exception ex)
{
    _logger.LogError(ex, "An error occurred while doing work");
}
```

### 6. Log Scope

Il `Log Scope` è una funzionalità opzionale che consente di creare contesti di log.
Non tutti i provider supportano gli scope, per esempio la Console non li supporta mentre li supporta la `JsonConsole`.
Gli scope possono essere utilizzati per correlare i messaggi di log che appartengono alla stessa operazione o transazione:
```csharp
using (_logger.BeginScope("TransactionId: {TransactionId}", transactionId))
{
	// Ogni log qui dentro avrà specificato la transaction id
    _logger.LogInformation("Starting transaction");
    // Perform transaction
    _logger.LogInformation("Transaction completed");
}
```
Mentre la categoria identifica la classe nel suo complesso, lo scope indica delle operazioni o dei metodi all'interno della stessa categoria.
### Esempio completo

Combiniamo tutti questi componenti in un esempio completo:

```csharp
public class MyService
{
    private readonly ILogger<MyService> _logger;

    public MyService(ILogger<MyService> logger)
    {
        _logger = logger;
    }

    public void DoWork(string taskName)
    {
        var eventId = new EventId(1001, "WorkStarted");

        using (_logger.BeginScope("TransactionId: {TransactionId}", Guid.NewGuid()))
        {
            _logger.LogInformation(eventId, "Starting task {TaskName}", taskName);

            try
            {
                // Simulate work
                _logger.LogDebug("Working on task {TaskName}", taskName);
                throw new InvalidOperationException("An error occurred during work");
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "An error occurred while doing task {TaskName}", taskName);
            }

            _logger.LogInformation("Task {TaskName} completed", taskName);
        }
    }
}
```





### Log su console

Per esempio un messaggio su console si struttura come segue:
```
info: Program[0]
      Messaggio! 
```
con `info` che è la gravità, `Program` indica la "category", `[0]` l' event id e `Messaggio!` il messaggio effettivo.

## Provider

I provider sono responsabili di determinare dove e come i messaggi di log vengono registrati. .NET offre diversi provider di logging built-in, tra cui:

- `ConsoleLoggerProvider`: logga i messaggi sulla console.
- `DebugLoggerProvider`: logga i messaggi nella finestra di debug.
- `EventSourceLoggerProvider`: logga i messaggi usando EventSource.
- `EventLogLoggerProvider`: logga i messaggi negli Event Logs di Windows.
- `FileLoggerProvider`: un provider custom comunemente utilizzato per loggare i messaggi su file.

### Configurazione di un Provider

La configurazione di un provider di logging in .NET è solitamente gestita nel file `Program.cs` o `Startup.cs`, a seconda del tipo di applicazione. Ecco un esempio per una console application:

```csharp
class Program
{
    static void Main(string[] args)
    {
        using var loggerFactory = LoggerFactory.Create(builder =>
        {
            builder
                .AddConsole()
                .AddDebug();
        });

        var logger = loggerFactory.CreateLogger<Program>();
        logger.LogInformation("Application started");

        // Application code here
    }
}
```

Per una web application, la configurazione avviene solitamente in `Startup.cs`:

```csharp
public class Startup
{
    public void Configure(IApplicationBuilder app, IWebHostEnvironment env, ILogger<Startup> logger)
    {
        if (env.IsDevelopment())
        {
            app.UseDeveloperExceptionPage();
        }
        else
        {
            app.UseExceptionHandler("/Home/Error");
            app.UseHsts();
        }

        app.UseHttpsRedirection();
        app.UseStaticFiles();

        app.UseRouting();

        app.UseAuthorization();

        app.UseEndpoints(endpoints =>
        {
            endpoints.MapControllerRoute(
                name: "default",
                pattern: "{controller=Home}/{action=Index}/{id?}");
        });

        logger.LogInformation("Application configured");
    }
}
```

### Creazione di un provider custom

Oltre ai provider built-in, è possibile creare provider custom per soddisfare esigenze specifiche.
Ecco un esempio di un provider custom che logga i messaggi su un file:
#### Implementazione di un Provider Custom

1. Creare la classe `FileLogger`:
```csharp
public class FileLogger : ILogger
{
    private readonly string _filePath;
    private static readonly object _lock = new object();

    public FileLogger(string filePath)
    {
        _filePath = filePath;
    }

    public IDisposable BeginScope<TState>(TState state) => null;

    public bool IsEnabled(LogLevel logLevel) => true;

    public void Log<TState>(LogLevel logLevel, EventId eventId, TState state, Exception exception, Func<TState, Exception, string> formatter)
    {
        if (!IsEnabled(logLevel))
        {
            return;
        }

        var message = formatter(state, exception);
        lock (_lock)
        {
            File.AppendAllText(_filePath, $"{logLevel}: {message}{Environment.NewLine}");
        }
    }
}
```

2. Creare la classe `FileLoggerProvider`:

```csharp
public class FileLoggerProvider : ILoggerProvider
{
    private readonly string _filePath;

    public FileLoggerProvider(string filePath)
    {
        _filePath = filePath;
    }

    public ILogger CreateLogger(string categoryName)
    {
        return new FileLogger(_filePath);
    }

    public void Dispose() { }
}
```

3. Configurare il provider custom:

```csharp
class Program
{
    static void Main(string[] args)
    {
        using var loggerFactory = LoggerFactory.Create(builder =>
        {
            builder.AddProvider(new FileLoggerProvider("log.txt"));
        });

        var logger = loggerFactory.CreateLogger<Program>();
        logger.LogInformation("Application started");

        // Application code here
    }
}
```


### Application Insights

#### Configurazione

Application Insights è una potente soluzione di monitoraggio di Microsoft Azure che permette di raccogliere e analizzare dati telemetrici dalle applicazioni.
Uno dei componenti configurabili di Application Insights è il canale di telemetria. `InMemoryChannel` è uno dei canali di telemetria che memorizza i dati in memoria prima di inviarli ad Application Insights, offrendo una soluzione efficace per gestire la telemetria in scenari con bassa latenza infatti è usato per le Console Application standalone.
Questo oggetto ha:
1. **Bassa Latenza**: Memorizza i dati in memoria, riducendo il tempo di attesa prima dell'invio.
2. **Configurabilità**: Permette di configurare dimensioni del buffer e intervalli di invio.
3. **Resilienza**: In caso di fallimento temporaneo della rete, i dati rimangono in memoria fino a quando non possono essere inviati.
L'esempio seguente scrive i messaggi di log ad `Application insights` in modo estremamente semplice a meno di incollare la connection string.
```csharp
using var channel = new InMemoryChannel();
try  
{  
    IServiceCollection services = new ServiceCollection();  
    services.Configure<TelemetryConfiguration>(x => x.TelemetryChannel = channel);  
    services.AddLogging(x =>  
    {  
        x.AddApplicationInsights(  
            configureTelemetryConfiguration: teleConfig =>  
                teleConfig.ConnectionString =  
                    "ADD HERE",  
            configureApplicationInsightsLoggerOptions: _ => { });  
    });  
    var serviceProvider = services.BuildServiceProvider();  
  
    var logger = serviceProvider.GetRequiredService<ILogger<Program>>();  
  
    logger.LogInformation("Hello from console!");  
  
}  
finally  
{  
    await channel.FlushAsync(default);  
    await Task.Delay(1000);  
}
```

#### Analisi dei dati telemetrici

Una volta configurato e avviato il logging, i dati telemetrici verranno inviati ad Application Insights.
Per filtrare i log si utilizza il linguaggio di query Kusto (KQL), esempio
```kql
traces
| where timestamp > ago(1h)
| summarize count() by resultCode
```
![[Pasted image 20240606121454.png]]
Puoi monitorare e analizzare questi dati nel portale di Azure.

1. **Dashboard di Overview**: Fornisce una panoramica delle richieste, delle dipendenze, delle eccezioni e delle metriche chiave.
2. **Live Metrics Stream**: Mostra le metriche in tempo reale per monitorare l'applicazione mentre è in esecuzione.
3. **Log Analytics**: 
4. **Metriche**: Analizza le metriche personalizzate inviate dall'applicazione.
5. **Analisi delle Eccezioni**: Fornisce dettagli approfonditi sulle eccezioni rilevate, inclusi stack trace e contesto dell'errore.


#### Monitoraggio
Potrebbe essere utile settare degli allarmi su determinate condizioni che deduco dai miei log, potenzialmente anche aggregando dati, facendo analisi sui percentili e così via.
Per fare questo devo usare un'altra risorsa di Azure chiamata `Monitor`.
Una volta collegata ad `Application Insights` devo creare una nuova `Alert Rule` e indicare la `Condition`, quindi quando voglio triggerare l'alert.
Posso prendere direttamente le eccezioni oppure delle query specifiche usando `Custom log search` dove posso indicare la query in linguaggio `KQL` di ricerca dei messaggi.
Una volta definita la logica posso utilizzare un `Action group` per notificare l'alert, per esempio via mail.

##### Esempio
Assumiamo che abbia un log che indica quanto ci ha messo una determinata operazione, per esempio
```csharp
using (_logger.BeginTimedOperation("Weather retrieval"))
{
    await Task.Delay(Random.Shared.Next(10, 100));
}
```
Questo codice scrive `Weather retrieval completed in {OperationDurationMs}ms`.
Ora voglio creare un alert se il tempo impiegato è maggiore di un k valore nel 95esimo percentile.
Per prima cosa devo scrivere la query KPL:
```
traces
| where customDimensions.MessageTemplate == "Weather retrieval completed in {OperationDurationMs}ms"
| order by timestamp
| summarize percentile(todouble(customDimensions.OperationDurationMs), 95)
```
che fornisce, per esempio, che il 95esimo percentile di `OperationDurationMs` è 229.
Ora inserisco la query in un alert `Custom log search` indicando nella `Alert logic` come operatore `Greater than or equal` e come threshold `300` che è il mio valore soglia.

## Pacchetti NuGet

In una console application devo esplicitare i pacchetti nuget come segue
```xml
<!-- Contiene solo le interfaccie, tipo ILogger -->  
<PackageReference Include="Microsoft.Extensions.Logging.Abstractions" Version="7.0.1" />  
<!-- Contiene le implementazioni delle astrazioni, per esempio LoggerFactory,  ma senza i provider -->  
<PackageReference Include="Microsoft.Extensions.Logging" Version="7.0.0" />  
<!-- Contiene il provider per scrivere su console -->  
<PackageReference Include="Microsoft.Extensions.Logging.Console" Version="7.0.0" />
```
Invece in una `WebApplication` le dipendenze dai log sono implicite e non bisogna specificarle nel csproject.


## Log Filters

I log filters sono meccanismi che permettono di controllare quali messaggi di log vengono emessi in base a criteri predefiniti.
Questi filtri possono essere configurati per livello di log, categoria, provider o una combinazione di questi.
I filtri di log in .NET sono configurati per ogni provider di log specifico e possono essere definiti tramite la configurazione dell'applicazione (ad esempio, `appsettings.json`) o tramite codice nel `Program.cs` o `Startup.cs`.
Essi determinano quali messaggi di log saranno registrati da ciascun provider, in base a:

- Livello di log (`LogLevel`)
- Categoria del logger (tipicamente il nome della classe o del namespace)
- Provider di log (Console, File, Debug, ecc.)

### Configurazione di Log Filters tramite `appsettings.json`

Un modo comune per configurare i filtri di log è tramite il file di configurazione `appsettings.json`. Ecco un esempio di configurazione:

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Warning",
      "Microsoft": "Information",
      "Microsoft.Hosting.Lifetime": "Information",
      "System": "Error"
    },
    "Console": {
      "LogLevel": {
        "Default": "Information",
        "Microsoft": "Warning"
      }
    },
    "Debug": {
      "LogLevel": {
        "Default": "Debug"
      }
    }
  }
}
```

In questo esempio:
- La configurazione generale (`Logging:LogLevel`) imposta il livello di log predefinito a `Warning`, il livello di log per `Microsoft` a `Information` e per `System` a `Error`.
- Il provider Console ha una configurazione specifica che imposta il livello di log predefinito a `Information` e per `Microsoft` a `Warning`.
- Il provider Debug è configurato per registrare i messaggi a partire dal livello `Debug`.

### Configurazione di Log Filters tramite codice

È possibile configurare i filtri di log anche tramite codice, utilizzando il metodo `AddFilter` sugli `ILoggerFactory` o `ILoggingBuilder`. Ecco un esempio per una console application:

```csharp
class Program
{
    static void Main(string[] args)
    {
        using var loggerFactory = LoggerFactory.Create(builder =>
        {
            builder
                .AddConsole()
                .AddDebug()
                .AddFilter("System", LogLevel.Error)
                .AddFilter<ConsoleLoggerProvider>("Microsoft", LogLevel.Warning)
                .AddFilter<DebugLoggerProvider>("Default", LogLevel.Debug);
        });
    }
}
```

In questo esempio:
- Viene aggiunto il provider Console e Debug.
- Un filtro generale per la categoria `System` è impostato a `Error`.
- Un filtro specifico per il provider Console per la categoria `Microsoft` è impostato a `Warning`.
- Un filtro specifico per il provider Debug per la categoria `Default` è impostato a `Debug`.











## High Performance Logging
Dato che i metodi di log hanno in ingresso un `object[]` quando passo dei parametri ho sempre delle operazioni di *boxing*.
Negli scenari ad alte performance posso voler evitare queste passando dei parametri già tipizzati correttamente.

### `LoggerMessage.Define`

La prima opzione è usare il metodo `LoggerMessage.Define<T1..Tn>` che permette di definire una `Action` sullo specifico log con i parametri esplicitati del tipo corretto.
Per esempio se voglio loggare un messaggio con un parametro `string`, uno `decimal` e l'ultimo `int` posso scrivere
```csharp
private static readonly Action<ILogger, string, decimal, int, Exception?> _logPayment =  
    LoggerMessage.Define<string, decimal, int>(  
        LogLevel.Information,  
        new EventId(5001, nameof(CreatePayment)),  
        "Customer {Email} purchased product {ProductId} at {Amount}"  
    );
```
e utilizzarlo in questo modo:
```csharp
_logPayment(_logger, email, amount, productId, null);
```
Questo metodo ha lo svantaggio di essere estremamente verboso e poco leggibile (esempio devo sempre passare `null` nel parametro dell'eccezione).

### Source Generator

^f609e8

Per risolvere i problemi di cui sopra Microsoft fornisce in automatico l'attributo `[LoggerMessage]` per creare codice autogenerato estremamente performante per ogni singolo log.
Si utilizza creando una extension di `ILogger` che esplicita il singolo log che voglio rendere performante:
```csharp
[LoggerMessage(Level = LogLevel.Information,  
    EventId = 5001,  
    Message = "Customer {Email} purchased product {ProductId} at {Amount}")]  
public static partial void LogPaymentCreation(  
    this ILogger logger, string email, decimal amount, int productId);
```
l'utilizzo è semplice:
```csharp
_logger.LogPaymentCreation(email, amount, productId);
```
Lo svantaggio di questo metodo è che, essendo una extension di `ILogger` questo metodo viene suggerito ogni volta che faccio `logger.`; se ho 1000 log ad alte performance avrò 1000 extension.
## Varie

### Boxing e log levels
Gli `args` che vengono passati al messaggio di log sono dei `object[]`, quindi quando li passo ho un boxing sicuro che potrebbe non servire qualora il minimum log level non sia raggiunto (esempio livello minimo `Warning` e sto loggando ad `Info`).
La soluzione più semplice è, nelle applicazioni ad alte performance, controllare che il log sia abilitato prima di chiamare il comando:
```csharp
if (logger.IsEnabled(LogLevel.Inmformation))
	logger.LogInformation("Message {Par1} - {Par2}", par1, par2)
```
oppure un modo più elegante per risolvere il problema è usare l'attributo `LoggerMessage`, vedi capitolo sui [[Logging in .NET#^f609e8|Source Generators]]. 
### Timed log entries
Posso sfruttare lo `using` per creare dei log che aggiungono al messaggio di log anche quanto ci ha messo una determinata operazione.
Per farlo posso creare una classe con delle extension come questa:
```csharp
public class TimedOperation : IDisposable  
{  
    private readonly ILogger _logger;  
    private readonly LogLevel _logLevel;  
    private readonly string _messageTemplate;  
    private readonly object?[] _args;  
    private readonly long _startingTimestamp;  
  
    public TimedOperation(ILogger logger, LogLevel logLevel, string messageTemplate, object?[] args)  
    {        _logger = logger;  
        _logLevel = logLevel;  
        _messageTemplate = messageTemplate;  
        _args = new object[args.Length + 1];  
        Array.Copy(args, _args, args.Length);  
        _startingTimestamp = Stopwatch.GetTimestamp();  
    }  
    public void Dispose()  
    {        var delta = Stopwatch.GetElapsedTime(_startingTimestamp);  
        _args[^1] = delta.TotalMilliseconds;  
        _logger.Log(_logLevel, $"{_messageTemplate} completed in {{OperationDurationMs}}ms", _args);  
    }
}

public static IDisposable BeginTimedOperation(  
    this ILogger logger, LogLevel logLevel, string messageTemplate, params object[] args)  
{  
    return new TimedOperation(logger, logLevel, messageTemplate, args);  
}
```
e chiamarla in questo modo:
```csharp
using (var _ = logger.BeginTimedOperation("Operation {Par1}", par1))  
{  
    // measured operation here
};
```

### Cambiare livello di log runtime
Questa operazione è possibile qualora il provider su cui mi sto appoggiando per la mia minimal api o applicazione asp.net fornisca l'hot reload del file `appsettings.json`.
Se è così (e tutti i provider normali come Azure o AWS offrono questa cosa) allora basta modificare il file di cui sopra modificando il `LogLevel` minimo e automaticamente posso visualizzare più o meno log senza alcun riavvio.

## Serilog
Serilog è la libreria più utilizzata in .NET per la gestione dei log ed è famosa per la quantità di provider che fornisce (che nel linguaggio di Serilog si chiamano `Sink`).
Attenzione che Serilog **non eredita da `ILogger`** di Microsoft ma da una sua implementazione di `ILogger`.
Una delle caratteristiche più importanti di Serilog è che fornisce la possibilità di utilizzare anche un logger statico, che può quindi essere acceduto in tutta l'applicazione anche senza DI.
```csharp
ILogger logger = new LoggerConfiguration()  
    .WriteTo.Console(theme:AnsiConsoleTheme.Code)  
    .CreateLogger();  
  
// Da ora in poi posso accedere a Log.Logger in modo statico
Log.Logger = logger;
```

### Structured data
In Serilog se metto la `@` prima di una variabile questa viene visualizzata nei log serializzata Json in automatico.
```csharp
logger.logInformation("New payment {@Payment}", payment)
```
Se voglio limitare il numero di property che vengono automaticamente serializzata nei log posso usare `Decostruct.ByTransform` quando definisco il logger.

### Timed operation
In Serilog bisogna aggiungere il pacchetto nuget `Serilog.Timings` e poi scrivere
```csharp
var op = logger.BeginOperation("Begin Operation")
await Task.Delay(100);
logger.Information("End Operation")
// Con questa riga scrive il messaggio sopra aggiungendo "completed in xxx ms"
op.Complete(); //op.Abandon();
```

### Mask sensitive logs
Per prima cosa è necessario aggiungere il pacchetto nuget `Destructurama.Attributed` e poi aggiungere l'attributo `LogMasked` sull'attributo della classe che voglio mascherare nei log.

```csharp
using System;
using Serilog;
using Destructurama;
using Destructurama.Attributed;

// Definisci una classe con dati sensibili
public class UserLogin
{
    public string Username { get; set; }
    
    [LogMasked]
    public string Password { get; set; }
}

ILogger logger = new LoggerConfiguration()  
    .WriteTo.Console()
    // obbligatorio per dire a Serilog di usare gli attributi
    .Destructure.UsingAttributes()  
    .CreateLogger();
Log.Information("User login attempt: {@UserLogin}", loginAttempt);
// 2023-06-06 12:34:56 [Information] User login attempt: UserLogin { Username: "user123", Password: "***" }
```
Con l'attributo posso fare varie mascherature:
* **Specifica il Carattere di Mascheramento**: `[LogMasked(Mask = "#")]`
* **Specifica la Lunghezza della Mascheratura**: `[LogMasked(Mask = "#", Length = 5)]`
* **Solo le prime lettere visibili**: `[LogMasked(ShowFirst = 2)]`

### Async logs
Quando noi scriviamo un log questo viene gestito in maniera sincrona fino al provider/sink e poi è questo ultimo che penserà a come rendere il tutto asincrono, facendo batching e implementando logiche sue.
Non tutti i provider però forniscono implementazioni asincrone, per esempio la Console gestisce i log in maniera 100% sincrona.
Qualora volessi gestire un provider come asincrono sempre indipendentemente dalla sua implementazione posso usare il pacchetto nuget `Serilog.Sinks.Async`.
Utilizzando `Serilog.Sinks.Async`, i log vengono messi in una coda e inviati a un sink separato su un thread di background, riducendo così l'impatto delle operazioni di I/O sul thread principale dell'applicazione.
```csharp
Log.Logger = new LoggerConfiguration()
	.WriteTo.Async(a => a.Console())
	.CreateLogger();

	Log.Information("Log message {Number}", i);
	// Chiudi e svuota i log
	Log.CloseAndFlush();
```

### Custom sink
Analogamente al logger i MIcrosoft anche in Serilog è molto semplice creare un sink custom, basta creare una classe figlia di `ILogEventSink` compilando il metodo `Emit`
```csharp
public class CustomSink : ILogEventSink  
{  
    private readonly IFormatProvider? _formatProvider;  
  
    public CustomSink(IFormatProvider? formatProvider)  
    {
	    _formatProvider = formatProvider;  
    }
    public CustomSink() : this(null)
    {
    }  
    
    public void Emit(LogEvent logEvent)  
    {
	    var message = logEvent.RenderMessage(_formatProvider);  
        Console.WriteLine($"{DateTime.UtcNow} - {message}");  
    }
}
  
  
public static class CustomSinkExtensions  
{  
    public static LoggerConfiguration CustomSink(  
        this LoggerSinkConfiguration sinkConfiguration,  
        IFormatProvider? formatProvider = null)  
    {        return sinkConfiguration.Sink(new CustomSink(formatProvider));  
    }
}

```
E utilizzare l'extension nel metodo di configurazione dei log
```csharp
ILogger logger = new LoggerConfiguration()  
    .WriteTo.NickSink()
    .CreateLogger();
```

### Minimal API
Usare Serilog al posto del logger classico in una minimal API è molto semplice in quanto usare la DI per iniettare il logger di Serilog invece di quello built-in in questo modo.
```csharp
var builder = WebApplication.CreateBuilder(args);  
  
Serilog.ILogger logger = new LoggerConfiguration()  
    .WriteTo.Console(theme:AnsiConsoleTheme.Code)  
    .CreateLogger();  
  
Log.Logger = logger;  
  
builder.Services.AddSingleton(logger);  
  
var app = builder.Build();  
  
// il logger qui è quello di Serilog in quanto lo ho iniettato con la DI sopra in "AddSingleton"
app.MapGet("/", (Serilog.ILogger log) =>  
{  
    log.Information("Hello from the endpoint");  
    return "Hello World!";  
});  
  
app.Run();
```
Il limite di questo approccio è che tutti i log di Microsoft verranno gestiti con il suo logger, mentre i miei con Serilog.
Nella prossima sezione vediamo come far sì che anche Microsoft usi Serilog e, ancora più importante, la mia applicazioni usi sempre `ILogger` di Microsoft e Serilog sia solo un provider di questo ultimo.
### ASP.NET Core
Uno dei limiti di Serilog è la non compatibilità automatica con il logger built-in di Microsoft, quindi l'interfaccia e i metodi sono diversi.
Vorrei invece usare sempre l'interfaccia `ILogger` di Microsoft e usare Serilog solo come "dettaglio" implementativo.
Questa operazione può essere fatta molto semplicemente in ASP.NET Core usando il pacchetto nuget `Serilog.AspNetCore` e scrivendo così.
```csharp
var builder = WebApplication.CreateBuilder(args);  
  
// Definisco il logger che voglio impostando la variabile statica
Log.Logger = new LoggerConfiguration()  
    .ReadFrom.Configuration(builder.Configuration)  
    .CreateLogger();  
  
// Inietta la variabile statica sopra ovunque io abbia un ILogger di Micorosft
builder.Host.UseSerilog();
```
Per esempio in questo controller il logger sembra quello di Microsoft ma invece internamente userà quello di Serilog.
```csharp
public WeatherForecastController(ILogger<WeatherForecastController> logger)  
{  
    _logger = logger;  
}
```

### Configurazione tramite File

Serilog può anche essere configurato tramite un file di configurazione JSON, che può essere particolarmente utile per separare la configurazione dal codice.
Ecco un esempio completo di file `appsettings.json`:

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "Serilog": {
    "MinimumLevel": {
      "Default": "Information",
      "Override": {
        "Microsoft.AspNetCore": "Warning"
      }
    },
    "WriteTo": [
      {
        "Name": "Console"
      },
      {
        "Name": "File",
        "Args": {
          "path": "logs/log.txt",
          "rollingInterval": "Day"
        }
      },
      {
        "Name": "ApplicationInsights",
        "Args": {
          "connectionString": "APPLICATION INSIGHTS CONNECTION STRING",
          "telemetryConverter": "Serilog.Sinks.ApplicationInsights.TelemetryConverters.TraceTelemetryConverter, Serilog.Sinks.ApplicationInsights"
        }
      }
    ],
    "Enrich": ["FromLogContext", "WithMachineName", "WithThreadId"],
    "Properties": {
      "Application": "LoggingCourse"
    }
  },
  "AllowedHosts": "*"
}
```

Per utilizzare questo file di configurazione, è necessario aggiungere il pacchetto `Serilog.Settings.Configuration`:
```csharp
var configuration = new ConfigurationBuilder()
	.AddJsonFile("appsettings.json")
	.Build();

Log.Logger = new LoggerConfiguration()
	.ReadFrom.Configuration(configuration)
	.CreateLogger();

```

### Application Insights
Per poter usare come Sink Application Insights, oltre al pacchetto nuget, devo usare la seguente configurazione
```json
{
	"Name": "ApplicationInsights",
	"Args": {
	  "connectionString": "APPLICATION INSIGHTS CONNECTION STRING",
	  "telemetryConverter": "Serilog.Sinks.ApplicationInsights.TelemetryConverters.TraceTelemetryConverter, Serilog.Sinks.ApplicationInsights"
	}
  }
```