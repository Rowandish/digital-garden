Un `ManualResetEvent` viene utilizzato per poter lanciare segnali tra thread diversi, in particolare server per notificare a uno o più thread in attesa che si è verificato un evento.

## Creazione
Un `ManualResetEvent` mantiene internamente una variabile booleana, quando la variabile è **false** questo blocca tutti i thread (che sono in attesa utilizzando il metodo `WaitOne()`, quando viene impostata a **true** invece permette a chi è in attesa di procedere.
Al costruttore nel `ManualResetEvent` viene indicato il suo stato iniziale, tipicamente **false** (quindi bloccante)

```csharp
ManualResetEvent manualResetEvent = new ManualResetEvent(false);
```

### WaitOne
Il metodo `WaitOne()` blocca il thread corrente fino a che un altro thread non invii un segnale di sblocco, ritorna quindi **true** se riceve un segnale, **false** altrimenti.

```
manualResetEvent.WaitOne();
```

E' possibile inoltre indicare un tempo massimo di attesa per il segnale, utilizzando un overload del metodo:

```csharp
bool isSignalled = manualResetEvent.WaitOne(TimeSpan.FromSeconds(5));
```

Se il `manualResetEvent` non riceve un segnale entro 5 secondi, la variabile `isSignalled` viene impostata a `false`.

#### WaitOne(0)
`WaitOne(0)` non aspetta alcun segnale, rimane bloccante fino a che la variabile interna è false e appena diventa true si sblocca.
Viene utilizzato per autosincronizzare un singolo thread (vedi esempio).


### Set
Il metodo `Set()` viene utilizzato per inviare un segnale a tutti i thread che stanno aspettando; questo viene impostato settando la variabile booleana interna a true. Tutti i thread aspettanti sono sbloccati e possono procedere.

```csharp
manualResetEvent.Set();
```

### Reset
Una volta chiamato il metodo `Set()` sull'oggetto `manualResetEvent`, il suo valore booleano rimane a true. Per resettare il suo valore al valore iniziale (`false`) possiamo utilizzare il metodo `Reset()`.

```csharp
manualResetEvent.Reset();
```
Se vogliamo inviare un segnale tra thread più volte è indispensabile chiamare il metodo `Reset`.

### Esempio
Nella `Stazione.cs` voglio un segnale per il fermo del ciclo che mi permette di uscire dal ciclo macchina a richiesta.
Creo il seguente `ManualResetEvent`:
```csharp
protected ManualResetEvent StopCicloSignal = new ManualResetEvent(false);
```
Nella funzione `Ciclo()` inserisco il seguente codice:
```csharp
if (!StopCicloSignal.IsValid() || StopCicloSignal.WaitOne(0))
{
  return false;
}
```
Questo codice mi permette di uscire dalla funzione qualora `StopCicloSignal` diventi `true`, quindi quando qualcuno (in questo caso internamente) chiami la funzione `StopCicloSignal.Set()`.
Questo è il metodo StopCiclo() che infatti effettua
```csharp
StopCicloSignal.Set();
```
interrompendo così (non istantaneamente ma appena il codice arriva al controllo sul while) il ciclo.

### Esempio 2
```csharp
private ManualResetEvent _tryToLoadInProgress;
public LatestRejectionUi(MultiLanguage lang) : base(lang)
{
_tryToLoadInProgress = new ManualResetEvent(false);
}
private bool TryToLoadImage()
{
_tryToLoadInProgress.Set();
// Codice complesso che deve essere acceduto da un thread alla volta
_tryToLoadInProgress.Reset();
}
private void HandleTimer(object sender, ElapsedEventArgs e)
{
if (_tryToLoadInProgress.WaitOne(0))
return;
TryToLoadImage()
}
```