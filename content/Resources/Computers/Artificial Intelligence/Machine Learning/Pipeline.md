---
tags:
  - MachineLearning
  - Python
---
`Pipeline` è un oggetto molto utile che consente di ==concatenare più trasformazioni di dati e modelli di machine learning in un'unica sequenza==. Questo è particolarmente utile quando si lavora con flussi di lavoro complessi che coinvolgono molteplici passaggi di pre-elaborazione dei dati e modelli di apprendimento automatico.

L’oggetto Pipeline accetta in input un elenco di tuple, dove il primo valore di ciascuna tupla è un identificatore stringa arbitrario, che possiamo utilizzare per accedere ai singoli elementi della pipeline, e il secondo elemento di ogni tupla è un trasformatore o estimatore scikit-learn. I passi intermedi di una pipeline costituiscono i trasformatori scikit-learn e l’ultimo passo è un estimatore.

Ad esempio, immagina di dover costruire un modello di classificazione utilizzando un insieme di dati. Prima di addestrare il modello, potresti dover eseguire diverse operazioni di pre-elaborazione come la standardizzazione delle caratteristiche e la riduzione della dimensionalità. Successivamente, potresti voler applicare un modello di classificazione come Support Vector Machine (SVM) per fare previsioni.

Ecco un esempio di come potresti utilizzare `Pipeline` in scikit-learn per questo scopo:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Carica il dataset (ad esempio il dataset Iris)
iris = load_iris()
X = iris.data
y = iris.target

# Dividi il dataset in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definisci i passaggi della pipeline
steps = [
    ('scaler', StandardScaler()),  # Standardizzazione delle caratteristiche
    ('pca', PCA(n_components=2)),  # Riduzione della dimensionalità con PCA
    ('classifier', SVC())  # Modello di classificazione (Support Vector Machine)
]

# Crea la pipeline
pipeline = Pipeline(steps)

# Addestra il modello utilizzando la pipeline
pipeline.fit(X_train, y_train)

# Valuta il modello
accuracy = pipeline.score(X_test, y_test)
print("Accuracy:", accuracy)
```

In questo esempio, stiamo costruendo una pipeline per la classificazione utilizzando il dataset Iris. La pipeline include tre passaggi:

1. `StandardScaler`: questo passaggio [[Standardizzazione dei dati|standardizza]] le caratteristiche rimuovendo la media e riducendo la varianza in modo che tutte le caratteristiche abbiano una varianza unitaria. Questo è importante quando si utilizzano algoritmi sensibili alla scala delle caratteristiche, come le SVM.
2. `PCA`: questo passaggio esegue la [[Riduzione della Dimensionalità]] utilizzando l'analisi delle componenti principali (PCA) per proiettare i dati in un nuovo spazio di dimensioni inferiori. In questo esempio, stiamo riducendo la dimensionalità a 2 per facilitare la visualizzazione, ma in pratica il numero di componenti principali potrebbe essere scelto in modo più accurato.
3. `SVC`: infine, applichiamo un modello di classificazione Support Vector Machine (SVM) per fare previsioni sul dataset.

Con la pipeline definita, possiamo addestrare il modello chiamando il metodo `fit` e valutarlo chiamando il metodo `score` utilizzando i dati di test. La pipeline si occupa automaticamente di eseguire tutte le trasformazioni di dati necessarie prima di addestrare il modello, rendendo il flusso di lavoro molto più pulito e organizzato.