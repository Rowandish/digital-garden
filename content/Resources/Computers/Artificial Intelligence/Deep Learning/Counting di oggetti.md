Il counting di oggetti, ossia il conteggio automatico degli oggetti presenti in un'area o in un video, è una delle applicazioni principali della computer vision.
Due strumenti molto utilizzati per questo scopo sono l'algoritmo SORT (Simple Online and Realtime Tracking) e [[YOLO]] (You Only Look Once).
La YOLO è una [[Rete neurale convoluzionale]] per il rilevamento di oggetti in tempo reale mentre SORT è un algoritmo di tracciamento che utilizza le informazioni fornite da YOLO per tracciare gli oggetti nel tempo.
SORT è un algoritmo di tracciamento degli oggetti che associa le rilevazioni di oggetti tra i fotogrammi di un video.
È progettato per essere semplice e veloce, senza richiedere una pesante elaborazione computazionale.
SORT utilizza un filtro di Kalman per prevedere la posizione futura degli oggetti e l'algoritmo di associazione delle assegnazioni più vicine (Hungarian algorithm) per abbinare le rilevazioni agli oggetti tracciati.

## Implementazione
### 1. Rilevamento degli Oggetti con YOLO

Il primo passo è utilizzare YOLO per rilevare gli oggetti in un fotogramma. Supponiamo di avere un video di una strada trafficata e di voler contare le auto che passano. Ad ogni fotogramma, YOLO rileva tutte le auto presenti e restituisce i bounding box per ciascuna auto rilevata.
Esempio:
- Frame 1: YOLO rileva 3 auto con bounding box nelle coordinate [(30, 50, 200, 150), (400, 100, 550, 200), (600, 80, 750, 180)].

### 2. Inizializzazione del Tracciamento con SORT

SORT prende i bounding box forniti da YOLO e inizializza i tracciatori per ciascun oggetto rilevato. Utilizza un filtro di Kalman per ogni oggetto per prevedere la sua posizione nel prossimo fotogramma.
- Frame 1: SORT inizializza 3 tracciatori per le 3 auto rilevate.

### 3. Previsione della Posizione e Associazione delle Rilevazioni

Per ogni nuovo fotogramma, SORT prevede la posizione dei tracciatori utilizzando il filtro di Kalman.
Successivamente, YOLO rileva nuovamente gli oggetti e fornisce nuovi bounding box. SORT utilizza l'algoritmo di assegnazione ungherese per associare i nuovi bounding box alle previsioni dei tracciatori esistenti. Se una rilevazione non può essere associata a nessun tracciatore esistente, viene inizializzato un nuovo tracciatore.
Se un tracciatore non viene aggiornato per un certo numero di fotogrammi, viene eliminato.

Esempio:

- Frame 2: YOLO rileva 3 auto con bounding box nelle coordinate [(35, 55, 205, 155), (405, 105, 555, 205), (605, 85, 755, 185)].
- SORT prevede la posizione dei tracciatori e abbina i nuovi bounding box:
    - Tracciatore 1 (auto 1): Previsione (32, 52, 202, 152), abbinato a (35, 55, 205, 155).
    - Tracciatore 2 (auto 2): Previsione (402, 102, 552, 202), abbinato a (405, 105, 555, 205).
    - Tracciatore 3 (auto 3): Previsione (602, 82, 752, 182), abbinato a (605, 85, 755, 185).

#### 4. Counting degli Oggetti

Per contare gli oggetti, è possibile monitorare l'ingresso e l'uscita degli oggetti da una regione definita dell'area di interesse. Ad esempio, se vogliamo contare le auto che passano una linea specifica sulla strada, possiamo incrementare il conteggio ogni volta che un tracciatore attraversa quella linea.
