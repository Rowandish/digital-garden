---
tags:
  - Crypto
  - Definition
  - PublishedPosts
---


Le [[Blockchain]] layer-2 sono state introdotte per risolvere il problema di scalabilità di blockchain (layer-1) che soffrono di questo problema, una su tutte Ethereum. Una migliore scalabilità porta ad un aumento della velocità e riduzione delle fee necessarie ad ogni transazione.

Una soluzione layer-2 è un algoritmo o blockchain o piattaforma che permette di risolvere i problemi di scalabilità della blockchain sottostante non utilizzando una blockchain o utilizzandone una alternativa. Successivamente verranno inserite le transazioni nella blockchain sottostante.

Ad oggi esistono varie soluzioni layer-2.

## State Channels

Uno state channel è un canale di comunicazione tra due o più partecipanti che permette di effettuare le stesse interazioni che avvengono con una blockchain ma senza usarne effettivamente una. Non avendo una blockchain non ho PoW, miner o quant'altro. Una volta che tutte le transazioni sono state completate, lo stato finale viene aggiunto alla blockchain originale.

Le più famose soluzioni State Channel sono **Bitcoin Lightning Network** per Bitcoin e **Ethereum Raiden Network** per Ethereum.

## Nested Blockchains

Una nested blockchain è una (o più) blockchain che opera sopra una altra blockchain. In particolare potrei avere n blockchain dedicate ognuna ad un particolare compito (pagamenti, [[DEX]], [[Smart contract]]) particolarmente veloci e dedicate che ogni tanto vanno a salvare sulla blockchain principale quanto hanno fatto.

Un esempio è il [Plasma Project di Ethereum](https://docs.ethhub.io/ethereum-roadmap/layer-2-scaling/plasma/).

## Conclusioni

Il problema della scalabilità il problema maggiore che le blockchain devono affrontare. Le blockchain moderne come [[Solana]], [[Avalanche]] o [[Polkadot]]; in quei casi non ho bisogno di layer-2 in quanto le chain sono già state pensate in quel modo.

Per le blockchain classiche [[Proof-of-Work (PoW)]] come [[Bitcoin]] ed Ethereum sembra sia necessario introdurre dei layer-2 per poter essere utilizzate a meno di profonde modifiche al protocollo come avverrà con Ethereum 2.0.
