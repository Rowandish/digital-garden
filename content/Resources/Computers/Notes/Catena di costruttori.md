---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


C# offre un metodo estremamente comodo per **scrivere più costruttori di una stessa classe che si richiamano l'un l'altro**.
Questa tecnica è detta *constructor chaining*.
E' possibile inoltre concatenare **costruttori della classe padre tramite il comando `base`**.
Segue un esempio:
```csharp
class Foo {
private int id;
private string name;
// Costruttore effetivo
public Foo(int id, string name) {
this.id = id;
this.name = name;
}
// estensione senza parametri in ingresso
public Foo() : this(0, "") { }
// estensione passando solo l'id
public Foo(int id) : this(id, "") { }
// estensione passando solo il name
public Foo(string name) : this(0, name) { }
// Chiamata del costruttore della superclasse
public Foo(string name) : base(name) { }
}
```
E' importante sottolineare che, qualora non venga utilizzato l'attributo `this`, il compilatore considererà l'estensione con il costrutore della superclasse, analogamente ad aver scritto `base`.
L'ordine con cui questi costruttori viene eseguito segue la logica, in quanto viene chiamato prima il costruttore concatenato, e poi il costruttore effetivamente chiamato dall'esterno.
Per capirne bene il funzionamento indico questo esempio, preso da [questo post](http://csharp.2000things.com/tag/constructor-chaining/).

```csharp
public Dog(string name, int age, string favToy) {
Console.WriteLine("name/age/favToy constructor executing");
}
public Dog(string name, int age) : this(name, age, "ball") {
Console.WriteLine("name/age constructor executing");
}
public Dog(string name) : this(name, 1) {
Console.WriteLine("name constructor executing");
}

Dog dog = new Dog("dog name");

// name/age/favToy constructor
// name/age constructor
// name constructor
```