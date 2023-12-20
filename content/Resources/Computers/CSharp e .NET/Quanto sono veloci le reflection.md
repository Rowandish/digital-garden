---
tags:
  - Coding
  - CSharp
  - Performance
  - PublishedPosts
---


La reflection permette al codice di poter istanziare classi o chiamare metodi privati senza passare per la classe stessa; capire quanto queste siano veloci permette di scrivere codice più performante.

E' possibile utilizzare le reflection per creare una istanza di un oggetto di un determinato tipo, per chiamare dei metodi non public, per accedere ai suoi campi privati.

L'obiettivo di questo articolo è capire quanto è lenta la reflection rispetto all'utilizzo di un metodo normale e cose è possibile fare per ottimizzarla il più possibile.

Per effettuare questa misurazione utilizzeremo il mitico pacchetto [benchmarkDotNet](https://github.com/dotnet/BenchmarkDotNet).

Consideriamo la seguente classe `Furniture` con una property `Color {get; private set;}` e un metodo `SetColor` per andare ad impostarne il colore.
```csharp
public class Furniture
{
    public string Color { get; private set; }

    public void SetColor(string color)
    {
        Color = color;
    }
    
    private void SetColorPrivate(string color)
    {
        Color = color;
    }
}
```
Andiamo ad impostare ora la property `Color` utilizzando vari metodi, per poi misurarne le performance.

## Non Reflection

In questo caso andiamo a impostare il colore usando il metodo `SetColor`.
```csharp
[Benchmark]
public void NonReflection()
{
    _furniture.SetColor("Foo");
}
```
## Reflection senza cache

Il metodo più semplice per impostare una property privata è usare il metodo `SetValue` di una `PropertyInfo` ottenuta dal metodo `GetProperty`.
```csharp
[Benchmark]
public void ReflectionNonCached()
{
    typeof(Furniture).GetProperty("Color")?.SetValue(_furniture, "Foo");
}
```

## Reflection con cache

Un miglioramento del metodo precedente è calcolare una sola volta la `PropertyInfo` nel seguente modo.
```csharp
private static readonly PropertyInfo ColorPropertyInfo = typeof(Furniture).GetProperty("Color")!;

[Benchmark]
public void ReflectionCached()
{
    ColorPropertyInfo.SetValue(_furniture, "Foo");
}
```
## Reflection su backing field

Le property vengono tradotte da .NET in due metodi che puntano ad un _backing field_. Per dimostrare questo apriamo Sharplab e incolliamo la classe `Furniture`. Otteniamo il seguente codice:
```csharp
public class Furniture
{
    [CompilerGenerated]
    [DebuggerBrowsable(DebuggerBrowsableState.Never)]
    private string <Color>k__BackingField;

    public string Color
    {
        [CompilerGenerated]
        get
        {
            return <Color>k__BackingField;
        }
        [CompilerGenerated]
        private set
        {
            <Color>k__BackingField = value;
        }
    }

    public void SetColor(string color)
    {
        Color = color;
    }
}
```
Vediamo infatti la presenza di un campo chiamato <`Color>k__BackingField`. Possiamo sfruttare questa informazione per modificare quel campo tramite reflection, scrivendo quindi:
```csharp
private static readonly FieldInfo CachedField =
typeof(Furniture).GetField("<Color>k__BackingField", BindingFlags.Instance | BindingFlags.NonPublic)!;

[Benchmark]
public void ReflectionCachedWothField()
{
    CachedField.SetValue(_furniture, "Foo");
}
```
## Reflection con delegate

Infine sfruttiamo il metodo `GetSetMethod` di `PropertyInfo`: questo metodo permette di andare a prendere un puntatore a funzione del metodo set di una property, anche se questo è privato.

Questo puntatore viene convertito in `Delegate` e castato come `Action` in modo da poter essere chiamato.

Il codice per ottenere ciò è il seguente:
```csharp
private static readonly Action<Furniture, string> SetColorDelegate =
(Action<Furniture, string>)Delegate.CreateDelegate(typeof(Action<Furniture, string>), ColorPropertyInfo.GetSetMethod(true)!);

[Benchmark]
public void ReflectionWithDelegate()
{
    SetColorDelegate(_furniture, "Foo");
}
```
## Reflection con metodo privato

Come ultimo test proviamo a modificare la property chiamando un metodo privato (`SetColorPrivate`) nella classe.
```csharp
private static readonly Action<Furniture, string> SetColorPrivateDelegate =
(Action<Furniture, string>)Delegate.CreateDelegate(typeof(Action<Furniture, string>), SetColorPrivateMethodInfo);

[Benchmark]
public void ReflectionMethodWithDelegate()
{
    SetColorPrivateDelegate(_furniture, "Foo");
}
```
## Risultati

Dopo aver descritto tutti i metodi con cui è possibile modificare un campo privato di una classe andiamo a vedere i risultati.

|                       Method |       Mean |     Error |     StdDev |
|----------------------------- |-----------:|----------:|-----------:|
|                NonReflection |   2.321 ns | 0.1104 ns |  0.2445 ns |
|          ReflectionNonCached | 254.680 ns | 8.7334 ns | 23.7599 ns |
|             ReflectionCached | 168.553 ns | 4.8918 ns | 13.7973 ns |
|    ReflectionCachedWithField |  85.107 ns | 1.9745 ns |  5.5690 ns |
|       ReflectionWithDelegate |   5.944 ns | 0.3231 ns |  0.9425 ns |
| ReflectionMethodWithDelegate |   5.970 ns | 0.4275 ns |  1.2334 ns |

Ovviamente il metodo più veloce è quello senza reflection, ma quanto posso andarci vicino?

Utilizzare una cache della `PropertyInfo` sicuramente aiuta, come si vede dalla differenza tra i benchmark `ReflectionNonCached` e `ReflectionCached`.

Un ulteriore miglioramento è puntare al backing field privato <`Color>k__BackingField`.

Il vero boost di prestazioni si ha utilizzando il puntatore a funzione del metodo set, con un miglioramento di circa 25x rispetto al metodo che punta al backing field e di 55x rispetto al metodo più lento.

Puntare ad un metodo privato ha delle performance praticamente uguali a quelle di puntare al metodo `set`, come è intuitivo che sia, dato che, di fatto, sono la stessa cosa.

## Conclusioni

Le reflection in .NET sono estremamente veloci, utilizzando i giusti accorgimenti hanno quasi le performance di chiamare un metodo in modo classico.

Il loro problema non è quindi la velocità ma semmai la manutenibilità e l’estendibilità del codice: questo infatti risulta più difficile da leggere, gli errori vengono rilevati solo runtime e, in generale, le reflection permettono di violare tutte le regole di buona programmazione.
