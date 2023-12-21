---
tags:
  - Crypto
  - Definition
  - PublishedPosts
---
Un DEX (Decentralized Exchange) è un exchange decentralizzato che permette lo scambio di coin senza un intermediario.

Ho due tipologie di DEX, l'**Automatic Market Maker (AMM)** che funziona con i pool di liquidità (la maggioranza dei DEX funziona così) oppure i più moderni **Order Book based** che hanno le stesse caratteristiche fornite da un CEX, quindi limit order, stop loss e così via.

## DEX AMM

I DEX AMM si basano su dei liquidity provider che forniscono liquidità e dei **trader, che vogliono scambiare monete**: per esempio voglio scambiare ETH con [[USDT]] o viceversa.

Per scambiare ETH con [[USDT]] ho bisogno che **qualcuno abbia fornito sia ETH (qualora li voglia fornendo [[USDT]]) che [[USDT]] (qualora voglia quelli fornendo ETH) in rapporto 50 e 50 in base al loro prezzo**.
Il rapporto dei due token all'interno del pool è proporzionale al prezzo dell'uno rispetto all'altro: quindi se ETH vale 4000€, per aggiungere 1ETH al pool dovrò aggiungere anche 4000€ in [[USDT]].

Queste coppie di monete sono fornite a quello che viene definito **pool di liquidità**. Utilizzandoli anche in combinazione uno con l'altro il trader può scambiare qualsiasi moneta in qualsiasi altra moneta (sulle stessa chain).

Il **liquidity provider riceve parte delle commissioni** che vengono fornite dai trader per lo scambio di monete. In verità questo non è del tutto vero: le fee vanno prima all'interno del pool in modo da farlo crescere in liquidità; una volta che io vado a ritirare non ho solo i token che ho fornito al pool ma anche le fee che mi spettano.

Analogamente alle piattaforme di lending, i DEX, per attrarre liquidità, possono fornire degli **incentivi ai liquidity provider sotto forma dei token della piattaforma stessa (incentivo di liquidity mining)**.

### [[Token LP]]

### [[Impermanent loss]]

### [[Slippage]]

### Routing

Il routing è una operazione automatica che viene fatta dal DEX qualora io voglia scambiare due token di cui non esiste alcun pool, ma ne esistono utilizzando token intermedi.

Per esempio per scambiare il token A con C posso utilizzare il pool A-B concatenato con B-C.

Quando ho un routing posso avere più commissioni e più rischio di slippage se uno dei due pool è poco liquido.

### Pancakeswap

[PancakeSwap](https://pancakeswap.finance/) è il più famoso DEX su Ethereum.

![[image-19-1024x481.webp]]

Interfaccia per il trader. In questo caso voglio scambiare (su BSC) BNB con ETH

![[image-20.webp]]

Interfaccia per il Liquidity Provider: in questo caso il pool è quello tra BNB e CAKE, in proporzione 50/50. Una volta completato riceverò i token LP.

![[image-21-1024x474.webp]]

I token LP possono essere messi in stake nella sezione farming per ottenere [[APR]] molto interessanti

### Altri DEX famosi

[VVS Finance](https://vvs.finance/) è un DEX su Cronos, [Terraswap](https://terraswap.io/) per l'ecosistema Terra, [Quickswap](https://quickswap.exchange/) e [SushiSwap](https://sushi.com/) su Polygon, [UniSwap](https://uniswap.org/) su BSC, [Curve](https://curve.fi/) multichain,

## DEX basati su Order Book

In questi DEX vi sono due ruoli fondamentali: **il market maker e il market taker**.

**Il market maker (equivalgono ai liquidity provider) sono coloro che forniscono la liquidità all'order book**. Questo ultimo deciderà il prezzo di mercato a cui verranno scambiate le monete richieste dal market taker. Il market maker riceverà una percentuale sulla fee ed eventuali token della piattaforma.

**Il market taker è invece colui che compra o vende a mercato utilizzando la liquidità sull'order book**. Paga una fee e riceverà eventualmente delle ricompense in token dalla piattaforma.

Gli [[Order book]] based devono utilizzare una chain molto veloce, infatti sono stati introdotti con l'avvento di [[Solana]].
