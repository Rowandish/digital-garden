---
tags:
  - MachineLearning
---
Il "train set" e il "test set" sono due insiemi distinti di dati utilizzati nell'addestramento e nella valutazione di modelli di machine learning.

1. **Train Set (Insieme di Addestramento):** **Il train set è l'insieme di dati utilizzato per addestrare un modello di machine learning**. Questi dati vengono utilizzati per insegnare al modello come fare previsioni basate sulle feature fornite. Il modello cerca di apprendere relazioni e pattern nei dati di addestramento in modo da poter fare previsioni accurate sui dati futuri.
2. **Test Set (Insieme di Test):** Il test set è un ==insieme separato di dati che non è stato utilizzato durante l'addestramento del modello. Viene utilizzato per valutare le prestazioni del modello e misurare la sua capacità di fare previsioni su dati non visti in precedenza==. Il test set serve a valutare se il modello è in grado di generalizzare correttamente dalle informazioni apprese durante l'addestramento.

Per scegliere la proporzione tra il train set e il test set, solitamente si utilizza una divisione comune, ad esempio l'80% dei dati per il train set e il restante 20% per il test set. Tuttavia, la scelta dipende anche dalla quantità di dati disponibili. In generale, più dati hai, più puoi ridurre la percentuale del test set.

Per vederne un esempio vedi la funzione [[Scikit Learn#^63440e|train_test_split]] di Scikit Learn.