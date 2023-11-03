---
tags:
  - Crypto
  - Coding
  - PublishedPosts
---

 
Solidity è un linguaggio orientato agli oggetti pensato per implementare [[Smart contract]].

E' un linguaggio fortemente influenzato da C++, quindi è fortemente tipizzato, con ereditarietà e permette la definizione di tipi forti definiti dall'utente.

Un contratto in Solidity è un insieme di funzioni e dati (assomigliano quindi ad una classe di C++) che risiede su uno specifico address sulla [[Blockchain]] Ethereum.

## Il linguaggio

### Header
```c
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;
```
Tutti gli header degli script di Solidity iniziano con l'indicazione della licenza (in formato standard leggibile da macchina). Dato che sono script che per definizione saranno pubblici, indicare la licenza è importante.

La riga seguente indica le versioni di Solidity con cui questo script è compatibile.

### Variabili di stato

Prendiamo la seguente riga di codice:
```c
uint data;
```
Questa riga indica una variabile chiamata `data` di tipo `uint`. Fin qui tutto bene, come in C.

La differenza rispetto ai normali linguaggi di programmazione è che tale variabile non è salvata su una ram, ma è salvata sulla [[Blockchain]], come se fosse su un database.

Una volta impostata (da una funzione dello smart contract), tale variabile rimarrà perennemente a tale valore fino a che non verrà modificata.

### Variabili globali

Quando si sviluppa uno smart contract è possibile accedere sempre a delle variabili standard.

- `block.timestamp`: valore Unix dell'ora corrente. Per "corrente" intendo quando il blocco dove verrà aggiunta la mia transazione viene aggiunto alla chain
- `msg.sender`: address di chi sta chiamando lo smart contract
- `msg.gas`: gas della transazione rimanente in quel punto della funzione
- `msg.value`: messaggio del mittente
- `this`: indirizzo dello smart contract corrente.
- `this.balance`: quanti Ether sono posseduti dallo smart contract (in Wei)

### Tipi o keyword

#### `Address`

In Solidity posso utilizzare un nuovo tipo di variabile, chiamato `address`, che indica un indirizzo, di uno smart contract o di un wallet.

Questo tipo di dato è estremamente comodo per gestire chi possiede una determinata di quantità di coin o quanto viene gestito dallo smart contract.

#### `public`
```c
uint public data;
```
La keyword `public` associata ad una variabile di stato permette di creare una funzione implicita per accedere al valore di tale variabile fuori dal contratto (quindi tipicamente da parte di interfacce web o altri smart contract).

#### `Mapping`

Il mapping è il corrispettivo in Solidity dei dizionari (o hash tables) per cui ho una struttura dati chiave-valore.
```c
mapping (address => uint) public saldi;
```
Per esempio nella riga seguente creo un dizionario chiave valore in cui mappo indirizzi con un numero che, per esempio, potrebbero indicare il numero di coin possedute da tale indirizzo.

#### `Event`

Gli event permettono di comunicare ai listener dello smart contract (tipicamente applicazioni web) che un determinato evento è avvenuto all'interno dello smart contract.
```c
event Sent(address wallet, uint data);
// Quando serve...
emit Sent(wallet, data);
```
Per esempio nell'esempio indicato sopra posso fornire all'interfaccia web i parametri `wallet` e `data` quando l'evento viene lanciato.

Per approfondire come costruire applicazioni web che possano ascoltare a tale evento approfondire [web3.js](https://github.com/ChainSafe/web3.js).

#### Require

La keyword `require` permette di indicare un determinato insieme di condizioni per cui una determinata funzione dello smart contract possa essere chiamata.

Per esempio con il codice seguente posso forzare che la chiamata ad una determinata funziona possa essere chiamata solo dall'address chiamato `special_wallet`.
```c
require(msg.sender == special\_wallet);
```