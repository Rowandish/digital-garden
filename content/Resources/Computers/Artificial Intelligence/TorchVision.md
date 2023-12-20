---
tags:
  - MachineLearning
  - ComputerVision
---
`TorchVision` è una libreria popolare nel campo del machine learning e deep learning, strettamente integrata con il framework [[PyTorch]].
Essa fornisce una vasta gamma di utility e strumenti per semplificare lo sviluppo e la gestione di problemi di computer vision, che coinvolgono l'elaborazione di immagini e video.
Questa libreria gioca un ruolo fondamentale nell'ecosistema di PyTorch, offrendo un'ampia varietà di risorse che vanno dalla manipolazione delle immagini all'addestramento di reti neurali per compiti di visione artificiale.

**Principali componenti di TorchVision:**

1. **Trasformazioni delle immagini**: TorchVision offre una vasta gamma di trasformazioni delle immagini, tra cui il ridimensionamento, il ritaglio, la rotazione, la normalizzazione e molte altre. Queste trasformazioni consentono di preparare e pre-processare i dati delle immagini prima di utilizzarli per l'addestramento di reti neurali.
```python
import torchvision.transforms as transforms

# Esempio di trasformazione per la riduzione delle dimensioni e normalizzazione
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
```

2. **Caricamento di dati**: TorchVision semplifica il caricamento di dataset comuni utilizzati in visione artificiale, tra cui CIFAR-10, MNIST, ImageNet e molti altri. Questi dataset possono essere facilmente importati e divisi in insiemi di addestramento e di test.
```python
import torchvision.datasets as datasets

# Carica il dataset CIFAR-10
train_dataset = datasets.CIFAR10(root='./data', train=True, transform=transform, download=True)
test_dataset = datasets.CIFAR10(root='./data', train=False, transform=transform, download=True)
```

3. **Dataloader**: TorchVision offre la classe `DataLoader` per la creazione di iteratori che semplificano il caricamento dei dati durante l'addestramento. Questo è utile per effettuare l'addestramento in batch, che migliora l'efficienza e la stabilità dell'addestramento delle reti neurali.
```python
from torch.utils.data import DataLoader

# Crea dataloader per il training e il test
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)
```

4. **Modelli pre-addestrati**: TorchVision mette a disposizione modelli di reti neurali pre-addestrati, addestrati su dataset estesi come ImageNet. Questi modelli possono essere utilizzati direttamente o fine-tunati per risolvere specifici problemi di visione artificiale.

```python
import torchvision.models as models

# Carica un modello ResNet pre-addestrato
model = models.resnet18(pretrained=True)
```

5. **Operazioni di inferenza**: TorchVision semplifica l'esecuzione dell'inferenza utilizzando modelli di reti neurali. Dopo aver caricato un modello pre-addestrato, è possibile utilizzarlo per effettuare previsioni su nuove immagini.

```python
import torch

# Esegui l'inferenza su un'immagine
input_image = ...  # Carica o crea un'immagine
output = model(input_image)
```

6. **Allenamento di modelli personalizzati**: Sebbene TorchVision offra modelli pre-addestrati, è possibile creare modelli personalizzati utilizzando PyTorch e addestrarli su dataset specifici. La libreria fornisce gli strumenti necessari per l'addestramento, il monitoraggio e la valutazione dei modelli.

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Definisci un modello personalizzato
class CustomModel(nn.Module):
    def __init__(self):
        super(CustomModel, self).__init__()
        # Definisci l'architettura del modello

    def forward(self, x):
        # Definisci la logica di inoltro del modello
        pass

# Crea un'istanza del modello e del criterio di perdita
model = CustomModel()
criterion = nn.CrossEntropyLoss()

# Definisci l'ottimizzatore
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
```

7. **Valutazione dei modelli**: TorchVision offre una serie di metriche e strumenti di valutazione per valutare le prestazioni dei modelli di visione artificiale. Questo è fondamentale per comprendere quanto bene il modello sta eseguendo le previsioni.

```python
from sklearn.metrics import accuracy_score

# Esegui l'addestramento e la valutazione del modello
for epoch in range(num_epochs):
    # Fase di addestramento
    for inputs, labels in train_loader:
        # Esegui l'addestramento

    # Fase di valutazione
    model.eval()
    predictions = []
    true_labels = []
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
            predictions.extend(predicted.tolist())
            true_labels.extend(labels.tolist())

    accuracy = accuracy_score(true_labels, predictions)
    print(f'Accuracy: {accuracy}')
```

8. **Strumenti di visualizzazione**: TorchVision include funzionalità di visualizzazione per aiutare a esplorare e comprendere i dati delle immagini, nonché le attività di addestramento. Questo può essere utile per il debug e l'analisi dei risultati.

```python
import matplotlib.pyplot as plt

# Visualizza alcune immagini
sample_images, sample_labels = next(iter(train_loader))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(sample_images[i].permute(1, 2, 0))
    plt.title(f"Class: {sample_labels[i]}")
    plt.axis('off')
plt.show()
```