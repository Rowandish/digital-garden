---
tags:
  - Coding
  - CSharp
  - Multithreading
  - PublishedPosts
---
## 1. Introduzione
La parola chiave `lock` **contrassegna un blocco di istruzioni come sezione critica ottenendo il lock a mutua esclusione**. L'esempio seguente illustra un'istruzione lock.
La parola chiave `lock` **impedisce a un thread di entrare in una sezione critica del codice se è già presente un altro thread**. Se un altro thread tenta di accedere a un codice bloccato, **attenderà (in stato di blocco) finché l'oggetto non verrà rilasciato**.
Tipicamente un istruzione `lock` segue questo template:
```csharp
private readonly static object obj = new Object();

lock (obj)
{
// thread unsafe code
}
```
che può essere anche utilizzato black box, senza comprendere il funzionamento interno, ma con la certezza che **il codice inserito all'interno del blocco lock verrà acceduto da un thread alla volta, portandolo a diventare thread-safe**.

## 2. La classe Monitor
Il codice indicato sopra viene tradotto dal compilatore di C# 4.0 nel seguente codice:
```csharp
bool lockWasTaken = false;
var temp = obj;
try
{
Monitor.Enter(temp, ref lockWasTaken);
// body
}
finally
{
if (lockWasTaken)
{
Monitor.Exit(temp);
}
}
```
Per citare la documentazione ufficiale, il metodo `Enter` di `Monitor` permette di acquisire **l'esclusività di accesso sull'oggetto passato come parametro**.
Se un altro thread ha eseguito un `Enter` sullo stesso oggetto in precedenza ma non lo ha ancora rilasciato tramite il metodo `Exit`, **il thread corrente verrà verrà fermato fino a che l'altro thread non rilascerà l'oggetto**.
Il metodo `Monitor.Enter` indica al thread di aspettare anche all'infinito una risorsa, senza andare mai in timeout.

## 3. Il parametro in ingresso a lock
Il metodo lock prevede un parametro in ingresso, che spesso viene definito come un `new object()`.
Questo perché **l'oggetto che viene passato come parametro serve solo come chiave**: se un `lock` è già stato preso sulla stessa chiave, un ulteriore `lock` non può essere fatto, altrimenti il lock è permesso.
Questo è il motivo per cui è sbagliato usare le stringhe come chiavi del metodo lock, in quanto queste sono oggetti immutabili e inoltre sono accessibili da altre parti dell'applicazione.
E' necessario invece **usare una variabile privata generica, come, per esempio, un istanza della classe `Object`**.

### 3.1 Non usare lock(this)
E' una pratica di cattiva programmazione utilizzare `lock(this)` per bloccare l'esecuzione di codice perché generalmente è fuori dal controllo del programmatore chi altro potrebbe stare eseguendo un lock su tale oggetto.
Infatti, ogni codice che possiede un riferimento all'oggetto `this` in questione, può eseguirne un lock senza che il programmatore di tale oggetto ne venga a conoscenza. Questo aumenta la complessità di soluzioni multi-thread e può modificarne la loro correttezza.
