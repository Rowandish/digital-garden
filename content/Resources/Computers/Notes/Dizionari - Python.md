---
tags:
  - Python
---
I dizionari in Python sono una struttura di dati estremamente utile e flessibile che permette di organizzare e memorizzare dati in una forma chiave-valore.

## Creazione

Un dizionario è una raccolta di coppie chiave-valore, dove ogni chiave è unica. Per creare un dizionario in Python, si utilizza l'operatore `{}` e si specificano le coppie chiave-valore separando le chiavi dai valori con il simbolo `:`. Ad esempio:

```python
# Creazione di un dizionario vuoto
my_dict = {}

# Creazione di un dizionario con coppie chiave-valore
person = {
    "nome": "Mario",
    "cognome": "Rossi",
    "età": 30,
    "città": "Roma"
}
```

In questo esempio, abbiamo creato un dizionario denominato `person` con quattro coppie chiave-valore che rappresentano i dettagli di una persona.

## Accesso ai Valori

Per accedere ai valori in un dizionario, è possibile utilizzare la chiave corrispondente tra parentesi quadre `[]`. Ad esempio:

```python
# Accesso ai valori nel dizionario
nome = person["nome"]
età = person["età"]

print(nome)  # Stampa: "Mario"
print(età)   # Stampa: 30
```

È importante notare che se si cerca di accedere a una chiave che non esiste nel dizionario, si otterrà un errore `KeyError`.

## Aggiunta e Modifica di Elementi

È possibile aggiungere nuove coppie chiave-valore a un dizionario o modificare i valori esistenti. Per aggiungere una nuova coppia, è sufficiente assegnare un valore a una nuova chiave:

```python
# Aggiunta di una nuova coppia chiave-valore
person["professione"] = "Ingegnere"
```

Per modificare un valore esistente, basta assegnare un nuovo valore a una chiave esistente:

```python
# Modifica del valore di una chiave
person["età"] = 31
```

## Rimozione di Elementi

Per rimuovere una coppia chiave-valore da un dizionario, è possibile utilizzare l'istruzione `del` seguita dalla chiave da rimuovere:

```python
# Rimozione di una coppia chiave-valore
del person["città"]
```

In alternativa, è possibile utilizzare il metodo `pop()`, che rimuove un elemento e restituisce il suo valore:

```python
# Rimozione di una coppia chiave-valore con il metodo pop()
professione = person.pop("professione")
```

## Verifica della Presenza di una chiave

Per verificare se una chiave specifica esiste in un dizionario, è possibile utilizzare l'operatore `in`:

```python
# Verifica se una chiave esiste nel dizionario
if "professione" in person:
    print("La chiave 'professione' esiste nel dizionario.")
```

## Iterazione su Dizionari

È possibile iterare sui dizionari utilizzando cicli `for`. Per esempio, è possibile iterare sulle chiavi, sui valori o sulle coppie chiave-valore:

```python
# Iterazione sulle chiavi
for key in person:
    print(key)
```

```python
# Iterazione sui valori
for value in person.values():
    print(value)
```

```python
# Iterazione sulle coppie chiave-valore
for key, value in person.items():
    print(key, value)
```

**Metodi comuni dei dizionari:**

Python offre una serie di metodi incorporati utili per lavorare con i dizionari. Alcuni dei metodi più comuni includono:

- `keys()`: Restituisce una lista di tutte le chiavi nel dizionario.
- `values()`: Restituisce una lista di tutti i valori nel dizionario.
- `items()`: Restituisce una lista di tuple (chiave, valore) per tutte le coppie chiave-valore nel dizionario.
- `get()`: Restituisce il valore associato a una chiave specifica. Se la chiave non esiste, è possibile specificare un valore predefinito da restituire.
- `clear()`: Rimuove tutte le coppie chiave-valore dal dizionario.
- `copy()`: Restituisce una copia superficiale del dizionario.
- `update()`: Aggiunge coppie chiave-valore da un altro dizionario al dizionario corrente.
- `popitem()`: Rimuove e restituisce l'ultima coppia chiave-valore inserita nel dizionario (inserita per la prima volta).
- `fromkeys()`: Crea un nuovo dizionario con chiavi specificate e un valore predefinito opzionale per tutte le chiavi.

## Dizionari Annidati

I dizionari in Python possono contenere altri dizionari, consentendo di cre

are strutture dati complesse. Ad esempio:

```python
students = {
    "studente1": {
        "nome": "Alice",
        "età": 20
    },
    "studente2": {
        "nome": "Bob",
        "età": 22
    }
}
```

Per accedere ai valori in un dizionario annidato, è necessario utilizzare l'indicizzazione multipla:

```python
nome_studente1 = students["studente1"]["nome"]
età_studente2 = students["studente2"]["età"]
```