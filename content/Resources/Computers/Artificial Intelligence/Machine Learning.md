
![[machine-learning-map.png]]

![[public_images_1605842918803-AI+vs+ML+vs+DL.png|600]]

L'intelligenza artificiale è un campo dell'informatica che si occupa di sviluppare algoritmi e sistemi in grado di eseguire compiti che richiedono solitamente l'intelligenza umana, come il riconoscimento di pattern, il ragionamento, la pianificazione e l'apprendimento automatico.
Il Machine Learning è una branca dell'Intelligenza Artificiale che si concentra sull'idea di ==far imparare ai computer attraverso l'esperienza==, piuttosto che essere esplicitamente programmati per compiere un compito specifico. Invece di seguire regole specifiche, i modelli di machine learning sono in grado di migliorare le loro prestazioni man mano che vengono esposti a più dati.
Il Deep Learning è un sottoinsieme del Machine Learning che si basa su [[Reti neurali]] artificiali con molti strati (profondi) di neuroni. Questi modelli sono in grado di apprendere direttamente dai dati, e sono particolarmente efficaci nel riconoscere modelli complessi e fare previsioni in una vasta gamma di domini, come il riconoscimento di immagini, il riconoscimento del linguaggio naturale e altro ancora.
Gli algoritmi di machine learning si basano tutti sull'apprendimento a partire da un [[dataset]], in particolare questo viene tipicamente diviso in [[Train, test e validation set]] in modo da avere dei dati per la costruzione del modello e altri per la valutazione dello stesso.

## Tipologie

### Apprendimento supervisionato

L'apprendimento supervisionato è un approccio in cui il modello viene allenato su un set di dati etichettato, il che significa che ogni esempio nel set di dati è accompagnato dalla risposta corretta (etichetta). L'obiettivo è quello di apprendere una funzione che, data un'entrata, può predire l'etichetta di uscita.
Le due macrocategorie di problemi per l'apprendimento supervisionato sono:
- **[[Classificazione]]:** L’obiettivo è quello di prevedere le etichette di categoria delle classi per le nuove istanze, sulla base delle osservazioni compiute nel passato.. Ad esempio, determinare se un'email è spam o no.
- **[[Regressione]]** Implica la previsione di un valore numerico continuo basato su variabili indipendenti. Un esempio è la previsione del prezzo di una casa in base alle sue caratteristiche.    

### Apprendimento Non Supervisionato (Unsupervised Learning)

L'apprendimento non supervisionato coinvolge la modellazione di dati non etichettati. Il modello cerca di comprendere la struttura dei dati senza etichette predefinite.
Le categorie questo apprendimento sono:
* **Clustering**: Il clustering è una tecnica esplorativa di analisi dei dati che ci consente di organizzare una serie di informazioni all’interno di gruppi significativi (i cluster) senza avere alcuna precedente conoscenza delle appartenenze a tali gruppi. Alcuni metodi di clustering includono:
	* K-Means: Partiziona i dati in 'k' gruppi.
	* Mean Shift: Trova i centroidi dei dati basandosi sulla densità.
	* C-Means Fuzzy (Fuzzy C-Means): Assegna probabilità di appartenenza ai cluster.
	* DBSCAN: Basato sulla densità, identifica 'spot' di alta densità.
* **Association Rule Learning**: L'apprendimento delle regole di associazione è usato per scoprire relazioni interessanti tra variabili in grandi database. Algoritmi noti includono:
	* FP Growth: Utilizza una struttura ad albero per il calcolo delle frequenze.
	- Apriori: Un algoritmo iterativo che identifica gli insiemi di oggetti frequenti.
- [[Riduzione della Dimensionalità]]: La riduzione della dimensionalità riduce il numero di variabili casuali da considerare. Tecniche comuni sono:
	- PCA (Principal Component Analysis): Riduce la dimensionalità attraverso la decomposizione ortogonale.
	- LDA (Linear Discriminant Analysis): Trova una combinazione lineare di caratteristiche che separano due o più classi di oggetti o eventi.
	- SVD (Singular Value Decomposition): Fattorizza una matrice in valori singolari e vettori singolari.

### Reinforcement Learning

Qui l’obiettivo è quello di sviluppare un sistema (agente) che migliori le proprie prestazioni ==sulla base delle interazioni con l’ambiente==. Poiché, tipicamente, le informazioni relative allo stato corrente dell’ambiente includono anche un cosiddetto segnale di ricompensa (reward), possiamo considerare l’apprendimento di rafforzamento come un esempio di apprendimento con supervisione. Tuttavia, nell’apprendimento di rafforzamento, ==questo feedback non è l’etichetta o il valore corretto di verità, ma una misura della qualità con cui l’azione è stata misurata da una funzione di ricompensa==.
Algoritmi comuni includono:
- Q-Learning: Un algoritmo di apprendimento basato sul valore che cerca di trovare una politica che massimizza la ricompensa totale.
- DQN (Deep Q-Network): Combina Q-Learning con reti neurali profonde.
- A3C (Asynchronous Advantage Actor-Critic): Utilizza più copie dell'agente che lavorano in parallelo.

### Deep Learning

Il deep learning è un sottoinsieme del machine learning in cui vengono utilizzate reti neurali con diverse strati nascosti.

* [[Rete neurale convoluzionale|Reti neurali convoluzionali]]: le CNN sono particolarmente efficaci nell'elaborazione di dati strutturati come le immagini.
* [[Reti neurali ricorrenti]]: le RNN sono progettate per lavorare con sequenze di dati, come il linguaggio naturale o le serie temporali.
* Generative Adversarial Networks (GAN): le GAN sono composti da due reti neurali, una che genera dati e l'altra che cerca di discriminare tra dati generati e reali.

### [[Ensemble Learning]]
L'apprendimento ensemble combina le previsioni di più modelli per migliorare l'affidabilità e l'accuratezza.
* **Bagging**: il Bagging crea più versioni di un modello di allenamento su sottocampioni del set di dati e poi aggrega le loro previsioni.
* **Boosting**: Il Boosting costruisce sequenzialmente modelli, dove ogni modello cerca di correggere gli errori del modello precedente.
* **Random Forest**: una collezione di alberi decisionali che migliora la stabilità e l'accuratezza.
* **XGBoost, LightGBM, CatBoost**: Algoritmi di boosting ottimizzati per velocità ed efficacia.

## Step

Ogni algoritmo di machine learning è più o meno definito dai seguenti passi.

### Pre-processing

Questo processo è cruciale per garantire che i dati siano adatti per l'addestramento del modello e per massimizzare le prestazioni del modello stesso. Ecco alcuni esempi di tecniche di pre-processing comuni:

1. **[[Selezione delle features]]**
2. **[[Algoritmi di encoding|Encoding]] delle [[Variabili categoriche e non|Variabili Categoriche]]**:
   - Le variabili categoriche, come il genere o il colore preferito, devono essere convertite in una forma numerica in modo che il modello possa utilizzarle.
   - Le tecniche di encoding comuni includono l'[[One-Hot Encoding]], il [[Label Encoding]] e il Target Encoding.
3. **[[Normalizzazione dei dati]]**:
   - La normalizzazione dei dati consiste nel ridurre la scala dei dati in modo che tutte le caratteristiche abbiano lo stesso ordine di grandezza.
   - Questo è particolarmente importante per algoritmi basati sulla distanza, come k-Nearest Neighbors (K-NN) o [[Support Vector Machines (SVM)]].
   - Nella visione la [[Normalizzazione pixel|normalizzazione a pixel]].
4. **[[Standardizzazione dei dati]]**:
   - La standardizzazione dei dati consiste nel centrare i dati attorno a zero (cioè sottrarre la media) e nel ridurre la loro varianza a uno (cioè dividere per la deviazione standard).
   - Questo è utile soprattutto per algoritmi che assumono una distribuzione normale dei dati, come la Regressione Lineare o le Reti Neurali.
5. **[[Gestione dei Dati Mancanti]]**:
   - I dati mancanti possono influenzare negativamente le prestazioni del modello. È necessario decidere come gestire i dati mancanti, ad esempio eliminando le righe o le colonne con valori mancanti, o imputando i valori mancanti con la media o la mediana dei dati.
6. **[[Riduzione della Dimensionalità]]**:
   - Ridurre la dimensionalità dei dati può migliorare le prestazioni del modello e ridurre i tempi di addestramento.
   - Tecniche come l'analisi delle componenti principali (PCA) o la selezione delle caratteristiche possono essere utilizzate per ridurre il numero di variabili.
7. **Gestione degli Outlier**:
   - Gli outlier sono valori anomali che possono influenzare negativamente il modello. È importante identificarli e decidere se eliminarli o trattarli in modo appropriato.

Posso concatenare le varie fasi del pre-processing usando l'oggetto [[Pipeline]] di `sklearn`.

### Scelta del modello (Define)
Esistono numerosissimi algoritmi e l'abilità della persona sta nel scegliere, o trovare il modo di scegliere quello corretto per il problema che deve affrontare.
Per esempio per un problema di classificazione vi sono [[Classificazione#^84ab24|questi algoritmi]].


### Addestramento (Fit)
L'addestramento è dove vengono rilevati dal modello i pattern rilevanti nel dataset.

### [[Valutazione delle prestazioni del modello]]
In questo step vengono fatte le previsioni su dei nuovi dati non usati nell'addestramento (validation data) al fine di capire se il modello è ok o deve essere ottmizzato.

### Ottimizzazione dell’algoritmo
In base alle performance sopra si possono ottimizzare gli iperparametri del modello tramite degli algoritmi (esempio validazione incrociata o la ricerca a griglia) e riiniziare dal fit.

### Inferenza
Una volta che il modello è addestrato e ottimizzato, è possibile utilizzarlo per effettuare previsioni su nuovi dati.


## Applicazioni di Deep Learning
### Computer Vision

L'intelligenza artificiale ha rivoluzionato il campo della computer vision, introducendo strumenti e tecniche che hanno notevolmente migliorato la capacità delle macchine di interpretare e interagire con il mondo visivo.
Rivoluzionarie per la computer vision sono le [[Rete neurale convoluzionale|reti neurali convoluzionali]] e la loro più famosa applicazione che è la [[YOLO]].

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


## Varie

* [[Semantic Kernel]]
* [[Formato ONNX]]


TODO ARRIVATO LIBRO: Valutazione della rilevanza delle parole in base alla frequenza (inversa) dei termini nel documento