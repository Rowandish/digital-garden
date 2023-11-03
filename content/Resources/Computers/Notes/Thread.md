---
tags:
  - Coding
  - CSharp
  - Multithreading
  - PublishedPosts
---


La parte introduttiva e conclusiva di questo articolo proviene dal libro *C# 5*(ISBN 978-8820352530), la seconda parte invece dalla [documentazione ufficiale](https://msdn.microsoft.com/it-it/library/7a2f3ay4).

## 1. Introduzione
Quando richiediamo l'esecuzione di un programma, il sistema operativo crea **un'istanza di un particolare oggetto del kernel** chiamato **process**, a cui assegna un ben definito (e isolato) spazio di indirizzamento in memoria.

Un processo, di per sé, non è in grado di eseguire alcun codice e svolge il compito di puro e semplice **contenitore di quelle che potremmo definire come le entità funzionali elementari del sistema operativo: i thread**.

Ogni processo dispone di almeno un thread, chiamato **primary thread**, al termine del quale esso viene distrutto, liberando lo spazio di memoria e le risorse a esso assegnate.

Il normale ciclo di vita di un'applicazione consiste nell'**esecuzione sequenziale di numerosi blocchi di codice richiamati dal thread principale**, che a loro volta possono richiamare ulteriori blocchi di codice.

Quando questo avviene, il metodo chiamante risulta ovviamente bloccato fintanto che la routine invocata non giunge al termine: si tratta di un operazione non sempre percorribile in quanto appesantirebbe notevolmente l'utilizzo delle applicazioni.

Fortunatamente **ogni thread ha la possibilità di assegnare ad un thread secondario l'esecuzione di un metodo**; in questo caso, la chiamata a quest'ultimo ritorna immediatamente il controllo al thread chiamante e **i due blocchi di codice possono effettivamente essere eseguiti in parallelo**.

## 2. Esempio applicativo
La classe `System.Threading.Thread` viene usata per lavorare con i thread.

Quando un programma viene lanciato, viene creato automaticamente il corrispettivo thread principale, mentre i thread che vengono creati dallo sviluppatore tramite la classe Thread sono chiamati thread figli.

Nell'esempio riportato di seguito, viene illustrato come creare un thread parallelo ausiliario, da utilizzare per l'elaborazione in parallelo con il thread primario.

Vogliamo creare una classe chiamata `Worker` che contiene il metodo `DoWork` che verrà eseguito dal nostro thread di lavoro. Questo è essenzialmente la funzione Main del thread.

Quando verrà eseguito, il thread di lavoro chiamerà questo metodo e terminerà automaticamente quando il metodo verrà restituito.

```csharp
public void DoWork()
{
while (!_shouldStop)
{
Console.WriteLine("worker thread: working...");
}
Console.WriteLine("worker thread: terminating gracefully.");
}
```
La classe `Worker` contiene inoltre un altro metodo utilizzato per indicare che `DoWork` deve essere restituito, questo metodo, denominato `RequestStop`, è analogo al seguente

```csharp
public void RequestStop()
{
_shouldStop = true;
}
```
Il metodo `RequestStop` assegna semplicemente l'attributo `_shouldStop` a true.

Poiché questo attributo è controllato dal metodo `DoWork`, si ottiene l'effetto indiretto di causare la restituzione di `DoWork` terminando in questo modo il thread di lavoro.

È tuttavia importante tenere presente che **`DoWork` e `RequestStop` verranno eseguiti da thread differenti**.

`DoWork` viene eseguito dal thread di lavoro, mentre `RequestStop` viene eseguito dal thread primario, quindi **l'attributo `_shouldStop` viene dichiarato `volatile`**, come riportato di seguito

```csharp
private volatile bool _shouldStop;
```
La parola chiave `volatile` avvisa il compilatore che più thread accederanno al membro dati `_shouldStop` e che pertanto non deve formulare ipotesi di ottimizzazione sullo stato di questo membro.

**Il modificatore `volatile` è utilizzato in genere per un campo al quale accedono più thread senza ricorrere all'istruzione `lock` per la serializzazione dell'accesso**.

L'utilizzo di questo modificatore è così comodo perché _shouldStop è un valore bool. Se tuttavia questo membro dati fosse un oggetto complesso, l'accesso da più thread genererebbe un danneggiamento dei dati.

Prima di creare il thread di lavoro, la funzione `Main` crea un oggetto `Worker` e un'istanza di `Thread`.

L'oggetto thread viene configurato per utilizzare il metodo `Worker.DoWork` passando al costruttore `Thread` un riferimento a questo metodo, come riportato di seguito

```csharp
Worker workerObject = new Worker();
Thread workerThread = new Thread(workerObject.DoWork);
```
A questo punto, anche se l'oggetto thread esiste ed è configurato, questo non è ancora stato creato, per fare ciò è necessario lanciare il metodo `Start`

```csharp
workerThread.Start();
```
A questo punto **il sistema avvia l'esecuzione del thread di lavoro, ma in modo asincrono rispetto al thread primario**. La funzione `Main` continua infatti ad eseguire immediatamente il codice mentre il thread di lavoro viene sottoposto contemporaneamente a inizializzazione.

Per evitare che `Main` tenti di terminare il thread di lavoro prima che venga eseguito, la funzione `Main` esegue un ciclo finché la proprietà `IsAlive` dell'oggetto thread di lavoro non viene impostata su true:

```csharp
while (!workerThread.IsAlive);
```
Successivamente il thread primario viene interrotto brevemente con una chiamata a `Sleep`.

In questo modo la funzione `DoWork` del thread di lavoro eseguirà il ciclo all'interno del metodo `DoWork` per alcune iterazioni prima che la funzione `Main` esegua altri comandi

```csharp
Thread.Sleep(1);
```
Trascorso un millisecondo, `Main` segnala all'oggetto thread di lavoro che deve terminare utilizzando il metodo `Worker.RequestStop` descritto in precedenza

```csharp
workerObject.RequestStop();
```
È inoltre possibile terminare un thread da un altro thread utilizzando una chiamata a `Abort`. In questo modo il thread interessato viene **terminato in modo forzato** anche se non ha completato l'attività e non consente la pulitura delle risorse.

Infine la funzione `Main` chiama il metodo `Join` sull'oggetto thread di lavoro. 
Tramite questo metodo **il thread corrente si blocca oppure attende finché non termina il thread rappresentato dall'oggetto**.

Pertanto `Join` non verrà restituito finché non viene terminato, il thread di lavoro

```csharp
workerThread.Join();
```
Il metodo Join accetta come parametro anche un timeout, che rappresenta il tempo massimo di attesa al termine del quale proseguire con l'applicazione.

Di seguito è riportato l'esempio completo.

```csharp
using System;
using System.Threading;

public class Worker
{
// Questo metodo viene passato a costruttore come delegato
// alla inizializzazione della classe Thread
public void DoWork()
{
while (!_shouldStop)
{
Console.WriteLine("worker thread: working...");
}
Console.WriteLine("worker thread: terminating gracefully.");
}
public void RequestStop()
{
_shouldStop = true;
}
// Volatile permette di evitare il lock su attributi booleani
// che vengono acceduti da più thread
private volatile bool _shouldStop;
}

public class WorkerThrea[[DEX]]ample
{
static void Main()
{
Worker workerObject = new Worker();
Thread workerThread = new Thread(workerObject.DoWork);

workerThread.Start();
Console.WriteLine("main thread: Starting worker thread...");

// Aspetta fino a che il thread non viene ativato
while (!workerThread.IsAlive);

// Aspetto 1ms in modo che il worker faccia qualcosa
Thread.Sleep(1);

workerObject.RequestStop();

// Blocco il thread corrente fino a che il worker
// non viene terminato con successo
workerThread.Join();
Console.WriteLine("main thread: Worker thread has terminated.");
}
}
```
L'output di questo programma è il seguente

```csharp
main thread: starting worker thread...

worker thread: working...

worker thread: working...

worker thread: working...

worker thread: working...

worker thread: working...

worker thread: working...

worker thread: working...

worker thread: working...

worker thread: working...

worker thread: working...

worker thread: working...

worker thread: terminating gracefully...

main thread: worker thread has terminated
```

## 3. Il [[ThreadPool]]

## 4. Modello di programmazione asincrono
Il comando **`BeginInvoke` permette di eseguire delegate in maniera asincrona**, in quanto questo ritorna immediatamente il controllo al thread chiamante e parallelamente fa partire il codice del delegato.

Internamente il `BeginInvoke` utilizza il threadPool del CLR.

Ci sono due fondamentali differenze tra usare questo metodo e le classi `Thread` o `ThreadPool` illustrate in precedenza:

- **il passaggio di parametri al metodo asincrono avviene in maniera tipizzata**, mentre con Thread o ThreadPool l'eventale parametro è sempre object;
- i delegate risultano particolarmente** comodi per intercettare il termine dell'elaborazione parallela** e, in particolare, per recuperare il risultato.

Esistono tre diverse modalità per gestire l'esecuzione parallela e recuperarne il risultato, descritte di seguito.

### 4.1 Utilizzo del metodo EndInvoke
Insieme al metodo `BeingInvoke` indicato in precedenza, ogni delegato espone anche il metodo `EndInvoke` che può essere utilizzato per **attendere la conslusione dell'operazione asincrona e recuperarne il risultato.**
`BeginInvoke` restituisce un oggetto `IAsyncResult` che può essere utilizzato per monitorare l'avanzamento della chiamata asincrona ed inoltre viene passato come parametro al metodo `EndInvoke`.

**`EndInvoke` blocca effetivamente in thread in esecuzione fino al termine dell'operazione asincrona, consentendoci quindi di sincronizzare i due thread**.

Qualora il delegate preveda un valore di ritorno, `EndInvoke` lo restituisce come output.

### 4.2 Utilizzo di `IAsyncResult` e polling
Il metodo `BeginInvoke` restituisce un oggetto che implementa l'interfaccia di tipo `IAsyncResult`.

La proprietà più importante di questo oggetto è `AsyncWaitHandle` che restituisce un oggetto di tipo `WaitHandle`, analogo al `ManualResetEvent` indicato in precedenza.

Tramite questo metodo è possibile implementare un algoritmo di polling per verificare quando un thread ha concluso il suo lavoro nel seguente modo

```csharp
while(!asyncResult.isCompleted)
{
asyncResult.AsyncWaitHandle.WaitOne(200);
}
```

### 4.3 Utilizzare un metodo di callback
In alcune occasioni vi è la necessità di **evitare che sia il metodo chiamante a gestire il termine del thread**; in questo caso possiamo configurare il delegate in modo che **esegua un metodo di callback**, passando il metodo come secondo parametro al `BeginInvoke`.

La firma del metodo di callback deve rispettare quella del delegate `AsyncCalback`, quindi deve ritornare `void` e prendere come unico parametro in ingresso un oggetto di tipo `IAsyncResult`.

## 5. Operazioni cross-thread con Windows Form

### 5.1 Problema
Accedere a dei controlli *Windows Forms* (quindi andare a eseguire operazioni nel thread di gestione dell'I/O) non è intrinsecamente thread-safe, infatti potrei avere delle inconsistenze nei dati o perfino dei deadlock.
E' insicuro chiamare un controllo da un thread che non sia colui che ha creato e gestisce il controllo, senza usare il metodo `BeginInvoke`.
Nell'esempio seguente ho una chiamata non thread safe:
```vb
'Quando clicco un pulsante creo un thread che chiama un controllo Windows Form in modo insicuro
Private Sub setTextUnsafeBtn_Click(ByVal sender As Object, ByVal e As EventArgs) Handles setTextUnsafeBtn.Click
Me.demoThread = New Thread(New ThreadStart(AddressOf Me.ThreadProcUnsafe))
Me.demoThread.Start()
End Sub

' Effettuo una modifica all'I/O da un thread esterno
Private Sub ThreadProcUnsafe()
Me.textBox1.Text = "This text was set unsafely."
End Sub
```
Il debugger .NET rileva queste situazioni lanciando un eccezione `InvalidOperationException` con il messaggio:
```vb
Control control name accessed from a thread other than the thread it was created on.
```

### 5.2 Soluzione
Per chiamare un controllo *Windows Form* in modo thread-safe devo effettuare i seguenti controlli:

1. Controllare la proprietà `InvokeRequired` della classe
2. Se `InvokeRequired` ritorna **true**, chiamare il metodo `BeginInvoke` con un delegate con la stessa firma del metodo attuale
3. Se `InvokeRequired` ritorna **false**, chiamare il metodo direttamente

```vb
'Quando clicco un pulsante creo un thread che chiama un controllo Windows Form in modo, questa volta, sicuro
Private Sub setTextUnsafeBtn_Click(ByVal sender As Object, ByVal e As EventArgs) Handles setTextUnsafeBtn.Click
Me.demoThread = New Thread(New ThreadStart(AddressOf Me.ThreadProcUnsafe))
Me.demoThread.Start()
End Sub

' Effettuo una modifica all'I/O da un thread esterno
Private Sub ThreadProcUnsafe()
Me.SetText("This text was set safely.")
End Sub

Delegate Sub SetTextDelegate(text As String)

Private Sub SetText(ByVal text As String)
If Me.textBox1.InvokeRequired Then
Me.BeginInvoke(New SetTextDelegate(AddressOf SetText), New Object() {text})
Else
Me.textBox1.Text = text
End If
End Sub
```

`InvokeRequired` compara il *thread ID* del thread chiamante con il *thread ID* del thread corrente: se questi thread sono differenti ritorna `True`.
Se `InvokeRequired` ritorna `True` sto quindi facendo una chiamata cross-thread: in questo caso il metodo crea una nuova istanza del delagate che permette di autochiamarsi in modo asincrono dal thread corretto.


## 6. Tips generici
Questo articolo è una libera traduzione di [questo blog post](http://blog.goyello.com/2014/01/21/threading-in-c-7-things-you-should-always-remember-about/)

### 6.1 I thread condividono le variabili se hanno una reference comune all'istanza dello stesso oggetto
Consideriamo il seguente esempio:
```csharp
class SomeClass
{
private bool _isWorkDone;
static void Main(string[] args)
{
SomeClass someClass = new SomeClass();
// Passso il metodo dell'istanza someClass
Thread newThread = new Thread(someClass.DoWork);
newThread.Start();
// Chiamo il metodo dalla stessa istanza del thread
someClass.DoWork();
Console.Read();
}
void DoWork()
{
if (!_isWorkDone)
{
_isWorkDone = true;
Console.WriteLine("Work done");
}
}
}
```
Il risultato di questo codice è la scritta "_Work done_" sullo schermo.
Come si può vedere dal codice, il metodo `DoWork()` viene chiamato da entrambi i thread a partire dalla stessa istanza di `SomeClass`: come risultato, dato che il campo `_isWorkDone` non è statico, questo viene condiviso dai due thread.
Conseguentemente, "_Work done_" viene printato a schermo una volta sola.

### 6.2 Il blocco finally nei thread in background non viene eseguito quando il processo termina
Consideriamo il seguente esempio:
```csharp
class SomeClass
{
static void Main(string[] args)
{
SomeClass someClass = new SomeClass();
Thread backgroundThread = new Thread(someClass.DoWork);
backgroundThread.Start();
Console.WriteLine("Closing the program....");
}
void DoWork()
{
try
{
Console.WriteLine("Doing some work...");
Thread.Sleep(1000);
}
finally
{
Console.WriteLine("This should be always executed");
}
}
}
```
Questo codice fornisce:
```
Doing some work...
Closing the program...
```
Questo esempio dimostra come quando il thread principale termina la sua esecuzione, il campo `finally` del thread in background non viene eseguito.
Non considerare questa eccezione può portare numero di problemi quando ho lavori di dispose() nel blocco finally di un thread, che non verrebbero lanciati portando, in questo caso, a dei memory leak difficili da individuare

### 6.3 I valori trovati da lambda espressioni sono anch'essi condivisi
Consideriamo il seguente codice:
```csharp
class SomeClass
{
static void Main(string[] args)
{
for (int i = 0; i &lt; 10; i++)
{
Thread thread = new Thread(()=> Console.Write(i));
thread.Start();
}
Console.Read();
}
}
```
Noi ci aspettiamo un risultato come 0123456789.
Il risultato ottenuto è invece assolutamente non deterministico!
Il trucco è che la variabile i si riferisce alla stessa locazione di memoria della variabile iterata nell'`for`, che quindi continua a cambiare.
La soluzione è utilizzare una variabile temporanea:
```csharp
for (int i = 0; i<= 10; i++)
{
int temp = i ;
Thread thread = new Thread(()=> Console.Write(temp));
thread.Start();
}
```
### 6.4 Un thread non è influenzato dalla presenza di un try catch esterno alla sua creazione
Consideriamo il seguente codice:
```csharp
class SomeClass
{
static void Main(string[] args)
{
try
{
Thread thread = new Thread( ()=&gt; Divide(10,0));
thread.Start();
}
catch (Exception ex)
{
Console.WriteLine("An exception occured");
}
}
static void Divide(int x, int y)
{
int z = x / y;
}
}
```
L'eccezione di divisione per zero non verrà catturata dal catch del `main`, ma rimarrà `ncaught` portando allo spegnimento del programma.
Il modo migliore per risolvere questa cosa è banalmente spostare il blocco `try catch` all'interno del metodo del thread.

## [[ManualResetEvent]]
