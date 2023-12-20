Nello sviluppo di un'applicazione multithreading dobbiamo tenere presente che:

- ogni [[Thread]] consuma risorse di sistema ed impiega una certa quantità di memoria
- la creazione e la distruzione di un thread sono, in generale, operazioni onerose

Per limitare questi inconvenienti posso **evitare di distruggere un thread ogni volta che questi abbia terminato l'esecuzione di mantenerlo attivo per un certo periodo di tempo in stato *idle***, in modo che possa essere riutilizzato in seguito.

Il CLR mette a disposizione un contenitore, chiamato `ThreadPool`, all'interno del quale **mantiene la lista di thread attivi** e tramite il quale permette di **gestire le code dei task** che vengono ad esso via via assegnati.

La classe statica `ThreadPool` espone il metodo `QueueUserWorkItem`, che accetta un delegate di tipo `WaitCallback`, tramite il quale possiamo accodare un nuovo task da gestire in parallelo.

Sottolineo che la **sincronizzazione dei task eseguiti in questo modo è implicita e non richiede alcun accorgimento di codice**: non essendo disponibile alcuna istanza di `Thread`, non è possibile usare il metodo `Join` per poterne attendere la conclusione.

Allo scopo, possiamo utilizzare la classe [[ManualResetEvent]].

```csharp
public class Example {
public static void Main() {
// Inserisco il metodo nel ThreadPool,
// questo viene fatto partire automaticamente
//senza l'utilizzo di Start,
// e termina senza l'utilizzo di Join
ThreadPool.QueueUserWorkItem(new WaitCallback(ThreadProc));

Console.WriteLine("Main thread does some work, then sleeps.");
// Inserisco uno Sleep in quanto, altrimenti,
// il programa (quindi il main thread) terminerebbe,
// portando ad un abort anche di tutti i suoi thread figli
Thread.Sleep(1000);

Console.WriteLine("Main thread exits.");
}

// This thread procedure performs the task.

static void ThreadProc(Object stateInfo) {
Console.WriteLine("Hello from the thread pool.");
}
}
// L'output dell'applicazione sarà il seguente:
// Main thread does some work, then sleeps.

// Hello from the thread pool.

// Main thread exits.
```
