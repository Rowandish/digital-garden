---
tags:
  - MachineLearning
---
In ambito di machine learning, un tensore è un ==tipo di struttura dati multidimensionale utilizzata per rappresentare dati==.
I tensori sono essenziali nelle librerie di machine learning come [[PyTorch]] e TensorFlow, poiché consentono di ==rappresentare dati in forma di array multidimensionali e di eseguire operazioni matematiche su di essi==.
In generale, un tensore può essere visto come una generalizzazione delle matrici, poiché può avere qualsiasi numero di dimensioni (ad esempio, scalari, vettori, matrici e tensori di ordine superiore).
Esistono due tipi di tensori: statici e dinamici: i tensori statici sono più adatti per operazioni matematiche su dati con dimensioni fisse, mentre i tensori dinamici sono essenziali per la costruzione e l'addestramento di reti neurali che possono avere input di dimensioni variabili.

## Tensore Statico

   - Le dimensioni del tensore sono fisse durante la sua creazione e non possono essere cambiate.
   - È utilizzato in librerie come NumPy per eseguire operazioni matematiche su dati statici.
   - È più efficiente in termini di utilizzo della memoria poiché la dimensione è fissa.
   - In PyTorch, il tipo di tensore statico è rappresentato dalla classe `torch.Tensor`, che ha dimensioni fisse definite al momento della creazione.

Ecco un esempio di creazione di un tensore statico in PyTorch:

```python
import torch

# Creazione di un tensore statico di forma (2, 3)
static_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Stampa del tensore
print(static_tensor)
```

## Tensore Dinamico

   - Le dimensioni del tensore possono essere modificate dinamicamente.
   - È utilizzato in librerie di deep learning come PyTorch e TensorFlow per costruire e addestrare reti neurali.
   - È più flessibile per gestire input di dimensioni variabili.
   - In PyTorch, il tipo di tensore dinamico è rappresentato dalla classe `torch.Tensor`, ma è più comunemente utilizzato con il modulo `torch.nn.Module` per definire reti neurali.

Ecco un esempio di creazione di un tensore dinamico in PyTorch:

```python
import torch

# Creazione di un tensore dinamico
dynamic_tensor = torch.randn(2, 3)  # Creazione di un tensore di forma (2, 3) con valori casuali

# Stampa del tensore
print(dynamic_tensor)
```