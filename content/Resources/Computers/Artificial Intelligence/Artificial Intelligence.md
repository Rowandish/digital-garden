L'intelligenza artificiale è un campo dell'informatica che si occupa di sviluppare algoritmi e sistemi in grado di eseguire compiti che richiedono solitamente l'intelligenza umana, come il riconoscimento di pattern, il ragionamento, la pianificazione e l'apprendimento automatico.

## Machine Learning

Il machine learning è un ramo dell'intelligenza artificiale che permette ai computer di imparare e migliorare le loro prestazioni compiendo compiti specifici, attraverso l'analisi e l'interpretazione di dati, senza essere esplicitamente programmati per farlo.
Gli algoritmi di machine learning tipicamente seguono una sequenza di passaggi base che includono la raccolta e la preparazione dei dati, la scelta e l'allenamento di un modello su un set di dati, la valutazione delle sue prestazioni e infine l'applicazione del modello per fare previsioni o prendere decisioni su nuovi dati.

Il primo passo nell'allenamento di un modello è la divisione del [[dataset]] in [[Train set e Test set]]. Questo permette al modello di apprendere da un insieme di dati (train set) e poi di essere valutato su un insieme separato e non visto in precedenza (test set). Tale separazione è fondamentale per garantire che il modello sia in grado di generalizzare e non solo di memorizzare le informazioni dei dati di allenamento.

Una volta definiti i train e test set, il processo di allenamento inizia effettivamente. Durante questo processo, è importante monitorare e prevenire l'[[Overfitting]], una condizione in cui il modello si adatta troppo bene ai dati di allenamento, perdendo la capacità di performare efficacemente su dati nuovi o non visti. L'overfitting può portare a prestazioni ingannevolmente elevate sui dati di allenamento ma scarse sui dati di test.

Per mitigare l'overfitting, si applicano tecniche come la [[L1 - L2 regularization]]. Queste tecniche aggiungono un termine di penalità alla funzione di perdita del modello, incentivando la semplicità e riducendo la complessità del modello.

Successivamente, si utilizza una metrica come l'[[Errore quadratico medio]] per valutare le prestazioni del modello. Questa metrica aiuta a capire quanto bene il modello sta prevedendo rispetto ai dati reali, fornendo un feedback essenziale per l'ottimizzazione del modello.

Nel corso dell'allenamento, si definiscono il numero di [[Epoche]] e la [[Batch size]]. Una "epoca" è un termine che indica un completo ciclo di passaggio di tutti i dati di allenamento attraverso il modello. La "batch size" si riferisce al numero di esempi di dati processati prima di aggiornare i parametri del modello. Queste impostazioni influenzano la velocità e l'efficacia dell'apprendimento.

Dopo l'allenamento, il modello è pronto per l'[[Inferenza]], dove viene applicato a nuovi dati per fare previsioni o prendere decisioni basate su ciò che ha appreso.

Infine, durante tutto il processo di allenamento, vengono utilizzati [[Algoritmi di ottimizzazione]] per regolare i parametri del modello in modo da minimizzare la funzione di perdita. Questi algoritmi sono cruciali per garantire che il modello apprenda in modo efficace e efficiente dai dati.

### Tipologie di problemi da risolvere 

L'intelligenza artificiale può aiutare a risolvere una gran quantità di problemi di diversa natura, per esempio i seguenti:

- **Classificazione:** Questo problema si concentra sull'identificazione della categoria a cui appartiene un oggetto basandosi su un insieme di dati di addestramento. Ad esempio, determinare se un'email è spam o no.
- **[[Regressione]]** Implica la previsione di un valore numerico continuo basato su variabili indipendenti. Un esempio è la previsione del prezzo di una casa in base alle sue caratteristiche.    
- **Clustering:** Questa tecnica raggruppa insiemi di dati in sottogruppi (cluster) in base alla loro somiglianza, utilizzata per scoprire strutture o pattern nascosti nei dati senza etichette predefinite.    
- **Analisi di Pattern:** Si riferisce all'identificazione e all'analisi di modelli o strutture regolari nei dati, come riconoscere sequenze ricorrenti in serie temporali o dati spaziali.

## Computer Vision

L'intelligenza artificiale ha rivoluzionato il campo della computer vision, introducendo strumenti e tecniche che hanno notevolmente migliorato la capacità delle macchine di interpretare e interagire con il mondo visivo.

### YOLO

[[YOLO]] (You Only Look Once) rappresenta un punto di svolta nel riconoscimento degli oggetti nell'ambito della computer vision, grazie alla sua capacità unica di rilevare oggetti in un'unica passata attraverso l'immagine, a differenza degli approcci tradizionali che richiedono più passaggi. Cruciali in YOLO sono le [[bounding box]], che delineano e identificano la posizione degli oggetti nell'immagine, assegnando a ciascuna un punteggio di fiducia e una classe di appartenenza; per evitare la creazione di multiple bounding box per lo stesso oggetto, si adotta la tecnica di [[Non-Maximum Suppression (NMS)]], che seleziona la bounding box con il punteggio più alto e elimina quelle con un'elevata sovrapposizione, migliorando così l'accuratezza del rilevamento.

### Tools

Nel contesto dell'evoluzione della computer vision, due aspetti cruciali sono stati lo sviluppo di librerie come [[TorchVision]], parte dell'ecosistema [[PyTorch]], che ha notevolmente semplificato il lavoro degli sviluppatori offrendo una vasta gamma di dataset pre-caricati, modelli e trasformazioni per facilitare l'addestramento e lo sviluppo di modelli di intelligenza artificiale per la visione, e l'interoperabilità tra diversi framework di intelligenza artificiale, una sfida risolta efficacemente dal [[formato ONNX]] (Open Neural Network Exchange), che consente il trasferimento di modelli tra vari framework senza perdita di efficienza, promuovendo la portabilità e la scalabilità dei modelli AI in diversi ambienti di produzione.

### Preprocessing

Due tecniche essenziali per l'ottimizzazione dei modelli di intelligenza artificiale sono la [[Normalizzazione pixel|normalizzazione dei pixel]] e la [[data augmentation]]: la normalizzazione dei pixel, un processo che modifica i valori dei pixel per una distribuzione più uniforme e quindi cruciale per migliorare prestazioni e velocità dei modelli di apprendimento profondo, evitando l'influenza di variazioni di luminosità o colore irrilevanti, si affianca alla data augmentation, una tecnica che accresce varietà e quantità dei dati di addestramento attraverso modifiche come rotazioni, traslazioni, zoom e variazioni cromatiche, migliorando così la capacità del modello di generalizzare e operare efficacemente in scenari reali.

## Large Language Models

Gli Large Language Models (LLM) sono noti per la loro capacità di generare testi realistici e coerenti, aprendo nuove frontiere in applicazioni diverse, dalla scrittura creativa all'assistenza clienti.

Il cuore di questi modelli, come il [[GPT Model|GPT]], è costituito da milioni di parametri addestrati su vasti set di dati. Questi modelli apprendono a riconoscere pattern nel linguaggio e a generarne di nuovi. Grazie a questo addestramento, possono comprendere e produrre lingua su un'ampia gamma di argomenti e stili.

Un aspetto fondamentale per sfruttare al meglio questi modelli è il cosiddetto "[[Prompt Engineering]]". Questa pratica implica la progettazione di input specifici (o prompt) che guidano il modello verso risposte più precise e utili. Attraverso un prompt ben formulato, è possibile dirigere il modello verso un particolare stile di scrittura, tono, o persino verso un argomento specifico. È una sorta di arte, dove la chiarezza e la specificità del prompt determinano la qualità del risultato.

### Concetti utili

Nel panorama tecnico degli Large Language Models (LLM), due concetti emergono come fondamentali: la [[Cosine Similarity]], un meccanismo matematico che misura la somiglianza tra due vettori e che, nel contesto del linguaggio, è cruciale per determinare la similitudine di contenuto e contesto tra due pezzi di testo, facilitando funzionalità come la classificazione del testo, la risposta alle domande e la generazione di testi pertinenti; e il concetto di [[Token (LLM)|token]], che può essere una parola, una parte di una parola, o anche un segno di punteggiatura, essenziale per gli LLM che analizzano e generano testo dividendo le frasi in token e elaborandoli per costruire o comprendere il significato complessivo, un processo di tokenizzazione che si rivela fondamentale per la flessibilità e l'efficacia di questi modelli nel gestire vari tipi di testi.

### Cloud

[[Azure OpenAI]] è un esempio di come queste tecnologie vengano implementate in soluzioni cloud. Microsoft, attraverso la sua piattaforma Azure, offre l'accesso ai modelli di OpenAI, permettendo alle aziende di integrare capacità avanzate di elaborazione del linguaggio naturale nei loro sistemi. Questo rende la potenza degli LLM disponibile per un'ampia gamma di applicazioni, dall'analisi di dati alla customer interaction.


## Data Science



## Tools e SDK

* [[Semantic Kernel]]
* [[PyTorch]]
* [[Keras]]
* [[Scikit Learn]]
* [[Jupyter Notebook]]
