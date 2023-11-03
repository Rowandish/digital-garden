---
tags:
  - MachineLearning
  - ComputerVision
---
A rete YOLO (You Only Look Once) è un **algoritmo di rilevamento degli oggetti utilizzato nell'intelligenza artificiale**.

YOLO utilizza una singola [[Rete neurale convoluzionale]] per **trovare le posizioni degli oggetti in un'immagine e classificarli contemporaneamente**. Ciò significa che l'algoritmo può ==individuare più oggetti in una sola volta==, senza la necessità di eseguire il processo più volte come avviene con altre tecniche.

Il funzionamento della rete YOLO si basa su due componenti principali: la prima è la suddivisione dell'immagine in una griglia regolare, mentre la seconda consiste nella previsione delle caselle contenenti gli oggetti e delle relative etichette.

In pratica, **l'algoritmo divide l'immagine in celle rettangolari sovrapposte tra loro; ogni cella viene poi analizzata per determinare se contiene o meno un oggetto e quale sia la sua classe** (ad esempio persona, cane o macchina). Questo viene fatto attraverso l'utilizzo di filtri convoluzionali che scansionano ogni cella dell'immagine per identificare i tratti distintivi dei vari tipi di oggetti.

Una volta completata questa fase preliminare, ==YOLO procede a calcolare le probabilità associate ad ogni casella contenente un possibile oggetto. Inoltre, vengono anche generate coordinate precise per ogni box contenente gli oggetti individuati dall’algoritmo==.

L'algoritmo successivamente applica alcune strategie avanzate come [[Non-maximum suppression (NMS)]], ovvero rimozione dei box duplicati ed eliminazione degli elementi superflui presenti all’interno del frame così da ottenere solo quelli significativi ai fini della classificazione richiesta dal sistema AI.

## Vantaggi

I vantaggi offerti dalla rete YOLO sono molteplici: innanzitutto consente una maggiore velocità rispetto ad altri metodi poiché evita il passaggio attraverso varie fasi intermedie; inoltre permette di individuare oggetti molto piccoli o parzialmente nascosti, che potrebbero essere persi da altre tecniche. Inoltre, la capacità di rilevare più oggetti contemporaneamente rende YOLO particolarmente utile in applicazioni come il monitoraggio del traffico stradale e la sorveglianza video.

## Limiti

Tuttavia, ci sono anche alcune limitazioni della rete YOLO. Ad esempio, l'algoritmo può avere difficoltà a distinguere tra oggetti simili ma con dimensioni diverse (come un gatto e un leopardo) o a identificare correttamente gli oggetti quando si sovrappongono. Inoltre, poiché utilizza una griglia regolare per suddividere l'immagine, potrebbe non essere in grado di individuare oggetti che si trovano ai margini dell'immagine stessa.

In generale comunque YOLO è un algoritmo molto popolare e ampiamente utilizzato nell'intelligenza artificiale per il riconoscimento degli oggetti grazie alla sua velocità ed efficienza nella gestione delle immagini complesse.