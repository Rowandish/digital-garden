---
tags:
  - Crypto
  - Coin
  - PublishedPosts
---


[Avalanche](https://www.avax.network/) è stata lanciata nel settembre 2020 dal team di Ava Labs negli Stati Uniti. L'obiettivo è migliorare la scalabilità, ridurre le commissioni ma senza compromettere la decentralizzazione.

Questa è una piattaforma open source che permette di fare le stesse cose che permette Ethereum, quindi **creare nuovi token, NFT, smart contract e DApp ma risolvendo i grossi problemi che ultimamente affliggono Ethereum**.
Avalanche inoltre permette di **creare blockchain interoperabili e personalizzate, sia pubbliche che private**.

## Problemi che Avalanche vuole risolvere

### Problema 1: aumentare la scalabilità senza centralizzare

Da sempre le blockchain devono fare un **trade-off tra scalabilità e decentralizzazione**: mano a mano che la blockchain aumenta di dimensioni e aumentano il numero di transazioni da validare, può risultare sempre più oneroso ottenere il consenso e quindi validare una transazione. Oneroso sia in termini di tempo che in termini di commissioni, in quanto i miner, data l'elevata richiesta, tenderanno a prediligere sempre le transazioni con associata una commissione più alta.  
La soluzione è ridurre il numero di persone validatori/minatori offrendo ad essi un maggiore potere per validare i blocchi della rete. Questa centralizzazione del potere è però contrario allo spirito delle criptovalute, che nascono proprio con l'intento di essere una moneta decentralizzata non censurabile.

### Problema 2: ridurre le commissioni

Un esempio di questo problema è la rete Ethereum, sempre più utilizzata sia per la sua valuta Ether che per gli smart contract. Questo ha portato un **aumento del gas richiesto per validare ogni transazione a cifre non sostenibili** per una rete che punta ad essere utilizzata globalmente.

### Problema 3: interoperabilità tra le blockchain

Per poter utilizzare gli smart contract su una blockchain è necessario passare su Ethereum. Sarebbe invece interessante riuscire a creare blockchain che possano comunicare tra di loro.

## Funzionamento

Avalanche è una piattaforma unica nel suo genere in quanto **utilizza 3 blockchain diverse ma interoperabili: X-Chain, C-Chain e P-Chain**.  
Queste blockchain hanno ruoli diversi in modo da migliorare la velocità e scalabilità invece di utilizzare una sola chain. Anche l'algoritmo di consenso non è unico ma dipende dalle varie chain. L'utility token nativo per le tre chain è AVAX, utilizzato per lo [[Staking]] e per pagare le commissioni di rete.

**Avalanche ha la propria Avalanche Virtual Machine (AVM), che è anche compatibile con (EVM). Gli sviluppatori che conoscono [[Solidity]] possono utilizzare facilmente Avalanche e trasferirci sopra dei progetti esistenti**.

![[primary-network-b3e87276c00ce9c3f875cf17aaa29422-1024x512.webp]]

Fonte immagine: [https://docs.avax.network/learn/platform-overview/](https://docs.avax.network/learn/platform-overview/)

### Exchange Chain (X-Chain)

Viene utilizzata per **creare e scambiare token AVAX e altri asset digitali** (versioni su blockchain di azioni, bond, nft…). Le commissioni di transazione vengono pagate in AVAX e la blockchain utilizza il protocollo di consenso Avalanche.

Questa chain è la chain con cui si integrano i vari Exchange, per esempio se compro AVAX su Binance li sto comprando da questa chain. Binance permette di prelevare sia su rete AVAX-X (chiamato AVAX) che direttamente AVAX C-Chain per poter essere subito operativi sulla [[DeFi]].

![[image-2.webp]]

Opzioni di prelievo di AVAX su Binance

### Contract Chain (C-Chain)

**C-Chain è la blockchain in cui vengono eseguiti gli smart contract**. E' compatibile con la [[Ethereum Virtual Machine (EVM)]] è possibile effettuare un fork delle Dapp compatibili con EVM per passare a C-Chain. Utilizza una versione modificata del protocollo di consenso Avalanche chiamato Snowman.

### Platform Chain (P-Chain)

**Questa chain gestisce tutto l'algoritmo di consenso della rete, quindi si occupa di coordinare i validatori di rete, lo [[Staking]] e la creazione e gestione di nuove sottoreti (subnet)**. Le sottoreti sono un insieme di validatori che forniscono il consenso per le blockchain personalizzate. Una blockchain può essere convalidata da una sola subnet, ma ogni subnet può convalidare più blockchain.  
Ogni sottorete gestisce i membri che vi appartengono e può richiedere che i validatori debbano avere determinate caratteristiche, per esempio può richiedere, per esempio, che:

- i validatori siano tutti dello stesso stato
- i validatori devono passare dei controlli KYC (Know Your Customer) o AML (Anti-Money Laundering) https://complyadvantage.com/insights/kyc-aml-know-your-customer-vs-anti-money-laundering/
- i validatori devono possedere una determinata licenza
- i validatori devono possedere un determinato hardware (per esempio per gestire una sottorete la cui applicazione deve essere particolarmente performante)

Anche P-Chain utilizza il protocollo di consenso Snowman.

## Gli algoritmi di consenso

### Avalanche

Nei classici algoritmi di consenso [[Bitcoin#^ca85ef|Proof of Work]], [[Proof of Stake (PoS)]] o DPoS si basano sul fatto di avere un solo attore che crea un blocco valido, che viene poi validato dalla rete. Con Avalanche invece non ho un solo nodo che crea il blocco ma **sono tutti i** **nodi della rete** **impegnati nel lavoro.**

Prendiamo una transazione, questa viene **gestita da più validatori i quali chiedono ad altri validatori casuali di determinare se la transazione è valida**. Se la maggioranza è favorevole a validare la transazione il validatore va in stato OK e i validatori vicini a lui chiederanno la stessa cosa alla rete. C'è un contatore chiamato contatore di confidenza che aumenta di uno ogni volta che un validatore fornisce la stessa risposta. In caso di transazioni conflittuali viene costruito un grafico aciclico diretto (directed acyclic graph) (DAG) che i validatori devono risolvere. Dopo un certo numero di questi sotto campionamenti casuali ripetuti, è statisticamente dimostrato che sarebbe quasi impossibile che una transazione risulti falsa. Inoltre non vi sono dei blocchi come nelle blockchain tradizionali, ma transazioni principali note come vertici.

Un esempio grafico del funzionamento dell'algoritmo di consenso lo si può trovare qui: [https://tedyin.com/archive/snow-bft-demo/#/snow](https://tedyin.com/archive/snow-bft-demo/#/snow)

  
L'esecuzione di un nodo validatore e la convalida delle transazioni hanno requisiti hardware minimi e accessibili, che portano a prestazioni e decentralizzazione maggiori.

### Snowman

Il protocollo di consenso Snowman si basa sul protocollo di consenso Avalanche ma ordina le transazioni linearmente. Questa proprietà è vantaggiosa sopratutto per gli smart contract. A differenza del protocollo di consenso Avalanche, Snowman crea dei blocchi.

## Il token AVAX

**AVAX è il token nativo di Avalanche con una supply limitata a 720 milioni di token. Tutte le commissioni pagate sulla rete sono bruciate come meccanismo deflazionistico**. Il token ha tre funzionalità principali:

1. Gli AVAX possono essere messi in [[Staking]] per diventare un nodo validatore (stake minimo di 2000 AVAX e un hardware di fascia media) oppure delegarli ad un altro validatore (minimo 25 AVAX). Il rendimento [[APY]] dello [[Staking]] è circa il 10%.
2. AVAX funge da unità comune tra tutte le sotto reti, migliorando l'interoperabilità.
3. Le commissioni di transazione e gli abbonamenti subnet sono pagabili in AVAX.

## Blockchain personalizzate

Avalanche consente anche la creazione di blockchain interoperabili e personalizzate in base alle proprie esigenze; in particolare permette **la creazione sia di blockchain senza autorizzazione (pubbliche) che con autorizzazione (private)**.  
Nelle blockchain private posso autorizzare solo un determinato numero di validatori a vedere il contenuto della rete, in modo che questo ultimo rimanga quindi privato.  
Ogni blockchain può avere dei token nativi personalizzati e le commissioni di transazione possono esseri pagati con questi. **È prevista una tariffa di abbonamento pagata in AVAX per la creazione e il mantenimento di una sottorete e di una blockchain**. Anche chi si occupa della gestione delle sotto reti deve essere autorizzato nella sottorete primaria così da poter convalidare anche le sotto reti personalizzate.

## Vantaggi

Avalanche può essere definito come un progetto completo, di fatto non è necessario utilizzare niente che sia esterno alle blockchain. Gli eventuali oracoli necessari per svolgere alcuni progetti vengono messi a disposizione da Chainlink, che si trova sempre all’interno del protocollo. Uno dei punti di forza di Avalanche è il suo lato fortemente green, si tratta infatti di un progetto a consumo energetico particolarmente basso e permette quindi di svolgere le stesse funzioni ma a un dispendio energetico ridotto.

## DeFi su Avalanche

Sull'ecosistema Avalanche sono presenti tutta una serie di piattaforme di [[DeFi]], quindi piattaforme per il lending, il pooling, aggregatori, [[DEX]] e così via.

Una idea del mondo DeFi su Avalanche la si può trovare qui: [https://defillama.com/chain/Avalanche](https://defillama.com/chain/Avalanche)

### Aggiungere Avalanche a MetaMask

Per aggiungere Avalanche a MetaMask è necessario aggiungerlo come rete custom, dato che MetaMask di default lavora solo con Ethereum.  
Per fare questo cliccare sul dropdown indicante le reti -> Custom RPC e inserire i seguenti valori:

- **Network Name**: Avalanche Network
- **New RPC URL**: https://api.avax.network/ext/bc/C/rpc
- **ChainID**: 43114
- **Symbol**: AVAX
- **Explorer**: https://snowtrace.io/

Avalanche su MetaMask funziona **solo con la C-Chain**, quindi qualora siano stati trasferiti dei fondi da un exchange e non siano visibili su MetaMask significa che questi sono sulla X-Chain. In questo caso è necessario effettuare un trasferimento cross-chain per far passare gli AVAX dalla X-Chain alla C-Chain.

### Spostare gli asset dalla rete Ethereum alla AVAXC

Per spostare degli asset presenti sulla blockchain Ethereum (come ETH o token ERC20) alla blockchain AVAXC è necessario utilizzare una piattaforma di [[Bridge]] come [https://bridge.avax.network/](https://bridge.avax.network/).

Queste piattaforme prendono il token ERC20 da Ethereum e te ne **forniscono una versione ".e"**, che è un token AVAXC che ha lo stesso valore del token su Ethereum. Per esempio se forniamo un ETH, questo verrà trattenuto dal bridge e in cambio lui mi fornirà un token ETH.e, sulla rete AVAC. In qualsiasi momento posso fornire il token .e al bridge e riottenere il token sulla blockchain Ethereum.

### BENQI - Lending su Avalanche

[BENQI](https://benqi.fi/) è la maggiore piattaforma di lending basata su Avalanche C-chain (ovviamente, essendo basata su smart contract). Il gas viene pagato in token AVAX. Posso quindi depositare collaterale, ricevere una ricompensa, prendere un prestito e così via.

### Pangolin - DEX

[Pangolin](https://pangolin.exchange/) che permette lo swap (scambiare un token con un altro) e mettere i token in pool. Su Pangolin il rendimento è interessante se presenti AVAX o PNG (la coin di Pangolin).

### TraderJoe - DEX

Con [TraderJoe](https://traderjoexyz.com/#/home) posso fare tutto ciò che posso fare in un [[DEX]], quindi posso creare pool, fare trade, farmare e così via.

### Yield Yak - Aggregatore

[Yield Tak](https://yieldyak.com/) è un aggregatore che permette di fare farming e pool nelle piattaforme con [[APY]] maggiore. Si appoggia agli altri DEX ma con l'aggiunta dell'[[Autocompounder]].
