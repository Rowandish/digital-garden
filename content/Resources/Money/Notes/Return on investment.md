---
tags:
  - Finance
---

Il ritorno dell'investimento è definito come il rapporto tra il prezzo di acquisto e quello di vendita di un determinato bene diviso il prezzo di acquisto.
$$R = \frac{C_f-C_i}{C_i}$$
Questo valore però non tiene in considerazione il fattore tempo, che invece è determinante come spiegato in [[Interesse composto]]. Infatti avere un rendimento dell'$x\%$ in a mese non è la stessa cosa di avere lo stesso rendimento in un anno.
Bisogna quindi annualizzare il rendimento in modo che sia confrontabile con altri rendimenti con tempo differenti.

## Rendimento giornaliero -> annualizzato

La formula del rendimento annualizzato è il seguente, con $x$ il numero di giorni in cui sono stato investito.
$$R_a = (1+R)^{\frac{365}{x}} - 1$$
Applicando la formula del [[Tasso interno di rendimento (TIR)]] ottengo esattamente $R_a$.

## Rendimento multi anno -> annualizzato
Dato un rendimento percentuale complessivo in vari anni, per trasporlo ad un rendimento annualizzato uso una formula analoga alla precedente
$$R_a = (1+R)^{\frac{1}{NumeroAnni}} - 1$$