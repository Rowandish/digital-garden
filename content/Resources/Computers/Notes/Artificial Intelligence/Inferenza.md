---
tags:
  - MachineLearning
---
L'inferenza sulla [[Rete neurale convoluzionale]] (CNN) è il processo di utilizzo della CNN per effettuare previsioni su nuovi dati, dopo che la rete è stata addestrata sui dati di training. L'obiettivo dell'inferenza è quello di utilizzare la CNN per classificare o fare previsioni su nuovi input in modo efficiente e preciso.

Durante l'addestramento della CNN, i pesi dei nodi vengono regolati in base ai dati di training, al fine di minimizzare una funzione costo specifica. Una volta completato l'addestramento, i pesi sono fissati e la CNN viene usata per fare inferenze sui nuovi dati entranti nel sistema AI.

In pratica, durante l'inferenza sulla rete neurale convoluzionale, ==l'algoritmo elabora un nuovo input attraverso le varie fasi del modello: prima passando attraverso uno strato convoluzionale che estrae le caratteristiche distintive dell’immagine , poi attraverso uno strato totalmente connesso che combina queste informazioni in una serie di valori numerici corrispondenti alle probabilità delle etichette degli oggetti rilevati nell’immagine==.

Il risultato finale dell'inferenza sarà quindi un output contenente le probabilità associate a ciascuna classe possibile degli oggetti presenti nell'immagine analizzata.
Queste probabilità possono essere poi confrontate con soglie predefinite per determinare se gli oggetti individuati dall'algoritmo soddisfano i criteri stabiliti dal progetto AI cui appartiene il sistema implementativo YOLO .