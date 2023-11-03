---
tags:
  - MachineLearning
---
==Le epoche nell'addestramento di una rete neurale indicano il numero di volte che l'intero [[dataset]] viene presentato al modello durante la fase di addestramento==.

In altre parole, un'epoca corrisponde a un ciclo completo attraverso tutti i dati dell'insieme di addestramento.

==Durante ogni epoca, il modello impara dai dati e aggiorna i suoi pesi per migliorare le sue prestazioni. Di solito, più epoche vengono eseguite, maggiori sono le possibilità che il modello migliori le sue performance.==

Tuttavia, scegliere quante epoche fare dipende dalle specifiche del problema e dal tipo di dataset utilizzato. Se si utilizza un set di dati molto grande o complesso, potrebbe essere necessario eseguire molte epoche per ottenere buone prestazioni del modello.

D'altra parte, se si utilizza un set di dati relativamente piccolo o semplice, potrebbe non essere necessario eseguire troppe epoche per evitare l'[[Overfitting]] (ovvero quando il modello memorizza troppo bene i dati dell'insieme di addestramento ma generalizza male su nuovi dati).

In generale è consigliabile monitorare costantemente le metriche delle prestazioni del modello durante l'addestramento e fermarlo quando queste smettono di migliorare significativamente anche aumentando ulteriormente il numero delle epoche.