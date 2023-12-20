---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


L'utilizzo della parola chiave [`yield` `return`](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/yield) in C# da spesso adito a dubbi in quanto il suo comportamento è peculiare: tale parola chiave indica che l'oggetto che sto ritornando (tipicamente un _IEnumerable_) si comporta come un iteratore e non come un normale oggetto.

Essendo tale oggetto un iteratore significa che l'oggetto non viene effettivamente creato ma **il metodo viene chiamato solo quando l'oggetto viene iterato in un foreach** (o in una query LINQ).

## Funzionamento

Quando sto ciclando su un oggetto _IEnumerable_ fornito da un metodo con lo `yield return` ho il seguente comportamento:

- Il metodo viene chiamato solo alla chiamata del foreach
- Il metodo viene eseguito fino al primo `yield return` oggetto
- L'oggetto viene ritornato e viene memorizzato il punto del metodo dove mi sono fermato in precedenza
- Alla prossima chiamata di foreach (metodo `MoveNext()` di `IEnumerator`) viene richiamato il metodo che **ripartirà dove si era fermato prima** con le stesse variabili locali
- Il metodo si fermerà al prossimo `yield return`
- Così via fino alla conclusione del metodo
- E' inoltre possibile utilizzare yield break per interrompere il ciclo

Questo avviene in quanto il compilatore crea una sorta di macchina a stati interna in cui memorizza lo stato precedente e ricomincia da tale stato per la chiamata successiva del ciclo.

## Utilità

L'utilizzo dello yield return al posto del normale return ha un senso in alcuni specifici casi:

- Quando voglio fornire un `IEnumerable` di oggetti senza necessariamente creare una classe che lo implementa, come Liste o simili. Sarà il compilatore a fare tutto;
- Quando voglio ridurre il numero di linee di codice facendo che sia il compilatore a memorizzare lo stato;
- Quando voglio far diventare una chiamata sincrona simil-asincrona, in quanto ogni viene chiamato del codice solo quando necessario e non a priori;
- Quando ho una lista enorme da iterare e non voglio leggerla tutta a priori per non occupare RAM.

## Esempio

Prendiamo due semplici metodi che forniscono la lista dei numeri a 0 a 4, il primo che utilizza lo yield return e il secondo no.
```csharp
private static IEnumerable<int> RangeZeroToFourYield()
{
    Console.WriteLine("Entro nel metodo RangeZeroToFourYield");
    yield return 0;
    yield return 1;
    yield return 2;
    yield return 3;
    yield return 4;
}

private static IEnumerable<int> RangeZeroToFour()
{
    Console.WriteLine("Entro nel metodo RangeZeroToFour");
    var output = Enumerable.Range(0, 5);
    return output;
}
```
Si nota già la prima differenza: nel metodo con lo `yield return` non ho avuto bisogno di istanziare classi `IEnumerable`, ho ritornato direttamente gli oggetti che lo componevano. Nel secondo metodo invece ho l'istanza della classe `IEnumerable`.

Per dimostrare la differenza nella chiamata ho scritto il seguente metodo
```csharp
Console.WriteLine("Ottengo i valori di RangeZeroToFourYield");
var rangeYield = RangeZeroToFourYield();
Console.WriteLine("Non sono entrato nel metodo RangeZeroToFourYield!");
Console.WriteLine("Ottengo i valori di RangeZeroToFour");
var rangeNotYield = RangeZeroToFour();
Console.WriteLine("Con il return normale sono entrato nel metodo RangeZeroToFour!");
foreach (var i in rangeYield)
    Console.Write($"{i} ");
foreach (var i in rangeNotYield)
    Console.Write($"{i} ");
Console.ReadKey();
```
Chiamandolo ottengo il seguente output:
```
Ottengo i valori di RangeZeroToFourYield
Non sono entrato nel metodo RangeZeroToFourYield!
Ottengo i valori di RangeZeroToFour
Entro nel metodo RangeZeroToFour
Con il return normale sono entrato nel metodo RangeZeroToFour!
Entro nel metodo RangeZeroToFourYield
0 1 2 3 4
0 1 2 3 4
```
Come dimostrato, quando ho la prima chiamata al metodo `RangeZeroToFourYield` questo non viene effettivamente chiamato, se non quando effettivamente itero gli oggetti.
