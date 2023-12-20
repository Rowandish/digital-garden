---
tags:
  - Coding
  - CSharp
  - Memory
  - PublishedPosts
---


.NET semplifica di molto la vita dei programmatori in quanto **evita l'obbligo di liberare la memoria dagli oggetti non più utilizzati tramite l'utilizzo di un Garbage Collector**.

Il **Garbage Collector è un componente fondamentale della CLR (Common Language Runtime)** e viene fornito in automatico a tutte le applicazioni .NET.

Non è scontato avere un meccanismo automatico di gestione della memoria, per esempio nei linguaggi come C o C++ è invece indispensabile liberare la memoria a mano, per esempio con il comando `free` di C o `delete` di C++.

**Un oggetto "garbage" (spazzatura) è un oggetto che non è più utilizzato, quindi che non può essere più raggiunto da nessuno in quanto non ho alcun riferimento (puntatore) ad esso**. L'oggetto è presente ancora in memoria ma, di fatto, non serve a nulla. Si dice che l'oggetto è _out of scope_.

Il GC lavora solo sugli oggetti presenti nel _**managed [[Heap]]**_, gli oggetti unmanaged devono essere gestiti manualmente tramite l'interfaccia `IDisposable`.

Il garbage collector funziona creando una struttura ad albero che, a partire da oggetti _root_ raggiunge tutte le variabili. Gli oggetti che non sono più raggiungibili dalla _root_ vengono marcati come "da eliminare".

**Il garbage collector può eliminare solo gli oggetti che non hanno riferimenti (_no references_) oppure che hanno solo riferimenti deboli (_[weak references](https://docs.microsoft.com/it-it/dotnet/api/system.weakreference?view=net-6.0)_).**

## Generations

^cef812

Gli oggetti che vengono gestiti dal GC si dividono in 3 categorie, chiamate **_generations_**, in particolare gen 0,1,2.

**La frequenza di collect è inversamente proporzionale all'aumento del numero di gen**, quindi gli oggetti gen 0 verranno eliminati più frequentemente degli oggetti gen 1 e questi ultimi più frequentemente degli oggetti gen 2.

La gen 0 viene effettuata molto frequentemente e gli oggetti che la compongono sono tipicamente molto facili da eliminare in quanto hanno poche reference con il resto del codice essendo appena stati creati. **Maggiore è la gen maggiore è il tempo impiegato per lo scan e l'eliminazione, per questo avviene più di rado**.

Quando viene lanciato il software la CLR imposta una dimensione massima, in kb, per gli oggetti presenti nella generation 0 e 1. Se la creazione di un nuovo oggetto va a eccedere la dimensione impostata per la generazione in questione, viene lanciato un collect sugli oggetti appartenenti a questa gen.

Gli oggetti spazzatura vengono rimossi e gli oggetti sopravvissuti passano alla gen successiva.

La dimensione massima delle gen 0 e 1 non è fissa ma può essere modificata in real time dal GC in base alle sue esigenze: per esempio se dopo un collect della gen0 vedo che ci sono pochi oggetti posso ridurne la dimensione, al contrario se rimangono molti oggetti posso aumentarla.

### Generations 0

Contiene tutti i nuovi oggetti creati in memoria che non sono mai stati esaminati dal GC.

### Generations 1

Contiene tutti gli oggetti che sono sopravvissuti al collect della gen0. Quando viene superata la dimensione massima per questi oggetti viene lanciato un Collect del GC sulla gen 0 e sulla gen1. Alcuni oggetti passeranno quindi alla gen1 e altri alla gen2.

### Generations 2

Contiene tutti gli oggetti sopravvissuti sia alla gen0 che alla gen1. Tipicamente sono gli oggetti più "vecchi" che hanno meno probabilità di diventare spazzatura.

## Quando parte il GC?

Il GC utilizza al suo interno varie euristiche per capire quando e come agire, è infatti impossibile prevedere in modo certo quando viene lanciato.

Vi sono però tre condizioni particolari dove si ha la certezza di un Collect:

- Il sistema sta esaurendo la memoria
- E' finito lo spazio impostato per la gen0 o per la gen1
- E chiamato un metodo `GC.Collect()` dal programmatore.

## Fasi della collection

Tipicamente la garbage collection avviene in 3 fasi distinte. la marking phase (compresa una collect phase), la relocating phase e la compacting phase.

### Marking phase

Viene creata una lista di tutti gli oggetti ancora vivi, seguendo l'albero a partire degli oggetti root.

Di seguito una spiegazione molto semplificata del funzionamento.

A partire dalle root il GC viaggia in tutto il grafico degli oggetti seguendo le dipendenze; quando visita un nodo già marcato lo skippa in modo da evitare dipendenze cicliche.

In particolare ogni nodo del grafo può avere tre stati:

- Non ancora visitato;
- Nodo da visitare prima o poi
- Nodo già visitato, quindi raggiungibile

Quando tutti i nodi del grafo sono stati analizzati e non ci sono più nodi da visitare; tutti i nodi che sono rimasti nello stato "non visitato" sono i nodi da eliminare.

#### Collect phase

Tutti gli oggetti che non si trovano nella lista degli oggetti ancora vivi vengono eliminati.

### Relocating Phase

Tutti i puntatori degli oggetti ancora vivi vengono modificati in modo da puntare alla loro nuova posizione in memoria dopo la compacting phase.

### Compacting phase

Il GC effettua uno scan del managed heap, sposta la memoria libera al top mentre gli oggetti al bottom. In questo modo i buchi di memoria degli oggetti rimossi vengono eliminati.

E' l'analogo del processo di deframmentazione degli hard disk ma nel managed heap.

Gli oggetti presenti nel **Large Object Heap (LOH)** non vengono compattati in quanto la loro copia in memoria può essere estremamente onerosa e portare a problemi di performance.

## Tipologie di Heap

### Small Object Heap

Gli oggetti appartenenti al SOH sono tutti gli oggetti di piccole dimensioni (la maggior parte di un software) e vengono compattati durante la _Compacting Phase_ del `Collect`.

### Large Object Heap

Il Large Object Heap (LOH) è una speciale parte della memoria dedicata agli oggetti di grandi dimensioni (> 85KB). Questi oggetti sono onerosi per il GC per cui vengono eliminati solo durante una collect full (quindi gen 0,1,2).

Questi oggetti non vengono compattati durante la _Compacting Phase_ del `Collect` è quindi necessario porre particolare attenzione: si possono creare facilmente dei buchi di memoria e conseguente frammentazione.

Questi oggetti sono quindi pesanti da eliminare per il GC e portano alla frammentazione della memoria con conseguente aumento della sua dimensione.

## System.GC

**_System.GC_** è la classe che rappresenta il Garbage Collector e che posso utilizzare per forzarlo a effettuare delle logiche custom per la mia applicazione.

### GC.Collect()

Questo metodo permette di **forzare un `Collect` di tutte le generazioni, oppure forzare solo una determinata generazione passando il numero in ingresso**.

Quasi mai è necessario chiamare forzatamente il `Collect` del GC, tipicamente le sue euristiche sono migliori di quelle del programmatore. Ricordo inoltre che questo metodo è **estremamente _time-consuming_ e _resource-intensive_**.

Può comunque avere un senso in alcuni casi particolari, come dei metodi che allocano molta memoria ma che, una volta eseguiti, non servono a nulla; in quel caso potrei chiamare un `Collect` per rimuovere subito gli oggetti dalla memoria.

Può essere utile anche per il debugging: chiamando un `Collect` sono sicuro che tutti gli oggetti che devono essere eliminati lo sono stati e, se un oggetto rimane in memoria, significa che ho un leak.

Un altro utilizzo di questo metodo è, in fase di test o benchmarking, di essere sicuro che tutti i test partano da uno stato noto standard.

Questo metodo non deve essere usato per effettuare il `Dispose()` di risorse unmanaged (se sono unmanaged il GC non può fare nulla per definizione); in quel caso è necessario utilizzare il pattern [[Dispose]].

### GC.GetTotalMemory()

Fornisce il numero di byte presenti nella memoria managed.

### GC.KeepAlive (object obj)

Impedisce ad GC di effettuare il `Collect` del metodo anche se non ho alcun riferimento. Questo metodo viene usato quando il metodo finalizer ha dei comportamenti distruttivi sull'oggetto stesso o su altri oggetti in esso contenuto e voglio avere un controllo sul quando e come questo metodo deve essere chiamato.

Utilizzare l'interfaccia [[IDisposable]] è un modo molto più pulito per evitare l'utilizzo di `GC.KeepAlive`

### GC.SuppressFinalize (object obj)

Permette di comunicare al GC che non deve chiamare il metodo `Finalize()`di questo oggetto, in quanto le sue risorse sono già state eliminate in precedenza (tipicamente dal metodo Dispose).

### GC.GetGeneration (object obj)

Fornisce la generazione di appartenenza dell'oggetto passato in ingresso.

### GC.WaitForPendingFinalizers()

Blocca il thread corrente fino a che tutti i finalizers non sono stati completati. Il collect del GC avviene in parallelo senza essere bloccante; qualora abbia la necessità (per esempio negli unit test) di partire da una situazione di memoria pulita in modo sincrono è necessario chiamare questo metodo dopo il `Collect`.
