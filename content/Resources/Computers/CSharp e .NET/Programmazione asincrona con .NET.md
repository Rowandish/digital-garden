---
tags:
  - Coding
  - CSharp
  - Multithreading
  - PublishedPosts
---
## 1. Introduzione
La programmazione asincrona viene spesso utilizzata nei progetto web per evitare colli di bottiglia e migliorare l'usabilità dell'applicazione in generale.
Spesso però tale tipo di programmazione risulta più complessa di quella tradizionale sincrona, pertanto risulta più difficile sia il debug che la gestione effettiva.
Con **.NET 4.5** è stato introdotto un approccio semplificato alla programmazione asincrona, in modo che sia il compilatore a fare quello che prima faceva il programmatore.
Le parole chiave della programmazione asincrona in C# .NET sono **async** e **await**. Tramite queste due parole chiave, è possibile utilizzare le risorse di .NET Framework o di Windows Runtime per **creare un metodo asincrono con la stessa facilità con cui è possibile creare un metodo sincrono**.

## 2. Caratteristiche di un metodo asincrono
Di seguito indichiamo un esempio di un metodo asincrono (come da documentazione), indicandone successivamente la caratteristiche.
```csharp
// Tre cose da notare nella firma del metodo
// - Presenza del modificatore asyn
// - The return type is Task or Task<T>, in questo caso Task<int>
// - Il nome del metodo termina con "Async"
async Task<int> AccessTheWebAsync()
{ 
	// GetStringAsync ritorna un Task<string>. Questo significa che quando il processo sarà terminato, avrò una stringa
	Task<string> getStringTask = new HttpClient().GetStringAsync("http://msdn.microsoft.com");
	
	// Parallelamente al processo di reperimento della stringa getStringTask, posso eseguire dell'altro
	DoOtherIndependentWork();
	
	// L'operatore await ferma l'esecuzione del metodo fino a che non ho ottenuto la string getStringTask.
	// Mentre il metodo "aspetta£, il controllo del codice passa al chiamante di AccessTheWebAsync e ritorna qui quando la stringa getStringTask è arrivata correttamente
	string urlContents = await getStringTask;
	
	// Una volta ottenuta la stringa, posso fornirne la sua lunghezza, come se fosse un normale metodo sincrono
	return urlContents.Length;
}
```
Spesso non ho alcuna operazione che intercorre tra la chiamata di `GetStringAsync` e il suo completamento, posso quindi semplificare il codice chiamando l'istruzione singola seguente e rimanendo in attesa.
```csharp
string urlContents = await client.GetStringAsync();
```
Le seguenti caratteristiche riepilogano gli aspetti che rendono l'esempio precedente un metodo asincrono.

- La firma del metodo **include un modificatore async**;
- Il nome di un metodo asincrono termina per convenzione con un suffisso `Async;
- Il tipo di valore restituito è uno dei seguenti:
  - `Task<TResult>` se nel metodo è presente un'istruzione return in cui l'operando è di tipo `TResult.
  - `Task` se nel metodo non è presente un'istruzione return oppure è presente un'istruzione return senza l'operando.
  - `Void` se si sta scrivendo un gestore eventi asincrono.
- Il metodo include in genere almeno un'espressione **await**, che contrassegna **un punto in cui il metodo non può continuare fino a quando l'operazione asincrona attesa non sia completata. Nel frattempo, il metodo viene sospeso e il controllo ritorna al chiamante del metodo**.

## 3. Thread
I metodi **asincroni vengono considerati operazioni non bloccanti. Un'espressione await in un metodo asincrono non blocca il thread corrente quando l'attività attesa è in esecuzione**. Al contrario, l'espressione registra il resto del metodo come continuazione e restituisce il controllo al chiamante del metodo asincrono.

## 4. La classe Task
La classe `Task` rappresenta una singola operazione che non restituisce un valore e che in genere viene eseguita in modo asincrono.
Un'istanza della classe *Task* può essere creata in molti modi; l'approccio più comune consiste nel chiamare il metodo statico *Run*, che consiste nell'avviare un'attività utilizzando i valori predefiniti senza parametri addizionali.

## 5. Valori di ritorno
Come indicato sopra un metodo **async** può ritornare `Task<T>`, `Task` e `void`; di seguito indico le differenze tra i tre.

### 5.1 `Task<T>`
Caratterizza un metodo **async** che può essere aspettato e che, quando il task è completo, fornisce una variabile di tipo **T**.

### 5.2 `Task`
Caratterizza un metodo **async** che può essere aspettato e che, quando il task è completo, è schedulata una continuazione del task.

Viene utilizzato quando non ho un valore di ritorno ma il chiamante vuole avere la possibilità di aspettare che il `Task` sia completo.

### 5.3 `void`
Un metodo async che ritorna void **non può essere aspettato**, in quanto è un metodo di tipo "fire and forget". Questo metodo funziona sì in maniera asincrona, ma non ho alcun modo di sapere quando ha finito.
Tipicamente un metodo asyn void viene utilizzato quando voglio creare un **gestore di eventi asincrono**: quando l'evento viene catturato, l'handler corrispettivo viene lanciato, ma nessuno sta aspettando il **Task** ottenuto dal gestore di eventi in quanto questo tipicamente non ne ritorna alcuno.
Tipicamente un metodo asincrono void è il "_top-level_" di un'operazione asincrona, nel senso che i metodi _Task_ spesso sono chiamati da un metodo *async void*.