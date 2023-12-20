---
tags:
  - DigitalImageProcessing
  - PublishedPosts
---


## Introduzione
La trasformata di Hough è una tecnica che viene utilizzata per isolare le caratteristiche di una determinata forma all'interno di un'immagine.
Dato che questa trasformata richiede che tali _feature_ devono avere una determinata conformazione parametrica, viene usata tipicamente per rilevare linee, cerchi o ellissi.
Il vantaggio principale di questa tecnica è che non è sensibile ne agli eventuali "buchi" che si possono trovare nella _feature_ analizzata, ne al rumore.

## Funzionamento
Il funzionamento avviene tramite la costruzione di una matrice di accumulazione che contiene tutti i valori di `(r, θ)`, in quanto il metodo lavoro con le coordinate polari.
Per un'analisi più approfondita leggere in [questo link](http://homepages.inf.ed.ac.uk/rbf/HIPR2/hough.htm)

## Applicazioni
La trasformata di Hough utilizza in ingresso un insieme di punti di frontiera (_edge point_). Questi punti sono comunemente ottenuti tramite un algoritmo di _edge detection_ sull'immagine.
Per capire meglio il suo funzionamento partiamo dalla seguente immagine che descrive due rettangoli sovrapposti

![[sqr1.gif]]

Lanciando un algoritmo di _edge detection_ (in questo caso _Canny_) ottengo la seguente figura

![[sqr1can1.gif]]

Che mi permette di individuare sì i bordi dell'immagine, ma non ho alcuna informazione su che tipi di bordo sono ne sulla loro quantità. in questo caso, possiamo usare la trasformata di Hough per il rilevamento di linee per rilevare le 8 separate linee che compongono l'immagine e successivamente la struttura geometrica dell'oggetto.
Utilizzo questi edge come input alla trasformata, la matrice di accumulazione ottenuta è la seguente (il raggio è l'ascissa mentre l'angolo l'ordinata).

![[sqr1hou1.gif]]

Le linee trovate nell'immagine in ingresso coincidono con i picchi del piano di Hough.
Esistono più metodi che permettono di estrarre questi punti dalla matrice di accumulazione, per esempio usare prima un _thresholding_ e poi qualche _thinning_ alle zone di punti luminosi isolati.
In questo modo estraggo dei punti univoci `(r, θ)` in cui ognuno corrisponde ad una linea retta nell'immagine originale (in pratica prendiamo solo i massimi locali della matrice di accumulazione i cui valori sono maggiori o uguali di una certa percentuale del massimo assoluto della matrice).
Eseguendo un mapping inverso dallo spazio di Hough al piano cartesiano fornisce un insieme di linee dell'immagine iniziale.
Ecco il risultato ottenuto:

![[sqr1hou3.gif]]

E' importante notare che le rette trovate hanno lunghezza infinita. Per trovare quale parte della retta coincide con l'immagine sottostante è necessaria un'analisi ulteriore.