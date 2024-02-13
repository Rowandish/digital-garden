---
tags:
  - MachineLearning
---
Gli algoritmi di encoding nel machine learning sono utilizzati per convertire le [[Variabili categoriche e non|variabili categoriche]] in una forma che i modelli di machine learning possano comprendere e utilizzare per fare previsioni.
Le variabili categoriche sono quelle che rappresentano categorie o classi anziché quantità numeriche, come ad esempio il genere, il colore preferito o il tipo di veicolo.

Sono necessari perché ==molti algoritmi di machine learning richiedono input numerici anziché categorici==. Senza l'encoding, i modelli di machine learning non sarebbero in grado di interpretare e utilizzare le variabili categoriche nei dati.

Ecco alcuni dei principali algoritmi di encoding utilizzati nel machine learning:

1. **[[Label Encoding]]**: Converte le categorie in numeri interi univoci, assegnando a ciascuna categoria un valore numerico. È utile quando le categorie hanno un ordine intrinseco.
2. **[[One-Hot Encoding]]**: Crea nuove colonne binarie per ciascuna categoria, assegnando un valore '1' alla presenza della categoria e '0' altrimenti. È utile quando non c'è un ordine intrinseco tra le categorie e si desidera mantenere l'informazione di tutte le categorie.
3. **Binary Encoding**: Converte le categorie in numeri binari e quindi rappresenta ciascun numero binario in una colonna separata. Riduce la dimensionalità dei dati rispetto all'One-Hot Encoding, ma conserva comunque le informazioni sulle categorie.
4. **Ordinal Encoding**: Assegna un numero univoco a ciascuna categoria, ma in base all'ordine delle categorie. È utile quando le categorie hanno un ordine intrinseco, come nelle variabili ordinali.
5. **Frequency Encoding**: Sostituisce ogni categoria con la sua frequenza nel dataset. È utile quando la frequenza delle categorie è importante per il modello.
6. **Target Encoding**: Sostituisce ogni categoria con la media del target corrispondente a quella categoria. È utile quando si desidera catturare la relazione tra le variabili categoriche e il target.