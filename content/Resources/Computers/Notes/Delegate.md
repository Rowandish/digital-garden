---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


## 1. Introduzione
La parte introduttiva dell'articolo è presa direttamente dala [documentazione ufficiale MSDN](https://msdn.microsoft.com/it-it/library/ms173172.aspx).

* * *
Un *delegate* è un **tipo che incapsula un metodo**, simile a un puntatore a funzione in C e C++.

A differenza dei puntatori a funzione, tuttavia, **i delegati sono orientati a oggetti, indipendenti dai tipi e sicuri**.

Un delegate deve essere usato per comunicare all'utilizzatore della classe sviluppata: "*Sentiti libero di usare qualsiasi metodo che rispetta la firma che ti fornisco e questo verrà chiamato correttamente*".

I delegate sono utili per offrire all'utilizzatore dei miei oggetti l'abilità di **personalizzarne il comportamento**, separando in ogni caso la classe dal suo utilizzatore.

Spesso è possibile ottenere lo stesso comportamento con modalità alternative all'utilizzo dei delegate (un esempio è l'utilizzo del pattern *Strategy*), ma spesso questi sono il modo più semplice e pulito per ottenere questi comportamenti.

Nell'esempio seguente viene dichiarato un delegato denominato `Del` che può incapsulare un metodo che accetta una stringa come argomento e restituisce `void`:

```csharp
public delegate void Del(string message);
```

Un oggetto delegato viene normalmente creato in due modi:

- **fornendo il nome del metodo** di cui il delegato eseguirà il wrapping
- con un **metodo anonimo** (funzioni lambda)

I parametri passati al delegato dal chiamante vengono passati al metodo e il valore restituito, se presente, dal metodo viene restituito al chiamante dal delegato.

Se creasi una funzione con la stessa firma del delegato, posso richiamarla in questo modo:

```csharp
//Stessa firma del delegate
public static void DelegateMethod(string message){
System.Console.WriteLine(message);
}

// Istanzio un oggetto di tipo Del con la funzione sopra
Del handler = DelegateMethod;

// Chiamo la funzione
handler("Hello World");
```

Poiché l'istanza del delegato è un oggetto, può essere passata come parametro o assegnata a una proprietà; in questo modo **un metodo può accettare un delegato come parametro e chiamare il delegato in un secondo momento**.

Questa operazione è nota come **callback asincrono** ed è un metodo comune per notificare un chiamante al termine di un processo lungo.

Quando un delegato viene usato in questo modo, **per il codice che usa il delegato non è richiesta alcuna conoscenza dell'implementazione del metodo in uso**. La funzionalità è simile all'incapsulamento fornito dalle interfacce.

Un altro utilizzo comune dei callback è la definizione di un metodo di confronto personalizzato e il passaggio di tale delegato a un metodo di ordinamento. Consente al codice del chiamante di entrare a far parte dell'algoritmo di ordinamento. Nell'esempio di metodo seguente viene usato il tipo `Del` come parametro:

```csharp
public void MethodWithCallback(int param1, int param2, Del callback)
{
  callback("The number is: " + (param1 + param2).ToString());
}
```
È quindi possibile passare il delegato creato in precedenza a tale metodo:

```csharp
MethodWithCallback(1, 2, handler);
```
E ottenere come risultato:

```csharp
The number is: 3
```

## 2. Multicasting
Assumiamo di aver definito la seguente classe

```csharp
public class MethodClass
{
  public void Method1(string message) { }
  public void Method2(string message) { }
}
```
**Un delegato può chiamare più di un metodo, quando viene richiamato**. Questo processo viene definito **multicasting**. Per aggiungere un ulteriore metodo all'elenco dei metodi del delegato (l'elenco chiamate), è necessario semplicemente **aggiungere due delegati usando gli operatori addizione o di assegnazione di addizione** ("+" o "+=").

Ad esempio:

```csharp
MethodClass obj = new MethodClass();
Del d1 = obj.Method1;
Del d2 = obj.Method2;
Del d3 = DelegateMethod;

//Both types of assignment are valid.

Del allMethodsDelegate = d1 + d2;
allMethodsDelegate += d3;
```
A questo punto `allMethodsDelegate` contiene tre metodi nel relativo elenco chiamate: `Method1`, `Method2` e `DelegateMethod`.

**Quando si richiama `allMethodsDelegate`, tutti e tre i metodi vengono chiamati nell'ordine**.

Se il delegato usa **parametri di riferimento**, il riferimento viene passato in sequenza a ciascuno dei tre metodi a turno e le eventuali **modifiche apportate da un solo metodo saranno visibili al metodo successivo**.

Per **rimuovere un metodo dall'elenco chiamate**, usare l'operatore di **decremento** o l'operatore di decremento di assegnazione ("-" o "-="'). Ad esempio:

```csharp
//remove Method1
allMethodsDelegate -= d1;

// copy AllMethodsDelegate while removing d2
Del oneMethodDelegate = allMethodsDelegate - d2;
```
**I delegati multicast vengono ampiamente usati nella gestione degli eventi**.

## 3. Metodi anonimi ed espressioni lambda
(questa sezione proviene da [questo post](http://www.albertobarbazza.it/Programming/Lambda_expression_it.aspx))
Di solito **per assegnare una funzione a un delegato si scrive la funzione separatamente e si assegna al delegato il nome della funzione**, invece con i metodi anonimi si può **assegnare direttamente la funzione stessa**, ecco un esempio:

```csharp
delegate int MyDelegate(int a);
...

MyDelegate d = delegate(int a) { return a * 10; }
```
In questo modo non è necessario creare un metodo apposta. I metodi anonimi possono essere utili in vari casi ad esempio per passare la funzione di avvio di un thread.

```csharp
Thread t = new Thread(
  delegate()
  {
    thread code ... ;
  });
  t.Start();
```
Una **particolare forma di metodo anonimo sono le lambda expression** utilizzate ad esempio in LINQ.

Nelle espressioni lambda compare l' operatore lambda "=>" che si legge "fino a", **alla sua sinistra vi sono i parametri di input** (possono mancare) e **alla sua destra il codice del metodo**, che spesso si riduce ad una espressione, ma può essere complesso a piacere, quindi:

```csharp
parametri => metodo
```
Ora assumiamo di aver definito il seguente delegato:

```csharp
delegate int MyFunc(int i);
```
Questo può essere inizializzato con due modalità, un metodo anonimo o una espressione lambda:

```csharp
// Esempio con metodo anonimo:
MyFunc p = delegate(int i) { return i * 10; }

// La stessa cosa con una lambda expression
MyFunc p = i => i* 10;
```
In questo caso il compilatore **deduce il tipo di '*i*' e del valore di ritorno in base al tipo del delegato**.

Qualora via siano **più parametri** scrivo

```csharp
(x, y) => x + y;
```
Si possono specificare anche **i tipi dei parametri** in ingresso quando il compilatore non li può dedurre:

```csharp
(double x, string s) => s.Length + x;
```
Infine quando **non vi sono parametri** si usano le parentesi vuote:

```csharp
() => DateTime.Now.Year % 2000;
```
Se invece il metodo contiene **più parametri** devo racchiuderlo tra parentesi graffe:

```csharp
p => { int a = p * 2; return a + 1; }
```

## 4. I delegate e i generics
Essendo i delegate delle classi, è possibile **sfruttare i generics per creare delle strutture facilmente riutilizzabili e versatili**.

All'interno del framework .NET sono presenti un gran numero di delegate generici già fatti da poter riutilizzare, in particolare seguenti:
- **Action**: `Action<TParameter>`: un delegate che prende da 0 a 8 parametri in ingresso e non ritorna nulla
- **Func**: `Func<TParameter, TResult>`: un delegate che prende da 0 a 8 parametri in ingresso e che ritorna un valore o una referenza (di tipo `TResult`)
- **Predicate**: è un wrapper di `Func<T, bool>`, viene usata per il compare di oggetti.

Analizziamoli uno ad uno.+

### 4.1 `Func<TParameter, TOutput>`
`Func` è logicamente simile all'implementazione base dei delegate. La differenza è il modo in cui questa viene dichiarata:

```csharp
Func<string, int, int> tempFuncPointer;
```
**I primi due parametri sono i parametri in ingresso del metodo**, mentre l'ultimo parametro è un parametro in `out` che deve essere il **tipo di dato di ritorno dal metodo**.

```csharp
Func<string, int, int> tempFuncPointer = tempObj.FirstTestFunction;
int value = tempFuncPointer("hello", 3);
```
### 4.2 `Action<TParameter>`
`Action` è usato quando la funzione **non ha parametri in uscita**.

```csharp
Action<string, int> tempActionPointer;
```
Analogamente a `Func`, i parametri indicati sono i parametri in ingresso alla funzione, con la differenza che questa non ne ritorna nessuno.

```csharp
Action<string, int> tempActionPointer = tempObj.ThirdTestFunction;
tempActionPointer("hello", 4);
```

### 4.3 `Predicate<in T>`
Predicate è **un tipo `Func` che ritorna un valore booleano**. E' spesso usato nell'analizi di liste di oggetti.

La dichiarazione è la seguente

```csharp
Predicate<Employee> tempPredicatePointer;
```
in questo caso la funzione `tempPredicatePointer` prende in ingresso un oggetto `Employee` e ritorna true se `Employee.age < 27`:

```csharp
public bool FourthTestFunction(Employee employee)
{
  return employee.Age < 27;
}
```

## 5. Delegate come interfacce anonime
La seguente idea proviene da [questo post](http://blog.ploeh.dk/2009/05/28/DelegatesAreAnonymousInterfaces/) di Mark Seemann.

* * *
I delegate possono essere visti a tutti gli effetti come **interfacce anonime formate da un solo metodo**.

Consideriamo un semplice esempio, ho la classe `MyClass` che che possiede un metodo `DoStuff`. Questo metodo prende in ingresso un oggetto astratto (`IMyInterface`) che deve avere il metodo `DoIt` il quale, data una stringa, fornisce un intero.

Nella programmazione ad oggetti classica abbiamo:

```csharp
public interface IMyInterface
{
  int DoIt(string message);
}
```

```csharp
public string DoStuff(IMyInterface strategy)
{
  return strategy.DoIt("Ploeh").ToString();
}
```
Ma definire una nuova interfaccia solo per fare questo non è necessario, possiamo utilizzare il tipo `Func<string, int>` nel seguente modo:

```csharp
public string DoStuff(Func<string, int> strategy)
{
  return strategy("Ploeh").ToString();
}
```
Questo metodo ci **risparmia sia di definire una nuova interfaccia, che di implementare tale interfaccia per definire il metodo `DoStuff`**.

Possiamo invece definire il codice scritto sopra con una lambda function:

```csharp
string result = sut.DoStuff(s => s.Count());
```
Ovviamente questa tecnica funziona bene quando ho l'astrazione di un singolo metodo: appena la mia struttura prevede l'introduzione di un secondo metodo, l'utilizzo di un interfaccia o di una classe astratta è obbligatorio.

## 6. Delegate per evitare lo switch case
In accordo con la [antiifcampaign](http://antiifcampaign.com/) è una pratica di buona programmazione **ridurre al minimo l'utilizzo degli if basati sul confronto tra una variabile e n costanti**, come nel seguente esempio:

```csharp
if(input == "foo")
{
  Writeln("some logic here");
}
else if(input == "bar")
{
  Writeln("something else here");
}
else if(input == "raboof")
{
  Writeln("of course I need more than just Writeln");
}
```
Esistono due modalità di buona programmazione che eliminano questo caso:

- il pattern strategy (che approfondirò in un articolo successivo);
- i delegate.

Analizziamo il secondo metodo: **creiamo un dizionario che associa una stringa ad una funzione delegata**

```csharp
delegate void DoStuff();
IDictionary<string, DoStuff> dict = new Dictionary<string, DoStuff>();
dict["foo"] = delegate { Console.WriteLine("some logic here"); };
dict["bar"] = delegate { Console.WriteLine("something else here"); };
dict["raboof"] = delegate { Console.WriteLine("of course I need more than just Writeln"); };
```
Ogni funzione presente come valore nel dizionario indica una logica da implementare nell'if.

Per richiamare la funzione corretta in base alla variabile `input` basta eseguire il seguente codice:

```csharp
dict["foo"]();
```
