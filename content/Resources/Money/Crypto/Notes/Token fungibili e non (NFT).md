---
tags:
  - Crypto
  - Definition
  - PublishedPosts
---


## Introduzione

Per capire lo scopo dei [[Token fungibili]] e non ([[NFT]]) bisogna fare un passo indietro. All'inizio dell'era crypto esisteva un solo tipo di asset digitale: la valuta. In particolare Bitcoin è un sistema pensato proprio per gestire un nuova valuta digitale e centralizzata. Questa ha lo scopo di avere tutte le caratteristiche di una valuta fisica ma senza un ente centrale che la può coordinare.

Con l'avvento di Ethereum si è superato il concetto di valuta, infatti si parla di "piattaforma distribuita" in quanto, oltre alla valuta (nello specifico ETH) è stata creata la possibilità di sviluppare anche gli [[Smart contract]] che di fatto sono degli script che girano sulla rete blockchain.

"_E se io scrivessi uno smart contract che gestisce degli asset digitali rappresentanti un determinato bene in una determinata piattaforma?_" Good point.

Una volta che sviluppo la possibilità di creare del codice all'interno della [[Blockchain]] le possibilità sono infinite!

Gli asset digitali gestiti da uno o più smart contract vengono chiamati _[[Resources/Money/Crypto/Notes/Token]]_, che possono rappresentare qualsiasi cosa: soldi, servizi, tempo, [[azioni]], [[obbligazioni]], bene virtuale, un gioco…

La comodità di rappresentare qualcosa come token è che possiamo permettere agli smart contract di interagire con loro, quindi scambiarli, crearli o distruggerli in modo completamente virtuale e decentralizzato.

La differenza con una moneta è che il token è pensato funzionante solo **in una determinata piattaforma**: chi ha sviluppato Binance ha pensato di sviluppare anche il token BNB come token per poter pagare i servizi della piattaforma o genericamente permettere a questa ultima di funzionare. In alcuni casi tali token sono diventati talmente grandi da diventare simili ad una valuta, per cui possono essere scambiati anche all'esterno della piattaforma che li ha creati.

## [[Tokenizzazione]]

## Cosa significa avere un token?

Un token contract è semplicemente uno smart contract su Ethereum che contiene un mapping tra indirizzi e saldi e metodi per aumentare o diminuire questi saldi.
```CSharp
mapping (address => uint) public balances;
```

Quindi "inviare token" di fatto significa "chiamare un metodo su uno smart contract che riduce il mio saldo e ne aumenta dello stesso valore quello di qualcun altro".

**Qualcuno quindi "ha un token" se, all'interno di tale smart contract, ha un bilancio maggiore di zero**. Semplice.

## [[Token fungibili]]

## [[NFT]]


