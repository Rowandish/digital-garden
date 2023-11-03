---
tags:
  - Crypto
  - Coding
  - PublishedPosts
---


L'obiettivo di oggi è creare un nuovo [[Resources/Money/Crypto/Notes/Token]] [[ERC20]] con [[Solidity]] sulla [[Blockchain]] Ethereum.

_Figo! Potremmo fare il token dedicato a Squid Game!_

Calma amico, [lo hanno già fatto ed è finita male](https://www.bbc.com/news/business-59129466)...

_Potremmo cambiare serie TV! Facciamo il Game of thrones token!_

Per dimostrare la facilità con cui si può creare la propria (shit)coin, mettiamo un timer 15 minuti e via.

## Preparare l'ecosistema di sviluppo

Per prima cosa è necessario preparare quanto serve per lo sviluppo quindi:

- **[Remix](https://remix.ethereum.org/)**: IDE per sviluppare smart contract in Solidity per chain EVM compatibili
- **[Ganache](https://trufflesuite.com/ganache/)**: [[Blockchain]] locale per il testing
- **[OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts)**: libreria open source per lo sviluppo di token [[ERC20]] e [[ERC721]]

### Lavorare con file in locale

Remix permette di lavorare su dei file nella sua cache del browser. Per un token serio come il nostro è necessario avere dei file in locale (magari in una repository…) che si sincronizzano automaticamente con Remix.

Per lavorare con file in locale è necessario il pacchetto NPM chiamato `remixd` Una volta installato `npm` scrivere su terminale
```bash
npm install -g @remix-project/remixd
```
per installare remixd. Una volta fatto è necessario lanciarlo in background indicando la cartella che si vuole utilizzare per sviluppare, usando la sintassi
```bash
remixd -s <Path completo della cartella a cui puntare> -u https://remix.ethereum.org/
```
Una volta lanciato il demone sul proprio PC andare su Remix nel browser e nei workspace selezionare "localhost".

Dopo aver premuto "Connect" appariranno i file presenti in locale.

### Deployare e testare in una [[Blockchain]] locale

![[image-27-1024x364.webp]]

Il modo più comodo per deployare e testare è utilizzare una [[Blockchain]] locale. Per farlo è comodo utilizzare [Ganache](https://trufflesuite.com/ganache/) che, una volta installato, permette di far girare sul proprio pc in localhost su una determinata porta una [[Blockchain]] Ethereum.

Da Remix è possibile deployare su tale [[Blockchain]] indicando come Environment "Web3 Provider" e fornendo la porta di Ganache (default 7545).

## Sviluppo del token

Ok, ora che tutto il nostro ecosistema per lo sviluppo è pronto possiamo iniziare.

_Abbiamo solo 15 minuti, non possiamo perdere tempo a scrivere codice!_

Nessun problema, per lo sviluppo del token ci pensa OpenZeppelin e il suo [Contracts Wizard](https://wizard.openzeppelin.com/)!

Aprendo il link troviamo:

- **Name**: nome del token. Nel nostro caso direi che va benissimo _GameOfThrones_
- **Symbol**: simbolo del token. Formato da 3 lettere, nel nostro caso direi che _GOT_ è perfetto
- **Premint**: numero di token iniziali che vengono forniti automaticamente al creatore dello smart contract. Qualora il token non sia mintabile questo valore è la max supply del token
- **Features**: caratteristiche del token, opzionali.
- **Access control**: possibilità di avere un solo owner del token oppure vari address ognuno con il suo ruolo e i suoi permessi
- **Upgradeability**: gli smart contract, essendo su [[Blockchain]], sono immutabili. Questo può essere evitato se dono deployati su un proxy aggiornabile.

Per il nostro semplicissimo token scegliamo solo _Pausable_ come feature (l'owner può mettere in pausa lo smart contract) e _Ownable_ come Role (l'address che ha fatto il deploy del contratto è salvato come owner e può chiamare delle funzioni speciali).

Indichiamo un premint di 10000 token senza possibilità di minting ulteriore, sarà quindi il nostro max supply et voilà!

![[image-28-1024x646.webp]]

Interfaccia di OpenZeppelin con il nostro GOT token

Copiamo il tutto su Remix e siamo pronti al deploy!

## Deploy

Il deploy può avvenire su 3 diverse chain

- **Blockchain vere**: Ethereum mainnet
- **Blockchain di test**: Ropsten, [Görli](https://goerli.net/)
- **Blockchain locali**: Ganache

Dato che non vogliamo consumare gas fee utilizzeremo Ropsten test network.

Per fare questo è necessario andare nella sezione Deploy di Remix, indicare Injected Web3 e autorizzare con MetaMask (dopo essere passati, su MetaMask, alla chain di test ovviamente…).

![[image-29-1024x654.webp]]

1. Ambiente dove voglio inviare il contratto. Injected Web3 indica che lo sto inviando ad una [[Blockchain]] vera tramite MetaMask; Web3 Provider su una [[Blockchain]] locale come Ganache. La [[Blockchain]] dove verrà aggiunto tale script sarà quella indicata in MetaMask se Injected Web3 oppure sarà la [[Blockchain]] standard di Ganache;
2. Address creatore dello smart contract, sarà quindi anche l'owner
3. Nome dello smart contract da deployare;
4. Deploy! Permette di trasferire lo smart contract sulla [[Blockchain]]

Una volta premuto "Deploy" comparirà l'alert di MetaMask per autorizzare la transazione e pagare le gas fee.

![[image-30.webp]]

Gas fee da pagare per poter mettere il proprio smart contract sulla chain

Confermiamo e via! Il nostro token è sulla [[Blockchain]] e MetaMask fornisce il [link univoco alla transazione](https://ropsten.etherscan.io/tx/0xab64d0af9dcb00c473f768614ed0c88bcd7e03c4f486b39536bcc20820ff423c).

Andando a vedere la transazione troviamo molte informazioni interessanti:

![[image-31.webp]]

1. Address del wallet creatore dello smart contract;
2. Indirizzo univoco dello smart contract che gestirà il token GOT
3. Transazione di minting dei 10000 token GOT, quindi un passaggio dall'address null
4. Al mio address
5. Di 10000 token GOT.

Cliccando sul token si apre la pagina riepilogativa del token che ne indica la max supply, gli holder, le transazioni e l'identificativo univoco del token.

Andando a copiare tale id e inseriamolo in [[MetaMask]] tramite "import token"

![[image-32.webp]]

![[image-33.webp]]

Eccolo! Il nostro bellissimo GOT token è stato aggiunto a MetaMask.

Andando a copiare l'address del contract in Remix compariranno tutti i metodi public dello standard [[ERC20]]. Il metodo transfer, per esempio, permette di trasferire una determinata somma all'address indicato.

![[image-34.webp]]

## Conclusioni

Abbiamo visto come sia semplicissimo sviluppare e deployare un token [[ERC20]] sulla [[Blockchain]] Ethereum. Ovviamente nessun token serio sarà formato dalle 10 righe di codice fornite da un wizard; però non siamo troppo lontani…

Capire come sviluppare un token è una ottima difesa intellettuale contro gli scam, le shitcoin e le piattaforme copincollate. State attenti prima di investire soldi o tempo in un progetto.

A proposito, vi servono dei GOT token?
