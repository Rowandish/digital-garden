---
tags:
  - Coding
  - SOLID
  - PublishedPosts
---
L'ISP si concentra sulla struttura e l'organizzazione delle interfacce all'interno di un'applicazione, ==promuovendo l'uso di interfacce più piccole e specifiche invece di interfacce grandi e generiche==.

L'ISP è stato introdotto da Robert C. Martin e afferma che "==le classi che implementano interfacce non dovrebbero essere costrette a implementare metodi di cui non hanno bisogno==". In altre parole, le interfacce dovrebbero essere suddivise in componenti più piccoli e specifici per garantire che le classi che le implementano abbiano solo le funzionalità di cui hanno effettivamente bisogno.

Seguendo l'ISP, gli sviluppatori possono evitare di creare interfacce "grasse" che combinano molte responsabilità diverse, rendendo così più difficile la manutenzione e la modifica del codice. Invece, l'ISP promuove la creazione di interfacce "snelle" che hanno una singola responsabilità o un gruppo di responsabilità strettamente correlate.

Questo principio è strettamente legato agli altri principi SOLID, in particolare al  [[Principi SOLID. Single responsibility]] (SRP) e al [[Principi SOLID. Dependency Inversion Principle]] (DIP). L'SRP si concentra sulla divisione delle classi in modo che abbiano una singola responsabilità, mentre l'ISP si concentra sulla divisione delle interfacce. Il DIP, d'altra parte, suggerisce che le classi dovrebbero dipendere da astrazioni piuttosto che da implementazioni concrete, il che è facilitato dall'uso di interfacce specifiche.

## Vantaggi

- **Facilità di manutenzione**: suddividere le interfacce in parti più piccole e specifiche facilita il processo di manutenzione del codice. In questo modo, è possibile apportare modifiche a un'interfaccia senza influenzare altre parti del codice che non utilizzano la parte modificata.
- **Minore accoppiamento**: l'ISP riduce l'accoppiamento tra le classi, poiché ==le classi dipendono solo dalle interfacce che utilizzano effettivamente==. Questo rende il sistema più flessibile e modulare.
- **Maggiore coesione**: L'ISP promuove una maggiore coesione tra le classi e le interfacce, poiché ==ciascuna interfaccia ha una responsabilità ben definita==. Avere interfacce più specifiche contribuisce a mantenere il codice organizzato e comprensibile.
- **Sostituibilità**: Seguendo l'ISP, le classi diventano più intercambiabili, poiché le nuove implementazioni possono essere facilmente sostituite senza interrompere il codice esistente. Questo incoraggia lo sviluppo di componenti riutilizzabili.

## Limiti

1. **Aumento del numero di interfacce**: Come menzionato in precedenza, l'adozione dell'ISP può portare ad un aumento del numero di interfacce nel sistema. Un numero eccessivo di interfacce può aumentare la complessità e rendere il codice più difficile da gestire se non viene mantenuto correttamente.
2. **Sovraprogettazione**: Seguire l'ISP può portare alla sovraprogettazione del sistema. Creare interfacce troppo specifiche e granulari può rendere il codice più difficile da mantenere e capire, soprattutto se i membri dell'interfaccia sono strettamente correlati tra loro ([KISS](https://it.wikipedia.org/wiki/KISS_(sviluppo_software))).
3. **Maggiore curva di apprendimento**: Con un numero maggiore di interfacce, gli sviluppatori potrebbero avere difficoltà a capire la struttura e le relazioni tra le classi e le interfacce. Questo può portare a una maggiore curva di apprendimento per i nuovi membri del team di sviluppo.
4. **Difficoltà nella gestione delle dipendenze**: Sebbene l'ISP riduca l'accoppiamento tra le classi, la gestione di un gran numero di interfacce può complicare la gestione delle dipendenze all'interno del sistema. Gli sviluppatori potrebbero dover prestare maggiore attenzione a come le dipendenze sono organizzate e iniettate tra le classi, il che potrebbe richiedere un investimento maggiore di tempo e sforzo nella progettazione del sistema.
5. **Potenziale ridondanza del codice**: L'adozione dell'ISP potrebbe portare a una potenziale ridondanza del codice in alcuni casi. Quando diverse interfacce hanno funzionalità simili o condividono metodi comuni, gli sviluppatori potrebbero finire per duplicare il codice tra diverse classi che implementano tali interfacce. Questo può rendere il codice meno efficiente e aumentare il rischio di errori e inconsistenze.

## Esempi

### Esempio 1

Immaginiamo di avere un sistema che gestisce diversi tipi di stampanti, alcune delle quali supportano anche la scansione.
Un approccio non conforme all'ISP potrebbe utilizzare un'interfaccia generale come questa:
```csharp
public interface IDevice
{
    void Print();
    void Scan();
}
```
Tuttavia, seguendo l'ISP, divideremmo l'interfaccia in interfacce più specifiche:
```csharp
public interface IPrinter
{
    void Print();
}

public interface IScanner
{
    void Scan();
}
```
Ora, le classi che implementano solo la funzionalità di stampa o scansione possono implementare l'interfaccia appropriata, senza dover implementare metodi non necessari:
```csharp
public class Printer : IPrinter
{
    public void Print()
    {
        // Logica di stampa
    }
}

public class Scanner : IScanner
{
    public void Scan()
    {
        // Logica di scansione
    }
}
public class AllInOnePrinter : IPrinter, IScanner
{
    public void Print()
    {
        // Logica di stampa
    }

    public void Scan()
    {
        // Logica di scansione
    }
}
```

In questo esempio, possiamo vedere come l'ISP renda il codice più pulito e flessibile. Le classi `Printer` e `Scanner` implementano solo le interfacce pertinenti alle loro funzionalità, evitando l'implementazione di metodi inutili.
La classe `AllInOnePrinter`, che supporta sia la stampa che la scansione, implementa entrambe le interfacce.

### Esempio 2

In questo caso, stiamo suddividendo l'interfaccia più grande in parti più piccole e più specifiche per garantire che le nostre classi implementino solo ciò di cui hanno effettivamente bisogno.

```csharp
// Violates ISP
public interface IWorker
{
    void Work();
    void Eat();
}

public class HumanWorker : IWorker
{
    public void Work()
    {
        // Working
    }

    public void Eat()
    {
        // Eating in the break
    }
}

public class RobotWorker : IWorker
{
    public void Work()
    {
        // Working much more efficiently
    }

    public void Eat()
    {
        throw new NotImplementedException("Robots do not eat.");
    }
}

// Adheres to ISP
public interface IWork
{
    void Work();
}

public interface IEat
{
    void Eat();
}

public class HumanWorker : IWork, IEat
{
    public void Work()
    {
        // Working
    }

    public void Eat()
    {
        // Eating in the break
    }
}

public class RobotWorker : IWork
{
    public void Work()
    {
        // Working much more efficiently
    }
}
```