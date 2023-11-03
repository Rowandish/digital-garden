---
tags:
  - Crypto
  - Coin
  - PublishedPosts
---


BNB è la moneta nativa di Binance, la piattaforma di exchange di criptovalute che vanta il volume di transazioni più grande al mondo. È stata fondata del 2017 dallo sviluppatore cinese Changpeng Zhao.

I BNB nascono come mezzo per pagare le commissioni sulle transazioni dell’Exchange anche con il tempo il loro utilizzo si è espanso alla possibilità di essere utility [[Resources/Money/Crypto/Notes/Token]] della comunità nell'ecosistema [[Binance Smart Chain (BSC)]] (come giochi e DApp), alla possibilità di partecipare alla vendita di [[Resources/Money/Crypto/Notes/Token]] ospitate su [Binance Launchpad](https://launchpad.binance.com/) e così via.

BNB è nato come [[Resources/Money/Crypto/Notes/Token]] [[ERC20]] su Ethereum, poi è stato trasferito su Binance chain (BEP2). Inoltre è stata creata una ulteriore [[Blockchain]] in grado di ospitare BNB chiamata Binance Smart Chain.

Questo significa che ora è possibile trovare BNB in tre diverse forme:

- BNB BEP-2 su Binance Chain.
- BNB BEP-20 su Binance Smart Chain.
- BNB ERC-20 sulla rete Ethereum.

## Il coin burn

![[04-Binance-BNB-coin-burn.webp]]

Uno dei vantaggi di Bitcoin è l'impossibilità che ne esistano più di 21 milioni. Questo vincolo è una fortissima leva antinflazionistica che porta bitcoin a essere più simile all'oro che a una moneta effettiva. Binance ha avuto l'idea simile ma più sottile: invece di imporre un tetto massimo di monete circolanti nel sistema, emetto una certa quantità di monete subito e poi, con il passare del tempo, secondo dei parametri interni, riduco forzatamente una certa quantità di monete dall'offerta totale fino a raggiungere il valore massimo di monete desiderato.

Binance **rimuove quindi permanentemente una quantità specifica di BNB in base alle statistiche delle transazioni all’interno dell'Exchange negli ultimi tre mesi**. Questo permette di ridurre l'offerta totale di BNB in circolazione in modo che questi ultimi aumentino il loro valore, agendo quasi come processo antinflazionistico. Maggiore risulta il volume di trading sulla piattaforma, maggiore risulta il quantitativo bruciato.

Gli eventi burn di BNB sono programmati per avvenire ogni trimestre **fino a quando 100.000.000 BNB non saranno stati distrutti**, valore che rappresenta il 50% del totale dei BNB emessi (200.000.000 BNB).

Ad oggi sono stati bruciati 33.199.679 BNB portando quindi il loro quantitativo totale a 166.801.147 BNB.

### Burn function

Lo smart contract BNB presenta una funzione nota come burn function la quale rimuovere in modo permanente una quantità di monete dall'offerta in circolazione del richiedente. Ovviamente nessuno chiamerà questa funzione eccetto Binance stesso. Un esempio di chiamata alla funzione burn lo si può trovare [qui](https://etherscan.io/tx/0xbf97244cf0c5709e0dd36e37bacb994f95c245aaf20a279595b5371ff592f4b0) (quando BNB era ancora sulla rete Ethereum).L'attuale meccanismo di coin burn su BNB non si basa più su uno smart contract, ma su un comando specifico eseguito su Binance Chain.

## Ethereum chain (standard ERC20)

I [[Resources/Money/Crypto/Notes/Token]] **BNB supportavano lo standard [[ERC20]] per lo sviluppo di smart contract basati su Ethereum** (vedi [[Resources/Money/Crypto/Notes/Token]] [[ERC20]], [[Stablecoin]], ICO. Un po’ di chiarezza]]. Inizialmente queste monete erano effettivamente [[Resources/Money/Crypto/Notes/Token]] ospitati sulla rete di Ethereum ma, nell’aprile 2019, si decise di cambiare le monete BNB [[ERC20]] con BEP2 BNB con una proporzione di **1:1**. Ciò significa che BNB non è più ospitata sulla [[Blockchain]] Ethereum.

## Binance Chain (standard BEP2)

Binance Chain è un nuova [[Blockchain]] lanciata da Binance ad aprile 2019 con l'obiettivo primario è permettere il **trading di valute in modo veloce** e decentralizzato.

**BEP-2 è lo standard tecnico per l'implementazione di [[Resources/Money/Crypto/Notes/Token]] nella [[Blockchain]] Binance**, quindi è un analogo dello standard [[ERC20]] per l'implementazione di [[Resources/Money/Crypto/Notes/Token]] nella [[Blockchain]] Ethereum. Lo standard permette ai [[Resources/Money/Crypto/Notes/Token]] BEP2 di poter interagire fra di loro e con l'ambiente, inoltre permette di poter rappresentare un ampio range di veni digitali o scambiabili.

L'asset nativo della Binance chain è BNB che è usato per pagare le fee di transazione (analogamente al gas di Ethereum), quindi per poter scambiare [[Resources/Money/Crypto/Notes/Token]] BEP2 è necessario avere sempre una piccola quantità di BNB nel wallet.

I [[Resources/Money/Crypto/Notes/Token]] BEP2 possono essere scambiati sul Binance Decentralized Exchange ed è possibile visualizzare tutti i [[Resources/Money/Crypto/Notes/Token]] BEP2 esistenti sulla [Binance Chain block explorer](https://explorer.binance.org/assets/bep2).

## [[Binance Smart Chain (BSC)]]

### Consenso

L'algoritmo di consenso utilizzato è il Proof-of-Stake (vedi [[Perchè il Proof-of-Stake è rivoluzionario]]**. A differenza di molti protocolli, non vengono distribuite ricompense in BNB appena emessi, in quanto BNB non è inflazionario, ma solo ricompense nelle fee di transazione.

### Compatibilità cross-chain

Binance ha pensato BSC come un sistema indipendente ma complementare alla Binance Chain: grazie all'architettura **_Dual-chain_ è possibile trasferire facilmente asset da una chain all'altra**.

In questo modo Binance offre le **performance di un trading rapido con la Binance chain**, mentre la possibilità di scrivere **smart contract e quindi dApp su BSC**; in questo modo viene offerta una soluzione completa per tutti i casi d'uso.

### Dapp su BSC

[Defistation.io](https://www.defistation.io/) è sito che mostra una classifica di progetti [[DeFi]] che operano su Binance Smart Chain. È possibile controllare il valore totale bloccato (TVL) nei progetti [[DeFi]] sulla Binance Smart Chain in tempo reale.

![[2021-12-22-11_29_56-Defistation-1024x325.webp]]

Maggiori quattro dApp presenti su BSC

## Considerazioni

L'ecosistema Binance è sicuramente vasto e funzionale, ogni giorno si arricchisce di nuove funzionalità. Il problema è la centralizzazione del potere. Le criptovalute sono nate per essere decentralizzate e anarchiche: non vi deve essere alcun ente centrale in grado modificarne il valore, di censurarle e così via.

Con Binance stiamo andando esattamente nella direzione opposta: un ente centrale che gestisce la compravendita da valute (exchange), crea nuove valute (BNB) e perfino creare nuove [[Blockchain]] (BSC e BC).

Data la quantità di crypto presenti sugli exchange, questi ultimi possono influenzare il mercato comprando o vendendo valute per centinaia di milioni di dollari per i propri interessi speculativi. Inoltre, nel caso di BNB, essi possiedono metà dell'offerta delle monete in circolazione, permettendo così di avere un potere gigantesco sul valore di queste ultime.

Qualora ci fosse un crollo del mercato e tutti volessero vendere le proprie monete per ottenere soldi, siamo sicuri che Binance permetterebbe tutto ciò? E se Binance o andasse in bancarotta chiudesse cosa succederebbe?

> Not your keys, not your crypto.
