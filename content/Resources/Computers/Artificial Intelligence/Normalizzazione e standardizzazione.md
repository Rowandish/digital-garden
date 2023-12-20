---
tags:
  - DataScience
---
La normalizzazione e la standardizzazione sono due tecniche di preprocessing dei dati utilizzate per ==portare le feature su una scala comune==.
Questo processo è importante per garantire che le feature abbiano un impatto equo sui modelli di machine learning e per far sì che gli algoritmi siano in grado di convergere più rapidamente e di produrre risultati più accurati.

Ecco una spiegazione più dettagliata di ciascuna tecnica, seguita da un esempio in pandas:

## Normalizzazione

La normalizzazione dei dati è il processo di riduzione delle feature in modo che ==i valori rientrino in un intervallo specifico, di solito tra 0 e 1==.
Questa tecnica è particolarmente utile quando si desidera mantenere l'interpretazione delle feature originali in termini di percentuale o proporzione rispetto al massimo valore possibile.

**Esempio:** Supponiamo di avere un dataset di punteggi in un test, con valori che vanno da 0 a 100. Per normalizzare questi dati tra 0 e 1, possiamo utilizzare la formula:

$$X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$$

Dove $X$ è il punteggio originale, $X_{norm}$ è il punteggio normalizzato, $X_{min}$ è il valore minimo dei punteggi nel dataset e $X_{max}$ è il valore massimo dei punteggi.

### Esempio in pandas

```python
import pandas as pd

# Creiamo un DataFrame di esempio
data = {
    'Punteggio': [75, 90, 60, 80, 95]
}

df = pd.DataFrame(data)

# Normalizziamo la feature 'Punteggio' tra 0 e 1
df['Punteggio_norm'] = (df['Punteggio'] - df['Punteggio'].min()) / (df['Punteggio'].max() - df['Punteggio'].min())

print(df)
```

## Standardizzazione dei dati

La standardizzazione dei dati è il processo di ==trasformazione delle feature in modo che abbiano una media zero e una deviazione standard 1==.
Questa tecnica è spesso utilizzata quando ==si desidera che le feature abbiano una distribuzione normale== (a campana) e quando gli algoritmi di machine learning sono sensibili alle differenze di scala.

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