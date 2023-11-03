---
tags:
  - Finance
  - Definition
  - PublishedPosts
---


Una opzione è un derivato finanziario che rappresenta un contratto assicurativo tra un venditore e un contraente.
In inglese è detto anche *warrant* ed è molto simile al [[Futures]] con la differenza che non è un obbligo simmetrico ma è un impegno solo per una delle due parti.

Una opzione è definita da tre parametri:

- **Asset**: la stock o [[ETF]] su cui si basa il contratto;
- ***Strike price***: quale è il prezzo affinché la option può essere esercitata;
- ***Expiration date***: data di scadenza nella quale la option può essere esercitata.

Delle opzioni posso essere venditore o acquirente, in particolare:

- ***Option writer*** o ***option seller***: colui che vende l’opzione;
- ***Option buyer***: colui che compra l’opzione.

Nello slang si dice essere ***long*** su una opzione se la compro, mentre essere ***short*** se la vendo.

Una opzione non è gratis ma ha un prezzo ***proporzionale al rischio che corre per assicurare il contraente contro l’evento, questo prezzo viene chiamato premium*** o ***price.*** Questo prezzo viene definito dal mercato e dipende da tanti fattori.

Le opzioni possono essere in tre stati in base alla differenza tra il prezzo attuale della stock e lo strike price:

- ***Out of The Money (OTM)***: l’opzione, se scadesse ora, non verrebbe esercitata. Una call è OTM quando lo strike price è maggiore di quello attuale.
- ***In The Money (ITM):***  l’opzione, se scadesse ora, verrebbe esercitata. Una call è OTM quando lo strike price è inferiore di quello attuale.
- **At The Money (ATM)**: lo strike price e il valore dell’azione sono molto vicini.

Dato uno strike price e una expiration date, il numero di opzioni aperte per un determinato sottostante si chiama ***open interest.***

Anche le opzioni hanno un Bid Ask spread analogo alle azioni ma, essendo comunque un prodotto molto più granulare (per una stock ho potenzialmente infiniti contratti diversi apribili) il mercato è meno efficiente e quindi tale spread è relativamente alto.

E’ importante sapere che le opzioni si basano sempre su 100 azioni, anche se il premium indicato è su una singola azione (che va quindi moltiplicato per 100 per sapere il valore complessivo).

Mentre le stock sono emesse da una azienda, quindi il loro numero circolante è costante o comunque modificabile solo dall’azienda, nelle opzioni invece il numero di queste ultime aperte è potenzialmente infinito in quanto dal nulla è sempre possibile creare un nuovo contratto.

La somma algebrica delle opzioni long e short fa sempre zero, in quanto per ogni una nuova opzione che vendo c’è sempre qualcuno che la sta comprando.

## Short call

![[Untitled 8.png]]

Vendere una call (short call) è una strategia ribassista che consiste nel vendere una call su una stock che si crede scenderà di prezzo; in particolare che non salga più dello strike price + premium entro l’expiration date.

<aside>
💡 Vendendo una call ho fornisco la garanzia di vendere all’acquirente una stock allo strike price all’expiration date.
</aside>

Assumiamo che oggi l’azione ABC valga 100\$. Posso vendere una call a 110\$ fra un mese a 5\$ (quindi fra un mese sarò obbligato a vendere l’azione ABC a 110\$ indipendentemente dal suo valore in quel momento).

Fra un mese l’azione potrà valere:

- meno di 110\$: l’opzione non verrà esercitata e avrò guadagnato 5\$;
- tra 110\$ e 115\$: l’opzione verrà esercitata ma ci avrò guadagnato comunque, in quanto ho incassato il premium (nel grafo sono tra *x* e *break-even*);
- Maggiore di 115\$: l’opzione verrà esercitata e avrò perso proporzionalmente al valore dell’azione in quel momento. Se l’azione vale 1000\$ ho perso 875\$.

| Massimo profitto | Premium |
| --- | --- |
| Massima perdita | Illimitata (per naked call) |
| Break-even | Strike price + premium |
| Aspettative sulla stock | Ribassiste |

### Naked

E’ possibile vendere una call anche se non si possiedono le stock da vendere qualora venisse superato lo strike price, in questo caso si dice che sto vendendo delle short call ***naked (call scoperte).*** 

Questa è una operazione molto pericolosa in quanto posso avere potenzialmente perdite illimitate in quanto, al momento dell’esercizio dell’opzione, **dovrei comprare le stock in questione qualsiasi sia il loro prezzo per poterle rivendere a chi mi ha comprato la call**.

Tipicamente i broker liquidano le posizioni qualora vi siano naked call non coperte da altri asset eventualmente liquidabili in caso di realizzo per pagare le stock.

### Covered

Le covered call sono il contrario delle naked ed è la strategia di vendere call su delle stock che si possiedono (call coperte).

In questo modo le perdite non sono illimitate in quanto, anche se la stock facesse 1000x, comunque io non devo comprarle al prezzo di mercato ma rivendo quelle che ho, che quindi hanno fatto anche loro 1000x.

In questo caso più che una perdita ho un mancato guadagno.

<aside>
💡 Vendere covered call permette di ridurre il caso migliore di tali stock (se crescono più dello strike price io sono obbligato a venderle a tale valore) ma riducono anche il caso peggiore in quanto ho il premium che mi aiuta in caso di caduta nel valore della stock.

</aside>

### Short call Deep Out of The Money

Essendo deep out of the money ho una alta probabilità che l’evento non si realizzi e quindi di incassare il premium.

Questo è un reverse lottery ticket: sto assicurando su evento estremamente improbabile. Ho una alta probabilità di prendere il premium senza fare nulla.

## Long call

![[Untitled 1 6.png]]

Comprare una call (***long call***) è una strategia rialzista che consiste nel comprare una call su una stock che si crede aumenterà di prezzo; in particolare quando ci si aspetta che il suo prezzo aumenti di più dello strike price + premium entro l’expiration date.

<aside>
💡 **Comprando una call io voglio la garanzia di poter *comprare* una stock ad un determinato strike price all’expiration date.**

</aside>

Assumiamo che oggi l’azione ABC valga 100\$. Posso comprare una call a 110\$ fra un mese a 5\$ (quindi fra un mese potrò comprare l’azione ABC a 110\$ indipendentemente dal suo valore in quel momento).

Fra un mese l’azione potrà valere:

- meno di 110\$: l’opzione non verrà esercitata e avrò perso 5\$;
- tra 110\$ e 115\$: l’opzione potrà essere esercitata ma ci avrò perso comunque, in quanto ho pagato precedentemente il premium (nel grafo sono tra *x* e *break-even*);
- Maggiore di 115\$: l’opzione verrà esercitata e avrò guadagnato proporzionalmente al valore dell’azione in quel momento. Se l’azione vale 1000\$ ho guadagnato 875\$.

| Massimo profitto | Illimitato |
| --- | --- |
| Massima perdita | Premium |
| Break-even | Strike price + premium |
| Aspettative sulla stock | Rialziste |

### Long call deep out of the money

Comprare una call deep out of the money è molto simile al gambling in quanto costano poco (l’evento è improbabile) ma se succede la botta di fortuna posso fare potenzialmente parecchi soldi.

Esempio se una stock vale 60\$ io compro una call a 100\$ a un prezzo bassissimo, diciamo 10\$. Se l’azione non supera i 100\$ ho perso solo 10\$, se invece va a 200\$, esempio, posso fare molti soldi con un investimento piccolissimo.

Fare una operazione del genere è molto simile a comprare un gratta e vinci o un biglietto della lotteria, posso vincere molto ma con una probabilità molto bassa.

### Long call deep in the money

Questo tipo di operazioni è considerabile investimento a leva (***leveraged investment***): se ho una azione a 100% e compro una call a 50\$ sto investendo a leva 2x sul sottostante.

Se l’azione sale del 10% anche la mia call salirà del 10% (il valore intrinseco aumenta all’aumentare del valore della stock), quindi ho un guadagno del 20% (leverage 2x).

## Put

### Short Put

![[Untitled 2 4.png]]

Vendere una put (short put) è una strategia rialzista che consiste nel vendere una put su una stock che si crede salirà di prezzo: in particolare che non scenda meno dello strike price - premium entro l’expiration date.

<aside>
💡 **Vendendo una put fornisco la garanzia di comprare all’acquirente una stock allo strike price all’expiration date.**

</aside>

E’ consigliabile seguire questa strategia qualora si abbia intenzione di acquistare comunque la stock in questione a sconto qualora l’opzione sia in the money: se va bene prendo il premium, altrimenti prendo una stock ad un prezzo scontato rispetto al prezzo attuale.

Assumiamo che oggi l’azione ABC valga 100\$. Posso vendere una put a 90\$ fra un mese a 5\$ (quindi fra un mese sarò obbligato a comprare l’azione ABC a 90\$ indipendentemente dal suo valore in quel momento).

Fra un mese l’azione potrà valere:

- meno di 85\$: l’opzione verrà esercitata e avrò perso la differenza tra il valore attuale della stock e (strike price - 5\$); La massima perdita possibile si ha se il valore crolla a 0, in quel caso perderò lo strike price meno il premium (la perdita è comunque limitata).
- tra 85\$ e 90\$: l’opzione verrà esercitata ma ci avrò guadagnato comunque, in quanto ho incassato il premium (nel grafo sono tra *x* e *break-even*);
- Maggiore di 90\$: l’opzione non verrà verrà esercitata e avrò guadagnato il premium

| Massimo profitto | Premium |
| --- | --- |
| Massima perdita | (Strike price - premium) |
| Break-even | Strike price - premium |
| Aspettative sulla stock | Rialziste |

### Short put per stock da acquistare

Vendere una put su una stock che si è disposti ad acquistare può essere una buona strategia per incassare un premium e prendere una stock a sconto rispetto al prezzo attuale.

Assumiamo di volere comprare una stock che ora vale 95\$: invece di comprarla a mercato vendo una put a 90\$: se la stock sale ho incassato il premium ma non ho la stock. Se la stock scende a 90\$ la comprerò scontata. Ho una perdita qualora la stock scendesse sotto i 90\$ ma comunque la avrei avuta comunque la perdita anche se l’avessi acquistata normalmente a 95\$. La perdita vera la avrei se la stock aumenta di molto il suo prezzo, ipotizziamo 200\$: in questo caso ho sì incassato il premium ma ho un mancato guadagno in quanto non ho in mano la stock il cui valore ora è 200\$.

Un ulteriore svantaggio di questa strategia è che richiede molta liquidità bloccata (100 x lo strike price) in quanto devo avere modo di esercitare la put.

Questo metodo non è più efficiente di comprare una stock a mercato ma può essere una strategia per migliorare il caso peggiore.

### Long Put

![[Untitled 3 4.png]]

Comprare una put (***long put***) è una strategia ribassista che consiste nel comprare una put su una stock che si crede scenderà di prezzo: in particolare che scenda più dello strike price - premium entro l’expiration date.

<aside>
💡 **Comprando una put io voglio una garanzia di poter *vendere* all’acquirente una stock allo strike price all’expiration date.**

</aside>

Assumiamo che oggi l’azione ABC valga 100\$. Posso comprare una put a 90\$ fra un mese a 5\$ (quindi fra un mese potrò vendere l’azione ABC a 90\$ indipendentemente dal suo valore in quel momento).

Fra un mese l’azione potrà valere:

- meno di 85\$: l’opzione verrà esercitata e avrò guadagnato la differenza tra il valore attuale della stock e (strike price - 5\$); Il massimo guadagno possibile si ha se il valore crolla a 0, in quel caso guadagnerò lo strike price meno il premium.
- tra 85\$ e 90\$: l’opzione verrà esercitata ma ci avrò perso comunque, in quanto ho pagato il premium (nel grafo sono tra *x* e *break-even*);
- Maggiore di 90\$: l’opzione non verrà verrà esercitata e avrò perso il premium

| Massimo profitto | (Strike price - premium) |
| --- | --- |
| Massima perdita | Premium |
| Breakeven | Strike price - premium |
| Aspettative sulla stock | Ribassiste |

I broker presentano una schermata analoga alla seguente per l’acquisto o la vendita di opzioni.

![[Untitled 4 4.png]]

Nell’esempio ho una stock di Coca Cola al valore 64.20 \$ e sto guardando le opzioni con scadenza domani.

A sinistra abbiamo le calle e a destra le put.

Sto guardando l’esempio di domani ho pochissimo time value, quindi i prezzi delle opzioni riflettono il valore attuale della stock.

Dato che comprando una call a 61\$ io voglio la garanzia di poter comprare una stock a 61\$ domani, se oggi il valore di KO vale 64\$ la call dovrà valere almeno la differenza. Domani quindi pagherò i 61\$ di KO con l’opzione che, sommati ai 3\$ di premium ottengo i 64\$ di oggi. Se non fosse così potrei generare soldi dal nulla. Questo valore è detto **valore intrinseco della call**.

Una call in the money ha sempre un valore intrinseco che è la differenza tra lo strike price e il valore attuale più eventualmente u**n valore estrinseco che dipende dal tempo e della variabilità**.

Analogamente le call out of the money per domani valgono quasi zero in quanto la probabilità che KO vada a 70\$ domani sono estremamente basse.

Lo stesso ragionamento si ha comprando una put out of the money: se compro una put a 70\$ domani, significa che voglio poterti vendere KO a 70\$: se KO oggi vale 64\$ la put costerà almeno 6\$ (valore intrinseco) più un eventuale valore estrinseco (che se lo strike price è domani è praticamente zero).

Se aumentiamo il tempo inizio a vedere dei valori un po’ diversi in quanto il valore estrinseco aumenta, in quanto aumenta la probabilità che l’evento accada.

Per esempio se prendo un intervallo di 2 settimane vedrò che le call out of the money cominciano ad avere un valore. Per esempio una call a 67€ la pagherò un minimo che dipende dalla probabilità che KO superi 67\$ fra 15 giorni,

![[Untitled 5 2.png]]

## Prezzo delle opzioni

Il presso delle opzioni dipende dalla variabilità del sottostante e dalla distanza temporale dallo strike price. All’aumentare del tempo e della variabilità ho un aumento del prezzo della opzione.114,03

Il valore IV che si vede al centro sopra “Strike” significa ***Implied Volatility*** (nel caso di KO è 20.5%) e indica quanto ci si aspetta che il sottostante si muova: maggiore è la sua volatilità maggiore è il prezzo che andrò a pagare per comprare una determinata opzione; questo ha senso in quanto con una andamento volatile ho una maggiore probabilità che l’evento si verifichi.

Questo è un valore che viene calcolato dal prezzo delle opzioni scambiati, maggiore è il prezzo che il mercato è disposto a pagare una opzione maggiore sarà il valore di IV di una stock.

Prendendo una azione più volatile di KO, per esempio Coinbase vedo che il suo valore di IV è 112%.

Il valore di IV varia con il tempo e aumenta all’aumentare di questo, nel senso che con un orizzonte temporale di 1 anno avrò più volatilità potenziale di 1 mese, per esempio.

Per esempio potrei avere che la IV di KO con un orizzonte di 3 anni sia uguale a quella di COIN di 1 mese, e conseguentemente anche i prezzi delle opzioni seguiranno tale andamento.

### Esempio

Considerando lo stesso Strike Price 17/06/22 vediamo un acquisto di due call, la prima per KO e la seconda per COIN.

![[Untitled 6 1.png]]

Valori delle call per KO

![[Untitled 7 1.png]]

Valori delle call per COIN

Prendiamo il valore della call più vicina al prezzo attuale: nel caso di KO costa 0.93€ per azione nel caso di COIN 7.5€. KO è molto stabile quindi comprare una assicurazione di comprare l’azione al prezzo attuale non è molto costoso.

COIN invece è molto volatile, quindi è molto probabile che al 17/06 il prezzo non sia 70\$ ma potrebbe essere molto più alto o molto più basso, comprare un’assicurazione è quindi più caro.