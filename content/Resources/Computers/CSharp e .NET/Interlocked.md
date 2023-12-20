---
tags:
  - Coding
  - CSharp
  - Multithreading
  - PublishedPosts
---
La sincronizzazione dei thread è un elemento fondamentale nella programmazione asincrona, ne ho infatti parlato [[in vari post]].

La soluzione più versatile è sicuramente utilizzare il costrutto `[[lock]]` ma, in alcuni casi, l'utilizzo dei metodi della classe `Interlocked` permette di ottenere performance decisamente migliori.

Questa classe permette di eseguire operazioni atomiche semplici per variabili condivise da più thread: in particolare permette di effettuare somme o sottrazioni o di effettuare degli assegnamenti anche condizionali.

Essendo operazioni atomiche non c'è alcuna possibilità che un thread legga e modifichi una variabile mentre la sto modificando tramite un metodo `Interlocked`.

Dato che sto lavorando a passo livello sulle celle di memoria in tutti i metodi di `Interlocked` devo passare il sempre riferimento alla variabile (keyword `ref`).

## Add, Increment, Decrement

La classe `Interlocked` possiede i metodi `Add` per sommare una quantità ad una variabile in modo atomico, `Increment` e `Decrement` per aumentare o diminuire di 1 rispettivamente.
```Csharp
Interlocked.Add(ref value, 1);
Interlocked.Increment(ref value);
Interlocked.Decrement(ref value);
```
### Performance

Andiamo ad analizzare le performance del metodo Add confrontandolo con il rispettivo metodo con il lock utilizzando il fido [BenchmarkDotNet](https://benchmarkdotnet.org/articles/overview.html).
```CSharp
[MemoryDiagnoser]
public class InterlockedTest
{
    private readonly object _synclock = new();
    private const int Iteration = 100_000;
    private int _interlockedValue;
    private int _lockValue;
    
    [Benchmark]
    public int AddWithNoSync()
    {
        Parallel.For(0, Iteration, i =>
        {
            _lockValue+=i;
        });
        return _lockValue;
    }
    
    [Benchmark]
    public int AddWithInterlocked()
    {
        Parallel.For(0, Iteration, i =>
        {
            Interlocked.Add(ref _interlockedValue, i);
        });
        return _interlockedValue;
    }
    
    [Benchmark]
    public int AddWithLock()
    {
        Parallel.For(0, Iteration, i =>
        {
            lock (_synclock)
                _lockValue+=i;
        });
        return _lockValue;
    }
}
```
Ecco i risultati:

|             Method |       Mean |      Error |    StdDev | Allocated |
|------------------- |-----------:|-----------:|----------:|----------:|
|      AddWithNoSync |   662.5 us |   337.9 us |  18.52 us |      3 KB |
| AddWithInterlocked | 3,231.2 us |   990.1 us |  54.27 us |      3 KB |
|        AddWithLock | 8,687.8 us | 8,888.4 us | 487.20 us |      3 KB |

Utilizzando il metodo Add ho un boost di prestazioni di 2x rispetto all'utilizzo di un normale lock.

## Exchange

Il metodo `Exchange` permette di assegnare un valore ad una variabile, è un assegnamento atomico thread safe.
```Csharp
Interlocked.Exchange(ref value, 10);
```
## CompareExchange

Questo metodo racchiude una condizione e un assegnamento nella stessa istruzione (_compare-and-swap_), il tutto in modo ovviamente atomico.

Se il valore della variabile è uguale a quello del terzo argomento, modificalo a quello del secondo argomento e ritorna poi il valore originale.
```Csharp
var i = 5;
var output = Interlocked.CompareExchange(ref i, 10, 5);
```
è equivalente a
```Csharp
if (i == 5)
            i = 10;
var output = 5;
```
**Questo metodo utilizza direttamente istruzioni assembly per confrontare e swappare il contenuto di due indirizzi di memoria, il tutto quindi a bassissimo livello.**

La funzione di uguaglianza che viene utilizzata è il confronto diretto in memoria, senza alcuna equality function customizzabile dall'utente.

### CompareExchange pattern

Un utilizzo classico di `CompareExchange` è aggiornare una property di una classe in modo thread-safe senza utilizzare lock.

Assumiamo quindi di avere il field `field` che vogliamo modificare con il metodo `f(field)`; il problema è che mentre chiamiamo f(field) qualche altro thread potrebbe modificare field, portando quindi a race condition e bug critici gravi.
```Csharp
// Utilizzo una variabile di appoggio cachedField per poter capire se qualcuno ha modificato field
var cachedField;
var newValueFromField;
do
{
  // Faccio puntare cachedField allo stesso indirizzo in memoria di field
  cachedField = field;
  // Calcolo newValueFromField in base a field. Questa è l'istruzione che voglio rendere thread-safe
  newValueFromField = f(field);
}
// Confronto field con cachedField. In teoria è uguale ma qualcuno potrebbe averlo modificato nel frattempo.
// Se è stato modificato il risultato di CompareExchange è diverso da cachedField quindi non modifico field a newValueFromField e riprovo con il while; in caso contrario effettuo la modifica e esco
while (cachedField != Interlocked.CompareExchange(ref field, newValueFromField, cachedField));
```
## Perché interlocked è così veloce?

Vi sono tre tipologie di costrutti di sincronizzazione in C#:

- **User-mode**: utilizzano istruzioni a basso livello della CPU per coordinare i threads. Dato che utilizza l'hardware questi costrutti sono i più veloci. Esempi sono `volatile` e `Interlocked`.
- **Kernel-mode**: utilizzano il sistema operativo e posso avere quindi vari context-switch tra codice managed, codice user-mode e codice nativo kernel-mode. Tutti questi context switch possono influire negativamente sulle performance. Esempi sono `Semaphore` e `Mutex`.
- **Costrutti ibridi**: sono veloci come i costrutti user-mode se non c'è concorrenza ma c'è uno switch in kernel-mode qualora più thread cerchino di accedere alla stessa risorsa lo stesso tempo. Esempi sono `Monitor`, `SemaphoreSlim`, `ReaderWriterLockSlim`.

Interlocked è un costrutto _user-mode_, il costrutto lock invece viene modificato direttamente dal compilatore con:
```Csharp
object obj = new object();
object obj2 = obj;
bool lockTaken = false;
try
{
    Monitor.Enter(obj2, ref lockTaken);
}
finally
{
    if (lockTaken)
    {
        Monitor.Exit(obj2);
    }
}
```
che quindi utilizza il costrutto ibrido `Monitor`: in caso di multipli thread passa a kernel-mode influenzando così le sue performance.

## Conclusione

Quando si ha la necessità di sincronizzare dovremo sempre prima capire se è possibile utilizzare `Interlocked`: in caso affermativo il suo utilizzo porta ad un notevole miglioramento di prestazioni.

E' comunque importante sottolineare che non tutto quanto può essere fatto con un `lock` può essere fatto con `Interlocked`; per cui è sempre necessario capire quale è la soluzione migliore per ogni caso.
