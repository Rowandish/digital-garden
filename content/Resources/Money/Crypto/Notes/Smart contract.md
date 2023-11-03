---
tags:
  - Crypto
  - Definition
  - Coding
---


Gli **smart contract** sono protocolli informatici che facilitano, verificano, o fanno rispettare, la negoziazione o l'esecuzione di un contratto, essi quindi specificano le condizioni di un accordo tra parti diverse. Sono la versione informatica dei contratti fisici tra le persone validati da un notaio.

Il termine smart si riferisce al fatto che **le condizioni sono specificate ed eseguite sotto forma di codice eseguito in una [[Blockchain]]**, anziché su un foglio di carta conservato da un notaio.

La blockchain è l'infrastruttura informatica che si sostituisce al notaio in quanto garantisce, intrinsecamente, sicurezza, affidabilità e accessibilità. Io potrei, potenzialmente, scrivere i miei smart contract con un normale software ma questo non sarebbe trasparente ne sicuro. Si sfrutta quindi la blockchain per poter far girare degli script "validati" intrinsecamente. E quando si parla di milioni di dollari questa condizione è fondamentale.

## Differenze tra contratto tradizionale e smart contract

Il contratto tradizionale trova il proprio meccanismo di salvaguardia nel suo essere giuridicamente vincolante, in quanto protetto da una fonte normativa esterna al contratto, ovvero, dall’ordinamento giuridico. Infatti, è l’ordinamento giuridico a prevedere, nel caso in cui una delle parti dovesse essere inadempiente, la possibilità per la parte soccombente a questo tipo di condotta, di adire l’autorità giudiziaria per modificare, annullare o far eseguire le obbligazioni pattuite.

Il contratto intelligente, a differenza del contratto tradizionale, pone il suo meccanismo di vincolatività nella peculiare tecnologia della _blockchain_ e dello _smart contract_ che impedisce _ab initio_ l’inadempimento delle parti. Per il nodo è tecnicamente impossibile violare volontariamente le condizioni prestabilite. Tutto questo pone in secondo piano le problematiche attinenti alla condotta del singolo ai fini dell’adempimento.

## Smart contract sulla blockchain Ethereum

Ethereum è la blockchain più utilizzata per la definizione di smart contract. Vediamo velocemente i passaggi per poter inserire un nuovo contratto all'interno di essa.

- **Definizione dell'accordo**: Per prima cosa vi deve essere un accordo univoco tra le parti, oppure una procedura standard, da tradurre in linguaggio macchina. Gli smart contract sono scritti in numerosi linguaggi di programmazione (tra cui [[Solidity]], Web Assembly e Michelson).
- **Inserimento nella blockchain**: Una volta scritto questo deve essere trascritto nella blockchain. Ethereum, in quanto permissionless, permette a tutti di effettuare questa operazione. C'è una verifica sulla disponibilità dei fondi dell'utente che registra il contratto.
- **Creazione del blocco**: La rete dei dispositivi interconnessi garantisce il mantenimento, l'accessibilità e il corretto aggiornamento di un [[Distributed Ledger]]. Lo smart contract entra a far parte di un blocco (identificato univocamente da un codice hash) che viene validato dai partecipanti della blockchain
- **Validazione**: in Ethereum la validazione di un blocco è attraverso il  [[Proof-of-Work (PoW)]], quindi la soluzione di un problema matematico. Il nodo che trova la soluzione e registra un contratto riceve una remunerazione in Ether.
- **Aggiunta alla catena**: una volta validato il nodo viene aggiunto alla catena, la quale è certificata. L'operazione è pubblica e mostrata sulla piattaforma. Ogni nodo aggiunge un hash alla catena in modo che questa sia sicura e non contraffabile
- **L'oracolo**: per definizione uno smart contract **non può accedere a dati off-chain**, quindi fuori dalla blockchain. In questi casi è necessario utilizzare gli oracoli (oracles in inglese) che sono programmi terzi che fungono tra bridge tra dati on-chain e off-chain. Esistono anche oracoli decentralizzati come [Chainlink](https://github.com/smartcontractkit/chainlink).
- **Esecuzione**: ricevuto l'input dall'oracolo avviene l'esecuzione del contratto, qualora le condizioni siano rispettate. per eseguire uno smart contract sulla rete Ethereum, è necessario versare una commissione denominata "gas" (è chiamata così perché le commissioni consentono alla blockchain di funzionare).

## Esempi

- **Etherisc**: assicurazione sui viaggi aerei decentralizzata, che opera sulla piattaforma Ethereum. Lo _smart contract_ interroga delle Api (alla fine è codice, quindi le sue potenzialità sono infinite) per avere informazioni sugli orari di partenza e, in caso di ritardo del volo garantito dalla polizza, fa scattare automaticamente il rimborso
- **Uniswap**: una piattaforma di negoziazione decentralizzata che consente agli utenti, tramite smart contract, di scambiare alcuni tipi di criptovaluta senza alcuna autorità centrale che stabilisca i tassi di cambio.
- **Compound**: una piattaforma che utilizza gli smart contract per consentire agli investitori di guadagnare interessi e ai richiedenti di ottenere immediatamente un prestito, senza l'intermediazione di un istituto bancario. 

## Eliminazione

Uno smart contract, una volta inserito in una blockchain non è, teoricamente, eliminabile. Come fare quindi se non le parti non vogliono più utilizzare tale contratto? Potrebbe essere anche una clausola del contratto stesso la sua eliminazione. In alcune blockchain evolute (come Ethereum) è stata implementata la possibilità di effettuare il _kill_ o **funzione di autodistruzione** dello smart contract.
Questa funzione è stata pensata per rimuovere i programmi non più impiegati, con la finalità di efficientare le performance della blockchain, ma può essere anche utilizzata dal nodo che ha creato lo smart contract per, attraverso l’inoltro di una transazione e immettendo nella blockchain il corrispondente codice elettronicamente firmato, ovvero, le parti potrebbero anche inserire la funzione di autodistruzione all’interno dello smart contract e nell’eventualità prevedere, in un accordo a latere, i casi di attivazione della medesima.

## Limiti

- Non tutto è traducibile in linguaggio informatico: nella realtà è facile riscontrare casi in cui per gestire alcuni accordi si rende necessario conferire un certo grado di ambiguità e discrezionalità che è impossibile tradurre in codice
- Le parti che sottoscrivono tale contratto possono non essere dei programmatori, essi quindi si troverebbero nella condizione di chiedere a terzi programmatori che si occuperebbero di trasporre il linguaggio naturale in linguaggio formale comprensibile alla macchina. Ho quindi un dispendio economico e una delega a terzi, che di fatto sono gli intermediari che dovrebbero, teoricamente, non servire più con l’avvento di questa tecnologia.
- Il programmatore che scrive il contratto potrebbe compiere degli errori, sia di interpretazione che di programmazione. Questi errori porterebbero dei risultati inattesi senza la possibilità di modificare tale contratto.
- Essendo la blockchain una tecnologia per definizione internazionale, in caso di controversie quale sistema giuridico utilizzare?

## Conclusione

Definiti i vantaggi e i limiti, lo _smart contract_ è una soluzione estremamente innovativa e conveniente in presenza di accordi standard definiti univocamente e poco complessi. In quel caso basta programmare una sola volta lo smart contract e poi numerosi enti lo potranno utilizzare senza temere bug o ambiguità.

Pensare di sostituire qualsiasi accordo commerciale con uno smart contract ad oggi è difficile, ma si possono fare dei passi in avanti per la regolamentazione e giustiziabilità di tali contratti in modo da poter utilizzare, potenzialmente, una soluzione ibrida.

La finanza centralizzata, o [[DeFi]], è l'applicazione più concreta ed utilizzata di smart contract e permette di investire denaro, o di ottenerlo tramite prestiti, senza passare per una banca o un exchange, riducendo quindi i costi senza rinunciare alla sicurezza.

## Fonti

- [https://www.altalex.com/documents/news/2020/10/21/blockchain-smart-contract-benefici-limiti](https://www.altalex.com/documents/news/2020/10/21/blockchain-smart-contract-benefici-limiti)
- [https://www.coinbase.com/it/learn/crypto-basics/what-is-a-smart-contract](https://www.coinbase.com/it/learn/crypto-basics/what-is-a-smart-contract)
- [https://www.ilsole24ore.com/art/smart-contract-cosa-sono-e-come-funzionano-clausole-blockchain-ACsDo2P?refresh\_ce=1](https://www.ilsole24ore.com/art/smart-contract-cosa-sono-e-come-funzionano-clausole-blockchain-ACsDo2P?refresh_ce=1)
