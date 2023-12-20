---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---
In questo articolo descrivo le parole chiave che è possibile usare quando si dichiarono i parametri dei metodi ed il loro significato.

## 1. Il parametro di metodo ref
Nella programmazione a oggetti è molto comune, ovviamente, lavorare con questi e passarli a dei metodi. E' importante sottolineare che **gli oggetti sono sempre passati come referenza, mai per valore**.
Per i tipi semplici di C#, come le **structs** e gli **enum** così invece non è, infatti tali dati vengono passati per valore.
La parola chiave **ref** di C# permette di indicare che il parametro in ingresso a cui questa è associata **deve essere passato per riferimento e non per valore**.
A differenza di **out**, il parametro indicato come **ref** deve essere inizializzato prima di essere passato

La parola chiave **ref** deve essere usata **sia nella dichiarazione degli argomenti di un metodo, che durante la chiamata di questo ultimo**.

```csharp
class RefExample
{
  static void Method(ref int i)
  {
    // Rest the mouse pointer over i to verify that it is an int.
    // The following statement would cause a compiler error if i
    // were boxed as an object.
    i = i + 44;
  }

  static void Main()
  {
    int val = 1;
    Method(ref val);
    Console.WriteLine(val);
    // Output: 45
  }
}
```

## 2. Il parametro di metodo out
Spesso quando devo chiamare un metodo che va a modificare lo stato interno di un oggetto, questo oggetto viene creato in precedenza e passo al metodo **il riferimento a tale oggetto**.
Qualora dovessi creare un nuovo oggetto all'interno di un metodo e poi fornirlo all'esterno, il modo migliore è utilizzare il `return` del metodo.
Se invece voglio creare un metodo che mi ritorni **più di un oggetto** (eventualità che, nella buona programmazione, è piuttosto rara) e sono impossibilitato ad istanziare gli oggetti in questione prima dell'effettiva chiamata al metodo, devo utilizzare la parola chiave **out**.
Solitamente, il compilatore C# non permette di passare ad un metodo il riferimento a variabili dichiarate ma non inizializzate, indicare **out** prima di un parametro indica al compilatore che **l'inizializzazione della variabile a cui è riferita è resposabilità del metodo chiamante**, il compilatore si può quindi "fidare" e passare ad un metodo il riferimento ad una variabile non ancora inizializzata.
Analogamente a **ref**, devo indicarla sia nella lista dei parametri che nella chiamata al metodo.

```csharp
class OutExample
{
static void Method(out int i)
{
i = 44;
}

static void Main()
{
int value;
Method(out value);
// value is now 44
}
}
```

## 3. Il parametro di metodo params
Questo modificatore può essere applicato solo all'**ultimo parametro di un metodo** specifica che tale metodo può essere chiamato con un qualsiasi numero di parametri con quel tipo specifico.
Un esempio preso dalla documentazione ufficiale è il seguente

```csharp
public static void UseParams(params int[] list)
{
for (int i = 0; i < list.Length; i++)
{
Console.Write(list[i] + " ");
}
Console.WriteLine();
}
```