---
tags:
  - DataScience
---
Pandas è una potente libreria open-source per la ==manipolazione e l'analisi dei dati in Python==.
È ampiamente utilizzata nel mondo dell'analisi dati, del machine learning e della data science per la gestione di dati strutturati e tabellari.
La libreria fornisce strumenti flessibili e intuitivi per importare, esplorare, pulire, trasformare e analizzare dati in modo efficace.

## Caratteristiche

Pandas offre diverse caratteristiche che la rendono una libreria indispensabile per l'analisi dei dati:

1. **Strutture Dati Potenti:** Pandas introduce due principali strutture dati, il DataFrame e la Serie. Il DataFrame è una tabella bidimensionale simile a un foglio di calcolo, mentre la Serie è un array unidimensionale con etichette.
2. **Importazione e Esportazione dei Dati:** Pandas supporta una vasta gamma di formati dati, inclusi CSV, Excel, SQL, JSON, HTML e molti altri. È possibile importare dati da molte fonti diverse e esportare i risultati in vari formati.
3. **Indicizzazione Etichettata:** Pandas consente di assegnare etichette personalizzate alle righe e alle colonne dei DataFrame, semplificando la ricerca e l'accesso ai dati.
4. **Operazioni Flessibili:** Pandas offre numerosi metodi per la manipolazione dei dati, tra cui selezione, filtraggio, ordinamento, raggruppamento, aggregazione e molto altro. È possibile applicare queste operazioni in modo semplice e intuitivo.
5. **Gestione di Dati Mancanti:** La libreria offre strumenti avanzati per la gestione dei dati mancanti, consentendo di riempire, rimuovere o sostituire i valori mancanti in modo efficace.
6. **Integrazione con NumPy:** Pandas è integrato con NumPy, un'altra libreria fondamentale per l'analisi dei dati in Python. Ciò significa che è possibile utilizzare le funzionalità di NumPy all'interno di Pandas.



## DataFrame

Un ==`DataFrame` è una struttura dati bidimensionale simile a una tabella o uno spreadsheet. È composto da righe e colonne, e ogni colonna può contenere dati di tipo diverso==.
Un `DataFrame` è fondamentalmente una raccolta di `Serie`, dove ogni colonna rappresenta una Serie. Ecco alcune caratteristiche principali dei `DataFrame`:

1. **Dati Ibridi:** I `DataFrame` possono contenere dati eterogenei, il che significa che le colonne possono contenere diversi tipi di dati.
2. **Indici delle Righe e Etichette delle Colonne:** I DataFrame hanno indici per le righe e etichette per le colonne, consentendo un accesso flessibile ai dati.
3. **Operazioni su Colonne e Righe:** È possibile eseguire operazioni su singole colonne o su righe intere del DataFrame.
4. **Utilizzo:** I `DataFrame` sono ampiamente utilizzati per rappresentare e analizzare dati tabellari, come i dati di un database o di un file CSV. Sono la struttura dati più comunemente utilizzata in Pandas.

Ecco come creare un DataFrame in Pandas:

```python
import pandas as pd

# Creazione di un DataFrame da un dizionario
df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(df)
```

I `DataFrame` offrono una flessibilità incredibile nella gestione e nell'analisi dei dati: è possibile eseguire una vasta gamma di operazioni, tra cui filtraggio, selezione, raggruppamento, aggregazione, calcolo di statistiche, operazioni di join e molto altro.

#### `read_csv`
L'operazione più comune per creare un dataframe è tramite un csv tramite il comando `read_csv`
```python
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")
```
Qualora il csv contenga già una colonna per l'indice, per esempio un csv di una tabella compresa la colonna `id` possiamo utilizzare il parametro `index_col` per esplicitare la colonna contenente tale indice
```python
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
```

#### Informazioni sul dataframe
* `shape`: permette di sapere numero di righe e colonne
* `describe`: offre panoramica dei dati, quindi, per ogni colonna, il numero di elementi, la media, la std e il numero di elementi al 25, 50 e 75 percentile, oltre che al numero più alto.


### Indexing

#### Index based

Pandas permette di selezionare un dati a partire dalla loro posizione all'intero del dataframe usando la funzione `iloc` utilizzando l'indice di dove si trova il dato che mi serve.
Attenzione che la notazione è prima la riga e successivamente la colonna e non il contrario come avviene in python classico.
Alcuni esempi:
* Ottenere la prima riga: `data.iloc[0]`
* Ottenere la prima colonna: `data.iloc[:, 0]`
* Ottieni le prime 3 righe della prima colonna: `data.iloc[:3, 0]`
* Ottieni le ultime 5 righe della prima colonna: `data.iloc[-5:, 0]`
* Ottieni la seconda e la terza riga della prima colonna: `data.iloc[1:3, 0]`

`iloc` utilizza lo schema di indicizzazione stdlib di Python, in cui il primo elemento dell'intervallo è incluso e l'ultimo escluso. Quindi `0:10` selezionerà le voci `0,...,9`.

#### Label based

Pandas permette di selezionare un dati a partire dalla loro posizione all'intero del dataframe usando la funzione `loc` utilizzando la label di dove si trova il dato che mi serve.
Per esempio se voglio ottenere il contenuto della cella della colonna `country` della prima riga di un dataframe scrivo `reviews.loc[0, 'country']`.
Dato che spesso i dataset hanno label spesso è più comodo usare il metodo `loc`, per esempio qui seleziono solo un sottoinsieme di colonne identificate da un name: `reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

`loc`, indicizza in modo inclusivo a differenza di `iloc`. Quindi `0:10` selezionerà le voci `0,...,10.

`loc` può essere usata anche insieme a dei filtraggi, per esempio per sapere tutti i vini italiani con punteggio maggiore di 90 posso fare `reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]`.
Posso usare anche il metodo `isin` per scrivere un filtraggio in OR, per esempio questo comando fornisce tutti i vini italiani o francesi `reviews.loc[reviews.country.isin(['Italy', 'France'])]`.


### Operazioni Comuni

Ecco alcune delle operazioni comuni eseguite su `Serie` e `DataFrame` in Pandas:

#### Selezione di una colonna
Una delle operazioni più comuni  è la selezione di una colonna, per esempio se voglio selezionare la colonna su cui voglio fare le predizioni.
Esistono due notazioni per selezionare una colonna
```python
# Standard notation
colonna = df["Nome"]
# Dot notation
colonna = df.Nome
```
e la più moderna è sicuramente la dot-notation.
#### Selezione di una serie di colonne
Qualora voglia considerare solo un sottoinsieme delle colonna del dataframe di partenza posso definire il sottoinsieme come una array di stringhe di nomi e poi usare la seguente sintassi:
```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
# X contiene solo le colonne definite sopra
X = melbourne_data[melbourne_features]
```

#### Primi n dati
```python
primi_5_record = df.head(5)
```

**Filtraggio dei Dati:**

```python
# Filtraggio dei dati in base a una condizione
df_filtrato = df[df['Età'] > 30]
```

**Operazioni Aggregazione:**

```python
# Calcolo della media per una colonna
media_età = df['Età'].mean()
```

**Aggiunta di Nuove Colonne:**

```python
# Aggiunta di una nuova colonna basata su calcoli
df['Anno_di_Nascita'] = 2023 - df['Età']
```

**Raggruppamento e Aggregazione:**

```python
# Raggruppamento per una colonna e calcolo della media
media_età_per_nome = df.groupby('Nome')['Età'].mean()
```

**Unione di DataFrame:**

```python
# Concat (semplice)
canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")
pd.concat([canadian_youtube, british_youtube])

# Join (medio): combina dataframe che hanno un index in comune. Permette di aggiungere suffissi per le colonne comuni

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')

# Merge (complesso)
df1 = pd.DataFrame({'Chiave': ['A', 'B'], 'Valore1': [1, 2]})
df2 = pd.DataFrame({'Chiave': ['B', 'C'], 'Valore2': [3, 4]})
risultato = pd.merge(df1, df2, on='Chiave')
```


## Series
Una `Serie` in Pandas è una ==struttura dati unidimensionale che può contenere dati di qualsiasi tipo ma omogenei==, tra cui numeri interi, float, stringhe, oggetti complessi e altro. Come fosse un array di un linguaggio fortemente tipizzato.
Ogni elemento in una Serie è associato a un'etichetta o un indice.
Gli indici possono essere etichette personalizzate o interi predefiniti che iniziano da zero.
Ecco alcune caratteristiche principali delle `Serie`:

1. **Dati Omogenei:** Le Serie contengono dati omogenei, il che significa che tutti gli elementi devono essere dello stesso tipo di dati.
2. **Etichette degli Indici:** Ogni elemento della Serie ha un'etichetta di indice che consente di accedere a un elemento specifico.
3. **Operazioni Vettoriali:** Le operazioni su Serie in Pandas sono in genere vettoriali, il che significa che è possibile eseguire operazioni su tutta la Serie in modo efficiente.
4. **Utilizzo:** Le Serie sono utilizzate per rappresentare una singola colonna di dati e sono spesso utilizzate in contesti in cui è necessario lavorare con una singola dimensione di dati, ad esempio le altezze di una lista di persone.

Ecco come creare una Serie in Pandas:

```python
import pandas as pd

# Creazione di una Serie
serie = pd.Series([10, 20, 30, 40, 50])
print(serie)
```



## Operazioni

Pandas permette di eseguire varie operazioni sui dati, tra cui il filtraggio dei dati, il raggruppamento, l'aggregazione e il calcolo di statistiche.

### Filtraggi

Ad esempio, è possibile filtrare le righe del `DataFrame` in base a una condizione:

```python
df_filtrato = df[df['Età'] > 30]
```


### Raggruppamenti

È possibile raggruppare i dati in base a una colonna e calcolare la media:

```python
media_eta_per_nome = df.groupby('Nome')['Età'].mean()
```

### Gestione dei Dati Mancanti

Pandas fornisce strumenti per gestire dati mancanti, inclusi i metodi `dropna()` per rimuovere righe o colonne con dati mancanti e `fillna()` per riempire valori mancanti con dati specifici.

```python
# Rimuove le righe con dati mancanti
df_senza_dati_mancanti = df.dropna()

# Riempie i dati mancanti con un valore specifico
df_riempito = df.fillna(0)
```

### Rimozione di righe o colonne

La funzione `drop` in Pandas viene utilizzata per eliminare righe o colonne da un DataFrame. Per farlo, è necessario specificare l'etichetta delle righe o delle colonne che si desidera rimuovere

#### Eliminare righe

```python
import pandas as pd

# Creare un DataFrame di esempio
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Eliminare la riga con indice 1
df = df.drop(1)

# Il risultato sarà un DataFrame senza la riga con indice 1
print(df)
```

Output:
```
   A  B
0  1  4
2  3  6
```

#### Eliminare colonne

```python
# Creare un DataFrame di esempio
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Eliminare la colonna 'B'
df = df.drop('B', axis=1)

# Il risultato sarà un DataFrame senza la colonna 'B'
print(df)
```

Output:
```
   A
0  1
1  2
2  3
```

Nell'esempio sopra, abbiamo rimosso la colonna 'B' dal DataFrame `df`.
È importante notare che abbiamo specificato `axis=1` per indicare che vogliamo eliminare una colonna. Se non specifichi `axis`, il comportamento predefinito sarà eliminare righe.

Puoi anche eliminare più righe o colonne passando una lista di etichette:

```python
import pandas as pd

# Creare un DataFrame di esempio
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Eliminare più colonne
df = df.drop(['B', 'C'], axis=1)

# Il risultato sarà un DataFrame senza le colonne 'B' e 'C'
print(df)
```

#### Calcolo delle Statistiche di Base

```python
media_età = df['Età'].mean()
massima_età = df['Età'].max()
minima_età = df['Età'].min()
conteggio_nomi = df['Nome'].value_counts()
```

#### Lettura e scrittura
```python
df = pd.read_csv('dati.csv')
df.to_csv('dati_salvati.csv', index=False)
```