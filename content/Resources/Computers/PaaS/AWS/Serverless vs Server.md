Un'architettura **serverless** consente agli sviluppatori di concentrarsi sulla logica applicativa senza preoccuparsi della gestione dell'infrastruttura server.
E' quindi banalmente del codice che funziona sulla rete senza che lo sviluppatore abbia pensato all'infrastruttura server dove questo gira.
Un esempio è il processing di una chiamata API, o di un messaggio [[SQS]]/SNS, o il processing di un modifica ad un record in [[DynamoDB]] o, in generale, funzioni che vengono eseguite on-demand in risposta a eventi.
In un sistema serverless, il cloud provider gestisce automaticamente l'infrastruttura, inclusi provisioning, scaling e manutenzione dei server: l'unica cosa che conosce lo sviluppatore è l'entry point, tutto il resto è delegato e trasparente.
Gli sviluppatori scrivono .

Esempi di servizi serverless:

- [[Lambda|AWS Lambda]] (Amazon Web Services)
- **Azure Functions** (Microsoft Azure)
- **Google Cloud Functions** (Google Cloud)
- **IBM Cloud Functions**

Un'architettura serverless ha molto senso per l'esecuzione di task brevi ed eventi sporadici, mentre per applicazioni a lungo termine o complesse ha senso un'infrastruttura classica.

### Vantaggi e Svantaggi

|**Vantaggi di Serverless**|**Svantaggi di Serverless**|
|---|---|
|Scalabilità automatica|Cold start può aumentare latenza iniziale|
|Paghi solo per l'uso|Difficoltà a gestire processi complessi e persistenti|
|Minima gestione|Legato all'ecosistema del provider|
|Rapidità di sviluppo|Debugging e testing meno immediati|
|Alta disponibilità|Limitazioni di runtime e risorse per funzione|

|**Vantaggi di Server Classico**|**Svantaggi di Server Classico**|
|---|---|
|Controllo completo sull'ambiente|Costi fissi anche in caso di bassa attività|
|Pieno accesso hardware e software|Necessità di manutenzione continua|
|Adatto a task complessi e stateless|Scalabilità manuale|
|Ecosistema flessibile|Maggior tempo per setup e configurazione|

---

### Esempio

Un esempio comune è l'elaborazione di immagini caricate dagli utenti su un sito web. La funzione serverless può essere attivata dall'evento di caricamento di un'immagine su un bucket S3 (AWS).
1. Un'immagine viene caricata in un bucket S3.
2. AWS Lambda si attiva, ridimensiona l'immagine a 128x128 pixel e la salva in una cartella "resized" all'interno dello stesso bucket.
