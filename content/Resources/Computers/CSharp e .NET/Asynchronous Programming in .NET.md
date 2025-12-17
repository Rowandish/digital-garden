---
tags:
  - Dometrain
---
Questa nota prende a piene mani dal corso [Asynchronous Programming in C# - From Zero to Hero](https://dometrain.com/course/from-zero-to-hero-asynchronous-programming-in-csharp/).
## Introduzione
Un `Task` rappresenta un'operazione asincrona ed è un'astrazione rispetto a `System.Threading.Thread` e ci permette di non preoccuparci sul context switching, sul threadpool o qualsiasi altra cosa che riguarda i Thread.
Il comando `await` permette di lanciare ciò che è scritto dopo in un thread diverso da quello del chiamante e permettere però al metodo chiamante di proseguire.
Per esempio se sto chiamando dal `Thread 1` (della UI) il metodo
```csharp
var response = await httpClient.GetAsync("URL")
```
il metodo `GetAsync` verrà eseguito su un thread diverso da quello del chiamante (e quindi non nel Thread 1 della UI) e questo ultimo potrà proseguire non freezando l'interfaccia..
Appena il metodo `GetAsync` avrà finito il Thread 1 della UI ritornerà a fare le istruzioni successive a tale metodo.
Non sempre viene cambiato il contesto ad un altro thread: se il task dopo l'`await` è già in stato `Completed` viene subito preso il risultato dal thread 1 e si prosegue senza alcun context swtich.

## Await decompilato
Quando scrivo un'istruzione con `await` il compilatore la traduce in una macchina a stati che riproduce il comportamento che voglio ad alto livello.
Vediamo come funziona sfruttando *sharplab.io*.
Questo è il codice C# che voglio analizzare:
```csharp
public async Task<List<LibraryModel>> GetLibraries()
    {
        var response = await httpClient.GetAsync("https://codeTraveler.io/Map");
        response.EnsureSuccessStatusCode();

        var contentStream = await response.Content.ReadAsStreamAsync();
        var libraries = await JsonSerializer.DeserializeAsync<List<LibraryModel>>(contentStream);

        return libraries ?? throw new InvalidOperationException("Libraries could not be retrieved.");
    }
```
Questo codice viene tradotto in
```csharp
[AsyncStateMachine(typeof(<GetLibraries>d__2))]
[DebuggerStepThrough]
public Task<List<LibraryModel>> GetLibraries()
{
    <GetLibraries>d__2 stateMachine = new <GetLibraries>d__2();
    stateMachine.<>t__builder = AsyncTaskMethodBuilder<List<LibraryModel>>.Create();
    stateMachine.<>4__this = this;
    stateMachine.<>1__state = -1;
    stateMachine.<>t__builder.Start(ref stateMachine);
    return stateMachine.<>t__builder.Task;
}
```
Nota: il compilatore crea tutte le variabili con le parentesi angolari `<>` per evitare name clash in quanto sono illegali per il programmatore umano.
Come si vede dal codice sopra viene creata una `stateMachine`, fatta partire e poi alla fine il metodo ritorna un `Task` al chiamante.
Vediamo come è fatta tale macchina a stati (commenti nel codice).
```csharp
[StructLayout(LayoutKind.Auto)]
[CompilerGenerated]
private struct <GetLibraries>d__2 : IAsyncStateMachine
{
    public int <>1__state;

    [Nullable(new byte[] { 0, 0, 1 })]
    public AsyncTaskMethodBuilder<List<LibraryModel>> <>t__builder;

    [Nullable(0)]
    public LibraryService <>4__this;

    //Le variabili locali si sono trasformate in field: questa è 'var response'
    [Nullable(new byte[] { 0, 1 })]
    private TaskAwaiter<HttpResponseMessage> <>u__1;

    [Nullable(new byte[] { 0, 1 })]
    private TaskAwaiter<Stream> <>u__2;

    [Nullable(new byte[] { 0, 2, 1 })]
    private ValueTaskAwaiter<List<LibraryModel>> <>u__3;

    private void MoveNext()
    {
  - // alla prima iterazione num = -1, quindi entrerà nel default case sotto
	// che è la prima riga che ho scritto nel metodo originale
        int num = <>1__state;
        LibraryService libraryService = <>4__this;
        List<LibraryModel> result3;
        try
        {
            TaskAwaiter<HttpResponseMessage> awaiter3;
            TaskAwaiter<Stream> awaiter2;
            ValueTaskAwaiter<List<LibraryModel>> awaiter;
            HttpResponseMessage result;
            switch (num)
            {
                default:
                    awaiter3 = libraryService.httpClient.GetAsync("https://codeTraveler.io/Map").GetAwaiter();
                    // Se il task è già completo non ho alcun cambio di thread, vado direttamente a IL_007e che sono le istruzioni che ho scritto successivamente all'await (EnsureSuccessStatusCode...)
                    if (!awaiter3.IsCompleted)
                    {
	                    // Imposto lo state=0 in modo che la prossima volta che entro nello switch proseguirò con l'istruzione successiva dopo l'await e non entrerò più qui.
                        num = (<>1__state = 0);
                        <>u__1 = awaiter3;
                        // Quando awaiter3 ha finito (asincrono) .net ritornerà si ritornerà nel MoveNext() ma con lo state cambiato a 1
                        <>t__builder.AwaitUnsafeOnCompleted(ref awaiter3, ref this);
                        // Dopo aver lanciato l'operazione in questione in un altro thread faccio il return in modo che il thread chiamante sia libero di proseguire.
                        return;
                    }
                    goto IL_007e;
	            // Questo case fa solo pulizia delle variabili ma poi serve solo ad andare a IL_007e che sono le righe successive all'await
				case 0:
                    awaiter3 = <>u__1;
                    // Ottimizzazione per dire al GC che awaiter3 ora non è più utilizzata e può eliminarla
                    <>u__1 = default(TaskAwaiter<HttpResponseMessage>);
                    // Imposta a -1 solo per emergenza se qualcosa crasha
                    num = (<>1__state = -1);
                    goto IL_007e;
                case 1:
                    awaiter2 = <>u__2;
                    <>u__2 = default(TaskAwaiter<Stream>);
                    num = (<>1__state = -1);
                    goto IL_00e7;
                case 2:
                    {
                        awaiter = <>u__3;
                        <>u__3 = default(ValueTaskAwaiter<List<LibraryModel>>);
                        num = (<>1__state = -1);
                        break;
                    }
                    IL_00e7:
                    awaiter = JsonSerializer.DeserializeAsync<List<LibraryModel>>(awaiter2.GetResult()).GetAwaiter();
                    if (!awaiter.IsCompleted)
                    {
                        num = (<>1__state = 2);
                        <>u__3 = awaiter;
                        <>t__builder.AwaitUnsafeOnCompleted(ref awaiter, ref this);
                        return;
                    }
                    break;
                    IL_007e:
                    result = awaiter3.GetResult();
                    result.EnsureSuccessStatusCode();
                    // Faccio partire il prossimo await, quello sullo stream
                    awaiter2 = result.Content.ReadAsStreamAsync().GetAwaiter();
                    // Se già completato vai subito a IL_00e7 che sono le istruzioni successive
                    if (!awaiter2.IsCompleted)
                    {
	                    // prossimo step state = 1
                        num = (<>1__state = 1);
                        <>u__2 = awaiter2;
                        <>t__builder.AwaitUnsafeOnCompleted(ref awaiter2, ref this);
                        return;
                    }
                    goto IL_00e7;
            }
            List<LibraryModel> result2 = awaiter.GetResult();
            if (result2 == null)
            {
                throw new InvalidOperationException("Libraries could not be retrieved.");
            }
            result3 = result2;
        }
        // Nota: tutte le eccezioni che avvengo all'interno di un metodo async vengono prese e non throwate ma inserite al builder. Questo comporta, per motivi vari, che se non faccio un await di un metodo async le eccezioni vengono perse. Il metodo giusto è chiamare `await GetLibraries()` all'interno di un blocco try/catch gestendo le eccezioni che questo fornisce.
        catch (Exception exception)
        {
            <>1__state = -2;
            <>t__builder.SetException(exception);
            return;
        }
        <>1__state = -2;
        <>t__builder.SetResult(result3);
    }
}
```

## Implementazione Task a mano
Per capire meglio come funziona la classe `Task` e considerarla meno magica di quello che è può essere interessante reimplementarla nelle sue funzioni principali, in modo da capire bene cosa succede internamente.
La classe in questione può venire chiamata come fosse un vero `Task` in questo modo:
```csharp
Console.WriteLine($"Starting Thread Id: {Environment.CurrentManagedThreadId}");

await DomeTrainTask.Run(() => 
    Console.WriteLine($"First DomeTrainTask Id: {Environment.CurrentManagedThreadId}"));

await DomeTrainTask.Delay(TimeSpan.FromSeconds(1));

Console.WriteLine($"Second DomeTrainTask Id: {Environment.CurrentManagedThreadId}");

await DomeTrainTask.Delay(TimeSpan.FromSeconds(1));

await DomeTrainTask.Run(() => 
    Console.WriteLine($"Third DomeTrainTask Id: {Environment.CurrentManagedThreadId}"));
```

```csharp
using System;
using System.Runtime.CompilerServices;
using System.Runtime.ExceptionServices;
using System.Threading;

/// <summary>
///     Implementazione semplificata di un task asincrono, simile a `Task` di .NET.
/// </summary>
public class DomeTrainTask
{
    private readonly Lock _lock = new();
    private bool _completed;
    private Exception? _exception;
    private Action? _action;
    private ExecutionContext? _context;

    /// <summary>
    ///     Indica se il task è stato completato.
    /// </summary>
    public bool IsCompleted
    {
        get
        {
            lock (_lock)
            {
                return _completed;
            }
        }
    }

    /// <summary>
    ///     Esegue un'azione quando il task è completato.
    ///     Se il task è già completato, esegue immediatamente l'azione su un thread del pool.
    ///     Se non è ancora completato, salva l'azione per eseguirla in seguito.
    /// </summary>
    /// <param name="action">L'azione da eseguire al completamento del task.</param>
    /// <returns>Un nuovo `DomeTrainTask` che rappresenta l'azione successiva.</returns>
    public DomeTrainTask ContinueWith(Action action)
    {
        DomeTrainTask task = new();

        lock (_lock)
        {
            if (_completed)
            {
                ThreadPool.QueueUserWorkItem(_ =>
                {
                    try
                    {
                        action();
                        task.SetResult();
                    }
                    catch (Exception e)
                    {
                        task.SetException(e);
                    }
                });
            }
            else
            {
                _action = action;
                _context = ExecutionContext.Capture();
            }
        }

        return task;
    }

    /// <summary>
    ///     Segna il task come completato con successo.
    /// </summary>
    public void SetResult() => CompleteTask(null);

    /// <summary>
    ///     Segna il task come completato con un'eccezione.
    /// </summary>
    /// <param name="exception">L'eccezione da segnalare come errore del task.</param>
    public void SetException(Exception exception) => CompleteTask(exception);

    /// <summary>
    ///     Completa il task, segnalando eventualmente un'eccezione.
    ///     Se è registrata un'azione di continuazione, viene eseguita.
    /// </summary>
    /// <param name="exception">L'eccezione da impostare, se presente.</param>
    private void CompleteTask(Exception? exception)
    {
        lock (_lock)
        {
            if (_completed)
                throw new InvalidOperationException(
                    "DomeTrainTask già completato. Impossibile impostare il risultato.");

            _completed = true;
            _exception = exception;

            if (_action is not null)
            {
                if (_context is null)
                {
                    _action.Invoke();
                }
                else
                {
                    ExecutionContext.Run(_context, state => ((Action?)state)?.Invoke(), _action);
                }
            }
        }
    }

    /// <summary>
    ///     Blocca il thread chiamante fino al completamento del task.
    ///     Se il task è già completato, ritorna immediatamente.
    ///     Se è stato completato con un'eccezione, l'eccezione viene rilanciata.
    /// </summary>
    public void Wait()
    {
        ManualResetEventSlim? resetEventSlim = null;

        lock (_lock)
        {
            if (!_completed)
            {
                resetEventSlim = new ManualResetEventSlim();
                ContinueWith(() => resetEventSlim.Set());
            }
        }

        resetEventSlim?.Wait();

        if (_exception is not null)
        {
            ExceptionDispatchInfo.Throw(_exception);
        }
    }

    /// <summary>
    ///     Crea un task che viene completato dopo un determinato intervallo di tempo.
    /// </summary>
    /// <param name="delay">Il tempo di attesa prima del completamento del task.</param>
    /// <returns>Un `DomeTrainTask` che si completa dopo il ritardo specificato.</returns>
    public static DomeTrainTask Delay(TimeSpan delay)
    {
        DomeTrainTask task = new();
        new Timer(_ => task.SetResult()).Change(delay, Timeout.InfiniteTimeSpan);
        return task;
    }

    /// <summary>
    ///     Esegue un'azione in modo asincrono su un thread del pool e restituisce un task che rappresenta l'operazione.
    /// </summary>
    /// <param name="action">L'azione da eseguire.</param>
    /// <returns>Un `DomeTrainTask` che rappresenta l'operazione in esecuzione.</returns>
    public static DomeTrainTask Run(Action action)
    {
        DomeTrainTask task = new();

        ThreadPool.QueueUserWorkItem(_ =>
        {
            try
            {
                action();
                task.SetResult();
            }
            catch (Exception e)
            {
                task.SetException(e);
            }
        });

        return task;
    }

    /// <summary>
    ///     Restituisce un awaiter per supportare la sintassi async/await.
    ///     infatti .NET utilizza il duck typing per determinare se un tipo è awaitable e posso scrivere await su di esso.
    /// </summary>
    /// <returns>Un `DomeTrainTaskAwaiter` per il task corrente.</returns>
    public DomeTrainTaskAwaiter GetAwaiter() => new(this);
}

/// <summary>
///     Awaiter personalizzato per `DomeTrainTask`, implementa `INotifyCompletion` per supportare `await`.
/// </summary>
public readonly struct DomeTrainTaskAwaiter : INotifyCompletion
{
    private readonly DomeTrainTask _task;

    /// <summary>
    ///     Costruttore interno dell'awaiter.
    /// </summary>
    /// <param name="task">Il task da gestire.</param>
    internal DomeTrainTaskAwaiter(DomeTrainTask task) => _task = task;

    /// <summary>
    ///     Indica se il task è completato.
    /// </summary>
    public bool IsCompleted => _task.IsCompleted;

    /// <summary>
    ///     Registra un'azione da eseguire al completamento del task.
    /// </summary>
    /// <param name="continuation">L'azione da eseguire.</param>
    public void OnCompleted(Action continuation) => _task.ContinueWith(continuation);

    /// <summary>
    ///     Restituisce l'awaiter stesso (self-referencing).
    /// </summary>
    /// <returns>L'awaiter corrente.</returns>
    public DomeTrainTaskAwaiter GetAwaiter() => this;

    /// <summary>
    ///     Attende il completamento del task, bloccando il thread se necessario.
    ///     Se il task è completato con un'eccezione, la rilancia.
    /// </summary>
    public void GetResult() => _task.Wait();
}
```

## Task e eccezioni
In .NET la gestione delle eccezioni nei task è da capire bene: ci sono tre casi principalmente:
* Metodo `async Task` `await`ato
* Metodo `async Task` non `await`ato
* Metodo `async void`
Vediamo i 3 casi.
### Async Task awaitato
Il metodo `TaskWithException` è un metodo `async Task`: se viene `await`ato come sotto posso fare un `try/catch` classico.
Questo è il metodo più pulito.
```csharp
static async Task TaskWithException()
{
    await Task.Delay(500);
    throw new InvalidOperationException("Errore nel Task!");
}

static async Task ExampleWithAwait()
{
    try
    {
        await TaskWithException(); // Eccezione propagata e catturata
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Eccezione catturata: {ex.Message}");
    }
}
```
Ci sono diversi modi per rilanciare eccezioni che vengono generate in un metodo asincrono:
* Usare la parola chiave `await` (preferito perché consente al `Task` di essere eseguito in modo asincrono su un thread diverso, evitando di bloccare il thread corrente): _ `await DoSomethingAsync();`
* Usare `.GetAwaiter().GetResult()`: `DoSomethingAsync().GetAwaiter().GetResult();`

### Async Task non awaitato
Se chiamo il metodo `TaskWithException` senza l'`await` l'eccezione viene mangiata 
In questo caso, il `Task` parte in background e, quando l'eccezione viene generata, **nessuno l'aspetta** e il runtime la ignora ("mangiata"). Per capirne il motivo vedi codice decompilato sopra.
Il .NET **non considera le eccezioni non osservate nei Task come fatali**, a meno che non venga attivata un'eventuale gestione globale degli errori (come `TaskScheduler.UnobservedTaskException`).

```csharp
TaskWithException();
Console.WriteLine("Il metodo termina senza rilevare errori.");

static async Task TaskWithException()
{
    await Task.Delay(500); // Simula un'operazione asincrona
    throw new InvalidOperationException("Errore nel Task!");
}
```

### Async void
I metodi `async void` sono un caso speciale perché **non restituiscono un `Task`**.  
Questo significa che:
1. Non possono essere `await`ati dal chiamante.
2. Non permettono di catturare l'eccezione con un normale `try-catch` attorno alla chiamata.
3. Se si verifica un'eccezione non gestita all'interno, questa viene **propagata direttamente al contesto di esecuzione globale**, causando il **crash dell'app**.
```csharp
static async void ThrowExceptionAsyncVoid()
{
    await Task.Delay(500);
    throw new InvalidOperationException("Errore in async void!");
}

static void ExampleAsyncVoid()
{
    try
    {
        ThrowExceptionAsyncVoid(); // L'eccezione non può essere catturata!
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Catturata eccezione: {ex.Message}"); // Questo non verrà mai eseguito!
    }
}
```

## Non usare mai async void
Per il motivo di cui sopra per cui è impossibile gestire le eccezioni di un metodo `async void` tali metodi devono [essere evitati il più possibile](https://johnthiriet.com/removing-async-void/) salvo dove non si ha altra scelta come in:
- Lifecycle method
- Event handler
- Delegate
- Lambda expressions
Quando non ho altra scelta (esempio un evento di `click` di un pulsante) refactorare da così:
```csharp
public async void OnPrepareButtonClick(object sender, EventArgs e)
{
    Button button = (Button)sender;

    button.IsEnabled = false;
    activityIndicator.IsRunning = true;

    var coffeeService = new CoffeeService();
    await coffeeService.PrepareCoffeeAsync();

    activityIndicator.IsRunning = false;
    button.IsEnabled = true;
}
```
a così
```csharp
public void OnPrepareButtonClick(object sender, EventArgs e)
{
    Button button = (Button)sender;
    _ = PrepareCoffeeAsync(button);
}

public async Task PrepareCoffeeAsync(Button button)
{
    try
    {
        button.IsEnabled = false;
        activityIndicator.IsRunning = true;
    
        var coffeeService = new CoffeeService();
        await coffeeService.PrepareCoffeeAsync();
    
        activityIndicator.IsRunning = false;
        button.IsEnabled = true;
    }
    catch (Exception ex)
    {
        // Do something
        System.Diagnostics.Debug.WriteLine(ex);
    }
}
```
o utilizzare il metodo `SafeFireAndForget` del pacchetto nuget `AsyncAwaitBestPractices` che permette di lanciare un task in background ma gestendo le sue eccezioni correttamente.

## `IAsyncEnumerable` per lo streaming di dati

La classe `IAsyncEnumerable<T>` è un'interfaccia che rappresenta una sequenza asincrona di elementi di tipo `T`: permette di fornire i risultati di operazioni IO lente (esempio chiamate API) mano a mano che arrivano senza aspettare che siano tutte pronte.
Permette di usare l'istruzione `await foreach` che itera in modo asincrono tale lista: **Permette di eseguire operazioni in streaming**: i dati vengono restituiti man mano che vengono elaborati.

Per esempio prendiamo questo codice che fa delle chiamate API per ottenere una lista di `StoryModel`:
```csharp
// EnumeratorCancellation passa automaticamente il token all'await foreach
async IAsyncEnumerable<StoryModel> GetTopStories([EnumeratorCancellation] CancellationToken token, int storyCount = int.MaxValue)
{
	// Dopo aver preso i topStoryId chiama il metodo GetStory con un task dedicato per ognuno di questi ma senza aspettarlo. Lo aspetterà nel Task.WhenEach
    var topStoryIds = await GetTopStoryIDs(token).ConfigureAwait(false);
    var getTopStoriesTasks = topStoryIds.Select(id => GetStory(id, token)).ToList();
    // Task.WhenEach fornisce un IAsyncEnumerable bloccante che si sblocca con un nuovo Task appena questo è completato. 
	await foreach (var topStoryTask in Task.WhenEach(getTopStoriesTasks).WithCancellation(token))
    {
        if (storyCount is 0)
            break;
    
        // Appena ha una nuova StoryModel fa lo yield al chiamante
        yield return await topStoryTask.ConfigureAwait(false);
    
        storyCount--;
    }
}
```
Posso ciclare il risultato di questo metodo con il `await foreach`

```csharp
await foreach (var story in GetTopStories(token, storyCount: StoriesConstants.NumberOfStories).ConfigureAwait(false))
{
	// So something with story
}
```

### Esempio di `IAsyncEnumerable<T>` Semplificato

In questo metodo vengono visualizzati i numeri da 1 a 10 a distanza di 500ms l'uno dall'altro con un effetto "streaming" o effetto "ChatGPT".
```csharp
public async IAsyncEnumerable<int> GenerateNumbers([EnumeratorCancellation] CancellationToken token)
{
    for (int i = 1; i <= 10; i++)
    {
        if (token.IsCancellationRequested)
            yield break; // Esce se viene richiesto l'annullamento

        await Task.Delay(500); // Simula un'operazione asincrona
        yield return i; // Restituisce il numero corrente
    }
}

// Metodo che consuma l'IAsyncEnumerable
public async Task ConsumeNumbers()
{
    using var cts = new CancellationTokenSource();
    
    try
    {
        await foreach (var number in GenerateNumbers(cts.Token))
        {
            Console.WriteLine($"Numero ricevuto: {number}");
        }
    }
    catch (OperationCanceledException)
    {
        Console.WriteLine("Operazione annullata.");
    }
}
```

## Evitare `return await`
Se in un metodo l'unico punto in cui uso `await` è nel `return`, posso evitare di dichiararlo `async` e restituire direttamente il `Task`, migliorando le prestazioni riducendo il context switch.
```csharp
// Da così
async Task<int> GetNumberAsync()  
{  
    return await Task.FromResult(42);  
}
// A così
Task<int> GetNumberAsync()  
{  
    return Task.FromResult(42); // Nessun async/await necessario  
}
```
Nota bene che se il `return` con `await` è dentro un `try/catch`, omettere `await` impedisce di intercettare le eccezioni.
```csharp
async Task<int> GetNumberWithExceptionAsync()  
{  
    try  
    {  
        return await SomeFailingTask(); // Necessario per catturare l'eccezione  
    }  
    catch (Exception ex)  
    {  
        Console.WriteLine($"Errore: {ex.Message}");  
    }  
}
```
## ValueTask

`ValueTask<T>` è una struttura (`struct`) introdotta per ridurre l'allocazione di oggetti quando si restituisce un valore asincrono. A differenza di `Task<T>`, che è una classe e quindi causa un'allocazione sulla heap, `ValueTask<T>` può evitare questa allocazione se il risultato è già disponibile.
Si usa quando l'**hot path** (il caso più frequente) di un metodo restituisce immediatamente un valore senza usare `await`. Questo evita la creazione inutile di un `Task<T>`.
### Esempio

```csharp
ValueTask<int> GetNumberAsync(bool fastPath)  
{  
    if (90percentMethodCall) // more often  
    {  
        return new ValueTask<int>(42); // Nessuna allocazione di Task  
    }  
    else  // less often
    {  
        return new ValueTask<int>(SomeAsyncOperation()); // Usa un Task solo se serve  
    }  
}
```

## IAsyncDisposable
L’interfaccia **IAsyncDisposable** è stata introdotta in C# 8 per consentire la dismissione asincrona delle risorse, offrendo un’alternativa a **IDisposable** quando la liberazione delle risorse richiede operazioni asincrone (ad esempio flush, chiusura di connessioni di rete, ecc.).
Quando una risorsa (per esempio uno stream) ha bisogno di eseguire operazioni di pulizia potenzialmente costose o bloccanti, eseguire la dismissione in modo asincrono evita di bloccare il thread chiamante.
1. **`await` viene eseguito alla fine del blocco `using`**  
    Quando si utilizza la sintassi `await using`, l’operazione di **DisposeAsync** (definita da IAsyncDisposable) viene invocata in modo asincrono una volta terminato il blocco `using`. In altre parole, l’“attesa” effettiva della dismissione avviene in chiusura del blocco.
2. **Si può aggiungere `ConfigureAwait(false)`**  
3. **Al momento, `CancellationToken` non è supportato**  
### Esempio
```csharp
await using (var fileStream = new FileStream(filePath, FileMode.OpenOrCreate)
                                .ConfigureAwait(false))
{
    // Operazioni sul file...
}
// Il "dispose" asincrono (await) viene atteso qui
```

## ExecutionContext
L'**ExecutionContext** è un concetto utilizzato per rappresentare tutte le informazioni riguardanti lo stato del programma tra più thread. In particolare:
1. **Memorizza dati specifici di un thread**, tra cui:
    - Informazioni di sicurezza (ad esempio, per l'impersonificazione).
    - Contesto di sincronizzazione.
    - Informazioni culturali (ad esempio, la localizzazione del thread).
2. **È associato a un Task**:
    - L'ExecutionContext viene **caricato nel thread** prima dell'esecuzione del Task.
3. **È immutabile**:
    - Una volta creato, non può essere modificato.
4. **Può essere soppresso**:
    - Tramite i metodi `ExecutionContext.SuppressFlow()` e `ExecutionContext.RestoreFlow()` si può controllare il flusso di propagazione dell'ExecutionContext.
## Note
* Ogni metodo `async` aggiunge circa 80 byte in quanto, in release, ogni metodo async diventa una `struct`. Questo è molto poco a meno di lavorare in condizioni particolari dove lo spazio è importante come sistemi embedded.
* Mai `.Result` o `.Wait()`: Sia `.Result` che `.Wait()` bloccheranno il thread corrente. Se il thread corrente è il **Main Thread** (noto anche come **UI Thread**), l'interfaccia utente si bloccherà fino al completamento del `Task`. Inoltre `.Result` e `.Wait()` rilanciano le eccezioni come `System.AggregateException`, rendendo più difficile individuare l'eccezione effettiva. Se vogliamo un codice sincrono usare `GetAwaiter().GetResult()` che è bloccante come sopra ma almeno non wrappa in `AggregateException`.
* Ogni volta che si sviluppa un metodo `async Task` è buona norma prevedere in ingresso un `CancellationToken` in modo che il chiamante possa avere modo di interrompere l'operazione asincrona.
* `.WaitAsync(token)`: permette di aggiungere la possibilità di cancellare un `Task` tramite un `CancellationToken` anche ai metodi che non lo supportano nativamente. Per i metodi che invece ritornano `IAsyncEnumerable` ho a disposizione l'extension `WithCancellation(token)` che fa la stessa cosa.
* Se devo lanciare un task "fire and forget", quindi senza nessuno che lo aspetta ma gestendo correttamente le eccezioni usare il metodo `SafeFireAndForget` del pacchetto nuget `AsyncAwaitBestPractices`
* `ConfigureAwait(false)`: indica che il codice seguente l'await non deve essere eseguito sul thread chiamante ma su un altro thread in background usando il `ThreadPool`. Ha senso metterlo ovunque tranne quando le operazioni seguenti all'`await` devono essere eseguite sul thread dell'interfaccia. Per esempio se scrivo con pattern MVVM, solo nelle View non avrò `ConfigureAwait(false)`, in tutte le altri classi lo avrò sempre. Sotto al cofano viene effettuato impostando `SynchronizationContext` a null: .NET non trovando un `SynchronizationContext` da utilizzare prenderà un nuovo thread.