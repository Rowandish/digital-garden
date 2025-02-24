Le caratteristiche, o "features", sono le informazioni che il modello utilizza per apprendere dai dati e fare predizioni.
La selezione delle caratteristiche consiste ==nel scegliere le variabili più rilevanti e informative dai dati disponibili per addestrare il modello==. Questo processo è cruciale perché influisce direttamente sulla capacità del modello di generalizzare correttamente su nuovi dati e di ottenere prestazioni ottimali.

Per convenzione le caratteristiche scelte del dataset che voglio fornire al modello sono definite dalla lettera `X` (`y` invece è la caratteristica che voglio predire).
Nei dataset di `sklearn` le feature sono in `data` mentre il target è in `target`, tipicamente quello che si fa è:
```python
X = dataset['data']  
y = dataset['target']
```

Esistono diverse tecniche per operare la selezione delle caratteristiche:

1. **Analisi univariata**: Questa tecnica valuta l'importanza di ciascuna caratteristica individualmente. Si possono utilizzare test statistici o tecniche come l'analisi della varianza (ANOVA) per determinare quali caratteristiche hanno una relazione significativa con l'obiettivo del modello.    
2. **Selezione basata sulle prestazioni del modello**: Questo approccio coinvolge l'addestramento di diversi modelli utilizzando subset di caratteristiche diverse e quindi valutando le prestazioni di ciascun modello. Le caratteristiche che portano a modelli con prestazioni migliori vengono selezionate.    
3. **Selezione ricorsiva delle caratteristiche**: Questa tecnica funziona rimuovendo iterativamente le caratteristiche meno informative fino a quando le prestazioni del modello non peggiorano significativamente. Inizia con tutte le caratteristiche disponibili e rimuove quelle meno importanti una alla volta.    
4. **Selezione basata sulla regolarizzazione**: Alcuni algoritmi di apprendimento automatico, come la regressione lineare regolarizzata (ad esempio Lasso e Ridge), incorporano la selezione delle caratteristiche durante il processo di addestramento. Questi algoritmi applicano penalità alle caratteristiche meno importanti, spingendo il modello a selezionare solo le più rilevanti.    
5. **Metodi di apprendimento automatico per la selezione delle caratteristiche**: Alcuni algoritmi di ML, come gli alberi decisionali o le reti neurali, possono gestire la selezione delle caratteristiche internamente durante il processo di addestramento. Questi algoritmi possono pesare automaticamente l'importanza delle caratteristiche e selezionare quelle più utili per la previsione.    
6. **Ingegneria delle caratteristiche**: Questo approccio coinvolge la creazione di nuove caratteristiche derivate dalle caratteristiche esistenti, che potrebbero essere più informative per il modello. Ad esempio, si potrebbero calcolare nuove variabili come il rapporto tra due caratteristiche esistenti o le loro interazioni.
