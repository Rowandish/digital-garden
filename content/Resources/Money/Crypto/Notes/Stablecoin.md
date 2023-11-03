---
tags:
  - Crypto
  - Definition
  - PublishedPosts
---
Le stablecoin sono dei **token il cui prezzo è stabile in quanto vincolato ad un mezzo di scambio stabile, come una valuta fiat (dollaro, euro) o una commodity (come l'oro)**. Il loro prezzo quindi non è variabile come potrebbe essere quello di una criptovaluta ma è associato uno ad uno alla moneta in questione.
Nella politica monetaria, questo è noto come **tasso di cambio fisso**. In questo modo si possono avere i vantaggi delle criptovalute come decentralizzazione, sicurezza e velocità senza avere le oscillazioni prezzo che impediscono, di fatto, che possano essere un valido sostituto al denaro reale.

Dato che 1 token vale 1$, ad ogni token emesso sul mercato dovrebbe essere associato ad un dollaro "bloccato" in cassaforte. Quando il richiedente del token vuole il suo dollaro il token diventerà inutilizzabile e in cambio verrà restituito il dollaro in questione. Tecnicamente parlando questo significa che la moneta è supportata 1:1 da attività reali come il dollaro americano, l’oro o il petrolio che devono essere archiviati in ambienti centralizzati fidati come un conto bancario. Gli utenti di un sistema come questo devono fidarsi della terza parte che lo garantisce.

Le stablecoin sono state create per risolvere il problema della variazione continua nel prezzo delle criptovalute che impedisce il loro utilizzo sia quotidiano, sia su derivati o accordi a lungo termine.
La stabilità delle stablecoin permette, per esempio, di fornire prestiti in criptovalute, attraverso la [[DeFi]], e guadagnare dai loro interessi senza correre il rischio di incappare in grosse svalutazioni.

Il progetto più noto di stablecoin è Tether, basato sul dollaro americano. Ci sono attualmente 2,6 miliardi di dollari in gettoni Tether in circolazione, senza audit fidati sulle corrispondenti garanzie.

## Cosa vuol dire [[Collateralizzazione]]?

### stablecoin collateralizzate fiat e commodities

Gran parte delle stable coin adottano un ancoraggio off-chain, ossia al di fuori del sistema della [[Blockchain]] utilizzando beni garantiti da autorità terze, solitamente istituzioni finanziarie di tipo tradizionale.

L’emissione di _stablecoin off-chain_ prevede i seguenti passaggi:

- Raccolta di capitale nella valuta o commodity in questione
- Deposito del capitale certificato da una autorità terza
- Emissione dei token](https://codicepragmatico.it/crypto/token-[[ERC20]]-stablecoin-ico-un-po-di-chiarezza/) corrispondenti tramite [smart contract]]

### Stablecoin collateralizzate in crypto

Le stablecoin con asset crypto bypassano la tradizionale infrastruttura e utilizzano altre risorse crittografiche come garanzia di stabilità di valore.

Questo metodo di funzionamento **elimina l’ingerenza di un’autorità centrale**, ma richiede un surplus di valute crittografiche al fine di fare fronte alla volatilità del prezzo.

Il rapporto di garanzia in questo caso è 1:1,5 se non addirittura maggiore. 

### Stablecoin non collateralizzate

In questo caso vi è un algoritmo che funge da banca centrale e che, tramite gli Smart Contract, gestisce domanda e offerta: **se il prezzo sale, si conia un numero maggiore di token**; **se il prezzo scende, parte dei token in circolazione vengono riacquistati e bruciati**.

## Stable Coin USD collateralizzate fiat

### [[USDT]]

### [[USDC]]

### Paxos (USDP)

Paxos è una stablecoin lanciata dall'[omonima azienda](https://paxos.com/usdp/). Questa stablecoin non fa riserva frazionaria, si appoggia ad una liquidità completamente presente in conti correnti, inoltre è certificata e segue tutte le leggi americane come [[USDC]]. Per questo motivo è molto utilizzata sopratutto nelle piattaforme di [[CeFi]].

Il limite principale è la difficoltà di trovarla negli Exchange, tranne quelli più famosi.

### Binance USD (BUSD)

BUSD è una stablecoin erogata sempre da Paxos ma in collaborazione con Binance. E' molto simile a Paxos ma molto legata all'ecosistema Binance. Ne esiste una versione token BEP2 in modo che sia compatibile con la Binance Chain.

Fuori da Binance per ora è poco utilizzata.

### TrueUSD (TUSD)

Emessa dalla società [TrustToken](https://www.trusttoken.com/) il cui scopo è, come dice il nome, fornire la massima trasparenza e fiducia: non vi è riserva frazionaria, il collaterale è completamente liquido e non conservato dalla società stessa ma da degli _conti bancari escrow_ che sono dei depositi di terze parti a cui Trusttoken non ha accesso diretto.

Il detentore del token ha inoltre tutela legale dei fondi che possiede.

Il suo problema è principalmente la centralizzazione, analogamente a [[USDT]], [[USDC]] e BUSD.

## Stable Coin USD collateralizzate crypto

Queste stablecoin non hanno una azienda centrale emettitrice ma sono gestite dalla [[Blockchain]] mediante [[Smart contract]] collateralizzando cripto.
Questo avviene tramite una leva di interessi che bilanciano di domanda e offerta per portare il valore del token tendente a 1$. La collateralizzazione è _on-chain_ con altre crypto

Queste stablecoin hanno il vantaggio della decentralizzazione, quindi non sono censurabili, non legate ad un asset fisico svalutabile, non legate ad una azienda privata e così via. Non c'è quindi alcun audit né controllo. Queste caratteristiche le rendono molto utilizzate sulla [[DeFi]].

A differenza dei token collateralizzati USD, il sottostante è molto più rischioso poiché si aggiungono ai rischi delle coin sopra indicati anche il rischio di svalutazione del sottostante. Inoltre non c'è alcuna legge a tutela dell'investitore.

### Dai (DAI)

DAI (anno di lancio 2017) è al prima stablecoin _crypto-backed_.

E' un token [[ERC20]] ed è la stablecoin più utilizzata.

### sUSD (SUSD)

E' la coin della piattaforma [Synthetix](https://synthetix.io/) che è una piattaforma che, come dice il nome, ha lo scopo di creare asset sintetici: è possibile fare trading di asset tradizionali collateralizzati crypto.

### mStable (MUSD)

E' la coin di [MStable](https://mstable.org/) che la crea collateralizzandola con altre stablecoin.

### Reserve (RSV)
E' la coin di [Reserve](https://reserve.org/).

Collateralizzata con altre stablecoin (1/3 [[USDC]], 1/3 TUSD e 1/3 PAX) ma con una differenza rispetto a MUSD: l'obiettivo è diventare sempre più decentralizzata svincolandosi sempre più al valore del dollaro in modo da avere come unica costante il suo potere d'acquisto. L'obettivo è quindi ottenere una moneta immune all'inflazione o alla deflazione, il cui potere di acquisto rimane sempre costante nel tempo. Come dice il loro slogan "_Stable currency, an human right"._