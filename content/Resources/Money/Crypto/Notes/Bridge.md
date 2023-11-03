---
tags:
  - Crypto
  - Definition
  - PublishedPosts
---


## Blockchain EVM e non EVM

Negli ultimi anni sono nate numerose blockchain diverse, ognuna con la sue caratteristiche e compatibilità.

In particolare possiamo dividere le [[Blockchain]] in due famiglie principali: **le chain EVM compatibili e non EVM compatibili**. L' [[Ethereum Virtual Machine (EVM)]] è la macchina che permette agli smart contract di Ethereum di girare.

Oltre a Ethereum anche altre chain sono compatibili con l'EVM, questo significa che una DApp scritta per la chain ETH può girare allo stesso modo sulla chain [[Avalanche]], per esempio, oppure [[Binance Smart Chain (BSC)]].

Le chain EVM compatibili hanno tutte l'indirizzo del wallet che inizia con 0x, utilizzano [[Solidity]] come linguaggio di programmazione e sono compatibili con [[MetaMask]].

Le chain non EVM (per esempio [[Polkadot]] o [[Solana]] e gli address sono diversi.

## A cosa servono i Bridge?

L'esistenza tra tutte queste chain porta alla necessità di doversi muovere tra una e l'altra: da questa esigenza nascono i bridge. Dato che ogni chain è, per definizione, indipendente da qualsiasi altra chain **per poter far passare dei token da una chain all'altra ho bisogno di un intermediario, chiamato appunto bridge**.

Se voglio trasferire 1 ETH da un indirizzo 0xFoo a 0xBar, su Ethereum, devo effettuare una normale transazione senza bisogno di alcun bridge.

Se invece voglio **trasferire 1 ETH da 0xFoo sulla rete ETH a 0xFoo sulla rete Avalanche ho bisogno di un bridge, analogamente ho bisogno di quest'ultimo se voglio trasferire da 0xFoo a terraFoo**.

N.b.: **a partire da un seed, l'indirizzo per tutte le reti EVM compatibili è esattamente lo stesso**. MetaMask infatti, a parità di wallet, fornisce lo stesso indirizzo per Eth, Avalanche, BSC e tutte le eventuali reti EVM compatibili.

## Funzionamento

Per esempio assumiamo di voler far passare [[USDC]] ([[Resources/Money/Crypto/Notes/Token]] [[ERC20]]) da dalla chain Ethereum alla chain [[Binance Smart Chain (BSC)]] quindi token BEP20. Un bridge è analogo ad un pool di liquidità contenente i due collaterali che voglio "scambiare": quando riceve i token [[USDC]] [[ERC20]] li terrà per se e invierà al wallet di destinazione i corrispettivi token BEP20.

Un bridge ovviamente funziona se possiede i due collaterali, analogamente ai pool di liquidità.

## Tipologie di Bridge

### CEX - Centralized Exchange

Gli exchange centralizzati come [[Binance](https://codicepragmatico.it/crypto/appunti-su-bnb-e-binance/), [FTX](https://ftx.com/it) o [crypto.com]] sono anche dei bridge in quanto permettono di depositare e prelevare sulle varie chain ed effettuare tutti gli swap che mi servono. Qualora un CEX non abbia il token che mi interessa potrei potenzialmente combinarli tra di loro: per esempio depositare euro su Crypto.com, convertirli in [[USDT]], passarli a Binance, convertirli in Luna e caricarli su Terrastation.

### Bridge Multichain

Questi bridge sono piattaforme decentralizzate che tipicamente possiedono una grande quantità di coin e di chain. Il bridge più famoso è [Multichain](https://app.multichain.org/) per lo scambio di token cross-chain in ambito EVM.

Qualora il token sulla chain di destinazione non sia compatibile ne viene fornita una versione wrappata come, per esempio, il famoso [[WBTC]]. Per esempio ETH sulla rete Ethereum è una coin ma non sulla rete Avalanche, nella quale la coin è AVAX. Per avere ETH sulla rete Avalanche ne viene fornita una sua versione [[ERC20]], che è, appunto, WETH.

### RenBridge

![[ren_og_image-1024x535.webp]]

[RenBridge](https://bridge.renproject.io/) permette di ottenere la versione "ren" del token in questione su qualsiasi chain. **La comodità del token ren è che c'è molta liquidità**, quindi è sempre possibile scambiarlo poi successivamente nel token che voglio.

Per funzionare RenBridge mi fornisce un address temporaneo per 35 ore dove andare a caricare la crypto in questione; una volta ricevute esso accrediterà lo stesso valore in rentoken nell'address della [[Blockchain]] di destinazione.

Viene utilizzato principalmente per BTC in quanto renBTC è utilizzatissimo.

### WormHole

![[WhatsApp-Image-2021-09-19-at-11.08.26-PM.webp]]

[WormHole](https://wormholebridge.com/) bridge è stato creato per Solana. Esso converte il token nella sua versione whtoken nella [[Blockchain]] di destinazione. Tutte le piattaforme basate su Solana accettano e swappano il token "wh"

### Terra Bridge

[Terra Bridge](https://bridge.terra.money/) permette di spostare un qualsiasi token del mondo Terra (Luna, USD, Anchor) nelle chain compatibili

### Celer Bridge

[Celer Bridge](https://cbridge.celer.network/#/transfer) è un bridge layer 2 su Ethereum, quindi permette di spostare token nelle chain EVM come Polygon, BSC ma anche [Arbitrum](https://bridge.arbitrum.io/) e [Optimism](https://www.optimism.io/).
