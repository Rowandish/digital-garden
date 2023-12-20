---
tags:
  - Crypto
  - Coin
  - PublishedPosts
---


Il [Wrapped Bitcoin](https://wbtc.network/) (WBTC) è un [[Token]] [[ERC20]] emesso con uno [[Smart contract]] dedicato che consente di variarne la supply in modo che il suo valore sia costante a 1 [[Bitcoin]]. In particolare ogni volta che viene immobilizzato un bitcoin (BTC) viene emesso 1 token Wrapped Bitcoin (WBTC). Di fatto è quindi una [[Stablecoin]] collateralizzata 1:1 con BTC, analogamente come [[USDT]] è collateralizzata 1:1 con USD.

E' un po' come fosse una opzione put che fornisce fornisce in qualunque momento diritto al detentore di ottenere un BTC al prezzo di mercato dello stesso.

## Parchè creare questo token?

Il token è stato creato in quanto i BTC si possono solo utilizzare sulla loro blockchain nativa, che però, non supportando smart contract, non rendono possibile lo sviluppo di DApp.

Essendo il Wrapped Bitcoin WBTC **un token ERC20 con lo stesso valore di BTC posso utilizzarlo sulle reti Ethereum o Ethereum compatibili,** quindi su piattaforme come Curve o Uniswap. In questo modo posso operare sulla blockchain Ethereum ma espormi sul BTC. Posso quindi fare farming, lending, trading e così via utilizzando BTC.

## [[Collateralizzazione]]

La parte più delicata di questo processo è la certezza che il sottostante esista: se un giorno tutti i possessori di WBTC volessero riconvertirli in BTC, vi saranno per tutti?

La società società di intermediazione che gestisce questo processo è BitGo, il suo compito è quello di bloccare i BTC che vogliono essere wrappati e garantirne la custodia.

La sicurezza è ovviamente legata a doppio filo alla credibilità che ha in questo caso l’intermediario. L'idea è che i BTC custoditi sono sempre pubblicamente controllabili, al fine di garantire che per ogni WBTC in circolazione ci sia un Bitcoin reale a fare da sottostante; possiamo quindi avere la certezza che il sottostante esista e che non si utilizzi alcun sistema di riserva frazionaria, a differenza di alcune stablecoin.

## Come funziona il processo di wrapping?

Un esercente (*merchant*) manda una quantità in BTC al custode (*custodian*) per il processo di coniazione del token wrappato. Il custode quindi crea WBTC su Ethereum in base all'importo BTC inviato. Quando WBTC deve essere scambiato nuovamente per BTC, il commerciante invia una richiesta di burn al custode e il valore BTC viene svincolato dalle riserve.

## Token BTC analoghi

WBTC non è l'unico token collateralizzato BTC, per esempio Uniswap utilizza anche i *renBTC (RENBTC),* *Aave* utilizza gli *AWBTC*, *Curve* utilizza entrambi questi ultimi oltre anche a *sBTC*, *Balancer* utilizza anche i *BTC++* di *PieDAO*, mentre *Compound* utilizza i suoi *CWBTC*.
Ogni [[Blockchain]] che vuole operare con i BTC deve avere i suoi token wrapped che lo rappresentano.

## I Wrapped token

Non esiste la versione wrapped solo di BTC ma anche di tante altre valute, questo allo scopo di poter essere usate su delle blockchain diverse da quelle in cui sono state create. Per esempio potrei wrappare ETH per poter essere usato sulla Binance Smart Chain, o in generale [rendere ETH ERC20 compatibile](https://academy.binance.com/en/glossary/wrapped-ether) (ETH è stato creato prima di [[ERC20]] per cui questo ultimo non è compatibile con le DApp create sulla sua stessa rete).

Di fatto un wrapped token è la versione tokenizzata di una generica coin collateralizzata 1:1 con la coin in questione.

### I bridge

I [[Bridge]] sono le piattaforme che consentono di convertire delle crypto nella loro versione wrapped per una determinata blockchain.
Per esempio [Binance Bridge](https://www.binance.org/en/bridge) permette di wrappare delle crypto per usarli su Binance Smart Chain sotto forma di token BEP-20. Esistono vari altri bridge come [celercBridge](https://cbridge.celer.network/#/transfer) o [AnySwap](https://bsc.anyswap.exchange/bridge#/router).


