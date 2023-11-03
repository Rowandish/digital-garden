---
tags:
  - Python
---
I set e i `frozenset` sono due tipi di collezioni in Python utilizzate per rappresentare insiemi di elementi univoci.

## Set

==Un set in Python è una collezione non ordinata di elementi univoci.
Questo significa che, a differenza delle [[List - Python|liste]] o delle tuple, un set non può contenere duplicati.==
I set sono implementati utilizzando una struttura dati detta "hash table", che consente di eseguire operazioni di inserimento, rimozione e verifica della presenza di un elemento in tempo quasi costante.
I set sono mutabili, il che significa che è possibile modificarli dopo la loro creazione.

Ecco come è possibile creare un set in Python:

```python
# Creazione di un set
my_set = {1, 2, 3, 4, 5}
```

In questo esempio, abbiamo creato un set denominato `my_set` contenente cinque elementi. Nota che utilizziamo le parentesi graffe `{}` per definire un set.

I set supportano una serie di operazioni comuni, tra cui:

- **Aggiunta di elementi**: Puoi aggiungere un elemento a un set utilizzando il metodo `add()`.
```python
my_set.add(6)
```

- **Rimozione di elementi**: Puoi rimuovere un elemento da un set utilizzando il metodo `remove()`.
```python
my_set.remove(3)
```

- **Unione di set**: Puoi unire due set utilizzando l'operatore di unione `|` o il metodo `union()`.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Oppure union_set = set1.union(set2)
```

- **Intersezione di set**: Puoi ottenere l'intersezione di due set utilizzando l'operatore di intersezione `&` o il metodo `intersection()`.
```python
intersection_set = set1 & set2  # Oppure intersection_set = set1.intersection(set2)
```

- **Differenza di set**: Puoi ottenere la differenza tra due set utilizzando l'operatore di differenza `-` o il metodo `difference()`.
```python
difference_set = set1 - set2  # Oppure difference_set = set1.difference(set2)
```

- **Verifica della presenza di un elemento**: Puoi verificare se un elemento è presente in un set utilizzando l'operatore `in`.
```python
element_present = 3 in set1  # Restituirà True
```

- **Iterazione sui set**: Puoi iterare sugli elementi di un set utilizzando un ciclo `for`.
```python
for element in my_set:
    print(element)
```

## `frozenset`

A differenza dei set, ==i `frozenset` in Python sono immutabili, il che significa che non è possibile modificarli dopo la loro creazione==.
Questo li rende utili quando è necessario garantire che un insieme di elementi rimanga costante nel tempo.
I `frozenset` sono implementati utilizzando una struttura dati simile a un set, ma questa struttura dati è immutabile.

Ecco come è possibile creare un `frozenset` in Python:
```python
# Creazione di un `frozenset`
my_`frozenset` = `frozenset`([1, 2, 3, 4, 5])
```

In questo esempio, abbiamo creato un `frozenset` denominato `my_`frozenset`` contenente gli stessi elementi del set precedente.

Poiché i `frozenset` sono immutabili, non è possibile aggiungere o rimuovere elementi da un `frozenset`. Tuttavia, puoi eseguire operazioni come l'intersezione, la differenza e la verifica della presenza di elementi nello stesso modo in cui lo faresti con un set.

Ecco alcune operazioni comuni con i `frozenset`:

- **Intersezione di `frozenset`**: Puoi ottenere l'intersezione di due `frozenset` utilizzando l'operatore di intersezione `&` o il metodo `intersection()`.
```python
`frozenset`1 = `frozenset`([1, 2, 3])
`frozenset`2 = `frozenset`([3, 4, 5])
intersection_`frozenset` = `frozenset`1 & `frozenset`2  # Oppure intersection_`frozenset` = `frozenset`1.intersection(`frozenset`2)
```

- **Differenza di `frozenset`**: Puoi ottenere la differenza tra due `frozenset` utilizzando l'operatore di differenza `-` o il metodo `difference()`.
```python
difference_`frozenset` = `frozenset`1 - `frozenset`2  # Oppure difference_`frozenset` = `frozenset`1.difference(`frozenset`2)
```

- **Verifica della presenza di un elemento in un `frozenset`**: Puoi verificare se un elemento è presente in un `frozenset` utilizzando l'operatore `in`.
```python
element_present = 3 in `frozenset`1  # Restituirà True
```
- **Iterazione sui `frozenset`**: Puoi iterare sugli elementi di un `frozenset` utilizzando un ciclo `for` nello stesso modo in cui lo faresti con un set.

```python
for element in my_`frozenset`:
    print(element)
```

Un'altra caratteristica importante dei `frozenset` è che possono essere utilizzati come chiavi nei dizionari, a differenza dei set mutabili. Questo è possibile poiché i `frozenset` sono immutabili e quindi hashabili.

```python
my_dict = {my_`frozenset`: "Valore del `frozenset`"}
```

Inoltre, poiché i `frozenset` sono immutabili, sono più adatti per essere utilizzati in contesti in cui è necessaria l'immutabilità, ad esempio all'interno di dizionari o come elementi di set più grandi.

## Differenze chiave tra set e `frozenset`

1. **Mutabilità**: I `set` sono mutabili, il che significa che è possibile modificarli dopo la loro creazione, mentre i `frozenset` sono immutabili e non possono essere modificati.
2. **Hashability**: I `frozenset` sono hashabili e possono essere utilizzati come chiavi nei dizionari, mentre i `set` mutabili non possono essere utilizzati come chiavi nei dizionari poiché non sono hashabili.
3. **Operazioni di inserimento e rimozione**: I `set` supportano operazioni di inserimento e rimozione di elementi, mentre i `frozenset` non supportano queste operazioni poiché sono immutabili. 
4. **Utilizzo**: I `set` sono utilizzati quando è necessario un insieme mutabile di elementi, mentre i `frozenset` sono utilizzati quando è necessario garantire che l'insieme rimanga costante e immutabile nel tempo.