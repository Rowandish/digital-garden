---
tags:
  - DigitalImageProcessing
  - PublishedPosts
---
## 1.Normalizzazione
### 1.1 Introduzione
La normalizzazione è una semplice tecnica di miglioramento di un'immagine che cerca di migliorarne il contrasto eseguendo una **"stiratura" dei valori dei pixel in modo che siano distribuiti su un range noto**, come per esempio, tutto il range dei valori assumibili dai pixel: 0-255.
E' un metodo meno sofisticato e più grezzo rispetto all'equalizzazione.

### 1.2 Funzionamento
Per prima cosa è necessario scegliere il valore minimo e massimo che vogliamo dare ai pixel dell'immagine (tipicamente 0 e 255). Questi valori li chiamiamo _a_ e _b_.
Il metodo più semplice di normalizzazione per prima cosa trova il più basso valore di pixel nell'immagine (_c_) e il più alto (_d_).
Successivamente ogni pixel è scalato secondo la seguente funzione

![[eqnstr1.gif]]

Considerando il fatto che i valori minori di 0 vengono settati a 0 e analogamente i valori maggiori di 255 vengono settati a tale valore.
Il problema di questo metodo è che un pixel con valore molto alto o molto basso viene notevolmente influenzato dai valori di _c_ o _d_ portando ad un output non rappresentativo.
Esiste quindi una modalità più robusta che prima prende in ingresso l'istogramma dell'immagine e poi sceglie _c_ e _d_, per esempio, al quinto e novantacinquesimo percentile dell'istogramma (il 5% dei pixel dell'istogramma avranno valore minore di _c_, e il 5% maggiore di _d_). Questo approccio migliora notevolmente il risultato.

### 1.3 Applicazioni
La normalizzazione è comunemente usata per **migliorare il contrasto in un'immagine senza distorcere troppo i valori di intensità dei pixel**.
Per esempio, consideriamo la seguente immagine

![[wom1.gif]]

Dato che l'istogramma ha un picco tra i valori 79 e 136:

![[wom1hst1.gif]]

La normalizzazione ottiene ottimi risultati usando _c = 79_ e _d = 136_

![[wom1str1.gif]]

Per rendere meno piatta l'immagine, possono usare un'equalizzazione che migliora notevolmente il contrasto, ma porta ad un risultato artefatto:

![[wom1heq1.gif]]

Un comune uso della normalizzazione vi è nella **conversione tra tipi di immagini diversi**: per esempio, se voglio convertire un'immagine i cui valori dei pixel solo float (in cui i valori dei pixel possono andare, per esempio, da 0 a 5000) ad un'immagine integer 8-bit, possono eseguire una normalizzazione con _c = 0_ e _d = 255_.
Ovviamente in questo processo va persa dell'informazione, ma le relative intensità dei pixel verranno preservate.

## 2. Equalizzazione

### 2.1 Introduzione
I metodi di equalizzazione di un'immagine modificano il contrasto della stessa in modo che **l'istogramma dell'immagine assuma una forma desiderata**.
A differenza della normalizzazione, l'equalizzazione può usare funzioni **non lineari** o **non monotone** per assegnare i valori di intensità ai pixel in modo che l'immagine di output contenga una distribuzione di intensità uniforme (per esempio un'istogramma piatto).

### 2.2 Applicazioni
Per illustrare il funzionamento dell'equalizzazione consideriamo la seguente immagine

![[moo2.gif]]

che è un'immagine 8 bit in scala di grigi della superfice della luna.
L'immagine ha range dinamico molto basso (significa che la maggior parte dei pixel è concentrata in pochi valori di intensità).
Per migliorarne il contrasto senza introdurre artefatti o modificare l'informazione in essa contenuta, possiamo applicare un algoritmo di equalizzazione, che permette di ottenere la seguente immagine

![[moo2heq1.gif]]

Andiamo a vedere il seguente esempio (da wikipedia); la segeunte è l'immagine in ingresso non equalizzata:

![[Unequalized_Hawkes_Bay_NZ.jpg]]

Che ha il seguente istogramma (in rosso) e funzione cumulativa (in nero)

![[620px-Unequalized_Histogram.svg.png]]

Dopo il processo di equalizzazione ottengo la seguente immagine

![[Equalized_Hawkes_Bay_NZ.jpg]]

In cui l'istogramma è stato modificato in modo che la cumulata cresca in maniera costante

![[Equalized_Histogram.svg.png]]
