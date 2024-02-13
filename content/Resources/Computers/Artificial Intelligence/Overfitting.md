---
tags:
  - MachineLearning
---
L'overfitting è un problema comune nell'addestramento di algoritmi di machine learning, che si verifica quando ==il modello impara troppo bene i dati dell'insieme di addestramento e non generalizza correttamente su nuovi dati==.
Questo significa che il modello si è adattato con grande precisione alle specifiche osservazioni avvenute nel dataset di addestramento, ma fallisce nella generalizzazione con i dati reali, ovvero il modello ha una elevata varianza.
In altre parole, l'overfitting si verifica quando il modello diventa troppo complesso per la quantità di dati disponibili. Il modello ==memorizza le caratteristiche specifiche dei dati dell'insieme di addestramento invece di apprendere le relazioni più generalizzate tra i dati==. Ciò significa che il modello può avere prestazioni molto elevate sui dati utilizzati durante l'addestramento ma prestazioni scarse su nuovi dati.

### Cause

Ci sono diverse cause dell'overfitting:
* una rete neurale con troppe unità nascoste o strati può essere troppo complessa per i pochi esempi presenti nel [[Dataset]];
* gli esempi del training set hanno rumore o errori casuali, la rete potrebbe imparare anche questi errori come parte della soluzione ottimale al problema;
* se ci sono poche variazioni nei campioni del dataset (esempio tutti gli oggetti da rilevare nella stessa posizione), la rete potrebbe concentrarsi solo sulle caratteristiche specifiche a quelle posizioni piuttosto che sulle proprietà generalizzate degli oggetti.

### Come evitarlo

Per evitare l’overfitting, è possibile utilizzare tecniche come
* Raccogliere più dati di addestramento;
* la regolarizzazione (come [[L1 - L2 regularization]]) che introduce una penalità per la complessità;
* Scegliere un modello più semplice, con un minor numero di parametri
* aumentando il numero di esempi nel training set attraverso tecniche come [[Data augmentation]] (creazione artificiale di varianti dei campioni originali)
* [[Riduzione della Dimensionalità|Ridurre la dimensionalità]] dei dati tramite selezione o estrazione delle caratteristiche

Dobbiamo notare che la raccolta di una maggiore quantità di dati di addestramento riduce le probabilità di un overfitting. Tuttavia, non sempre questo potrebbe essere utile, per esempio quando i dati di addestramento sono estremamente rumorosi o il modello è già piuttosto vicino a quello ottimale.

