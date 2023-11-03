---
tags:
  - DigitalImageProcessing
---


Il pattern matching è quella procedura che permette di trovare una immagine master in un nuova immagine acquisita.

## Ricerca in aree piccole

Idea: devo allineare due aree, una master e la nuova acquisita in modo da effettuare un allineamento sul master o confronto.

Qualora l'immagine acquisita non abbia molta variabilità con l'immagine master, quindi io so che il mio pattern matching sarà sempre più o meno nella stessa posizione, posso operare come segue.

### Full Search
Assumiamo che io debba cercare il mio pattern in una area di 32 pixel, la soluzione ottima sarebbe il confronto pixel pixel tra l'immagine e il master in tutte le 32*32 posizioni possibili, dove ho la maggiore percentuale di somiglianza tra i pixel ho la corrispondenza col master. Soluzione ottima ma lenta, dobbiamo utilizzare una euristica.

### Fast Search

Non provo davvero tutte le posizioni, utilizzo un algoritmo per andare molto vicino all'ottimo.
Dato lo spazio di ricerca, provo di sicuro dove deve essere, poi provo a nord, sud, est, ovest (distanza 8 dal centro). Guardo che punteggi ho, quella che mi da il punteggio migliore effettuo un dimezzamento del passo e faccio come sopra.
Ultimo passo 1 effettuo la FullSearch, sugli ultimi 9 pixel.
Il numero di controlli è 9+8*numeroPassi, sicuramente inferiore alla FullSearch come sopra.
Il metodo funziona se la funzione di somiglianza è monotona decrescente mano a mano che mi allontano dal master, cosa che succede sempre a meno di utilizzare pattern ripetitivi

### Livelli piramidali

Invece che ragionare in posizione di ricerca ragiono in risoluzione: se devo fare un pattern matching con un pattern grande sono lento, allora creo _n_ sottolivelli (copie della immagine di ricerca corrente) dimezzando la risoluzione ogni volta.
Con l'immagine a risoluzione 1/8 (esempio) sono molto veloce e più o meno capisco dove è, poi proseguo con 1/4 e 1/2.
Se parametrizzo in modo errato i livelli, o in genere sbaglio la prima ricerca ad 1/8 poi non esco più, l'algoritmo non è in grado di uscire da eventuali minimo locali che trova.
Tipicamente utilizzando i livelli, in alcune situazioni, posso ottenere una precisione maggiore.

## Parametri
Si seguito una spiegazione dei vari parametri del pattern matching presenti nel nostro software.

### Greediness

Quanta scrematura fai all'inizio. Attenzione che Halcon utilizza il `GreedinessScore` per scremare i risultati, quindi se io metto uno `GreedinessScore` alto, diventa molto più greedy e screma conseguentemente molto di più.
Quindi posso avere il caso strano per cui dico ad Halcon di trovare un pattern con punteggio minimo 0.9 e lui non lo trova. Se metto 0.8 lui lo trova con punteggio 0.92. Conseguentemente introduco il parametro `MinScore` che è lo score vero, mentre `GreedinessScore` è un valore più basso che indica ad Halcon di trovare più soluzioni possibili.

### GreedinessScore

Punteggio minimo affinché il pattern risulti trovato, sempre minore del `MinScore`.
Tipicamente 

### MinScore

Punteggio minimo affinché il pattern risulti trovato. Analogo al `GreedinessScore` con la differenza che non lo mettiamo nelle funzioni di Halcon, altrimenti c'è il rischio che non trovi un pattern che effettivamente esiste per il problema indicato sopra.
