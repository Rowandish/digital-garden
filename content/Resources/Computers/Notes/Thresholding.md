## Thresholding

#DigitalImageProcessing #PublishedPosts

### 1. Introduzione
_Thresholding_ è il metodo di segmentazione di un'immagine più semplice per distinguere i pixel in *background* dai pixel in *foreground* di un'immagine in base alla loro intensità.
Nell'implementazione più semplice, l'algoritmo prende in ingresso un'immagine binaria o in scala di grigi e produce in uscita un'immagine binaria i cui pixel neri rappresentano i pixel in _background_ mentre i pixel bianchi i pixel in _foreground_.
Per distinguere l'insieme in cui inserire un pixel esiste un unico parametro chiamato _intensità di soglia_ (o _intensity threshold_ in inglese): se l'intensità di un pixel ha valore minore della soglia viene indicato come bianco (per esempio), altrimenti come nero.
In implementazini più complesse posso anche indicare più valori di soglia oppure, per immagini colorate, impostare un valore di soglia per ogni componente di colore.

### 2. Applicazioni
Non tutte le immagini possono essere segmentate in questo modo, per poter capire la struttura di un'immagine e se questa può essere correttamente segmentata tramite _tresholding_ è necessario analizzare il suo _intensity histogram_ (grafo che mostra sull'asse delle ordinate le intensità possibili che ogni pixel può assumere, comunemente da 0 a 255, e sull'asse delle y il numero di occorrenze che un pixel con tale intensità si trova nell'immagine).
E' possibile separare i pixel in primo piano dai pixel in _background_ se l'intensità dei pixel in primo piano è notevolmente differente da quella dei pixel in _background_; in questo caso ci aspettiamo di vedere un picco nell'istogramma dell'immagine che corrisponde ai pixel dell'oggetto in _foreground_ che vogliamo evidenziare.
Se tale picco non esiste, con ottima probabilità questo tipo di segmentazione non produrrà risultati apprezzabili. In questo caso è consigliabile usare un algoritmo di _adaptive thresholding_, che verrà spiegato successivamente in questo articolo.

Prendiamo il seguente esempio

![[thrshist.gif]]

Nel primo caso abbiamo il caso più semplice in cui un singolo valore di soglia _T1_ permette di distinguere i pixel in primo piano dai pixel in _background_. Nel secondo caso abbiamo invece nu esempio più complesso in quanto i pixel centrali rappresentano l'oggetto che voglio rilevare e conseguentemente la soglia deve essere di due valori: _T1_ e _T2_.
Nel terzo caso invece è molto probabile che non si riesca ad ottenere una segmentazione corretta.

### 3. Adaptive Thresholding
Nel algoritmo tradizionale di _thresholding_ il valore id soglia è impostato all'inizio e rimane costante per tutta la durata dell'algoritmo.
Il metodo di _adaptive thresholding_ invece cambia il valore della soglia dinamicamente in base all'immagine in ingresso, per esempio per avere risultati migliori in immagini in cui cambia la condizione di luminosità dell'oggetto dovuto a illuminazioni laterali che portano a gradienti d'ombra.
Questo metodo seleziona un valore di soglia diverso per ogni pixel in base al range di valori che assumono i pixel nel suo vicinato. Questo permette il _thresholding_ in immagini che non hanno un picco distintivo nell'istogramma.
Per esempio, consideriamo la seguente immagine:

![[son1.gif]]

Dato che l'immagine contiene un notevole gradiente d'ombra, il metodo di _thresholding_ classico non funziona correttamente, come dimostra il risultato indicato sotto

![[son1thr1.gif]]

Usando un metodo di _Adaptive Thresholding_ utilizzando come algoritmo interno la _media_ e un vicinato 7x7 ottengo:

![[son1adp1.gif]]

che ottiene buoni risultati per il testo, ma non per il background.
La situazione può essere migliorata utilizzando, al posto della media, il _mean-C_, dove _C_ è una costante, in questo caso tutti i pixel che hanno vicinato uniforme, vengono settati a _background_, per esempio usando un vicinato 7x7 e la costante _C=7_ ottengo:

![[son1adp2.gif]]

Che è sicuramente un buon risultato.
