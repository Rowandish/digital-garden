![[public_images_1605842918803-AI+vs+ML+vs+DL.png|600]]

L'intelligenza artificiale è un campo dell'informatica che si occupa di sviluppare algoritmi e sistemi in grado di eseguire compiti che richiedono solitamente l'intelligenza umana, come il riconoscimento di pattern, il ragionamento, la pianificazione e l'apprendimento automatico.
Il Machine Learning è una branca dell'Intelligenza Artificiale che si concentra sull'idea di far imparare ai computer attraverso l'esperienza, piuttosto che essere esplicitamente programmati per compiere un compito specifico. Invece di seguire regole specifiche, i modelli di machine learning sono in grado di migliorare le loro prestazioni man mano che vengono esposti a più dati.
Il Deep Learning è un sottoinsieme del Machine Learning che si basa su [[Reti neurali]] artificiali con molti strati (profondi) di neuroni. Questi modelli sono in grado di apprendere direttamente dai dati, e sono particolarmente efficaci nel riconoscere modelli complessi e fare previsioni in una vasta gamma di domini, come il riconoscimento di immagini, il riconoscimento del linguaggio naturale e altro ancora.
Gli algoritmi di machine learning si basano tutti sull'apprendimento a partire da un [[dataset]], in particolare questo viene tipicamente diviso in [[Train set e Test set]] in modo da avere dei dati per la costruzione del modello e altri per la valutazione dello stesso.

### Tipologie di Machine Learning

* **Apprendimento con supervisione**: Lo scopo principale dell’apprendimento con supervisione consiste nel trarre un modello ==a partire da dati di addestramento etichettat==i, i quali ci consentono di effettuare previsioni relative a dati non disponibili o futuri. Qui il termine con supervisione fa riferimento al fatto che nell’insieme di campioni i segnali di output desiderati (le etichette) sono già noti.
* **Apprendimento senza supervisione**: In questo caso ==i dati di addestramento non sono etichettati== e sarà l'algoritmo che dovrà rilevare le relazioni tra gli stessi.
* **Reinforcement Learning**: Qui l’obiettivo è quello di sviluppare un sistema (agente) che migliori le proprie prestazioni ==sulla base delle interazioni con l’ambiente==. Poiché, tipicamente, le informazioni relative allo stato corrente dell’ambiente includono anche un cosiddetto segnale di ricompensa (reward), possiamo considerare l’apprendimento di rafforzamento come un esempio di apprendimento con supervisione. Tuttavia, nell’apprendimento di rafforzamento, ==questo feedback non è l’etichetta o il valore corretto di verità, ma una misura della qualità con cui l’azione è stata misurata da una funzione di ricompensa==.

### Tipologie di problemi da risolvere 

L'intelligenza artificiale può aiutare a risolvere una gran quantità di problemi di diversa natura, per esempio i seguenti:

#### Con supervisione

- **[[Classificazione]]:** L’obiettivo è quello di prevedere le etichette di categoria delle classi per le nuove istanze, sulla base delle osservazioni compiute nel passato.. Ad esempio, determinare se un'email è spam o no.
- **[[Regressione]]** Implica la previsione di un valore numerico continuo basato su variabili indipendenti. Un esempio è la previsione del prezzo di una casa in base alle sue caratteristiche.    
#### Senza supervisione

- **Clustering:** Il clustering è una tecnica esplorativa di analisi dei dati che ci consente di organizzare una serie di informazioni all’interno di gruppi significativi (i cluster) senza avere alcuna precedente conoscenza delle appartenenze a tali gruppi. Ogni cluster che può essere derivato durante l’analisi definisce un gruppo di oggetti che condividono un certo grado di similarità, ma che sono più dissimili rispetto agli oggetti presenti negli altri cluster, motivo per cui il clustering viene talvolta chiamato “classificazione senza supervisione”.
- **Analisi di Pattern:** Si riferisce all'identificazione e all'analisi di modelli o strutture regolari nei dati, come riconoscere sequenze ricorrenti in serie temporali o dati spaziali.
- **Riduzione Dimensionale**: l'obiettivo è ridurre il numero di variabili di input mantenendo il maggior numero possibile di informazioni rilevanti. Spesso ci troviamo a operare con dati a elevata dimensionalità (ogni osservazione fornisce un elevato numero di misure) il che può rappresentare una sfida in termini di spazio di memorizzazione disponibile e prestazioni computazionali degli algoritmi di apprendimento automatico. 

## Pre-processing

Questo processo è cruciale per garantire che i dati siano adatti per l'addestramento del modello e per massimizzare le prestazioni del modello stesso. Ecco alcuni esempi di tecniche di pre-processing comuni:

1. **[[Algoritmi di encoding|Encoding]] delle [[Variabili categoriche e non|Variabili Categoriche]]**:
   - Le variabili categoriche, come il genere o il colore preferito, devono essere convertite in una forma numerica in modo che il modello possa utilizzarle.
   - Le tecniche di encoding comuni includono l'[[One-Hot Encoding]], il [[Label Encoding]] e il Target Encoding.
2. **[[Normalizzazione dei dati]]**:
   - La normalizzazione dei dati consiste nel ridurre la scala dei dati in modo che tutte le caratteristiche abbiano lo stesso ordine di grandezza.
   - Questo è particolarmente importante per algoritmi basati sulla distanza, come k-Nearest Neighbors (K-NN) o Support Vector Machines (SVM).
   - Nella visione la [[Normalizzazione pixel|normalizzazione a pixel]].
3. **[[Standardizzazione dei dati]]**:
   - La standardizzazione dei dati consiste nel centrare i dati attorno a zero (cioè sottrarre la media) e nel ridurre la loro varianza a uno (cioè dividere per la deviazione standard).
   - Questo è utile soprattutto per algoritmi che assumono una distribuzione normale dei dati, come la Regressione Lineare o le Reti Neurali.
4. **[[Gestione dei Dati Mancanti]]**:
   - I dati mancanti possono influenzare negativamente le prestazioni del modello. È necessario decidere come gestire i dati mancanti, ad esempio eliminando le righe o le colonne con valori mancanti, o imputando i valori mancanti con la media o la mediana dei dati.
5. **[[Riduzione della Dimensionalità]]**:
   - Ridurre la dimensionalità dei dati può migliorare le prestazioni del modello e ridurre i tempi di addestramento.
   - Tecniche come l'analisi delle componenti principali (PCA) o la selezione delle caratteristiche possono essere utilizzate per ridurre il numero di variabili.
6. **Gestione degli Outlier**:
   - Gli outlier sono valori anomali che possono influenzare negativamente il modello. È importante identificarli e decidere se eliminarli o trattarli in modo appropriato.

Posso concatenare le varie fasi del pre-processing usando l'oggetto [[Pipeline]] di `sklearn`.
## Addestramento

I cinque passi principali che sono coinvolti nell’addestramento di un algoritmo di machine learning e possono essere riepilogati nel seguente modo.
* Scelta delle caratteristiche;
* Scelta di una [[Valutazione delle prestazioni del modello#^98f960|Metrica prestazionale]];
* Scelta di un algoritmo per la classificazione e per l'ottimizzazione;
* [[Valutazione delle prestazioni del modello]];
* Ottimizzazione dell’algoritmo.

## Applicazioni di Deep Learning
### Computer Vision

L'intelligenza artificiale ha rivoluzionato il campo della computer vision, introducendo strumenti e tecniche che hanno notevolmente migliorato la capacità delle macchine di interpretare e interagire con il mondo visivo.

#### YOLO

[[YOLO]] (You Only Look Once) rappresenta un punto di svolta nel riconoscimento degli oggetti nell'ambito della computer vision, grazie alla sua capacità unica di rilevare oggetti in un'unica passata attraverso l'immagine, a differenza degli approcci tradizionali che richiedono più passaggi. Cruciali in YOLO sono le [[bounding box]], che delineano e identificano la posizione degli oggetti nell'immagine, assegnando a ciascuna un punteggio di fiducia e una classe di appartenenza; per evitare la creazione di multiple bounding box per lo stesso oggetto, si adotta la tecnica di [[Non-Maximum Suppression (NMS)]], che seleziona la bounding box con il punteggio più alto e elimina quelle con un'elevata sovrapposizione, migliorando così l'accuratezza del rilevamento.

#### Tools

Nel contesto dell'evoluzione della computer vision, due aspetti cruciali sono stati lo sviluppo di librerie come [[TorchVision]], parte dell'ecosistema [[PyTorch]], che ha notevolmente semplificato il lavoro degli sviluppatori offrendo una vasta gamma di dataset pre-caricati, modelli e trasformazioni per facilitare l'addestramento e lo sviluppo di modelli di intelligenza artificiale per la visione, e l'interoperabilità tra diversi framework di intelligenza artificiale, una sfida risolta efficacemente dal [[formato ONNX]] (Open Neural Network Exchange), che consente il trasferimento di modelli tra vari framework senza perdita di efficienza, promuovendo la portabilità e la scalabilità dei modelli AI in diversi ambienti di produzione.

#### Preprocessing

Due tecniche essenziali per l'ottimizzazione dei modelli di intelligenza artificiale sono la [[Normalizzazione pixel|normalizzazione dei pixel]] e la [[data augmentation]]: la normalizzazione dei pixel, un processo che modifica i valori dei pixel per una distribuzione più uniforme e quindi cruciale per migliorare prestazioni e velocità dei modelli di apprendimento profondo, evitando l'influenza di variazioni di luminosità o colore irrilevanti, si affianca alla data augmentation, una tecnica che accresce varietà e quantità dei dati di addestramento attraverso modifiche come rotazioni, traslazioni, zoom e variazioni cromatiche, migliorando così la capacità del modello di generalizzare e operare efficacemente in scenari reali.

### Large Language Models

Gli Large Language Models (LLM) sono noti per la loro capacità di generare testi realistici e coerenti, aprendo nuove frontiere in applicazioni diverse, dalla scrittura creativa all'assistenza clienti.

Il cuore di questi modelli, come il [[GPT Model|GPT]], è costituito da milioni di parametri addestrati su vasti set di dati. Questi modelli apprendono a riconoscere pattern nel linguaggio e a generarne di nuovi. Grazie a questo addestramento, possono comprendere e produrre lingua su un'ampia gamma di argomenti e stili.

Un aspetto fondamentale per sfruttare al meglio questi modelli è il cosiddetto "[[Prompt Engineering]]". Questa pratica implica la progettazione di input specifici (o prompt) che guidano il modello verso risposte più precise e utili. Attraverso un prompt ben formulato, è possibile dirigere il modello verso un particolare stile di scrittura, tono, o persino verso un argomento specifico. È una sorta di arte, dove la chiarezza e la specificità del prompt determinano la qualità del risultato.

#### Concetti utili

Nel panorama tecnico degli Large Language Models (LLM), due concetti emergono come fondamentali: la [[Cosine Similarity]], un meccanismo matematico che misura la somiglianza tra due vettori e che, nel contesto del linguaggio, è cruciale per determinare la similitudine di contenuto e contesto tra due pezzi di testo, facilitando funzionalità come la classificazione del testo, la risposta alle domande e la generazione di testi pertinenti; e il concetto di [[Token (LLM)|token]], che può essere una parola, una parte di una parola, o anche un segno di punteggiatura, essenziale per gli LLM che analizzano e generano testo dividendo le frasi in token e elaborandoli per costruire o comprendere il significato complessivo, un processo di tokenizzazione che si rivela fondamentale per la flessibilità e l'efficacia di questi modelli nel gestire vari tipi di testi.

#### Cloud

[[Azure OpenAI]] è un esempio di come queste tecnologie vengano implementate in soluzioni cloud. Microsoft, attraverso la sua piattaforma Azure, offre l'accesso ai modelli di OpenAI, permettendo alle aziende di integrare capacità avanzate di elaborazione del linguaggio naturale nei loro sistemi. Questo rende la potenza degli LLM disponibile per un'ampia gamma di applicazioni, dall'analisi di dati alla customer interaction.


## Tools e SDK

* [[Semantic Kernel]]
* [[PyTorch]]
* [[Keras]]
* [[Scikit Learn]]
* [[Jupyter Notebook]]

TODO ARRIVATO LIBRO: Valutazione della rilevanza delle parole in base alla frequenza (inversa) dei termini nel documento