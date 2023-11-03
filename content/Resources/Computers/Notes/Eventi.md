---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


## 1. Introduzione
I delegate vengono usati diffusamente per la gestione degli eventi, cioè quando voglio fare in modo che **una classe fornisca delle notifiche ai suoi utilizzatori**.

L'azione può essere **causata dall'utente**, ad esempio il clic su un pulsante oppure può essere **generata da un altro programma logico**, ad esempio modificare le proprietà di un valore.

La classe che invia (o genera) l'evento è chiamata *event sender* e le classi che ricevono (o gestiscono) l'evento sono chiamate *subscribers*.

Il mittente dell'evento non sa quale oggetto o metodo riceverà (dovrà gestire) gli eventi generati.

### 1.1 Come usare gli eventi
Ora, conosciamo i delegate come dei puntatori a funzione identificati univocamente dalla loro firma.

Pensiamo allo scopo degli eventi: vogliamo che un particolare codice venga eseguito quando accade qualcosa da qualche parte nel mio sistema.

Per fare questo, creiamo dei metodi specifici per il codice che vogliamo che venga eseguito.

**Il collante tra l'evento e il metodo sono i delegati: l'evento deve internamente memorizzare una lista di puntatori a funzioni da eseguire quando tale evento viene lanciato (aggiunti tramite il comando `+=`)**.

Ovviamente se vogliamo chiamare un metodo, dobbiamo sapere quali parametri passare a quest'ultimo!
Consideriamo **i delegate quindi come dei "contract" tra l'evento e i metodi che vengono chiamati**.

Quando dichiaro un evento con la parola chiave `event`, devo indicare come tipo un delegate, quindi la firma del metodo che deve essere chiamato al lancio dell'evento.

```csharp
//Definisco una firma che indica un metodo che
// prende in ingresso una string e ritorna void
public delegate void MyEventHandler(string foo);

//Definisco un evento, che ha come tipo il delegate
//indicato sopra
public event MyEventHandler SomethingHappened;

// Quando l'evento chiamato SomethingHappened viene lanciato,
// eseguo questo codice, che rispecchia la firma
// del delegate descritto sopra
protected virtual void OnSomethingHappened(string foo)
{
//Do some stuff
}

//Assegno un nuovo delegate che punta a OnSomethingHappened
// e lo aggiungo alla lista di eventi chiamata SomethingHappened
myObj.SomethingHappened += new MyEventHandler(OnSomethingHappened);
```

## 2.La parola chiave event
Per definire un evento, **utilizzare `event` nella firma del metodo che genera l'evento** e specificare il tipo di delegato questo ultimo.

In genere, per generare un evento, si aggiunge **un metodo contrassegnato come protected e virtual chiamandolo `OnEventName`**.

Il seguente esempio mostra come dichiarare un evento denominato `ThresholdReached`: l'evento viene associato al delegato con il `EventHandler` e viene generato in un metodo denominato `OnThresholdReached`.

```csharp
class Counter
{
public event EventHandler ThresholdReached;

protected virtual void OnThresholdReached(EventArgs e)
{
EventHandler handler = ThresholdReached;
if (handler != null)
{
handler(this, e);
}
}

// provide remaining implementation for the class
}
```

## 3. Utilizzare i delegate del .NET
Negli esempi precedenti non abiamo posto particolare attenzione sulla firma che deve avere il delegate; .NET consiglia di seguire però questo standard per la definizione dei delegate:

```csharp
delegate void MyEventHandler(object sender, EventArgs e);
```
quindi quando sollevo l'evento devo obbligatoriamente fornisce la classe che l'ha sollevato e degli argomenti di evento.

Il .NET fornisce un delegate apposito, chiamato `EventHandler`.

Il secondo argomento è un'istanza della classe `EventArgs`, si tratta di un tipo che non contiene aluna informazione ma la cui adozione è congliata per un requisito di forma che vedremo fra poco.

Il modo più semplice di valorizzarlo è tramite il suo campo statico `Empty`:

```csharp
myMethod(this, EventArgs.Empty)
```
Qualora volessimo fornire all'evento ulteriori informazioni di stato, conviene creare una classe personalizzata che derivi da `EventArgs` il cui nome convenzionalmente termina con tale suffisso.

```csharp
internal class ModeChangedEventArgs : EventArgs
{
public ImageLogSettingMode Mode;
public ModeChangedEventArgs(ImageLogSettingMode mode)
{
Mode = mode;
}
}
```
## 4. Esempio
Un esempio di gestione degli eventi è la classe `CameraWatchDog` di IMACore, che andiamo ad analizzare.

Il codice è ampiamente commentato.

```csharp
// metodo che ha la stessa firma del delegate del metodo (di standard, tutti i metodi di questo tipo hanno la stessa firma)
private void WatchDog_OnDisconnectionDetected(object sender, EventArgs e)
{
ThreadPool.QueueUserWorkItem(o =>{try{Reconnect();} catch (Exception){}});
}

// Creo una nuova istanza della classe
WatchDog = new CameraWatchDog(this);
// Fornisco alla classe il metodo da lanciare qualora vi sia una disconnessione alla camera
WatchDog.DisconnectionDetected += WatchDog_OnDisconnectionDetected;

/// <summary>
/// Strumento di monitoraggio della connessione ad una telecamera.

/// Si occupa di generare eventi nel caso in cui venga rilevata
/// una disconnessione dal dispositivo.

/// </summary>
public class CameraWatchDog
{
// Idea: voglio separare cioè che rileva che è succeso un particolare evento
// (in questo caso il fatto che il watchdog rilevi una disonnessione della camera)
// dall'implementazione effettiva delle procedure qualora vi sia tale disconnessione
// questo segue il pattern per cui separo il controllore, che rileva gli eventi,
// che potrebbe essere lo stesso per tutte le applicazioni, dalla gestione dell'evento stesso
// che invece può variare da applicazione ad applicazione.

// La classe CameraWatchDog non sa quello che succede qualora vi sia una disconnessione, lei si occupa
// solo di rilevarla

// Il delegate di gestione degli eventi ha sempre questa struttura, termina con EventHandler
// e ha come parametri in ingresso (object sender, EventArgs e)
public delegate void DisconnectionDetectedEventHandler(object sender, EventArgs e);

// Evento: ha sempre il tipo del delegate definito sopra.

// per aggiungere l'evento utilizzo il comando += su DisconnectionDetected
public event DisconnectionDetectedEventHandler DisconnectionDetected;

// Metodo che chiama il delegate associato all'evento, con un controllo
// preliminare sul fatto che questo sia stato correttamente definito
// anche questo metodo è standard, a meno di una ridefinizione di EventArgs
protected virtual void OnDisconnectionDetected()
{
DisconnectionDetected?.Invoke(this, EventArgs.Empty);
}

// Ciclo watchDog: metodo effetivo che rileva, in uqesto caso, che la camera si è disconnessa
// e conseguentemente lancia l'evento associato.

private void WatchCycle()
{
while (!_stopSignal.WaitOne(0))
{
if (!CameraWatched.IsOpen())
{
// lancia l'evento associato alla disconnessione della camera
OnDisconnectionDetected();
break;
}
WaitForPolling();
}
}
}

```