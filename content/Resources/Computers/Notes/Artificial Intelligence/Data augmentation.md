---
tags:
  - MachineLearning
  - ComputerVision
---
La data augmentation è una tecnica utilizzata nell'addestramento delle reti neurali per aumentare la quantità di dati disponibili e migliorare le prestazioni del modello. Consiste nel creare nuovi esempi di addestramento a partire dai campioni originali, applicando trasformazioni casuali come rotazione, zoom, shift orizzontale o verticale, flip orizzontale o verticale e altri tipi di manipolazioni.

L'obiettivo della data augmentation è quello di generare un insieme più ampio e variegato di dati che il modello può imparare durante l'addestramento. Ciò aiuta a prevenire l'overfitting e migliorare le prestazioni generali del modello su nuovi dati.

Ci sono diverse tecniche implementative per la data augmentation:

1. Rotazione: ruotando leggermente le immagini in modo casuale (per esempio tra -10° e +10°) si possono ottenere varianti dell’immagine originale;
2. Zoom: ingrandendo / rimpicciolendo in modo casuale l’immagine originale si possono ottenere varianti con oggetti più vicini / distanti;
3. Shift orizzontali/verticali: spostando leggermente l’immagine verso sinistra/destra/alto/basso si possono ottenere varianti dell’immagine originale;
4. Flip orizzontali/verticalia : ribaltando lateralmente/orizontalmente rispetto all'asse centrale dell’immagine si ottiene una nuova variante simmetrica dall’originale
5. Cambiare luminosità/contrastro/saturazione dei pixel dell'immmaginie rende ancora diverso ogni singolo sample.
6. altre tecniche specifiche per problem-specific (esempio aggiungere rumore alle immagini mediche)

Inoltre è possibile combinare queste tecniche assieme oppure creandone delle proprie personalizzate.

L'applicazione della data augmentation può essere fatta sia durante la fase di preprocessing dei dati che on-the-fly durante il training stesso attraverso librerie apposite come [[Keras]] `ImageDataGenerator` o [[PyTorch]] `torchvision.transforms` eccetera