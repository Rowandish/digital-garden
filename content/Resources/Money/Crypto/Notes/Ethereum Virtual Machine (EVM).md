---
tags:
  - Crypto
  - Definition
---


La EVM è la virtual machine nella quale girano gli smart contract su Ethereum.
Questa è sandboxed, quindi non può accedere alla rete, ai file system o a qualsiasi altro processo.
E' stata studiata per essere eseguita da tutti i partecipanti del network contemporaneamente

### Account

Esistono due tipi di account che possono accedere ad uno smart contract, gli **external account** (che sono i wallet delle persone fisiche definiti da una coppia di chiavi pubblica e privata) e i **contract account** che sono gli address di altri smart contract.

Gli external account sono identificati univocamente dalla loro chiave pubblica mentre i contract account hanno un address che viene fornito al momento della loro creazione.

Ogni account ha un **balance** che è una determinata quantità di Ether: all'inizio 0 e poi può essere modificata tramite delle transaction a tale account, senza poter mai scendere sotto 0.

Inoltre ogni account possiede dello **storage**, che è una struttura dati contenenti delle variabili di stato. E' in questa area che sono memorizzate le variabili di stato degli smart contract descritte sopra.

Ogni smart contract non può scrivere su alcuno storage eccetto il proprio.

### Transazioni

Una transazione è un messaggio che viene inviato da un account ad un altro (sottolineo che gli account sono sia quelli degli umani che quelli degli smart contract).

Ogni transazione può avere dei dati binari (_payload_) e degli Ether.

Se la transazione punta ad una funzione di uno smart contract, il codice è eseguito utilizzando il _payload_ come ingresso alla funzione.

### Gas

Al fine di limitare il lavoro che deve effettuare l'infrastruttura Ethereum e al fine di ricompensare i nodi della rete **ogni transazione che viene effettuata deve comprendere un determinato valore di gas**.

Per gas si intende una **unità di misura speciale per pagare la computazione effettuata**, quindi, di fatto, quanto lavoro deve fare la EVM per eseguire una serie di istruzioni.

Maggiore sarà la complessità della funzione chiamata, maggiore sarà la quantità di gas richiesta dalla rete per poter funzionare.

Si ritorna quindi alla programmazione vecchia scuola dove le risorse sono finite ed è indispensabile ottimizzare il tutto in modo da ridurre il più possibile il gas necessario a far girare il proprio smart contract. **Per poter scrivere uno smart contract economico è necessario avere una conoscenza su  
come i dati vengono organizzati, modificati e scritti e quale è il costo in gas di ogni operazione**.

Per esempio le operazioni di lettura e scrittura su storage sono costosissime: `sstore` costa 20000 gas e `sload` costa 5000 gas.

Anche se una unità misurabile, non esiste alcun [[Resources/Money/Crypto/Notes/Token]] per il gas, ma questo viene pagato direttamente in Ether. Nel momento in cui effettuiamo una transazione ci viene addebitata una certa quantità di ether che sarà utilizzata automaticamente per comprare il gas necessario alla transazione.

In ogni transazione possiamo definire il _gas price_, che è il prezzo che intendiamo pagare in ether per ogni singola unità di gas e il _gas limit_, ovvero la massima quantità di gas che vogliamo comprare.

Il valore di Ether che pagherò sarà quindi il risultato della **moltiplicazione del gas utilizzato per il prezzo del gas che ho definito**.

Maggiore è il _gas price_ maggiore è la probabilità che i nodi validatori della rete prendano in considerazione velocemente la transazione e la aggiungano ad un blocco della chain. Ovviamente maggiore è il _gas price_ maggiore sarà la fee che pagherò, è quindi sempre necessario trovare il giusto compromesso.

In questo punto è evidente il problema della rete Ethereum: **maggiore è il numero di utilizzatori, maggiori saranno le transazioni da validare e, conseguentemente, maggiore è il _gas price_ minimo richiesto dai validatori per accettare una transazione invece che l'altra**.

Ad oggi la rete Ethereum è utilizzatissima e conseguentemente esageratamente costosa.
