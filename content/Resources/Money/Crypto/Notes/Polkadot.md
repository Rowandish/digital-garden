---
tags:
  - Crypto
  - Coin
  - PublishedPosts
---


**Polkadot è un ecosistema [[Blockchain]] open source che si pone come obiettivo di risolvere i problemi di scalabilità e interoperabilità tra blockchain**.

È un progetto della Web3 Foundation, consorzio svizzero il cui scopo è creare delle applicazioni per il web decentralizzato, web3 appunto. Il presidente è [Gavin Wood](https://en.wikipedia.org/wiki/Gavin_Wood), cofondatore di Ethereum e inventore di [[Solidity]]; sicuramente c'è da fidarsi.

Il punto di forza di Polkadot è proprio la sua estendibilità: è stato progettato per essere un gigantesco ecosistema scalabile ed estendibile dalla comunità, ne sono un esempio i progetti che sono già stati lanciati nel suo breve periodo di vita.

![[g9mzgq7ajif71-1024x621.webp]]

Progetti su Polkadot aggiornati ad Agosto 2021.

## Scalabilità

Il problema delle blockchain è riuscire a supportare un gran numero di transazioni al secondo, con basse commissioni mantenendo la decentralizzazione.

Polkadot risolve questo problema utilizzando lo sharding: la blockchain viene divisa in tante sotto-blockchain coordinate da una blockchain centrale. In questo modo aumenta notevolmente il numero di operazioni che è possibile effettuare nell'unità di tempo.

## Interoperabilità

Le blockchain classiche non sono pensate per poter lavorare insieme: se voglio usare BTC sulla blockchain di Ethereum, per esempio, devo tokenizzarlo]] per poter utilizzare coin di altre reti.

Polkadot supera questo limite permettendo l'interoperabilità tra diverse blockchain in modo che ogni chain che sa fare bene una determinata cosa (per esempio una chain per i pagamenti, una chain per gli smart contract e così via) possa comunicare con le altre chain.

In questo modo verrà creato un ecosistema completo e molto vasto.

## Il token DOT

**Il [[Resources/Money/Crypto/Notes/Token]] nativo DOT non è nato come moneta ma è nato come strumento di gestione dell'ecosistema in modo che possa funzionare**. In particolare serve per:

- **Governance**: i possessori del token possono gestire come andrà a svilupparsi la chain, gestire eventi eccezionali, aggiornamenti e fix. Inoltre i possessori dei DOT possono gestire il consenso agendo come validator, collator, nominator o fisherman;
- **[[Staking]]**: con lo stake gli holder saranno incentivati a comportarsi onestamente: coloro che si comporteranno bene riceveranno dei DOT, gli altri invece verranno eliminati perdendo i DOT in stake. In questo modo il sistema rimane sicuro;
- **Bonding**: i DOT servono anche come garanzia nella creazione di nuove parachain. Infatti questi vengono "legati" (bonding) alla parachain e rimangono bloccati fino a che questa ultima non viene eliminata. E' una sorta di PoS per la creazione di parachain invece che per la normale creazione di blocchi.[](https://polkadot.network/dot-token/#page-top)

DOT è un token inflazionario, non c'è infatti un numero massimo fissato di questi ultimi. Indicativamente questa ultima dovrebbe essere circa il 10% ogni anno, calcolata in quanto i premi per i validatori sono in funzione del numero di DOT messi in stake. Il numero di DOT totali in circolazione è circa ~1,000,000,000, a seguito della procedura di "[Redenomination](http://Redenomination)" avvenuta il 21 Agosto 2021 per cui ogni DOT è stato trasformato in 100 DOT, aumentando quindi di 100 la supply (e conseguentemente portato a 1/100 il valore di ogni singolo DOT).

Controllando il [visualizzatore della blockchain Polkadot](https://polkadot.subscan.io/) è possibile avere informazioni sul numero totale di DOT in stake, sul numero di validatori e sul tasso di inflazione del DOT corrente.

## Relay Chain

![[0_aMrY0Wn71gVRYgHF-1-1024x658.webp]]

Il centro del cerchio può essere visto come la Relay Chain

L'architettura è formata da una architettura modulare composta da diversi componenti con degli specifici compiti che lavorano sinergicamente tra di loro. La rete principale è la Relay Chain a cui verranno collegate le chain secondarie, chiamate parachain. La Relay Chain ha tre compiti fondamentali: governance, consenso e coordinamento delle parachain.

### Governance

Modulo centrale sul quale gira il token DOT, che è il token nativo. Lo scopo del token DOT è principalmente la **governance: gli holder di questo token possono votare per nuove modifiche al sistema in base alle necessità del mondo esterno**. In questo modo non abbiamo un sistema immutabile ma un sistema in continua evoluzione che si adatta. Il "parlamento" è formato da tutti gli holder del token DOT.

In questo modo rende non necessari i fork, cioè le suddivisioni di una blockchain per venire incontro a più esigenze: fork che spesso portano all'indebolimento della chain stessa. E' preferibile invece un sistema "democratico" dove vi sia la maggioranza a decidere la direzione da dare al progetto.

### Consenso

Questa chain inoltre garantisce la sicurezza dei blocchi validati tramite un **algoritmo di consenso proprietario chiamato GRANDPA** (GHOST-based Recursive ANcestor Deriving Prefix Agreement) che è una sorta di [[Proof-of-Stake]] migliorato.

Vi sono quattro ruoli all'interno della rete:

- **Nominators**: nodi che eleggono i validatori. Il potere di nomina avviene tramite lo [[Staking]] di DOT.
- **Validators**: validano le transazioni e i blocchi della blockchain. Anch'essi devono fare [[Staking]] di DOT.
- **Collators**: recuperare tutte le transazioni tra le varie shard, quindi tra le varie sotto blockchain. Le elaborano, producono prove e le passano ai validatori
- **Fisherman**: controllano che non vi siano dei nodi validatori malevoli. In caso di attività sospette i nodi vengono "denunciati" ad altri validatori i quali provvederanno alle punizioni. La più grave è lo slashing: il validatore malevolo viene eliminato e perde i token DOT in stake.

Per maggiori informazioni sull'algoritmo consiglio la documentazione ufficiale: [https://wiki.polkadot.network/docs/learn-consensus](https://wiki.polkadot.network/docs/learn-consensus)

### Coordinamento

Coordina tutte quelle attività necessarie all'interoperabilità tra le diverse chain, quindi **coordinare sia le blockchain natve di polkadot (chiamate parachain) ma anche con blockchain esterne come Avalanche o Ethereum**.

## Bridges

![[upload_62d49fef620fa1829d837944f798f869-1024x568.webp]]

[[Bridge]] che fa comunicare Polkadot con Ethereum

I bridges permettono di far comunicare l'ecosistema Polkadot con le blockchain esterne, come Bitcoin o Ethereum. I bridges sono delle blockchain effettive con un loro token.

### Darwinia Network

Un esempio di bridge è [Darwinia Network](https://darwinia.network/), per Ethereum.

## Parachain

Le parachain sono delle **blockchain sviluppate su Polkadot (comunicano direttamente con la Relay chain) da terzi**. Hanno un loro **token specifico, e ognuna è deputata a svolgere una particolare attività**: dato che è molto semplice svilupparle the sky is the limit.

Sfruttando l'ecosistema Polkadot queste parachain possono comunicare facilmente sia con altre parachain e che con blockchain esterne usando i bridges.

La creazione di parachain è semplice utilizzando il framework [Substrate](https://polkadot.network/build/) fornito dal Polkadot. Essa inoltre si integrerà alle altre blockchain grazie alla Relay Chain, permettendo quindi la creazione di un universo completo di possibilità.

Il numero massimo di parachain è utilizzabili è 100. Ogni slot viene assegnato ad un determinato progetto mediante un asta e solo per un periodo limitato di tempo (lease period).

### Aste di parachain

Data la semplicità nella creazione, per evitare che vengano create parachain inutili, **Polkadot ha pensato che, per poter lanciare una parachain, è necessario vincere una asta (parachain slot auctions).**

Per poter partecipare a queste aste è necessario vincolare dei DOT per un termine anche di 2 anni; questo per far sì che solo progetti seri vi partecipino portando quindi al massimo la qualità dei prodotti.

Le parachain vincenti avranno quindi un boost non solo di visibilità ma anche nel prezzo del loro token interno e, di riflesso, porteranno anche ad un aumento del valore intrinseco di DOT.

La asta viene eseguita periodicamente per alcuni blocchi di slot; chi vince l'asta si aggiudica lo slot per un certo periodo (lease period) per 2 anni. Dopo 2 anni devono partecipare ancora ad un asta per avere ancora lo slot.

**Vince l'asta il progetto che è in grado vincolare più DOT per il lease period. Per recuperare i DOT il partecipante chiede al pubblico di prestargli dei DOT da impegnare (crowdloan o in particolare parachain lease offering) per il lease period, ovviamente in cambio di una ricompensa in token della parachain.**

Di fatto questa è una ICO a tutti gli effetti.

Il pubblico quindi è incentivato nell'investire nei progetti che crede di più, dato che le ricompense saranno proprio nel token della parachain che sto votando.

Una volta finito il lease period vi sarà una altra asta: durante i 2 anni la parachain si auspica che abbia raccolto dei DOT dal suo funzionamento e per i suoi servizi (esempio le fee di una piattaforma [[DeFi]]). Userà quindi i DOT raccolti per vincere l'asta e rimanere in Polkadot.

Per verificare i progetti candidati a entrare come parachain c'è [https://parachains.info/](https://parachains.info/)

![[image-18.webp]]

Controllando lo status è possibile capire se la parachain è già su Polkadot (come Stetemint o Acala) oppure sta partecipando all'asta, come SubDAO o Equilibrium.

Esempi di parachain sono Moonbean (piattaforma di smart contract), Parallel Finance (piattaforma di lending [[DeFi]]), Acala (progetto all-in-one di [[DeFi]]); Bit.Country (creatore di community nel metaverso). Ne vedremo alcune di queste nella sezione successiva.

#### Candle Auction

Come funziona davvero l'asta? Vi è un Candle Auction che è un periodo di 7 giorni durante il quale si possono fare delle offerte: ogni giorno posso aumentare o diminiuire la mia offerta in base a quello che fanno gli altri e così via.

Alla fine dei sette giorni viene preso un giorno a random e si verifica chi offriva di più tale giorno: a quella persona viene assegnato lo slot della parachain.

Questo metodo viene utilizzato per fare sì che le varie parachain offrano subito e sempre l'offerta massima disponibile, per evitare speculazioni sull'offerta degli altri.

## Kusama

![[Que´-es-Kusama-KSM1.webp]]

Kusama è un ambiente in cui i progetti, prima di andare su Polkadot, vengono testati; essa è quindi una testnet.

La differenza con le normali testnet come quelle su Ethereum è che essa ha delle regole di governance più blande rispetto a Polkadot, è più semplice entrare come blockchain nel sistema.

Per questo motivo alcuni progetti rimarranno sempre su Kusama, rendendola così non solo una rete di test ma una blockchain vera a propria.

Kusama possiede il proprio token KSM.

## Moonbeam

![[cropped-Moonbeam-Logo-Final-500px.webp]]

L'idea di [Moonbeam](https://moonbeam.network/) è portare un ecosistema al 100% compatibile su Ethereum come parachain su Polkadot.
Quindi posso eseguire degli smart contract scritti in Solidity e farli interagire con tutte le altre reti presenti su Polkadot. In questo modo posso avere una integrazione al 100% di qualsiasi DApp su Ethereum o Ethereum compatibile (come potenzialmente anche [[Avalanche]] o [[Binance Smart Chain (BSC)]] sfruttando i vantaggi di Polkadot come la governance, la scalabilità e l'estendibilità.

Controllando infatti i [progetti che stanno lavorando su Moonbeam](https://moonbeam.network/community/projects/) troviamo varie piattaforme del mondo Ethereum, una su tutte [MetaMask](https://moonbeam.network/community/projects/metamask/).

## Acala

![[60b973d6fdaaf7fb0cc1aaa2_2021-06-04-02_28_41-Photos-1024x536.webp]]

L'obiettivo di [Acala](https://acala.network/) è creare un hub di finanza centralizzata: tutti i servizi della [[DeFi]] come prestito, credito, lo swap, colleteralizzazione, creazione di [[Stablecoin]] in un unica piattaforma basata su Polkadot.

[Karura](https://acala.network/karura) è la parachain su Kusama analoga ad Acala su Polkadot.

## Astar (Plasm Network)

![[card-image-1024x538.webp]]

Piattaforma simile a Moonbeam, l'obiettivo è rendere compatibile il mondo Polkadot con il mondo Ethereum.

## Reef Finance

![[Reef_Finance_logo-e1636359509238.webp]]

A differenza degli altri progetti di cui sopra [Reef finance](https://reef.io/) non punta a diventare una parachain di Polkadot ma punta ad essere una blockchain indipendente che poi si interfaccerà con altre blockchain come Polkadot, Ethereum gli Exchange centralizzati.

L'idea è riuscire ad integrare la liquidità tra questi mondi: infatti maggiore è la liquidità disponibile più la [[DeFi]] funziona bene in tutte le sue applicazioni. Reef finance vuole essere un mezzo per poter scambiare liquidità tra i vari mondi.

Per comunicare con Polkadot, dato che non sarà una parachain, utilizzerà Moonbeam e Plasm Network.
