---
tags:
  - Coding
  - CSharp
  - Memory
  - ImagoLearning
Date: 2023-05-22
Done: true
---
La Lazy Initialization è una tecnica di programmazione che consiste nell'==assegnare un valore a un oggetto solo quando è effettivamente necessario, ritardando la sua inizializzazione fino al momento in cui viene effettivamente utilizzato==.
Lo scopo è principalmente ridurre lo startup time di un programma (qualora si tratti di oggetti da creare sempre) o, in generale, ridurre il consumo di memoria  quando si lavora con oggetti di grandi dimensioni o costosi in termini di risorse qualora questi non servono in tutti i casi.
La memoria inoltre viene effettivamente risparmiata nel caso in cui l'oggetto non venga mai utilizzato, altrimenti il consumo vi è allo stesso modo ma "ritardato".

## Vantaggi

1. **Riduzione del consumo di memoria**: Non vengono allocate risorse per gli oggetti non utilizzati, risparmiando memoria.
2. **Miglioramento delle prestazioni**: L'allocazione e l'inizializzazione degli oggetti avviene solo quando è effettivamente necessario, riducendo il tempo di avvio dell'applicazione.
4. **Scalabilità**: La Lazy Initialization può migliorare la scalabilità di un'applicazione, in quanto riduce il carico iniziale di risorse.

## Limiti

1. **Overhead aggiuntivo**: La classe `Lazy<T>` aggiunge un livello di astrazione, il che potrebbe causare un lieve overhead di prestazioni.
2. **Performance**: chiamare la property `.Value` di un oggetto `Lazy` è comunque più lento di chiamare l'oggetto stesso
3. **Complessità del codice**: La Lazy Initialization può rendere il codice più complesso e difficile da gestire, in particolare se è necessario garantire la sincronizzazione tra thread.
4. **Non adatto per scenari multi-thread**: Sebbene la classe `Lazy<T>` supporti la sincronizzazione dei thread, potrebbe essere meno efficiente rispetto all'inizializzazione anticipata in scenari multi-thread ad alta concorrenza.
5. **Potenziali problemi di temporizzazione**: La Lazy Initialization può causare problemi di temporizzazione se un oggetto viene inizializzato in un momento inaspettato o critico dell'esecuzione dell'applicazione.
6. **Difficoltà nel debugging**: La Lazy Initialization può rendere il debugging più difficile, poiché l'inizializzazione degli oggetti avviene solo in determinati momenti, e potrebbe essere complicato individuare eventuali errori o eccezioni legate all'inizializzazione.

## Esempio 
Immaginiamo di avere un'applicazione che richiede l'accesso a un database remoto per recuperare alcuni dati. L'inizializzazione della connessione al database potrebbe richiedere tempo e risorse significativi, soprattutto se si considerano le operazioni di rete coinvolte. In una situazione in cui non si sa con certezza se l'applicazione avrà effettivamente bisogno di accedere al database, l'utilizzo della classe Lazy può essere molto utile.

Inizializzare la connessione al database solo quando viene effettivamente richiesto potrebbe migliorare le prestazioni dell'applicazione e ridurre l'uso delle risorse del sistema. Utilizzando la classe Lazy, possiamo ritardare l'inizializzazione della connessione fino al momento in cui viene richiesta la prima operazione di accesso al database. In questo modo, se l'applicazione non ha bisogno di accedere al database durante l'esecuzione, non sarà mai creata una connessione e non verranno sprecate risorse di sistema.

## C\#
In C#, è possibile utilizzare la classe `Lazy<T>` del namespace `System` per implementare la Lazy Initialization.
Il metodo principale è la property `Value` che permette di inizializzare l'oggetto, se non è mai stato fatto, oppure ritornare l'istanza se è già stata costruita in precedenza.
L'utilizzo è molto semplice:
```csharp
// Utilizzo di Lazy Initialization per l'oggetto 'MyExpensiveObject'
Lazy<MyExpensiveObject> lazyObject = new Lazy<MyExpensiveObject>();
MyExpensiveObject expensiveObject = lazyObject.Value;
```
La classe fornisce anche un costruttore per creare l'oggetto tramite factory `new Lazy<T>(Func<T> valueFactory)` e una property booleana `IsValueCreated` per sapere se è stato mai costruito l'oggetto.

### Multi-threading
La classe Lazy permette di configurarne il comportamento di creazione qualora venga utilizzati in scenari multi-thread.
Queste configurazioni influiscono solo sulla creazione, l'accesso alla variabile interna è invece sempre thread-safe.

#### `isThreadSafe`
A costruttore posso passare il parametro `isThreadSafe` che, se impostato a true, circonda di un lock la creazione dell'oggetto.
Vediamo esplicitamente i due casi:
* `isThreadSafe: false`: il metodo per creare il valore creerà semplicemente il valore, lo imposterà nella memoria interna e restituirà il valore.
* `isThreadSafe: true`: la creazione verrà racchiusa all'interno di un `lock`, impedendo a più di un thread di creare l'oggetto.

#### `LazyThreadSafetyMode Enum`

A costruttore posso definire il comportamento della classe `Lazy` in scenari multi-thread tramite l'enum `LazyThreadSafetyMode`.
Questo può avere tre modalità:
1.  `None`: Indica che non sono previste misure di sicurezza del thread. Questa modalità è la meno costosa in termini di prestazioni, ma non è thread-safe. Questo è il comportamento di default.
2.  `PublicationOnly`: Con questa modalità non ho lock sulla creazione dell'oggetto, conseguentemente ci può essere la creazione simultanea di più di un valore interno ma poi la classe utilizzerà un `Interlocked.CompareExchange` internamente per assicurarsi che il valore del primo oggetto creato completamente sia quello utilizzato per l'oggetto.
3.  `ExecutionAndPublication`: Indica che la creazione e l'inizializzazione dell'oggetto sono thread-safe (circondata da `lock`, analogo a `isThreadSafe=true`).



### Esempio
In questo esempio, l'oggetto `MyExpensiveObject` viene inizializzato (quindi ne viene chiamato il costruttore) solo quando si accede alla proprietà `Value` dell'oggetto `lazyObject`. Successivamente, il valore viene messo in una cache all'interno dell'oggetto `Lazy<T>` stesso in modo che, nelle chiamate successive alla proprietà `.Value`, verrà restituito il valore memorizzato senza ulteriori chiamate al costruttore.

Questo permette di ridurre la memoria utilizzata sullo [[heap]], in quanto l'oggetto `MyExpensiveObject` verrà allocato e inizializzato solo quando è effettivamente necessario.

```csharp
// Utilizzo di Lazy Initialization per l'oggetto 'MyExpensiveObject'
Lazy<MyExpensiveObject> lazyObject = new Lazy<MyExpensiveObject>();

Console.WriteLine("Lazy object creato.");

// L'oggetto verrà inizializzato solo quando lo richiediamo esplicitamente
Console.WriteLine("Premi un tasto per inizializzare l'oggetto.");
Console.ReadKey();

MyExpensiveObject expensiveObject = lazyObject.Value;

Console.WriteLine("Oggetto inizializzato e pronto per l'uso.");

Console.WriteLine("Premi un tasto per accedere nuovamente all'oggetto.");
Console.ReadKey();
MyExpensiveObject expensiveObject2 = lazyObject.Value;
Console.WriteLine("Oggetto già inizializzato, nessuna nuova inizializzazione.\n");

class MyExpensiveObject
{
    public MyExpensiveObject()
    {
        Console.WriteLine("Inizializzazione dell'oggetto MyExpensiveObject...");
        // Simulazione di un'operazione costosa
        System.Threading.Thread.Sleep(2000);
        Console.WriteLine("Inizializzazione completata.");
    }
}
```

### Esempio 2
In questo caso utilizzo la classe Lazy per definire una Regex come field ma senza occupare la memoria nell'inizializzazione, qualora esistano scenari in cui questa non mi serve.
```csharp
private static Lazy<Regex> colorBlockRegEx = new Lazy<Regex>(
            ()=>  new Regex("VERY_COMPLEX_REGEX"));
```

### Test completo
I file di test si trovano in `RowandishAwesomeWiki` progetto `Various` e classe `LazyTest`. Vi sono anche dei benchmark con la classe `LazyMemoryBenchmark`.