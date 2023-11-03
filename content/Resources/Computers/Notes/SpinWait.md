---
tags:
  - Coding
  - CSharp
  - Multithreading
---


Lo struct `SpinWait` permette di mettere in pausa un Thread utilizzando lo spinning, quindi facendogli fare del lavoro inutile in loop.

Effettuando un wait con spinning usando un classico `while`
```csharp
while (!condition);
```
può portare a numerosi problemi:

- Il thread consumerà tutti i core della CPU fino a che `condition` non sarà `true`;
- Gli altri Thread dell'applicazione rallenteranno (_starvation_);
- Perfino il Thread che dovrà mettere `condition` a `true` rallenterà, portando ad un loop di rallentamento orribile (chiamato priority inversion);
- In caso di CPU single core la priority inversion è pressoché certa.

La struct `SpinWait` risolve questi problemi in due modi:

- Limita il numero di spinning CPU intensive ad un massimo numero di iterazioni: dopo aver raggiunto tale numero massimo fa lo _yield_ del _time slice_ a lui assegnato utilizzando `Thread.Sleep` o `Thread.Yield` (ricordo che il thread scheduler del sistema operativo assegna dei _time slice_ ad ogni thread e rapidamente continua a cambiare l'esecuzione, aumento inoltre il parallelismo in base al numero di CPU a disposizione);
- Rileva se sta lavorando su una CPU single core e in quel caso fa lo `yield` ad ogni ciclo.

`SpinWait` si può utilizzare con la sua classe statica in questo modo:
```csharp
SpinWait.SpinUntil(() => myPredicate(), 1000)
```
che di fatto aspetta che `myPredicate()` diventi true per al massimo 1000 ms.

Aspettare facendo spinning per 1000ms non ha senso, potrebbe essere una idea più interessante provare lo spinning per, esempio, 10ms e successivamente un `Thread.sleep` classico.

Una alternativa è utilizzare il metodo `SpinOnce()` all'interno di un `while` che esce su una determinata `condition`
```csharp
var sw = new SpinWait();
while (!condition)
{
    sw.SpinOnce();
}
```
Oppure è possibile utilizzare la property `NextSpinWillYield` per poter essere intenzionale nel block:
```csharp
private void SpinBeforeBlocking()
{
    var wait = new SpinWait();
    while (!_condition)
    {
        // Utilizzando questa property posso sapere se sono arrivato al numero massimo di spin disponibili e il prossimo spin farà uno yielding
        if (wait.NextSpinWillYield)
        {
            /* block! */
        }
        else
        {
            wait.SpinOnce();
        }
    }
}
```
E' estremamente interessante e ben commentato il [codice ufficiale di Microsoft](https://referencesource.microsoft.com/#mscorlib/system/threading/SpinWait.cs), quindi consiglio di darci una letta.