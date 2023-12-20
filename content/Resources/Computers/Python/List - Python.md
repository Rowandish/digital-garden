---
tags:
  - Python
---
Le liste sono un tipo di sequenza, che consente di raccogliere una collezione ordinata di elementi eterogenei all'interno di una singola variabile.

## Creazione
Per creare una lista in Python, è sufficiente racchiudere gli elementi tra parentesi quadre `[]`. Le liste possono contenere elementi di diversi tipi, tra cui numeri, stringhe, oggetti personalizzati e altre liste. Ecco un esempio di creazione di una lista:

```python
my_list = [1, 2, 3, "quattro", 5.0]
```

In questo caso, `my_list` è una lista che contiene numeri interi, una stringa e un numero floating-point.

## Accesso agli elementi
Per accedere agli elementi di una lista, è possibile utilizzare l'indice dell'elemento desiderato, iniziando da zero per il primo elemento. Ad esempio, per accedere al secondo elemento di `my_list`, possiamo fare:

```python
second_element = my_list[1]
print(second_element)  # Stampa 2
```

## Aggiunta e Rimozione
Le liste supportano una serie di operazioni per aggiungere e rimuovere elementi.

### Aggiunta di Elementi
- `append()`: Aggiunge un elemento alla fine della lista.
    ```python
    my_list.append(6)
    ```
- `insert()`: Inserisce un elemento in una posizione specifica.
    ```python
    my_list.insert(2, "inserito")
    ```
- `extend()`: Aggiunge una sequenza di elementi (ad esempio, un'altra lista) alla fine della lista.
    ```python
    my_list.extend([7, 8, 9])
    ```

### Rimozione di Elementi
- `remove()`: Rimuove la prima occorrenza di un elemento specifico.
    ```python
    my_list.remove("quattro")
    ```
- `pop()`: Rimuove un elemento in una posizione specifica e lo restituisce. Se non si specifica una posizione, viene rimosso l'ultimo elemento.
    ```python
    popped_element = my_list.pop(2)  # Rimuove l'elemento alla posizione 2 (terzo elemento)
    ```
- `del`: Rimuove un elemento in una posizione specifica senza restituirlo.
    ```python
    del my_list[0]  # Rimuove il primo elemento
    ```

## Altre Operazioni Comuni
- `len()`: Restituisce la lunghezza di una lista (il numero di elementi).
  ```python
  length = len(my_list)
  ```
- `count()`: Restituisce il numero di occorrenze di un elemento specifico nella lista.
  ```python
  count = my_list.count(2)  # Restituirà 1
  ```
- `index()`: Restituisce l'indice della prima occorrenza di un elemento specifico nella lista.
  ```python
  index = my_list.index("quattro")  # Restituirà 2
  ```
- `sort()`: Ordina la lista in ordine crescente (per le liste di numeri) o in ordine alfabetico (per le liste di stringhe).
  ```python
  my_list.sort()  # Ordina la lista in loco
  ```
- `reverse()`: Inverte l'ordine degli elementi nella lista.
  ```python
  my_list.reverse()  # Inverte la lista in loco
  ```

## Slicing
Lo slicing delle liste in Python è una tecnica potente che consente di estrarre porzioni specifiche di una lista. Lo slicing utilizza un'indicizzazione basata su intervallo per specificare quali elementi devono essere inclusi nella porzione estratta. Qui di seguito, approfondiremo lo slicing con vari esempi dedicati.

**Sintassi di base dello slicing:**

La sintassi per eseguire lo slicing in una lista è la seguente:

```python
lista[inizio:fine:passo]
```

- `inizio`: L'indice da cui iniziare a estrarre elementi. Questo elemento è incluso nella porzione risultante (default: inizio della lista).
- `fine`: L'indice fino al quale estrarre elementi. Questo elemento non è incluso nella porzione risultante (default: fine della lista).
- `passo`: L'intervallo tra gli elementi da estrarre. Se omesso, il passo è 1.

Ecco alcuni esempi che illustrano come utilizzare lo slicing:

```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Esempio 1: Estrazione di una sotto-lista dal terzo elemento al settimo elemento (indice 2-6):**

```python
subset = my_list[2:7]
print(subset)  # Stampa: [2, 3, 4, 5, 6]
```

**Esempio 2: Estrazione di tutti gli elementi fino al quarto elemento (indice 0-3):**

```python
subset = my_list[:4]
print(subset)  # Stampa: [0, 1, 2, 3]
```

**Esempio 3: Estrazione di tutti gli elementi dal quarto elemento in poi (indice 4-9):**

```python
subset = my_list[4:]
print(subset)  # Stampa: [4, 5, 6, 7, 8, 9]
```

**Esempio 4: Estrazione di tutti gli elementi con un passo di 2 (elementi pari):**

```python
subset = my_list[::2]
print(subset)  # Stampa: [0, 2, 4, 6, 8]
```

**Esempio 5: Estrazione di tutti gli elementi in ordine inverso:**

```python
subset = my_list[::-1]
print(subset)  # Stampa: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

**Esempio 6: Estrazione di una sotto-lista con un passo negativo (in ordine inverso):**

```python
subset = my_list[7:2:-1]
print(subset)  # Stampa: [7, 6, 5, 4, 3]
```

**Slicing con step diversi:**

Puoi specificare un passo diverso da 1 per estrarre elementi ad intervalli specifici:

```python
subset = my_list[1:9:2]  # Estrae gli elementi dall'indice 1 all'indice 9 con un passo di 2
print(subset)  # Stampa: [1, 3, 5, 7]
```

Lo slicing con passi diversi può essere utilizzato per estrarre elementi alternati, invertire l'ordine degli elementi o eseguire altre operazioni complesse.

## List Comprehensions

Le list comprehensions in Python sono un ==modo conciso e potente per creare nuove liste applicando trasformazioni o filtri agli elementi di una lista esistente==. Questa tecnica è molto apprezzata per la sua chiarezza e leggibilità del codice. Qui di seguito, approfondiremo le list comprehensions con vari esempi dedicati.

**Sintassi di base delle List Comprehensions:**

La sintassi generale di una list comprehension è la seguente:

```python
nuova_lista = [espressione for elemento in lista_originale if condizione]
```

- `nuova_lista`: La nuova lista che verrà creata.
- `espressione`: L'espressione da applicare a ciascun elemento nella lista originale.
- `elemento`: La variabile che rappresenta ciascun elemento nella lista originale.
- `lista_originale`: La lista da cui verranno estratti gli elementi.
- `condizione` (facoltativa): Una condizione che determina se un elemento deve essere incluso nella nuova lista.

**Esempi di List Comprehensions:**

Ecco alcuni esempi che illustrano come utilizzare le list comprehensions:

**Esempio 1: Creazione di una lista dei quadrati dei numeri da 0 a 9:**
```python
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)
# Stampa: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Esempio 2: Creazione di una lista dei numeri pari da 0 a 9:**
```python
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
# Stampa: [0, 2, 4, 6, 8]
```

**Esempio 3: Estrazione di lettere maiuscole da una stringa:**
```python
stringa = "Questo è un Esempio di List Comprehension"
uppercase_letters = [lettera for lettera in stringa if lettera.isupper()]
print(uppercase_letters)
# Stampa: ['Q', 'E', 'L', 'C']
```

**Esempio 4: Creazione di una lista di tuple con elementi e il loro quadrato:**
```python
numbers = [1, 2, 3, 4, 5]
squared_tuples = [(x, x**2) for x in numbers]
print(squared_tuples)
# Stampa: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

**Esempio 5: Filtraggio dei numeri primi in un intervallo:**
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [x for x in range(30) if is_prime(x)]
print(prime_numbers)
# Stampa: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

**Esempio 6: Rimozione delle vocali da una stringa:**
```python
sentence = "Questa è una frase di esempio"
consonants = [letter for letter in sentence if letter.lower() not in "aeiou"]
filtered_sentence = "".join(consonants)
print(filtered_sentence)
# Stampa: "Qst  n frs d xmpl"
```

**Esempio 7: Creazione di una lista annidata con due loop in una list comprehension:**

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [number for row in matrix for number in row]
print(flattened_matrix)
# Stampa: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Liste Annidate
Le liste possono contenere altre liste, creando liste annidate. Questo è utile per rappresentare dati strutturati. Ad esempio:

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Per accedere agli elementi di una lista annidata, è necessario utilizzare l'indicizzazione multipla. Ad esempio, per accedere al numero 5:

```python
number = nested_list[1][1]  # Riga 1, colonna 1
```

## Copia di Liste
Quando si lavora con liste, è importante comprendere come le copie funzionino. L'assegnazione diretta di una lista a un'altra variabile non crea una copia indipendente, ma piuttosto un riferimento alla stessa lista. Per creare una copia indipendente di una lista, è possibile utilizzare il metodo `copy()` o eseguire una slicing completo:

```python
original_list = [1, 2, 3]
copied_list = original_list.copy()  # Crea una copia indipendente
sliced_list = original_list[:]  # Crea una copia indipendente
```
