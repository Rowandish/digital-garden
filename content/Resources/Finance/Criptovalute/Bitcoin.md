---
tags:
  - Crypto
  - Coin
  - PublishedPosts
---


Bitcoin è stata la prima criptovaluta inventata nel 2009 da Satoshi Nakamoto. A differenza delle normali valute Bitcoin non ha un ente centrale che lo stampa o ne definisce il valore, questo è invece determinato unicamente dalla leva domanda e offerta.

Esso di basa su una tipologia di [[Distributed Ledger]], chiamato [[Blockchain]], per tenere traccia delle transazioni. Utilizza inoltre la crittografia per l'attribuzione della proprietà di un bitcoin e la generazione di nuova moneta.

La struttura peer-to-peer della rete Bitcoin e la mancanza di un ente centrale rende impossibile a qualunque autorità, governativa o meno, il blocco dei trasferimenti, il sequestro di bitcoin senza il possesso delle relative chiavi o la svalutazione dovuta all'immissione di nuova moneta.

## Proprietà dei btc, i wallet

La proprietà dei bitcoin è determinata dal possesso di una coppia chiave pubblica e chiave privata chiamato [[Wallet crypto]].

Le chiavi pubbliche fungono da punti d'invio o ricezione per tutti i pagamenti. La corrispondente chiave privata serve ad apporre una firma digitale a ogni transazione facendo in modo che sia autorizzato al pagamento solo l'utente proprietario di quella moneta. La rete verifica la [firma utilizzando la chiave pubblica](https://it.wikipedia.org/wiki/Firma_digitale).

Bitcoin è una tecnologia anonima, quindi gli indirizzi non contengono alcuna informazione riguardo ai loro proprietari. E' possibile inoltre generarli in modo molto semplice e in numero arbitrario. Questi indirizzi sono delle stringhe alfanumeriche lunghe in media 33 caratteri che iniziano sempre per 1, 3 o bc1.

Se la chiave privata viene smarrita, la rete Bitcoin non potrà riconoscere in alcun altro modo la proprietà del denaro, la relativa somma di denaro sarà inutilizzabile da chiunque e, quindi, da considerarsi persa in modo irrimediabile.

## Scambio di Btc, le transazioni

La gestione delle transazioni è il cuore del funzionamento di bitcoin, come delle altre criptovalute. Devo poter gestire lo scambio di denaro evitando che:

- Sia impossibile spendere soldi che non si possiedono
- Sia impossibile spendere due volte gli stessi soldi
- Sia impossibile contraffare le transazioni simulando di essere qualcun altro

Essendo un sistema decentralizzato non ho un ente centrale regolatore, ma è il sistema stesso che si deve autogestire.

### Come evitare la contraffazione - la firma digitale

Per capire il funzionamento è necessario capire il significato di firma digitale con chiave pubblica e privata. Questo meccanismo utilizza due metodi fondamentali, il metodo **Sign** (firma) e il metodo **Verify** (verifica). Il primo utilizza la chiave privata (che non deve essere divulgata a nessuno) mentre il secondo la chiave pubblica che, per definizione, è pubblica.

La firma digitale di un documento (_Message_) è l'output di una funzione che dipende dal documento stesso e della chiave privata (_PrivateKey_). Il vantaggio della firma digitale è che questa cambia ogni volta in base al documento che voglio firmare.

```
Sign(Message, PrivateKey) = Signature.
```

Il metodo _Verify_ un metodo che ha in uscita solo un valore booleano: true se la firma è autenticata, false altrimenti. Questo metodo utilizza la chiave pubblica (_PublicKey_). Grazie a questo metodo posso capire se il messaggio _Message_ è stato firmato (_Signature_) con la chiave privata corrispondente alla chiave pubblica _PrivateKey_.
```
Verify(Message, Signature, PublicKey) = true/false. 
```
Utilizzando questo trucco è possibile verificare che il firmatario sia davvero l'utente X senza che questo mi riveli la sua chiave privata. Dato che questa ultima è un numero a 256 bit esistono 2^256 possibili chiavi, numero gigantesco e impossibile da conoscere.

Un dettaglio: dato che la funzione _Signature_ dipende solo dal _Message_ e dalla _PrivateKey_, a parità di _Message_ otterrei la stessa firma. Questa firma può essere copiata quindi da un malintenzionato duplicando il messaggio varie volte. Supponiamo che il messaggio sia "A deve dare a B 1 BTC": se io potessi copiare la _Signature_ potrei fare inviare più volte a B 1 BTC. Per evitare questo problema si aggiunge un numero univoco ad ogni _Message_ in modo che questo cambi ogni volta e conseguentemente porti che anche la firma cambi ogni volta.

## Proof of Work

^ca85ef

Nelle criptovalute il concetto fondamentale è che la moneta è, di fatto, una lista di transazioni ([[Distributed Ledger]]) da quando la moneta è stata creata ad oggi. Questa lista è chiamata [[Blockchain]] in cui **ogni blocco ha uno e un solo padre, come uno e un solo figlio**. Tale lista deve essere condivisa identica tra tutti i nodi della rete e sempre sincronizzata con le nuove transazioni.

![[source-Hoyes1-1024x535.webp]]

Ora, analogamente al metodo della firma digitale che permette di sapere se una transazione è autentica, deve esistere un modo per **validare un blocco**, quindi capire se è un blocco formato da delle transazioni effettivamente avvenute oppure è un blocco formato da transazioni contraffatte.

Per capire il funzionamento è necessario capire cosa sia una **funzione crittografica di hash**: questa è una funzione che, dato in ingresso una stringa (_Message_) fornisce una stringa di bit con lunghezza fissa, per esempio 256 bit. La loro caratteristica fondamentale è che se anche un solo bit di _Message_ cambia il risultato sarà completamente diverso, inoltre dato un risultato è impossibile ottenere il _Message_ originale se non provando a indovinare. Un esempio di funzione di hash utilizzato per tutta la crittografia mondiale (e anche in Bitcoin) è SHA256.

**Per la rete un blocco è valido se è associato ad un numero per cui lo SHA256 del blocco inizi con una serie di zeri.**

Per esempio se il numero di zeri è 30 la probabilità di ottenere tale hash è circa 1 su un miliardo: dato che per trovarla è necessario provare a caso, questo è un lavoro lungo per un PC ma non eterno. Una volta trovato quel numero casuale che concatenato al messaggio fornisca in hash che inizia con 30 zeri il blocco viene considerato valido dalla rete. Più è la potenza computazionale dei computer, prima verrà trovato tale numero.

Questo metodo è detto **Proof-of-Work e indica la prova che per validare il nodo è stato eseguito del lavoro** **computazionale**. Il PoW fa parte, genericamente, degli **algoritmi di consenso**, che sono il cuore di ogni Distributed Ledger permissionless (come la [[Blockchain]] di Bitcoin).

L'idea dietro il concetto di [[Blockchain]] è che ogni blocco contiene l'hash del blocco precedente. Qualora io modificassi l'ordine di due o più blocchi dovrei modificare anche invertissi l'ordine di due blocchi, per esempio, cambierebbe l'hash e conseguentemente cambierebbe anche il numero da trovare per avere lo SHA256 che inizia con gli zeri. Dovrei quindi rifare il lavoro per tutta la rete.

Nota bene: tecnicamente l'algoritmo del PoW dei Bitcoin **non si basa sul numero di zeri ma che l'hash, se interpretato come un numero intero, sia inferiore ad un numero target**. Dato che lo SHA256 è un numero binario, esso è convertibile in un numero. Impostare che il numero binario prodotto dallo SHA256 abbia _n_ zeri all'inizio è equivalente a dire che tale numero, in formato decimale, sia minore di un target. Questo valore è indicato nel campo _nBits_ dell'header di un blocco.

### Sincronizzazione

Il problema principale da risolvere è la sincronizzazione tra i vari nodi: assumiamo che il nodo A abbia validato il blocco _X_, come fa a trasmetterla agli altri nodi? Gli altri nodi infatti potrebbero avere validato il blocco _Y_ ma, dato che la [[Blockchain]] è una catena unica, un nodo può avere un solo padre.

Quindi dopo il blocco _B_ ci può essere o _X_ o _Y_.

La rete deciderà il blocco con la catena più lunga e, in caso di pareggio, aspetterà che una delle due catene diventi più lunga dell'altra per sceglierla.

Il blocco non scelto diventerà un blocco orfano (vedi [[Cosa è una [[Blockchain]]?]].

### Tempo di blocco

Il numero di zeri da trovare non è costante ma varia in base al numero di minatori presenti nella rete (TH/s della rete, vedi il paragrafo "difficulty" più in basso) in modo che il tempo necessario alla rete per trovare un blocco sia sempre circa 10 minuti.

Questo tempo è chiamato **tempo di blocco**.

Maggiore quindi è il numero di miner in gioco maggiore sarà la loro potenza di calcolo e maggiore sarà il numero di zeri da trovare.

Non tutte le crypto hanno uguale tempo di blocco, per esempio ETH ha 15 secondi, LTC 2.5 minuti e così via. Dato che in un blocco vi sono circa 2400 transazioni il numero di transazioni al secondo è circa 5, pochissime.

Per maggiori informazioni vedi il [Bitcoin scalability problem](https://en.wikipedia.org/wiki/Bitcoin_scalability_problem).

## Il mining

Definito come validare un blocco introduco un altro concetto fondamentale per comprendere il funzionamento di Bitcoin, che è il mining.

![[farm-2852024_1280-1024x682.webp]]

Come descritto sopra varie transazioni sono racchiuse in blocchi concatenati tra di loro, tali blocchi devono avere un PoW corretto. **Lo scopo dei miner è quindi raccogliere tali transazioni, creare un blocco, trovare il numero per cui lo SHA256 del blocco inizi con _n_ zeri e inviare tale blocco corretto a tutta la rete**. Questo lavoro di creazione dei blocchi della [[Blockchain]] è computazionalmente dispendioso e il sistema deve implementare un incentivo affinché vengano investite delle risorse, tempo ed energia elettrica, per far funzionare questa rete.

Questo incentivo è il "_block reward_" che è una speciale transazione che viene aggiunta all'inizio del blocco indicante che il creatore del blocco riceve _n_ BTC. Questi soldi non provengono da nessuno (quindi non devono essere firmati) e inoltre significa che **all'aumentare dei blocchi aumenta il numero totale dei BTC presenti nella rete**.

Esistono degli enti chiamati minatori (_miner_) che effettuano tali computazioni allo scopo di ottenere i _block reward_.

### Mining pool

Ora il che il TH/s della rete Bitcoin è gigantesco è assolutamente impossibile pensare di lavorare da soli come miner (a differenza dell'inizio della rete Bitcoin) in quanto la probabilità di trovare un blocco valido autonomamente è infima.

E' molto meglio decidere di ricevere delle piccola ricompense costanti rispetto ad avere una enorme ricompensa ma ogni 1000 anni; per questo motivo i miner si uniscono in quelle che si chiamano "**mining pool**", quindi insieme di nodi che si dividono il compito (e quindi anche la ricompensa).

### Halving

Il numero di BTC che vengono forniti ai creatori di un nuovo blocco valido non è un valore costante ma, partendo da 50 BTC viene dimezzato ogni 210000 blocchi che corrispondono circa a 4 anni. Quindi se nel 2009 creare un nuovo blocco valido forniva ai miner 50 BTC ora ne fornisce 6.25. Questo processo è detto **halving.**

Inoltre vi è un limite imposto della rete di un massimo di 21000000 bitcoin, per cui una volta raggiunta tale cifra di btc estratti non ci saranno più _block reward_ ma solo i reward delle transazioni. Questo per creare una valuta deflazionistica il cui valore è destinato ad aumentare nel tempo data l'impossibilità di stampare nuove monete. Di fatto è una versione dell'oro ma digitale, ovviamente a patto che tale bene sia universalmente accettato.

### Transaction fees

Oltre al block reward ogni transazione può includere una piccola fee ai miner per incentivare questi ultimi ad includere la transazione in questione nel prossimo blocco. Dato che ogni blocco può avere solo circa 2400 transazioni i partecipanti alla rete bitcoin avranno delle alte commissioni per evitare che la propria transazione sia dimenticata dai minatori.

## Come evitare transazioni non autorizzate

Ora vediamo come il metodo descritto sopra permetta di evitare che una persona A crei un blocco contraffatto indicante, per esempio, che la persona B ha dato 1 BTC ad A.  
Il malfattore A dovrà quindi creare una transazione indicante questo passaggio e incapsularla in un blocco. Dovrà inoltre trovare il numero per il PoW del blocco. Una volta creato un blocco valido questo verrà inviato agli altri nodi della rete. Il punto è che nel frattempo anche tutti i miner della rete stanno creando i nuovi blocchi della [[Blockchain]] e li stanno inviando a tutti i nodi. Come fa un nodo a decidere chi ascoltare? Sceglierà la catena più lunga.

I nodi della rete vedranno quindi parallelamente il blocco contraffatto e gli altri blocchi validati dai minatori ma tipicamente la catena formata da questi ultimi sarà più lunga. Anche fosse lunga uguale con il passare del tempo la catena creata dai minatori sarà per forza più lunga di quella creata da A, portando quindi la rete ad escluderla.

A potrebbe vincere la sfida con i minatori se possedesse più del 50% della potenza computazionale dell'intera rete, cosa impossibile.

## Struttura di un blocco

Andiamo ora ad analizzare nel dettaglio la struttura di un blocco btc, partendo da un esempio reale, il blocco 714176.

Per guardare come è fatto ogni blocco btc esiste il sito [https://www.[[Blockchain]].com/](https://www.[[blockchain]].com/) , per esempio [qui](https://www.[[blockchain]].com/btc/block/714176) abbiamo tutte le informazioni sul blocco in questione.

Questi valori non sono letteralmente i valori dell'header di un blocco btc, ma sono tutte le info esplicite ed implicite presenti in un blocco. Ho indicato con **\[H\]** i valori che sono espliciti nell'header bitcoin (per approfondire vedi [qui](https://developer.bitcoin.org/reference/block_chain.html)).

<table><tbody><tr><td><strong>Nome</strong></td><td><strong>Valore</strong></td></tr><tr><td>Hash</td><td>00000000000000000007dcf0c0fd8dfe65e42e29559e9f4ea736fd11fc009437</td></tr><tr><td>PrevHash <strong>[H]</strong></td><td>000000000000000000085fdc889506f714f7b4cb931943b23bd100da8c7086bc</td></tr><tr><td>Confirmations</td><td>85</td></tr><tr><td>Timestamp <strong>[H]</strong></td><td>2021-12-14 23:44</td></tr><tr><td>Height</td><td>714176</td></tr><tr><td>Miner</td><td>SlushPool</td></tr><tr><td>Number of Transactions</td><td>3,397</td></tr><tr><td>Difficulty</td><td>24,195,286,980,613.62</td></tr><tr><td>Merkle root hash <strong>[H]</strong></td><td>2edbefb589929ff4810216e463f07ef31a642db0ac3c14a52d399e5a1297738f</td></tr><tr><td>Version <strong>[H]</strong></td><td>0x20e00004</td></tr><tr><td>Bits <strong>[H]</strong></td><td>386,638,367</td></tr><tr><td>Weight</td><td>3,993,085 WU</td></tr><tr><td>Size</td><td>1,542,631 bytes</td></tr><tr><td>Nonce <strong>[H]</strong></td><td>3,326,021,014</td></tr><tr><td>Transaction Volume</td><td>9375.27337835 BTC</td></tr><tr><td>Block Reward</td><td>6.25000000 BTC</td></tr><tr><td>Fee Reward</td><td>0.12704690 BTC</td></tr></tbody></table>

### Hash

Identificativo univoco del blocco corrente. Questo identificativo è due volte lo SHA256 di tutto il blocco, compreso lo l'hash del blocco precente. Questo dettaglio garantisce l'impossibilità di invertire l'ordine dei blocchi a meno di ricalcolare tutti i nonce.

### PrevHash

Hash del blocco precente. In questo modo ho un collegamento univoco tra i due blocchi.

### Confirmations

Numero di blocchi successivi al blocco in questione. Questo valore indica la probabilità che tale blocco sia accettato definitivamente dalla rete. Come abbiamo detto in precedenza, il fatto che vi sia un blocco valido non porta al fatto che tale blocco sia accettato dalla rete: potrebbero esistere altri minatori che hanno trovato un blocco quasi simultaneamente a me e conseguentemente la rete deve aspettare prima di inserire un blocco nelle [[Blockchain]] in modo definitivo. In altre parole, la rete deve aspettare che il blocco abbia un certo numero di "conferme", che sono i blocchi successivi a questo ultimo. Più sono le conferme più abbiamo la certezza che il blocco sia legittimo e entrato nella [[Blockchain]].

Per transazioni gigantesce di bitcoin potrebbero essere necessarie 6 conferme, quindi 6 blocchi successivi e il processo impiegare circa una ora. Per valori più piccoli invece ci possono volere anche solo due o una conferma.

Per esempio [Binance](https://www.binance.com/it/activity/referral-entry?fromActivityPage=true&ref=LIMIT_RL2B9JPF) richiede una conferma affinché il btc venga visualizzato nel portafoglio ma 2 conferme per essere sbloccato, in questo modo Binance si tutela sul fatto che il blocco in questione non sia un blocco orfano ma un blocco effettivamente accettato nella [[Blockchain]].

![[image-1.webp]]

Conferme richieste da Binance

### Timestamp

Tempo di creazione del blocco.

### Height

Posizione del blocco nella Blockchain, nel nostro caso significa che vi sono 714175 blocchi prima di questo.

### Miner

Nome, opzionale, del minatore che ha completato il blocco (e ha ricevuto il block reward).

### Number of Transactions

Numero di transazioni presenti nel blocco.

### Difficulty

Misura di quanto difficile sia trovare il nonce che permetta allo SHA256 del blocco di essere inferiore ad un numero target, quindi che inizi con un determinato numero di zeri.

La difficoltà è modificata ogni 2016 blocchi minati è deriva dalla potenza stimata di tutti i miner misurata in TH/s (vedi [Total Hash Rate (TH/s)](https://www.[[blockchain]].com/charts/hash-rate)), in questo modo maggiore è l'hash rate complessivo della rete maggiore sarà la difficoltà e viceversa, il tutto per avere sempre un tempo intrablocco di 10 minuti.

In questo modo la rete bitcoin è resiliente anche ai crolli di hash rate (come il crollo del 2021 dovuto al ban del mining in cina) in quanto adegua di conseguenza la difficoltà.

Sottolineo che TH/s significa Tera Hash al secondo, cioè 10^12 hash al secondo. In questo momento la rete bitcoin viaggia sui 200m TH/s, cifre assolutamente impensabili per un normale PC.

Per avere una idea di come è variata la difficoltà è interessante il grafico: [https://www.[[Blockchain]].com/charts/difficulty](https://www.[[blockchain]].com/charts/difficulty)

### Merkle root

Hash di tutti gli hash di tutte le transazioni nel blocco. Questo valore permette che nessuna transazione può essere modificata senza modificare anche l'header e conseguentemente invalidare la PoW. Per approfondire vedi [https://it.wikipedia.org/wiki/Albero\_di\_Merkle](https://it.wikipedia.org/wiki/Albero_di_Merkle)

### Version

Indica quale versione delle regole di validazione di un blocco seguire. Ad oggi esistono quattro versioni dalla più vecchia (1) all'ultima (4).

### Bits

L'hash dello SHA-256 dell'header di un blocco dev'essere minore o uguale ad un determinato valore target per essere accettato dalla rete. Questo valore è rappresentato in forma compatta da _nBits_. Per convertire il campo _nBits_ nel numero target utilizzo la formula:
```
(last three bytes) \* 256 ^ ((first byte) - 3)
```
Che fornisce il numero a 256 bit il quale ha i primi 3 byte significativi del target. Per approfondire vedi [qui](https://developer.bitcoin.org/reference/block_chain.html#target-nbits).

### Weight

Misura della dimensione del blocco, misurata in Weight Units (WU). Il protocollo limita la dimensione massima di un blocco a 4 milioni di WU, limitando così il numero di transazioni massimo includibili in un blocco. 4 milioni di WU sono equivalenti a 4MB, che è infatti la dimensione massima attuale di un blocco.

### Size

Misura della dimensione massima dei dati presenti in un blocco. Prima della modifica SegWit i blocchi Bitcoin erano limitati a 1MB, ora sono a 4MB.

### Nonce

Numero che permette all'hash del blocco di essere minore o uguale al target. E' la Proof-of-Work.

### Transaction Volume

Numero di transazioni nel blocco.

### Block Reward

Reward in BTC che vengono forniti al creatore del blocco.

### Fee Reward

Somma dei reward delle transazioni presenti nel blocco.

## Conclusione

Come abbiamo visto capire nel dettaglio il funzionamento della [[Blockchain]] Bitcoin non è immediato, è necessario capire bene alcuni dettagli ad alto livello ma anche scendere a particolari di crittografia e informatici.

Vi sono numerosi altri dettagli su cui non mi sono soffermato, probabilmente li approfondirò in articoli successivi.