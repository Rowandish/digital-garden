---
tags:
  - Crypto
  - Coin
  - PublishedPosts
---
Terra è una [[Blockchain]] il cui obiettivo è creare un sistema monetario decentralizzato, quindi con tutto il mondo [[DeFi]] **ma soprattutto con stablecoin decentralizzate algoritmiche**.

Il problema delle stablecoin algoritmiche (non collateralizzate sul dollaro) è che l'unico obiettivo di averle in portafoglio è che ci hanno dei ritorni; un sistema che non serve a nulla tranne autoalimentarsi prima o poi collasserà.

Le [[Stablecoin]] Luna sono stablecoin decentralizzate, non rispondono ad alcun ente centrale e non hanno collaterale fisico ma **mantengono il loro valore costante tramite un meccanismo di burn e mint dei Luna in base alla domanda e all'offerta**.

Le stablecoin Terra invece hanno l'ambizione di essere usate nel mondo reale. Per esempio KRT (che è la stablecoin del Won Koreano) viene già correntemente utilizzata anche fuori del mondo crypto.

## Differenze con le altre chain

A differenza delle altre blockchain innovative come [[Avalanche](https://codicepragmatico.it/crypto/appunti-su-avalanche/), [Polkadot](https://codicepragmatico.it/crypto/appunti-su-polkadot/), [Solana]] il cui obiettivo è risolvere tutti i problemi di Ethereum, Terra di pone come obiettivo lo sviluppo e l'utilizzo delle sue stablecoin.

Per come è strutturata LUNA, **tanto più queste stablecoin prendono piede tanto più la coin Luna aumenterà di valore**.

Le altre coin sono tutte pensate per essere in concorrenza tra di loro: se uso Solana non sto usando Avalanche, se uso Polkadot non sto usando Ethereum e così via. Terra invece offre un modo di pensare la [[DeFi]] completamente nuovo: l'introduzione di UST come stablecoin in più piattaforme possibili.

Maggiore è l'utilizzo di UST da parte del mondo, maggiore sarà il valore di Luna. Inoltre, essendo UST una stablecoin algoritmica, ho una vera finanza decentralizzata, non una finanza decentralizzata che si basa su stablecoin centrali come [[USDT]] o [[USDC]].

## Come ottenere UST

Il metodo principale è andare ad acquistare LUNA in un qualsiasi CEX e poi trasferirli su TerraStation. Su TerraStation andare nella voce swap e ottenere così gli UST. Il procedimento è analogo ad andare su [Terraswap](https://app.terraswap.io/swap?to=uusd&type=swap&from=uluna).

Qualora invece si abbiano dei WUST [[ERC20]] ottenuti, per esempio, su Uniswap posso utilizzare il [[Bridge]] per passare da WUST su Ethereum a UST su Terra.

## TerraStation

Una volta ottenuti dei LUNA li posso o mettere in [[Staking]] o convertirli in stablecoin.

Il wallet di LUNA è [TerraStation](https://station.terra.money/), posso fornire in miei LUNA ad un validatore in modo da delegare lo [[Staking]] e ricevere un incentivo in primis dalle tax reward (che sono le fee degli utilizzatori di Terra in UST) e inoltre ricevere dei token (airdrop) dei nuovi progetti su Terra. Ad oggi il reward è circa il 10%.

Sempre tramite TerraStation posso effettuare lo swap di un LUNA con la relativa stablecoin; anch'essa può essere messa in [[Staking]] e così via.

### Testnet

Analogamente a Ropsten per ETH e MetaMask anche Terra ha la sua testnet. Il suo faucet è [questo](https://faucet.terra.money/) che permette di ricevere 1000 Luna di test su TerraStation.

![[image-43.webp]]

1000 Luna di test sulla testnet

## Anchor Protocol

E' una piattaforma di [[lending]] e anche costante. Ma come fa?

![[image-36-1024x116.webp]]

![[image-35-1024x426.webp]]

Analogamente ad Aave ho vari lender che depositano liquidità e dei borrower che depositano del collaterale per potere avere il prestito in questione. Il collaterale è sottoforma di LUNA (bETH) o ETH (bETH).

**Il trucco è avere solo collaterali PoS e questi ultimi vengono automaticamente messi in [[Staking]] dalla piattaforma, ottenendo così un APY**. Dato che ci vuole un collaterale minimo di 2x anche se mediamente ne vengono depositati il triplo e che mediamente ho un [[APY]] dallo [[Staking]] del 10%, la piattaforma ha un notevole guadagno dalla liquidità depositata.

Per esempio per 10 UST presi a prestito ci sono circa 30$ di LUNA in [[Staking]] che avranno un APY del 10%. Quindi 3x10% forniscono un APY del 30%; a questo va aggiunto l'[[APR]] del borrow (pagato da chi prende in prestito) del 16%.

Anchor quindi può permettersi di offrire un 20% costante di APY ai lender senza problemi. L'eccedenza viene utilizzata per acquistare il [[Token]] della piattaforma ANC in modo da aumentarne il valore.

In futuro sarà possibile mettere in [[Staking]] su Anchor anche [[Polkadot](https://codicepragmatico.it/crypto/appunti-su-polkadot/), [AVAX](https://codicepragmatico.it/crypto/appunti-su-avalanche/), [Solana]] o, in generale, tutte le coin che possono essere messe in [[Staking]] per lo stesso motivo.

### Earn

![[image-37-1024x321.webp]]

Interfaccia della sezione Earn di Anchor

La sezione Earn permette di aggiungere liquidità in UST al protocollo in modo da ottenere il famoso APY del 20%. L'interfaccia è estremamente semplice e questi numeri sono difficili da trovare nel mondo [[DeFi]].

Posso anche assicurare il capitare depositato contro hack o furti con delle assicurazioni automatiche come Nexus Mutual.

### Borrow

![[image-38-1024x356.webp]]

Interfaccia per ottenere UST in prestito

Borrow permette di prendere in prestito UST depositando collaterale in bLUNA o bETH. Vi è un interesse da fornire dell'11.74% che però viene parzialmente compensato dal distribution APR del 9.65%.

Il distribution APR è un premio che viene fornito in token ANC a chi utilizza la piattaforma.

La somma dei due porta ad un tasso di interesse netto per il prestito del 2.08%, un ottimo tasso.

L'idea del Borrow è **rimanere esposti a Luna** (quindi da fare se si è bullish sulla coin) **e avere allo stesso tempo una rendita in UST** (gli UST presi in prestito verranno poi messi a rendita su Earn o su Mirror, per esempio).

## Mirror Protocol

Questa è una piattaforma di asset sintetici su Terra. Asset sintetici possono essere azioni o ETF, sono di fatto degli asset tokenizzati.

Lo scopo di acquistare questi token invece delle azioni normali possono essere molteplici: il primo che non è detto che nel paese dove risiedo abbia accesso a tali azioni e il secondo, e più importante, è che **questi asset possono essere usati come collaterale**.

Dato che di fatto sono dei token per la [[DeFi]] hanno lo stesso comportamento di tutti gli altri, quindi possono essere collateralizzati e utilizzabili anche su altre piattaforme.

### Borrow

La sezione borrow permette di prendere in prestito delle azioni tokenizzate collateralizzando UST e altri token. Prendere in prestito una azione ha lo scopo di shortarla, quindi sperare che scenda di valore.

Assumiamo che l'azione Apple valga 100\$. Io deposito come collaterale 200\$ per ottenere questa azione che vado a vendere subito per 100\$. La mia speranza è che Apple scenda, assumiamo che ora valga 70\$. Io la riacquisterò a 70\$ (guadagnandoci 30\$ quindi) e ripagherò il mio debito.

Di fatto è una sezione inutile dato che lo stesso comportamento automatizzato con premio lo ho nello short farm (vedi sotto).

### Farm

Ci sono due tipologie di Farm, il farm long e il farm short.

Queste strategie sono spiegate in maniera molto completa qui: [http://www.mirrortracker.info/](http://www.mirrortracker.info/)

![[image-39-1024x95.webp]]

Ricompensa del 23.18% in token MIR per il long farm e del 5.24% per lo short farm

#### Long Farm

Questa modalità funziona come i [[pool di liquidità]].

Essendo un pool sono esposto anche all'[[Impermanent loss]] nella variazione tra il valore del token e UST.

#### Short Farm

![[image-40-1024x95.webp]]

Esempio di premium elevato, viene incentivato a farmare short con APY elevati.

Il prezzo dell'Exchange non è il prezzo reale (fornito dall'oracolo), vi è una differenza indicata nella colonna Premium. Questa differenza può essere positiva o negativa.

Se la differenza è positiva e alta significa che il prezzo di Mirror è maggiore del prezzo reale, si incentiva quindi a farmare short fornendo un APY elevato.

![[image-42.webp]]

Per farmare short Mirror presenta una interfaccia che fa automaticamente quanto descritto sopra.

Prendiamo l'esempio di PayPal, il suo costo è 163.60\$. Io prendo in prestito una sua azione fornendo il doppio del collaterale, quindi 327.2\$.

La piattaforma non mi fornirà una azione PayPal ma questa verrà automaticamente venduta su Terraswap per 163.60 UST, questi UST mi verranno forniti dopo 2 settimane.

Per riottenere i 327.2$ di collaterale dovrò fornire una azione PayPal che dovrò riacquistare successivamente sperando che il prezzo sia sceso (short).

In questo periodo di tempo riceverò come ricompensa il 19.88% di APY.

#### Guadagnare con il farming long e short contemporaneo

Per andare a ottenere la ricompensa senza rischiare posso andare sia short che long contemporaneamente (delta neutral) in modo da avere una strategia win-win indipendentemente dal valore del sottostante.

Per ottenere questo comportamento devo **acquistare una azione (nella sezione Trade non Farm) e poi shortarla con lo Short Farm. In questo modo ottengo le commissioni dello short farm senza rischi.**

Tornando all'esempio precedente posso quindi acquistare una azione PayPal a 172.88$ e inoltre shortare sempre PayPal collateralizzando il doppio di 172.88$ in modo da avere lo short farming.

Avendo già una azione PayPal di fatto posso chiudere il borrow short quando voglio, indipendentemente dal valore di PayPal che può salire o scendere. **E nel mentre che la posizione di borrow rimane aperta guadagno le fee dello short farm**.

Non conviene fare sia short farm che long farm in quanto il long farm ha impermanent loss, per cui non sono più delta neutral.

**Inoltre gli UST che mi vengono sbloccati dopo 2 settimane di short farm possono metterli a rendita su Anchor con APY del 20%.** Questi APY mi vengono forniti in aUST che possono essere usati come collaterale su Mirror.

La ricompensa di short farming avviene viene fornita con il token MIR che a sua volta posso mettere in [[Staking]].
