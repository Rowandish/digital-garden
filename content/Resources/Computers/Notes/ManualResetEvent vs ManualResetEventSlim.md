---
tags:
  - Coding
  - CSharp
  - Multithreading
  - PublishedPosts
---


Dal .NET 4 è stato introdotto un nuovo tipo di [[ManualResetEvent]] chiamato `ManualResetEventSlim` che permette di avere delle performance migliori qualora il tempo di blocco atteso sia molto breve.

Questo miglioramento viene effettuato effettuando dello spinning per un determinato numero di operazioni prima di effettuare il _context switch_ e passare al _blocking_.

Permette, inoltre, di cancellare un `Wait` utilizzando un `CancellationToken`, cosa impossibile con i classici `ManualResetEvent`.

La classe permette o a costruttore o mediante la property `SpinCount` di impostare il numero di spin da effettuare prima di effettuare un vero block.

## Utilizzo

L'utilizzo di un `ManualResetEventSlim` è estremamente simile al suo simile `ManualResetEvent`, le differenze sono le seguenti:

- Il metodo `WaitOne()` dei `ManualResetEvent` è stato rinominato in `Wait()` che ha in ingresso, oltre ad un timeout in ms, anche un `TimeSpan` o un `Cancellation[[Token]]`.
- Presenta una property get-only `IsSet` che permette di sapere se è stato o meno settato (di fatto analoga a `WaitOne(0)`)

## Chi preferire?

Dal libro [C# 9.0 in a Nutshell](https://amzn.to/3w43nN5) leggo che `ManualResetEventSlim` può essere fino a 50 volte più veloce in scenari dove l'attesa è minima in quanto non vi è alcun passaggio al sistema operativo.

Per capire quanto deve essere minima questa attesa ho creato il seguente [benchmark](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwifmsX4k8T2AhXEh_0HHYazBV4QFnoECA8QAQ&url=https%3A%2F%2Fbenchmarkdotnet.org%2FOverview.htm&usg=AOvVaw2upcZg99TGvZYc6ZLSgot-):
```Csharp
[ShortRunJob]
public class ManualResetEventTest
{
    [Params(0, 1, 10)]
    public int MillisecondsSleep;

    [Benchmark]
    public void ManualResetEventSlim()
    {
        using var mres = new ManualResetEventSlim(false);
        var t = Task.Run(() =>
        {
            mres.Wait();
        });

        Thread.Sleep(MillisecondsSleep);
        mres.Set();
        t.Wait();
    }
    
    [Benchmark]
    public void ManualResetEvent()
    {
        using var mres = new ManualResetEvent(false);
        var t = Task.Run(() =>
        {
            mres.WaitOne();
        });

        Thread.Sleep(MillisecondsSleep);
        mres.Set();
        t.Wait();
    }
}
```
Che porta ai seguenti risultati:

![[immagine.png]]

Come si può notare quando il tempo di attesa è maggiore o uguale a 1ms i due metodi si equivalgono. La differenza sostanziale si ha quando ho un tempo di sleep di 0ms (quindi un solo context switch senza ulteriori attese) dove ho un miglioramento di performance di 6x.

Per rimuovere l'overhead della creazione dei task ho pensato a questo ulteriore benchmark:
```csharp
[Benchmark]
public void ManualResetEventSlimSetWait()
{
    using var mres = new ManualResetEventSlim(false);
    mres.Set();
    mres.Wait();
}

[Benchmark]
public void ManualResetEventSetWait()
{
    using var mres = new ManualResetEvent(false);
    mres.Set();
    mres.WaitOne();
}
```
In questo esempio al momento del wait il `ManualResetEvent` è già stato impostato a true, di fatto non ho quindi alcuna attesa.

I risultati sono i seguenti:

![[immagine-1.png]]

Il `ManualResetEventSlim` , qualora il semaforo sia già stato settato, è decisamente più veloce; stiamo parlando di circa 2 ordini di grandezza.

## Conclusioni

Nella stragrande maggioranza dei casi utilizzare un `ManualResetEvent` è più che sufficiente, la differenza di performance è trascurabile.

Ha senso utilizzare il `ManualResetEventSlim` in caso eventi dove spesso l'attesa è nulla (è già stato effettuato un `Set()`) oppure inferiore a 1ms.
