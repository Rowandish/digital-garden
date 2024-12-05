---
tags:
  - MachineLearning
---
Il Label Encoding è un modo per ==convertire le [[Variabili categoriche e non|variabili categorie]] ordinali (che hanno quindi un ordine intrinseco) in numeri==.
Le variabili vengono trasformate in numeri con un ordine preciso ma questo ordine riflette la realtà, quindi va bene.
Qualora invece le variabili fossero nominali, quindi non hanno un ordine intrinseco come per esempio il colore di una maglietta, allora è necessario procedere con l'[[One-hot encoding]].

Immagina di avere una variabile 'Livello di Istruzione' con le categorie 'Scuola Elementare', 'Scuola Media', 'Diploma', 'Laurea', 'Master', e 'Dottorato'.
Utilizzando il Label Encoding, assegneremo a ciascuna categoria un numero unico in base all'ordine: ad esempio, 'Scuola Elementare' potrebbe essere codificata come 0, 'Scuola Media' come 1, 'Diploma' come 2 e così via fino a 'Dottorato' che potrebbe essere codificata come 5. 

| Livello di Istruzione | Livello di Istruzione_LabelEncoded |
|-----------------------|------------------------------------|
| Scuola Elementare     | 0                                  |
| Scuola Media          | 1                                  |
| Diploma               | 2                                  |
| Laurea                | 3                                  |
| Master                | 4                                  |
| Dottorato             | 5                                  |


```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd

# Esempio di dati per il Label Encoding
livello_istruzione = ['Scuola Elementare', 'Scuola Media', 'Diploma', 'Laurea', 'Master', 'Dottorato']

# Creazione di un DataFrame con la variabile 'Livello di Istruzione'
df_label_encoding = pd.DataFrame({'Livello di Istruzione': livello_istruzione})

# Inizializzazione del LabelEncoder
label_encoder = LabelEncoder()

# Applicazione del LabelEncoder alla colonna 'Livello di Istruzione'
df_label_encoding['Livello di Istruzione_LabelEncoded'] = label_encoder.fit_transform(df_label_encoding['Livello di Istruzione'])

print("Dati con Label Encoding:")
print(df_label_encoding)
```