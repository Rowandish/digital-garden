---
tags:
  - MachineLearning
---
L'overfitting è un problema comune nell'addestramento delle reti neurali, che si verifica quando ==il [[GPT Model|modello]] impara troppo bene i dati dell'insieme di addestramento e non generalizza correttamente su nuovi dati==.

In altre parole, l'overfitting si verifica quando il modello diventa troppo complesso per la quantità di dati disponibili. Il modello ==memorizza le caratteristiche specifiche dei dati dell'insieme di addestramento invece di apprendere le relazioni più generalizzate tra i dati==. Ciò significa che il modello può avere prestazioni molto elevate sui dati utilizzati durante l'addestramento ma prestazioni scarse su nuovi dati.

### Cause

Ci sono diverse cause dell'overfitting:
* una rete neurale con troppe unità nascoste o strati può essere troppo complessa per i pochi esempi presenti nel [[dataset]];
* gli esempi del training set hanno rumore o errori casuali, la rete potrebbe imparare anche questi errori come parte della soluzione ottimale al problema;
* se ci sono poche variazioni nei campioni del dataset (esempio tutti gli oggetti da rilevare nella stessa posizione), la rete potrebbe concentrarsi solo sulle caratteristiche specifiche a quelle posizioni piuttosto che sulle proprietà generalizzate degli oggetti.

### Come evitarlo

Per evitare l’overfitting, è possibile utilizzare tecniche come
* la regolarizzazione (come [[L1 - L2 regularization]]),
* aumentando il numero di esempi nel training set attraverso tecniche come [[Data augmentation]] (creazione artificiale di varianti dei campioni originali)
* ridimensionando / modificando lo stesso insieme originale in modo casuale;
* Monitorare costantemente le metriche delle performance del modello sia sull’insieme usato per allenarlo che su uno "validation" set separato dal primo permettono anche un controllo sulla presenza o meno dell’overfitting.