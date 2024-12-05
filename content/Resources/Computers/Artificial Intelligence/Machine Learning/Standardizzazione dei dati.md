---
tags:
  - DataScience
---
La standardizzazione dei dati è il processo di ==trasformazione delle feature in modo che abbiano una media zero e una deviazione standard 1==  in quanto la maggior parte degli algoritmi di machine learning e di ottimizzazione si comporta molto meglio se le caratteristiche adottano sulla stessa scala.
Questa tecnica è spesso utilizzata quando ==si desidera che le feature abbiano una distribuzione normale== (a campana) e quando gli algoritmi di machine learning sono sensibili alle differenze di scala.
La standardizzazione mantiene informazioni utili riguardo alle anomalie e rende l’algoritmo meno sensibile a questo problema rispetto alla [[Normalizzazione dei dati|riduzione in scala min-max]], che riporta i dati a un intervallo limitato di valori.

**Esempio:** Supponiamo di avere un dataset di altezze in centimetri. Per standardizzare questi dati, possiamo utilizzare la formula:

$$X_{std} = \frac{X - \mu}{\sigma}$$

Dove $X$ è l'altezza originale, $X_{std}$ è l'altezza standardizzata, $\mu$ è la media delle altezze nel dataset e $\sigma$ è la deviazione standard delle altezze.

**Esempio in pandas:**

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Creiamo un DataFrame di esempio
data = {
    'Altezza': [170, 165, 180, 160, 175]
}

df = pd.DataFrame(data)

# Standardizziamo la feature 'Altezza' con StandardScaler di scikit-learn
scaler = StandardScaler()
df['Altezza_std'] = scaler.fit_transform(df[['Altezza']])

print(df)
```

In questo esempio, abbiamo utilizzato il `StandardScaler` di scikit-learn per standardizzare la feature 'Altezza' in modo che abbia una media zero e una deviazione standard unitaria.