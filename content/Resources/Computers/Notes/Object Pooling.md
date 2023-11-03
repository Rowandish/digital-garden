---
tags:
  - Coding
  - CSharp
  - Memory
---


## Introduzione

Analogamente all'[[Array Pooling]], l'Object Pooling ti permette di riutilizzare gli oggetti invece di crearne di nuovi ogni volta che ne hai bisogno al fine di ridurre la memoria allocata sullo [[heap]] e conseguentemente ridurre al pressione sul [[Garbage Collector]].

La classe `ObjectPool<T>` è una struttura di dati che ==mantiene un insieme di oggetti di un determinato tipo, pronti per essere riutilizzati==. Questo è particolarmente utile quando si lavora con oggetti la cui creazione, inizializzazione e distruzione sono costose in termini di tempo e memoria.

A differenza dell'`ArrayPool<T>` non è una classe presente nativamente in .NET ma è necessario implementarla in base alle proprie esigenze.

### Caratteristiche
- **Riduzione delle allocazioni di memoria**: Poiché gli oggetti vengono riutilizzati, si riduce la quantità di allocazioni di memoria sullo heap, riducendo la pressione sul GC e migliorando le prestazioni complessive dell'applicazione.
- **Flessibilità**: La classe `ObjectPool<T>` è generica e può essere utilizzata con qualsiasi tipo di oggetto, rendendola flessibile e adattabile a diverse situazioni.
- **Thread-safety**: La maggior parte delle implementazioni di `ObjectPool<T>` garantiscono la sicurezza nell'uso concorrente da parte di più thread, evitando potenziali problemi di sincronizzazione.

### Metodi principali

Le implementazioni della classe `ObjectPool<T>` solitamente forniscono i seguenti metodi:
-   `T Acquire()`: Preleva un oggetto disponibile dal pool. Se il pool è vuoto, viene creato un nuovo oggetto.
-   `void Release(T obj)`: Restituisce un oggetto al pool, rendendolo disponibile per un utilizzo futuro. Se questo oggetto ha uno stato questo deve essere resettato quando viene restituito.

## Esempio di implementazione
```csharp
public class ObjectPool<T> where T : new()
{
    private readonly ConcurrentQueue<T> _objects;
    private int _counter;

    public ObjectPool(int initialSize)
    {
        _objects = new ConcurrentQueue<T>();
        for (int i = 0; i < initialSize; i++)
	        _objects.Enqueue(new T());
	}
	public T Acquire()
	{
	    if (_objects.TryDequeue(out T obj))
	    {
	        return obj;
	    }
	
	    Interlocked.Increment(ref _counter);
	    return new T();
	}
	
	public void Release(T obj)
	{
	    _objects.Enqueue(obj);
	}
	
	public int Count => _counter;
}
```
Supponiamo di avere una classe `MyExpensiveObject` che rappresenta un oggetto con operazioni di creazione, inizializzazione e distruzione costose in termini di tempo e memoria. Possiamo utilizzare un `ObjectPool` per gestire tali oggetti:
```csharp
var pool = new ObjectPool<MyExpensiveObject>(5); // Crea un pool con 5 oggetti iniziali
// Acquisizione e utilizzo di un oggetto
var obj = pool.Acquire();
// ... Utilizzare 'obj' per eseguire operazioni
pool.Release(obj); // Rilasciare l'oggetto al pool per la successiva riutilizzazione
```

## Limiti

1. **Overhead di gestione**: La creazione, il mantenimento e l'utilizzo di un ObjectPool comportano un overhead aggiuntivo in termini di codice e complessità. Questo overhead potrebbe compensare i benefici delle prestazioni in alcuni scenari, soprattutto se il numero di allocazioni e deallocazioni di memoria è relativamente basso o se gli oggetti hanno un tempo di vita breve.
2. **Dimensione del pool e risorse inutilizzate**: La dimensione del pool deve essere scelta attentamente per bilanciare l'utilizzo delle risorse e le prestazioni. Un pool troppo grande potrebbe comportare un uso eccessivo di memoria a causa di risorse inutilizzate, mentre un pool troppo piccolo potrebbe non offrire i benefici desiderati in termini di riduzione delle allocazioni.
3. **Gestione dello stato degli oggetti**: Gli oggetti all'interno del pool potrebbero mantenere uno stato tra i vari utilizzi, il che potrebbe causare comportamenti inaspettati se non vengono ripristinati correttamente. È responsabilità del programmatore assicurarsi che lo stato degli oggetti sia resettato prima di essere rilasciato e riutilizzato.
4. **Thread-safety**: Se l'`ObjectPool` viene utilizzato in un contesto multithread, è necessario garantire la sicurezza nell'uso concorrente da parte di più thread.  È importante assicurarsi che l'implementazione utilizzata supporti la concorrenza o implementare meccanismi di sincronizzazione appropriati.
5. **Tempo di vita degli oggetti**: In alcuni casi, gli oggetti all'interno del pool potrebbero avere una durata più lunga di quanto sia effettivamente necessario. Ad esempio, un oggetto creato all'interno del pool potrebbe rimanere in memoria per l'intera durata dell'applicazione, anche se non viene più utilizzato. Questo può portare a un utilizzo inefficiente delle risorse e potenzialmente a problemi di memoria.