---
tags:
  - Coding
  - CSharp
  - Memory
  - PublishedPosts
---
## Introduzione

[SemaphoreSlim](https://docs.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim?view=net-6.0) è una classe che permette la sincronizzazione di _n_ thread che hanno una risorsa (scarsa) condivisa limitandone l'uso ad un numero massimo.

Questa classe può essere utile nel caso in cui abbia un metodo che richiede della potenza computazionale o di rete (`HttpClient`, gestione DBMS) a cui voglio limitare l'accesso a _n_ thread e non di più.

Di fatto è un [[ManualResetEvent]] che gestisce l'accesso ad un metodo ad _n_ thread invece che a solo uno.

Per capire facciamo un esempio: un `SemaphoreSlim` è come una scatola che contiene *n* chiavi per accedere al bagno.
Se la scatola è vuota significa che tutte le chiavi sono prese e di conseguenza bisogna aspettare che qualcuno esca dal bagno per mettere una chiave nella scatola (metodo `Release()`). Quando definisco un `SemaphoreSlim` a costruttore passo il numero di chiavi che sono presenti inizialmente nella scatola.

## Sintassi

La sintassi è molto semplice: a costruttore indico il numero di thread che possono accedere alla risorsa contemporaneamente, con la il metodo `WaitAsync` blocco il thread se ho finito il numero di "biglietti" disponibili oppure entra acquisendo un "biglietto" e infine con `Release` rilascio la risorsa (rendo disponibile il mio "biglietto" a qualcun altro).
```Csharp
_semaphore = new _semaphore = new(5);
await _semaphore.WaitAsync();
_semaphore.Release();
```
## Esempio

In questo esempio creo 100 task che effettuano delle eventuali operazioni lunghe di durata casuale impostando a 5 il numero massimo di task che possono accedere al metodo contemporaneamente.
```csharp
/// <summary>
///     Dichiaro il semaforo con 5 "biglietti": solo 5 task contemporaneamente possono accere al metodo prima di essere
///     bloccati.
/// </summary>
private readonly SemaphoreSlim _semaphore = new(5);

/// <summary>
///     Lancio i 100 task
/// </summary>
public void Run()
{
    Task.WaitAll(CallLongTasks().ToArray());
}

/// <summary>
///     100 task chiamano tutti il metodo <see cref="LongMethod" />. Non voglio però che più di 5 ci possano accedere
///     contemporanemanete.
/// </summary>
private IEnumerable<Task> CallLongTasks()
{
    for (var i = 0; i < 100; i++)
        yield return LongMethod(i);
}

/// <summary>
///     Questo metodo non può essere eseguito da più di 5 task contemporaneamente.
/// </summary>
private async Task LongMethod(int value)
{
    try
    {
        // Attendo che si liberi un posto
        await _semaphore.WaitAsync();
        Console.WriteLine($"{DateTime.Now.ToString("h:mm:ss:ffff")} Inizio task {value}");
        // Operazione lunga: impiega un tempo casuale da 0 a 10 secondi
        await Task.Delay(new Random().Next(10_000));
        // Ho terminato l'operazione complessa, posso rilasciare il mio biglietto a qualcun altro.
        _semaphore.Release();

        Console.WriteLine($"{DateTime.Now.ToString("h:mm:ss:ffff")} - Task {value} completato!");
    }
    catch (Exception e)
    {
        Console.WriteLine(e.Message);
    }
}
```
Output:
```
3:39:26:3210 Inizio task 0
3:39:26:9517 Inizio task 1
3:39:27:0623 Inizio task 2
3:39:27:0904 Inizio task 3
3:39:27:1363 Inizio task 4
3:39:29:0305 - Task 0 completato!
3:39:29:0307 - Task 3 completato!
3:39:29:0355 Inizio task 6
3:39:29:0379 Inizio task 5
3:39:29:4648 - Task 4 completato!
.......
.......
3:41:04:8495 Inizio task 99
3:41:06:1380 - Task 99 completato!
3:41:08:3384 - Task 93 completato!
3:41:09:0626 - Task 96 completato!
3:41:12:0472 - Task 97 completato!
3:41:14:3705 - Task 98 completato!
```
Come si vede i primi 5 task partono in contemporanea mentre gli altri aspettano che qualcuno finisca.

## SemaphoreSlim vs Semaphore

Dato che esiste anche la classe `Semaphore` è interessante capirne la differenza.

La classe `SemaphoreSlim` si basa su [[SpinWait]] e Monitor, quindi il thread prova prima ad acquisire il lock senza context switch (per approfondire vedi [[Blocking vs Spinning]] e [[ManualResetEvent vs ManualResetEventSlim]] se non ci riesce entro poco tempo viene effettuato un context switch passando la passando la palla al sistema operativo.

Quando quest'ultimo assegnerà uno slot di tempo al task verrà riprovato ad acquisire il lock tramite spinning.

Questa modalità è molto performante quando nella maggior parte dei casi non devo aspettare il lock: in questo modo non ho alcun context switch per il wait e il risultato è molto performante.
