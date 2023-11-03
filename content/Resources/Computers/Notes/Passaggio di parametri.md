---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


Per la scrittura di questo articolo mi sono basato principalmente sui seguenti link:

- [Documentazione ufficiale](https://msdn.microsoft.com/it-it/library/0f66670z.aspx)
- [Domanda di StackOverlfow](http://stackoverflow.com/questions/373419/whats-the-difference-between-passing-by-reference-vs-passing-by-value)
- [Articolo di Jon Skeet](http://www.yoda.arachsys.com/csharp/parameters.html)

## 1. Introduzione
In questo articolo approfondisco una parte fondamentale della programmazione: **il passaggio di parametri**, con particolare riferimento al linguaggio C#.
In molti linguaggi, soprattutto compilati, è possibile passare argomenti a parametri di funzioni **per valore o per riferimento**.
La conoscenza di questa differenza e la sua padronanza è indispensabile per una buona programmazione.
Un ottimo esempio della differenza tra i due l'ho trovata spiegata in [questa domanda di StackOverflow](http://stackoverflow.com/questions/373419/whats-the-difference-between-passing-by-reference-vs-passing-by-value): assumiamo che io voglia condividere una pagina web con te: se ti fornisco l'URL della pagina sto facendo un passaggio per riferimento, infatti se la pagina cambia entrambi vediamo gli stessi cambiamenti. Qualora tu elimini l'URL non stai eliminando la pagina in se, ma solo il modo che tu hai per accedere a tale pagina.
Se invece stampo la pagina su un foglio e te lo fornisco, allora sto effettuando un passaggio per valore: la tua pagina è disconnessa dall'originale, le modifiche che tu effettui o che vengono effettuate sull'originale, non vengono rilevate.

In C# esistono quattro differenti tipologie passaggio di parametri:

- per **valore** (il comportamento di default);
- per **riferimento** (usando la parola chiave **ref**);
- come **parametri di output** (usando la parola chiave **out**);
- come **array di parametri** (usando la parola chiave **params**).

Per un approfondimento sui parametri di metodo vedi [questo articolo](http://ilprogrammatorepigro.tumblr.com/post/135479024392/i-parametri-di-metodo).


### 1.1 Tipi per referenza e per valore
In C# esistono due insiemi di tipi di variabili: i *tipi per referenza* e i *tipi per valore*.
**Classi, oggetti ed array sono tipi per referenza, tipi semplici, struct ed enum sono tipi per valore**.
#### 1.1.1 Tipi per referenza (reference types)
Un tipo per referenza è un tipo che **ha come valore il riferimento ai dati invece che i dati stessi**. Per esempio, consideriamo il codice seguente:
```csharp
StringBuilder sb = new StringBuilder();
```
In questa riga di codice abbiamo dichiarato una variabile `sb`, creato un nuovo oggetto `StringBuilder` e assegnato a `sb` un riferimento a tale oggetto.
Il valore di `sb` non è l'oggetto stesso, ma la sua referenza, come si può capire dall'esempio seguente
```csharp
StringBuilder first = new StringBuilder();
first.Append("hello");
StringBuilder second = first;
first.Append(" world");
Console.WriteLine(second); // Prints hello world
```
E' importante sottolineare che le due variabili `first` e `second` sono variabili indipendenti, infatti cambiare il valore di first non influisce in alcun modo la variabile `second`.

#### 1.1.2 Tipi per valore (value types)
**Le variabili di tipo per valore contengono direttamente i dati**. L'assegnamento di una variabile di questo tipo presuppone che **tutti i dati vengano copiati**.
Per esempio, consideriamo la seguente struct
```csharp
public struct IntHolder
{
public int i;
}
```
Quando lavoro con una variabile di tipo `IntHolder`, questa contiene tutti i dati (nel caso seguente un valore intero). Un assegnamento copia il valore, slegandolo dalla variabile iniziale
```csharp
IntHolder first = new IntHolder();
first.i = 5;
IntHolder second = first;
first.i = 6;
// La linea seguente scrive "5", non è influenzata dalla modifica
Console.WriteLine (second.i);
```
E' importantissimo sottolineare che **tutti i tipi semplici, compresi gli struct e gli enum (ma non string) sono tipi per valore**.

Il tipo `string` è un tipo particolare in quanto spesso si comporta come se fosse un tipo per valore invece è un tipo per referenza a tutti gli effetti. Questi tipi di oggetti sono detti *tipi immutabili*, che significa che una volta che è stata creata un'istanza di questi, non può più essere cambiata. Questo permette ad un tipo per referenza di comportarsi in maniera simile ad un tipo per valore in quanto posso passarlo a dei metodi black box ed essere sicuro che questi non ne possano cambiare il valore.

## 2. Passaggio per valore
Questo meccanismo permette alla funzione invocata di ricevere come parametro **il valore del parametro effettivo**, infatti questo viene **copiato** nella variabile della funzione chiamata.
Questo è il **comportamento di default della maggior parte dei linguaggi**.
Se la funzione chiamata lo modifica, la funzione chiamante non potrà vedere questa modifica.
Quando si passa un parametro associato a un **reference type (vedi sezione 1.1.1), è possibile modificare i dati associati al riferimento in modo che siano visibili all'esterno**, ad esempio il valore del membro di una classe ma non è tuttavia possibile modificare il valore del riferimento stesso.
Nell'esempio che segue viene illustrato il passaggio per valore di un array al metodo `Change`. Poiché il parametro è un array (quindi un *reference type*), è possibile **modificare il valore degli elementi dello stesso e far sì che queste modifiche siano visibili anche al di fuori del metodo stesso**.
Il tentativo di riassegnare il parametro a una diversa posizione in memoria, tuttavia, è efficace solo all'interno del metodo e non ha alcun effetto sulla variabile originale.
```csharp
static void Change(int[] pArray)
{
// Questo cambiamento modifica anche il valore esterno, in quanto ho una modifica dei dati associati alla variabile
pArray[0] = 888;
// In questo caso invece ho un malloc: il cambiamento è solo locale
pArray = new int[5] {-3, -1, -2, -3, -4};
// il valore di pArray[0] ora è -3, ma solo all'interno del metodo
}
static void Main() 
{
int[] arr = {1, 4, 5};
// arr[0] ora è uguale a 1
Change(arr);
// arr[0] ora è uguale a 888, la modifica all'interno del metodo ha effetti anche globali
}
```

## 3. Passaggio per riferimento
Questo meccanismo permette alla funzione invocata di ricevere come parametro **il puntatore** (valore dell'indirizzo di memoria) **all'oggetto effettivo**. Se la funzione chiamata modifica il parametro passato per riferimento, allora **la modifica sarà visibile anche alla funzione chiamante**.
In C# gli oggetti complessi (come le classi) sono **sempre passati per riferimento e mai per valore**. Come suggerito da Jon Skeet questa affermazione non è completamente corretta, infatti egli afferma che la frase corretta sarebbe "**i riferimenti agli oggetti sono passati per valore di default**"
L'esempio seguente è lo stesso dell'esempio precedente, tranne per il fatto che **la parola chiave `ref`viene aggiunta all'intestazione e alla chiamata di metodo**. Tutte le modifiche che hanno luogo nel metodo hanno effetti anche nel programma chiamante.
```csharp
static void Change(ref int[] pArray)
{
// Questo cambiamento modifica anche il valore esterno
pArray[0] = 888;
// Anche questo cambiamento viene rilevato dall'esterno
pArray = new int[5] {-3, -1, -2, -3, -4};
// il valore di pArray[0] ora è -3
}
static void Main() 
{
int[] arr = {1, 4, 5};
// arr[0] ora è uguale a 1
Change(ref arr);
// arr[0] ora è uguale a -3, la modifica all'interno del metodo ha effetti anche globali
}
```

## 4. Differenze tra i linguaggi
Non tutti i linguaggi permettono entrambe le modalità di passaggio dei parametri, di seguito indico i linguaggi più comuni e la sintassi per il passaggio di parametri per valore o referenza.

| Linguaggio | Passaggio per valore | Passaggio per referenza |
|--------|--------|--------|
|C |`call_by_value(int p)`|`call_by_reference(int & p)`|
|C++ |`call_by_value(int p)`|`call_by_reference(int & p)`|
|C# |`call_by_value(int p)`|`call_by_value(int ref p)`|
|Java |ogni cosa in Java è passata per valore|-|
|Python |ogni cosa in Python è passata per valore|indirettamente, tramite i *mutable objects*|
|PHP |`call_by_value(int $p)`|`call_by_reference(&$p)`|
|Javascript|ogni cosa in Javascript è passata per valore|-|
|Matalb |ogni cosa in MAtlab è passata per valore|-|

Come si può notare spesso i linguaggi intepretati non offrono la possibilità di poter passare una variabile ad un metodo per referenza (tranne il PHP), mentre i linguaggi compilati puri (come il C o il C++) e i compilati su bytecode (come il Java o C#) offrono tale possibilità.