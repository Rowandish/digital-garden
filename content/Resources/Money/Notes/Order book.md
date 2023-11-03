---
tags:
  - PersonalFinance
  - PublishedPosts
---
## Introduzione

Il prodotti finanziari vengono scambiati principalmente all'interno dei mercati finanziari (a meno degli scambi [[Over the Counter]]).
I mercati finanziari funzionano con un sistema chiamato *order book* dove vengono indicati da una parte gli ordini di vendita e dall'altra gli ordini di acquisto (entrambi limit order, che vedremo successivamente).
Quando si vuole vendere qualcosa si inserisce il rispettivo *ordine di vendita* indicando al mercato la propria disponibilità a vendere *x* quantità del bene *y* al prezzo *z*.
Analogamente negli *ordini di acquisto* comunico al mercato la volontà di acquistare una determinata quantità dello stesso bene ad un preciso prezzo.
Negli ordini di vendita avrò quindi numerosi ordini, ognuno con la sua quantità e il suo prezzo e la stessa cosa simmetrica ci sarà negli ordini di acquisto.
Per le vendite il book è ordinato **dal prezzo minore al maggiore** mentre per l'acquisto in ordine inverso, in modo che la vendita e l'acquisto "più conveniente" (quindi che si accontentano di meno soldi) siano in cima.
Un book viene detto "stabile" (quindi senza scambi) quando la vendita migliore è comunque ad un prezzo maggiore dell'acquisto maggiore.
Esempio di book stabile, non ci sono scambi.
![[Pasted image 20221205224935.png]]

## Prezzo
Lo scambio avviene quando viene inserito un nuovo ordine che vada a matchare un ordine già presente, in questo caso viene aggiornato il *prezzo* del bene che è, di fatto, il prezzo pagato nell'ultimo scambio effettuato.
In alcuni exchange molto liquidi ci sono moltissimi scambi e conseguentemente il prezzo continua a variare, anche migliaia di volte al secondo.
Il prezzo che vedo è tipicamente un prezzo campionato, per esempio una volta al secondo.
Dato un mercato che ha una chiusura (i mercato tradizionali, non gli exchange di criptovalute) vengono forniti quattro prezzi:
* **Prezzo di apertura**: prezzo che è uscito dall'asta di apertura
* **Prezzo massimo del giorno**
* **Prezzo minimo del giorno**
* **Prezzo di chiusura**: prezzo medio degli ultimi minuti di scambio.

Di solito ogni prezzo è associato ad un volume (quantità venduta a tale prezzo) in quanto è importante sapere se un prezzo è dovuto a numerosi movimenti oppure è dovuto solo a, potenzialmente, un singolo ordine.

## Ordini
### Ordine senza limiti di prezzo (al mercato)
In questo caso metto un ordine di acquisto che va a prendere il prezzo migliore della colonna sell.
Se la quantità richiesta è maggiore di quella presente in un ordine già presente (nell'esempio sopra se è maggiore di 40) andrò a prendere tutti i 40 e poi parte dei successivi (al prezzo impostato dal venditore ovviamente).
Qualora ci sia un book poco liquido con molti gab tra i vari ordini di vendita questa tipologia di ordine è pericolosa in quanto potrei matchare degli ordini sconvenienti.

### Ordine con limite di prezzo (limit order)
Negli ordini con limite di prezzo sono io che decido il prezzo a cui voglio pagare o vendere un bene: il mio ordine non verrà quindi immediatamente evaso ma entrerà nel book (in inglese *limit order*).
In alcuni mercati, specialmente di criptovalute, viene incentivato l'utilizzo dei limit order per rendere più liquido il book abbassando le commissioni.

### Opzioni
A questi ordini posso aggiungere anche particolari opzioni:
* **Tutto o niente (ToN)**: significa che se non trova un match di tutta la quantità che voglio non parte l'ordine. Nel caso sopra se inserissi un ordine di 50 pezzi a 19€ non partirebbe con questa opzione in quanto a quel prezzo ne sono disponibili solo 40.
* **Esegui o cancella**: o viene trovato subito un match oppure lo cancella
* **Esegui quantità minima**: esegui l'ordine solo se troviamo come minimo una determinata quantità
* **Validità in giorni**: di default gli ordini valgono una giornata, anche se esistono delle opzioni per farli rimanere più giorni.

### Apertura mercato
A fine giornata tutti gli ordini vengono cancellati (a meno di quelli validi più giorni), quando il mercato riapre non c'è un book anche se magari prima sono arrivati degli ordini.
In questo caso il mercato, prima dell'apertura, effettua il più possibile dei match degli ordini già presenti (**asta di preapertura**) con un algoritmo che massimizza le compravendite. Di solito questa asta dura 5 minuti.
Con gli ordini che rimangono costruisce il nuovo book e si inizia la giornata

## Esempio
Su Directa è possibile vedere un book, un po' rudimentale, ma efficace di ogni strumento finanziario.
Per esempio nell'esempio sotto si vedono i vari ordini di acquisto (ordinati dal più alto al più basso) e gli ordini di vendita ordinati all'opposto.
L'ordine di acquisto migliore è quindi 100,71 mentre la vendita migliore è 100,72.
Qualora piazzassi un ordine a mercato, quindi senza limiti di prezzo, andrei a pagare 100,72.
![[Pasted image 20221207102039.png]]
In questo esempio ho piazzato un ordine di acquisto a 142,35€ per 17 azioni con un limit order. La mia offerta è la prima dell'order book, nel senso che è la migliore tra le offerte di acquisto non ancora accettate.
![[Pasted image 20230530110205.png]]