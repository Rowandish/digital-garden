---
tags:
  - Coding
  - CSharp
  - Memory
  - PublishedPosts
---


Questo articolo è una libera traduzione di [questa](http://stackoverflow.com/questions/538060/proper-use-of-the-idisposable-interface#) domanda di stackoverflow.

## 1. Introduzione
Il metodo `Dispose()`viene usato per **liberare risorse non più gestite che non possono essere rilevate dal [[Garbage Collector]]** (chiamate in inglese _unmanaged_, per maggiore chiarezza d'ora in poi userò questo termine).

E' importante sottolineare che il .NET possiede di garbage collector per l'eliminazione delle istanze di classi non più referenziate, analogamente al Java.

L'eliminazione delle risorse dalla memoria deve essere eseguito ad un certo punto del codice, altrimenti tali risorse rimarranno in RAM e potrebbero portare a dei [memory leak](https://it.wikipedia.org/wiki/Memory_leak).

## 2. Managed e unmanaged
Per capire la distinzione tra risorse *managed* e *unmanaged* basti pensare a questo:

- tutti i tipi di variabili che **si possono trovare in .NET** (quindi su MSDN) sono **managed**. Il GC conosce tutto di loro e può eliminarle in autonomia;
- tutti i tipi che invece **non si trovano su MSDN** sono **unmanaged**. Tutte le risorse che sono state create tramite chiamate di PInvoke (Platform Invocation Services) che quindi escono dal confortevole mondo dei tipi .NET è _unmanaged_ e, conseguentemente, si ha anche la responsabilità della loro eliminazione dalla memoria.

Assumiamo per esempio di avere una variabile di tipo `intPtr`. Il Garbage Collector non conosce come chiamare il metodo `DeleteHandle()` (che è il suo metodo tipico di eliminazione di oggetti), ne se chiamare o meno tale metodo.

## 3. L'interfaccia IDisposable
L'oggetto creato **deve** esporre un metodo che può essere chiamato dall'esterno che permette di eliminare questa risorsa **unmanaged**. Questo metodo è chiamato `Dispose()` e, per rendere più chiara la struttura del codice, esiste un'interfaccia, chiamata `IDisposable` che ha solo un metodo, il `Dipose()`.

```csharp
public interface IDisposable
{
void Dispose()
}
```
Esempio di implementazione del metodo `Dispose()`.

```csharp
public void Dispose()
{
Win32.DestroyHandle(this.CursorFileBitmapIconServiceHandle);
}
```

## 4. Dipose di oggetti managed
Assumiamo di lavorare con oggetti *managed*, per esempio una `System.Drawing.Bitmap`. Ora, questa può occupare anche, per esempio, 250MB di memora.

Ovviamente questo è un oggetto *managed* e quindi il GC prima o poi lo eliminerà.

Ora, davvero noi vogliamo che ci siano 250MB di memoria occupati per nulla, nell'attesa che eventualmente il GC arrivi e la liberi? Ovviamente no.

Il metodo `Dispose()` di un oggetto deve quindi eliminare

- le risorse *unmanaged* (perchè è obbligato a farlo)
- le risorse *managed* (perchè può essere utile per l'applicazione stessa)

Aggiorniamo il metodo `Dispose()`indicato sopra con l'eliminazione anche delle risorse _managed_, come una connessione a DB e un frame buffer.

```csharp
public void Dispose()
{
//Free unmanaged resources
Win32.DestroyHandle(this.CursorFileBitmapIconServiceHandle);

//Free managed resources too
if (this.databaseConnection != null)
{
this.databaseConnection.Dispose();
this.databaseConnection = null;
}
if (this.frameBufferImage != null)
{
this.frameBufferImage.Dispose();
this.frameBufferImage = null;
}
}
```

## 5. Il metodo Finalize()
Assumiamo ora che il programmatore **dimentichi** di chiamare il metodo `Dispose()` sull'oggetto che ho creato. Avrò un leak di risorse *unmanaged*, eventualità ovviamente da evitare!
Ovviamente le risorse *managed* verranno eliminate prima o poi dal GC, anche senza chiamare il metodo `Dispose()`, portando però alle problematiche descritte sopra.

Vorremo avere un modo per cui, quando il GC elimina il mio oggetto, **ne elimini anche le risorse unmanaged senza rendersene conto**.

Quando il GC elimina tutti gli oggetti managed, chiama il metodo `Finalize()` su ogni oggetto. Il GC non conosce il nostro metodo `Dispose()`.

++Per fare in modo che, quando il GC elimina le risorse *managed*, vengano eliminate anche le risorse *unmanaged* è l'override del metodo `Finalize()`++.

In C#, non devo esplicitamente fare un override del metodo `Finalize()`. Invece per fare ciò scrivo un metodo che **ha la stessa sintassi di un distruttore C++**, sarà il compilatore a tradurlo in un implementazione del metodo `Finalize()`.

Per esempio posso avere una situazione analoga (attenzione, l'esempio successivo ha un bug!)

```csharp
~MyObject()
{
//we're being finalized (i.e. destroyed), call Dispose in case the user forgot to
Dispose(); //<--Warning: subtle bug! Keep reading!
}
```
Il codice indicato sopra ha però un problema: come sappiamo, il GC lavora con un thread in background, conseguentemente non conosce l'ordine in cui due oggetti vengono distrutti.

Conseguentemente è possibile che, nel codice del mio `Dispose()` gli oggetti **managed** che sto cercando di eliminare siano a tutti gli effetti **già stati eliminati dal GC**.

Alle chiamate di:

```csharp
this.databaseConnection.Dispose();
```
o

```csharp
this.frameBufferImage.Dispose();
```
avrei un crash dell'applicazione, in quanto sto cercando di eliminare risorse che sono già state eliminate.

Conseguentemente devo avere un modo per cui il metodo `Finalize()` comunica al metodo `Dispose()` che questo **non deve toccare le risorse managed** in quanto **potrebbero** non essere più lì, mentre deve agire normalmente per le risorse *unmanaged*.

Il pattern standard per ottenere ciò è che sia il metodo `Finalize()` che il metodo `Dispose()` chiamino un terzo metodo con un parametro booleano che indica se è stato chiamato dal metodo `Dispose()` o dal metodo `Finalize()`.

E' prassi comune chiamare questo metodo con la seguente firma:

```csharp
protected void Dispose(Boolean disposing)
```
anche se sarebbe più esplicativo scrivere:

```csharp
protected void Dispose(Boolean itIsSafeToAlsoFreeManagedObjects)
```
Ottenendo quindi:

```csharp
public void Dispose()
{
Dispose(true); //I am calling you from Dispose, it's safe
}
```
e

```csharp
~MyObject()
{
Dispose(false); //I am *not* calling you from Dispose, it's *not* safe
}
```
N.b. Se sto facendo l'override di un metodo `Dispose()`della mia superclasse, devo ricordare di chiamare anche tale metodo:

```csharp
public Dispose()
{
try
{
Dispose(true); //true: safe to free managed resources
}
finally
{
base.Dispose();
}
}
```
## 6. Gestione del Garbage Collector
Per come abbiamo strutturato il codice, quando l'utente chiama il metodo `Dispose()`su un oggetto, ogni cosa viene eliminata dalla memoria.

Successivamente, quando arriva il Garbage Collector e chiama il metodo `Finalize()` verrà eseguita una ulteriore chiamata al metodo `Dispose()`
Questa modalità non solo è uno spreco di risorse, ma se il mio oggetto ha riferimenti ad oggeti che sono già stati eliminati dal'ultima chiamta del metodo `Dispose()` cercherò di eliminarli ancora!
Faccio notare che nel codice indicato sopra, ho la rimozione dei riferimenti ad oggetti eliminati:

```csharp
this.frameBufferImage.Dispose();
this.frameBufferImage = null;
```
conseguentemente non avrei questo bug, però qualora dimenticassi di assegnare a `null` la variabile avrei il problema.

Il modo per risolvere questo comportamento è **dire al Garbage collector** che non deve chiamare il metodo `Finalize()`di questo oggetto, in quanto le sue risorse sono già state eliminate in precedenza.

Questo comportamento è implementato grazie al metodo `GC.SuppressFinalize()`:

```csharp
public void Dispose()
{
Dispose(true); //I am calling you from Dispose, it's safe
GC.SuppressFinalize(this); //Hey, GC: don't bother calling finalize later
}
```
## 7. Perchè non liberare le risorse unmanaged nel Finalize()
In teoria io potre avere l'eliminazione delle risorse _unmanaged_ anche nel metodo `Finalize()` ma è sempre consigliabile usare il metodo `Dispose()`
Questo perchè il metodo `Finalize()`viene chiamato solo dal GC, e io non ho idea di quando questo opererà, mi affido alle sue tempistiche per l'eliminazione di oggeti che potrebbero potenzialmente portare a dei leak.

La documentazione di Object.Finalize è infatti chiara: il metodo `Finalize()`viene chiamato con tempistiche non deterministiche. per avere eliminazione a tempistiche note, è necessario avere un implementazione del metodo `Dispose()`di `IDisposable`.

## 8. Codice Finale
Di seguito indico il pattern completo dell'implementazione di una classe `IDisposable`.

```csharp
class BaseClass : IDisposable
{
// Flag: Has Dispose already been called?
bool disposed = false;

// Public implementation of Dispose pattern callable by consumers.
public void Dispose()
{ 
Dispose(true);
GC.SuppressFinalize(this); 
}

// Protected implementation of Dispose pattern.
protected virtual void Dispose(bool disposing)
{
if (disposed)
return; 

if (disposing) {
// Free any other managed objects here.
//
}

// Free any unmanaged objects here.
//
disposed = true;
}

~BaseClass()
{
Dispose(false);
}
}

```