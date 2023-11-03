---
tags:
  - Crypto
  - Coin
  - PublishedPosts
---


Polygon (ex Matic) nasce come [[Blockchain]] per risolvere i soliti problemi legati ad Ethereum: la scalabilità (lento e fee elevate) e la interoperabilità (compatibilità solo con coin EVM).

Ora è un framework per la creazione di reti blockchain e soluzioni di scalabilità compatibili con Ethereum.

Similmente ad altre chain moderne come [[Avalanche]], [[Polkadot]] o [[Solana]] Polygon nasce come Ethereum-killer, transazioni velocissime, fee nulle e la possibilità tramite Polygon di comunicare con altre chain.

## Scalabilità

Polygon è una [[Blockchain layer-2]] sidechain, quindi con una blockchain semi indipendente in quanto ha un suo algoritmo [[Proof-of-Stake]] delegato e il suo pool di validatori ma comunque mantenendo la compatibilità e comunicazione tra la chain Polygon e la mainnet Ethereum.

La maggiore scalabilità rispetto ad Ethereum non è data solo dal PoS, che già non è poco, ma anche da ulteriori accortezze.

### Rollups

Un rollup è una chain detta anche secured-chain: queste chain ereditano i propri meccanismi di sicurezza da Ethereum (non ne sviluppano loro di proprietari) ma, lavorando su una altra chain, offrono maggiore velocità e fee ridotte.

L'obiettivo è spostare tutte le transazioni eseguite da uno smart contract sulla secured chain (layer-2) e poi poi mettere il risultato di queste transazioni sul layer-1.

In pratica lo smart contract gira sul layer-2 e scrive sul layer-1 solo i risultati.

Questo porta ad un notevole risparmio di fee.

### Plasma

Plasma è una funzionalità nativa della rete Ethereum che permette di comunicare off-chain alcune informazioni creando una struttura a catene più piccole.

Polygon sfrutta questa funzionalità allo scopo di creare la sua blockchain (ed eventualmente altre) che lavorano al posto della rete Ethereum, lasciando a questa ultima il solo compito di verificare al correttezza delle transazioni.

## Interoperabilità

Gli sviluppatori di Polygon hanno sviluppato un SDK (Polygon SDK appunto) che permette di fare il **deploy di blockchain layer-2 di Ethereum o chain stand-alone**.

Entrambe queste categorie di chain sono compatibili con EVM e con la mainnet di Ethereum.

## Il token MATIC

Il [[Resources/Money/Crypto/Notes/Token]] Matic è il token che gestisce il PoS della sidechain layer-2 descritta sopra. Quindi posso essere io un validatore oppure delegare i miei Matic ad un altro validatore; la classica funzione delle chain PoS.

Inoltre viene utilizzato per pagare le fee e per la governance del sistema.

## Spostare fondi da Eth a Polygon

![[image-57.webp]]

Per spostare fondi dalla chain Ethereum alla chain Polygon è necessario utilizzare il [wallet web](https://wallet.polygon.technology/).

Una volta acceduto con MetaMask (verrà richiesto di firmare una transazione che non costerà alcuna fee) e aggiunta la chain Polygon è possibile utilizzare il Polygon [[Bridge]] per spostare fondi da una chain all'altra.

## [[Staking]]

Per fare [[Staking]] di token Matic per ottenere la reward è necessario andare nello [stesso wallet](https://wallet.polygon.technology/[[staking]]/) descritto prima, in particolare nella sezione [[Staking]].

Vi sono in totale 100 validatori, si può sceglierne uno e delegare a lui una determinata quantità di token Matic.

L'[[APY]] è circa del 10% e può essere visualizzata dal [loro calcolatore](https://wallet.polygon.technology/[[staking]]/rewards-calculator).

## QuickSwap

QuickSwap è il principale [[DEX]] basato su Polygon. Analogamente ad Uniswap o altri DEX ci sono le classiche funzionalità come lo swap di token, limit order, pool di liquidità e farming e [[Staking]].

### Il token QUICK

Il token QUICK è il token della piattaforma, permette di pagare le fee, viene utilizzato per pagare i liquidity provider e inoltre viene utilizzato per avere diritto di voto per la governance della piattaforma.

Ha una supply molto limitata, in totale solo 1 milione di esemplari di cui 327,100 in circolazione in questo momento.

Ha avuto un boom del valore ad aprile 2021 ad oltre 1400\$, oggi invece siamo sui 60\$ a token.
