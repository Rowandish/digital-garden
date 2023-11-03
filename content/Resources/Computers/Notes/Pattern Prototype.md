---
tags:
  - Coding
  - CreationalDesignPattern
  - PublishedPosts
---


Il design pattern prototype è uno dei pattern creazionali fondamentali introdotti dalla Gang of Four e permette di **creare nuovi oggetti clonando un oggetto iniziale**, detto appunto *prototipo*.
A differenza di altri pattern come *Abstract factory* o *Factory* permette di **specificare nuovi oggetti a tempo d'esecuzione (run-time)**, utilizzando una `PrototypeFactory` per salvare e reperire dinamicamente le istanze degli oggetti desiderati.
Questo pattern può rivelarsi utile quando:
- le classi da istanziare **==sono specificate solamente a tempo d'esecuzione==**, per cui un codice statico non può occuparsi della creazione dell'oggetto;
- quando ==**le istanze di una classe possono avere soltanto un limitato numero di stati**==, per cui può essere più conveniente clonare al bisogno il prototipo corrispondente piuttosto che creare l'oggetto e configurarlo ogni volta.
I vantaggi nel suo utilizzo sono i seguenti:
- **Indipendenza dal metodo d'instanziazione**: analogamente ai pattern *Abstract factory* e *Builder*, *Prototype* permette di **incapsulare al suo interno la modalità di istanziazione degli oggetti**, liberando i Client dalla necessità di conoscere i nomi delle classi da instanziare.
- **Modularità a run-time**: l'aggiunta di un prodotto richiede semplicemente la **registrazione dell'oggetto da clonare alla `PrototypeFactory`.
- **Definire nuovi oggetti modificando valori**: Quando si devono **definire numerosi oggetti differenziati tra loro solo dai valori che assumono le loro variabili interne** è più comodo istanziare nuovi oggetti semplicemente clonando un prototipo iniziale e successivamente impostare la rappresentazione interna perché assuma la configurazione desiderata.
- **Minore necessità di sottoclassi**: Il pattern *Prototype* permette di risolvere un problema di *Factory* relativo alla dimensione della gerarchia di classi necessarie: usando un metodo *factory* è necessario creare sottoclassi per inserire un nuovo prodotto e, se si hanno numerosi prodotti molto simili tra di loro, la definizione di una nuova classe per ognuno può portare a grandi quantità di codice duplicato.

La difficoltà principale nell'utilizzo del pattern è l'implementazione del metodo `Clone` in quanto  deve comportarsi come una copia in profondità (*deep copy*): **la copia di un oggetto composto implichi la copia delle sue sottoparti**.

> [!info] Title
> In .NET il pattern è disponibile utilizzando l'interfaccia `ICloneable`.

## Implementazione

Questo pattern è formato dai seguenti oggetti:
- `Prototype`: Definisce un'interfaccia per clonare sé stesso.
- `ConcretePrototype`: Le sottoclassi `ConcretePrototype` implementano l'interfaccia di `Prototype`, **fornendo un'operazione per clonare sé stessi**.
- `Client`: crea un nuovo oggetto del tipo desiderato **chiedendo a un prototipo di clonarsi**, ovvero invocando il metodo clone definito da `ConcretePrototype`.

![[prototype.png]]

Ho creato l'interfaccia `IPrototype` che eredita da `ICloneable` con i suoi prototype concreti e la classe factory.

```csharp
/// <summary>
///     Interfaccia dell'oggetto che voglio clonare
/// </summary>
public interface IPrototype : ICloneable
{
    /// <summary>
    ///     Guid: identificativo univoco di ogni singola istanza
    /// </summary>
    Guid Guid { get; }

    /// <summary>
    ///     Property name public modificabile dall'esterno. Tipicamente verrà fornita una nuova istanza della classe e poi sarà
    ///     il chiamante
    /// </summary>
    string Name { get; set; }
}

/// <summary>
///     Oggetto concreto di tipo "Foo"
/// </summary>
public class ConcretePrototypeFoo : IPrototype
{
    /// <summary>
    ///     Stringa costante interna
    /// </summary>
    private const string Status = "Foo Status";

    /// <summary>
    ///     Identificativo univoco che cambia ad ogni clone
    /// </summary>
    public Guid Guid { get; private set; }

    /// <summary>
    ///     Property modificabile dall'esterno
    /// </summary>
    public string Name { get; set; } = "Foo Name";

    /// <summary>
    ///     Effettuo il Clone modificando il Guid interno
    /// </summary>
    public object Clone()
    {
        var clone = (ConcretePrototypeFoo)MemberwiseClone();
        clone.Guid = Guid.NewGuid();
        return clone;
    }

    public override string ToString()
    {
        return $"Name: {Name} - Status: {Status} - Guid: {Guid}";
    }
}

/// <summary>
///     Oggetto concreto di tipo "Bar"
/// </summary>
public class ConcretePrototypeBar : IPrototype
{
    /// <summary>
    ///     Stringa costante interna
    /// </summary>
    private const string Status = "Bar Status";

    /// <summary>
    ///     Identificativo univoco che cambia ad ogni clone
    /// </summary>
    public Guid Guid { get; private set; }

    /// <summary>
    ///     Property modificabile dall'esterno
    /// </summary>
    public string Name { get; set; } = "Bar Name";

    /// <summary>
    ///     Effettuo il Clone modificando il Guid interno
    /// </summary>
    public object Clone()
    {
        var clone = (ConcretePrototypeBar)MemberwiseClone();
        clone.Guid = Guid.NewGuid();
        return clone;
    }

    public override string ToString()
    {
        return $"Name: {Name} - Status: {Status} - Guid: {Guid}";
    }
}

/// <summary>
///     Factory che permette la creazioni di classi di tipo <see cref="IPrototype" /> clonando il prototype base ogni volta
///     che viene richiesta una nuova istanza. Invece di creare ogni volta una classe da zero parto già da un prototipo con
///     tutti i suoi campi e poi eventualmente effettuo delle modifiche alle property che mi servono
/// </summary>
public class PrototypeFactory
{
    /// <summary>
    ///     Dizionario contenente le istanze base dei prototipi che posso creare. Quando mi viene richiesto un nuovo prototipo
    ///     parto da questi e ne effettuo il Clone() senza che il mondo esterno se ne accorga
    /// </summary>
    private static readonly IDictionary<RecordType, IPrototype> Prototypes = new Dictionary<RecordType, IPrototype>();

    /// <summary>
    ///     Costruttore: crea le istanze di tutti i prototipi che poi andrò a creare
    /// </summary>
    public PrototypeFactory()
    {
        Prototypes.Add(RecordType.Foo, new ConcretePrototypeFoo());
        Prototypes.Add(RecordType.Bar, new ConcretePrototypeBar());
    }

    /// <summary>
    ///     Fornisce una nuova istanza di una classe di tipo <see cref="IPrototype" /> partendo dal <paramref name="type" />
    ///     passato in ingresso
    /// </summary>
    public IPrototype CreatePrototype(RecordType type)
    {
        return Prototypes[type].Clone() as IPrototype;
    }
}

/// <summary>
///     Tipologie di classi <see cref="IPrototype" /> che posso creare
/// </summary>
public enum RecordType
{
    Foo,
    Bar
}
```
Chiamiamo ora il pattern dall'esterno:
```csharp
var prototypeFactory = new PrototypeFactory();
var foo = prototypeFactory.CreatePrototype(RecordType.Foo);
Console.WriteLine($"Creo il prototype Foo: {foo}");
foo = prototypeFactory.CreatePrototype(RecordType.Foo);
foo.Name = "NewName";
Console.WriteLine($"A partire dal clone dello standard ci cambio nome (e guid): {foo}");
Console.WriteLine($"Creo il prototype Bar: {prototypeFactory.CreatePrototype(RecordType.Bar)}");
Console.WriteLine($"Creo un secondo prototype Bar clonando il primo: {prototypeFactory.CreatePrototype(RecordType.Bar)}");
```
Che mostra questo:
```
Creo il prototype Foo: Name: Foo Name - Status: Foo Status - Guid: fb61fb21-4cea-45d0-ab2e-c0c1fc5e843e
A partire dal clone dello standard ci cambio nome (e guid): Name: NewName - Status: Foo Status - Guid: 327baa46-e4a8-4a25-8203-675a5834
2ca0
Creo il prototype Bar: Name: Bar Name - Status: Bar Status - Guid: 82a20aa0-71d8-423c-a8ee-8f16a8316cd0
Creo un secondo prototype Bar clonando il primo: Name: Bar Name - Status: Bar Status - Guid: 05b09aa8-990d-4d69-820d-6585f85944d6
```
