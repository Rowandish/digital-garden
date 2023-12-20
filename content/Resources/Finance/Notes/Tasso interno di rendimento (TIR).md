---
tags:
  - Finance
---
## Definizione matematica

Il tasso interno di rendimento (in inglese IRR) è quel valore del tasso di sconto di che rende il valore del [[Valore attuale netto (VAN)]] uguale a $0$.
![[Pasted image 20231020154630.png|450]]
Questa è una equazione di grado pari al massimo dei valori di $t$ in valore assoluto ($m$); quindi ha un numero di soluzioni che fa da $0$ a $m$.
Nei casi classici del debito (il primo $C$ positivo e poi tutti gli altri positivi) o del credito (il primo $C$ negativo e poi tutti gli altri positivi) l'equazione ha sempre soluzione.

## Utilizzo

Questa funzione permette quindi, dato un generico flusso di cassa, di fornire il  di **rendimento annuale**.
Questo strumento permette quindi di **paragonare qualsiasi rendimento** che sia a debito o a credito, che abbia date e flussi di cassa differenti e così via, l'importante è che questi flussi di cassa siano certi.
Per esempio è utilissimo per confrontare debiti (mutui con durata e interessi diversi) o crediti (acquisto di [[Obbligazioni]] con determinate cedole).
Non funziona invece quando i flussi di cassa non sono certi, esempio principe l'investimento in azioni.
Il vantaggio del TIR rispetto al [[Valore attuale netto (VAN)]] è che posso confrontare due investimenti anche senza sapere quale è il mio tasso di sconto, quindi quanto vale il mio tempo.
## Spreadsheets

Su Excel c'è una funzione per calcolare il TIR chiamata `XIRR` (in inglese, mentre `TIR.X` in italiano) che prende come primo il flusso di cassa (quindi l'array dei $C$) e secondo le date associate ai $C$.

![[Pasted image 20230929175814.png]]