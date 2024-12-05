---
tags:
  - MachineLearning
  - ComputerVision
---
La "non-maximum suppression" (NMS) è un importante concetto nell'ambito dell'elaborazione delle immagini e del riconoscimento di oggetti.
Si tratta di un ==algoritmo utilizzato per ridurre i falsi positivi generati da algoritmi di rilevamento di oggetti==, come l'algoritmo di rilevamento di bordi di Canny o i rilevatori di caratteristiche nelle immagini.
La non-maximum suppression è una tecnica essenziale in molte applicazioni di visione artificiale, tra cui il rilevamento di oggetti in tempo reale, il tracciamento di oggetti in video, il riconoscimento di caratteri OCR e molto altro.
==L'obiettivo principale della NMS è selezionare solo i punti salienti o le regioni di interesse nell'immagine e rimuovere i punti non significativi o le regioni sovrapposte==. Questo è particolarmente utile quando si tratta di rilevare oggetti in un'immagine, poiché evita che lo stesso oggetto venga rilevato più volte o che regioni non significative vengano erroneamente considerate.

Per comprendere meglio come funziona la NMS, è utile suddividerla in diversi passaggi:

1. **Generazione dei candidati:** Iniziamo generando una serie di candidati che rappresentano possibili regioni o punti di interesse nell'immagine. Questi candidati possono essere generati da vari algoritmi di rilevamento di oggetti, come il rilevamento di contorni, il rilevamento di caratteristiche o reti neurali convoluzionali (CNN).
2. **Calcolo della confidenza:** Ogni candidato è associato a un valore di confidenza che indica quanto l'algoritmo sia sicuro che quel candidato rappresenti un oggetto o una caratteristica significativa nell'immagine.
3. **Ordinamento dei candidati:** I candidati vengono quindi ordinati in base alla loro confidenza in ordine decrescente. Questo significa che i candidati più promettenti verranno posti all'inizio della lista.
4. **Iterazione sui candidati:** Si procede ora all'iterazione sulla lista ordinata dei candidati. Per ciascun candidato, vengono considerati i candidati successivi per valutare se sono sufficientemente simili e dovrebbero essere soppressi. Questa somiglianza viene generalmente valutata sulla base della sovrapposizione spaziale tra i candidati.

Ecco un esempio di codice Python che mostra come eseguire la NMS su una lista di candidati con relative confidenze:

```python
def non_maximum_suppression(candidates, confidences, threshold):
    # Inizializziamo una lista vuota per i candidati selezionati
    selected_candidates = []

    # Ordiniamo i candidati in base alla confidenza decrescente
    sorted_indices = sorted(range(len(confidences)), key=lambda i: confidences[i], reverse=True)

    while len(sorted_indices) > 0:
        # Prendiamo il candidato con la confidenza più alta
        best_index = sorted_indices[0]
        best_candidate = candidates[best_index]

        # Aggiungiamo il miglior candidato alla lista dei selezionati
        selected_candidates.append(best_candidate)

        # Rimuoviamo il miglior candidato e gli altri candidati sovrapposti
        del sorted_indices[0]
        indices_to_remove = []

        for i, index in enumerate(sorted_indices):
            candidate = candidates[index]
            overlap = calculate_overlap(best_candidate, candidate)  # Calcola l'overlap tra i candidati

            if overlap > threshold:
                indices_to_remove.append(i)

        # Rimuoviamo i candidati sovrapposti dalla lista ordinata
        sorted_indices = [index for i, index in enumerate(sorted_indices) if i not in indices_to_remove]

    return selected_candidates

def calculate_overlap(candidate1, candidate2):
    # Calcola l'overlap tra due candidati (può variare a seconda del tipo di candidati)
    # In questo esempio, consideriamo i candidati come rettangoli e calcoliamo l'area di sovrapposizione
    # Risultato tra 0 e 1: 0 indica nessuna sovrapposizione, 1 indica sovrapposizione completa
    intersection = calculate_intersection(candidate1, candidate2)
    area1 = calculate_area(candidate1)
    area2 = calculate_area(candidate2)
    overlap = intersection / (area1 + area2 - intersection)
    return overlap

def calculate_intersection(candidate1, candidate2):
    # Calcola l'area di sovrapposizione tra due rettangoli (candidati)
    # candidate1 e candidate2 sono tuple con coordinate (x1, y1, x2, y2)
    x1_1, y1_1, x2_1, y2_1 = candidate1
    x1_2, y1_2, x2_2, y2_2 = candidate2
    x1_i = max(x1_1, x1_2)
    y1_i = max(y1_1, y1_2)
    x2_i = min(x2_1, x2_2)
    y2_i = min(y2_1, y2_2)
    if x1_i < x2_i and y1_i < y2_i:
        return (x2_i - x1_i) * (y2_i - y1_i)
    return 0

def calculate_area(candidate):
    # Calcola l'area di un rettangolo (candidato)
    x1, y1, x2, y2 = candidate
    return (x2 - x1) * (y2 - y1)

# Esempio di utilizzo della NMS
candidates = [(50, 50, 100, 100), (60, 60, 110, 110), (200, 200, 250, 250)]
confidences = [0.9, 0.75, 0.8]
threshold = 0.5

selected_candidates = non_maximum_suppression(candidates, confidences, threshold)
print("Candidati selezionati dopo NMS:", selected_candidates)
```

In questo esempio, abbiamo una lista di candidati rappresentati come rettangoli con coordinate (x1, y1, x2, y2) e valori di confidenza associati. L'algoritmo NMS selezionerà i candidati con le confidenze più alte e rimuoverà i candidati sovrapposti rispetto a una certa soglia di sovrapposizione.

