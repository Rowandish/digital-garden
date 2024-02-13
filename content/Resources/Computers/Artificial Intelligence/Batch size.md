---
tags:
  - DeepLearning
---
La dimensione del batch è la quantità di dati di addestramento utilizzata in ogni [[Epoche|epoca]] che viene fornita all'[[Algoritmi di ottimizzazione|algoritmo di ottimizzazione]] al fine di aggiornare i pesi.
Per esempio con un batch size uguale a 1, i pesi vengono aggiornati ad ogni iterazione con l'utilizzo di un singolo esempio mentre con un batch size maggiore come 10 o più, i pesi vengono tenuti in memoria e alla fine del batch (ovvero dopo aver processato tutti gli esempi all'interno del minibatch) viene calcolata la media dei gradienti ottenuti dalle varie iterazioni e quindi utilizzata per l'aggiornamento dei pesi.

## Full batch
Full batch significa che l'intero set di addestramento viene utilizzato per calcolare il gradiente della funzione di costo.
Il vantaggio principale è che utilizza tutte le informazioni disponibili per aggiornare i pesi, quindi la direzione del gradiente è più accurata.
Gli svantaggi sono:
* Inefficienza per dataset grandi, dato che devono caricare l'intero dataset in ram per fornirlo all'algoritmo
* Poco dinamico: per migliorare il modello con nuovi dati bisogna riaddestrarlo sull'intero dataset;
* Rischio di incorrere in un minimo locale.
L'esempio classico è il [[Algoritmi di ottimizzazione#^119eb8|Full Batch Gradient Descent]].

## Batch size = 1
Se la batch size è piccola l'algoritmo pesa poco in memoria ed è molto dinamico, in quanto per aggiornare il modello con nuovi dati basta eseguire uno step dell'SGD solo su questi nuovi dati.
Inoltre date le fluttuazioni della funzione di costo posso evitare i minimi locali.
Il problema è che può essere "rumoroso" a causa dell'alta variabilità nei singoli esempi.
L'esempio classico è il [[Algoritmi di ottimizzazione#^29ecb9|Stochastic Gradient Descent (SGD)]].

## Batch size = n

La dimensione dei dati di addestramento da utilizzare per calcolare il gradiente e aggiornare i pesi è pari a *n*.
Un buon compromesso tra l'efficienza computazionale del SGD e la stabilità del Full Batch Gradient Descent.
L'esempio classico è il [[Algoritmi di ottimizzazione#^41654a|Mini Batch Gradient Descent]].
I valori consigliati di batch size sono 32, 64, 128, 256 e 512.
## TensorFlow
In TensorFlow posso definire la dimensione del batch nel metodo `fit`.
```python
batch_size = 32
model.fit(train_data, train_labels, batch_size=batch_size, epochs=num_epochs)
```