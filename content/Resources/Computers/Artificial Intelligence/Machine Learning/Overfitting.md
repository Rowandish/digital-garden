---
tags:
  - MachineLearning
---
L'overfitting è un problema comune nell'addestramento di algoritmi di machine learning, che si verifica quando ==il modello impara troppo bene i dati dell'insieme di addestramento e non generalizza correttamente su nuovi dati==.
Questo significa che il modello si è adattato con grande precisione alle specifiche osservazioni avvenute nel dataset di addestramento, ma fallisce nella generalizzazione con i dati reali, ovvero il modello ha una elevata varianza.
In altre parole, l'overfitting si verifica quando il modello diventa troppo complesso per la quantità di dati disponibili. Il modello ==memorizza le caratteristiche specifiche dei dati dell'insieme di addestramento invece di apprendere le relazioni più generalizzate tra i dati==. Ciò significa che il modello può avere prestazioni molto elevate sui dati utilizzati durante l'addestramento ma prestazioni scarse su nuovi dati.
Per verificare se un modello soffre di overfitting basta vedere che l'errore sul set di test è notevolmente maggiore dell'errore sul set di addestramento come nell'immagine sotto.

![[Pasted image 20240402115003.png]]

### Cause

Ci sono diverse cause dell'overfitting:
* Non c'è un numero sufficiente di esempi di addestramento
* Il numero di proprietà è superiore al numero di esempi
* La rete neurale è troppo complessa, quindi  con troppe unità nascoste o strati;
* gli esempi del training set hanno rumore o errori casuali, la rete potrebbe imparare anche questi errori come parte della soluzione ottimale al problema;
* se ci sono poche variazioni nei campioni del dataset (esempio tutti gli oggetti da rilevare nella stessa posizione), la rete potrebbe concentrarsi solo sulle caratteristiche specifiche a quelle posizioni piuttosto che sulle proprietà generalizzate degli oggetti.

### Come evitarlo

Per evitare l’overfitting, è possibile utilizzare tecniche come
* Raccogliere più dati di addestramento (eventualmente fake usando tecniche di [[Data augmentation]]);
* [[Riduzione della Dimensionalità|Ridurre la dimensionalità]] dei dati tramite selezione o estrazione delle caratteristiche;
* Ridurre la complessità della rete, con un minor numero di parametri;
* Introducendo tecniche di [[Regolarizzazione]] del modello (L1-L2 o dropout).
