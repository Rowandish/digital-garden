---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


Il linguaggio C# permette di creare delle proprietà di una classe particolari, queste vengono chiamate **proprietà indexed default**.
L'idea è poter fare una cosa del genere:
```csharp
Test t = new Test();
string value = t[1];
// value assume un valore in base a quanto è stato definito nella classe Test
```
Come si vede dall'esempio indicato sopra, voglio poter accedere ad una classe come se fosse una specie di array, anche se ovviamente questo non è.
Spesso questo comportamento viene implementato quando la classe interna ha effettivamente una `List` o un `Dictionary` come proprietà e creo questo modo comodo per potervi accedere.
Proseguiamo la spiegazione con un esempio, preso da [questo link](http://pietschsoft.com/post/2007/03/17/c-give-your-object-a-default-indexer-property).
Assumiamo di avere un oggetto Club con al suo interno una List di oggetti Person, ed inoltre ha una default indexer property per poter accedere a tale lista
```csharp
public class Club
{
/// Collection of Person objects in the Club
private List<Person> people = new List<Person>();
public List<Person> People { get; set; }

/// The Default property of the Club object
public Person this[int index]
{
get { return people[index]; }
set { people[index] = value; }
}
}

public class Person
{
private string _name;
public Person(string name)
{
_name = name;
}
public string Name {get; set;}
}
```
In questo modo posso correttamente scrivere il seguente codice:
```csharp
Club club = new Club();
club.People.Add(new Person("Chris"));
// Cambio il nome della prima persona usando il metodo tradizionale
club.People[0].Name = "Joe";
// Cambio il nome della prima persona usando il metodo tradizionale usando la default property
club[0].Name = "John";
```
Come per ogni altro metodo di una classe, anche queste particolari proprietà possono subire un overload, posso quindi avere un accesso tramite indice con un intero e anche con una stringa, la quale potrebbe fare, per esempio, un dictionary lookup.