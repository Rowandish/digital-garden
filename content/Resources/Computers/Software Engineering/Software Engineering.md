Per essere un buon programmatore è per prima cosa seguire i [[Principi di buona programmazione]] e, in secondo luogo, conoscere i pattern e i principi SOLID.

## Design Pattern
I design pattern sono spesso divisi in tre categorie (vedi *Gamma Categorization*)
### Creazionali
Si occupano della costruzione di oggetti, si dividono in espliciti (costruttori) o impliciti ([[Dependency Injection Framework|DI]], Reflection) e in *wholesale* (una singola istruzione) e *piecewise* (step-by step).

* [[Pattern Builder]]
* [[Pattern Prototype]]
* [[Pattern Singleton]]
* [[Pattern Factory]]
* **Prototype**: crea un oggetto a partire da un oggetto esistente. Richiede il concetto di `deep copy` dell'oggetto.

### Strutturali
Si occupano della struttura della classe (esempio property e field), e sono tipicamente dei wrapper che mascherano la struttura interna della classe
* **Adapter**: converte l'interfaccia che ottieni da un metodo nell'interfaccia che ti serve;
* **Bridge**: effettua il decoupling dell'astrazione dalla sua implementazione;
* **Composite**: permette di trattare un singolo oggetto o un insieme degli stessi allo stesso modo implementando `Ienumerable<T>`;
* **Decorator**: aggiunge ulteriori responsabilità ad un oggetto;
* **Facade**: fornisce un'interfaccia singola unificata per un insieme di classi/sistemi;
* **Flyweight**: permette di gestire in un gran numero di oggetti simili;
* **Proxy**: fornisce un oggetto surrogato che inoltra le chiamate al vero oggetto sotto al cofano effettuando anche funzioni ulteriori.
### Comportamentali
Si occupano genericamente del comportamento di classi; sono tutti diversi, non hanno un tema centrale.

* **Chain of responsibility**: permette ai componenti di processare le informazioni in una catena in cui ogni elemento ha un riferimento all'elemento successivo;
* **Command**: incapsula una richiesta in un oggetto separato;
* **Iterator**: fornisce un'interfaccia per accedere agli elementi di un oggetto aggregato tramite `Ienumerable<T>`;
* **Mediator**: fornisce una mediazione tra due oggetti (esempio chat room);
* **Memento**: gestisce il passaggio di stato di un oggetto, permettendo l'undo/redo;
* **Observer**: permette di osservare il comportamento di un oggetto e venire notificato. Incapsulato nella keyword `event`in .NET;
* [[Pattern State]]: gestisce il concetto di *macchina a stati*;
* **Strategy/Template**: permette di modificare runtime il comportamento di un oggetto;
* **Visitor**: aggiunge funzionalità ad una classe tramite il *double dispatch*;
* [[Special Case Pattern]]

## Principi SOLID

* [[Principi SOLID. Single responsibility|Single responsibility]]
* [[Principi SOLID. Open-closed principle|Open-closed principle]]
* [[Principi SOLID. Liskov Substitution Principle|Liskov Substitution Principle]]
* [[Principi SOLID. Interface segregation principle|Interface segregation principle]]
* [[Principi SOLID. Dependency Inversion Principle|Dependency Inversion Principle]]

## Altro
* [[Dependency Injection Framework]]