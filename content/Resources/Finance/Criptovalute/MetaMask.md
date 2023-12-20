---
tags:
  - Crypto
  - DeFi
---


[**MetaMask**](https://metamask.io/) è un'estensione del browser e wallet che consente agli utenti di interagire facilmente con gli smart contract della blockchain, quindi le DApp. Potremmo dire che MetaMask connette il web tradizionale con Web3.

**MetaMask è [[Ethereum Virtual Machine (EVM)]] compatibile, quindi compatibile Ethereum e tutte le chain "simili" a Ethereum** (come [[Binance Smart Chain (BSC)]] o [[Avalanche]]. Non è quindi compatibile con Solana, Terra, Cardano, Atom…

L'idea geniale dietro MetaMask è **utilizzare il proprio browser come wallet** che quindi non appartenga ad una determinata piattaforma come Binance o Crypto.com, ma sia possibile interagire con qualsiasi sito di [[DeFi]]; MetaMask inoltre **non è solo un wallet, ma controlla anche l'interazione dell'utente con la DApp**: fornisce i token, paga le fee, indica la disponibilità.

MetaMask funziona grazie all'utilizzo di [web3.js](https://web3js.readthedocs.io/en/v1.5.2/), un insieme di librerie per interagire con la blockchain Ethereum.

Per aumentare la sicurezza è possibile usare MetaMask solo come bridge per la [[DeFi]] collegandolo con un [[Wallet crypto]] esterno, in modo da evitare che il nostro wallet sia online.

## Installazione

Una volta installato dal Chrome store MetaMask fornirà una lista di parole. Quello è il **seed del nostro portafoglio, che lo identifica univocamente**. Essendo un wallet non custodial, perso il seed non si ha alcun modo di recuperare il wallet.

Una volta che MetaMask fornisce il seed verrà richiesto di inserire anche una password, che è la password per poter accedere a quel determinato wallet in quel PC.

Quindi se io vengo a conoscenza di una password MetaMask ma provo ad accedere da un PC diverso, dovrò inserire prima il seed (altrimenti se due persone scelgono la stessa password potrebbero accedere l'uno ai contenuti dell'altro).

Ripeto che se invece venissi a conoscenza del **seed di qualcun altro potrei accedere al suo wallet anche senza conoscere la password**.

## Interfaccia iniziale

![[image-6-1024x440.webp]]

Una volta installato mi verrà fornito un address pubblico sulla rete Ethereum (nell'immagine sopra inizia con 0x692...) con, ovviamente, 0 ETH.

Nel menu a tendina in alto a destra è possibile vedere tutte le reti a cui MetaMask si può collegare, di default la rete Ethereum e le varie testnet.

![[image-7.webp]]

Selezionando una blockchain diversa ovviamente il bilancio cambia.

## Account

In centro in alto è indicato "Account 1" sopra la chiave pubblica del vostro wallet.

MetaMask permette di definire più "account" per ogni profilo, quindi **legati al seed generato sopra**. Infatti **un account è, di fatto, una coppia di chiavi pubbliche/private** e non c'è limite al numero di coppie di chiavi che posso generare.

Per generare un secondo account basta cliccare sull'icona circolare di fianco al menu a tendina e cliccare su "Create Account", inserito il nome e il gioco è fatto.

![[image-9.webp]]

**In MetaMask quindi Account == Address**.

E' possibile anche importare anche un account esterno inserendone la chiave privata (non il seed, proprio la stringa RSA). Questo account non è legato però al seed iniziale, è esterno. Se quindi usassi il mio MetaMask su un altro PC inserendo il seed **non vedrei gli account importati**.

E' infine possibile **connettere a MetaMask un hardware wallet**. Questa è la modalità più sicura in quanto la chiave privata del wallet è su un dispositivo esterno e non online ma comunque senza rinunciare alla comodità di MetaMask: questo ultimo infatti firma le transazioni come se il wallet fosse suo.

MetaMask legge automaticamente i wallet presenti nel Ledger e li aggiunge al proprio account con l'etichetta "hardware": queste sono però sempre le chiavi pubbliche, mai le chiavi private. Quando devo effettuare una operazione come l'invio di ETH ad un account devo confermare la transazione sia su MetaMask ma soprattutto sul ledger: è lui che firma la transazione con le sue chiavi private che non escono mai.

Ovviamente la soluzione hardware wallet è la consigliata qualora il capitale sia notevole: non essendoci un ente centrale che gestisce la sicurezza, la sicurezza sei tu ;)

## Utilizzo

L'utilizzo di MetaMask è estremamente semplice: quando accedo ad una piattaforma di [[DeFi]] questa avrà una specie di pulsante di "login" che di fatto cercherà di connettersi ad un wallet.

Prendiamo ad esempio [Uniswap](https://app.uniswap.org/), una volta entrati in alto a destra premere Connect, selezionare MetaMask ed inserire la password. Comparirà un prospetto per poter selezionare l'account, nel mio caso ho una unica opzione.

![[image-11.webp]]

Una volta concessa l'autorizzazione di avere l'address dell'account (è una chiave pubblica, non c'è problema) avrò effettuato il login. Posso verificare che sia connesso se compare Connesso nell'interfaccia di MetaMask.

![[image-12.webp]]

Inoltre Uniswap mostrerà parte dell'address del mio wallet in alto a destra

![[image-14.webp]]

Le piattaforme di [[DeFi]] possono effettuare sia operazioni in lettura (per esempio mostrare il numero di token presenti nel wallet) che in scrittura, quindi prelevare o aggiungere token.

**Per ogni operazione è necessario pagare delle gas fee** (siamo su Ethereum, no?) che vengono gestite da MetaMask.

Per esempio proviamo a fare uno swap su Uniswap da ETH a UNI usando la rete di test Ropsten di Ethereum, a cui ho caricato 0.3 ETH finti (per ricaricare Ropsten puoi utilizzare [questo faucet](https://faucet.ropsten.be/)).

![[image-15.webp]]

Una volta premuto swap MetaMask mostrerà un prospetto con le gas fee da utilizzare per poter firmare la transazione

![[image-16.webp]]

Una volta confermato lo swap sarà stato effettuato e avrò i miei due token, per esempio ETH e UNI.

![[image-17.webp]]

## Aggiungere altre chain

Di default, oltre alle chain di test, è presente solo la chain Ethereum.

Come abbiamo visto in precedenza, MetaMask è compatibile con tutte le chain EVM compatibili. Per aggiungere una chain è necessario premere il menu a tendina e cliccare su "Add network".

Comparirà una interfaccia dove inserire il nome della rete, l'RPC URL e il Chain Id. Queste informazioni si possono recuperare su Google, ma ancor meglio dal sito ufficiale della chain. E' fondamentale che siano inseriti correttamente, quindi verifica sempre le fonti.

## Spostare liquidità tra le chain

Per spostare una valuta o token tra le varie chain di MetaMask è necessario usare i [[Bridge]] di cui ho approfondito il funzionamento in [[WBTC]].

Assumiamo che voglia spostare ETH sulla rete Avalanche: il [bridge di Avalance](https://bridge.avax.network/) tratterrà ([[Collateralizzazione]]) i miei ETH fornendomi una loro versione wrappata WETH compatibile con la rete Avalanche.

in questo modo avrò "spostato" i miei ETH dalla rete Ethereum alla rete Avalanche sotto forma di WETH.

## Come ottenere ETH di test

Oltre alle blockchain vere MetaMask permette anche di avere dei wallet su delle "test network" che sono delle blockchain Ethereum a tutti gli effetti ma i cui token al loro interno non hanno valore, per definizione.

Per ottenere dei token finti da utilizzare sulle test network esistono i cosiddetti "faucet" (rubinetto in italiano) che sono dei siti che inviano gratuitamente ETH a delle test network a partire dal proprio address.

La test network più famosa è [Ropsten](https://ropsten.etherscan.io/) e un suo faucet è: [https://faucet.ropsten.be/](https://faucet.ropsten.be/)
