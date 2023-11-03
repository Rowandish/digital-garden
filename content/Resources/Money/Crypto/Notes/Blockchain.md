---
tags:
  - Crypto
  - Definition
  - PublishedPosts
---


![[Blockchain_main_chain.webp]]

La [[Blockchain]] è una struttura dati condivisa e immutabile in cui le cui **voci sono raggruppate in "blocchi", concatenati in ordine cronologico**, e la cui integrità è garantita dall'uso della crittografia. Tale tecnologia fu inventata da [Satoshi Nakamoto](https://it.wikipedia.org/wiki/Satoshi_Nakamoto) per registrare le transazioni effettuate con i Bitcoin. Una volta scritti, i dati in un blocco non possono essere retroattivamente alterati senza che vengano modificati tutti i blocchi successivi ad esso e ciò, per la natura del protocollo e dello schema di validazione, necessiterebbe del consenso della maggioranza della rete.

Ad un blocco possono essere associate una o più transazioni e ogni blocco, inoltre, contiene un l'hash del blocco precedente e un timestamp.

Essa fa parte dei [[Distributed Ledger]], rimando all'articolo linkato per maggiori informazioni.

Ogni [[Blockchain]] deve avere le seguenti caratteristiche:

- Definire la struttura di un blocco
- Gestire come approvare un nuovo blocco (algoritmo del consenso)
- Gestire come risolvere i conflitti, per cui due nodi producono simultaneamente due blocchi concorrenti collegati allo stesso blocco ma diversi nel contenuto (fork).

## Definizione del blocco

Un blocco è la struttura dati core di una [[Blockchain]], contiene sempre **un header e un body**. Nell'header vi è l'hash del blocco precedente, un timestamp e delle informazioni addizionali; nel body invece vi sono le transazioni da salvare.

Di seguito un esempio di come sono strutturati gli header delle [[Blockchain]] di Bitcoin e Ethereum.

### Blocco Bitcoin

L'header di un blocco bitcoin è formato

| Bytes | Nome | Tipo | Significato |
|--|--|--|--|
|32|PrevHash|char\[32\]|Hash del blocco precedente|
|32|Merkle root|char\[32\]|Hash di tutti gli hash di tutte le transazioni nel blocco.|
|4|Timestamp|unit32|Timestamp dell'ultima transazione in Unix hex timestamp|
|4|nBits|unit32|Valore target: l'hash dello SHA-256 dell'header di un blocco dev'essere minore o uguale a questo valore per essere accettato dalla rete|
|4|Nonce|unit32|Numero che permette allo SHA-256 dell'header del blocco di essere inferiore al target _nBits_. E' la PoW del blocco.|
|4|Version|int32|Indica quale versione delle regole di validazione di un blocco seguire.|

### Blocco Ethereum

| Nome | Significato |
|--|--|
|Previous Block Hash|Hash del blocco precedente|
|Transaction Hash Root|Hash root generato da "Merkle Patricia Trie"|
|Receipt Root Hash|Hash receipt generato da "Merkle Patricia Trie"|
|State Root Hash|Hash world state generato da "Merkle Patricia Trie"|
|Timestamp|Timestamp di quando il mining è finito|
|Difficulty|Difficoltà nel trovare un hash corretto. Vedi [https://2miners.com/eth-network-difficulty](https://2miners.com/eth-network-difficulty)|
|Nonce|Valore utilizzabile una volta per funzioni di crittografia|
|Gas Limit|Valore massimo di gas utilizzabile per quel blocco|
|Gas Used|Somma di tutto il gas usato in tutte le transaction del blocco|
|Extra Data|Campo addizionale comodo per salvare dati extra|
|Number|Contatore del blocco. Il primo blocco ha number = 0.|

## Accettazione di un nuovo blocco - gli algoritmi di consenso

Questi algoritmi sono il cuore di ogni [[Blockchain]] e gestiscono la modalità con cui un nuovo blocco viene aggiunto in tutta la rete.

Questi algoritmi devono impedire l'aggiunta di blocchi errati da parte di nodi malevoli (vedi il [problema della doppia spesa](https://it.wikipedia.org/wiki/Doppia_spesa)), la sincronizzazione tra i nodi della rete e un reward per il lavoro svolto da questi ultimi. Mantenere coerente la [[Blockchain]] tra tutti i nodi di calcolo è un problema non banale, studiato ormai da quasi cinquant’anni e che va sotto il nome del “**problema del consenso**”.

Esistono tre macro tipologie di algoritmi di consenso:

| Nome | Significato |Fattore richiesto | Esempi |
|--|--|--|--|
| Proof-of-Work | PoW |Potenza computazionale | Bitcoin, Ethereum e molte altre |
| Proof-of-Stake |PoS | Criptovaluta posseduta | Cardano, Ethereum 2.0 |
| Proof-of-History | PoH |Ibrido tra Pow e PoS | Solana |
| Proof-of-Capacity | PoC |Spazio libero sull'hard disk | Burstcoin, Btchd |
| Proof-of-Activity |PoA |Ibrido tra Pow e PoS | Decred, Espers |
| Proof-of-Burn | PoB | Numero di monete bruciate | Slimcoin |

## La gestione del fork e dei blocchi orfani

Talvolta risulta possibile che alcuni nodi della rete producano quasi contemporaneamente più blocchi "concorrenti" (ossia collegati a uno stesso blocco già esistente, ma diversi tra loro nel contenuto): ciò dà origine a una biforcazione (_fork_) nella catena. Il protocollo di aggiornamento specifica quale regola i nodi debbano adottare per selezionare il blocco da accettare, tra quelli concorrenti. I blocchi non selezionati per l'inclusione nella catena sono chiamati "blocchi orfani".

### Blocchi orfani in Bitcoin

Quando due minatori riescono a risolvere un blocco quasi contemporaneamente, poiché la rete non accetta e distribuisce istantaneamente il blocco generato, ma piuttosto ha un ritardo, può accadere che un altro minatore risolva esattamente lo stesso blocco;. I due blocchi vengono generati in un tempo molto ravvicinato ed entrambi vengono distribuiti alla rete per la convalida. In questo caso alcuni minatori inizieranno a risolvere il blocco successivo in base all'hash del primo blocco e altri partiranno invece dall'altro blocco. Ad un certo punto uno dei due minatori troverà la soluzione del blocco successivo e lo consegnerà alla rete. I minatori prenderanno la catena più lunga, prediligendo quindi i nodi con maggiore PoW (sono riusciti a risolvere prima il problema matematico).

Il secondo blocco quindi non verrà più accettato dalla [[Blockchain]] divenendo così un blocco orfano, questi vengono conservati in un pool di blocchi orfani ma, di fatto, non servono a nulla.
