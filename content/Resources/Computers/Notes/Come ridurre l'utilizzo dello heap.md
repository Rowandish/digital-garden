---
tags:
  - Coding
  - CSharp
  - Memory
---


Allocare memoria sullo [[heap]] porta ad un lavoro addizionale per il [[Garbage Collector]] e conseguentemente alla necessità di hardware più performante o a prestazioni inferiori.
E' importante quindi conoscere come programmare riducendo, quando possibile, l'allocazione di variabili sullo heap.
Ci sono diversi costrutti e tecniche che si possono utilizzare:
1.  **Value types**: Utilizzare strutture (struct) invece di classi quando è possibile. Le strutture vengono allocate sullo [[stack]] (o come parte di altre strutture) e non richiedono l'allocazione di memoria sull'heap.
2.  **[[Stackalloc]]**: `stackalloc` può essere utilizzato per allocare array e buffer temporanei sullo stack, evitando l'allocazione sull'heap.
3. **[[Array Pooling]]**: Puoi utilizzare il pooling di array per riutilizzare gli array invece di crearne di nuovi ogni volta che ne hai bisogno. La classe `ArrayPool<T>` fornisce un pool di array condiviso che puoi utilizzare per ridurre l'allocazione di memoria sull'heap.
4.  **[[Object Pooling]]**: In modo simile all'Array Pooling, l'Object Pooling ti permette di riutilizzare gli oggetti invece di crearne di nuovi ogni volta che ne hai bisogno, riducendo così la pressione sul garbage collector. Puoi utilizzare la classe `ObjectPool<T>` o implementare il tuo object pool personalizzato.
5. ** Utilizzare le classi [[Span e ReadOnlySpan]] e la [[classe Memory]] per lavorare con segmenti di array senza dover allocare nuovi array. Queste classi forniscono una vista su un array esistente e possono essere utilizzate per ridurre l'allocazione di memoria sull'heap.
6. **[[Lazy Initialization]]**: Utilizzare l'inizializzazione pigra per creare oggetti solo quando sono effettivamente necessari. Questo può aiutare a ridurre l'allocazione di memoria sull'heap e migliorare le prestazioni, specialmente se alcuni oggetti non vengono mai utilizzati durante l'esecuzione del programma.
7. **Ottimizzazione delle collection**: Scegliere le collection appropriate per il tuo caso d'uso e preallocare la capacità delle collezioni quando è possibile. Ad esempio, se conosci la dimensione massima di una lista, puoi utilizzare il costruttore `List<T>(int capacity)` per preallocare la capacità e ridurre le allocazioni di memoria sull'heap.
8. **StringBuilder**: Utilizzare la classe `StringBuilder` invece della concatenazione di stringhe per ridurre le allocazioni di memoria sull'heap quando si lavora con stringhe.
9. **Evitare closure**: Evitare di utilizzare closure (funzioni anonime che catturano variabili esterne) quando non sono necessarie, poiché possono causare l'allocazione di memoria sull'heap.
10. **Delegates**: Utilizzare metodi statici invece di metodi di istanza per i delegate quando è possibile, in quanto i delegate che fanno riferimento ai metodi di istanza richiedono l'allocazione di memoria sull'heap.