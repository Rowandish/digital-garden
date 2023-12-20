---
tags:
  - Crypto
  - Coding
  - PublishedPosts
---
Per sviluppare sulla [[Blockchain]] con [[Solidity]] è necessario capire dove vanno memorizzati i dati; in particolare la EVM memorizza i dati in tre aree chiamate [storage, memory e calldata](https://solidity-by-example.org/data-locations/).

Mentre nella normale programmazione i dati vengono salvati su un database o, genericamente, sull'hard disk del PC, quando si lavora sulla blockchain non ho accesso ad alcun database o file system.

Per prima cosa è importante capire come vengono definite le variabili e la loro tipologia.

## Variabili

In Solidity esistono due tipologie di variabili:

- **Passaggio per riferimento**: array, stringhe, struct, mapping
- **Passaggio per valore**: tutti gli altri tipi, come `uint`, `boolean`, `char`

Inoltre una variabile può essere:

- **Locale**: dichiarata all'interno di una funzione. Una volta completata la funzione la variabile stessa sarà _out of scope_.
- **Globale**: variabili di stato, dichiarati fuori da tutte le funzioni

## Zone di memorizzazione

Solidity memorizza le variabili in 3 zone distinte: `storage`, `memory` e `calldata`.

E' possibile definire esplicitamente dove andare a memorizzare le variabili utilizzando le parole chiave rispettive `storage`, `memory` e `calldata` ma nella maggior parte dei casi l'utilizzo è implicito.

### Storage

Una variabile memorizzata in storage è **scritta sulla [[Blockchain]]**, queste sono quindi **persistenti** e possono cambiare valore solo se viene chiamato un metodo dello smart contract.

Ogni modifica alla variabile è memorizzato sulla blockchain.

Dato che ogni modifica alla variabile è sulla blockchain, questa tipologia di memorizzazione è la più costosa in termini di gas. La modifica di una variabile in storage è una delle **più costose operazioni in termini di gas** che è possibile fare su Ethereum.

### Memory

Le variabili memorizzate in memoria sono le **variabili locali**: hanno scope limitato alla funzione e possono essere accedute solo all'interno di questa ultima.
```c
function memoryTest(string memory \_exampleString) public returns (string memory) {
        \_exampleString = "example";  // variabile locale, posso modificarla
        string memory newString = \_exampleString; // assegno una altra variabile sempre in memory
        return newString; 
    }
```
### Calldata

Simile a memory, è una locazione temporanea limitata dalla funzione in cui sono dichiarate. Questa è una area di memoria speciale che contiene gli argomenti di chiamate a funzioni esterne.

Le variabili in `calldata` non possono essere modificate o overridate.
```c
function calldataTest(string calldata \_exampleString) external returns (string memory) {
        // \_exampleString viene da una una funzione external, non posso modificarla
        return \_exampleString;
    }
```