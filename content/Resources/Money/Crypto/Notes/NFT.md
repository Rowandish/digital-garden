---
tags:
  - Crypto
  - Definition
---


![[Everydays_the_First_5000_Days.webp]]

Un [[Resources/Money/Crypto/Notes/Token]] non fungibile (NFT) è un tipo speciale di [[Resources/Money/Crypto/Notes/Token]] concepito per fornire **la rappresentazione digitale di un oggetto unico, virtuale o fisico**. Un bene infungibile è un bene che esiste in un solo esemplare o ha caratteristiche intrinseche tali da renderlo infungibile; un esempio, nel mondo reale, di oggetto unico può essere la carta di identità, la propria automobile, la propria casa, una opera d'arte e così via.

**Un [[Resources/Money/Crypto/Notes/Token]] non fungibile è per definizione unico al mondo e non interscambiabile con nessun altro** (a differenza del [[Resources/Money/Crypto/Notes/Token]] fungibile). Attenzione, interscambiabile non vuol dire scambiabile! Gli NFT possono essere scambiabili analogamente ai [[Resources/Money/Crypto/Notes/Token]] fungibili: posso scambiare il [[Resources/Money/Crypto/Notes/Token]] della mia auto per il [[Resources/Money/Crypto/Notes/Token]] della tua auto senza problemi, ma il risultato sarà diverso dallo scambiare una banconota da 5€ con una altra banconota da 5€. Nel primo caso dopo la transazioni vi sono delle differenze, nel secondo caso no.

![[NFT_Non_Fungible_[[Resources/Money/Crypto/Notes/Token]]_-_Explained.webp]]

A differenza delle transazioni in criptovaluta, nelle transazioni aventi ad oggetto gli NFT viene quindi indicato (oltre al prezzo di acquisto) anche il codice di identificazione dell’oggetto creato (o appena scambiato) e, attraverso il sistema della [[Blockchain]], tali dati non possono essere alterati.

L'idea di creare degli oggetti digitali unici da collezione non è nuova, la novità è **che la scarsità e l’unicità dei [[Resources/Money/Crypto/Notes/Token]] [[ERC721]] sono dimostrabili senza che vi sia alcun ente centrale che ne confermi l'autenticità**.

Se la criptovaluta e i [[Resources/Money/Crypto/Notes/Token]] hanno il potenziale per imporre e garantire la proprietà personale del denaro e dei beni intercambiabili**, i [[Resources/Money/Crypto/Notes/Token]] non fungibili possono fare lo stesso per i beni unici.**

### Utilizzo degli NFT

- **Arte**. con gli NFT è possibile per un artista (sia di arte classica ma anche musica, cinema...) creare una opera non falsificabile.
- **Collezionismo**. Data l'unicità dell'NFT, questi possono essere usati per creare dei nuovi oggetti da collezione digitale la cui proprietà è garantita.
- **Gaming**: possono essere creati giochi basati su oggetti unici da collezionare (il più famoso è [AxieInfinity](https://axeinifiitniy.com/?))
- **Beni virtuali**. Ogni bene virtuale unico può essere [[Resources/Money/Crypto/Notes/Token]]izzato. Può essere un dominio (vedi Ethereum Name Service) o può essere delle terre in un videogioco (vedi Decentraland e Cryptovoxels).
- **Beni del mondo reale**. Analogamente ai beni virtuali anche i beni nel mondo reale possono essere [[Resources/Money/Crypto/Notes/Token]]izzati per dimostrare che qualcuno possiede un dato diritto su di un terreno, una casa, una auto e così via.
- **Accesso a club esclusivi**: Come ha insegnato [Bored Ape Yacht Club](https://opensea.io/collection/boredapeyachtclub) gli NFT possono essere utilizzati per poter accedere a dei club esclusivi: solo chi possiede un determinato [[Resources/Money/Crypto/Notes/Token]] può entrare in questi club.

![[ExeEzH3XEAED2BX-1024x611.webp]]

## Come evitare gli NFT di NFT

Cosa mi impedisce di creare un NFT a partire da una immagine scaricata di un altro NFT? Alla fine sono esattamente indistinguibili.

Per certificare l'autenticità di un NFT la [[Blockchain]] viene in aiuto: dato che è possibile vedere tutti i passaggi di proprietà che ha avuto un determinato [[Resources/Money/Crypto/Notes/Token]] è ottenere il wallet originale che lo ha creato dal nulla (mintato). Se questo ultimo è un wallet "certificato" tra quelli ufficiali allora l'NFT è originale, altrimenti no.

Per esempio se il wallet che ha mintato una Bored Ape è uno dei wallet ufficiali dello Bored Ape Yacht Club conseguentemente posso concludere che l'NFT è autentico.

## ERC-721

Analogamente come esiste lo standard [[ERC20]] per sviluppare uno smart contract rappresentante dei [[Resources/Money/Crypto/Notes/Token]] fungibili (vedi [[Resources/Money/Crypto/Notes/Token]] [[ERC20]], [[Stablecoin]], ICO. Un po’ di chiarezza]], esiste anche lo standard per i [[Resources/Money/Crypto/Notes/Token]] non fungibili chiamato ERC-721.

In particolare tutti gli NFT sono dei [[Resources/Money/Crypto/Notes/Token]] (quindi con un valore univoco _contract address_) ma che hanno un ulteriore campo `uint256` chiamato `[[token]]Id`, che è **l'identificativo univoco dell'oggetto non fungibile in questione**. La coppia quindi `address` e `[[token]]Id` è unica a livello globale. Tipicamente da DApp da cui avrai comprato l'NFT avrà un convertitore da `[[token]]Id` all'opera.

E' importante sottolineare che l'oggetto in questione (per esempio l'immagine NFT) non risiede sulla [[Blockchain]] ma su un database esterno. **Quello che effettivamente possiedo è il puntatore univoco a quel record di quel database contenente l'immagine**.

Lo standard ERC-721 impone allo sviluppatore di smart contract di fornire funzionalità per il trasferimento di [[Resources/Money/Crypto/Notes/Token]] da un account a un altro, la richiesta del saldo corrente di [[Resources/Money/Crypto/Notes/Token]] di un account, del proprietario di un [[Resources/Money/Crypto/Notes/Token]] specifico, la quantità totale di [[Resources/Money/Crypto/Notes/Token]] disponibili sulla rete, la possibilità di approvare che una quantità di [[Resources/Money/Crypto/Notes/Token]] di un account possa essere spostata da un account terzo.

Per approfondire tutte le specifiche tecniche consiglio vedi: [https://ethereum.org/it/developers/docs/standards/[[Resources/Money/Crypto/Notes/Token]]s/erc-721/](https://ethereum.org/it/developers/docs/standards/[[token]]s/erc-721/)

Su Etherscan è possibile visualizzare [tutti gli smart contract che rispettano lo standard ERC72](https://etherscan.io/[[token]]s-nft), un esempio è [The Ethereum Name Service (ENS)](https://ens.domains/) che è il corrispettivo de DNS (che permette di trovare un url con un nome leggibile invece di un indirizzo IP) ma per una risorsa all'interno della [[Blockchain]], passando quindi da un hash ad un nome leggibile come `my-amazing-website.eth`.