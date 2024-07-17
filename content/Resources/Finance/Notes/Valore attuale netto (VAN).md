---
tags:
  - Finance
---
Il valore attuale netto (VAN), in inglese *Net Present Value*, indica ==il valore attualizzato al tempo presente di un flusso di cassa che è successo nel passato o nel futuro==.

Indica quando vale un determinato investimento in base al proprio valore del tempo.
L'idea è che i soldi che vengono forniti nel futuro valgono di meno di quelli che vengono forniti oggi o nel passato, e questa formula permette di ==attualizzare i flussi di cassa scontandoli con un determinato [[Interesse composto#^dc9ed7|tasso di sconto]] che dipende da persona a persona==.
I soldi nel futuro valgono di meno in quanto ci sono le seguenti incertezze che è necessario prezzare:
* Non si è sicuri di riceverli nel futuro;
* Inflazione;
* Prima li ho prima li posso utilizzare.

Utilizza la formula dell'[[Interesse composto]] tramite la somma dei vari flussi di cassa ai vari istanti temporali utilizzando come $i$ il tasso di sconto e come $n$ positivo o negativo il momento in cui ricevo il determinato flusso di cassa.

Una persona per cui i soldi nel futuro valgono come i soldi oggi (es. una persona che non investe e mette tutti i soldi sul conto corrente) avrà tasso di sconto $i=0$, una persona con le mani bucate che appena ha soldi gli spende avrà perfino $i<0$ in quanto preferisce avere soldi nel futuro che oggi.

Per la maggior parte delle persone invece $i>0$ e dipende dalla propria propensione al rischio e cultura finanziaria: una persona che investe senza problemi in azioni avrà come un $i>5\%$; una persona più prudente magari avrà un $2\%<i<5\%$.
Assumiamo di ricevere il capitale $C_1$ al tempo $t_{-2}$, il capitale $C_2$ al tempo $t_0$, il capitale $C_3$ al tempo $t_1$ e il capitale $C_4$ al tempo $t_3$.

La formula per calcolare il VAN è:
$$VAN = \frac{C_1}{(1+i)^{-2}}+\frac{C_2}{(1+i)^0}+\frac{C_3}{(1+i)^1}+\frac{C_4}{(1+i)^3}$$
$$\sum_{j=1}^{n} \frac{C_j}{(1+i)^j}$$
Ovviamente assumendo che il tasso di sconto $i$ non cambi nel tempo.

![[Pasted image 20240704174842.png]]

Assumiamo di aver acquistato un BTP a 1000€ che da cedole ogni 3 mesi di 8,97€ e dopo 5 anni ritorna i 1000 investiti.
Per sapere quanto rende questo BTP in termini numerici (quindi non in termini percentuali con il [[Tasso interno di rendimento (TIR)|TIR]]) non basta bisogna banalmente sommare tutte le cedole (altrimenti così facendo si da valore nullo al tempo, $i=0$) ma si può fare un calcolo analogo a 
$$VAN = \frac{-1000}{(1+i)^{0}}+\frac{8,97}{(1+i)^\frac{3}{12}}+\frac{8,97}{(1+i)^\frac{6}{12}}+\frac{8,97}{(1+i)^\frac{9}{12}}+...+\frac{8,97}{(1+i)^\frac{60}{12}}+\frac{1000}{(1+i)^\frac{60}{12}}$$

A differenza del [[Tasso interno di rendimento (TIR)]] questo metodo funziona solo se si da un valore al proprio tempo, quindi quanto vale il denaro per la mia specifica situazione (per esempio se una persona investe senza problemi nell'azionario può essere un buon valore il 5%).
Attenzione che il metodo funziona bene solo se i flussi di cassa cambiano segno solo una volta per investimento, altrimenti rischia di dare risultati errati.

In questa immagine si vede come cambia il VAN di un investimento (in questo caso un BTP con rendita netta 3,83%) all'aumentare del tasso di sconto $i$: più questo cresce più il VAN diminuisce, fino a diventare negativo.
Il punto di intersezione del grafico sull'asse delle ascisse dove il VAN diventa negativo è esattamente il rendimento dello strumento finanziario in questione, quindi il [[Tasso interno di rendimento (TIR)]] che permette di confrontare strumenti finanziari diversi nel senso che strumenti che hanno lo stesso TIR sono finanziariamente equivalenti.
![[Pasted image 20231020154030.png]]

## Spreadsheets

Su Excel c'è una funzione per calcolare il VAN chiamata `XNPV` (o `VAN.X` in italiano) che prende come primo parametro il tasso di sconto, il secondo il flusso di cassa (quindi l'array dei $C$) e come ultimo le date associate ai $C$.
Attenzione che il flusso di cassa comprende sia quello iniziale (per intenderci il -1000€ per l'acquisto del BTP) che quello finale (quindi i +1000€).