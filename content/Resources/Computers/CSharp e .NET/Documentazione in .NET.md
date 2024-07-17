---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---
Questo articolo è una traduzione di quanto riportato nel libro _Thinking in C#_ di Larry O’Brien e Bruce Eckel.
## 1.Introduzione
C# è stato progettato in modo che il codice e la documentazione siano nativamente nello stesso luogo, in particolare che la documentazione venga generata automaticamente dai commenti al codice.
Esiste quindi una sintassi speciale per i commenti che identifica che tali commenti sono di documentazione, inoltre esiste un tool per estrarre tali commenti e inserirli insieme in un unico file utilizzabile.
I commenti che cominciano con la tripla barra (`///`) possono essere estratti lanciando il seguente comando in console
```
csc /doc:output.xml Program.cs
```
All'interno di tali commenti posso inserire un qualsiasi tag XML, includendo alcuni tag che hanno un significato speciale in questo contesto.
## 2. Tag particolari

| Tag | Utilizzo |
|--------|--------|
|`<summary></summary>`|Un breve riassunto del metodo|
|`<remarks></remarks>`|E' usato per un'analisi più dettagliata del comportamento del metodo|
|`<param name="name"></param>`|Questo tag deve essere scritto per ogni parametro in ingresso del metodo (indicato dal parametro _name_). Devono essere indicate le precondizioni dell'attributo, cioè le caratteristiche che deve avere questo parametro affinchè il metodo funzioni correttamente|
|`<returns></returns>`|tutti i metodi che ritornano non void devono avere questo tag che indica tutte la caratteristiche del valore di ritorno. Può essere null? Fornisce valori sempre all'interno di un determinato range?|
|`<exception cref="type"></exception>`|tutte le eccezioni generate **esplicitamente** nel metodo devono essere documentate (il tipo dell'eccezioni è indicato nell'attributo _cref_). Oltre al tipo di eccezzione, devono essere ben dettagliate le circostanze che portano a questa|
|`<example> <c></c> <code></code></example>`|Contiene una descrizione ed un codice di esempio. Il tag `<c>` è per il codice inlinde, `<code>` invece per il multilinea|
|`<see cref="other"></see><seealso cref="other"></seealso>`|Servono per collegare altre parti di documentazione/codice. Il tag `<see>` serve per le referenze inline, `<seealso>` invece per creare una sottosezione di riferimenti separata|
| `<value></value>` |Ogni proprietà visibile all'esterno di una classe deve avere questo tag|
|`<paramref name="arg"/>`|questo tag vuoto è usato per indicare che l'attributo _name_ è uno dei parametri in ingresso del metodo|
|`<para></para>`|Crea un paragrafo di lunghezza arbitraria dove inserire informazioni addizionali|

## 3. Esempio

```c#
///<summary>Entry point</summary>
///<remarks>Prints greeting to
/// <paramref name="args[0]"/>, gets a
/// <see cref="System.DateTime">DateTime</see>
/// and subsequently prints it
///</remarks>
///<param name="args">Command-line should have a single name. All other args will be ignored </param>
public static void Main(string[] args)
{
Console.WriteLine("Hello, {0} it's: ", args[0]);
Console.WriteLine(DateTime.Now);
}
```