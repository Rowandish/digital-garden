---
tags:
  - Crypto
  - Coin
  - PublishedPosts
---


[Solana](https://solana.com/) è una layer-1 [[Blockchain]] il cui obiettivo è riuscire a ottenere tutte e tre le caratteristiche della blockchain ideale: scalabilità, sicurezza e decentralizzazione.
Tipicamente di queste tre caratteristiche le blockchain ne hanno solo due, per esempio [[BNB]] non ha decentralizzazione, Ethereum e [[Bitcoin]] non hanno scalabilità e così via.

Solana è stata fondata da [Anatoly Yakovenko](https://www.linkedin.com/in/anatoly-yakovenko) nel 2017, un ingegnere delle telecomunicazioni; esso è riuscito a trovare un modo per cui una rete di nodi distribuiti abbia le stesse performance di un singolo nodo; obiettivo che nessuna delle blockchain alternative è riuscito a raggiungere.

Per avere una idea blockchain PoW come Bitcoin e Ethereum supportano circa 10 transazioni per secondo (tps), PoS chain alternative aumentano notevolmente il tps come, per esempio, [[Avalanche]] con 5000 tps. L'obiettivo di Solana è raggiungere le 50000 tps su oltre 200 nodi validatori.

Essendo una sola blockchain Solana inoltre **evita lo sharding, cioè la divisione delle blockchain in sotto-blockchain più piccole e specializzate che devono essere gestite sia a livello di sicurezza che di sincronizzazione**.

Queste performance incredibili si basano su 8 tecnologie innovative rispetto alle altre blockchain:

- **Proof of History (POH)**: un clock per la sincronizzazione della validazione dei blocchi;
- **Tower BFT**: algoritmo di consenso con BFT ottimizzato per sfruttare il clock sincronizzato del PoH;
- **Turbine**: un protocollo di propagazione dei blocchi;
- **Gulf Stream**: protocollo di inoltro delle transazioni senza sfruttare un mempool;
- **Sealevel**: meccanismo per lanciare l'elaborazione di transazioni e smart contract in parallelo;
- **Pipelining**: meccanismo per processare la validazione delle transazioni in vari step e ogni step è gestito da un hardware differente;
- **Cloudbreak**: Metodo per scalare la gestione dei database interni delle transazioni;
- **Archivers**: la memorizzazione dei dati avviene su dei nodi distribuiti.

Per avere una idea del numero di validatori correnti, tps e altre statistiche consiglio [Solana Beach](https://solanabeach.io/).

## Proof of History

Anche se si chiama Proof-of-History questo **non è un algoritmo di consenso** ma è il modo in cui Solana organizza i blocchi. L'idea è che i nodi validatori siano sincronizzati da un clock esterno. Le transazioni possono arrivare quindi ad un solo nodo che le valida ma, grazie al clock, il sistema sarà in grado di mettere in ordine tutte le transazioni che sono state validate dai vari nodi parallelamente.

Per approfonfire il PoH e le innovazioni del mondo Solana è molto interessante [questo articolo](https://medium.com/solana-labs/7-innovations-that-make-solana-the-first-web-scale-blockchain-ddc50b1defda).

## PoS with delegation

Per la validazione delle transazioni Solana utilizza un [[Proof-of-Stake]] con "delegation".

Chiunque può creare un nodo validatore a meno di avere un hardware molto performante. A differenza di Bitcoin e Ethereum che possono girare su, potenzialmente, anche un Raspbery un nodo solana deve avere un hardware incredibilmente carrozzato. A differenza con le altre blockchain per diventare un validatore non grande numero di monete in Stake minimo, infatti ad oggi Solana conta ben 1369 nodi validatori, un numero molto alto rispetto, per esempio, a [[Polkadot]] che ne conta solo 300.

Chi non può o non vuole fare il validatore può comunque delegare i propri SOL ad un validatore esistente. Ad oggi le [[APY]] per lo [[Staking]] di SOL delegati ad un validatore è circa del 13% a cui vanno tolte le fee che trattiene il validatore.

## Turbine

Turbine è un protocollo di propagazione dei blocchi contenenti le transazioni ai diversi nodi. Quando bisogna validare un blocco per ottenere un consenso più validatori devono ottenere tale blocco. Per far sì che la propagazione del blocco ai nodi validatori sia la più rapida possibile il blocco viene spezzettato in tanti frammenti con un algoritmo chiamato Turbine e ognuno di essi viene dato ad un nodo peer scelto a random. In questo modo abbiamo ridotto notevolmente la banda richiesta.

## Micropagamenti

Solana punta ad unire il mondo dei micropagamenti con il mondo della [[DeFi]]: il numero elevatissimo di transazioni per secondo permetterebbe a Solana, potenzialmente, di essere usata nei pagamenti di tutti i giorni con commissioni bassissime e alto grado di sicurezza.

Per fare un esempio Visa gestisce 24k transazioni per secondo ([anche se non tutti sono d'accordo](https://news.bitcoin.com/no-visa-doesnt-handle-24000-tps-and-neither-does-your-pet-blockchain/)), la metà di Solana.

## Wallet

### Phantom

[Phantom](https://phantom.app/) è la versione di [[MetaMask]] per Solana. E' quindi un estensione del browser che permette di gestire i propri [[Resources/Money/Crypto/Notes/Token]] basati si Solana.

Il wallet Phantom ha un [[DEX]] incorporato che permette agli utenti di effettuare swap diretti all'interno del software, evitando così il rischio di connettersi a un sito web malevolo o pagare ulteriori fee per trasferire i fondi dal wallet a un altro exchange.

Inoltre permette di visualizzare direttamente gli NFT nel proprio wallet e si connette comodamente a Serum.

### SolFlare

[Solflare](https://solflare.com/) è un wallet non custodial per Solana, molto simile a Phantom tranne che non ha una parte di [[DEX]] evoluta come Phantom.

## Progetti su Solana

Sulla piattaforma Solana sono nate numerose piattaforme, vediamone alcune.
![[0_DIOFu3eR_GElNQ_Z-1024x576.png]]

### Serum

[Serum](https://www.projectserum.com/) è un protocollo per exchange decentralizzati su Solana. E' decisamente la piattaforma di [[DeFi]] più importante di Solana e la base di molte altre. Data la velocità di Solana è possibile fare trading e avere strumenti e visualizzazioni complesse, come l'[[Order book]].

In particolare Serum offre vari singoli [[DEX]], ognuno con la propria caratteristica. E' possibile trovarne un elenco [qui](https://portal.projectserum.com/).

Un esempio è [Bonfida](https://[[DEX]].bonfida.org/#/), un Exchange con order book, limit order, stop losses, take profit… come fosse un normale exchange centralizzato. Bonfida inoltre permette di automatizzare il processo creando dei [bot](https://bots.bonfida.org/#/) che acquistano/vendono in automatico collegandosi a Trading view.

### Radium

Protocollo a pool di liquidità (quindi il classico pool con 2 coin per ottenere le fee di swapping) ma su Solana. Utilizza inoltre la liquidità di Serum e, come sappiamo, maggiore è la liquidità presente sulla piattaforma, meglio è per questa ultima.

[Radyum](https://raydium.io/) permette di ottenere le ricompense da Yield farming, inoltre dando liquidità anche a Serum permette di ottenere delle fee anche da questo ultimo.

Radyum fornisce anche le fusion tools che permettono di avere una fee sia in RAY che nelle altre coin (tipicamente appartenenti al mondo Solana).

### Oxygen

[Oxygen](https://www.oxygen.org/) è un Broker [[DeFi]]: unisce le funzionalità di tutte le piattaforme [[DeFi]] in una unica interfaccia. Per esempio prendo la mia liquidità e posso in parte usarla in prestito, in parte usarla come collaterale per prendere un prestito e così via. Unisce quindi le funzionalità, per esempio, di Aave, Uniswap, Sushiswap e così via.

### Solstarter

Solstarter è una applicazione per fare delle vendite di [[Resources/Money/Crypto/Notes/Token]] (IDO) su Solana. L'idea è attrarre liquidità per poter lanciare progetti in cambio di token del progetto in questione.
