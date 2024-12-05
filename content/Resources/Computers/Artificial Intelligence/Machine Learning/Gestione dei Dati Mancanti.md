---
tags:
  - DataScience
---
Tipicamente individuiamo i valori mancanti in termini di spazi vuoti nella tabella dei dati oppure come stringhe segnaposto, per esempio valori NaN (Not A Number). 

## Eliminazione

Uno dei modi più semplici per gestire il problema dei valori mancanti consiste nell’eliminare completamente dal dataset le caratteristiche (colonne) o i campioni (righe) corrispondenti; le righe con valori mancanti possono essere eliminate con facilità tramite il metodo `dropna`.
Possiamo eliminare le colonne che hanno almeno un valore NaN in una riga, impostando l’argomento `axis` a 1: `df.dropna(axis=1)`.
Il problema di questo approccio che rischia di rimuovere fin troppi campioni, il che potrebbe pregiudicare del tutto l’affidabilità.
Oppure, se rimuoviamo troppe colonne di caratteristiche, corriamo il rischio di perdere informazioni preziose, delle quali il nostro classificatore ha bisogno per poter discriminare le classi.

```python
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

## Interpolazione

Spesso, la rimozione dei campioni o l’eliminazione di intere colonne di caratteristiche non è una via percorribile, perché potremmo perdere troppi dati preziosi. In questo caso, possiamo utilizzare varie tecniche di interpolazione per stimare i valori mancanti sulla base degli altri campioni del dataset.
Una delle tecniche di interpolazione più comuni è l’imputazione media, mediante la quale sostituiamo semplicemente il valore mancante con il valore medio dell’intera colonna di caratteri della caratteristica.

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

Pandas fornisce anche tecniche più evolute come la stime dei dati mancanti in base ai valori circostanti.
```python
# Esempio di interpolazione lineare
df_interpolated = df.interpolate()

print("DataFrame originale:\n", df)
print("Dopo l'interpolazione:\n", df_interpolated)
```


## Creazione di indicatori (`isna` e `notna`)

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


