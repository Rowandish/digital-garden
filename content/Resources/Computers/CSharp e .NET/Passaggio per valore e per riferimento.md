---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


## Introduzione

In questo articolo approfondisco una parte fondamentale della programmazione: **il passaggio di parametri**, con particolare riferimento al linguaggio C#.

In molti linguaggi, soprattutto compilati, è possibile passare argomenti a parametri di funzioni **per valore o per riferimento**.

Questo articolo è una parziale traduzione di un vecchio articolo di Jon Skeet che si trovava in [qui](http://www.yoda.arachsys.com/csharp/) e ora si può reperire solo [su WebArchive](https://web.archive.org/web/20180219053344/http://www.yoda.arachsys.com/csharp/parameters.html); questo mio lavoro servirà quindi anche come backup per il futuro.

La conoscenza di questa differenza e la sua padronanza è indispensabile per una buona programmazione.

Un ottimo esempio della differenza tra i due l'ho trovata spiegata in [questa domanda di StackOverflow](http://stackoverflow.com/questions/373419/whats-the-difference-between-passing-by-reference-vs-passing-by-value): assumiamo che io voglia condividere una pagina web con te: se ti fornisco l'url della pagina sto facendo un passaggio per riferimento, infatti se la pagina cambia entrambi vediamo gli stessi cambiamenti. Qualora tu elimini l’url non stai eliminando la pagina in se, ma solo il modo che tu hai per accedere a tale pagina.

Se invece stampo la pagina su un foglio e te lo fornisco, allora sto effettuando un passaggio per valore: la tua pagina è disconnessa dall'originale, le modifiche che tu effettui o che vengono effettuate sull'originale, non vengono rilevate.

## Tipi di variabile: referenza e valore

In C# esistono due insiemi di tipi di variabili: i _tipi per referenza_ e i _tipi per valore_.

### Tipi per referenza (reference types)

Un tipo per referenza è un tipo che **ha come valore il riferimento ai dati invece che i dati stessi**. Per esempio, consideriamo il codice seguente:
```CSharp
StringBuilder sb = new StringBuilder();
```
In questa riga di codice abbiamo dichiarato una variabile `sb`, creato un nuovo oggetto `StringBuilder` e assegnato a sb un riferimento a tale oggetto.

Il valore di `sb` non è l'oggetto stesso, ma la sua referenza, come si può capire dall'esempio seguente:
```CSharp
StringBuilder first = new StringBuilder();
first.Append("hello");
StringBuilder second = first; // second è un puntatore alla stessa area di memoria di first
first.Append(" world");
Console.WriteLine(second); // Scrive ciò a cui punta first, cioè "hello world"
```
E’ importante sottolineare che le due variabili `first` e `second` sono variabili indipendenti, se first puntasse a una nuova area di memoria second punterebbe ancora alla vecchia area di first, come si vede da questo esempio:
```CSharp
StringBuilder first = new StringBuilder();
first.Append("hello");
StringBuilder second = first;
first.Append(" world");
first = new StringBuilder("goodbye"); // ora first punta ad un nuova area di memoria
Console.WriteLine(first); // Prints goodbye // quindi scrive "goodbye"
Console.WriteLine(second); // Still prints hello world // second punta ancora all'area di memoria originale e conseguentemente scrive "hello world"
```
### Tipi per valore (value types)

**Le variabili di tipo per valore contengono direttamente i dati** e non c'è quindi un livello intermedio di puntatore -> dati. L'assegnamento di una variabile di questo tipo presuppone che **tutti i dati vengano copiati**.

Per esempio, consideriamo la seguente _struct_:
```CSharp
public struct IntHolder
{
    public int i;
}
```
Quando lavoro con una variabile di tipo `IntHolder`, questa contiene tutti i dati (nel caso seguente un valore intero). Un assegnamento copia il valore, slegandolo dalla variabile iniziale
```CSharp
IntHolder first = new IntHolder();
first.i = 5;
IntHolder second = first; // second punta ad una nuova area di memoria contenente tutti i dati di first
first.i = 6;
// La linea seguente scrive "5", non è influenzata dalla modifica
Console.WriteLine (second.i);
```
Tutti i tipi semplici, compresi gli _struct_ e gli _enum_ (ma non _string_) sono tipi per valore.

Il tipo `string` è un tipo particolare in quanto spesso si comporta come se fosse un tipo per valore invece è un tipo per referenza a tutti gli effetti. Questi tipi di oggetti sono detti _tipi immutabili_, che significa che una volta che è stata creata un'istanza di questi, non può più essere cambiata. Questo permette ad un tipo per referenza di comportarsi in maniera simile ad un tipo per valore in quanto posso passarlo a dei metodi black box ed essere sicuro che questi non ne possano cambiare il valore.

## Le tipologie di passaggio di parametri

In C# esistono quattro differenti tipologie di parametri:

-   **value parameters**: default;
-   **reference parameters**: parola chiave **ref**;
-   **output parameters**: parola chiave **out**;
-   **array parameters**: parola chiave **params**.

Per un approfondimento sui parametri di metodo vedi [[questo articolo]].

**E' possibile utilizzare qualsiasi di questi parametri sia con tipi di riferimento che valore.**

E' sempre importante sottolineare che **un conto è se un tipo di dato è un reference type o value type, un altro conto è se il passaggio di un determinato parametro ad una funziona avviene per riferimento o per valore, sono due concetti diversi**.

### Value parameters

I parametri passati alle funzioni sono, di default, _value parameters._

Questo significa che **viene creata una nuova area di memoria per la variabile dichiarata nella firma della funzione e questa area viene inizializzata con il valore che specifichi nell'invocazione della funzione**.

Questo è il **comportamento di default della maggior parte dei linguaggi**.

Se la funzione chiamata modifica questo valore la funzione chiamante non potrà vedere questa modifica.

Questo è un punto particolarmente delicato, sopratutto in C#: nel seguente codice una classe (reference type) viene passato ad un metodo; all'interno del metodo viene assegnata a null: questa modifica non si riflette all'esterno. Perché?
```CSharp
void Foo (StringBuilder x)
{
    x = null; // x ora punta a null
}

StringBuilder y = new StringBuilder();
y.Append ("hello");
Foo (y);
Console.WriteLine (y==null); // False. y non è stato modificato
```
Se invece nel metodo `Foo` non ho un assegnamento a `null` ma ho una modifica ad una property questa invece viene riflessa anche all'esterno:
```CSharp
void Foo (StringBuilder x)
{
    x.Append (" world"); // x (che punta alla stessa area di memoria di y
}

StringBuilder y = new StringBuilder();
y.Append ("hello");
Foo (y);
Console.WriteLine (y); // print "hello world"
```
Questo comportamento, all'apparenza contraddittorio, è invece perfettamente coerente: l'affermazione "in C# gli oggetti complessi (come le classi) sono **passati per riferimento e mai per valore**" è estremamente confusionaria ([come suggerito da Jon Skeet](https://web.archive.org/web/20180219053344/http://www.yoda.arachsys.com/csharp/parameters.html)) in quanto l'affermazione corretta sarebbe “**i **di default**** i **riferimenti agli oggetti sono passati per valore**”.

Infatti nell'esempio sopra è evidente che **il riferimento alla variabile y viene copiato nella variabile x (passaggio per valore) ma, essendo un riferimento, la modifica alle property di x all'interno del metodo si riflette nella variabile x fuori dal metodo.**

Di conseguenza è evidente che impostare `x` a null non porta a nulla sulla variabile `y` in quanto `x` è una variabile diversa il cui riferimento è stato copiato da `y`.

### Reference parameters

I _reference parameters_ non passano il valore della variabile ma direttamente la variabile effettiva: invece di creare una nuova locazione di memoria viene utilizzata **la stessa del chiamante**.

Utilizzando questi parametri ogni modifica che avviene all'interno del metodo (anche l'indirizzo a cui punta la variabile) si rifletterà all'esterno.

In C# i _reference parameters_ devono essere esplicitati usando la parola chiave `ref` nella dichiarazione del metodo:
```CSharp
void Foo (ref StringBuilder x)
{
    x = null; // x === y, quindi impostare a null viene riflesso anche sul chiamante.
}

StringBuilder y = new StringBuilder();
y.Append ("hello");
Foo (ref y);
Console.WriteLine (y==null); // True
```
Ovviamente è possibile anche passare un _value type_ (come uno `struct`) per reference: in questo caso i valori non vengono copiati e conseguentemente ogni modifica si riflette anche all'esterno:
```CSharp
void Foo (ref IntHolder x)
{
    x.i=10;
}
IntHolder y = new IntHolder();
y.i=5;
Foo (ref y);
Console.WriteLine (y.i); // Scrive 10
```

## Combinazioni

Come abbiamo visto ho due tipologie di tipi di dato (referenza e valore) e due tipologie di passaggio di parametri (referenza e valore), vediamo quindi le 4 combinazioni possibili:

### Value types passati per valore

Questo è il comportamento di default quando viene passato un value type ad una funzione: viene creata una nuova variabile, copiato tutto il contenuto della prima e passata all'interno del metodo.

Ogni modifica all'interno del metodo non si riflette all'esterno.

### Value types passati per referenza

Utilizzando la parola chiave ref posso passare per referenza anche un value type: non ho alcuna copia e la variabile che uso all'interno del metodo è la stessa del chiamante: qualsiasi modifica viene riflessa.

### Reference types passati per valore

Questo è il comportamento di default anche per i reference type: viene creata una nuova variabile e viene **copiato l'indirizzo a cui punta la variabile del chiamante**.

Le modifiche alle property dell'oggetto si riflettono all'esterno (puntano entrambe le variabili alla stessa cosa) ma un eventuale assegnamento ad una nuova area di memoria non viene riflesso.

### Reference types passati per riferimento

Il comportamento è analogo ai value type passati per riferimento: viene passato un puntatore e tutte le modifiche interne al metodo vengono riflesse all'esterno.

## Differenze tra i linguaggi

Non tutti i linguaggi permettono entrambe le modalità di passaggio dei parametri, di seguito indico i linguaggi più comuni e la sintassi per il passaggio di parametri per valore o referenza.

| Linguaggio | Passaggio per valore | Passaggio per referenza |
| --- | --- | --- |
| C | `call_by_value(int p)` | `call_by_reference(int & p)` |
| C++ | `call_by_value(int p)` | `call_by_reference(int & p)` |
| C# | `call_by_value(int p)` | `call_by_value(int ref p)` |
| Java | ogni cosa in Java è passata per valore | \- |
| Python | ogni cosa in Python è passata per valore | indirettamente, tramite i _mutable objects_ |
| PHP | `call_by_value(int $p)` | `call_by_reference(&$p)` |
| Javascript | ogni cosa in Javascript è passata per valore | \- |
| Matlab | ogni cosa in Matlab è passata per valore | \- |

Come si può notare spesso i linguaggi interpretati non offrono la possibilità di poter passare una variabile ad un metodo per referenza (tranne il PHP), mentre i linguaggi compilati puri (come il C o il C++) e i compilati su bytecode (come il Java o C#) offrono tale possibilità.

## Approfondimento: ref struct

Le struct "ref" sono un costrutto introdotto in C# 7.2 e permettono di definire delle strutture dati di tipo struct che **per costruzione non possono andare sullo [[Heap]] ma risiedono sempre sullo [[Stack]].**

L'impossibilità di andare sullo heap permettono di avere codice sicuramente più leggero dal punto di vista della memoria e che richiede meno interventi del GC, ma porta con se molte limitazioni.

Anche se viene utilizzata la parola chiave "`ref`" analogamente al passaggio per referenza non centra nulla.

Per approfondire questo e altri concetti consiglio [questo articolo](https://docs.microsoft.com/en-us/dotnet/csharp/write-safe-efficient-code#use-ref-struct-types).

___

Per approfondire:
-   [Documentazione ufficiale](https://msdn.microsoft.com/it-it/library/0f66670z.aspx)
-   [Domanda di StackOverlfow](http://stackoverflow.com/questions/373419/whats-the-difference-between-passing-by-reference-vs-passing-by-value)
-   [Articolo di Jon Skeet](http://www.yoda.arachsys.com/csharp/parameters.html)