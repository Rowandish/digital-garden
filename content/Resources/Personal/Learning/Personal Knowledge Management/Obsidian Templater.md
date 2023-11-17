---
tags:
  - PersonalKnowledgeManagement
---


Questo plugin permette di estendere la funzionalità del plugin core "Template" aggiungendo delle funzionalità ulteriori complesse.
Per l'utilizzo normale dei template il plugin del core è sufficiente, questo serve per utilizzi complessi dove c'è di messo del codice.
Un suo utilizzo classico sono le note di journaling dove ho bisogno di template che ogni giorno siano diversi in base a quanto vengono creati.
## Aggiungere la data precedente e futura
```
<<[[2023-11-06 - Monday]] | [[2023-11-08 - Wednesday]]>>
```

## Aggiungere una data fissa in uno script
Per lo script della data casuale voglio che la quote sia sempre uguale a parità di nota, non che cambia tutte le volte che ricarico lo script.
Per fare questo ho bisogno di un template che vada ad inserire una costante che dipende dalla data (esempio il numero della giorno nell'anno).
Così ottengo sia la quote casuale ma che tale quote sia sempre la stessa a parità di giorno.
Per fare questo basta aggiungere:
``` javascript
let dayOfTheYear = 311;
```