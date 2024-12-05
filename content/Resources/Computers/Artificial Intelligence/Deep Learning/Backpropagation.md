---
tags:
  - DeepLearning
---
![[Pasted image 20240402095214.png]]
La backpropagation è un algoritmo per regolare i pesi delle connessioni tra i neuroni di una rete neurale in modo da minimizzare l'errore durante l'addestramento.

Ecco come funziona in breve:

1. **Forward Propagation**: Durante la fase di forward propagation, i dati di input vengono passati attraverso la rete neurale, uno strato dopo l'altro, fino a quando non viene generata un'output. Durante questo processo, i neuroni combinano i loro input utilizzando i pesi delle connessioni tra di loro e applicando una [[Funzione di attivazione]].
2. **Calcolo dell'Errore**: Dopo aver generato un'output, viene calcolato l'errore confrontando l'output previsto dalla rete con l'output desiderato usando una [[Loss function]].
3. **Backward Propagation**: Durante la fase di backward propagation, ==l'errore calcolato viene propagato all'indietro attraverso la rete, calcolando quanto ogni peso contribuisce all'errore complessivo. Quindi, i pesi delle connessioni vengono aggiornati in base a questo calcolo per ridurre l'errore complessivo==.
4. **Aggiornamento dei Pesi**: Infine, i pesi delle connessioni vengono aggiornati utilizzando un [[Algoritmi di ottimizzazione|algoritmo di ottimizzazione]] come la discesa del gradiente, che utilizza i gradienti calcolati durante la backpropagation per modificare i pesi in modo da ridurre l'errore complessivo.

La differenza principale tra forward propagation e backward propagation è che forward propagation è il processo in cui i dati di input vengono passati attraverso la rete per ottenere un'output, mentre backward propagation è il processo in cui l'errore viene propagato all'indietro attraverso la rete per aggiornare i pesi e migliorare le prestazioni della rete. In altre parole, forward propagation è l'avanzamento dei dati attraverso la rete, mentre backward propagation è il retroscena dell'addestramento della rete per migliorare le sue prestazioni.
## Esempio

Immagina di voler addestrare una rete neurale per riconoscere numeri scritti a mano. Durante la fase di forward propagation, i numeri di input (immagini dei numeri) vengono passati attraverso la rete e viene prodotto un'output che indica quale numero la rete pensa di aver visto. Successivamente, confrontiamo questo output con il numero reale scritto a mano per calcolare l'errore. Durante la fase di backward propagation, calcoliamo quanto ogni peso nella rete ha contribuito all'errore e aggiorniamo i pesi in modo da ridurre l'errore complessivo. Continuiamo questo processo iterativamente fino a quando la rete non è in grado di migliorare ulteriormente la sua capacità di riconoscere i numeri.

