---
tags:
  - DataScience
---
Pandas offre diverse tecniche per gestire dati mancanti (noti anche come "valori mancanti" o "valori NaN").

## Eliminazione dei dati mancanti (`dropna`)

Questa tecnica consiste nel rimuovere le righe o colonne che contengono dati mancanti.

```python
import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8]}

df = pd.DataFrame(data)

# Rimuovi le righe con dati mancanti
df_dropna_rows = df.dropna()

# Rimuovi le colonne con dati mancanti
df_dropna_columns = df.dropna(axis=1)
```

```
DataFrame originale:
     A    B
0  1.0  5.0
1  2.0  NaN
2  2.0  NaN
3  4.0  8.0

Dopo la rimozione delle righe con dati mancanti:
     A    B
0  1.0  5.0
3  4.0  8.0

Dopo la rimozione delle colonne con dati mancanti:
     A
0  1.0
1  2.0
2  NaN
3  4.0
```

## Sostituzione dei dati mancanti (`fillna`)

Questa tecnica consiste nel riempire i dati mancanti con valori specifici, come la media, la mediana o un valore personalizzato.

```python
# Riempimento dei dati mancanti con la media della colonna
df_fillna_mean = df.fillna(df.mean())

# Riempimento dei dati mancanti con un valore personalizzato (ad esempio, 0)
df_fillna_custom = df.fillna(0)
```

```
DataFrame originale:
     A    B
0  1.0  5.0
1  2.0  NaN
2  NaN  7.0
3  4.0  8.0

Dopo il riempimento dei dati mancanti con la media:
     A    B
0  1.0  5.0
1  2.0  6.67
2  2.33  7.0
3  4.0  8.0

Dopo il riempimento dei dati mancanti con un valore personalizzato:
     A    B
0  1.0  5.0
1  2.0  0.0
2  0.0  7.0
3  4.0  8.0
```

## Interpolazione (`interpolate`)

Questa tecnica permette di stimare i dati mancanti in base ai valori circostanti.
```python
# Esempio di interpolazione lineare
df_interpolated = df.interpolate()

print("DataFrame originale:\n", df)
print("Dopo l'interpolazione:\n", df_interpolated)
```

## Creazione di indicatori di dati mancanti (`isna` e `notna`)

Questa tecnica consiste nel creare colonne ausiliarie per indicare la presenza o l'assenza di dati mancanti.

```python
# Creazione di colonne ausiliarie per indicare i dati mancanti
df['A_missing'] = df['A'].isna()
df['B_present'] = df['B'].notna()

print("DataFrame con indicatori:\n", df)
```

```
     A    B  A_missing  B_present
0  1.0  5.0      False       True
1  2.0  NaN      False      False
2  NaN  7.0       True       True
3  4.0  8.0      False       True
```

## Riemissione (`ffill` e `bfill`)

Questa tecnica riempie i dati mancanti con i valori precedenti (`ffill`) o successivi (`bfill`) nella stessa colonna.

```python
# Riemissione dei dati mancanti utilizzando il valore precedente
df_ffill = df.ffill()

# Riemissione dei dati mancanti utilizzando il valore successivo
df_bfill = df.bfill()
```

```
DataFrame originale:
     A    B
0  1.0  5.0
1  2.0  NaN
2  NaN  7.0
3  4.0  8.0

Dopo la riemissione (ffill):
     A    B
0  1.0  5.0
1  2.0  5.0
2  2.0  7.0
3  4.0  8.0

Dopo la riemissione (bfill):
     A    B
0  1.0  5.0
1  2.0  7.0
2  4.0  7.0
3  4.0  8.0
```


