---
tags:
  - Coding
  - CSharp
  - Multithreading
  - PublishedPosts
---
Capire come [[sincronizzazione dei thread in C#]] è indispensabile per poter costruire applicazioni veloci e thread-safe; e in questo contesto è necessario avere chiara la differenza tra blocking e spinning.

Spesso può essere utile mettere in pausa un Thread in modo da aspettare che una determinata condizione avvenga, per ottenere questo ci sono due modi: il blocking e lo spinning.

**Tl;Dr**: il blocking rilascia il processore in modo che esso possa dedicarsi ad altri thread, mentre lo spinning lancia un loop che tiene il processore occupato sul thread corrente.

## Yielding e context switch

Un Thread bloccato **restituisce subito la sua gestione al processore** e non consuma più risorse fino a che la condizione non è stata rispettata.

Per fare queste operazioni quando un Thread si blocca o si sblocca il sistema operativo opera quello definito come _context switch_ che porta un overhead di qualche microsecondo.

Lo yielding di un thread è l'operazione per cui un thread informa lo scheduler che esso rilascia la slot di tempo assegnata, sarà il sistema operativo a scegliere a quale thread passare. Se non ho alcun thread rimarrò nel thread corrente.

In C# lo yielding può essere chiamato esplicitamente con l'istruzione `Thread.Yield()`.

## Blocking

Il modo più comune è il _blocking_ che consiste nel fermare un thread nell'attesa di un segnale (_signaling)_ o che si liberi una risorsa (_locking_).

Esempi di classi per il _signaling_ sono i [[ManualResetEvent]] o [`AutoResetEvent`](https://docs.microsoft.com/it-it/dotnet/api/system.threading.autoresetevent?view=net-6.0), poi ci sono anche classi secondarie come il [`Countdownevent`](https://docs.microsoft.com/it-it/dotnet/api/system.threading.countdownevent?view=net-6.0) o [`Barrier`](https://docs.microsoft.com/it-it/dotnet/api/system.threading.barrier?view=net-6.0), entrambi introdotti in .NET 4.

Il costrutto principale per il _locking_ invece è appunto il `lock` che permette di ottenere accesso esclusivo ad un metodo bloccando tutti gli altri fino che questo ultimo non viene rilasciato.

Alternative al lock sono la classe [`Mutex`](https://docs.microsoft.com/it-it/dotnet/api/system.threading.mutex?view=net-6.0) e la classe [`Semaphore`](https://docs.microsoft.com/it-it/dotnet/api/system.threading.semaphore?view=net-6.0).

## Spinning

Lo spinning è invece la modalità di blocco di un thread per cui questo rimane **bloccato in una attività CPU intensive senza alcun _context switch_**.

L'esempio classico nel blocco con spinning è un ciclo `while` senza corpo, per esempio:
```csharp
while (!condition);
```
Questo tipo di blocco è estremamente CPU-intensive in quanto la CLR (e conseguentemente il sistema operativo) continuano a effettuare calcoli e controlli alla massima velocità possibile.

Spesso infatti si utilizza un ibrido tra blocking e spinning utilizzando qualcosa come:
```csharp
while (!condition) Thread.Sleep(10);
```
che è sicuramente più efficiente dello spinning puro, anche se esteticamente non è il massimo…

## Chi preferire?

Lo spinning può essere migliore del blocking quando mi aspetto che una condizione sia verificata subito (nell'ordine di microsecondi) in quando evito l'overhead e la latenza del _context switch_ necessario ai metodi _blocking_.

In tutti gli altri il _blocking_ è da preferire.
