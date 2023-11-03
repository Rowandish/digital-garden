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

## Utilizzo

I dataset sono fondamentali in tutte le fasi del ciclo di vita del machine learning:

1. **Raccolta e Preparazione dei Dati:** La raccolta di dati grezzi da diverse fonti e la loro trasformazione in un formato utilizzabile costituiscono una parte significativa del lavoro iniziale nel machine learning. I dataset (prima di essere utilizzati per l'addestramento) devono essere:
	* puliti
	* normalizzati
	* pre-processati
2. **Addestramento del Modello:** I dataset supervisionati vengono suddivisi in [[Train set e Test set]]. ==Il set di allenamento viene utilizzato per addestrare il modello, mentre il set di test viene utilizzato per valutarne le prestazioni==. Il modello apprende le relazioni tra le caratteristiche e le etichette dal set di allenamento.
3. **Validazione e Ottimizzazione:** Dopo l'addestramento, è necessario ==validare il modello su un set di dati separato (set di validazione)== per valutare le prestazioni e ottimizzare i parametri del modello. Il dataset di validazione è essenziale per evitare l'[[overfitting]].
4. **Valutazione e Test Finale:** Dopo la fase di addestramento e validazione, il modello viene testato sul set di test indipendente per valutare le prestazioni reali. Questo offre una misura oggettiva delle capacità del modello.
5. **Deployment in Produzione:** Una volta che il modello è stato addestrato e testato con successo, può essere distribuito in produzione per compiere previsioni o decisioni automatizzate.

## Pandas
[[Pandas]] è la libreria fondamentale per Python per l'analisi di dati e quindi l'esplorazione dei dataset.

## Esempio con Keras

Ecco come utilizzare dataset in [[Keras]] per un semplice problema di classificazione: riconoscere cifre scritte a mano utilizzando il dataset MNIST.
In applicazioni reali, i dataset possono variare notevolmente in complessità e dimensioni, ma il processo di raccolta, preparazione e utilizzo dei dati rimane fondamentalmente lo stesso.

**1. Importazione delle Librerie:**

```python
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
```

**2. Caricamento del Dataset:**
Utilizzeremo il dataset MNIST, un dataset di immagini di cifre scritte a mano. Carichiamolo utilizzando Keras:

```python
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
```

**3. Preprocessing dei Dati:**
Le immagini vengono preprocessate normalizzandole e ridimensionandole:
```python
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255
```

**4. Creazione del Modello:**
Definiamo un modello di rete neurale semplice:
```python
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(Dense(10, activation='softmax'))
```

**5. Addestramento del Modello:**
Compiliamo il modello e addestriamolo utilizzando il set di allenamento:
```python
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5, batch

_size=64)
```

**6. Valutazione del Modello:**
Valutiamo le prestazioni del modello utilizzando il set di test:
```python
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_accuracy}')
```



## Sorgenti di Dataset

Esistono vari siti dove poter scaricare dei dataset per i propri progetti.
* [Kaggle](https://www.kaggle.com/datasets)
* [UCI](https://archive.ics.uci.edu/datasets)