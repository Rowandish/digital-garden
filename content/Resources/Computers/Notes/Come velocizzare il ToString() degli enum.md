---
tags:
  - Coding
  - CSharp
  - Performance
  - PublishedPosts
---


## Introduzione

Il metodo `ToString()` di un `enum` è implementato in maniera molto discutibile: è lento e inoltre porta a delle inutili allocazioni di memoria che dovranno essere eliminati dal GC.

Andiamo a vedere sotto il cofano come funziona il metodo `ToString()`; dopo qualche metodo interno otteniamo:
```Csharp
private static string? GetEnumName(EnumInfo enumInfo, ulong ulValue)
{
    int index = Array.BinarySearch(enumInfo.Values, ulValue);
    if (index >= 0)
    {
        return enumInfo.Names[index];
    }

    return null; // return null so the caller knows to .ToString() the input
}
```
Come si nota vi è un binary search su tutti i valori dell'enum e inoltre un accesso tramite indice all'array contenente i nomi.

Gli algoritmi di ricerca binaria hanno performance di `O(logn)`, quindi più sono i valori dell'enum maggiore sarà il tempo impiegato dall'algoritmo a trovare il valore corretto.

Questa complicazione può essere completamente evitata dato che il `ToString()` di un `Enum` è, di fatto, il suo `nameof`: il `ToString()` di `Color.Aquamarine` è esattamente `nameof(Color.Aquamarine)`

Questa chiamata è incredibilmente più veloce, non dipende dalla dimensione dell'enum e inoltre non alloca memoria.

Il problema è che, per ogni enum da velocizzare, servirebbe che ci sia un metodo con all'interno un gigantesco switch case che mappa ogni valore dell'enum al suo `nameof`.

Il primo approccio è fare tutto a mano ma, grazie ai [Source Generators](https://docs.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators-overview), è possibile automatizzare il lavoro.

Andrew Lock, nel suo blog [.NET Escapades](https://andrewlock.net/), ha creato un comodo pacchetto nuget per automatizzare la generazione di codice veloce per ogni enum che si vuole. Il progetto è open source e disponibile qui: [EnumGenerators](https://github.com/andrewlock/NetEscapades.EnumGenerators).

Una volta importato il pacchetto nuget è solo necessario aggiungere l'attributo `[EnumExtensions]` sopra l'enum da velocizzare e verranno generati degli extension methods automaticamente.

## Test

Oltre a `ToString()` ho testato `Enum.IsDefined` e `Enum.TryParse` utilizzando [BenchmarkDotNet](https://benchmarkdotnet.org/articles/overview.html) confrontando le loro performance con i metodi classici.
```CSharp
[Benchmark]
public string EnumToString()
{
    return EnumColor.Aquamarine.ToString();
}

[Benchmark]
public string EnumToStringFast()
{
    return EnumColor.Aquamarine.ToStringFast();
}

[Benchmark]
public bool EnumIsDefined()
{
    return Enum.IsDefined(typeof(EnumColor), 48);
}

[Benchmark]
public bool EnumIsDefinedFast()
{
    return EnumColorExtensions.IsDefined((EnumColor)48);
}

[Benchmark]
public (bool, EnumColor) EnumTryParse()
{
    var couldParse = Enum.TryParse("Aquamarine", false, out EnumColor value);
    return (couldParse, value);
}

[Benchmark]
public (bool, EnumColor) EnumTryParseFast()
{
    var couldParse = EnumColorExtensions.TryParse("Aquamarine", false, out var value);
    return (couldParse, value);
}
```
Ecco i risultati:

|            Method |       Mean |         Error |     StdDev |  Gen 0 |  Gen 1 | Allocated |
|------------------ |-----------:|--------------:|-----------:|-------:|-------:|----------:|
|      EnumToString |  55.941 ns |    66.2153 ns |  3.6295 ns | 0.0057 | 0.0002 |      24 B |
|  EnumToStringFast |   1.512 ns |     1.8909 ns |  0.1036 ns |      - |      - |         - |
|     EnumIsDefined | 301.073 ns | 1,289.5731 ns | 70.6859 ns | 0.0057 |      - |      24 B |
| EnumIsDefinedFast |   1.813 ns |     0.3078 ns |  0.0169 ns |      - |      - |         - |
|      EnumTryParse | 190.173 ns |   414.8240 ns | 22.7379 ns |      - |      - |         - |
|  EnumTryParseFast |  20.076 ns |    21.5005 ns |  1.1785 ns |      - |      - |         - |

## Conclusione

Come si nota abbiamo circa due ordini di grandezza di velocità e inoltre non abbiamo alcuna allocazione di memoria.

Analizzando l'extension `ToStringFast()` notiamo che internamente ha lo switch case di cui parlavamo in precedenza che mappa ogni valore dell'enum nel suo `nameof`.

Dei limiti degli enum e di questo pacchetto ne ha parlato anche Nick Chapsas [qui](https://www.youtube.com/watch?v=BoE5Y6Xkm6w) e [qui](https://www.youtube.com/watch?v=-RX6XKHkjOs).

NetEscapades.EnumGenerators è ancora in beta ed è richiede almeno .NET 6 SDK.
