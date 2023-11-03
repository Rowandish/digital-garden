---
tags:
  - Coding
  - Database
---


## Introduzione

Ogni applicazione che utilizza un database deve pensare a come gestire un aumento delle richieste e dell'utilizzo di questa ultima senza comprometterne l'usabilità.

Rendere scalabile l'applicazione non deve compromettere la sicurezza e l'integrità dei dati.

Un ulteriore requisito importante è sviluppare l'architettura di un database in un modo che sia scalabile dinamicamente in base alle richieste.

Per riuscire ad ottenere tutto questo esistono gli _shared database_, che è il partizionamento orizzontale di questi ultimi.

In questo articolo vedremo quando e come effettuare lo _sharding_ e soprattutto in che casi questo può essere necessario.

## Cosa è lo sharding?

Lo sharding è il partizionamento orizzontale di un database che consiste nel separare le righe di una tabella in righe di molte tabelle differenti, chiamate partizioni.

Ogni partizione ha lo stesso schema della tabella originale, ma con righe differenti; ogni sotto-tabella quindi ha dati differenti.

Nel _partizionamento verticale_ invece sono le colonne ad essere separate, quindi ogni partizione ha sia differenti righe che colonne.

### Physical shards e logical shards

Lo _sharding_ prevede quindi di dividere i dati presenti in una tabella in due o più _chunks_ chiamati _logical shard_. Questi ultimi sono distribuiti in nodi fisici differenti, chiamati _physical shards_,

Ogni _physical shard_ può contenere più _logical shard_.

Lo sharding di un database rispecchia la _[shared-nothing architecture](https://en.wikipedia.org/wiki/Shared-nothing_architecture)_, nel senso che ogni shard è autonomo, non ha bisogno potenzialmente di un nodo centrale per funzionare in quanto possiede già tutte le colonne; l'unica differenza è solo nel sottoinsieme delle righe.

Qualora risulti necessario alcune tabelle di gestione dell'applicazione possono risiedere in ogni _physical shards_.

### Implementazione

Spesso lo sharding è implementato a livello applicativo, per cui è direttamente l'applicazione che decide a quale shard inviare e ricevere dati.

Esistono anche alcuni DBMS che hanno delle funzionalità di sharding integrate per cui è possibile implementarlo direttamente a livello database nascondendo la logica al livello applicativo.

## Benefici dello sharding

### Scaling up e out

Il miglior beneficio dello sharding è che può facilitare l'_horizontal scaling_, chiamato anche _scaling out_.

L'_horizontal scaling_ è la pratica di aggiungere più macchine (nodi della rete) in modo da suddividere il carico e poter quindi supportare maggior traffico con una velocità maggiore.

Questo è in contrasto con il _vertical scaling_ (_scaling up_) per cui non si aumentano i nodi ma si migliora l'hardware dei nodi esistenti aggiungendo RAM o CPU.

Lo scaling up è molto più semplice da implementare: basta aggiornare la CPU o la RAM del server e sono a posto. Questa però non è aumentabile all'infinito per cui ad un certo momento non è più sufficiente ed è necessario implementare qualche tecnica di _scaling out_.

### Velocità delle query

Quando ho un database monolitico con milioni di righe, le query possono risultare incredibilmente lente in quanto devono sempre far passare tutti i record presenti.

Dividendo il database in più parti, le query devono controllare meno righe per volta risultando quindi più veloci.

### Sicurezza

Un ulteriore vantaggio dello sharding è dal punto di vista della sicurezza: avere tutto il database su un unico nodo porta ad avere un single-point-of-failure: caduto quello l'intero sistema si ferma.

La divisione in nodi permette di avere un sistema che comunque regge (anche se con meno dati) in caso di fallimento di un nodo: l'applicazione potrà quindi non essere disponibile solo per alcuni utenti ma non per tutti.

## Svantaggi dello sharding

### Implementazione

Il primo problema dello sharding è la maggiore difficoltà nell'implementazione: è molto più semplice avere dati corrotti o persi in caso di errori in questa ultima.

A livello applicativo si aggiunge inoltre la complessità di dover reperire dati da più punti distinti, quindi in ogni momento è necessario sapere a che shard chiedere il determinato dato.

### Bilanciamento degli shard

Un ulteriore problema è il bilanciamento degli shard: la logica con cui un dato viene messo nello shard A invece che B è estremamente importante in quanto devo evitare di avere uno sbilanciamento nella dimensione degli shard per cui molti più dati vengono inviati allo shard A invece che B.

Un database con molti dati può portare a tutti i problemi tipici della mancanza di sharding indicati sopra e viene detto _database hotspot_.

### Difficoltà nel ritorno ad una architettura monolitica

Una volta che un database è stato diviso può essere molto difficile tornare ad una architettura monolitica.

Inoltre c'è da capire come gestire i backup della versione shared.

E' sicuramente una operazione fattibile ma molto difficile e costosa in termini di tempo.

### Non tutti i database lo supportano nativamente

Non tutti i DBMS supportano nativamente lo sharding ma è necessario implementare tutta la logica a mano.

Per esempio PostgreSQL non supporta lo sharding, che viene supportato solo da alcuni fork che però non sono ufficiali e magari non sono aggiornati all'ultimissima versione.

Tipicamente è necessario procedere per versioni di DBMS pensate per lo sharding come, per esempio, [MySQL Cluster](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiQ4efkpcj2AhXPqqQKHV29AnUQFnoECA8QAQ&url=https%3A%2F%2Fwww.mysql.com%2Fit%2Fproducts%2Fcluster%2F&usg=AOvVaw2xQSxAVBJR6GECnvwLMZnb) o [MongoDB Atlas](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwju6vLppcj2AhXO-qQKHZjoBegQFnoECAkQAQ&url=https%3A%2F%2Fwww.mongodb.com%2Fatlas%2Fdatabase&usg=AOvVaw21MqaFtLofvOZafnXigoYD), mentre le versioni standard non lo supportano.

## Architetture per lo sharding

Una volta deciso di effettuare lo sharding è necessario scegliere l'architettura migliore per la propria applicazione.

### Key Based Sharding

Nel _Key based sharding_ (chiamato anche _hash based sharding_) è necessario scegliere una colonna della tabella da partizionare (tipicamente che contiene dati che non cambiano nel tempo) e calcolare l'hash di ognuno di questi dati.

L'hash sarà sempre diverso ma potrei aggiungere la seguente logica: se ho tre shard lo shard da utilizzare sarà quello indicante dal risultato dell'hash modulo 3.

In questo modo posso avere solo tre valori in uscita, 0, 1 e 2: questo valore sarà la mia _shard key_ e indicherà che shard utilizzare.

Il vantaggio principale di questa tecnica è che evita i _database hotspost_ in quanto ogni riga ha la stessa probabilità di essere inserita in uno dei miei _n_ shard.

Un altro vantaggio è che la localizzazione del dato negli shard è definito algoritmicamente, per cui è sempre possibile sapere ogni riga in che nodo si trova.

Lo svantaggio è che, qualora volessi aggiungere un nodo, rischio di dover ricalcolare tutti i valori di hash in quanto, seguendo l'esempio sopra, ora ho un modulo 4 e non un modulo 3.

Durante la migrazione ne la vecchia ne la nuova funzione di hash funzionerà correttamente e questo può portare a dei periodi di down.

### Range based sharding

Con questa modalità viene scelto il nodo in base al fatto che il valore di una determinata colonna appartenga o meno ad un determinato range.

Per esempio se ho la colonna "Età" posso mettere le persone con meno di 30 anni nello shard A, le persone tra 30 e 60 nello shard B e le altre nello shard C.

Il vantaggio principale è che estremamente semplice da implementare; il problema è che c'è il rischio che i dati non siano distribuiti equamente tra i vari shard.

### Directory Based Sharding

In questo caso è necessario creare una _lookup table_ che mappa una _shard key_ allo shard che contiene i dati.

Di fatto questa è una tabella statica che indica dove uno specifico dato può essere trovato.

Il vantaggio principale di questo approccio è la flessibilità: nel _range based sharding_ è necessario definire a priori i range, nel _key based sharding_ la funzione di hash e la modifica di questi parametri può essere complessa.

Nel _directory based sharding_ invece aggiungere o togliere shard è molto semplice, alla fine basta modifica in che modo i dati vengono inseriti nella lookup table.

Il problema è che prima di effettuare ogni query è necessario chiedere in che shard farla tramite la lookup table e questo può peggiorare le performance del sistema.

## Quando fare sharding?

Se e quando fare sharding è complesso: aggiunge un livello di complessità non da poco alla gestione dei dati e può portare a parecchi mal di testa.

E' importante non aggiungere complicazioni a applicazioni che non ne hanno alcun bisogno, come dicono i programmatori seguire sempre il metodo [KISS](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj4rNf5r8j2AhVDMewKHYoxAHYQFnoECAgQAQ&url=https%3A%2F%2Fit.wikipedia.org%2Fwiki%2FKISS_(principio)&usg=AOvVaw2PWFzfR7NN7FOZDgyxSTOJ).

E' necessario procedere con lo sharding quando si ha a che fare che enormi quantità di dati o in generale quando:

- L'ammontare dei dati dell'applicazione supera la capacità di memoria di un singolo nodo
- Il numero di letture e scritture di un database super quelle che può gestire un singolo nodo
- La banda richiesta supera la banda massima supportata da un nodo

In ogni caso prima di procedere con lo sharding è necessario effettuare tutte le possibili ottimizzazioni come:

- Lavorare con un database remoto che non risiede nello stesso server dell'applicazione;
- Implementare il caching dei dati che sono stati richiesti da poco tempo;
- Implementare una o più repliche in sola lettura (le scritture vanno sempre sul server principale mentre le letture vengono effettuare dalle repliche). In questo modo posso suddividere il carico dalla stessa macchina senza effettuare sharding o partizionamenti;
- Migliorare l'hardware del server

## Conclusione

Lo sharding è una ottima soluzione per scalare un database orizzontalmente in modo flessibile ma porta ad un aumento di complessità non indifferente.

I vantaggi che posso avere possono essere superati dal maggiore tempo richiesto nella gestione dell'architettura distribuita.

Prima di procedere è quindi importante avere ben chiara la propria situazione in modo da fare scelte oculate e non affrettate.
