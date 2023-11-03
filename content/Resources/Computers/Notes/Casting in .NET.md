---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


Il cast (in particolare il downcasting) permette di esplicitare il tipo di una variabile a quello di una classe figlia o sotto-figlia.

Il classico esempio è castare una variabile di tipo `object` al suo tipo effettivo.

Il cast è una operazione comunissima che viene effettuata tutti i giorni anche se è un _code smell_ a tutti gli effetti: è per quello che deve essere manifestata in modo esplicito all'interno del programma in modo che prima o poi qualcuno ci dia un occhio per vedere se è risolvibile.

Tipicamente chiamare un metodo `virtual` o `abstract` è un modo migliore di procedere rispetto al cast.

Esistono però circostanze dove il cast può andare bene:

- Si ha al 100% la certezza che del tipo di una variabile in runtime, informazione che non ho compile time
- Scrivere un cast e risolvere in una riga è una soluzione migliore rispetto a investire del tempo per refactorare tutto.

Se refactorare è semplice conviene sempre farlo rispetto a castare, operazione che dovrebbe essere invece una estrema ratio.

> "What is popular is not always right, what is right is not always popular"

## Hard Cast

Il cast standard è la sintassi analoga a tutti i linguaggi di programmazione fortemente tipizzati: il tipo di dato a cui voglio castare il mio oggetto viene definito tra parentesi nel seguente modo:
```CSharp
object animal = new Dog();
var dog = (Dog) animal;
```
Nell'esempio sopra ho una variabile di tipo `object` istanziata come `Dog`. Per effettuare il cast basta aggiungere (`Dog`).

Questa sintassi porta all'eccezione `InvalidCastException` qualora sia impossibile effettuare il cast.

## Safe Cast

Con questo cast ho un comportamento analogo all'_hard cast_ con la differenza che se il cast non è possibile ritorna `null` invece che `InvalidCastException`.
```CSharp
object animal = new Dog();
var dog = animal As Dog;
```

## Match Cast

Con questo cast posso scrivere una operazione condizionale con un safe cast integrato, la sintassi è la seguente:
```CSharp
object animal = new Dog();
if (animal is Dog castedObject)
{
	// castedObject è l'oggetto castato
}
```
Anche in questo caso non posso mai avere `InvalidCastException` in quanto, qualora non sia castabile, non entro mai nell'if.

## Performance

### Cast di un oggetto

A livello di performance non c'è storia, l'hard cast è nettamente il più veloce (circa 3x rispetto al safe cast e 2x rispetto al match cast).

Per verificarlo ho scritto seguente codice che casta nei tre modi descritti sopra l'oggetto `object` nell'oggetto `Random`.
```CSharp
private readonly object _objectToCast = new Random();

[Benchmark]
public Random HardCast()
{
    var rnd = (Random)_objectToCast;
    return rnd;
}

[Benchmark]
public Random SafeCast()
{
    var rnd = _objectToCast as Random;
    return rnd!;
}

[Benchmark]
public Random MatchCast()
{
    if (_objectToCast is Random rnd)
        return rnd;
    return null!;
}
```
Che fornisce i seguenti risultati

|         Method |      Mean |     Error |    StdDev |    Median |
|--------------- |----------:|----------:|----------:|----------:|
|       HardCast | 0.5802 ns | 0.1055 ns | 0.2466 ns | 0.5162 ns |
|       SafeCast | 1.2295 ns | 0.0583 ns | 0.0487 ns | 1.2473 ns |
|      MatchCast | 1.4336 ns | 0.1837 ns | 0.5182 ns | 1.2065 ns |

### Cast di una lista di oggetti

Per castare una lista di oggetti ci sono vari metodi, si possono vedere tutti nel seguente benchmark:
```CSharp
private readonly List<object> _listOfObjects = Enumerable.Range(0, 10_000).Select(i => (object) new Random()).ToList();

[Benchmark]
public List<Random> OfType()
{
    return _listOfObjects.OfType<Random>().ToList();
}

[Benchmark]
public List<Random> CastAs()
{
    return _listOfObjects.Where(o => o as Random is not null).Cast<Random>().ToList();
}

[Benchmark]
public List<Random> CastIs()
{
    return _listOfObjects.Where(o => o is Random).Cast<Random>().ToList();
}

[Benchmark]
public List<Random> HardCastAs()
{
    return _listOfObjects.Where(o => o as Random is not null).Select(o => (Random) o).ToList();
}

[Benchmark]
public List<Random> HardCastIs()
{
    return _listOfObjects.Where(o => o is Random).Select(o => (Random) o).ToList();
}

[Benchmark]
public List<Random> HardCastTypeOf()
{
    return _listOfObjects.Where(o => o.GetType() == typeof(Random)).Select(o => (Random) o).ToList();
}
```

Abbiamo quindi il metodo `OfType` di LINQ, il metodo `Where` con `as` e `is`, il metodo `Cast<>` e l'hard cast e infine questo ultimo filtrato sul `GetType`.

Questi sono i risultati:

|         Method |     Mean |    Error |    StdDev |
|--------------- |---------:|---------:|----------:|
|         OfType | 662.9 us | 51.65 us | 152.29 us |
|         CastAs | 687.1 us | 62.73 us | 182.00 us |
|         CastIs | 591.5 us | 28.46 us |  83.90 us |
|     HardCastAs | 288.0 us |  8.65 us |  24.10 us |
|     HardCastIs | 289.8 us |  9.97 us |  28.93 us |
| HardCastTypeOf | 235.2 us |  3.60 us |   8.77 us |

Anche se il metodo `GetType()` viene associato alle reflection, le quali sono spesso lente e non performanti, in questo caso ho invece le performance migliori: conviene sempre fare i propri benchmark prima di fare delle assunzioni sulle performance del codice.

Si noti che che la differenza di performance non è gigantesca tra i vari metodi, conviene scegliere la soluzione esteticamente più chiara e semplice, quindi il metodo `OfType` invece di sovraottimizzare ([Keep it Simple, Stupid](https://it.wikipedia.org/wiki/KISS_(principio))).

Qualora avessimo la necessità di rendere il codice molto performante possiamo optare per l'hard cast filtrando sul `GetType`.
