---
tags:
  - Coding
  - CreationalDesignPattern
  - PublishedPosts
---


## Introduzione

Il design pattern Builder, come tutti i pattern creazionali, **separa la costruzione di un oggetto complesso dalla sua rappresentazione** cosicché il processo di costruzione stesso possa creare diverse rappresentazioni.
In particolare questo pattern è utilizzato **quando l'oggetto deve essere creato mediante vari step ed è il builder che mantiene lo stato di tutti gli step**.
Alla fine della creazione l'oggetto viene ritornato.
Il pattern builder si può riconoscere in una classe che ha un solo metodo di creazione e vari metodi per configurare l'oggetto creato.
Un'esempio classico è la classe `StringBuilder`, che permette di costruire una stringa mediante vari step e fornirla solo alla fine.

### Rapporto con altri pattern creazionali
Il pattern creazionale più semplice è il [[Pattern Factory]] e generalmente si parte sempre da quello. Se il pattern genera troppe sottoclassi spesso conviene migrare verso l'`Abstract Factory`, il [[Pattern Prototype]] o il `Builder`, che sono più flessibili ma leggermente più complessi.

### Differenze con il pattern `Factory`
- Il `Builder` si focalizza sulla costruzione di un oggetto complesso **step by step**. [[Pattern Factory]] fornisce una determinato oggetto a partire da una famiglia in base ad un parametro in ingresso.
- Anche il `Builder` può creare vari sottoclassi in base al parametro in ingresso ma con una maggiore granularità nella loro creazione: esempio se il `Factory` ritorna come istanze di `Car` `Honda` e `Ford`, il `Builder` potrebbe ritornare una `Honda 4 cilindri` e una `Honda a 6 cilindri` in base alla configurazione. Il pattern `Factory` può essere visto come una versione semplificata del `Builder`.
- Il `Builder` restituisce il prodotto come **passo finale del processo di creazione**, mentre per quanto riguarda il `factory` o `Abstract Factory`, il prodotto viene ritornato immediatamente.

## Struttura
- `(Abstract) Builder`: è la classe astratta che viene utilizzata dall'esterno per creare le parti dell'oggetto `Product`. Ha questo come variabile di stato e vari metodi, da chiamare all'esterno, per assemblarlo.
- `ConcreteBuilder`: costruisce e assembla le parti del `Product` implementando l'interfaccia `Builder`. Aggiorna l'istanza della classe `Product` della classe padre.
- `Director`: costruisce un oggetto utilizzando l'interfaccia `Builder`. Lo scopo del Director è eseguire i passi della costruzione dell'oggetto in un particolare ordine, o solo alcuni passi, in base ai metodi chiamati dall'esterno. Questa classe non è obbligatoria nel pattern in quanto il client può fare la stessa operazione, ha senso solo se ho varie configurazioni diverse dello stesso oggetto da costruire.
- `Product`: rappresenta l'**oggetto complesso** che voglio costruire.

## Funzionamento
- Il `Client` crea un oggetto `Director` ne imposta l'oggetto `Builder`;
- Il `Director` notifica al `Builder` se una parte del prodotto deve essere costruita in base alle richieste del `Client`, il `Builder` riceve le richieste dal `Director` e aggiunge le parti al prodotto.
- Il `Client` riceve il prodotto dal `Builder` e lo utilizza.

### Esempio

#### Product
Classe `Product`, il prodotto complesso. In questo caso ho una lista di stringa come attributo ma nel mondo reale potrebbero essere anche oggetti più complessi.
Notare come il costruttore sia vuoto e di come gli attributi vengano creati con un metodo (o dei setter), caratteristica tipica del pattern builder, che **separa la costruzione di un oggetto dalla sua logica interna**.
```csharp
public class Product
{
    private readonly IList<string> _parts = new List<string>();

    public void Add(string part)
    {
        _parts.Add(part);
    }

    public string ListParts()
    {
        return $"Product parts: {string.Join(", ", _parts)}";
    }
}
```

#### AbstractBuilder

Il `Builder` è una classe astratta che indica **come bisogna creare l'oggetto `Product`**.
In questo caso quindi indica che per creare l'oggetto Product posso crearne la parte A, B o C (o tutte insieme) tramite i metodi `BuildPartA`, `BuildPartB` e `BuildPartC`.
Fornisce inoltre i metodi per **ottenere il product** e per **crearne uno nuovo**.
```csharp
/// <summary>
///     Il pattern builder  separa la costruzione di un oggetto complesso dalla sua rappresentazione, in modo che il
///     processo di costruzione stesso possa creare diverse rappresentazioni.
///     Ciò ha l'effetto immediato di rendere più semplice la classe, permettendo a una classe builder separata di
///     focalizzarsi sulla corretta costruzione di un'istanza e lasciando che la classe originale si concentri sul
///     funzionamento degli oggetti.
///     Il pattern builder si può riconoscere in una classe che ha un solo metodo di creazione e vari metodi per
///     configurare l'oggetto creato.
///     Differenze con il Factory: il Builder si focalizza sulla costruzione di un oggetto complesso "step by step".
///     Factory enfatizza una famiglia di oggetti (sia semplici che complessi).
///     Il Builder restituisce il prodotto come passo finale del processo di creazione, mentre per quanto riguarda
///     l'Abstract Factory, il prodotto viene ritornato immediatamente.
/// </summary>
public abstract class AbstractBuilder
{
    protected Product Product;

    /// <summary>
    ///     Costruttore, istanzia un nuovo <see cref="Product" />
    /// </summary>
    protected AbstractBuilder()
    {
        CreateNewProduct();
    }

    /// <summary>
    ///     Crea una nuova istanza di <see cref="Product" />
    /// </summary>
    public void CreateNewProduct()
    {
        Product = new Product();
    }

    /// <summary>
    ///     Costruisco la parte A dell'oggetto
    /// </summary>
    public abstract void BuildPartA();

    /// <summary>
    ///     Costruisco la parte B dell'oggetto
    /// </summary>
    public abstract void BuildPartB();

    /// <summary>
    ///     Costruisco la parte C dell'oggetto
    /// </summary>
    public abstract void BuildPartC();

    /// <summary>
    ///     Questo metodo fornisce il prodotto costruito. Opzionalmente posso chiamare anche il metodo <see cref="CreateNewProduct" /> che
    ///     annulla l'istanza; dipende dalle esigenze
    /// </summary>
    public Product GetProduct()
    {
        var result = Product;

        CreateNewProduct();

        return result;
    }
}
```

#### Concrete Builder
Implementa l'`Abstract Builder` implementando **solo** i metodi astratti della costruzione dell'oggetto.
```csharp
/// <summary>
///     Costruisce e assembla le parti del prodotto implementando l'interfaccia Builder; definisce e tiene traccia della
///     rappresentazione che crea.
///     Il builder concreto è figlio dell'interfaccia e fornisce le implementazioni dei vari step, in questo modo posso
///     avere n builder diversi che producono lo stesso oggetto.
/// </summary>
public class ConcreteBuilder : AbstractBuilder
{
    /// <summary>
    ///     Tutti i metodi per la creazione dell'oggetti utilizzano la stessa istanza di <see cref="Product" />
    /// </summary>
    public override void BuildPartA()
    {
        Product.Add("PartA1");
    }

    public override void BuildPartB()
    {
        Product.Add("PartB1");
    }

    public override void BuildPartC()
    {
        Product.Add("PartC1");
    }
}
```
#### Director
Il **Director** è colui che effettivamente si occupa della **creazione dell'oggetto `Product` a partire da un `Builder`**.
Avrà quindi sempre un setter che gli imposta il tipo di `Builder` da utilizzare, un metodo che fornisce l'oggetto `Product` e un metodo che lo costruisce utilizzando i metodi del `Builder`.
Notare come il `Director` sia **l'unico oggetto a sapere come si costruisce il `Product`**, è lui a chiamare i metodi `BuildPartA`, `BuildPartB` e `BuildPartC`.
```csharp
/// <summary>  
///     Il Director costruisce un oggetto utilizzando l'interfaccia Builder, infatti notifica al Builder se una parte  
///     del prodotto deve essere costruita, il Builder riceve le richieste dal Director e aggiunge le parti al prodotto.  
///     Lo scopo del Director è eseguire i passi della costruzione dell'oggetto in un particolare ordine, o solo alcuni  
///     passi, in base ai metodi chiamati dall'esterno.  
///     In questo caso <see cref="BuildMinimalViableProduct" /> chiamerà solo un metodo del Builder, mentre  
///     <see cref="BuildFullFeaturedProduct" /> chiamerà tutti i metodi.  
///     Questa classe non è obbligatoria nel pattern in quanto il client può fare la stessa operazione, ha senso solo se ho  
///     varie configurazioni diverse dello stesso oggetto da costruire.  
/// </summary>  
public class Director  
{  
    /// <summary>  
    ///     Costruttore: imposta il <paramref name="builder" /> iniziale    /// </summary>    public Director(AbstractBuilder builder)  
    {  
        Builder = builder;  
    }  
  
    /// <summary>  
    ///     Builder impostabile dall'esterno. Obbligo il passaggio anche a costruttore in quanto è obbligatorio avere almeno un    ///     builder impostato    /// </summary>    public AbstractBuilder Builder { get; set; }  
  
    /// <summary>  
    ///     Delega al builder la costruione di un nuovo <see cref="Product" />, in questo caso creando tutte le parti    /// </summary>    public void BuildFullFeaturedProduct()  
    {  
        Builder.CreateNewProduct();  
        Builder.BuildPartA();  
        Builder.BuildPartB();  
        Builder.BuildPartC();  
    }  
  
    /// <summary>  
    ///     Delega al builder la costruione di un nuovo <see cref="Product" /> ma creando solo la parte A    /// </summary>    public void BuildMinimalViableProduct()  
    {  
        Builder.CreateNewProduct();  
        Builder.BuildPartA();  
    }  
  
    /// <summary>  
    ///     Fornisce il <see cref="Product" /> costruito al Client    /// </summary>    public Product GetProduct()  
    {  
        return Builder.GetProduct();  
    }  
}
```

#### Client
Di seguito una invocazione dall'esterno del metodo `Builder`.
Notare che questo metodo offre i seguenti vantaggi per il client esterno:
- Il `Client` non deve conoscere gli attributi e i componenti dell'oggetto complesso `Product`
- Il client deve conoscere solo le tipologie possibili Product, in questo caso che ne esiste una tipologia full optionale `BuildFullFeaturedProduct` e una tipologia base (`BuildMinimalViableProduct`). Non conosce di cosa queste pizze sono composte.
- Il client deve solo creare un `Director` e dirgli il tipo di `Product` da creare, al resto ci pensa lui
- Alla fine del procedimento il `Director` mi fornisce una istanza dell'oggetto `Product` di cui il client non conosce alcunchè.
- Se un giorno volessi creare un nuovo tipo di `Product` basta creare un nuovo oggetto `ConcreteBuilder`, il resto rimane immutato

```csharp
var director = new Director(new ConcreteBuilder());  
Console.WriteLine("Product minimal with standard builder:");  
director.BuildMinimalViableProduct();  
Console.WriteLine(director.GetProduct().ListParts());  
  
Console.WriteLine("Product full optional with standard builder:");  
director.BuildFullFeaturedProduct();  
Console.WriteLine(director.GetProduct().ListParts());  
  
director.Builder = new CustomBuilder();  
Console.WriteLine("Product minimal with custom builder:");  
director.BuildMinimalViableProduct();  
Console.WriteLine(director.GetProduct().ListParts());  
  
Console.WriteLine("Product full optional with custom builder:");  
director.BuildFullFeaturedProduct();  
Console.WriteLine(director.GetProduct().ListParts());  
  
// Il director è opzionale, posso usare direttamente il builder  
Console.WriteLine("Custom product:");  
var builder = new ConcreteBuilder();  
builder.BuildPartA();  
builder.BuildPartC();  
Console.Write(builder.GetProduct().ListParts());
```
Nel mio esempio il client fornisce:
```
Product minimal with standard builder:
Product parts: Standard PartA1
Product full optional with standard builder:
Product parts: Standard PartA1, Standard PartB1, Standard PartC1
Product minimal with custom builder:
Product parts: Custom PartA1
Product full optional with custom builder:
Product parts: Custom PartA1, Custom PartB1, Custom PartC1
Product without builder:
Product parts: Standard PartA1, Standard PartC1-
```
## Rider Live template

Allego il live template per utilizzare questo pattern in Rider o Visual Studio con ReSharper.
![[Builder Rider live template.txt]]