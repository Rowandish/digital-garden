I metodi di apprendimento di insieme, o ensemble learning, sono un approccio potente utilizzato nel campo del machine learning per migliorare le prestazioni e la robustezza dei modelli predittivi.
==L'idea alla base di questi metodi è quella di combinare le previsioni di più modelli di base per ottenere una previsione più accurata e stabile rispetto a quella di ciascun modello individuale==.

Immagina di avere un insieme di esperti, ognuno con le proprie conoscenze e prospettive uniche su un problema. Quando si tratta di prendere una decisione importante, potresti voler consultare tutti questi esperti per ottenere una previsione più accurata. Allo stesso modo, i metodi di apprendimento di insieme combinano le previsioni di diversi modelli di base per migliorare le prestazioni complessive del modello.

In `sklearn` l'enemble learning viene fatto principalmente con la classe `MajorityVoteClassifier`.

## Tipologie

### Bagging (Bootstrap Aggregating)

Il bagging è una tecnica di ensemble learning che coinvolge l'addestramento di diversi modelli di base su sottoinsiemi casuali del set di dati di addestramento (con il reinserimento).
Ogni modello produce una previsione indipendente e le previsioni sono combinate attraverso il voto o la media per ottenere una previsione finale.
L'obiettivo principale del bagging è ridurre la varianza del modello, riducendo l'overfitting e migliorando la generalizzazione.

### Random Forests

[[Random Forests]] è una variante del bagging che utilizza un insieme di alberi decisionali come modelli di base. Ogni albero è addestrato su un sottoinsieme casuale delle features e dei record del set di dati di addestramento. Le previsioni di tutti gli alberi sono combinate attraverso il voto o la media per ottenere una previsione finale.
Random Forests sono noti per la loro robustezza e capacità di gestire set di dati complessi con molte features.

### Boosting

Nel boosting, l’insieme è costituito da classificatori base molto semplici, chiamati anche sistemi di apprendimento deboli (weak learner), i quali sono dotati di un debole vantaggio prestazionale rispetto alla scelta casuale. Un tipico esempio di sistema di apprendimento debole potrebbe essere un “moncone” di un albero decisionale. Il concetto su cui si basa il boosting è quello di concentrarsi sui campioni di addestramento difficili da classificare, ovvero far sì che i sistemi di apprendimento deboli agiscano sui campioni di apprendimento mal classificati, con lo scopo di migliorare le prestazioni dell’insieme. Al contrario del bagging, la formulazione iniziale del boosting, l’algoritmo utilizza sottoinsiemi casuali dei campioni di addestramento, tratti da un dataset di addestramento e senza reinserimento. La procedura di boosting originale può essere riepilogata in quattro passi. Estrarre senza reinserimento dal set di addestramento un sottoinsieme casuale dei campioni di addestramento per addestrare un sistema di apprendimento debole . Estrarre senza reinserimento dal set di addestramento un secondo sottoinsieme di addestramento casuale e aggiungere un 50% dei campioni che sono stati precedentemente classificati in modo errato, in modo da addestrare un sistema di apprendimento debole . Trovare i campioni di addestramento nel set di addestramento in cui e non concordano, in modo da addestrare un terzo sistema di apprendimento debole . Combinare i risultati dei sistemi di apprendimento deboli , e tramite un voto a maggioranza. 

#### ADABoost

AdaBoost, abbreviazione di Adaptive Boosting, è un'altra tecnica popolare di ensemble learning utilizzata per migliorare le prestazioni dei modelli di machine learning. È particolarmente efficace nei problemi di classificazione, ma può essere adattato anche per problemi di regressione.

AdaBoost utilizza un set di addestramento completo per addestrare i sistemi di apprendimento deboli, ==dove i campioni di addestramento vengono ripesati a ogni iterazione==, in modo da costruire un classificatore più efficace, che impara dagli errori dei precedenti sistemi di apprendimento deboli dell’insieme.

Il processo di addestramento avviene in diverse fasi:

1. **Inizializzazione dei pesi:** Inizialmente, ogni record nel set di addestramento viene assegnato a un peso uniforme, in modo che ogni record abbia lo stesso peso nell'addestramento del modello.
2. **Addestramento dei modelli di base:** AdaBoost addestra un modello di base, tipicamente un classificatore debole, utilizzando il set di addestramento. Un classificatore debole è un modello che ha prestazioni leggermente migliori di un tasso casuale, come un albero decisionale molto superficiale.
3. **Calcolo dell'errore:** Una volta addestrato il modello di base, AdaBoost calcola l'errore del modello confrontando le sue previsioni con le etichette effettive nel set di addestramento. Gli errori maggiori ricevono un peso maggiore nella fase successiva.
4. **Aggiornamento dei pesi:** AdaBoost aggiorna i pesi dei record del set di addestramento in base agli errori commessi dal modello di base. I record che sono stati classificati erroneamente ricevono un peso maggiore, mentre quelli classificati correttamente ricevono un peso inferiore.
5. **Costruzione del modello finale:** Il processo viene iterato, con l'addestramento di nuovi modelli di base su versioni pesate del set di addestramento. Ad ogni iterazione, il modello finale combina le previsioni di tutti i modelli di base pesati in base alle loro prestazioni relative.

AdaBoost è particolarmente potente perché concentra l'attenzione sui record più difficili da classificare, permettendo così di focalizzarsi sui punti deboli del modello e migliorare progressivamente le prestazioni complessive del modello finale.
È noto per la sua capacità di produrre modelli complessi e altamente accurati utilizzando solo classificatori deboli come modelli di base.

### Gradient Boosting Machines (GBM)

GBM è una variante del boosting che addestra modelli di base in sequenza, ciascuno dei quali cerca di ridurre il residuo dell'errore fatto dai modelli precedenti.
Il modello finale è una combinazione pesata di tutti i modelli di base, dove i pesi sono assegnati in base alle prestazioni relative dei modelli.
GBM è noto per la sua efficacia nella modellazione di dati strutturati e la sua capacità di gestire set di dati di grandi dimensioni con molte features.

### Stacking

Lo stacking è una tecnica di ensemble learning che combina le previsioni di diversi modelli di base utilizzando un modello metalearner.
I modelli di base producono le loro previsioni, che vengono quindi utilizzate come features di input per addestrare il modello metalearner.
Il modello metalearner impara a combinare le previsioni dei modelli di base in modo ottimale per ottenere una previsione finale.
Stacking è noto per la sua flessibilità e la sua capacità di catturare relazioni complesse nei dati.

## Svantaggi

L’apprendimento d’insieme incrementa la complessità computazionale rispetto ai singoli classificatori. Nella pratica, dobbiamo riflettere attentamente se intendiamo pagare il prezzo di questo maggiore costo computazionale per ottenere solo un relativamente modesto miglioramento delle prestazioni predittive.