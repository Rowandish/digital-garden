---
tags:
  - MachineLearning
  - Python
---
PyTorch è un framework di deep learning open-source apprezzato per la sua flessibilità, facilità d'uso e capacità di calcolo su GPU, rendendolo una scelta ideale per gli sviluppatori e i ricercatori che lavorano su progetti di deep learning.

## Caratteristiche

1. **Tensori Dinamici:** Una delle caratteristiche distintive di PyTorch è il suo supporto ai [[Tensori]] dinamici. Questo significa che le operazioni su tensori possono essere definite e calcolate dinamicamente durante l'esecuzione, rendendo più facile definire modelli di deep learning complessi e adattarli a diverse situazioni.
2. **Interfaccia Pythonic:** PyTorch è noto per avere un'interfaccia Pythonic molto intuitiva, che rende la scrittura di codice più naturale e leggibile. Gli sviluppatori possono utilizzare strutture di controllo Python standard, come cicli for e condizioni, per definire i loro modelli.
3. **Calcolo su GPU:** PyTorch offre un'ottima accelerazione su GPU, consentendo di sfruttare appieno le potenzialità di calcolo delle schede grafiche per l'addestramento di modelli neurali. Questo è particolarmente utile per modelli complessi che richiedono molte operazioni matematiche.
4. **Librerie di Alto Livello:** PyTorch include librerie di alto livello come TorchScript e [[TorchVision]] che semplificano il deploy dei modelli in produzione e l'elaborazione delle immagini.
5. **Versatilità:** PyTorch è utilizzato sia in ambienti accademici che industriali per una vasta gamma di applicazioni, tra cui visione artificiale, processamento del linguaggio naturale, riconoscimento vocale, robotica e altro.

## Installazione

PyTorch può essere installato utilizzando pip, il gestore di pacchetti Python, ma è necessario specificare la versione desiderata (CPU o GPU) e la versione di Python. Ad esempio, per installare PyTorch per CPU con Python 3.7, è possibile utilizzare il seguente comando:

```bash
pip install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
```

Se si desidera utilizzare PyTorch con GPU, è possibile sostituire "cpu" con "cuda" nella versione specificata.

## Creazione e Manipolazione di Tensori

In PyTorch, i dati sono rappresentati utilizzando [[tensori]], che sono essenzialmente matrici multidimensionali.
Ecco come è possibile creare e manipolare tensori in PyTorch:

```python
import torch

# Creazione di un tensore vuoto (inizializzato a valori casuali)
tensor_vuoto = torch.empty(3, 3)

# Creazione di un tensore con zeri
tensor_zeri = torch.zeros(2, 2)

# Creazione di un tensore con valori specifici
tensor_valori = torch.tensor([1, 2, 3])

# Operazioni matematiche tra tensori
t1 = torch.tensor([1, 2, 3])
t2 = torch.tensor([4, 5, 6])
somma = t1 + t2
prodotto = t1 * t2
```

**Definizione di Modelli di Deep Learning:**

PyTorch semplifica la definizione dei modelli di deep learning utilizzando il modulo `torch.nn`.
Ecco un esempio di come definire una rete neurale semplice:

```python
import torch
import torch.nn as nn

class ReteNeurale(nn.Module):
    def __init__(self):
        super(ReteNeurale, self).__init()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 1)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

modello = ReteNeurale()
```

Il modulo `nn.Module` permette di definire i layer e le operazioni in modo chiaro e organizzato.

## Addestramento di Modelli

PyTorch rende anche l'addestramento di modelli molto intuitivo. Ecco un esempio di come addestrare una rete neurale su dati di addestramento:

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Definizione del modello
modello = ReteNeurale()

# Definizione della funzione di perdita e dell'ottimizzatore
criterio = nn.MSELoss()
ottimizzatore = optim.SGD(modello.parameters(), lr=0.01)

# Dati di addestramento
input_dati = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
target = torch.tensor([2.0])

# Addestramento del modello
for epoca in range(100):
    output = modello(input_dati)
    perdita = criterio(output, target)
    
    ottimizzatore.zero_grad()
    perdita.backward()
    ottimizzatore.step()
```

**Utilizzo di PyTorch per la Visione Artificiale:**

PyTorch è ampiamente utilizzato in applicazioni di visione artificiale. Con il modulo `torchvision`, è possibile caricare e pre-elaborare facilmente dati di immagini. Ecco un esempio di come addestrare una [[rete neurale convoluzionale]] (CNN) per il riconoscimento di cifre scritte a mano utilizzando il famoso dataset MNIST:

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# Trasformazioni delle immagini


trasformazioni = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

# Caricamento del dataset MNIST
train_set = datasets.MNIST('./data', train=True, download=True, transform=trasformazioni)
train_loader = torch.utils.data.DataLoader(train_set, batch_size=64, shuffle=True)

# Definizione di una CNN
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.fc1 = nn.Linear(32 * 26 * 26, 128)
        self.fc2 = nn.Linear(128, 10)
    
    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = x.view(-1, 32 * 26 * 26)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Addestramento del modello
modello = CNN()
criterio = nn.CrossEntropyLoss()
ottimizzatore = optim.Adam(modello.parameters(), lr=0.001)

for epoca in range(10):
    for dati, etichette in train_loader:
        output = modello(dati)
        perdita = criterio(output, etichette)
        
        ottimizzatore.zero_grad()
        perdita.backward()
        ottimizzatore.step()
```

## Deploy di Modelli in Produzione

Una volta addestrato il modello, PyTorch offre strumenti come TorchScript per esportare il modello in un formato che può essere facilmente utilizzato in produzione, incluso l'uso in applicazioni web o mobili.

## Keras vs Pytorch

[[Keras]] e PyTorch sono due framework di deep learning molto popolari che consentono agli sviluppatori di creare, addestrare e implementare modelli di reti neurali.

### Analogie

1. **Interfaccia di Alto Livello:** Entrambi Keras e PyTorch offrono un'interfaccia di alto livello per definire modelli di reti neurali. Questo rende più facile per gli sviluppatori creare e sperimentare con diversi tipi di reti neurali senza dover affrontare dettagli di basso livello.    
2. **Supporto GPU:** Entrambi i framework supportano il calcolo su GPU, consentendo di accelerare l'addestramento dei modelli neurali su hardware specializzato.
3. **Versatilità:** Entrambi i framework sono adatti per una vasta gamma di applicazioni, tra cui visione artificiale, elaborazione del linguaggio naturale, classificazione, regressione e altro.
    

### Differenze

1. **Backend e Modello di Calcolo:**    
    - **Keras:** Keras è un framework di alto livello che può funzionare su diversi backends, tra cui TensorFlow, Theano e Microsoft Cognitive Toolkit (CNTK). In TensorFlow 2.x, Keras è integrato come parte del pacchetto TensorFlow (tf.keras).        
    - **PyTorch:** PyTorch è un framework completo con un proprio backend che supporta tensori dinamici. Questo significa che PyTorch permette di definire e modificare il grafo di calcolo durante l'esecuzione, offrendo maggiore flessibilità in termini di definizione dei modelli.        
2. **Sintassi e Stile di Programmazione:**    
    - **Keras:** Keras è noto per la sua sintassi chiara e intuitiva, che è spesso considerata più facile da imparare e utilizzare, soprattutto per i principianti.
    - **PyTorch:** PyTorch offre un'interfaccia Pythonic che molti sviluppatori trovano naturale e flessibile. Tuttavia, richiede una maggiore familiarità con i dettagli tecnici rispetto a Keras.        
3. **Flessibilità e Controllo:**
    - **Keras:** Keras è progettato per una rapida prototipazione e facilità d'uso. È meno flessibile rispetto a PyTorch in termini di personalizzazione di modelli e operazioni di basso livello.        
    - **PyTorch:** PyTorch offre un maggiore controllo e flessibilità, consentendo agli sviluppatori di eseguire operazioni di basso livello, personalizzare le operazioni di gradiente e definire modelli complessi con facilità.
 4. **Applicazioni Popolari:**
    - **Keras:** Keras è ampiamente utilizzato per applicazioni aziendali e di produzione, specialmente quando è integrato in TensorFlow.        
    - **PyTorch:** PyTorch è molto popolare nella ricerca accademica e nell'esperimento con nuove idee, ed è spesso scelto da ricercatori e sviluppatori per la sua flessibilità.
        