---
tags:
  - Finance
  - Bond
  - PublishedPosts
---
> [!tip] Title
> Calcolatore prezzo: https://docs.google.com/spreadsheets/d/1dk5C2Jsts32zPvcdMWhl_tq0601aDGWrmYmu88L67GQ/edit?usp=sharing
## Introduzione
Le obbligazioni sono titolo di debito per chi le emette e titoli di credito per chi le acquista che sono emessi da stati o aziende. Questo prestito viene premiato con degli interessi anno per anno al creditore e inoltre il capitale viene restituito al termine.

Questo prestito diventa poi cedibile a terzi nel mercato secondario ad una cifra variabile in base alle condizioni del mercato.

## Caratteristiche
Le obbligazioni hanno 6 caratteristiche principali:

### Emittente
I bond possono essere emessi dagli stati (obbligazioni governative) o da aziende (obbligazioni societarie). Gli stati le emettono per ripagare il debito mentre le aziende come forma alternativa al prestito.

### Valuta di denominazione
La valuta dei soldi prestati. Se ho prestato degli euro dovrà ridare sempre euro; mi espongo quindi al rischio cambio.

### Cedola
Interessi che vengono forniti al creditori periodicamente e possono essere fisse (decise in partenza) o variabili.
Esistono le obbligazioni *zero coupon* che non danno alcuna cedola ma gli interessi sono dati solo dalla differenza tra il prezzo di acquisto e quello di vendita dell'obbligazione.
### Tipologie
* **Cedola (tasso) fissa**: mi verranno dati degli interessi periodici a ==percentuale costante== ogni mese e a scadenza mi verrà restituito il capitale. In questi casi so di preciso quando sarà il rendimento nominale complessivo. **Qualora i tassi aumentino (quindi le cedole delle altre obbligazioni) i bond a cedola fissa diminuiranno di prezzo, al contrario aumenteranno**. Questo meccanismo non interessa alle persone che tengono l'obbligazione fino alla fine.
* **Cedola (tasso) variabile**: ==variano in base a degli indici== (esempio obbligazioni indicizzate all'inflazione). Le più famose sono i BTP euro (indicizzati all'inflazione europea) e BTP Italia (indicizzati all'inflazione italiana). **Il loro prezzo sarà sempre attorno a 100 in quanto la loro cedola segue il mercato**.
	* Step-up: in questo caso il tasso cambia crescendo sempre di più di quantità definite a propri di anno in anno.
* **Zero coupon**: ==non abbiamo cedole==, il rendimento sarà tra il prezzo che ho pagato e quanto mi verrà restituito. **Il loro prezzo è sempre inferiore a 100 (altrimenti nessuno le comprerebbe)**. Esempio sono i BOT che hanno tipicamente durata inferiore all'anno.
* **Strutturate**: sono una unione tra una obbligazione classica e un derivato. Esempio sono le *obbligazioni convertibili* che a scadenza possono essere convertite in azioni di quella stessa azienda. Oppure le *obbligazioni callable* o le *obbligazioni putable*.
#### Acquistare il giorno prima della cedola?
Potrebbe sembrare furbo acquistare l'obbligazione il giorno prima dello stacco cedola in modo da incassare il premio.
Questo metodo non funziona in quanto quando acquistiamo una obbligazione ad una certa data ==dobbiamo dare a chi ce la vende anche la parte di cedola da lui maturata fino ad oggi==.
Questi calcoli vengono effettuati direttamente dalla banca: dovrò pagare quindi il prezzo dell'obbligazione e un ulteriore costo chiamato "rimborso cedola" che dipende dai giorni in cui li ha avuto l'obbligazione dall'ultimo stacco cedola.

### Data di scadenza
In tale data dovrà ridare il capitale versato e una parte gli interessi (*maturity*).
Esistono obbligazioni a scadenza breve come i BOT oppure con scadenze molto lunghe (come i BTP). Tipicamente più è lunga la scadenza dell'obbligazioni maggiori sono gli interessi.

### Prezzo
Abbiamo tre tipologie di prezzo
* **Prezzo di emissione**: prezzo a cui viene venduta inizialmente l'obbligazione in un asta. Prezzo iniziale.
* **Prezzo di quotazione**: prezzo dell'obbligazioni in un determinato momento al mercato. Prezzo durante la vita.
* **Valore nominale**: i soldi che ci verranno restituiti alla scadenza (tipicamente 100/centesimi). A differenza delle azioni non si dice "comprare una obbligazione" ma "comprare x€ di valore nominale di una obbligazione". Questo è anche il valore **su cui vengono calcolatri gli interessi**. Prezzo finale.

## Rischio
Le obbligazioni hanno un rischio che dipende dalla solvibilità del debitore. Le agenzie di rating si occupano di valutare quanto è affidabile un debitore e distinguono le obbligazioni in buone (*investment grade*) e cattive (*junk bond*).
Esistono vari rischi:
* **Rischi di credito**: rischio che l'emittente non riesca a pagare le cedole o magari neanche il capitale versato. L'emettitore va in default.
* **Rischio interesse**: se vendo l'obbligazione prima della scadenza posso venderla ad un prezzo anche minore rispetto a quanto l'ho comprata.
* **Rischio liquidità**: non è detto che qualora volessi vendere il mio bond ci sia qualcuno che lo vuole, soprattutto se sono bond di piccoli stati o roba esotica. In questi casi devo aspettare obbligatoriamente la scadenza.
* **Rischio cambio**: se la valuta del bond si svaluta rispetto alla mia valuta, ci perdo.

## Tasse
Sugli interessi cedolari e sulla plusvalenza ho una aliquota del 12.5% per le obbligazioni italiane o della comunità europea, altrimenti il 26%.
Anche per le obbligazioni le minusvalenze sono compensabili con le plusvalenze ma solo sulla differenza tra il prezzo di acquisto e di vendita; le cedole invece non sono compensabili.

## Orizzonte temporale
Se una obbligazione ha scadenza tra *n* anni ciò non significa che io non possa rivenderla prima al prezzo di quotazione corrente, ovviamente assumendo i rischi che tale prezzo sia inferiore al prezzo a cui l'ho pagata.
Esempio, assumiamo che io acquisti una obbligazione all'emissione, quindi a 100 e che tale obbligazioni duri 6 anni.
Se la tengo fino a scadenza mi verranno ridati i miei 100 e avrò preso le cedole.
Se invece ho bisogno di soldi prima e sono costretto a venderle, dovrò venderle al prezzo attuale, quindi magari sotto al 100 e conseguentemente avere una minusvalenza (o anche una plusvalenza se sono fortunato).

## Il prezzo delle obbligazioni

La particolarità delle obbligazioni è che il loro prezzo viene sempre definito in centesimi di euro (posso vederlo come una percentuale) assumendo che **alla data del termine mi verrà ridato sempre 100**.
I tagli delle obbligazioni sono tipicamente di 1000€.

Es.: acquisto oggi 1000 euro nominali di btp scadenza 2030 al prezzo di 98 ; il capitale investito e’ di 980 euro (valore nominale 1000 * prezzo d’acquisto 98)/100.
A scadenza riceverò’ 1000 euro come restituzione del capitale, a fronte dei 980 euro investiti, con un guadagno capitale aggiuntivo del 2%; nel periodo di “vita” del titolo incassero’ ovviamente le cedole previste.

Il prezzo di quotazione delle obbligazioni varia principalmente **da quanto i tassi sono alti o bassi in un determinato momento del mercato e dalla solidità dell'emittente**: è per questo che il prezzo di quotazione delle obbligazioni continua a cambiare e non rimane costante nel tempo.
==Il prezzo delle obbligazioni dipende dai tassi in quanto dipende dalle altre obbligazioni che sono a mercato: se oggi esce una nuova obbligazione con un tasso maggiore, l'obbligazione corrente diminuirà il proprio valore.==
Un altro elemento che fa cambiare il prezzo delle obbligazioni è quanto l'emittente sia affidabile: se sorgono dei dubbi sul fatto che l'emittende non paghi del cedole o l'obbligazione (se l'azienda/stato rischiano di fallire) il loro prezzo diminuirà per compensare il rischio.
Per esempio i famosi bond argentini di qualche anno fa sono stati rimborsati a 25 dopo il fallimento della stessa argentina.

Per esempio se un BTP ha una cedola del 2% ma i tassi sono al 6% nessuno vorrà acquistarlo, conseguentemente il suo valore tenderà a scendere ben sotto i 100 fino a compensare il mancato guadagno delle cedole.
Al contrario se ho una cedola del 2% per 20 anni e i tassi sono allo 0%, tale obbligazione avrà un valore ben superiore a 100 in quanto mi sobbarco una perdita alla fine (pago 120 esempio ma riceverò 100) ma nel mentre ho delle cedole molto più alte del mercato.
Analogamente se ora l'azienda emittente è considerata a rischio fallimento nessuno vorrà pagare una sua obbligazione a 100, esempio, ma magari a 70 o anche meno.
Per esempio questa obbligazione di Coinbase è partita a 95 ma è scesa toccando anche i 50: Coinbase nell'utlimo anno è diventata una azienda a rischio e conseguentemente gli investitori sono disposti a pagare pochissimo una sua obbligazione.
![[Pasted image 20221204222150.png]]

### Tipologie di acquisto

Una obbligazione può essere acquistata sotto, alla o sopra la pari.

#### Sotto la pari
Acquisto sotto la pari quando acquisto una obbligazione il cui valore è sotto 100.
Possono essere emesse obbligazioni sotto la pari per invogliare gli investitori con un prezzo scontato. La cedola verrà sempre calcolata con il valore nominale (100) ma **a scadenza l’investitore percepirà più del capitale versato, cioè la differenza tra prezzo di sottoscrizione e il valore nominale**.
Per esempio se emetto un BTP con un tasso più basso di quanto interessi al mercato posso emettere tale BTP a 95, così è vero che avrò cedole basse ma magari un premio più alto alla fine.
Una obbligazione può andare sotto 100 in seguito ad una aumento generale dei tassi d’interesse (o del rischio di insolvenza) sulle nuove obbligazioni emesse: **le vecchie obbligazioni con tassi d’interesse minori garantiscono annualmente dei ritorni minori** che vengono compensati con il premio finale.

#### Alla pari
Acquisto a 100. L'obbligazione ha una cedola uguale ai tassi del mercato: al termine riceverò quanto versato ma prendo delle cedole pari ai tassi.

#### Sopra la pari
Il **prezzo** di un’obbligazione sia superiore a 100, quindi sopra la pari: questo succede **nel caso in cui l’obbligazione garantisca una cedola più alta rispetto alle altre obbligazioni in circolazione**.
Preferisco quindi perderci sulla valutazione finale (acquisto a 120 esempio e alla fine avrò 100) per avere una cedola più alta della media.
Una obbligazione può andare sopra 100 in seguito ad una discesa generale dei tassi d’interesse sulle nuove obbligazioni emesse: **le vecchie obbligazioni con tassi d’interesse maggiori garantiscono annualmente dei ritorni maggiori**.

### Rendimenti
Nelle obbligazioni i rendimenti ci sono in due modi: con le cedole periodiche e il conto capitale (differenza tra quanto abbiamo pagato l'obbligazione e quanto ho preso alla fine).
#### Tasso di rendimento
Il tasso di rendimento (*Yield-to-Maturity*) è quel tasso che rende equivalenti i pagamenti futuri al prezzo pagato in partenza.
Se il prezzo pagato per comprare il bond è uguale al capitale restituito a scadenza, ossia il suo valore nominale (=100), il tasso di rendimento sarà uguale al tasso d’interesse. Mentre **se il prezzo pagato è inferiore, il tasso di rendimento sarà maggiore del tasso d’interesse e viceversa**.

Per le obbligazioni a tasso variabile indicizzate all'inflazione (come il BTP italia) il calcolo del rateo non è una operazione semplice, si può vedere come si può fare qui: [[Calcolo rateo BTP Italia]].

## Obbligazioni e ETF
Le obbligazioni sono emesse da governi o aziende, nel primo caso tendenzialmente sono più sicure. Il secondo punto è il rating delle obbligazioni, quindi il rating che le agenzie di rating danno allo stato che emette tali obbligazioni. Più il rating è buono più l’interesse sarà basso, in quanto l’investimento risulta più sicuro. Le obbligazioni Junk, sotto il livello chiamato *Investment Grade* sono invece le obbligazioni considerate non sicure, quindi tipicamente con u interesse più alto. Il termine *Investment Grade* indica la bontà delle obbligazioni in questione, se nella descrizione dell’ETF ci sono termini come “sub investment grade” o “jnk” significa che si tratta di obbligazioni di stati instabili.

## Obbligazioni famose
### BOT
I Buoni Ordinari del Tesoro (BOT) sono **obbligazioni zero coupon in quanto non hanno cedole e sono di breve durata** in quanto possono avere durata trimestrale, semestrale oppure annuale e rappresentano un modo immediato per lo Stato per far fronte alle proprie esigenze di cassa.
Le emissioni di nuovi titoli di Stato (BOT compresi) avvengono tramite le cosiddette aste pubbliche che vengono annunciate [qui](http://www.dt.mef.gov.it/it/debito_pubblico/titoli_di_stato/aste_titoli_di_stato/).
Per vedere i BOT che sono acquistabili basta vedere il sito di Borsa Italiana nella [sezione apposita](https://www.borsaitaliana.it/borsa/obbligazioni/mot/bot/lista.html); dato che sono degli zero coupon per capirne il rendimento lordo basta confrontare il loro prezzo attuale (colonna "ultimo") con 100. Esempio se il prezzo è 98 significa che hanno un rendimento del 2% netto da oggi alla scadenza.
Il loro nome comprende tipicamente la digitura "Zc" che indica appunto "zero coupon".
La cosa comoda dei bot è che, a meno che lo stato italiano non subisca degli attacchi speculativi, il loro prezzo tenderà a salire sempre in modo lineare fino a raggiungere i 100 alla scadenza. Posso quindi **venderli quando voglio senza paura di perdere soldi**.
### CCT
I Certificati di Credito del Tesoro sono titoli con scadenza superiore ai 24 mesi con cedole di tipo variabile.
Sono consigliabili in periodi di forti rialzi dei tassi d’interesse.
### BTP
I Buoni del Tesoro Poliennali sono titoli con cedole semestrali e tasso d’interesse fisso.
Le scadenze arrivano anche a 60 anni , e rappresentano un investimento corretto se si pensa di non aver bisogno del capitale investito, prima della scadenza.

### Btp Italia (indicizzati all'inflazione)
Esiste una categoria di BTP che offrono **rendimenti indicizzati all'inflazione**, un esempio è il btp italia nv28 con isin IT0005497000.
Questi BTP hanno un cedola definita a priori (es. 1.60%) che **può aumentare in base all'inflazione corrente**.
Dato che hanno cedola variabile il loro valore è sempre intorno a 100 e vanno benissimo come alternativa al contante nel fondo di emergenza.
Non può scendere sotto il suo valore iniziale anche in caso di deflazione.
Assumiamo di avere 1.60% di cedola iniziale, ogni sei mesi ti verrà corrisposta una cedola pari a metà del tasso annuale (quindi almeno lo 0.80%) rivalutata in base all'inflazione calcolata: poniamo che investi mille euro: se dalla cedola precedente l'indice dei prezzi è salito dell'1% ti verrà corrisposto almeno lo 0.8(1+0.01) = 0.808% di quello che hai investito, quindi otto euro e otto centesimi, mentre se è salito del 5% ti verrà corrisposto almeno il 0.8 * 1.05 = 0.84%, quindi otto euro e quaranta centesimi e così via.
Insieme alle cedole semestrali, ti viene anche versata **la rivalutazione del capitale**. Quindi oltre a quello detto sopra, se dalla cedola precedente l'indice è salito dell'1% ti arrivano anche dieci euro extra, se è salito del 5% te ne arrivano cinquanta e così via.

## Esempio 

Prendiamo il BTP IT0003934657: questo è stato emesso il 01/08/2005 con scadenza 01/02/2037 con un tasso del 4% annuo che viene versato in due cedole, il 1° febbraio e il 1° agosto di ogni anno.
Questo è il grafico, commentato, negli ultimi 5 anni:
![[Pasted image 20221109152256.png]]
Come si vede il prezzo di quotazione del BTP varia in modo inversamente proporzionale all'aumento dei tassi. Questo perché la cedola è fissa e questa è più o meno conveniente in base al mercato.
Ho effettuato un ordine di 5 BTP (valore nominale 5000€) con la mia banca, cerchiamo di capire il prospetto indicato:
![[Pasted image 20221109153538.png]]

### Denominazione
Nome dell'obbligazione, in questo caso BTP 01/02/2037 4%.

### Controvalore EUR
$$Numero\_obbligazioni * Quotazione\_corrente$$
Nel mio caso ho quindi
$$5000 * (96.140 / 100) = 4807\unicode{x20AC}$$

### Quantità
Questo valore indica il numero di bond in possesso per il loro taglio (quasi sempre 1000€). Quindi 5000 indica che ho 5 BTP dal valore di 1000€ l'uno anche se non è detto che li abbia pagati 5000€, anzi: li ho pagati il prezzo medio in percentuale * 5000 quindi $5000*0.95475 = 4773.75\unicode{x20AC}$.

### Quotazione
Prezzo corrente espresso in centesimi (96.140) alla data 09/11/2022.

### Prezzo medio
Prezzo medio di acquisto del titolo (95.475). E' una media in quanto io potrei aver acquistato tale titolo in varie occasioni e quindi a vari prezzi, questo valore ne indica la media.

### Profitto
Differenza la quotazione corrente e il prezzo medio di acquisto: $96.140 - 95.475 = 0.665$ (arrotondato nell'immagine a 0.7).
La sua conversione in euro si ha:
$$5000*(0.96140-0.95475) = 33.25\unicode{x20AC}$$

### Rateo
Il rateo indica l'ammontare di interesse accumulato dall'ultima cedola.
Il rateo è proporzionale al periodo di tempo trascorso:
$$Rateo = Cedola * \frac{giorni\_effettivi}{giorni\_totali}$$.
In questo caso l'obbligazione rende il 4% annuo con due cedole da 2% l'una fornite il 1°Febbraio e il 1°Agosto.
Oggi è il 09/11/2022 e la cedola scorsa è stata il 01/08/2022.
Il numero di giorni passati dalla scorsa cedola è stato 101 giorni e il numero di giorni totali della cedola 01/08/2022-02/02/2023 = 186 giorni.
$$Rateo = 2 * \frac{101}{186} = 1.086$$.

Dal 01/08 ho quindi accumulato l'1.086%.

### Riassunto
Ricapitolando ho quindi acquistato speso 4773.75€ per acquistare 5 BTP del valore nominale di 5000€ a scadenza 01/02/2037.
Questi renderanno il 4% lordo annuo, quindi 200€ all'anno e in particolare 100€ lordi al bimestre.
Inoltre a scadenza riceverò 5000€, con un guadagno extra di 226.25€ rispetto al prezzo pagato inizialmente.
Per esempio oggi è il 09/11/2022 e al 01/02/2037 mancano 14 anni e 2 mesi, complessivamente riceverò 2900€ (2800+100€ rateo corrente) lordi + 226.25€ = 3126.25€.
Di questi il 12.5% va in tasse quindi $3126.25 - (3126.25*0.125)=2735.46\unicode{x20AC}$.
Posso inoltre rinunciare a questo rendimento quando voglio vendendo il BTP al prezzo corrente. Per esempio se scommetto in una riduzione dei tassi il suo prezzo aumenterà sopra 100 e posso venderlo ottenendo una plusvalenza.

## Acquisto BTP Italia su Directa
Il 14/11/2022 è stato emesso un nuovo BTP con delle regole particolari: oltre alla cedola fissa del 1.6 ho anche un extra cedola che dipende dall'inflazione e che va direttamente sul conto capitale.
Quindi se ho un'inflazione del 5% riceverò come cedola il 5% del conto capitale oltre all'1.6%.
Questo BTP (ISIN IT0005517187) dura 6 anni e, se acquistato all'emissione, ha commissioni 0.
Vediamo come comprarlo all'emissione su Directa.
Cercando l'ISIN compare questa schermata:
![[Pasted image 20221114215614.png]]
Il prezzo è fisso a 100 e non c'è mercato in quanto nessuno vende tranne lo stato a prezzo imposto.
Il taglio è 1000€, per acquistarne 1 basta mettere "1000" nella voce "quantità" (anche se non è una vera quantità con i BTP funziona così).
![[Pasted image 20221114215759.png]]
Premendo su "Compra" compare la schermata riassuntiva con il prezzo che andrò a pagare:
![[Pasted image 20221114215826.png]]
Come si vede non ho commissioni e andrò a pagare 1000€.
Dato che ora il mercato è chiuso l'ordine è stato solo immesso e diventerà operativo solo all'apertura del mercato:
![[Pasted image 20221114215948.png]]



## Spreadsheet
Per calcolare il rendimento di una obbligazione posso utilizzare la formula per il calcolo del [[Tasso interno di rendimento (TIR)]] di Excel, che è `XIRR`.

