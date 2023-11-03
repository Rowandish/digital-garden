---
tags:
  - MachineLearning
  - ComputerVision
---
Un modello ONNX (Open Neural Network Exchange) nel mondo del machine learning è un ==formato di scambio aperto e interoperabile per rappresentare reti neurali artificiali e modelli di apprendimento automatico==.
Questo formato è stato sviluppato per consentire la portabilità dei modelli tra diversi framework di machine learning, rendendo più agevole la creazione, l'addestramento e la distribuzione di modelli su diverse piattaforme e architetture hardware.
==Un modello ONNX è un file che contiene le informazioni necessarie per descrivere l'architettura di una rete neurale, i pesi, i parametri, le operazioni e altro ancora==.

ONNX è stato sviluppato con l'obiettivo di superare le limitazioni legate alla compatibilità tra i vari framework di deep learning.
Prima dell'introduzione di ONNX, i modelli addestrati con un framework specifico erano spesso difficili da utilizzare con un altro framework senza complesse operazioni di conversione.
Questo era particolarmente problematico quando si dovevano utilizzare diversi framework per diverse fasi del processo di sviluppo di un modello, come la progettazione, l'addestramento e l'implementazione.

ONNX risolve questo problema fornendo uno standard aperto per rappresentare modelli di machine learning: ciò significa che è ==possibile creare un modello con un framework, addestrarlo e poi convertirlo in un formato ONNX, rendendolo così facilmente utilizzabile con un altro framework o applicazione che supporti ONNX==. 

Ora esamineremo come è possibile esportare e importare modelli ONNX utilizzando esempi di codice in Python e C#. Per prima cosa, vediamo come esportare un modello ONNX in Python, utilizzando il framework [[PyTorch]] con [[TorchVision]] come esempio.

**Esportazione di un modello PyTorch in formato ONNX:**

```python
import torch
import torchvision

# Carica un modello preaddestrato da torchvision
model = torchvision.models.resnet18(pretrained=True)
model.eval()

# Definisci l'input fittizio con le dimensioni corrette
dummy_input = torch.randn(1, 3, 224, 224)

# Esporta il modello in formato ONNX
onnx_file_path = "resnet18.onnx"
torch.onnx.export(model, dummy_input, onnx_file_path, verbose=True)
```

In questo esempio, abbiamo importato il modello di rete neurale ResNet-18 da torchvision e l'abbiamo esportato in formato ONNX utilizzando `torch.onnx.export`.
Il file ONNX risultante conterrà l'architettura del modello, inclusi tutti i pesi e i parametri.

Ora vediamo come è possibile importare un modello ONNX in C#. utilizzando la libreria ONNX Runtime.

**Importazione di un modello ONNX in C#:**

```csharp
using System;
using Microsoft.ML.OnnxRuntime;
using Microsoft.ML.OnnxRuntime.Tensors;

class Program
{
    static void Main()
    {
        // Percorso del file ONNX del modello
        string modelPath = "resnet18.onnx";

        // Crea una sessione ONNX
        using (var session = new InferenceSession(modelPath))
        {
            // Crea un tensore di input con i dati desiderati
            float[] inputData = new float[3 * 224 * 224]; // Adattare alle dimensioni del modello
            var inputTensor = new DenseTensor<float>(inputData, new int[] { 1, 3, 224, 224 });

            // Esegui l'inferenza
            var inputs = new NamedOnnxValue[] { NamedOnnxValue.CreateFromTensor("input", inputTensor) };
            var results = session.Run(inputs);

            // Estrai il tensore di output
            var outputTensor = results.FirstOrDefault().AsTensor<float>();
            
            // Puoi ora lavorare con i risultati
            Console.WriteLine("Output shape: " + string.Join(", ", outputTensor.Dimensions));
        }
    }
}
```

In questo esempio, abbiamo utilizzato la libreria ONNX Runtime in C# per importare un modello ONNX precedentemente esportato. Abbiamo creato una sessione ONNX, fornito dati di input (un [[Tensori|tensore]]) e ottenuto risultati in forma di tensore di output. Questi risultati possono essere ulteriormente elaborati o utilizzati per le operazioni successive.

È importante notare che le dimensioni del tensore di input devono corrispondere alle dimensioni di input specificate durante l'esportazione del modello. Inoltre, il nome dell'input "input" nel codice C# deve corrispondere al nome specificato durante l'esportazione del modello.

ONNX offre un'interfaccia standard per esportare e importare modelli di machine learning, il che semplifica notevolmente il processo di integrazione dei modelli in diverse applicazioni e framework.
È importante notare che ONNX è supportato da una vasta gamma di framework e librerie di machine learning, il che lo rende una scelta eccellente per garantire la portabilità dei modelli in ambienti diversi.