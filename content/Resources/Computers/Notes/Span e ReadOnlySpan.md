---
tags:
  - Coding
  - CSharp
  - Memory
  - PublishedPosts
---


`Span` è un nuovo tipo introdotto in C#7.2 e supportato dal .NET Core 2.1 in poi ed è utilizzato per ==ottenere un puntatore type-safe ad una area contigua di memoria== (che sia sullo [[heap]], [[stack]] o anche unmanaged).

Utilizzando lo `Span` è possibile effettuare delle elaborazioni su tale oggetto in memoria 100% sullo stack senza passare dallo heap, risparmiando quindi memoria e facendo risparmiare tempo al [[Garbage Collector]].

E' importante utilizzarlo in software dove la performance e la gestione della memoria sono importanti.

Esiste anche la versione in sola lettura dello `Span` chiamata `ReadOnlySpan` utilizzata principalmente per manipolare sullo stack oggetti immutabili come le [[Le stringhe in C Sharp]].

## Implementazione
```csharp
public readonly ref struct Span<T>
{
  private readonly ref T \_pointer;
  private readonly int \_length;
  public ref T this[int index] => ref \_pointer + index;
  ...
}
```
Lo `Span` è un `ref struct` che quindi, per definizione, non può essere allocato sullo heap.

Inoltre per accedere ad un elemento utilizzo il `ref return` che permette di ritornare il puntatore all'oggetto ritornato e non un valore.
Per gli [[oggetti passati per referenza]] non cambia nulla, mentre cambia per gli oggetti passati per valore e soprattutto per le stringhe.

## Funzionamento

Per spiegare il funzionamento utilizzo un `ReadOnlySpan` che, come dice il nome, è l'analogo dello `Span` ma in sola lettura, quindi senza la possibilità di modificare la memoria. Viene utilizzato principalmente per manipolare stringhe.

Uno `ReadOnlySpan` parte sempre da una variabile presente sullo heap (per esempio una stringa già allocata) e **ne effettua delle elaborazioni utilizzando solo offset e lunghezze**.

Per esempio se ho la stringa "`foo bar`" sullo heap e voglio lavorare solo su "`foo`" posso creare uno `ReadOnlySpan` sullo stack con offset 0 e lunghezza 3.

Senza quindi allocare alcuna stringa ulteriore ho una rappresentazione di "`foo`".

Il risparmio di allocazione porta sia ad un risparmio di memoria ma anche migliora le performance del GC che non deve pulire da stringhe non utilizzate.

Lo `ReadOnlySpan` è molto più limitato sulle cose che può fare rispetto alle stringhe, però può essere utile in alcuni casi specifici dove la performance è importante.

## Esempio  

Per capire meglio il funzionamento facciamo dei test con [Benchmark.net](https://benchmarkdotnet.org/articles/overview.html). Il problema da risolvere è il seguente: data una stringa di due parole separate da spazio prenderne la prima.

Ho pensato a tre implementazioni diverse, dalla più lenta alla più veloce.

La classe contenente ha una `const "TwoWords = "Foo Bar"`; e i seguenti header
```csharp
[RankColumn]
[Orderer(SummaryOrderPolicy.FastestToSlowest)]
[MemoryDiagnoser]
public class SpanTests{}
```
### Implementazione 1 - LINQ
```csharp
[Benchmark]
public string GetFirstString()
{
    // Alloco un array di stringhe sullo heap, in particolare alloco "Foo" e "Bar"
    var words = TwoWords.Split(" ");
    // Prendo l'ultimo valore dell'array. Dato che le stringhe sono immutabili alloco una ulteriore sullo heap
    var firstWord = words.FirstOrDefault();
    // Ritorno la prima parola. L'array words contenente le due string che vanno out of scope in quanto perdo i puntatori dello stack.
    // Essendo variabili locali entreranno nella gen 0 del GC e al prossimo collect verranno eliminate
    return firstWord ?? string.Empty;
}
```
### Implementazione 2 - Substring
```csharp
[Benchmark]
public string GetFirstWordUsingSubstring()
{
    // Ottengo un valore intero dell'ultimo index di ' ' (sono sullo stack)
    var lastSpaceindex = TwoWords.LastindexOf(" ", StringComparison.Ordinal);
    // Il metodo Substring alloca una nuova stringa sullo heap contentente "Foo"
    var firstString = TwoWords.Substring(0, lastSpaceindex);
    return lastSpaceindex == -1 ? string.Empty : firstString;
}
```
### Implementazione 3 - ReadOnlySpan
```csharp
[Benchmark]
public ReadOnlySpan<char> GetFirstWordUsingSpanAndLastindexOf()
{
    // Creo uno Span sullo stack che punta alla variabile \_twoWords sullo heap
    ReadOnlySpan<char> nameAndSurnameAsSpan = TwoWords;
    // Ottengo un valore intero dell'ultimo index di ' ' (sono sullo stack)
    var lastSpaceindex = nameAndSurnameAsSpan.LastindexOf(' ');
    // Utilizzo Slice che è l'analogo di Substring. Aggiungo allo stack due variabili: offset "0" e lenght "lastSpaceindex".
    var firstString = nameAndSurnameAsSpan.Slice(0, lastSpaceindex);
    return lastSpaceindex == -1 ? ReadOnlySpan<char>.Empty : firstString;
}
```
### Risultati

Dopo aver lanciato il benchmark questi sono i risultati:

![[immagine.webp]]

Il metodo `GetFirstString` è il più lento e inoltre alloca più memoria e, dal codice è evidente il motivo: ho un nuovo array di stringhe sullo heap e inoltre una chiamata a LINQ che non è performante.

Il metodo `GetFirstWordUsingSubstring` utilizza `Substring` invece di `FirstOrDefault` di LINQ e infatti ho un notevole miglioramento di performance e di allocazione di memoria.

L'ultimo metodo `GetFirstWordUsingSpanAndLastindexOf` è estremamente veloce e soprattutto non porta ad alcuna nuova allocazione di memoria.
