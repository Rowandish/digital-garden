---
tags:
  - Crypto
  - Definition
  - PublishedPosts
---
## Introduzione

Il Proof-of-Stake (PoW) è una tipologia di algoritmo di consenso sviluppato come evoluzione del classico [[Bitcoin#^ca85ef|Proof of Work]]. Analogamente al PoW l'obiettivo è validare un nuovo blocco in una [[Blockchain]] decentralizzata senza l'ausilio di un ente centrale.

Nel PoW i miner devono risolvere un problema crittografico, il primo che lo risolve "valida" il blocco e questo può essere immesso nella rete. Un nodo per immettere un nodo malevolo nella rete dovrebbe avere più della metà della potenza computazionale della rete, cosa impossibile. Il miner che risolve il problema riceve il _block reward_, una quantità definita di [[Criptovaluta]].

Questo approccio ha portato, negli anni, a creare delle vere e proprie _mining farm_, capannoni giganteschi contenenti calcolatori con il solo scopo di minare e ottenere Bitcoin, portando ad un consumo gigantesco di energia (ad oggi [ci stiamo spingendo oltre i 91 TWh](https://www.punto-informatico.it/bitcoin-energivoro-mining-consuma-91-twh-anno/)). Per avere maggiore hash/rate e quindi essere premiati dalla piattaforma inoltre i minatori si uniscono nelle cosiddette _mining pool_ portando quindi **ad un accentramento del potere nella rete, cosa opposta alla decentralizzazione necessaria della rete.**

Tutte queste problematiche portano alla necessità di pensare ad un nuovo algoritmo di consenso.

## Funzionamento

L'idea di base è quella di permettere a tutti di competere contro l'altro per il mining è uno spreco. Quindi **sarà la rete che sceglierà, secondo dei parametri, il nodo che dovrà validare il blocco**. Il nodo in questione si chiamerà **_validator_** e il blocco non verrà minato ma coniato (_**forge**)_.

**Il nodo non viene scelto a caso, ma viene scelto tra i nodi che hanno depositato una certa quantità di valuta nella rete (stake), in particolare maggiore è la valuta depositata maggiore sarà la probabilità di essere scelto, linearmente.**
Questa azione è detta [[Staking]].

Questa quantità di moneta è una sorta di deposito cauzionale bloccato che non può essere speso.

Selezione

Per selezionare un blocco validatori non ci si può basare solo sulla quantità di moneta depositata ma anche:

- la longevità dello stake (_coin age_, cioè da quanto tempo è stato fatto il deposito). Quando un nodo viene selezionato dall’algoritmo e conia un nuovo blocco, la sua _coin age_ viene azzerata e dovrà trascorrere un certo periodo di tempo prima che possa essere selezionato nuovamente. Questo sistema impedisce ai nodi con grandi stake di dominare la blockchain.
- fattore di randomizzazione
- Impossibilità di essere scelto due volte consecutive

### Perché la Proof-of-Stake non favorisce i ricchi

Apparentemente questo approccio potrebbe sembrare che avvantaggi i ricchi che possiedono tanta moneta e che, conseguentemente, accentri il potere analogamente al PoW. E' da sottolineare però anche anche il PoW avvantaggia i ricchi che possono permettersi di comprare _mining farm_ in paesi sottosviluppati, la loro potenza non cresce in modo lineare in quanto possono sfruttare le economie di larga scala. Nella Proof-of-Stake invece la relazione è lineare tra investimento e guadagno.

![[1_cuWzazno5Nqaz-qvWarGuQ-1024x576.webp]]

### Validazione

Se un nodo viene scelto come validatore, dovrà verificare che tutte le transazioni all'interno del blocco siano valide; l'algoritmo di controllo dipenderà dalla rete. Una volta verificato il nodo verrà immesso nella rete e inviato a tutti gli altri nodi (che verificheranno che il nodo non contenga transazioni invalide) in modo che aggiornino la loro copia della blockchain locale e il validatore otterrà le fee presenti sulla transazioni del blocco. Non c'è quindi un block reward fisso fornito dalla rete come nei sistemi PoW.

Come evitare che il nodo scelto per la validazione immetta nella rete un blocco invalido? Semplice: così facendo il nodo viene "multato" dalla rete e perderà parte del suo stake e inoltre non potrà più essere selezionato in futuro. Questa "multa" dovrà essere maggiore del _block reward_ ottenuto dalla fee delle transazioni. In questo modo ogni nodo non avrà alcuna convenienza nel validare blocchi contenenti transazioni invalide.

### Vantaggi

Il Proof-of-Stake **consuma notevolmente meno energia** dato che vi è solo un nodo che effettua la validazione e non _n_ in competizione.

Inoltre vi è **meno accentramento di potere**: per la rete bitcoin oggi _BTC.com, AntPool_ e _SlushPool_ insieme fanno più del 50% della forza computazionale della rete. Se si alleassero insieme avrebbero la forza di validare blocchi fraudolenti, mettendo in pericolo l'infrastruttura dell'intera rete. Nel Proof-of-Stake avrei lo stesso problema se avessi il 51% della moneta circolante, quindi il 51% della capitalizzazione della moneta in questione: maggiore è la capitalizzazione più è difficile ottenere ciò. Anche ammettendo di avere il 51% della capitalizzazione di una moneta il mercato attribuirebbe a questa ultima un valore molto basso portando quindi all'impossibilità di avere dei margini soddisfacenti con le sole fee delle transazioni.

Un ulteriore vantaggio vi è nella **velocità dell'approvazione di un blocco:** dato che non vi è alcun problema complesso da risolvere non ho tempi di attesa lunghi per l'approvazione delle transazioni (in btc un nuovo blocco viene immesso nella rete ogni 10 minuti) e quindi potrei, potenzialmente, utilizzare questi sistemi per i pagamenti al dettaglio.

Infine **configurare un nodo per essere un nodo di una rete Proof-of-Stake è molto più semplice** ed economico rispetto a un nodo PoW che necessita di hardware importante, questo incoraggia le persone a diventare dei nodi decentralizzando la rete e rendendola così più sicura.

### Problemi

Il principale problema da risolvere è l'accentramento di potere di chi possiede tante monete, il quale verrà selezionato più spesso e conseguentemente diventerà sempre più ricco. Una idea potrebbe essere considerare da quanto tempo le monete sono state messe in stake e non solo la loro quantità.

## Utilizzo

Il PoS viene utilizzato in questo momento da BNB, Solana (versione ibrida PoH), Avalanche, Cardano, Polkadot e soprattutto il nuovo Ethereum 2.0 che verrà completato nel 2023.