---
tags:
  - Crypto
  - DeFi
---


Anchor protocol è uno dei migliori progetti di [[DeFi]] in circolazione che permette di avere [[APY]] su [[Stablecoin]] del 20% annuo (!!).

Nel mio articolo precedente ho introdotto un po' di funzionalità della [[Blockchain]] Terra; in questo articolo analizzo nel dettaglio con screenshot ed esempi come utilizzare Anchor.

In tutti i seguenti esempi ho utilizzato la testnet di Terra. Ricordo che dal wallet TerraStation è possibile passare facilmente alla testnet e che è possibile ricevere i LUNA dal [faucet ufficiale](https://faucet.terra.money/) e swapparli in UST su [TerraSwap](https://app.terraswap.io/).

## Come ottenere i bLUNA

Per poter prendere in prestito UST Anchor richiede come collaterale dei bondedLUNA (bLUNA).

Per ottenerli è necessario andare nella sezione bASSET per mintare i bLUNA burnando i propri LUNA (pagando delle fee in UST, ricorda di averne sempre un po' sul wallet).

![[image-44.webp]]

Conversione di 500 Luna in circa 500 bLuna

Una volta effettuata la conversione otterrete una situazione analoga alla seguente

![[image-45.webp]]

Nel proprio wallet abbiamo Luna, UST e anche bLuna.

## Borrow

Una volta ottenuti i bLUNA è possibile collateralizzarli nella sezione borrow.

Cliccando su Provide nei bLUNA ottengo una schermata analoga alla seguente

![[image-46.webp]]

Questa schermata significa che, una volta collateralizzati i bLUNA, posso prendere in prestito massimo 15359€ (60% LTV).

Ricordo che finora non ho ancora preso in prestito nulla, ho solo fornito collaterale alla piattaforma.

![[image-47.webp]]
Interfaccia indicante quanti UST ho preso in prestito sul totale possibile. Consiglia un 45% di LTVe e un massimo di 60%. Superato quel valore si sarà liquidati.

Ora andiamo a prendere in prestito premendo il tasto Borrow, per esempio 10000$ che è circa il 39% dell'LTV.

![[image-48.webp]]

Una volta confermata la transazione mi verranno trasferiti sul mio wallet gli UST, come si vede dall'immagine seguente.

![[image-49-1024x429.webp]]

Nella testnet (purtroppo non più nella mainnet) la piattaforma fornisce un [[APR]] positivo per prendere in prestito: un 7.57% di interessi di prestito vengono compensati da un 76.66% di [[APR]] nel token ANC. Ho così un [[APR]] positivo.

## Earn

Una volta ottenuti degli UST (che sia tramite borrow o acquistati) è possibile metterli a rendita con [[APY]] altissime, in particolare circa il 20% costante.

E' molto semplice, una volta cliccato su Deposit si aprirà una modale analoga alla seguente dove è possibile depositare una determinata quantità di UST, nel mio caso 5000.

![[image-50.webp]]

Una volta depositati avrò una interfaccia dove è indicato il riepilogo e anche quanto guadagnerò potenzialmente, in un anno, mese e giorno.

![[image-51-1024x516.webp]]

### aUST

In cambio degli UST depositati Anchor fornisce dei token aUST, che sono dei token indicanti la liquidità messa in Earn su Anchor. Fornendo alla piattaforma gli aUST riotterrò quanto depositato.

**I token aUST sono definibili come _interest bearing token_, ovvero che maturano interessi col tempo solo detenendoli**. Ad oggi valgono circa 1.18 UST **ma il suo prezzo rispetto agli UST divergerà sempre di più**, in particolare divergerà, ad oggi, del 19% l'anno (che è l'[[APY]] di Anchor Earn).

In questo modo **si ottengono gli interessi solo holdando tali token del wallet, indipendentemente che siano su Earn o su altre piattaforme**; in particolare essendo un vero e proprio asset, gli aUST possono essere usati come collaterale su Mirror protocol per aprire posizioni short.

## Come ottenere le ricompense

Le ricompense di Earn sono automatiche: quando si andrà a prelevare quanto depositato verrà fornito un numero di UST maggiore rispetto a quello depositato.

Le ricompense per la [[Collateralizzazione]] invece vengono fornite in token ANC e devono essere ottenute manualmente mediante il pulsante "Claim all Rewards" nella sezione "My Page".

![[image-52-1024x391.webp]]

## [[Staking]] dei token ANC

Per mettere in [[Staking]] i token ANC è necessario andare su **Governance** e cliccare su _Gov stake_. Ad oggi l'[[APR]] è circa il 27%.

![[image-53.webp]]

Su _Unstake_ è possibile ottenere gli ANC in [[Staking]].

## Pool UST/ANC

E' possibile mettere nel pool UST/ANC in modo da guadagnare le fee di swapping da uno all'altro (come funziona nei classici [[DEX]].

Per farlo su Governance cliccare su ANC-UST LP e inserire lo stesso ammontare, in valore, di ANC e UST.

![[image-54.webp]]

Vengono mintati i rispettivi token ANC-UST LP che dovranno essere utilizzati per riottenere gli UST e ANC depositati.

Nota bene: i [[Token LP]] forniti **devono essere messi in [[Staking]] per ottenere le reward del liquidity provider.**

Per mettere in [[Staking]] i token LP nella stessa interfaccia di prima clicchiamo su "Stake" invece che su "Pool", otteniamo una interfaccia analoga alla seguente

![[image-55 1.webp]]

In cui possiamo mettere in stake i token LP ricevuti e ottenere i reward.
