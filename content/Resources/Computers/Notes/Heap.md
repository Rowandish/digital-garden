---
tags:
  - Coding
  - Memory
---


Lo heap è una **struttura dati in RAM non sequenziale ad accesso casuale**. Le variabili vengono istanziate in questa area e vi è possibile accedervi tramite un puntatore.

A differenza dello [[stack]], ==non esiste alcun modello forzato per l'allocazione e la deallocazione dei blocchi dall'heap: è possibile allocare un blocco in qualsiasi momento e liberarlo in qualsiasi momento==. Ciò rende molto più complesso tenere traccia di quali parti dell'heap sono allocate o libere in un dato momento.

## Caratteristiche

1. **Allocazione dinamica**: Lo heap permette di allocare e deallocare memoria in modo dinamico durante l'esecuzione del programma. A differenza dello stack, che ha una dimensione fissa e gestisce automaticamente la memoria per le variabili locali e i parametri delle funzioni, lo heap consente di allocare memoria in base alle esigenze del programma.
2. **Durata degli oggetti**: Gli oggetti allocati nello heap hanno una ==durata che va oltre la durata delle funzioni che li creano==. La memoria allocata nello heap rimane ==disponibile fino a quando non viene esplicitamente deallocata== o fino a quando il programma termina. **La deallocazione delle variabili nell'heap deve essere quindi gestita esplicitamente**: in alcuni linguaggi deve essere effettuata manualmente chiamando dei comandi appositi come `free, delete, or delete[[]`. In altri linguaggi esiste il _Garbage Collector_ che automaticamente elimina gli oggetti inutilizzati nello heap senza che il programmatore debba fare nulla. Per il Dispose in C# vedi [[Eliminazione di oggetti in .NET]]
3. **Accesso tramite puntatori o riferimenti**: Gli oggetti nello heap sono generalmente ==accessibili tramite puntatori o riferimenti==. Questo consente di condividere e modificare i dati tra diverse funzioni e moduli del programma senza dover passare copie degli oggetti stessi. Tuttavia, l'uso di puntatori e riferimenti può anche rendere il codice più complesso e aumentare il rischio di errori, come dereferenziazione di puntatori nulli o accesso a memoria non inizializzata.    
4. **Dimensioni variabili**: ==Lo heap può espandersi e contrarsi dinamicamente in base alle esigenze di memoria del programma==. Questo permette di gestire strutture dati di dimensioni variabili e di adattarsi alle esigenze di memoria che cambiano nel tempo. Tuttavia, l'espansione e la contrazione dello heap possono portare a frammentazione e ridurre l'efficienza nella gestione della memoria. Non avrò quindi mai problemi di overflow, al massimo rallentamenti dovuti allo [swapping](https://it.wikipedia.org/wiki/Swap_(informatica)).
5. **Condivisione tra thread**: In ambienti multithreading, ==lo heap è condiviso tra tutti i thread del processo==. Questo permette ai thread di condividere e scambiare dati facilmente, ma richiede anche l'uso di meccanismi di sincronizzazione per prevenire problemi di concorrenza, come condizioni di gara e incoerenza dei dati.

## Vantaggi

1. **Durata della memoria**: Le variabili allocate nello heap persistono per tutta la durata del programma, a meno che non vengano liberate esplicitamente. Ciò permette di utilizzare variabili con una durata più lunga rispetto a quelle dello stack, che vengono automaticamente eliminate al termine della funzione.
2. **Dimensioni**: Lo heap ha spesso una dimensione molto maggiore rispetto allo stack, consentendo l'allocazione di strutture dati di grandi dimensioni che potrebbero non essere gestibili nello stack.
3. **Flessibilità**: L'allocazione dinamica della memoria nello heap permette di creare e ridimensionare strutture dati come array e oggetti in modo più flessibile, a differenza dello stack, che richiede che le dimensioni delle variabili siano conosciute al momento della compilazione.
4. **Condivisione dei dati**: Poiché le variabili nello heap sono accessibili da qualsiasi parte del programma, possono essere facilmente condivise tra diverse funzioni e thread.
5. **Allocazione esplicita**: L'allocazione e la liberazione della memoria nello heap avvengono in modo esplicito, il che consente al programmatore di avere un maggiore controllo sulla gestione della memoria.

## Limiti

1. 1. **Overhead di gestione della memoria**: L'allocazione e la deallocazione della memoria nello heap richiedono tempo e risorse aggiuntive, poiché il sistema deve gestire la complessità delle operazioni, come la ricerca di blocchi di memoria liberi, la loro combinazione e la loro divisione. Questo overhead può influire negativamente sulle prestazioni del programma, specialmente se si effettuano frequenti operazioni di allocazione e deallocazione.
2. **Frammentazione della memoria**: Questo problema avviene quando l**a memoria disponibile nello heap è gestita tramite blocchi discontinui, in particolari blocchi utilizzati sono inframezzati da blocchi inutilizzati**. Quando vi è eccessiva frammentazione può risultare impossibile allocare nuova memoria in quanto, anche se potenzialmente avrei memoria utilizzabile, questa non è contigua.
3. **Problemi di sincronizzazione**: Nei programmi multithread, l'accesso e la manipolazione condivisa dello heap possono causare problemi di sincronizzazione e condizioni di gara. Per evitare questi problemi, è necessario utilizzare meccanismi di sincronizzazione, come semafori o mutex, che possono aggiungere ulteriore complessità e sovraccarico al programma.
4. **Gestione manuale della memoria**: In alcuni linguaggi di programmazione, come C e C++, è necessario gestire manualmente l'allocazione e la deallocazione della memoria nello heap. Questo può portare a errori umani, come dimenticare di liberare la memoria allocata, causando perdite di memoria (memory leak), oppure liberare la memoria più volte, portando a comportamenti indefiniti e potenzialmente crash del programma. Anche in linguaggi come il C# dove è presente il [[Garbage Collector]] comunque è necessario porre attenzione alla memoria allocata, sopratutto di quella degli oggetti `IDisposable`.
5. **Tempo di accesso**: L'accesso alla memoria nello heap è generalmente più lento rispetto all'accesso alla memoria nello stack, poiché l'indirizzo di memoria degli oggetti allocati nello heap può essere meno prevedibile. Inoltre, le operazioni di allocazione e deallocazione nello heap sono più complesse e richiedono più tempo rispetto alle operazioni nello stack. Questo può influire sulle prestazioni del programma, in particolare se si effettuano molte operazioni su dati allocati nello heap.

## Tipologie in .NET
In .NET ho due aree separate virtuali dello heap che vengono utilizzate per gestire in modo più efficiente l'allocazione e la raccolta dei diversi tipi di oggetti sulla base delle loro dimensioni.
Queste vengono utilizzare all'implementazione del [[Garbage Collector]] di .NET e sono quindi presenti solo in tale ambiente.

### Small Object Heap

Lo Small Object Heap è progettato per contenere oggetti di dimensioni ridotte. Nell'ambito del garbage collector di .NET, gli oggetti di dimensioni inferiori a 85.000 byte vengono allocati nello SOH. Il SOH è organizzato in generazioni (0, 1 e 2) per ottimizzare la raccolta dei rifiuti e ridurre l'overhead della scansione degli oggetti.
Questi vengono compattati durante la _Compacting Phase_ del `Collect`.

### Large Object Heap

Il Large Object Heap è destinato a contenere oggetti di dimensioni maggiori, tipicamente oggetti di dimensioni superiori a 85.000 byte. A differenza dello SOH, il LOH non è organizzato in generazioni. Il motivo di questa separazione è che gli oggetti di grandi dimensioni tendono ad avere un costo di allocazione e deallocazione più elevato e possono causare una maggiore frammentazione dello heap. Raggruppando gli oggetti di grandi dimensioni nel LOH, il garbage collector può gestire in modo più efficiente l'allocazione e la raccolta di questi oggetti.
Il LOH viene raccolto meno frequentemente rispetto allo SOH, in quanto si presume che gli oggetti di grandi dimensioni abbiano una durata più lunga. Tuttavia, quando il LOH viene raccolto, il processo è più dispendioso in termini di tempo e risorse, poiché coinvolge la scansione e la raccolta di oggetti di grandi dimensioni.


## Esempio
```csharp
void barFunction( )
{
  // Viene creato un puntatore nello stack ("f") che punta ad un nuovo oggetto che verrà creato nello heap
  Foo\* f = new Foo( ) ;

  // Sono al termine del metodo ma, dato che "m" è nello heap, nessuno lo elminerà. Qualora stia utilizzando linguaggi senza GC come C++ devo eliminare l'oggetto manualmente con il domando "delete", altrimenti incorrerò in un memory leak. Qualora invece utilizzi linguaggi con il GC come C# o Java il Dispose verrà effettuato automaticamente, a meno di oggetti IDisposable che rendono necessario il dispose manuale allo stesso modo.

  // Se non c'è il GC
  delete m; 
  // Se c'è il GC ma oggetto IDisposable
  m.Dispose()
} 
```

## Esempio complessivo
Di seguito un esempio che racchiude tutti i concetti descritti sopra, in C.
```csharp
int foo()
{
  char *fooPointerArray; // Non viene allocato nulla a meno del puntatore che viene allocato nello stack
  bool boolean = true; // La variabile b viene allocata nello stack.
  if(boolean)
  {
    // Alloca 100 byte nello stack 
    char fooArray[100];

    // Alloca 100 byte nello heap
    fooPointerArray = new char[100];

   }//<-- la variabile fooArray è deallocata qui, al contrario di fooPointerArray
}//<--- Senza un delete[] fooPointerArray ho un memory leak