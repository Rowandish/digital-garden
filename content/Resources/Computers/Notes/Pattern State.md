---
tags:
  - Coding
  - BehaviouralDesignPattern
  - PublishedPosts
---


## Introduzione

Il pattern state consente ad un oggetto di cambiare il proprio comportamento a run-time in funzione dello stato in cui si trova. Esso è un pattern comportamentale.

Questo pattern viene usato tipicamente quando voglio implementare [una macchina a stati finiti](https://it.wikipedia.org/wiki/Automa_a_stati_finiti).

In ogni momento il programma può quindi **essere in uno e un solo stato** ed è necessario definire le condizioni per passare da uno stato all'altro.

Consiglio quindi, prima di procedere con l'implementazione, scrivere il diagramma a stati finiti che si vuole implementare.

Prendiamo l'esempio di un apparecchio telefonico: esso è perennemente nello stato di _attesa_ fino a che non riceve una chiamata. Quando la riceve cambia di stato e va nello stato _chiamata_ dove il telefono squilla. Da questo stato l'utente può _rifiutare_ e quindi ritornare nello stato di _Attesa_ oppure accettare: ho quindi due transizioni diverse.

Se rifiuta si ritorna allo stato di _Attesa_ come sopra, se invece accetta si passa allo stato _Conversazione_. Una volta terminata la conversazione si conclude la telefonata tornando in _Attesa._

Questo schema è indicato nell'immagine qui sotto

![[Grafo_chiamata.png]]

## Implementazione C#

Il pattern state si basa su una classe `Context` che è l'oggetto che vuole cambiare stato (nell'esempio sopra il telefono) e vari `State` che sono gli stati in cui il `Context` può essere.

![[State_design_pattern.webp]]

L'esempio seguente è in C# ma il concetto è lo stesso per tutti i linguaggi orientati agli oggetti come Java.

### State

Tutti gli stati erediteranno dalla stessa classe astratta (o interfaccia) `State` la quale avrà almeno un metodo `Handle`, il quale sarà il metodo per il cambio di stato, che dipenderà da `Context`.
```CSharp
/// <summary>
///     Classe che identifica lo stato della classe <see cref="Context" />. Il metodo fondamentale è il metodo
///     <see cref="Handle" /> che *deve* avere in ingresso il <see cref="Context" /> e permette di modificarne il suo
///     <see cref="Context.State" /> in base a determinate condizioni.
///     Il trucco sta proprio nell'avere all'interno dello stato <see cref="State" /> una istanza del contesto
///     <see cref="Context" /> e che questo abbia una property public per poterne modificare lo stato.
/// </summary>
public abstract class State
{
    public abstract void Handle(Context context);
}
```

### State concreti

Ho quindi vari `State` concreti, in base all'applicazione, che sono tutti gli stati dove può essere il `Context`.
```CSharp
/// <summary>
///     Generico stato A del <see cref="Context" />
/// </summary>
public class ConcreteStateA : State
{
    /// <summary>
    ///     Una volta fatte tutte le operazioni dello stato A, questo viene modificato a B se vi sono determinate condizioni.
    ///     In questo caso viene solo modificato in <see cref="ConcreteStateB" />
    /// </summary>
    public override void Handle(Context context)
    {
        context.State = new ConcreteStateB();
    }
}

/// <summary>
///     Generico stato B del <see cref="Context" />
/// </summary>
public class ConcreteStateB : State
{
    /// <summary>
    ///     Una volta fatte tutte le operazioni dello stato B, questo viene modificato a A se vi sono determinate condizioni.
    ///     In questo caso viene solo modificato in <see cref="ConcreteStateA" />
    /// </summary>
    public override void Handle(Context context)
    {
        context.State = new ConcreteStateA();
    }
}
```

## Context

Il `Context` è l'oggetto di cui voglio modificare il comportamento. Notare la property `State` che permette di modificare il suo stato. Questa property dovrà essere settata nei metodi `Handle` dei `ConcreteState`.
```CSharp
/// <summary>
///     Oggetto che ha uno stato <see cref="State" /> che viene modificato nel tempo
/// </summary>
public class Context
{
    /// <summary>
    ///     Stato della classe
    /// </summary>
    private State _state;

    /// <summary>
    ///     Costruttore: serve per inizializzare lo stato <see cref="State" />
    /// </summary>
    public Context(State state)
    {
        State = state;
    }

    /// <summary>
    ///     Metodo fondamentale, in quanto permette agli stati <see cref="State" /> di modificare lo stato del Context
    /// </summary>
    public State State
    {
        set
        {
            _state = value;
            Console.WriteLine($"State: {_state.GetType().Name}");
        }
    }

    /// <summary>
    ///     Generico metodo verso il mondo esterno. Il comportamento di questo metodo cambia in base allo stato
    ///     <see cref="_state" />
    /// </summary>
    public void Request()
    {
        _state.Handle(this);
    }
}
```

## Quando usarlo

Il pattern State permette di sostituire istruzioni condizionali complesse con delle classi le quali contengono, al loro interno, tutte le loro logiche e le transizioni. In questo modo la classe Context, che, senza State, risulterebbe pachidermica, risulta invece piccola e semplice. Rispetto quindi il [[Open-closed principle](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle) e i [principi di buona programmazione]].

## Dove approfondire

Per approfondire consiglio assolutamente la lettura di [Head First Design Pattern](https://amzn.to/3EMwLsV), un libro imprendiscindibile per chiunque voglia migliorarsi come programmatore.