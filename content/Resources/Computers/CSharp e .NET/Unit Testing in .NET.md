---
tags:
  - CSharp
  - DotNET
---
## Tipologie di test

![[the-test-pyramid.png]]

* Uni testing:
* Component testing (functional testing o narrow integration testing):
* Integration test
* End to end test

## Librerie di test

* Testing library: la libreria che effettivamente lancia i test
	* **xunit**: è la libreria più popolare
	* **nunit**
	* **MSTest**
* Mocking Library: la libreria che permette la creazione di mock
	* **Moq**
	* **NSubstitute**
	* **FakeItEasy**
* Assertion Library: la libreria per validare l'outcome con quello aspettato
	* **Fluent Assertion**
	* **Shouldly**

## Naming
Assumiamo di avere un progetto chiamato `MyMathLibrary` che contiene una classe chiamata `MyMath` di funzioni matematiche custom della mia applicazione.

### Naming del progetto

Per prima cosa è importante sottolineare che tutti i progetti di test devono essere raggruppati in una cartella ad hoc, in modo che non siano confusi con il codice effettivo; è una buona idea collocare il proprio codice in una cartella `src` e i test in una cartella in `test`.

Una volta creata la cartella è necessario creare il progetto di test per `` `MyMathLibrary` ``, in particolare il nome deve dipendere dalla tipologia di test:

| Tipologia di test | Nome                             |
| ----------------- | -------------------------------- |
| Unit              | `MyMathLibraryTests.Unit`        |
| Integration       | `MyMathLibraryTests.Integration` |
| End to End        | `MyMathLibrary.Tests.E2E`        |
Come si vede il progetto di test è estremamente parlante in quanto indica il progetto testato e la tipologia di test che possiamo trovare al suo interno.

### Naming della classe

La classe di test si chiamerà con lo stesso nome della classe originale con la stringa `Tests` in fondo, quindi nel caso di `MyMath` questa si chiamerà `MyMathTests`.

### Naming del test

Il nome del test deve seguire lo stile `Method_Should_When`", in particolare dovrà quindi indicare dopo lo `Should` cosa dovrebbe fare e dopo il `When` in che caso dovrebbe fare quanto indicato.

Assumiamo che all'interno della mia classe `MyMath` vi sia il metodo `Log` che fa un logaritmo; il test sarà così scritto.
```csharp
[Fact]  
public void Log_ShouldCalculateLogOfANumber_WhenIntegerNumberIsGiven()  
{  
    // Test  
}
```

### System Under Test
Per convenzione l'oggetto che viene testato si chiama "System Under Test", abbreviato con `sut`.
```csharp
private readonly ClassToTest _sut = new();
```
## Arrange, Act, Assert

I test dovrebbero essere strutturati secondo la regola "Arrange, Act, Assert": `Arrange` prepara l'ambiente, `Act` esegue l'azione da testare, e `Assert` verifica che il risultato sia corretto.

```csharp
[TestMethod]
public void TestAdd()
{
    // Arrange
    var calculator = new Calculator();
    int a = 1, b = 2;

    // Act
    int result = calculator.Add(a, b);

    // Assert
    Assert.AreEqual(3, result);
}
```


## Testare metodi non public

### Private
I metodi privati vengono testati implicitamente chiamando i metodi `public` che che li chiamano.
### Internal
I metodi `internal`, quindi visibili solo nell'assembly dove si trovano, possono essere testati 
modificando il file `csproj` aggiungendo la stringa:
```xml
<ItemGroup>
	<InternalsVisibleTo Include="Nome.Progetto.Di.Test"/>
</ItemGroup>
```

## Testare gli eventi

Testare che degli eventi siano stato effettivamente lanciati in C# non è immediato; tipicamente è possibile testare che un evento venga lanciato aspettando un [[ManualResetEvent]] che viene settato in un listener dell'evento stesso.
Questo metodo funziona ma risulta un po' macchinoso; Fluent Assertion risolve il problema fornendo dei metodi comodi per testare il tutto.

### Fluent Assertion

[Fluent Assertion](https://fluentassertions.com/) permette di testare che un determinato evento venga lanciato in modo semplice.
Per prima cosa è necessario comunicare a Fluent Assertion che voglio monitorare l'oggetto utilizzando il l'extension `Monitor()`;
```csharp
using var monitoredClass = _myClass.Monitor();
```
e successivamente è possibile utilizzare il check `Should().Raise("EventName")` in questo modo:
```csharp
monitoredClass.Should().Raise(nameof(myClass.MyCustomEvent));
```
E' possibile anche aggiungere dei check sul `sender` e sugli `args` in questo modo:
```csharp
monitoredClass.Should()
            .Raise(nameof(myClass.MyCustomEvent))
            .WithSender(subject)
            .WithArgs<PropertyChangedEventArgs>(args => args.PropertyName == "SomeProperty");
```

 > [!tip] Non raisare eventi a costruttore
> Gli eventi a costruttore non possono essere presi da nessuno in quanto non potrò mai fare il +=.


## Testare il `Received` di extension e metodi statici
Gli extension method e i metodi statici non sono semplici da testare in quanto non è possibile mockarli o usare i metodi di `NSubstitute` come `Receive`.
Il modo migliore per risolvere il problema è wrappare la classe che voglio testare in una classe adapter e testare con i metodi `Received` direttamente questa ultima.
Vediamo il tutto con un esempio: il metodo `LogInformation` dell'interfaccia `ILogger` è una extension; come faccio a testare che il mio metodo abbia loggato, per esempio, `logger.LogInformation("This is a log message")`?.
L'idea è creare un adapter con tutti i metodi di log, per esempio:
```csharp
public interface ILoggerAdapter<TType>  
{  
    void LogInformation(string? message, params object?[] args);  
  
    void LogError(Exception? exception, string? message, params object?[] args);  
}

public class LoggerAdapter<TType> : ILoggerAdapter<TType>
{
    private readonly ILogger<TType> _logger;

    public LoggerAdapter(ILogger<TType> logger)
    {
        _logger = logger;
    }

    public void LogInformation(string? message, params object?[] args)
    {
        _logger.LogInformation(message, args);
    }

    public void LogError(Exception? exception, string? message, params object?[] args)
    {
        _logger.LogError(exception, message, args);
    }
}
```
La classe `LoggerAdapter`, essendo una classe normale senza extension ne roba statica, può essere testata come al solito.
Ovviamente la classe del codice dovrà usare tale adapter e non il logger effettivo.


## Mocking
Il mocking sono quelle tecniche che prevedono la "sostituzione" di una dipendenza con una sua versione "semplificata" che si comporta in modo prevedibile.
L'idea è che se devo testare una classe potrei non voler istanziare anche le sue dipendenze, soprattutto se queste fanno operazioni pesanti come scritture su disco, letture da file e così via.
Prerequisiti:
* La dipendenza che voglio sostituire deve avere un'interfaccia
* La classe che sto testando deve dipendere e utilizzare sempre tale interfaccia (senza cast ovviamente)
* La classe non deve istanziare la classe concreta ma deve ricevere l'istanza dall'esterno (Dependency Inversion), tipicamente da costruttore (in modo da poter fare comodamente Dependency Injection)
Le due librerie principali sono `Moq` e `NSubstitute`.



## xUnit

### Setup e TearDown
In xUnit il `Setup` è il costruttore della classe mentre il `TearDown` è il metodo `Dispose` (la classe di test dovrà ereditare da `IDisposable`).

#### Async code
Può succedere, tipicamente negli integration test, di avere del codice asincrono da aggiungere nei metodi `Setup` e `TearDown`.
In questo caso devo ereditare dall'interfaccia `IAsyncLifetime` che ha i metodi `InitializeAsync` e `DisposeAsync` e mettere il codice corrispondente nei due metodi.
Se ho codice sincrono e asincrono posso usare il costruttore per il codice sincrono e il metodo `InitializeAsync` per il codice asincrono tenendo a mente che **il costruttore viene chiamato prima di `InitializeAsync`**.


### Execution Model
==xUnit crea una nuova istanza della classe di test per ogni singolo test==.
Quindi se la classe di test ha un costruttore e un metodo `Dispose`, questi vengono chiamati **per ogni singolo test**.
Se la classe ha una `IClassFixture` come shared context, il costruttore di questo ultimo viene invece chiamato una sola volta prima di tutti i test.

### `ITestOutputHelper`
Questa classe permette di printare dei dati su console durante l'esecuzione dei test. Questo è utile per diagnosticare problemi, verificare lo stato di variabili e funzioni durante l'esecuzione del test, e documentare il flusso di esecuzione del test.
La classe viene passata automaticamente alla classe di test se definita a costruttore.
```csharp
public class CalculatorTests
{
    private readonly ITestOutputHelper _output;

    public CalculatorTests(ITestOutputHelper output)
    {
        _output = output;
    }

    [Fact]
    public void Add_ReturnsCorrectSum()
    {
        _output.WriteLine($"This string will be printed to Console");
    }
}
```

### OneTimeSetup e OneTimeTearDown
Se voglio scrivere del codice che venga eseguito una sola volta prima di tutti i test di una classe, e analogamente del codice che venga eseguito una sola volta solo alla fine, devo creare una classe `Fixture` che rappresenta uno `shared context` tra i vari metodi di test della mia classe.
Il costruttore di tale classe verrà chiamato una sola volta all'inizio e il `Dispose` una sola volta alla fine.
```csharp
public class MyClassFixture : IDisposable
{
    public Guid Id { get; } = Guid.NewGuid();

    public MyClassFixture()
    {
        // One time setup logic
    }

    public void Dispose()
    {
        // One time tear down logic
    }
}

public class ClassFixtureBehaviorTests : IClassFixture<MyClassFixture>
{
    private readonly MyClassFixture _fixture;

    public ClassFixtureBehaviorTests(MyClassFixture fixture)
    {
        _fixture = fixture;
    }
}

```
Qualora la classe `Fixture` fosse utilizzata in più di una classe di test, il costruttore viene chiamato comunque una sola volta per tutte, stessa cosa per il `Dispose`.

### Shared context
Spesso, soprattutto negli integration tests e e3e tests voglio condividere tra varie classi di test una determinata `Fixture`, in particolare condividere esattamente la stessa istanza.
A livello di flusso voglio il costruttore della `Fixture`, i costruttori delle classi di test in cui la `Fixture` è sempre la stessa chiamato uno per ogni metodo di test (ricordo che per ogni metodo xUnit istanzia una nuova classe) e infine il `Dispose` della classe `Fixture`.
Questo esatto comportamento avviene con il concetto di `CollectionFixture`.
Per fare questo devo prima definire una classe vuota con attributo `CollectionDefinition` che serve solo come aggregatore, esempio
```csharp
[CollectionDefinition("My awesome collection fixture")]
public class TestCollectionFixture : ICollectionFixture<MyClassFixture>
{

}
```
Ora se aggiungo l'attributo `[Collection("My awesome collection fixture")]` alla classe di test questa riceverà automaticamente a costruttore la classe `MyClassFixture` in questione.
Per esempio queste due classi riceveranno esattamente la stessa istanza di `MyClassFixture`.
```csharp
[Collection("My awesome collection fixture")]
public class CollectionFixturesBehaviorTests
{
    private readonly MyClassFixture _fixture;

    public CollectionFixturesBehaviorTests(MyClassFixture fixture)
    {
        _fixture = fixture;
    }
}

[Collection("My awesome collection fixture")]
public class CollectionFixturesBehaviorTestsAgain
{
    private readonly MyClassFixture _fixture;

    public CollectionFixturesBehaviorTestsAgain(MyClassFixture fixture)
    {
        _fixture = fixture;
    }
}
```

### Parallelizzazione
In xUnit i test all'interno della stessa classe **vengono eseguiti in serie**, mentre differenti classi di test vengono eseguite in parallelo tra loro.
Le classi di test che invece appartengono alla stessa `Collection` invece vengono lanciati in serie tra di loro.
==Possiamo quindi pensare ad ogni classe di test come appartenente ad una `Collection` con un solo elemento: tra `Collection` diverse i test vengono eseguiti in parallelo mentre in serie tra classi che condividono la stessa `Collection`==.
Questo comportamento di default è definito da
```csharp
[assembly: CollectionBehavior(CollectionBehaviour.CollectionPerClass)]
```
Se per un qualsiasi motivo voglio invece che tutti i test, indipendentemente dalla `Collection` in cui si trovano, debbano essere eseguiti in serie devo aggiungere un file con nome a mia scelta con questa riga:
```csharp
[assembly: CollectionBehavior(DisableTestParallelization = true)]
```



### Testare le date
Testare una classe che utilizza `DateTime` non è banale in quanto l'esito del test dipende da quando questo viene lanciato e non c'è modo per iniettare la data e l'ora corrente in base a quello che ci serve per i test.
Per esempio il seguente metodo non è testabile in quanto  non ho modo di modificare la data corrente
```csharp
public string GenerateGreetMessage()
{
    var dateTimeNow = DateTime.Now;
    return dateTimeNow.Hour switch
    {
        >= 5 and < 12 => "Good morning",
        >= 12 and < 18 => "Good afternoon",
        _ => "Good evening"
    };
}
```
Per risolvere il problema prima di .NET8 si doveva implementare un'`IDateTimeProvider` mentre ora una classe analoga  viene fornita già nel linguaggio chiamata `TimeProvider`.
La modifica del metodo di cui sopra con la nuova classe sarebbe
```csharp
public class Greeter
{
    private readonly TimeProvider _provider;

    // Il provider di sistema si chiama TimeProvider.System
    public Greeter(TimeProvider provider)
    {
        _provider = provider;
    }

    public string GenerateGreetMessage()
    {
        var dateTimeNow = _provider.GetLocalNow();
        return dateTimeNow.Hour switch
        {
            >= 5 and < 12 => "Good morning",
            >= 12 and < 18 => "Good afternoon",
            _ => "Good evening"
        };
    }
}
```
In questo modo nei test posso mockare il `TimeProvider` overridando i metodi per ottenere la data, principalmente il metodo `GetUtcNow()`.
Questa potrebbe essere la classe di test per il metodo di cui sopra:
```csharp
public class GreeterTests
{
    private readonly Greeter _sut;
    private readonly TimeProvider _dateTimeProvider = Substitute.For<TimeProvider>();

    public GreeterTests()
    {
	    _dateTimeProvider.LocalTimeZone.Returns(TimeZoneInfo.Utc);
        _sut = new Greeter(_dateTimeProvider);
    }

    [Fact]
    public void GenerateGreetMessage_ShouldSayGoodEvening_WhenItsEvening()
    {
        // Arrange
        _dateTimeProvider.GetUtcNow().Returns(new DateTime(2020, 1, 1, 20, 0, 0));

        // Act
        var result = _sut.GenerateGreetMessage();

        // Assert
        result.Should().Be("Good evening");
    }

    [Fact]
    public void GenerateGreetMessage_ShouldSayGoodMorning_WhenItsMorning()
    {
        // Arrange
        _dateTimeProvider.GetUtcNow().Returns(new DateTime(2020, 1, 1, 10, 0, 0));

        // Act
        var result = _sut.GenerateGreetMessage();

        // Assert
        result.Should().Be("Good morning");
    }

    [Fact]
    public void GenerateGreetMessage_ShouldSayGoodAfternoon_WhenItsAfternoon()
    {
        // Arrange
        _dateTimeProvider.GetUtcNow().Returns(new DateTime(2020, 1, 1, 15, 0, 0));

        // Act
        var result = _sut.GenerateGreetMessage();

        // Assert
        result.Should().Be("Good afternoon");
    }
}
```
La classe `TimeProvider` fornisce anche metodi per misurare intervalli temporali usando `GetTimestamp()` che internamente usa `Stopwatch` ma anche in questo caso il metodo è facilmente mockabile.