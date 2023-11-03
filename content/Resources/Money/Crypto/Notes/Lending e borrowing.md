---
tags:
  - Crypto
  - DeFi
---


Per prima cosa è necessario capire il concetto di Money Market (MM): questa è una piattaforma di prestito in cui da un lato abbiamo una persona che presta della liquidità (**lender**) e un relativo opposto che riceve tale liquidità chiedendo un prestito (**borrower**). Il lender, fornendo liquidità, si chiama in gergo **liquidity provider**.

Il lender riceve l'interesse pagato dal borrower con la piattaforma che ne trattiene una parte.

La piattaforma utilizza questa differenza per gestire se stessa e inoltre come incentivo di **liquidity mining**: questa viene regalata agli utenti sotto forma dei [[Resources/Money/Crypto/Notes/Token]] della piattaforma stessa al fine di incentivare gli utenti ad utilizzare la piattaforma stessa (farming).

In questo modo gli utenti sono contenti in quanto vengono pagati per usare la piattaforma (sia il lender che il borrower ricevono l'incentivo di liquidity mining) e questa ultima è contenta allo stesso modo in quanto riceve liquidità dagli utenti che la utilizzano facendo guadagnare alla piattaforma le commissioni.

## Collaterale

Nei prestiti nel mondo reale bisogna fornire dei collaterali fisici (come ipoteche) in modo che, qualora non sia possibile saldare il prestito, il collaterale risulti perso. Nella [[DeFi]] ho dei problemi ancora maggiori: dato che ho l'anonimato non posso sapere a chi sto prestando i soldi, il suo score finanziario o la sua busta paga.

L'unico modo per avere la **garanzia che il prestito venga restituito è necessario che sia versato un collaterale in criptovalute**, per esempio BTC.

Di solito si versa un collaterale molto maggiore del prestito richiesto, per esempio **il Loan To Value (LTV) del collaterale versato, quindi la percentuale del valore del prestito rispetto al collaterale, deve essere minore di una determinata percentuale, per esempio 50%**. Questo in modo tale che il mio prestito sia sempre coperto dal collaterale anche in caso di oscillazioni negative del prezzo dello stesso.

Per esempio per chiedere in prestito 500€ [[USDT]] dovrò versare il corrispettivo di 1000€ in BTC. Se BTC perde fino al 50% del suo valore io comunque ho il prestito coperto.

N.b. **Ad oggi gli smart contract hanno bisogno di un collaterale già immobilizzato per poter funzionare**. Uno smart contract che dice "se succede X allora Y deve pagare Z ETH" impone che gli Z ETH siano "immobilizzati" indipendentemente che il fatto X accada o meno. Questo perché, essendo un algoritmo, non ha potere di "imporre un pagamento" ma può solo trasferire dei soldi che ha già a disposizione dal conto X al conto Y.

## Calcolo del tasso di interesse

Il tasso di interesse viene **calcolato dinamicamente e algoritmicamente dal Money Market** in base al rapporto domanda/offerta: maggiore è la domanda per un certo asset più il tasso di interesse aumenterà; al contrario minore è la domanda con tanta offerta il tasso di interesse diminuirà.

Inoltre il MM deve fare in modo di **avere sempre della liquidità disponibile sulla piattaforma**: qualora un lender volesse prelevare la sua liquidità deve poterlo fare in qualsiasi momento. In questo caso non sto prelevando la liquidità effettivamente prestata al borrower ma sto prelevando della liquidità libera presente sulla piattaforma.

Per evitare che tutta la liquidità della piattaforma venga prestata e non ve ne sia più di libera **il tasso di interesse cresce vertiginosamente se i livelli di liquidità prestata per un certo asset superano una percentuale fissata, per esempio l'85%**.

Per esempio se io voglio prendere in prestito [[USDC]] ma la piattaforma ne ha già prestati il 90%, riceverò un tasso di interesse così alto da indurmi a non chiedere in prestito tale [[Resources/Money/Crypto/Notes/Token]]. Al contrario invece il lender sarà incentivato a depositarlo, aumentando così la liquidità e diminuendo il tasso di interesse.

## Liquidazione

Le piattaforme MM non possono permettersi di avere prestiti non coperti da collaterale: qualora fosse così la piattaforma diventa a debito. Se succede per vari borrower questa perdita si percuote sui lender e la piattaforma diventa così insolvente e, di fatto, fallendo.

Vi è quindi un sistema di [[Liquidazione del collaterale (margin call)]].

## Perché prendere in prestito?

Mentre nel mondo reale è facile capire i motivi per cui si ha spesso la necessità di un prestito, per esempio per l'acquisto di un bene di cui non si dispone di tutta la liquidità.

Ma nel mondo della [[DeFi]] perché una persona dovrebbe prendere in prestito delle criptovalute depositando inoltre un collaterale molto più alto di quanto richiedo?

Vi sono due possibili motivi.

### Doppia esposizione

Il primo è volere della liquidità rimanendo comunque esposto alla criptovaluta che voglio collateralizzare: questa ultima infatti rimane comunque mia ma nel mentre ho delle nuove [[Stablecoin]] che posso farmare ottenendo degli ottimi [[APY]] (le [[Stablecoin]] tipicamente forniscono delle [[APY]] interessanti).

Esempio: metto in [[Staking]] SOL e ottengo l'interesse dello [[Staking]] mSOL. mSOL lo utilizzo come collaterale per prendere in prestito delle [[Stablecoin]] come [[USDC]]. Sposto gli [[USDC]] su Terra e vado a fare farming su [Anchor](https://www.anchorprotocol.com/). In questo modo sono esposto solo a SOL e sto facendo sia [[Staking]] su SOL che farming su [[USDC]].

### Leva

Con il borrow posso avere una **esposizione in leva**. Per esempio per avere una esposizione a leva 2x su BTC collateralizzo questo ultimo per ottenere una [[Stablecoin]] e con queste compro altri BTC.

In questo modo ho un profitto (o una perdita) in leva, in quanto la [[Stablecoin]] ha un valore per definizione costante e quindi la mia doppia esposizione a BTC (i BTC miei e i BTC in prestito) mi portano ad avere un raddoppio dei guadagni o perdite.

## Aave

La piattaforma più famosa è [AAve](https://aave.com/), ora è presente su 3 chain: Ethereum, Polygon e Avalanche.

![](images/image-22-1024x140.png)

Header di AAve indicante le varie chain su cui può operare

Per prendere un prestito (esempio [[USDC]]) la prima cosa che devo fare è depositare del collaterale, per esempio AVAX.

![](images/image-24-1024x54.png)

Informazioni sul [[Resources/Money/Crypto/Notes/Token]] Avalanche e sul suo rendimento. Notare l'1.61% sul deposito e il 7.11% con liquidity mining in [[Resources/Money/Crypto/Notes/Token]] WAVAX.

Cliccando su Avalanche (quindi la moneta che voglio collateralizzare) si apre una schermata con tutte le informazioni

![](images/image-23-1024x508.png)

- **Utilization rate**: differenze percentuali tra la liquidità disponibile e quella prestata. In questo caso siamo poco oltre il 30% che è buono, ho un ridotto rischio di liquidità;
- **Deposit [[APR]]**: incentivo della piattaforma al deposito del collaterale (indipendentemente se poi prenderò un prestito o meno). In questo caso è l'1.61%. A questo andrà sommato il premio in liquidity mining.
- **Variable [[APR]]**: tasso di interesse per chi prende in prestito il [[Resources/Money/Crypto/Notes/Token]]. Come indicato sopra qualora il tasso di utilizzo superi una determinata soglia maggiore è questo tasso.
- **Maximum LTV** **50%**: posso prendere un prestito delle coin il cui valore è massimo la metà del valore degli Avalanche collateralizzati;
- **Liquidation threshold 65%**: Limite massimo di differenza tra il valore del collaterale e il valore del prestito prima che questo venga liquidato automaticamente. Assumendo di collateralizzare AVAX per [[Stablecoin]] con LTV 50% significa che se AVAX perde il 15% del suo valore vado in liquidazione;
- **Liquidation penalty 10%**: fee che mi viene addebitata qualora vada in liquidazione;
- **Used ad collateral**: flag booleano che indica se posso usare tale [[Resources/Money/Crypto/Notes/Token]] come collaterale;
- **Stable borrowing**: flag che indica se è disponibile un prestito a tasso fisso per il [[Resources/Money/Crypto/Notes/Token]].

## Alternative ad Aave

Nel mercato sono presenti numerose alternative ad Aave, cito [Geist Finance](https://geist.finance/) su Fantom, [Solend](https://solend.fi/) su Solana, [Tectonic](https://tectonic.finance/) cross-chain, [Anchor](https://www.anchorprotocol.com/) su Terra, [BenQi](https://benqi.fi/) su Avalanche.
