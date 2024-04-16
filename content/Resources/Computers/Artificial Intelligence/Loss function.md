---
tags:
  - DeepLearning
---
La loss function (o funzione di costo) rappresenta quanto il nostro modello si sbaglia nelle sue previsioni rispetto ai dati di addestramento. L'obiettivo durante l'addestramento è minimizzare questa funzione di costo, tramite gli [[Algoritmi di ottimizzazione]] cercando di rendere le previsioni del modello il più accurate possibile.

## Errore quadratico medio 

L'errore quadratico medio (MSE, Mean Squared Error) è una misura comune di quanto un modello di machine learning si discosti dalla verità nei suoi output predetti.
Viene utilizzato per valutare la precisione di un modello rispetto ai dati di addestramento o di test.
L'MSE calcola ==la media dei quadrati delle differenze tra i valori predetti dal modello e i valori effettivi nei dati==.

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

Dove:
- $n$ è il numero totale di campioni nei dati.
- $y_i$ rappresenta il valore effettivo del campione $i$.
- $\hat{y}_i$ rappresenta il valore predetto dal modello per il campione $i$.

Nel machine learning, l'MSE è ampiamente utilizzato come ==funzione di costo per la regressione, dove l'obiettivo è predire un valore continuo==, come ad esempio prevedere il prezzo di una casa basandosi su diverse caratteristiche.
L'obiettivo dell'addestramento di un modello di regressione è quello di minimizzare l'MSE, ovvero ridurre l'errore quadratico medio tra le previsioni del modello e i dati effettivi.

Ecco un esempio di utilizzo di Keras per addestrare un modello di regressione utilizzando l'errore quadratico medio come funzione di costo:

```python
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import numpy as np

# Genera dati di esempio
X = np.random.rand(100, 1)
y = 2 * X + 1 + 0.1 * np.random.randn(100, 1)

# Crea un modello sequenziale
model = Sequential()
model.add(Dense(1, input_dim=1))

# Compila il modello utilizzando l'MSE come funzione di costo
model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.01))

# Addestra il modello
model.fit(X, y, epochs=100, verbose=0)

# Effettua previsioni
predictions = model.predict(X)

# Valuta l'errore quadratico medio
mse = np.mean((predictions - y) ** 2)
print("Mean Squared Error:", mse)
```

### MSE standardizzato
L'MSE standardizzato, noto come coefficiente di determinazione $(R^2$), misura la frazione della varianza nei dati che è spiegata dal modello.
Un valore più alto di $R^2$ indica che il modello si adatta meglio ai dati. La formula per $R^2$ è la seguente in formato LaTeX:

$$R^2 = 1 - \frac{\text{MSE del modello}}{\text{Varianza dei dati effettivi}}$$

Di seguito un esempio di calcolo di $R^2$ in Python:

```python
from sklearn.metrics import r2_score

# Calcola l'R^2
r2 = r2_score(y, predictions)
print("R-squared (R^2):", r2)
```

Un valore di $R^2$ vicino a 1 indica che il modello spiega una grande parte della varianza nei dati, mentre un valore vicino a 0 indica che il modello non spiega la varianza nei dati ed è conseguentemente inutile.

 l'[[Errore quadratico medio]] (MSE)


## Altre
- **Errore assoluto medio (Mean Absolute Error - MAE):** MAE calcola la media delle differenze assolute tra le previsioni del modello e i valori reali. Anch'essa è utilizzata in problemi di regressione.
- **Entropia incrociata (Cross-Entropy o Log Loss):** Questa funzione di costo è comune nei problemi di classificazione. Misura la discrepanza tra le previsioni del modello e le etichette reali assegnando penalità più alte per le previsioni errate.
- **Hinge Loss (o Support Vector Machine Loss):** Utilizzata spesso in problemi di classificazione binaria, è associata ai support vector machines e misura la classificazione errata dei campioni.
- **Huber Loss:** Una combinazione di MSE e MAE, che è meno sensibile agli outlier rispetto all'errore quadratico medio.
- **Log-Cosh Loss:** Simile all'errore quadratico medio, ma con una penalità più morbida per i valori di errore elevati.