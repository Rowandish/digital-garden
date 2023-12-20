---
tags:
  - Coding
  - PublishedPosts
---


Questo lungo articolo è una parziale traduzione delle pagine trovate in http://www.regular-expressions.info/ e copre i principali argomenti riguardo le espressioni regolari, senza andare nel dettaglio del loro funzionamento interno.
Per prima cosa, definiamo una espressione regolare come **una stringa che identifica un insieme di stringhe**.

## 1. I caratteri letterali
La più semplice espressione regolare è un singolo carattere, come per esempio **a**, che trova la prima occorrenza di tale carattere nella stringa in ingresso.
Per esempio nella stringa
```perl
Jack is a boy
```
Rileva il carattere **a** dopo la **J**: il fatto che la **a** sia in mezzo ad una parola non è importante per il parser delle regexp. Nel caso in cui invece questa cosa sia importante è necessario utilizzare i _word boundaries_ a cui rimando alla sezione successiva.
E' importante segnalare come la regex può rilevare anche **la seconda a** all'interno della stringa, a patto di comunicare all'engine di andare oltre il primo match.
Posso anche concatenare più caratteri consecutivamente, per esempio con la regex **boy** trovo la stringa _boy_, per il motore regex è come scrivere: _trova la lettera b, seguita successivamente dalla lettera o ed infine dalla lettera y_.
Segnalo infine come le regex siano sempre **case sensitive**, a meno che non venga settata un opzione diversa.

## 2. I caratteri speciali
Esistono 12 caratteri che hanno un significato speciale nelle regex (metacaratteri), se voglio indicarli quindi come il carattere che questi rappresentano effettivamente devo anteporre un backslash.
Ecco l'elenco con spiegazione

| Matacarattere | Significato |
|--------|--------|
|`\`||
|`^`|Rileva la posizione all'inizio della stringa|
|`$`|Rileva la posizione alla fine della stringa|
|`.`|Rileva qualsiasi carattere (tranne `\n`)|
|`pipe`|Alternativa (OR)|
|`?`|Quantificatore: tra *0* e una volta|
|`*`|Quantificatore: tra *0* e *n* volte|
|`+`|Quantificatore: tra *1* e *n* volte|
|`{min, max}`| Quantificatore: tra min e max volte|
|`()`|Gruppo di cattura|
|`[]`|Insieme di caratteri|
|`\b`|Limite di parola|
|`\B`|Trova tutte le posizioni non rilevate da **\b**|

Inoltre aggiungere un backslash prima di un singolo carattere può essere un [[Token]] con un ulteriore significato, di seguito l'elenco dei più usati.

| [[Token]] | Notazione estesa |Significato |
|--------|--------|--------|
|`\d`|`[0-9]`|numero da 0 a 9|
|`\D`|`[^0-9]`|Carattere che non è un numero da 0 a 9|
|`\w`|`[A-Za-z0-9_]`|lettera di una parola|
|`\W`|`[^A-Za-z0-9_]`|Carattere che non è una lettera di una parola|
|`\s`|`[ \t\r\n\f]`|Caratteri invisibili di formattazione|
|`\S`|`[^ \t\r\n\f]`|Carattere che non è un carattere invisibili di formattazione|

## 3. Insieme di caratteri
Spesso si incontra il problema di dover rilevare una stringa che contenga solo uno di un insieme di caratteri. Questo viene risolto utilizzando le parentesi quadre, per esempio l'espressione regolare **gr[ae]y** rileva sia _gray_ che _grey_

| Espressione | Significato |
|--------|--------|
|`[ae]`|Rileva il carattere **a** o il carattere **b**|

Posso estendere questa funzionalità con il carattere **-** per indicare un **range di caratteri**. Posso usare anche più di un range concatenati fra loro e indicare sia range che singoli letterali nello stesso insieme.
Conseguentemente avrò

| Espressione | Significato |
|--------|--------|
|`[0-9]`|Singolo numero compreso tra 0 e 9]
|`[0-9a-fA-F]`|Rileva un qualsiasi valore esadecimale|
|`[0-9xa-fA-F]`|Rileva un qualsiasi valore esadecimale o la lettera _x_|

All'interno di un insieme di caratteri i metacaratteri perdono di significato, conseguentemente possono essere inseriti senza backslash.

| Espressione | Significato |
|--------|--------|
|`[*+]`|Rileva il carattere ***** o il carattere **+**|

### 3.1 Negare un insieme di caratteri
Inserendo un accento circonflesso subito dopo la parentesi quadra aperta, **nega l'insieme di caratteri definito**. A differenza del punto (che vedremo in seguito), gli insiemi di caratteri negati matchano anche gli invisibili caratteri di interruzione riga.
Esempi:

| Espressione | Significato |
|--------|--------|
|`[^0-9]`|qualsiasi carattere non numerico|
|`[^0-9\r\n]`|qualsiasi caratttere non numerico e non senza line breaks|

Segnalo che un insieme di caratteri negato deve comunque fare il match con un carattere: l'espressione **q[^u]** non significa "*una q non seguita da una u*" ma significa "*una q seguita da un carattere che non è una u*".
Conseguentemente la **q** della stringa _Iraq_ non verrà considerata, mentre lo sarà la **q** della stringa _Iraq is a country_ in quanto lo spazio viene considerato come carattere. Per risolvere questo problema è necessario utilizzare i *negative lookahead* (`q(?!u)`), che verranno spiegati nel capitolo dedicato.

Inserendo un accento circonflesso **^** dovunque eccetto subito dopo la parentesi quadra aperta **[**, questo viene considerato come un normale letterale, per esempio **[x^]** esegue il match di una **x** o di un **^**.

### 3.2 Ripetere un insieme di caratteri
Ripetendo gli insiemi di caratteri con gli operatori **?**, ***** o **+**, sto ripetendo l'intero insieme di caratteri, non il singolo carattere che viene trovato. Se voglio questo comportamento devo usare le backreferences.

| Espressione | Significato |
|--------|--------|
|`[0-9]+`|Trova qualsiasi numero ripetuto una o più volte|
|`([0-9])\1+`|Trova lo stesso numero trovato dall'insieme una o più volte|

### 3.3 Sottrarre insiemi di caratteri
Le espressioni regolari permettono (non in tutti i linguaggi) di trovare il match di un qualsiasi carattere presente in una lista che **non è presente in una seconda lista**.
La sintassi è la seguente
```perl
[class-[subtract]]
```
| Espressione | Significato |
|--------|--------|
|`[a-z-[aeiuo]]`|Trova una qualsiasi lettera che non sia una vocale|

#### 3.3.1 Sottrazioni di insiemi di caratteri innestate
E' possibile eseguire sottrazioni di sottrazioni tra insiemi di caratteri, per esempio le seguenti tre espressioni sono analoghe.

| Espressione originale | Prima elaborazione | Seconda elaborazione|
|--------|--------|--------|
|`[0-9-[0-6-[0-3]]]`|`[0-9-[4-6]]`|`[0-37-9]`|

La sottrazione **deve** sempre essere l'ultima elemento nell'insieme di caratteri, altrimenti è errore di sintassi.

### 3.4 Interesezione tra insiemi di caratteri
Analogamente alla sottrazione, è possibile anche l'interserzione tra più insiemi di caratteri. La sintassi è
```perl
[class&&[intersect]]
```
| Espressione | Significato |
|--------|--------|
|`[a-z&&[^aeiuo]]]`|Trova una qualsiasi lettera che non sia una vocale|
Analogamente alla sottrazione, posso anche concatenare intersezioni

## 4. Il metacarattere punto
Il carattere punto rileva un singolo carattere qualsiasi **tranne i caratteri di interruzione di riga \n** .
Per illustrare il suo comportamento illustriamo un esempio: vogliamo rilevare una data nel formato _mm/dd/yy_ indipendentemente dal tipo dei separatori.
La soluzione rapida è la seguente
```perl
\d\d.\d\d.\d\d.
```
che correttamente rileva *02/12/03* e *02-12-03*. Il problema è che rileva anche *02512703*, comportamento non voluto.
Una soluzione migliore è sicuramente la seguente (ricordo che all'interno degli insiemi di caratteri il punto perde il suo significato di metacarattere).
```perl
\d\d[- /.]\d\d[- /.]\d\d
```
L'espressione è ancora lontana dall'essere corretta, in quanto rileva come data corretta anche _99/99/99_.
Devo conseguentemente evitare l'uso di **\d** per il giorno e il mese, ottenendo quidni l'espressione seguente
```perl
[01]\d[- /.][0-3]\d[- /.]\d\d
```

### 4.1 Insiemi di caratteri negati invece del punto
Spesso negare un insieme di caratteri è più appropriato dell'uso del punto.
Consideriamo il seguente esempio, assumiamo di voler rilevare una stringa contenuta da due virgolette. La prima soluzione che viene in mente è la seguente
```perl
".*"
```
Utilizzando l'espressione nella frase *Put a "string" between double quotes* tutto sembra funzionare, ma se invece la stringa in ingresso è *Houston, we have a problem with "string one" and "string two"* l'espressione rileva *"string one" and "string two"*, che è un comportamento non voluto.
Questo perchè il carattere ***** è _greedy_ (per approfonire vedi capitolo seguente). Analogamente a quanto abbiamo fatto con le date nella sezione precedente, la soluzione è sostituire il punto con un insieme di caratteri negato, in questo caso con
```perl
"[^"\s]*"
```
Che indica che voglio ogni carattere che non è una virgoletta o carattere invisibile.

## 5. Ancore
Le ancore non eseguono un match di una lettera, ma di una **posizioone**, in particolare possono indicare **prima**, **dopo** o **tra** caratteri..
Le due ancora più importanti sono il carattere **^** e **$**, in particolare **^** indica la posizione **prima** del primo carattere della stringa, mentre **$** dopo l'ultimo.

| Espressione | Significato |
|--------|--------|
|`^a`|Trova una stringa che comincia con _a_|
|`c$`|Trova una stringa che finisce con _c_|

### 5.1 Applicazioni utili
Assumiamo di voler validare l'input dell'utnete, che deve essere un numero, quindi una stringa formata da solo cifre. Usare l'espressione **\d+** è sbagliato, in quanto, per esempio, la stringa *qsdf4ghjk* viene correttamente rilevata in quanto presenta il carattere _4_.
Il modo migliore è il seguente

| Espressione | Significato |
|--------|--------|
|`^\d+$`|Trova una stringa formata solo da numeri|


## 6. Word Boundaries
Il metacarattere **\b** è un'ancora, analogamente al **^** o al **$**, non indica un carattere ma rileva una posizione, cioè il limite di parola.
Ci sono tre differenti posizioni che qualificano un limite di parola
- Prima il primo carattere nella stringa, se il primo carattere è un **\w**
- Dopo l'ultimo carattere della stringa, se questo è un **\w**
- Tra due caratteri della stringa, in cui uno è un **\w** e l'altro è un **\W**.

Scrivendo questi punti nel linguagguio delle espressioni regolari, possiamo quindi scrivere che il metacarattere **\b** è analogo a **(^\w|\w$|\W\w|\w\W)**.

Per esempio l'espressione **\b4\b** indica un 4 che non è parte di un numero più grande. Per esempio, tale espressione non trova i **4** nella stringa *44 sheets of a4*

| Espressione | Significato |
|--------|--------|
|`\bis\b`|Trova la parola *is* non all'interno di una altra parola.|

## 7. Creare degli OR con il pipe
E' possibile indicare più espressioni regolari e inserirle in OR tramite il comando di pipe **|**, in questo modo è possibile rilevare le stringhe che eseguono il match di un'espressione o dell'altra.
Per esempio, se voglio cercare tutte le stringhe _dog_ o _cat_, devo semplicemente separare le due regexp con una pipe: **cat|dog**.
L'operatore di OR ha la precedenza minore tra tutti gli operatori. Se voglio modificare questo comportamento devo aggiungere delle parentesi per raggruppare le operazioni.
Volendo estendere il primo esempio a rilevare solo le parole _cat_ o _dog_ devo aggiungere delle ancora di _word boundaries_, in particolare scrivendo **\b(cat|dog)\b**.

## 8. Il quantificatore esisteziale ?
Per indicare un elemento che può esistere o meno all'interno di una espressione utilizzo il punto di domanda **?**, chiamato **quantificatore esistenziale**.

| Espressione | Significato |
|--------|--------|
|`colou?r`|Rileva sia *colour* che *color*|
|`Nov(ember)?`|Rileva sia *Nov* che *November*|

Il quantificatore **?** è _greedy_ che significa letteralmente _avido_, questo significa che fornisce al motore di espressioni regolari due scelte:
- Prova a trovare la parte a cui si applica il **?**
- Non provare ad eseguirne il match

In parole povere, si cerca sempre di trovare l'espressione che soddisfa il **?** e, solo se questa non viene trovata, si procede con la sua rimozione.
Per esempio, assumiamo di avere l'espressione **Feb 23(rd)?** da applicare alla stringa *Today is Feb 23rd, 2003*. L'espressione troverà **sempre** _Feb 23rd_ e mai _Feb 23_.

## 9. Ripetizioni di [[Token]] (* e +)
Nella sezione 8. abbiamo parlato del quantificatore esistenziale **?** che indica di eseguire il match zero o una volta.
L'asterisco ***** comunica invece di rilevare il [[Token]] precedente 0 o più volte, mentre il più **+** una o più.
Per esempio la seguente espressione regolare
```perl
<[A-Za-z][A-Za-z0-9]*>
```
Rileva tutti i tag HTML considerando il fatto che cominciano con una lettera e sono formati dal almeno un carattere.

### 9.1 Limitare le ripetizioni
Esiste un ulteriore quantificatore che permette di limitare il numero volte in cui un [[Token]] può essere ripetuto.
La sintassi è `{min,max}` dove `min` è un numero compreso tra 0 e un intero positivo ed indica il numero minimo di match, mentre `max` è un intero maggiore o uguale a `min`.
Esiste anche la sintassi `{min,}` che indica che il massimo è infinito.
Rimuovendo anche la virgola indico che il [[Token]] deve essere ripetuto esattamente `min` volte.

| Limitatori | [[Token]] analoghi |Significato |
|--------|--------|--------|
|`{0,1}`|`?`| *0* o una volta|
|`{0,}`|`*`| *0* o *n* volte|
|`{1,}`|`+`| *1* o *n* volte|
|`{min}`|| Esattamente *min* volte|

### 9.2 Greedy o lazy?
Lavorando con le espressioni regolari spesso si incontra il seguente problema:
assumiamo di analizzare una espresssione come `This is a <EM>first</EM> test` e di volerne rilevare i tag.
Di primo achito si potrebbe pensare ad una espressione analoga alla seguente:
```perl
<.+>
```
aspettandosi di trovare come risultato `<EM>` e `</EM>`, ma questo **non** succede; il risultato ottenuto sarà *<EM>first</EM>* che non è quanto ci aspettevamo.
Il motivo che il quantificatore **+** è _greedy_ (ingordo) che significa che il [[Token]] di riferimento verrà ripetuto **il maggior numero di volte possibile**.
Analogamente al **+**, anche l'asterisco e le ripetizioni **{min, max}** sono greedy.
Il contrario del termine _greddy_ è _lazy_ (pigro), esiste un semplice trucco per trasformare un quantificatore da greedy a lazy: insere un punto di domanda.
Per esempio l'espressione indicata sopra diventa
```perl
<.+?>
```
rilevando così quanto richiesto.

| Espressione | Significato |
|--------|--------|
|`(regexp)?`|Quantificatore esistenziale _greedy_|
|`(regexp)??`|Quantificatore esistenziale _lazy_|

## 10. Raggruppamenti
Inserendo parti di espressioni regolari all'interno di parentesi, è possibile raggruppare tale regexp insieme, in modo da poterci applicare quantificatori o pipe, inoltre posso riprendere tali raggruppamenti successivamente nella stessa regexp (backreferences).
Talvolta può rislutare utile, per chiarezza, distinguere i gruppi che sono indicati per catturare espressioni (per backreferences o sostituzioni) da quelli invece indicati per poterci applicare dei quantificatori.
Indicando un punto di domanda **?** seguito da un due punti **:** subito dopo la parentesi tonda aperta che identifica il gruppo, indica che tale gruppo di **non raggruppamento**.

| Espressione | Significato |
|--------|--------|
|`Set(Value)?`|Le parentesi servono per il **?** ma sono anche gruppo di cattura|
|`Set(?:Value)?`|Le parentesi servono per il **?** ma il contenuto non viene catturato|

### 10.1 Backreferences
Una backreferences trova lo stesso testo rilevato in precedenza da un gruppo di cattura.
Assumiamo di voler trovare una coppia di tag HTML e il testo presente al loro interno.
Inserendo il tag di apertura in un gruppo di cattura, posso riutilizzare tale nome per rilevare il tag di chiusura.
L'espressione per eseguire questo è la seguente:
```perl
<([A-Z][A-Z0-9]*)\b[^>]*>.*?</\1>
```
Le parentesi rilevano **[A-Z][A-Z0-9]*** che è il tag HTML di apertura, mentre la backreference **\1** si riferisce al primo gruppo di cattura, in particolare rileva **lo stesso testo trovato dal primo gruppo**. Conseguentemente non è equivalente a riscrivere la stessa espressione regolare due volte:

| Espressione | Significato |
|--------|--------|
|`<([A-Z][A-Z0-9]*)\b[^>]*>.*?</[A-Z][A-Z0-9]*>`|Il tag di apertura e chiusura possono essere diversi|
|`<([A-Z][A-Z0-9]*)\b[^>]*>.*?</\1>`|Il tag di apertura e chiusura devono essere gli stessi|

Un ulteriore esempio è il rilevamento delle parole duplicate, per esempio voglio rilevare tutte le volte che ho inserito per sbaglio due volte la stessa parola vicina nello stesso testo.

| Espressione | Significato |
|--------|--------|
|`\b(\w+)\s+\1\b`|Rileva una parola `\w+` seguita da uno o più spazi `\s+` seguito dalla stessa parola `\1`|

### 10.2 Forward References
Nei moderni parser per regex, è possibile eseguire anche la forward reference, cioè referenziare un gruppo che appare successivamente nell'espressione. Queste sono utili solo se sono all'interno di un gruppo ripetuto: prendiamo per esempio la seguente espressione
```perl
(\2two|(one))+
```
e proviamo a fare il match con **oneonetwo**.
Analizziamo il comportamento del motore per regex: per prima cosa prova a trovare `\2`, che non esiste e conseguentemente fallisce. Prova la seconda alternativa, che invece ha successo, portando quindi il secondo gruppo `\2` valorizzato a *one*. Ora il gruppo viene ripetuto e `\2` correttamente trova il secondo *one*.
Ricordo che non tutti supportano il *Forward References*, un esempio famoso è Javascript.

## 11. Lookahead e Lookbehind
*Lookahead* e *lookbehind* (chiamati *lookaround*) sono degli asserti a lunghezza zero analogamente a *inizio/fine riga* e *inizio/fine parola*.
La differenza fondamentale è che i lookaround forniscono solo il risultato del match: true e false. Indicano se un match è possibile o meno ma **non ritornano il risulato del match e non "consumano" caratteri nella stringa**.
#### 11.1 Lookahead positivi o negativi
I lookahead negativi sono indispensabili se voglio rilevare qualcosa che **non è seguito da qualcosa d'altro**. La loro sintassi è la seguente:
```perl
(?!regexp)
```
I lookahead positivi al contrario rilevano qualcosa **che è seguito da qualcosa d'altro** e la sintassi è
```perl
(?=regexp)
```
Ora analizziamo il loro comportamento con l'aiuto della seguente tabella:

| Test | Espressione | Significato | Match |
|--------|--------|--------|--------|
| _quit_ |`q(?=u)`|_q_ seguita da _u_ (che non partecipa al match)| TRUE |
| _quit_ |`q(?=u)i`|_q_ seguita da _u_ (che non partecipa al match) e _i_| FALSE |
| _quit_ |`q(?=u)ui`|_q_ seguita da _u_ (che non partecipa al match), _u_ e _i_| TRUE |
| _q uit_ |`q(?!u)`|_q_ seguita da non _u_ (che non partecipa al match)| TRUE |
| _q uit_ |`q(?!u)u`|_q_ seguita da non _u_ (che non partecipa al match) e _u_| FALSE|
| _q uit_ |`q(?!u) u`|_q_ seguita da non _u_ (che non partecipa al match), _spazio_ e _u_| TRUE |
Ho sottolineato pià volte il fatto che i _lookahead_ non partecipano al match in quanto è questo il punto fondamentale per capire se un match verrà eseguito o meno.

### 11.2 Lookbehind positivi o negativi
Lookbehind ha lo stesso effetto, ma lavorando all'indietro, conseguentemente rilevano un oggetto che **è (o non è) preceduto da qualcun altro, senza che questo partecipi effettivamente al match**.
La sinatssi per il *lookbehind negativo* è
```perl
(?<!text)
```
mentre per il positivo è
```perl
(?<=text)
```

### 11.3 Esempio complesso
I _lookaround_, per quanto potenti, spesso sono usati in maniera sbagliata in quanto sono zero-length e il risultato che trovano **non partecipa al match**.
Consideriamo il seguente esempio: vogliamo trovare una parola che sia lunga sei lettere e che contanga le tre lettere consecutive "_cat_".
Volendo possiamo scrivere l'espressione senza utilizzare un _lookaround_, basta specificare tutte le opzioni possibili ed unirle in OR.
```perl
cat\w{3}|\wcat\w{2}|\w{2}cat\w|\w{3}cat
```
Questo sistema funziona quando devo rilevare qualcosa di semplice, ma se assumiamo per esempio di dover trovare una parola compresa tra 6 e 12 caratteri che contiene o "cat" o "dog" o "mouse" l'espressione diventa incredibilmente lunga e complicata.
Il modo corretto per eseguire questo match è utilizzare i lookaround.
Analizziamo l'esempio: abbiamo due requisiti che devono essere soddisfatti:

- trovare una parola che sia lunga esattamente sei lettere (`\b\w{6}\b`)
- la parola deve contenere esattamente la sringa "cat" (`\b\w*cat\w*\b`).

Per combinare le due espressioni utilizzo il lookaround positivo nella seguente espressione
```perl
(?=\b\w{6}\b)\b\w*cat\w*\b
```
Il trucco è proprio sul fatto che i _lookaround_ sono match a lunghezza zero.
In questo caso il `(?=\b\w{6}\b)` serve per **filtrare** tutte le stringhe che sono formate da esattamente 6 caratteri di parola `\w`, una volta che questa espressione ritorna TRUE, allora posso proseguire con la seconda parte (**che inizierà il match dall'inizio della stringa**). I questo modo la seconda parte della regexp (`\b\w*cat\w*\b`) verrà lanciata solo sulle stringhe formate da sei caratteri, ottenendo così il risultato desiderato.
Riprendendo l'esempio indicato prima (trovare una parola compresa tra 6 e 12 caratteri che contiene o "cat" o "dog" o "mouse") l'espressione è la seguente
```perl
\b(?=\w{6,12}\b)\w{0,9}(cat|dog|mouse)\w*
```
### 11.4 Clausola IF-THEN-ELSE
Esiste un costrutto speciale (`(?ifthen|else)`) per creare espressioni regolari condizionali. Se la parte **if** fornisce true, allora il motore proverà a eseguire il match con il **then**, altrimenti con l'**else**.
Per la clausola **if**, devo utilizzare una espressione di _lookaround_, per esempio:
```perl
(?(?=regex)then|else)
```
Espressioni più complesse possono essere usate con la clausola OR, come nell'esempio seguente
```perl
(?(?=condition)(then1|then2|then3)|(else1|else2|else3))
```