---
tags:
  - Learning
  - PublishedPosts
---
## Introduzione
Lo spaced repetition è una tecnica di memorizzazione che consiste di ripassare quanto imparato a intervalli variabili nel tempo in base a quanto si sa tale concetto.
Questo approccio è l'opposto del "cramming" che consiste nel riempire il cervello di informazioni tutte insieme, magari i giorni prima di un test, per poi dimenticare tutto.
A quanti di noi è successo di non sapere nulla di un determinato argomento dopo solo pochi mesi da un esame?
Lo spaced repetition invece permette di memorizzare anche centinaia di migliaia di elementi (utilissimo per imparare lingue straniere per esempio) massimizzando il rapporto tempo/apprendimento puntando a spostare l'informazione dalla memoria a breve a quella a lungo termine.

## Funzionamento
Assumiamo di avere una parola in inglese da imparare, per esempio *awkward* e abbiamo un numero finito di volte in cui possiamo ripassarla (mettiamo 5).
La parola sarà imparata davvero se distribuisco i 5 ripassi su un lungo periodo, per esempio settimane o mesi rispetto a utilizzare tutti i 5 ripassi nel giro di un giorno o due.
Questo perché la [forgetting curve](https://en.wikipedia.org/wiki/Forgetting_curve) è un esponenziale decrescente, un po' come il decadimento di una sostanza radioattiva:

![[forgetting-curve-stahl.jpg]]
Se viene effettuato il ripasso (in inglese *recall*) dopo pochi giorni questa non serve a molto in quanto l'informazione è ancora nel cervello, la memoria non è deteriorata molto.

Il momento migliore del recall è poco prima che tale informazione sia dimenticata.

Il punto è: come faccio a ricordarmi di ripassare un concetto se me lo sto dimenticando? Posso rivedere solo cose che ho in memoria, e che quindi non le sto dimenticando.
**La soluzione è delegare un computer nei calcoli di quando farmi fare il recall del concetto.**

Questa è la base di tutti i software di spaced repetition: delegargli il calcolo degli intervalli di tempo crescenti ai quali fornirmi le informazioni da ripassare; all'inizio la recall verrà effettuata frequentemente per fissare il concetto, e poi aumentare a settimane e anche mesi.
Una volta che l'informazione è passata dalla memoria a breve termine a quella a lungo termine basta una recall occasionale per fissare il concetto.

## Spaced repetition con Obsidian
[Obsidian](https://obsidian.md/) è un tool fantastico, credo farò altri articoli perchè negli ultimi mesi mi sono veramente innamorato: permette di organizzarsi, imparare, gestire task, fare da CRM, costruirsi una second brain... Guardatelo.
Tra i vari community plugin disponibili ce ne è [uno dedicato proprio alla spaced repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) il quale permette di creare degli insiemi (chiamati *deck*) di microconcetti (chiamati *flashcards*) da imparare.
La review delle cards o dei concetti avviene in modo incrementale in base a quanto conosco il concetto (conosco bene, prossima review lontana, conosco male, prossima review vicina) e quanto tempo fa ho effettuato la precedente review.
In particolare dopo la review di ogni concetto questo viene marcato come:
- `Hard`: non ricordo la risposta (prossima recall a breve)
- `Good`: ricordo bene la risposta (prossima recall fra un po')
- `Easy`: ricordo senza alcun problema la risposta (prossima recall fra molto tempo)

### Deck
Una nota può essere indicata come "deck" contenente *n* flashcards. Per indicare che una nota è un deck è necessario aggiungere il tag `#flashcards`.
Esiste anche il concetto di subdeck, basta utilizzare il tag
`#flashcards/subdeck/subdeck`.

### Flashcards
Una nota può contenere una o più flashcard, la quale può essere creata in vari modi:

#### Single-line Basic
La domanda e la risposta possono essere separate da `::` (configurabile).
`the question goes on this side::answer goes here!`

#### Single-line Reversed
In questo caso creo due cards: `side1:::side2` e `side2:::side1`
La domanda e la risposta possono essere separate da `:::` (configurabile).
`the question/answer goes on this side:::question/answer goes here!`

#### Multi-line Basic
Questo metodo è comodo per creare cards lunghe, il separatore è il `?` e con il doppio `??` ho il reverse come sopra.

#### Cloze cards
E' possibile creare anche cloze deletion cards (la *cloze deletion* è una frase dove del testo importante è sostituito da "..." e tale frase è il testo da indovinare).
In questo caso il testo evidenziato o in grassetto diventa una cloze deletion (nei setting posso indicare se voglio solo l'evidenziato o solo il grassetto).

### Review
Premendo l'icona apposita in Obsidian è possibile iniziare la review delle card.
La schermata che compare è analoga a questa:

![[Pasted image 20221017111216.png]]
Dove sono presenti i vari *deck* che sono i contenitori di flashcards da ripassare, nel mio caso parole ed espressioni in inglese che voglio apprendere,
Cliccando su un *deck* verrà mostrata il concetto con la "risposta" nascosta. Sarò io a dover dichiarare quanto conosco il concetto.
![[Pasted image 20221017111719.png]]

![[Pasted image 20221017111839.png]]

In base alla mia risposta verrà aggiunto un commento HTML che indica la data della prossima review:
```
<!--SR:!2021-08-20,13,290-->
```
Essendo un commento HTML non è visibile in modalità preview della card.

### Conclusione
Lo spaced repetition è una tecnica incredibile per fissare i concetti riducendo al minimo il tempo "perso" a ripassare concetti già conosciuti o a "non ripassare" concetti che ormai sono stati dimenticati.
Nel prossimo post parlerò di come fare uno script che automaticamente crea il dizionario di flashcards nell'ambito dell'apprendimento di una nuova lingua.