---
tags:
  - DataScience
---
Le variabili categoriche richiedono tecniche speciali come il one-hot encoding per essere utilizzate efficacemente in modelli di machine learning, mentre le variabili non categoriche possono essere utilizzate direttamente.

L'encoding "one-hot" è una tecnica utilizzata in informatica e nell'analisi dei dati per ==rappresentare le variabili categoriche in modo numerico==.
In parole semplici, il one-hot encoding ==converte le categorie in vettori binari, in cui ogni categoria diventa una colonna e viene rappresentata da un 1 o un 0==.

## Variabili categoriche e non

Le variabili categoriche e le variabili non categoriche sono due tipi principali di variabili utilizzate nella statistica, nell'analisi dei dati e nell'apprendimento automatico (machine learning).

### Variabili Categoriche

1. **Definizione:** Le variabili categoriche, anche conosciute come variabili qualitative o nominali, ==rappresentano categorie o gruppi di oggetti che non hanno un ordine intrinseco o una scala==. Queste categorie sono solitamente descritte da etichette o nomi. Ad esempio, il genere (maschio, femmina, altro), il colore (rosso, verde, blu), il livello di istruzione (scuola elementare, scuola superiore, laurea) sono esempi di variabili categoriche.
2. **Rappresentazione:** Queste variabili vengono solitamente ==rappresentate da etichette o stringhe anziché da numeri==. Nel contesto dell'apprendimento automatico, è necessario convertirle in una forma numerica utilizzando tecniche come il one-hot encoding.
3. **Utilizzo:** Le variabili categoriche sono spesso utilizzate per descrivere caratteristiche o attributi ==che non possono essere misurati su una scala numerica==, ma sono essenziali per l'analisi e la modellazione. Possono essere utilizzate in analisi di segmentazione, classificazione, raggruppamento e altro.

### Variabili Non Categoriche (o Variabili Numeriche)

1. **Definizione:** Le variabili non categoriche, anche chiamate variabili quantitative, rappresentano ==misure o valori che possono essere espressi su una scala numerica==. Queste variabili possono avere valori numerici che possono essere sottoposti a operazioni matematiche come addizione, sottrazione, moltiplicazione, ecc. Ad esempio, l'età di una persona, il reddito annuo, la temperatura, il peso sono esempi di variabili non categoriche.
2. **Rappresentazione:** Queste variabili sono ==rappresentate direttamente da numeri== e possono essere utilizzate in calcoli matematici. Possono essere suddivise ulteriormente in variabili continue (come l'età) o variabili discrete (come il numero di figli).
3. **Utilizzo:** Le variabili non categoriche sono spesso utilizzate per ==misurare quantità o valori su una scala numerica==. Possono essere utilizzate in analisi statistiche, modelli di regressione, analisi dei trend, ecc.

## Funzionamento

Immagina di avere una colonna chiamata "Colore" con tre categorie: Rosso, Verde e Blu. Utilizzando il one-hot encoding, questa colonna verrebbe divisa in tre colonne separate: "Rosso", "Verde" e "Blu". Per ogni riga del dataset, verrà assegnato un valore 1 alla colonna corrispondente al colore presente in quella riga e 0 alle altre colonne.

![[Pasted image 20231027105001.png]]

- Se una riga ha il colore "Rosso", la colonna "Rosso" conterrà un 1 e le altre colonne conterranno 0: (1, 0, 0)
- Se una riga ha il colore "Verde", la colonna "Verde" conterrà un 1 e le altre colonne conterranno 0: (0, 1, 0)
- Se una riga ha il colore "Blu", la colonna "Blu" conterrà un 1 e le altre colonne conterranno 0: (0, 0, 1)

## Esempio

Ecco un esempio di come gestire un `DataFrame` rappresentante magliette con le colonne "Taglia", "Colore" e "Prezzo" in modo che sia facilmente gestibile da un algoritmo di machine learning utilizzando Pandas.
In questo esempio, utilizzeremo il one-hot encoding per la colonna "Colore", faremo un mapping numerico per "Taglia" mentre lasceremo il prezzo così come è in quanto è già un numero comodo.

```python
import pandas as pd

# Creiamo un DataFrame di esempio con magliette
data = {'Taglia': ['S', 'M', 'L', 'XL', 'M'],
        'Colore': ['Rosso', 'Verde', 'Blu', 'Rosso', 'Blu'],
        'Prezzo': [20, 25, 30, 22, 35]}

df = pd.DataFrame(data)

# Mappiamo la taglia a un valore numerico in base all'ordine crescente
taglia_mapping = {'S': 1, 'M': 2, 'L': 3, 'XL': 4}
df['Taglia'] = df['Taglia'].map(taglia_mapping)

# Applichiamo il one-hot encoding solo alla colonna 'Colore'
df_encoded = pd.get_dummies(df, columns=['Colore'])

# Stampiamo il DataFrame elaborato
print(df_encoded)
```

Output:
```
   Taglia  Prezzo  Colore_Blu  Colore_Rosso  Colore_Verde
0       1      20           0            1            0
1       2      25           0            0            1
2       3      30           1            0            0
3       4      22           0            1            0
4       2      35           1            0            0
```

