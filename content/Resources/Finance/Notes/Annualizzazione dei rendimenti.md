---
tags:
  - Finance
---
Spesso ho la necessità di confrontare due investimenti che hanno tempistiche diverse di cash flow (es. meglio un rendimento di 20% su 2 anni o del 10% all'anno?).
In questi casi è necessario annualizzare i rendimenti, quindi portarli tutti con lo stesso riferimento temporale (es. 1 anno) in modo che siano facilmente confrontabili.
La formula per ottenere il rendimento annualizzato è la seguente:
$$Rendimento_{annualizzato} = (1+Rendimento)^{\frac{1}{anni}}-1$$
Esempio se ho un rendimento del 20% in 2 anni avrò $(1+0,2)^\frac{1}{2}=9,545\%$.

Se ho un caso più difficile quindi confrontare rendimenti che hanno tempi discreti sul giorno (es. 10% su 9 mesi contro 20% su un anno e altri giorni) devo portare la differenza tra le due date in anni e poi usare la formula sopra.
Date due date (inizio e fine investimento) le posso portare nella formula con $$\frac{Data_{fineRendimento} - Data_{inizioRendimento}}{365}$$ (la differenza tra due date mi serve per ottenere il numero di giorni).
Posso quindi semplificare la formula sopra in questo modo
$$Rendimento_{annualizzato} = (1+Rendimento)^{\frac{365}{Data_{fineRendimento} - Data_{inizioRendimento}}}-1$$