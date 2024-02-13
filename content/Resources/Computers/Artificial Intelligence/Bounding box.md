---
tags:
  - ComputerVision
  - DeepLearning
---
In una rete neurale [[YOLO]] (You Only Look Once), il bounding box è un rettangolo che definisce la posizione e le dimensioni di un oggetto all'interno di un'immagine.

La rete YOLO utilizza i bounding box per individuare gli oggetti presenti in un'immagine e prevedere la loro classe. Ogni bounding box è descritto da quattro parametri: le coordinate x e y del vertice superiore sinistro, l'altezza e la larghezza del rettangolo.

Durante il processo di addestramento della rete YOLO, l'algoritmo cerca di ottimizzare i pesi della rete per minimizzare l'errore tra i bounding box previsti dalla rete neurale e quelli reali presenti nelle immagini di training. In questo modo, la precisione dell'algoritmo nel rilevare gli oggetti aumenta progressivamente durante il processo di apprendimento automatico.

Uno dei vantaggi principali delle reti neurali YOLO rispetto ad altre tecniche per il rilevamento degli oggetti basate su sliding windows o R-CNN (Region-Based Convolutional Neural Networks) è che riescono a processare intere immagini in una sola volta invece che analizzarle frammento per frammento. Ciò consente alle reti YOLO di essere molto più veloci nell'esecuzione rispetto ad altri algoritmi senza perdere accuratezza nella predizione dei risultati.

In sintesi, il bounding box rappresenta uno strumento fondamentale nella tecnica utilizzata dalle reti neurali YOLO per individuare ed etichettare gli oggetti all'interno delle immagini con elevata precisione ed efficienza computazionale.

### Label

Ad ogni bounding box individuato dalla rete neurale YOLO è associata una label che indica la classe dell'oggetto rilevato.

Nel processo di addestramento della rete YOLO, i bounding box sono etichettati con le rispettive classi degli oggetti presenti nell'immagine. Ad esempio, se l'immagine contiene un cane e un gatto, ciascun bounding box corrispondente verrà etichettato con la rispettiva classe "cane" o "gatto".

Durante il processo di inferenza (ovvero quando si utilizza la rete neurale per analizzare nuove immagini), la rete YOLO utilizza i bounding box previsti insieme alle relative probabilità di appartenenza a ciascuna classe per identificare gli oggetti presenti nell'immagine.

In questo modo, la combinazione tra l'utilizzo dei bounding box e delle label consente alla rete neurale YOLO di effettuare una precisa segmentazione degli oggetti all'interno delle immagini e prevedere in maniera accurata le loro classi.

In sintesi, ogni bounding box individuato dalla rete neurale YOLO è associato a una specifica label che rappresenta la classe dell'oggetto rilevato.

### Software

Esistono diversi software che consentono di creare bounding box e associarle ad ognuna una label. Questi strumenti sono spesso utilizzati durante la preparazione dei dati per l'addestramento della rete YOLO.

Ecco alcuni esempi di software:

1. LabelImg: è un'applicazione open source disponibile su Windows, Mac OS X e Linux che consente di creare facilmente bounding box sulle immagini e assegnare etichette alle varie classi degli oggetti rilevabili.

2. RectLabel: è un software a pagamento solo per macOS che permette di disegnare le caselle delimitatrici intorno agli oggetti in modo molto preciso ,associando poi ad ognuna delle etichette personalizzate dall’utente .

3. VGG Image Annotator (VIA): si tratta di uno strumento basato sul web gratuito sviluppato dal Visual Geometry Group dell'Università di Oxford . VIA consente agli utenti di annotare immagini con diverse forme geometriche come poligoni, rettangoli o cerchi ed associarli alle relative label .

Queste applicazioni semplificano notevolmente il processo manuale richiesto dalla fase preliminari alla costruzione del [[GPT Model|modello]] AI , riducendo al minimo gli errori umani nella definizione delle aree d’interesse all’interno dell’immagine stessa.
Inoltre questi tool offrono anche funzionalità avanzate come l’esportazione dei file creati in formato compatibile con i principali framework deep learning tra cui Tensorflow e [[PyTorch]].