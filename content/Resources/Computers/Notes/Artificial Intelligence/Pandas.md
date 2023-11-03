---
tags:
  - Python
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

## Installazione

Pandas può essere installato facilmente utilizzando PIP, il gestore di pacchetti Python. Ecco come farlo:

```bash
pip install pandas
```

Dopo l'installazione, è possibile importare Pandas nel proprio codice Python utilizzando il seguente comando:

```python
import pandas as pd
```

## `Series` e `DataFrame`

Un concetto fondamentale in Pandas è la differenza tra `Series` e `DataFrame`.
Entrambi sono strutture dati fondamentali per l'analisi dei dati in Pandas, ma differiscono per la loro dimensionalità e utilizzo.

### Series
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

### `DataFrame`

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
data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Età': [25, 30, 35, 40, 45]}
df = pd.DataFrame(data)
print(df)
```

I `DataFrame` offrono una flessibilità incredibile nella gestione e nell'analisi dei dati: è possibile eseguire una vasta gamma di operazioni, tra cui filtraggio, selezione, raggruppamento, aggregazione, calcolo di statistiche, operazioni di join e molto altro.

### Operazioni Comuni

Ecco alcune delle operazioni comuni eseguite su `Serie` e `DataFrame` in Pandas:

**Selezione di Colonne:**

```python
# Selezione di una colonna in un DataFrame
colonna = df['Nome']

# Selezione di una colonna in una Serie
elemento = serie[2]
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
# Unione di due DataFrame per colonne
df1 = pd.DataFrame({'Chiave': ['A', 'B'], 'Valore1': [1, 2]})
df2 = pd.DataFrame({'Chiave': ['B', 'C'], 'Valore2': [3, 4]})
risultato = pd.merge(df1, df2, on='Chiave')
```

## Lettura e Scrittura di Dati

Pandas semplifica la lettura e la scrittura di dati da e verso vari formati. Ecco come è possibile importare un file CSV in un DataFrame:

```python
df = pd.read_csv('dati.csv')
```

Ecco come è possibile esportare un DataFrame in un file CSV:

```python
df.to_csv('dati_salvati.csv', index=False)
```

## Selezione e Indicizzazione

Pandas offre molteplici opzioni per selezionare e indicizzare dati in un `DataFrame` o in una Serie.
Ad esempio, è possibile selezionare colonne specifiche utilizzando il nome della colonna:

```python
nome_colonna = df['Nome']
```

Questa operazione è possibile in quanto pandas legge automaticamente la prima riga del csv e associa le varie colonne con il nome della colonna letta da csv.
Qualora il CSV non abbia la prima riga che definisce le colonne oppure vogliamo definirne dei nomi diversi possiamo fare in questo modo

```python
```python
df = pd.read_csv("tuofile.csv", header=None, names=["NomeColonna1", "NomeColonna2", "NomeColonna3"])
```

È possibile selezionare righe specifiche utilizzando l'indicizzazione:

```python
riga = df.iloc[2]  # Seleziona la terza riga
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

## Esempi

Ecco alcuni esempi di analisi dati tipici utilizzando Pandas:

**Calcolo delle Statistiche di Base:**

```python
media_età = df['Età'].mean()
massima_età = df['Età'].max()
minima_età = df['Età'].min()
```

**Visualizzazione dei Primi N Record:**

```python
primi_5_record = df.head(5)
```

**Conta delle Occorrenze:**

```python
conteggio_nomi = df['Nome'].value_counts()
```

**Concatenazione di DataFrames:**

```python
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']})
df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'], 'B': ['B3', 'B4', 'B5']})
risultato = pd.concat([df1, df2])
```

**Fusione di DataFrames:**

```python
df1 = pd.DataFrame({'chiave': ['A', 'B', 'C'], 'valore1': [1, 2, 3]})
df2 = pd.DataFrame({'chiave': ['B', 'C', 'D'], 'valore2': [4, 5

, 6]})
risultato = pd.merge(df1, df2, on='chiave')
```

**Estrazione di Statistiche Descrittive:**

```python
statistiche_descrittive = df.describe()
```