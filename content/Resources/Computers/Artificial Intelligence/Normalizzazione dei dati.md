---
tags:
  - DataScience
---
La normalizzazione dei dati è il processo di riduzione delle feature in modo che ==i valori rientrino in un intervallo specifico, di solito tra 0 e 1== in quanto la maggior parte degli algoritmi di machine learning e di ottimizzazione si comporta molto meglio se le caratteristiche adottano sulla stessa scala.

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