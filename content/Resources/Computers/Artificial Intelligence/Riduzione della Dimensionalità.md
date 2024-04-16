---
tags:
  - MachineLearning
---
Un modo alternativo per ridurre la complessità del modello ed evitare il problema dell’[[overfitting]] è la riduzione della dimensionalità tramite la selezione delle caratteristiche, tecnica particolarmente utile per i modelli non [[Regolarizzazione|regolarizzati]].
Vi sono due categorie principali di tecniche per la riduzione della dimensionalità: selezione della caratteristica ed estrazione della caratteristica. 

## Selezione della caratteristica

Utilizzando la selezione della caratteristica, selezioniamo un sottoinsieme delle caratteristiche originarie.
Gli algoritmi sequenziali per la selezione delle caratteristiche sono una famiglia di algoritmi di ricerca greedy, utilizzati per ridurre uno spazio di caratteristiche *d-dimensionale* in un sottospazio di caratteristiche *k-dimensionale* dove $k < d$.
La motivazione su cui si basano gli algoritmi per la selezione delle caratteristiche consiste nel ==selezionare automaticamente un sottoinsieme delle caratteristiche che sia particolarmente rilevante per il problema==, in modo da migliorare l’efficienza computazionale o ridurre l’errore di generalizzazione del modello, rimuovendo le caratteristiche irrilevanti o il rumore, il che può essere utile per gli algoritmi che non supportano la regolarizzazione.
### Sequential Backward Selection (SBS)

Un classico algoritmo sequenziale di selezione delle caratteristiche è la selezione sequenziale all’indietro o Sequential Backward Selection (SBS), che mira a ridurre la dimensionalità del sottospazio di caratteristiche iniziale con un minimo decadimento in termini prestazionali del classificatore, in modo da migliorare l’efficienza computazionale.
L’idea su cui si basa l’algoritmo SBS è piuttosto semplice: ==SBS rimuove sequenzialmente l’intero insieme delle caratteristiche finché il nuovo sottospazio delle caratteristiche contiene solo il numero desiderato di caratteristiche==.
Per determinare quale caratteristiche devono essere rimosse in ogni fase, ==dobbiamo definire la funzione criterio che vogliamo minimizzare==.
Il criterio calcolato dalla funzione può essere semplicemente la differenza prestazionale del classificatore prima e dopo la rimozione di una determinata caratteristica. Poi la caratteristica da eliminare in ciascuna fase può semplicemente essere definita come la caratteristica che massimizza questo criterio; in termini più intuitivi, a ogni fase eliminiamo la caratteristica che provoca il minore degrado prestazionale dopo la rimozione.

### Random Forest
Un altro approccio utile per selezionare le caratteristiche rilevanti da un dataset consiste nell’utilizzare una [[Random Forests]]: possiamo misurare l’importanza delle caratteristiche come la riduzione media delle impurità, calcolata da tutti gli alberi decisionali della foresta senza effettuare alcuna supposizione sul fatto che i dati siano separabili linearmente oppure no.

## Estrazione della caratteristica

Nell’estrazione della caratteristica deriviamo le informazioni dall’insieme di caratteristiche, per costruire un nuovo sottospazio di caratteristiche di dimensionalità inferiore rispetto a quello originale.
Mentre con gli algoritmi di selezione delle caratteristiche, come nel caso della selezione sequenziale all’indietro (SBS) abbiamo mantenuto le caratteristiche originali, utilizziamo l’estrazione delle caratteristiche per trasformare o proiettare i dati in un nuovo spazio di caratteristiche. Nel contesto della riduzione della dimensionalità, l’estrazione delle caratteristiche può essere considerata come un approccio a compressione dei dati, con l’obiettivo di conservare la maggior parte delle informazioni rilevanti. L’estrazione delle caratteristiche viene tipicamente utilizzata per migliorare l’efficienza computazionale, ma può anche proteggere contro la maledizione della dimensionalità, specialmente quando si opera su modelli non regolarizzati.

Ci sono tre algoritmi principali che andremo ad analizzare nel dettaglio:
* **PCA**: abbiamo proiettato i dati su un sottospazio di minori dimensioni, in modo da massimizzare la varianza fra gli assi ortogonali delle caratteristiche, ignorando le etichette delle classi.
* **LDA**: al contrario di PCA, è una tecnica per la riduzione della dimensionalità con supervisione, ovvero considerando le informazioni sulla classe già presenti nel dataset di addestramento, per tentare di massimizzare la separabilità in classi in uno spazio di caratteristiche lineari.
* **Kernel PCA**: consente di mappare dataset non lineari su uno spazio delle caratteristiche dotato di dimensionalità inferiore, dove le classi possono risultare separabili in modo lineare. 

### Principal Component Analysis (PCA) 

La PCA prende un insieme di dati complessi e li trasforma in un nuovo set di dati più semplice, preservando al tempo stesso la maggior parte delle informazioni originali.

Immagina di avere un insieme di dati che rappresentano diverse variabili o caratteristiche, come altezza, peso, età e reddito di un gruppo di persone. Ogni persona nel dataset può essere rappresentata come un vettore di dati, dove ogni componente del vettore rappresenta una caratteristica. In questo esempio, avremmo un vettore per ogni persona contenente i valori per altezza, peso, età e reddito.

==La PCA cerca di semplificare questo insieme di dati trovando nuove direzioni, chiamate componenti principali, lungo le quali i dati variano di più==. In altre parole, cerca di capire quali combinazioni delle caratteristiche originali spiegano meglio la variazione nei dati.

==Per fare ciò, la PCA inizia calcolando la matrice di covarianza dei dati, che misura la relazione tra le diverse caratteristiche. Questa matrice ci dice quanto due caratteristiche variano insieme==. Ad esempio, se l'altezza e il peso delle persone tendono a variare insieme (ad esempio, persone più alte tendono ad avere un peso maggiore), allora la covarianza tra altezza e peso sarà alta.

Successivamente, ==la PCA utilizza i concetti di autovettori e autovalori per trovare le componenti principali della matrice di covarianza==. Gli autovettori sono direzioni nei dati lungo le quali la varianza è massima, mentre gli autovalori rappresentano la quantità di varianza spiegata da ciascun autovettore. La PCA ordina gli autovettori in base agli autovalori, in modo che il primo autovettore spieghi la massima varianza, il secondo spieghi la seconda massima varianza e così via.

Una volta calcolate le componenti principali, possiamo proiettare i nostri dati su queste nuove direzioni. Questo significa che ==trasformiamo i dati originali in un nuovo set di dati dove le variabili sono linearmente indipendenti e ordinate per importanza in termini di varianza spiegata==.

Per esempio, se avevamo originariamente un insieme di dati con quattro variabili (altezza, peso, età e reddito) e calcoliamo la PCA, potremmo scoprire che le prime due componenti principali spiegano la maggior parte della variazione nei dati. Potremmo quindi proiettare i nostri dati su queste prime due componenti principali per ottenere un nuovo set di dati più semplice, composto solo da due variabili, che conservano ancora la maggior parte delle informazioni originali.

E' importante scegliere il numero corretto di componenti principali da mantenere, poiché mantenere troppe componenti potrebbe non semplificare significativamente i dati, mentre mantenere troppe poche componenti potrebbe perdere informazioni importanti.
Inoltre, ==la PCA presuppone che i dati siano lineari e che le relazioni tra le variabili siano gaussiane, quindi potrebbe non essere adatta a tutti i tipi di dati==.

### Analisi dei Componenti Lineari Discriminanti (LDA)

L'Analisi dei Componenti Lineari Discriminanti (LDA) è una tecnica di riduzione della dimensionalità molto simile alla PCA, ma con l'obiettivo specifico di ==massimizzare la separazione tra classi nei dati==. In parole semplici, mentre la PCA cerca di trovare le direzioni nei dati lungo le quali variano di più, la LDA cerca di trovare le direzioni che massimizzano la differenza tra le classi.
LDA è un algoritmo senza supervisione, mentre PCA prevede la supervisione.

Immagina di avere un insieme di dati che rappresentano diverse caratteristiche (come altezza, peso, età) di oggetti appartenenti a diverse classi (come specie di fiori, tipi di frutta, ecc.). ==L'obiettivo della LDA è trovare le combinazioni di caratteristiche che meglio distinguono le diverse classi, rendendo i dati più separabili==.

Per fare ciò, la LDA calcola le medie delle caratteristiche per ciascuna classe e la dispersione delle caratteristiche all'interno di ciascuna classe. Successivamente, cerca di trovare la combinazione lineare delle caratteristiche che massimizza il rapporto tra la dispersione tra classi e la dispersione all'interno delle classi.

In termini più semplici, la LDA cerca di proiettare i dati in modo che le classi siano il più separabili possibile lungo le nuove dimensioni. Questo significa che le classi saranno più distinte e facilmente distinguibili nelle nuove dimensioni rispetto alle dimensioni originali.

Ad esempio, immagina di avere un insieme di dati con due classi, "gatti" e "cani", e le caratteristiche sono altezza e peso. La LDA cercherà di trovare la combinazione lineare di altezza e peso che massimizza la separazione tra gatti e cani, quindi i gatti saranno separati il più possibile dai cani nelle nuove dimensioni.

Attenzione che LDA è sensibile agli outlier e potrebbe non funzionare bene se le classi sono molto sovrapposte.

### Kernel PCA

L'analisi delle componenti principali con kernel (Kernel PCA) è una tecnica di riduzione della dimensionalità che si basa sulla PCA tradizionale, ma ==utilizzando una funzione kernel per proiettare i dati in uno spazio di dimensioni superiori prima di eseguire la PCA==. Questo consente di ==trovare strutture non lineari nei dati che non sarebbero state catturate dalla PCA lineare standard==.

Immagina di avere un insieme di dati che non può essere separato linearmente nello spazio delle caratteristiche originale, ad esempio i dati potrebbero essere distribuiti in modo non lineare come un cerchio o una spirale. In questo caso, la PCA standard potrebbe non essere efficace nel catturare la struttura dei dati. La Kernel PCA risolve questo problema proiettando i dati in uno spazio di dimensioni superiori, dove è più probabile che siano separabili linearmente, e quindi eseguendo la PCA in questo nuovo spazio di dimensioni superiori.

La funzione kernel è una funzione che calcola la somiglianza tra coppie di punti nei dati originali. Questa somiglianza può essere misurata in vari modi, ad esempio utilizzando il prodotto scalare o una funzione di base radiale (RBF). Il kernel specifica come i dati originali saranno trasformati nello spazio delle caratteristiche di dimensioni superiori.

Una volta trasformati i dati nello spazio delle caratteristiche di dimensioni superiori, la PCA standard può essere applicata per ridurre la dimensionalità dei dati e trovare le direzioni principali della varianza. Questo consente di mantenere solo le caratteristiche più rilevanti nei nuovi spazi di dimensioni superiori.

Kernel PCA è utile per catturare strutture non lineari nei dati che non possono essere gestite dalla PCA lineare standard e i dati nel mondo reale sono spesso non lineari.