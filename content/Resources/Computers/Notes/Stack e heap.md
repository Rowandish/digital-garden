---
tags:
  - Coding
  - Memory
---


Per ogni applicazione eseguita sul sistema operativo, quest'ultimo assegna una quantità di RAM nella quale si trovano due zone distinte: gli stack e lo heap.

In particolare il SO assegna **uno stack ad ogni thread dell'applicazione** (viene quindi assegnato alla creazione del thread e eliminato al suo termine), mentre **lo heap è unico** (viene creato al lancio dell'applicazione e eliminato alla sua chiusura).

La dimensione dello heap viene decisa al lancio dell'applicazione ma può aumentare in base allo spazio necessario.

Dato che vi è un unico heap per tutti i thread dell'applicazione, questo deve essere thread-safe: ogni allocazione e deallocazione nello heap deve essere sincronizzata.

**Dato un metodo da eseguire, nello stack verranno inseriti le variabili "passate per valore" che verranno eliminate al termine del metodo stesso, mentre nello heap le variabili "passate per riferimento" che invece rimarranno nella memoria anche al termine del metodo.**

**Queste ultime dovranno essere eliminate da un agente interno (Dispose manuale) o esterno ([[Garbage Collector]])**.

**Lo stack è notevolmente più veloce di un heap** in quanto il modello di accesso rende banale l'allocazione e la deallocazione della memoria da esso (un puntatore viene semplicemente incrementato o decrementato, vi è una operazione di push e pop che occupa un'istruzione macchina), mentre l'heap deve avere una gestione molto più complessa per l'allocazione o deallocazione che coinvolge il sistema operativo.

Per approfondire stack, heap e altri concetti fondamentali consiglio questo bellissimo articolo: [https://www.codeproject.com/Articles/76153/Six-important-NET-concepts-Stack-heap-value-types](https://www.codeproject.com/Articles/76153/Six-important-NET-concepts-Stack-heap-value-types)

## [[Stack]]
## [[Heap]]