---
tags:
  - Coding
  - CreationalDesignPattern
  - PublishedPosts
---


## Introduzione

Il **Factory Method** è uno dei design pattern fondamentali per l'implementazione del concetto di **factories**. Come altri pattern creazionali, esso **indirizza il problema della creazione di oggetti senza specificarne l'esatta classe**.
L'idea è utilizzare un **metodo factory** che ritorna una interfaccia dell'oggetto che voglio creare invece di utilizzare direttamente il costruttore della classe.
In questo modo la superclasse o il chiamante utilizzerà l'oggetto senza saperne il suo tipo specifico ma solo la sua interfaccia.
Usare metodi factory spesso non è una grande idea in quanto rompe la [[Principi SOLID. Liskov Substitution Principle]].

## Rapporto con altri pattern creazionali
Il Factory è il pattern creazionale più semplice e tendenzialmente si parte sempre da quello. Se il pattern genera troppe sottoclassi spesso conviene migrare verso l'`Abstract Factory`, il [[Pattern Prototype]] o il [[Pattern Builder]], che sono più flessibili ma leggermente più complessi.

## Factory vs Abstract Factory
Spesso c'è confusione sulla differenza tra i due pattern e quando usare uno invece che l'altro.
Un primo punto fondamentale è che nel `Factory` ho **un solo metodo**, chiamato **metodo factory**, in una classe che potenzialmente può fare anche altro; l'`Abstract Factory` invece prevede la creazione di più classi complesse.
* Il metodo Factory si usa per creare un solo prodotto, l'Abstract Factory invece si occupa di creare famiglie di oggetti o comunque oggetti legati tra loro;
* Nel `Factory` il metodo che costruisce la classe è un normale metodo (da overridare in una classe figlia per specificare l'istanza da creare), mentre nell'`Abstract Factory` viene d**delegata tramite composizione** ad una classe terza; **Il primo usa quindi l'ereditarietà mentre il secondo la composizione**.
* Tipicamente una classe contenente un metodo Factory può contenere anche altri metodi, **non serve solo a creare oggetti**. Una classe factory dell'`Abstract Factory` invece **serve solo a creare oggetti**;
* Il `Factory` nasconde la costruzione di un singolo oggetto, mentre l'`Abstract Factory` di una serie di oggetti;

### Factory
```csharp
internal abstract class A
{
    public abstract IProduct FactoryMethod();

    public string SomeOperation()
    {
        var product = FactoryMethod();
        return product.Operation();
    }
}

internal class B : A
{
    public override IProduct FactoryMethod()
    {
        return new ConcreteProduct1();
    }
}
```
### Abstract Factory
```csharp
internal abstract class A
{
	private Factory factory;

	public A(Factory factory)
	{
		_factory = factory;
	}

    public string SomeOperation()
    {
        var product = _factory.FactoryMethod();
        return product.Operation();
    }
}
```

## Esempio 1 - Ereditarietà
Nell'esempio seguente abbiamo la creazione di oggetti `IProduct`, in particolare `ConcreteProduct1` e `ConcreteProduct2`.
La classe che li crea è la classe `Creator` che definisce solo il metodo astratto, saranno le sue figlie a indicarne la classe concreta.

```csharp
/// <summary>
///     Il metodo Factory fornisce un'interfaccia per creare un oggetto, ma lascia che le sottoclassi decidano quale
///     oggetto istanziare. La creazione dell'oggetto avviene tramite ereditarità.
/// </summary>
internal abstract class Creator
{
    /// <summary>
    ///     Metodo principale della classe che si occupa di creare l'istanza di <see cref="IProduct" />.
    /// </summary>
    public abstract IProduct CreateProduct();

    /// <summary>
    ///     Potenzialmente il creator può anche eseguire delle operazioni sulla classe appena creata (un po' alla Builder)
    /// </summary>
    public string SomeOperation()
    {
        return CreateProduct().Operation();
    }
}

/// <summary>
///     Factory concreta, overrida il metodo per creare <see cref="ConcreteProduct1" />
/// </summary>
internal class ConcreteCreator1 : Creator
{
    public override IProduct CreateProduct()
    {
        return new ConcreteProduct1();
    }
}
/// <summary>
///     Factory concreta, overrida il metodo per creare <see cref="ConcreteProduct2" />
/// </summary>
internal class ConcreteCreator2 : Creator
{
    public override IProduct CreateProduct()
    {
        return new ConcreteProduct2();
    }
}

/// <summary>
///     Oggetto generico che deve essere creato, fornisce le operazioni che tutti i prodotti concreti devono avere
/// </summary>
public interface IProduct
{
    string Operation();
}

/// <summary>
///     Ho varie tipologie di prodotti concreti
/// </summary>
internal class ConcreteProduct1 : IProduct
{
    public string Operation()
    {
        return "{Result of ConcreteProduct1}";
    }
}

internal class ConcreteProduct2 : IProduct
{
    public string Operation()
    {
        return "{Result of ConcreteProduct2}";
    }
}
```

### Client
Utilizzare il metodo Factory viene utilizzato principalmente perchè così **il client non istanzia gli oggetti effettivi e non conosce nemmeno come sono fatti**: delega alla factory la creazione e poi il client si occupa solo di creare gli oggetti specifici.
```csharp
var product1 = new ConcreteCreator1().CreateProduct();  
var product2 = new ConcreteCreator2().CreateProduct();  
Console.WriteLine($"Product made by concrete creator 1: {product1.Operation()}"); // Product made by concrete creator 1: {Result of ConcreteProduct1}
Console.WriteLine($"Product made by concrete creator 2: {product2.Operation()}"); // Product made by concrete creator 2: {Result of ConcreteProduct2}
```

## Esempio 2 - Switch Case
Una versione semplificata è quella in cui non ho factory figlie della factory astratta principale ma è tutto racchiuso un un metodo e la decisione se istanziare la classe A o B è all'interno di uno switch case.
Un esempio banale è il seguente:
```csharp
internal class CreatorWithSwitchCase
{
    public IProduct CreateProduct(string type)
    {
        switch (type)
        {
            case "Concrete1": return new ConcreteProduct1();
            case "Concrete2": return new ConcreteProduct2();
            default: throw new ArgumentException("type");
        }
    }
}
```
### Client
Il client chiamerà la factory e in base al parametro in ingresso verrà fornita una istanza o l'altra.
```csharp
var factory = new CreatorWithSwitchCase();  
var product1 = factory.CreateProduct("Creator1");  
var product2 = factory.CreateProduct("Creator2");
```

## Rider Live template

Allego il live template per utilizzare questo pattern in Rider o Visual Studio con Resharper.
![[Factory Rider live template.txt]]