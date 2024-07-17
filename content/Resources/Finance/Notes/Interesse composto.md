---
tags:
  - Finance
---
==In finanza il tempo moltiplica il denaro.==

Data una linea temporale in cui oggi siamo al tempo $t_0$ con una determinata quantità di denaro $C$.
Ora prendiamo degli istanti temporali futuri definiti come $t_1$, $t_2$, $t_3$ e nel futuro come $t_{-1}$, $t_{-2}$, $t_{-3}$; lo scopo è cercare di capire la differenza del denaro $C$ averlo al tempo $t_0$ rispetto ai tempi futuri o passati.
A meno di situazioni particolari avere $C$ a $t_0$ è sempre meglio rispetto ad avere $C$ al tempo $t_1$ (inflazione, possibilità di investirlo, opportunità…).
Tanto più il denaro lo sia ha nel passato meglio è: questo concetto è rappresentato dalla formula dell'interesse con $i$ il tasso di interesse:
$$C*(1+i)$$
La formula sopra è la formula dell'interesse semplice, che funziona se i soldi ottenuti dagli interessi non vengono reinvestiti di anno in anno.
Dato che questo tipicamente non succede (**all'anno i-esimo avrò investito il capitale iniziale più gli interessi maturati dall'anno 0 all'anno i-esimo**) si usa la formula dell'interesse composto con $n$ il numero di anni passati.
$$C*(1+i)^n$$
Questa formula assume la capitalizzazione dell'interesse annualmente, se avviene più spesso (esempio trimestralmente) avrò rendimenti ancora maggiori.
Posso anche calcolare il valore attuale di una somma che ho ricevuto nel passato ($n$ negativo) o che riceverò nel futuro ($n$ positivo) usando la seguente formula

$$ValoreAttuale = \frac{C}{(1+i)^n}$$

## Tasso di sconto

^dc9ed7

Il valore di $i$ viene detto *tasso di sconto* ed è un tasso che viene deciso da chi fa i calcoli e indica quanto, per noi, il denaro si valuta ogni anno, quindi quanto sono in grado di far rendere il denaro.
Se sono una persona che spende tutto quello che guadagna il mio tasso di sconto sarà uguale a 0, se ho startup molto profittevole magari è anche il 10% o più.
Questo strumento è molto interessante in quanto permette di confrontare valori attuali con valori del passato o del futuro in base al proprio tasso.
Per esempio assumiamo di dover decidere se ricevere 100€ oggi o 105€ l'anno prossimo.
Se il nostro tasso di sconto è 10% (quindi 0,1) posso calcolare quanto sono 105€ l'anno prossimo oggi per me:
$$ValoreAttuale = \frac{105}{(1+0,1)^1} = 94,45$$
Dato che 94,45 è minore di 100 posso concludere che mi conviene avere i 100€ oggi.
Ovviamente posso utilizzare questa formula anche per flussi di cassa che non sono perfettamente dopo $n$ anni precisi, utilizzando numeri reali come $n$ (365/giorno del flusso di cassa).

Con questa formula posso anche calcolare quale è il tasso di sconto di break even per avere esattamente lo stesso rendimento.
Queste formule sono indispensabili per calcolare il [[Valore attuale netto (VAN)]] e soprattutto il [[Tasso interno di rendimento (TIR)]].