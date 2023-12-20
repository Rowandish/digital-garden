---
tags:
  - MachineLearning
---
La L1 e la L2 regularization sono tecniche utilizzate nell'addestramento delle reti neurali per prevenire l'[[Overfitting]]. Queste tecniche ==aggiungono un termine di regolarizzazione alla funzione di costo del modello==, il che aiuta a limitare i valori dei pesi della rete.

La L1 regularization (o "Lasso regularization") aggiunge un termine alla funzione di costo equivalente alla somma assoluta dei valori dei pesi moltiplicati da una costante lambda. In pratica questo porta ad avere molti parametri vicini allo zero, ottenendo una sorta di selezione automatica delle feature più importanti.

La L2 regularization (o "Ridge regularization"), invece, aggiunge un termine alla funzione di costo equivalente al quadrato della norma euclidea dei pesi moltiplicata da una costante lambda. In questo caso si cerca sempre di ridurre le dimensione dei coefficienti ma in modo meno aggressivo rispetto all'L1

Entrambe le tecniche cercano quindi di ==limitare la complessità del modello attraverso la penalizzazione sui grandi valori assunti dai parametri durante l’allenamento== e possono essere usate anche contemporaneamente nella stessa rete neurale con diverso peso assegnato alle due regolarizzazioni.

In generale, se i dati sono rumorosi o non molto correlati tra loro è possibile che l'utilizzo della regolarizzazione possa migliorare le prestazioni del modello evitando overfitting; d'altra parte se i dati hanno già intrinsecamente poco rumore oppure se ci si vuole concentrare su dettagli specifici potrebbe essere meglio non applicarle per avere modelli più precisi ma complessivamente più grandi.