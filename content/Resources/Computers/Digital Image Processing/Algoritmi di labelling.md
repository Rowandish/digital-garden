---
tags:
  - DigitalImageProcessing
  - PublishedPosts
---


![[labelb.gif]]

## 1. Introduzione 
Gli algoritmi di labelling di componenti connesse cercano di **raggruppare i pixel di un'immagine (binaria o in scala di grigi) in base alla loro connettività**, la quale può essere di varia natura, sia effettiva (pixel adiacenti) sia qualitativa (pixel con la stesso valore di intensità).
una volta che tutti i gruppi sono stati determinati, **ad ogni pixel viene associata un'etichetta di colore in base al gruppo a cui questo è stato assegnato**.
Rilevare questi gruppi e eseguirne il labelling di gruppi di pixel disgiunti è il punto fondamentale in molte applicazioni di analisi di immagini.

### 1.1 Approfondimento: Connettività tra pixel
La notazione di pixel connectivity descrive la relazione tra due o più pixel. Due pixel sono considerati connessi se soddisfano una certa condizione sul valore del pixel stesso, oppure sulla loro vicinanza spaziale.
Per formulare il concetto di "*adiacenza*" o "*vicinanza spaziale*" dobbiamo introdurre il concetto di *vicinato*. Dato un pixel _p_ di coordinate _(x,y)_ l'insieme dei pixel di coordinate

```
{(x+1, y), (x-1, y), (x, y+1), (x, y-1)}
```
è detto _4-neighbors_. _8-neighbors_ invece aggiunge, oltre ai pixel indicati sopra, anche i pixel in diagonale.
Un insieme di pixel in cui tutti sono connessi con gli altri è detto _componente connessa_.
Trovare tutte le _componenti connesse_ di un'immagine è il compito dell'algoritmo di labelling descritto in questo articolo.

## 2. Funzionamento
Questo algoritmo esegue uno scan pixel a pixel (dall'alto in basso e da destra a sinistra) in modo da indentificare regioni di pixel spazialmente connessi che condividono la stesso valore del pixel _V_. Se l'immagine è binaria _V_ può assumere solo un valore, se invece è in scala di grigi un insieme di valori.
Prendiamo come esempio la seguente immagine

![[art8.gif]]

L'algoritmo assegna ad ogni zona trovata un valore in scala di grigi

![[art8lab1.gif]]

é conveniente passare dalla scala di grigi al colore per il labelling in modo che siano più facilmente distinguibili, ottenendo così la seguente immagine

![[art8lab2.gif]]

L'algoritmo ottiene risultati migliori quando l'immagine è stata preprocessata da qualche algoritmo di segmentazione (come il _thresholding_) o schema di _classificazione_.

## 3. Applicazioni
L'applicazione più comune di questo algoritmo è contare il numero di oggetti in un'immagine. Per esempio, nell'esempio indicato sopra, avere 8 colori diversi significa che nell'immagine sono presenti 8 oggetti.
Prendiamo come esempio l'immagine seguente, in cui il nostro obiettivo è contare il numero di galline

![[tur1gry1.gif]]

Per prima cosa eseguo un algoritmo di _thresholding_ per ottenere un'immagine binaria

![[tur1thr1.gif]]

e lanciando l'algoritmo di labelling ottengo

![[tur1lab1.gif]]

come versione in scala di grigi e

![[tur1lab2.gif]]

con label colorate.
Il numero di colori diversi in questa immagine è 196, che non è assolutamente il numero di polli ricercato.
Questo esempio mostra come l'algoritmo di labelling è solo il passo finale, la parte difficile è ottenere una buona immagine binaria in ingresso che mi rappresenti fedelmente quanto voglio ricercare e che separi in maniera netta gli oggetti interessanti (_foreground_) dagli oggetti da scartare (_background_).