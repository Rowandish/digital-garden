---
tags:
  - MachineLearning
---
Un dataset è un insieme di dati organizzati che costituiscono il fondamento del machine learning e dell'analisi dei dati.
==I dataset sono essenziali per l'allenamento e la valutazione dei modelli di machine learning, poiché contengono le informazioni di input (caratteristiche) e le etichette di output (target) necessarie per addestrare un modello e testarne le prestazioni==.

I dataset sono presenti in vari formati, come tabelle, file CSV, database, immagini, testo e altro, a seconda del tipo di problema che si sta affrontando.
Possono variare notevolmente in termini di dimensioni, con dataset piccoli che contengono solo alcune centinaia di esempi e dataset enormi con milioni o addirittura miliardi di punti dati. Ecco una panoramica dettagliata sui dataset nel machine learning.

## Componenti

Un dataset è generalmente suddiviso in due componenti principali:

1. **Caratteristiche (Features):** Questa parte del dataset contiene le ==informazioni di input== che il modello deve analizzare e utilizzare per fare previsioni o compiere decisioni. Le caratteristiche possono essere numeriche (ad esempio, altezza, peso), categoriche (ad esempio, genere, colore), immagini, testo o qualsiasi altra forma di dati.
2. **Etichette (Labels o Target):** ==Le etichette rappresentano l'output o l'obiettivo desiderato==. In altre parole, sono le risposte corrette o le aspettative a cui il modello mira. Ad esempio, se stiamo sviluppando un modello per il riconoscimento di immagini di gatti e cani, le etichette saranno "gatto" o "cane" associate a ciascuna immagine.

## Tipi di Dataset

I dataset possono essere classificati in base a diversi criteri:

### Esistenza di label
Questa categoria richiama esattamente le tipologie di machine learning.

1. **Supervisionato:** ==In un dataset supervisionato, sia le caratteristiche che le etichette sono presenti==. Questo tipo di dataset è utilizzato per l'allenamento e la valutazione dei modelli di machine learning, poiché contiene esempi con cui il modello può apprendere le relazioni tra le caratteristiche e le etichette.
2. **Non Supervisionato:** In un dataset non supervisionato, ==solo le caratteristiche sono presenti, e il modello deve scoprire autonomamente modelli o strutture nei dati==. Questo è spesso utilizzato per il clustering e la riduzione della dimensionalità.
3. **Semisupervisionato:** Questo tipo di dataset è una combinazione di supervisionato e non supervisionato, in cui ==alcune etichette sono presenti, ma non tutte==. È utile quando non è pratico etichettare manualmente tutti i dati.
4. **Reinforcement Learning:** In un contesto di apprendimento per rinforzo, il dataset è costituito da ==esperienze dell'agente e dalle ricompense corrispondenti==. È utilizzato per addestrare agenti di apprendimento per rinforzo.

### Struttura
#### Dataset Strutturati

   - **Dati organizzati**: In un dataset strutturato, i dati sono organizzati in una tabella o in una forma simile, con righe e colonne chiaramente definite. Ogni colonna rappresenta un attributo o una variabile specifica, mentre ogni riga rappresenta un'istanza o un record dei dati.
   - **Schema ben definito**: I dataset strutturati seguono uno schema di dati ben definito, in cui il tipo di dati, la lunghezza e il formato di ogni attributo sono noti in anticipo. Questo facilita la gestione, la query e l'analisi dei dati.

Esempi di dataset strutturati includono tabelle di database relazionali, fogli di calcolo Excel, file CSV (Comma-Separated Values) e molti dati aziendali, finanziari e scientifici.

#### Dataset Non Strutturati

- **Dati non organizzati**: In un dataset non strutturato, i dati non seguono una struttura tabellare e possono essere presentati in vari formati, come testo libero, immagini, audio, video o file binari. Questi dati possono essere disorganizzati e non hanno una chiara separazione tra attributi e record.
- **Schema flessibile o assente**: I dataset non strutturati possono mancare di uno schema dati predefinito o seguire uno schema molto flessibile, il che li rende più complessi da gestire e analizzare rispetto ai dataset strutturati.

Esempi di dataset non strutturati includono testi in linguaggio naturale, foto, video, tweet sui social media, registrazioni audio, e-mail e altro contenuto multimediale.

## Pandas
[[Pandas]] è la libreria fondamentale per Python per l'analisi di dati e quindi l'esplorazione dei dataset.

## Dataset famosi

Esistono vari siti dove poter scaricare dei dataset per i propri progetti.
* [Kaggle](https://www.kaggle.com/datasets)
* [UCI](https://archive.ics.uci.edu/datasets)

### MNIST

Il dataset MNIST (Modified National Institute of Standards and Technology) è un famoso set di dati utilizzato comunemente per l'allenamento e la valutazione di algoritmi di riconoscimento di cifre scritte a mano. Contiene un insieme di immagini in scala di grigi di dimensioni 28x28 pixel, ciascuna rappresentante un singolo cifra da 0 a 9. Il dataset è composto da 60.000 immagini di allenamento e 10.000 immagini di test.

Ecco un esempio di come puoi utilizzare il dataset MNIST in Python utilizzando la libreria TensorFlow e Keras:

```python
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# Carichiamo il dataset MNIST utilizzando la funzione `load_data()` fornita da Keras. Questo restituisce due tuple: una per i dati di allenamento e l'altra per i dati di test. Ogni tupla contiene un array di immagini e un array di etichette corrispondenti.
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Normalizziamo le immagini dividendo tutti i valori dei pixel per 255.0. Questo porta i valori dei pixel nell'intervallo [0, 1], semplificando così l'allenamento della rete.
train_images, test_images = train_images / 255.0, test_images / 255.0

# Qui viene creato il modello di rete neurale utilizzando Keras. Il modello sequenziale è una sequenza lineare di strati. La funzione `Flatten` trasforma l'immagine 28x28 in un vettore di 784 elementi. Successivamente, abbiamo uno strato nascosto con 128 neuroni e attivazione ReLU, seguito da uno strato di dropout per prevenire l'overfitting e infine uno strato di output con 10 neuroni (uno per ogni cifra) e attivazione softmax.
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),   # Flatten l'immagine 28x28 in un vettore di 784 elementi
    layers.Dense(128, activation='relu'),    # Strato nascosto con 128 neuroni e attivazione ReLU
    layers.Dropout(0.2),                     # Dropout per prevenire l'overfitting
    layers.Dense(10, activation='softmax')   # Strato di output con 10 neuroni per le 10 cifre e attivazione softmax
])

# Qui compiliamo il modello specificando l'ottimizzatore ('adam' in questo caso), la funzione di perdita (`sparse_categorical_crossentropy` che è adatta per problemi di classificazione con etichette intere) e la metrica da monitorare durante l'allenamento (accuratezza).
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Alleniamo il modello utilizzando i dati di allenamento per 5 epoche. In ogni epoca, il modello cerca di migliorare la sua capacità di fare predizioni.
model.fit(train_images, train_labels, epochs=5)

# Valutazione del modello
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print(f'\nTest accuracy: {test_acc}')

# Facciamo un esempio di predizione su una singola immagine di test. Espandiamo le dimensioni dell'immagine per adattarle al formato richiesto dalla rete neurale. Stampiamo la predizione e l'etichetta reale, e visualizziamo l'immagine usando Matplotlib.
image_index = 0
img = test_images[image_index]
img = (np.expand_dims(img,0))  # Aggiunge una dimensione per la batch
predictions = model.predict(img)

# Stampa la predizione
predicted_label = np.argmax(predictions[0])
print(f"Predicted label: {predicted_label}")
print(f"True label: {test_labels[image_index]}")

# Visualizza l'immagine
plt.imshow(test_images[image_index], cmap='gray')
plt.show()
```

Questo esempio utilizza una semplice rete neurale con un singolo strato nascosto per classificare le cifre del dataset MNIST. La rete viene allenata per 5 epoche, e alla fine viene valutata sulla base del set di test. Infine, viene mostrato un esempio di predizione su una singola immagine di test.


