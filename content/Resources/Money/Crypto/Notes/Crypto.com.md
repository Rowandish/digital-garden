---
tags:
  - Crypto
  - Coin
  - PublishedPosts
---


Crypto.com è una piattaforma di gestione di criptovalute fondata nel 2016 formata da un'[app](https://play.google.com/store/apps/details?id=co.mona.android&hl=it&gl=US), un [exchange](https://shortener.punto-informatico.it/vd783xnecf) e eventualmente un [wallet non custodial per la [[DeFi]]](http://crypto.com/eea/defi-wallet).

Può essere quindi definito un ecosistema, in quanto fornisce tutti gli strumenti per poter operare in questo mondo.

Essendo un mondo estremamente vasto non è possibile trattare tutto con precisione, per ora indico solo una panoramica generale di tutti i prodotti Crypto.com in modo che possiate poi approfondire le parti che più vi interessano.

## Crypto.com Chain

Crypto.com ha una propria [[Blockchain]], la Crypto.com Chain, una [[Blockchain]] che offre **alta scalabilità e velocità nei pagamenti**. Infatti è stata progettata per poter essere **usata, potenzialmente, per i pagamenti di tutti i giorni**. Il tempo di conferma di una transazione è infatti meno di un secondo e con il supporto di circa 50000 transazioni per secondo.

Questa [[Blockchain]] è inoltre estremamente sicura in quanto utilizza vari sistemi di sicurezza come il [trusted execution environments](https://en.wikipedia.org/wiki/Trusted_execution_environment) (TEEs) il cui obiettivo è aumentare la protezione dei dati appartenenti ai partecipanti dell'ecosistema.

Per avere una panoramica della chain è disponibile il suo Explorer: [https://crypto.org/explorer/](https://crypto.org/explorer/)

La Crypto.com chain ha definito i ruoli dei vari attori che vi partecipano, in particolare vi sono:

- `Customers`
- `Merchants`
- `Crypto Customer Acquirers`
- `Merchant Acquirers`
- `Council nodes`

![[e2a0f1a195-1024x550.webp]]

### Customers

Lo scopo dei Customers è quello di utilizzare la rete per effettuare pagamenti in criptovalute. Il customer sarà incentivato per il reward in cashback offerto dalla rete sulle proprie spese.

### Merchants

Lo scopo dei Merchants è quello di accettare i pagamenti i crypto dei Customes per i prodotti o servizi che essi forniscono. In cambio ricevono 0% di commissioni e la possibilità di fornire al cliente gli sconti forniti dalla rete.

La Crypto.com Chain fa quindi da bridge tra il cliente e il fornitore, gestendo il pagamento dall'autorizzazione iniziale all'accredito finale. La chain inoltre distribuisce le fee ai partecipanti e gestisce eventuali le dispute tra nodi.

### I Crypto Customer e i Merchant Acquirers

I Crypto Customer acquirers hanno lo scopo di gestire il wallet del cliente, verificare che abbia saldo a sufficienza e ridurlo una volta completata la transazione.

Analogamente i merchant acquirers gestiscono la transazione e l'autorizzazione in base alla richiesta ricevuta dal POS.

### Council nodes

Gestiscono la validazione delle nuove transazioni e delle fee in CRO da elargire. Vengono ricompensati in base al numero di transazioni che validano.

I nodi utilizzano [[Tendermint Core](https://tendermint.com/docs/) come algoritmo di consenso che supporta la [BFT]].

## Cronos chain

Questa è la nuova chain ci Crypto.com dove le gas fee vengono pagate in [[Resources/Money/Crypto/Notes/Token]] CRO. Cronos offre tutti i classici servizi della [[DeFi]] anche se ora siamo ancora in una fase embrionale.

## Il token CRO

Il [[Resources/Money/Crypto/Notes/Token]] CRO la una valuta nativa di Crypto.com e permette all'intero sistema di funzionare in quanto è emessa dalla piattaforma stessa e viene utilizzata per pagare le commissioni di trading, di conversione e i vantaggi per gli utenti, come i cashback delle carte.

Questo è nato come un classico utility token [[ERC20]] per supportare tutti i costi della piattaforma ma, col tempo, si è evoluto in una vera e propria coin. Infatti ora è la coin della crypto.org chain e di Cronos, le due chain di Crypto.com.

Tutti i partecipanti della crypto.com chain devono usare i token CRO per pagare le fee delle transazioni per ogni blocco. Questi token sono guadagnati principalmente come reward ai nodi per processare e verificare le transazioni. Per poter entrare nel processo di validazione ogni nodo deve mettere in stake un determinato numero di CRO.

Un limite di CRO è che questo ultimo è scambiabile principalmente sulla piattaforma nativa Crypto.com e nell’universo legato a questa applicazione, come Crypto Exchange.

E' una moneta sicuramente più giovante di [[BNB]] ma dal grande potenziale.

## Carta VISA

Crypto.com, analogamente a Binance e altri, ha una sua **carta prepagata VISA che permette di effettuare pagamenti in tutto il mondo con un cashback in token CRO**.

E' possibile caricare la carta con anche criptovalute o [[Stablecoin]] come [[USDC]], ETH, BTC, Ripple e tanti altri.

E' possibile caricare la carta direttamente da una carta di credito esterna (senza commissioni e in tempo reale) oppure dal proprio wallet fiat (ricaricabile tramite un normale bonifico). Attenzione che è questo spostamento di fondi è unidirezionale: **non è infatti possibile spostare fondi dalla carta al wallet** (al contrario di Binance).

Questa carta non ha alcuna spesa, a meno di voler chiudere la carta o che venga smarrita.

Un vantaggio importante è che **la carta non ha alcuna fee di conversione**: questo significa che se io trasferisco 100€ di ETH sulla carta e li converto in euro, otterrò 100€ senza alcuna fee. Binance, per esempio, ha lo 0,9% di commissioni.

### Cashback

Il vantaggio principale di questa carta è il **cashback che fornisce si tutti i pagamenti effettati, in percentuale variabile in base al numero di CRO vincolati per minimo 6 mesi**.

In particolare la piattaforma richiede un determinato numero di CRO bloccati per 6 mesi per ogni tipologia di carta, da un minimo di 0€ per la Midnight Blue a un massimo di 350000€ (in controvalore) per la Obsidian.

**Al termine dei 6 mesi è possibile tenere ancora i CRO bloccati per avere tutti i vantaggi della carta oppure sbloccarli e ritirarli perdendo però i benefici**.

Qualora il valore dei CRO sia aumentato rispetto ai 6 mesi precedenti posso comunque ritirare tutti i CRO e poi ri depositare solo i 3500€ (per esempio) necessari per il tier di carta voluto.

Qui sotto la tabella riassuntiva di tutti i livelli.

![[image-5.webp]]

#### Midnight Blue

Offre soltanto il **cashback dell'1%** ma non necessita di alcun CRO vincolato. Utile per provare le funzionalità della carta.

#### Ruby Steel

Per questa carta sono necessari 350€ vincolati per 6 mesi. Si ottiene il **2% i cashback e l'abbonamento a Spotify**.

_Ok, ma come fa Crypto.com a pagarmi Spotify??_

Semplice, basta che il metodo di pagamento impostato su Spotify sia la carta ci crypto.com. Quando Spotify addebiterà il costo mensile riceverò un rimborso in CRO pari a quanto pagato fino a un massimo di 12.99$.

Questa è la versione migliore per chi si vuole esporre il meno possibile a CRO e utilizzare la carta. Inoltre usando [il mio referral link](https://crypto.com/app/7ase4g37jk), una volta messi in stake i 350€ in CRO riceveremo entrambi 25$ in CRO.

#### Royal Indigo & Jade Green

Per questa carta sono necessari 3500€ vincolati per 6 mesi. Si ottiene il 3% i cashback e l'abbonamento a Spotify e Netflix con le stesse modalità indicate sopra.

Inoltre da questo livello in poi della carta posso avere delle **rendite migliori nella parte di Earn**, come descrivo nella sezione seguente.

Un ultimo vantaggio che purtroppo non è indicato nel prospetto ufficiale del sito è che ho il **10% annuo sui CRO in [[Staking]]**, inclusi quelli per ottenere la carta stessa.

#### Frosted Rose Gold & Icy White

Per questa carta sono necessari 35000€ vincolati per 6 mesi. Si ottiene il 5% i cashback e l'abbonamento a Amazon Prime, oltre a quelli indicati sopra e altri vantaggi minori.

#### Obsidian

Per questa carta sono necessari 350000€ vincolati per 6 mesi e fornisce numerosi vantaggi

## Earn

Questa modalità permette di mettere a reddito le criptovalute possedute con una determinata rendita

Data una valuta, i rendimenti variano in base a 2 fattori: il numero di CRO in stake e il numero di giorni in cui tale valuta risulta bloccata e non utilizzabile.

![[image-1024x593.webp]]

### CRO in Stake

Per incentivare l'acquisto del [[Resources/Money/Crypto/Notes/Token]] CRO Crypto.com offre interessi differenti in base al numero di CRO tenuti in [[Staking]] per 6 mesi (li stessi CRO utilizzati per ottenere la carta Visa). In particolare i rendimenti variano se in stake ci sono (in controvalore) meno di 350€, da 350 a 3500€ o da 3500€ in su; ovviamente più CRO sono in stake maggiore saranno i rendimenti. Se si possiede più di 350000€ in CRO i rendimenti sono ancora maggiori ma non credo sia il caso di nessuno che legge questo blog ;).

Dall'app questo concetto viene espresso con la tipologia di carta in proprio possesso: Ruby o inferiore i tassi sono ridotti, mentre con Jade/Indigo o superiore i tassi sono maggiorati.

### Termine

Vi sono solo 3 opzioni per quanto riguarda il tempo in cui la moneta viene "bloccata":

- **Flexible**: non c'è un tempo minimo in cui gli asset risultano bloccati, questi possono essere ritirati in qualsiasi momento. Il rendimento è tipicamente più basso ma ho una maggiore flessibilità
- **1 month term**: Gli asset vengono bloccati per un mese ed è impossibile ritirarli prima. Tipicamente offrono un guadagno maggiore di Flexible
- **3 month term**: Gli asset sono tenuti per 3 mesi e il guadagno è ancora maggiore rispetto al punto precedente.

## Supercharger

Questo metodo è disponibile sia dall'Exchange che dall'app e permette di guadagnare mediante la distribuzione di nuove coin.

Il funzionamento è molto semplice: vi sono dei periodi chiamati "periodi di ricarica" (45 giorni) in cui è possibile andare a mettere i propri CRO in un pool e dei periodi chiamati "periodi di ricompensa" (45 giorni) in cui viene fornita una ricompensa in base a:

- l numero di CRO aggiunti nel pool per il periodo di ricarica (maggiore è il tempo dei CRO inseriti nel pool maggiore sarà la ricompensa
- Numero totale di CRO immessi da tutti gli utenti
- Alla ricompensa totale decisa dalla piattaforma (per esempio allocazione 1000000$ per ETH significa che vi è il controvalore in ETH di 1M di dollari in premio)

Questo metodo è possibile sia tramite app che tramite Exchange: dall'Exchange basta essere loggati e avere i CRO da depositare, analogamente dall'app. Ricordo che i CRO dell'app non sono gli stessi dell'Exchange ma è possibile spostarli da uno all'altro senza costi e istantaneamente.

## Syndicate

I syndicate sono degli eventi solo sull'Exchange che durano massimo una giornata durante il quale si può acquistare una crypto a un prezzo del 50%. Ho quindi un guadagno certo dato che il prezzo è volutamente la metà del prezzo di mercato.

_Wow! Adesso sono pronto a guadagnare!_

Non così in fretta.

Per poter partecipare al syndicate è necessario avere una certa quota di CRO in stake sull'Exchange (n.b. non sull'app) e avere un determinato volume di trading in $ sulla piattaforma. Per esempio con 5000 CRO in stake e 5000$ di volume di trading è possibile acquistare un controvalore massimo di 500$ della valuta in questione. Maggiori sono queste cifre maggiore è la quantità di valuta acquistabile. Vi è inoltre un limite massimo al numero di coin complessivi distribuibili definito dalla piattaforma.

Analogamente al launchpad di Binance vi è una prima parte di iscrizione. Dopo qualche giorno Crypto.com comunica quanti [[Resources/Money/Crypto/Notes/Token]] massimi è possibile acquistare ed è possibile accettare o rifiutare. Se accettate vengono dedotti i CRO e restituiti i [[Resources/Money/Crypto/Notes/Token]] in questione a metà prezzo.

## [[DeFi]] wallet

[Wallet non custodial](https://crypto.com/eea/defi-wallet) scaricabile come app dove è possibile caricare le proprie crypto e utilizzare la [[DeFi]] con tutti i relativi vantaggi (come gli [[APY]] maggiorati) e rischi.

Essendo un wallet non custodial le chaivi private sono in gestione del proprietario, come tutte le relative responsabilità.

I guadagni derivano da varie piattaforme di [[DeFi]] come [Compound lending](https://compound.finance/), [[[staking]] di Cosmos](https://cosmos.network/learn/[[staking]]/), [Yiern](https://yearn.finance/#/home), [[Staking]] su [Crypto.com chain](https://crypto.org/) e [Aave lending](https://aave.com/), la comodità è che **tutte queste operazioni possono essere effettuare direttamente dal wallet senza passare per le piattaforme in questione**.

## [[DeFi]] swap

[[[DEX]]](https://crypto.com/defi/swap) sviluppato da Crypto.com basato su Ethereum molto simile a [Uniswap](https://uniswap.org/). Essendo decentralizzato non è tecnicamente gestito da crypto.com ma solo brandizzato a suo nome. Come tutti i [[DEX]] è possibile connettersi ad un wallet esterno, come Metamask, il [[DeFi]] wallet di crypto.com o un wallet compatibile con wallet-connect.

Per avere le statistiche di utilizzo di questo [[DEX]] è possibile controllare [qui](https://crypto.com/defi/swap-info).

### Swap

![[image-1 1.webp]]

Permette di scambiare un [[Resources/Money/Crypto/Notes/Token]] con un altro

### Pool

![[image-2 1.webp]]

Serve per poter aggiungere liquidità ad un pool (in rapporto 50% 50%) in modo da guadagnare fee dai trader che effettuano gli swap dei due [[Resources/Money/Crypto/Notes/Token]] in questione.

Per poter avere le coppie con più rendimento (controllando sempre che abbiano un minimo di liquidità) è possibile andare [qui](https://crypto.com/defi/swap-info), nella sezione Pairs, ordinando per [[APY]] senza considerare le coppie con liquidità, per esempio, inferiore a 1M.

### Boost

![[image-3.webp]]

Questa modalità permette di fare yield farming sui propri CRO. In particolare permette di **aggiungere un moltiplicatore alle rendite del pool di liquidità visto prima in base al numero di CRO messi in stake sul [[DeFi]] wallet** per un determinato periodo di tempo (ricordo che questo wallet è diverso da quello dell'app e diverso da quello dell'Exchange).

Quindi fino a che questi CRO sono bloccati in stake quando andrò a mettere della liquidità nel pool riceverò dei CRO.

Tramite la sezione [[APY]] è possibile avere una idea dell'[[APY]] fornito dallo stake dei CRO. Il valore della liquidità inserita nel pool non influisce con questo valore.

![[image-4.webp]]

Qualora mettessi 1000 USD nel pool di liquidità otterrei, annualizzati, 79.10 CRO extra, oltre alle fee del pool

I CRO delle Yield non vengono forniti subito, ma vengono forniti dopo 90 giorni (30 giorni se 100k CRO in stake) da quanto è finito il periodo di stake.

Per avere una idea più chiara di come vengono calcolate queste commissioni è possibile vedere la tabella:

![[hedUrWZbFn6LE7P4Q23BlV4Ho2IeA8XqMzkXm0h2R-04xLYS8OhrzLOTMAQrZDSfZ46E4PSPVpodlv3uWQhsp9pIM-RosSkzPHnf_5qfY_iopnpi3cYmydvCd7GvVU3Ka-Ihxwn-1024x636.webp]]

Per una spiegazione completa vedi la [FAQ ufficiale](https://help.crypto.com/en/articles/4429871-how-is-my-accrued-cro-defi-yield-calculated-on-defi-swap).

## Conclusioni

Crypto.com è la principale concorrenza a Binance come ecosistema crypto. Come interfaccia lo ritengo più confusionario ma i guadagni e i vantaggi nell'utilizzo sono migliori.

Il suo [[Resources/Money/Crypto/Notes/Token]] nativo CRO è un [[Resources/Money/Crypto/Notes/Token]] ancora poco sviluppato fuori dal mondo Crypto.com ma di sicuro dal grande potenziale.

Se vi è piaciuto questo articolo e volete supportarmi potete usare [il mio referral link](https://crypto.com/app/7ase4g37jk) (code: 7ase4g37jk). Una volta messi in stake i 350€ in CRO per la carta Ruby Steel riceveremo entrambi 25$ in CRO.
