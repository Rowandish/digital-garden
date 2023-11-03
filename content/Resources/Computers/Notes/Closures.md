---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


Questo articolo è una libera traduzione di [questo articolo](http://csharpindepth.com/Articles/Chapter5/Closures.aspx) di Jon Skeet.

## 1. Introduzione
Per dirla nel modo più semplice possibile, le closures permettono di incapsulare alcuni comportamenti della nostra applicazione in oggetti che possno essere passati ad altri oggetti o metodi, che hanno però la caratteristica fondamentale di poter **aver accesso al contesto in cui queste sono state inzialmente dichiarate**.
Questa possibilità è ciò che separa le closures dai classici oggetti.

## 2. I predicati
E' estremamente comune voer filtrare una lista di oggetti secondo un determinato criterio: è particolarmente facile farlo "inline", basta creare una nuova lista, iterare sulla lista originale ed aggiungere solo gli elementi selezionati alla nuova lista.
A livello di codice è molto veloce, ma è sicuramente meglio cercare di nascdondere la logica del filtraggio in un altro luogo.
IN questo contesto introduciamo un nuovo termine: **predicate**.
Un predicato è semplicemente qualcosa che fa un match (o meno) di un deterinato oggetto, nel nostro esempio **creeremo una nuova lista con solo gli oggetti che matchano il predicato**.
Il modo naturale di rappresentare un predicato è scriverlo come un **delegate** e .NET contiene un tipo `Predicate<T>` (analogo al `Func<T,bool>` utilizzato da LINQ).
Di seguito la classica dichiarazione di un delegate in C#
```csharp
public delegate bool Predicate<T>(T obj)
```
E la dichiarazione del metodo di filtraggio che utilizza tale predicato:
```csharp
static class ListUtil
{
    public static IList<T> Filter<T>(IList<T> source, Predicate<T> predicate)
    {
        List<T> ret = new List<T>();
        foreach (T item in source)
        {
            if (predicate(item))
            {
                ret.Add(item);
            }
        }
        return ret;
    }
}
```
## 3. Esempi
### 3.1 Eseguire il match di stringhe a lunghezza fissa
Prendiamo in ingresso una lista di stringhe e produciamo in uscita una seconda lista che contiene solo le stringhe "corte" della prima. Costruire la lista è estremamente semplice, il predicate invece è un po' macchinoso.
In C# 2 abbiamo due possibilità:
- usare i **delegate** dichiarando esternamente la firma del metodo
- usere le **funzioni anonime** che semplificano ulteriormente il codice in quanto permettono di scrivere la definizione della funzione "inline".

Di seguito l'esempio direttamente con il metodo anonimo:
```csharp
Predicate<string> predicate = delegate(string item)
{
  return item.Length < 5;
};
IList<string> shortWords = ListUtil.Filter(SampleData.Words, predicate);
ListUtil.Dump(shortWords);
```
In C# 3 è stata introdotta una nuova funzionalità, che sono le **lambda espressioni**.
Per lo scopo di questo articolo, le lambda espressioni sono sempicemente delle funzioni anonime scritte in una forma ancora più concisa.
Usando tale funzionalità, il codice indicato sopra si semplifica ulteriormente
```csharp
static void Main()
{
    Predicate<string> predicate = item => item.Length < 5;
    IList<string> shortWords = ListUtil.Filter(SampleData.Words, predicate);
    ListUtil.Dump(shortWords);
}
```
### 3.2 Eseguire il match di stringhe a lunghezza variabile
Aumentiamo ora la complessità permettendo all'utente di poter scegliere la lunghezza delle stringhe da filtrare.
Grazie alle closures, possiamo passare il valore inserito dall'utente come parametro in ingresso della funzione:
```csharp
static void Main()
{
    Console.Write("Maximum length of string to include? ");
    int maxLength = int.Parse(Console.ReadLine());

    Predicate<string> predicate = item => item.Length < maxLength;
    IList<string> shortWords = ListUtil.Filter(SampleData.Words, predicate);
    ListUtil.Dump(shortWords);
}
```
E' importante sottolineare che, a differenza del java, non viene catturato il valore della variabile, **ma la variabile stessa**.
Conseguentemente, se un codice esterno cambia il valore di tale variabile prima che il metodo venga invocato, il metodo risenterà di tale modifica.
Nel codice seguente viene lancaito due volte lo stesso metodo cambiando esternamente a questo **solo la variabile maxLength**
```csharp
shortWords = ListUtil.Filter(SampleData.Words, predicate);
maxLength = 5;
shortWords = ListUtil.Filter(SampleData.Words, predicate);
```

### 4. Conclusione
Grazie alle closures, è possibile separare la struttura di controllo dalla logica del filtraggio.
Il beneficio che portano spesso le closures è la cosidetta *composability*.
Nella fase iniziale utilzzare le closures, che sono un modo per comodo per creare dei delegate, risulta difficile ma, dopo un po' di esperienza, le funzioni possono essere considerati poco di più di un altro tipo di dato.
