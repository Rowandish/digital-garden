---
tags:
  - Dometrain
---
Questa nota prende a piene mani dal corso [# From Zero to Hero: Event-Driven Architecture](https://dometrain.com/course/from-zero-to-hero-event-driven-architecture/).

## Introduzione
L'approccio classico di struttura di un'architettura a servizi è avere vari servizi che comunicano tra di loro in modo sincrono, esempio tramite API call.
Questo però porta a varie problematiche:
* Accoppiamento tra i servizi: sia temporale che di location (il servizio A deve sapere dove si trova e come chiamare il servizio B)
* Se il servizio chiamato non funziona rischia di compromettere il servizio chiamante
* Se devo aggiungere un nuovo servizio devo modificare anche il chiamante per fare in modo che il nuovo venga chiamato, portando ad alto accoppiamento.
La stessa idea la posso avere anche nelle strutture monolitiche: quando ho una chiamata ad un metodo ho un accoppiamento forte e il chiamante aspetta che il metodo sia finito prima di procedere.
L'idea è invertire le dipendenze in modo che sia il nuovo servizio che voglio aggiungere che vada a prendere un evento pubblicato dal servizio già esistente, quindi è il nuovo servizio che dipende dal vecchio e non viceversa.
Il servizio principale pubblicherà eventi da qualche parte e poi saranno i vari consumatori a prenderli in modo disaccoppiato e asincrono.
EDA è un pattern che riguarda la comunicazione tra entità, che siano servizi di un'architettura a microservizi o che siano classi di un sistema monolitico.
Il limite di questa architettura che aggiunge complessità e rende più difficoltoso il debugging: mentre con una relazione classica ho una richiesta a cui segue una risposta o un eventuale errore e quindi è facile seguire il flusso delle comunicazioni, nell'EDA è tutto asincrono e disaccoppiato e conseguentemente è molto più difficile seguire il flusso della richiesta e scoprire eventuali problemi.
Ha quindi molto senso utilizzare questa architettura per sistemi grossi e complessi.

### Building blocks
Un EDA è tipicamente composto da dei servizi che comunicano tra di loro tramite eventi che vengono inseriti in un **message channel**: questo può essere di due tipologie
* **Point-to-point**: un messaggio ha un solo destinatario e viene inserito in una coda (es. [[SQS]], RabbitMQ); è utile per task distribuiti tra consumatori indipendenti. Tipicamente l'ordine non viene garantito (esiste la FIFO in SQS ma è più lenta).
	* Durable: i dati rimangono nella coda fino a che non vengono consumati
* **Pub/Sub (Publish/Subscribe)**: un messaggio viene pubblicato su un bus e può essere ricevuto da più sistemi sottoscritti a cui interessa tale messaggio. Esempio [[SNS]].
	* Non durable: Gli eventi nel bus non vengono memorizzati per sempre ma una volta inviati vengono cancellati.
	* **Stream**: versione durable del bus, più costosa in quanto occupa più spazio su disco

Quello che tipicamente avviene è avere un message bus non durable dove vengono pubblicati gli eventi e poi ogni servizio ha la sua coda dedicata dove vengono inseriti tali eventi. In questo modo se il servizio fa offline non perdo l'evento in quanto rimane sempre nella coda.

## Eventi
Gli eventi sono degli oggetti che indicano che è successo qualcosa di significativo, sono immutabili, successi nel passato e non possono essere modificati successivamente.
Il servizio che produce gli eventi non è consapevole di chi li consuma.

> [!info]
> EDM è fondamentalmente un pattern di comunicazione, un modo di modellare l'integrazione tra sistemi diversi utilizzando business events che portano al trigger di funzionalità di businness.

### Tipologie

#### Notification Event (Thin Event)
Semplice e piccolo pacchetto di dati che indica che qualcosa è accaduto sul sistema.
```csharp
public record OrderConfirmedEvent {
    public string OrderId { get; set; }
}
```
Chi riceve questo evento dovrà probabilmente effettuare una **richiesta separata** (es. a un database) per ottenere le informazioni complete sull’ordine.
* **Vantaggio:** più leggero, meno dati in transito, più disaccoppiato
* **Svantaggio:** meno autonomo, richiede ulteriori passaggi per essere utile.
#### Event Carried State Transfer (Thick Event)
Evento **autosufficiente** che contiene tutte le informazioni: può essere utilizzato da altri servizi senza ulteriori chiamate.
```csharp
public record OrderConfirmedEvent {
    public string OrderId { get; set; }
    public string OrderNumber { get; set; }
    public decimal OrderValue { get; set; }
    public DeliveryAddress DeliveryAddress { get; set; }
	    public List<OrderItems> Items { get; set; }
}
```
* **Vantaggio:** ricco di informazioni, utile subito.
* **Svantaggio:** più grande da trasportare e aumenta l'accoppiamento tra i servizi

## Producer

### Responsabilità

In un sistema EDA il producer ha la sola responsabilità di produrre eventi che abbiano **sempre lo stesso schema**, che abbiano tutte le informazioni necessarie e nel modo più veloce possibile.
Per esempio se devo inviare una mail il producer non dovrà pensare allo storage dell'API KEY del servizio delle mail, al fatto che potrebbe essere down e così via; l'unica cosa di cui è responsabile è la creazione dell'evento.

### Outbox Pattern

Quando un servizio deve aggiornare il proprio stato su un database e contemporaneamente pubblicare un evento, si rischia un'inconsistenza. Se una delle due operazioni fallisce (es. il database è ok, ma il message broker non è raggiungibile), il sistema si trova in uno stato incoerente.

Il pattern Outbox risolve questo problema garantendo che l'aggiornamento del database e la pubblicazione dell'evento avvengano in modo atomico.

#### Come funziona

1.  **Transazione Unica:** L'operazione di business (es. creare un ordine) e la creazione dell'evento vengono eseguite all'interno della stessa transazione di database. L'evento non viene pubblicato subito, ma viene salvato in una tabella dedicata ("outbox") nello stesso database del servizio.
2.  **Commit Atomico:** Poiché l'operazione e il salvataggio dell'evento sono nella stessa transazione, o entrambe hanno successo o entrambe falliscono. Questo garantisce che non si perda mai un evento se l'operazione di business ha successo.
3.  **Processo Asincrono:** Un processo separato (un "message relayer" o "poller") monitora la tabella outbox. Quando rileva nuovi eventi, li pubblica sul message broker.
4.  **Gestione degli Errori:** Una volta che l'evento è stato pubblicato con successo, viene contrassegnato come "inviato" o eliminato dalla tabella outbox per evitare doppie pubblicazioni.

#### Quando Eliminare i Dati dalla Tabella Outbox

È sconsigliato eliminare un record dalla tabella outbox subito dopo la pubblicazione. Una strategia più robusta prevede due fasi:

1.  **Marcare come "Pubblicato":** Invece di eliminare, il record viene aggiornato con uno stato (es. `published = true`) o un timestamp di pubblicazione. Questo conferma che il message relayer ha fatto il suo lavoro.
2.  **Pulizia Periodica:** Un processo di pulizia separato (es. un batch job che gira di notte) elimina i record dalla tabella outbox che sono stati pubblicati da un certo periodo (es. più di 7 giorni).

Questo approccio offre una "finestra di sicurezza" che permette di revisionare gli eventi inviati, fare debugging o ri-pubblicare manualmente un evento in caso di problemi critici, senza perdere la traccia dell'evento originale.

### Schema Design ed Event Structure

Quando si progetta un'architettura guidata dagli eventi, la struttura degli eventi stessi (lo **schema**) è di fondamentale importanza.
Per risolvere questo problema, è nata la specifica **CloudEvents**, un progetto della Cloud Native Computing Foundation (CNCF) che fornisce un formato comune per descrivere i dati degli eventi. L'obiettivo è semplificare l'interoperabilità tra servizi, piattaforme e sistemi diversi.
La specifica [CloudEvents](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md) definisce un insieme di metadati (attributi) che costituiscono l'involucro ("envelope") di un evento. Questi metadati forniscono informazioni contestuali sull'evento, indipendentemente dal suo payload (i dati specifici dell'evento).
#### Struttura di un CloudEvent

Un CloudEvent è composto da:

*   **Attributi di Contesto (Context Attributes):** Metadati che descrivono l'evento.
*   **Dati dell'Evento (Event Data):** Il payload vero e proprio, che contiene le informazioni specifiche del dominio (es. i dettagli di un ordine).

Gli attributi di contesto obbligatori includono:

*   `id`: Un identificatore univoco per l'evento.
*   `source`: Il contesto in cui l'evento ha avuto origine (es. un URI del servizio).
*   `specversion`: La versione della specifica CloudEvents utilizzata (es. "1.0").
*   `type`: Una stringa che descrive il tipo di evento (es. "com.example.order.created").

Attributi opzionali ma comuni sono:

*   `datacontenttype`: Il tipo di contenuto del payload `data` (es. "application/json").
*   `dataschema`: Un URI che punta allo schema a cui il payload `data` aderisce.
*   `subject`: Descrive l'oggetto dell'evento a scopo di filtraggio.
*   `time`: Il timestamp di quando si è verificato l'evento.

Per l'ecosistema .NET, il pacchetto NuGet di riferimento per lavorare con queste specifiche è `CloudNative.CloudEvents`.

## Consumer

Il consumer è il componente che riceve e processa gli eventi. Le sue responsabilità sono cruciali per la stabilità e l'affidabilità dell'intero sistema.

### Responsabilità

#### Ingestion Rate

Il consumer deve essere progettato per gestire il volume di messaggi che si aspetta di ricevere. Se i producer inviano eventi a un ritmo superiore a quello che il consumer può sostenere, la coda di messaggi inizierà a crescere, introducendo latenza. È fondamentale monitorare la lunghezza della coda e implementare strategie di scaling (es. aumentare il numero di istanze del consumer) per far fronte ai picchi di carico.

#### Sovraccarico di Messaggi (Backpressure)

Cosa succede se i producer pubblicano costantemente più messaggi di quanti i consumer possano elaborare? Questo porta a un accumulo indefinito nella coda. Per gestire questa situazione, si possono adottare diverse strategie:
*   **Scaling Automatico:** La soluzione più comune è scalare orizzontalmente il numero di consumer in base a metriche come la lunghezza della coda o il tempo di elaborazione.
*   **Limitare la Coda:** Alcuni message broker permettono di impostare limiti sulla dimensione della coda o sulla durata di vita dei messaggi, scartando i più vecchi per far spazio ai nuovi.
*   **Backpressure:** In alcuni sistemi (specialmente nello streaming), il consumer può segnalare al broker o al producer di rallentare l'invio di messaggi.

#### Gestione degli Errori e Dead Letter Queue (DLQ)

Un consumer deve essere resiliente agli errori. Se un messaggio non può essere processato (a causa di un bug, un servizio esterno non disponibile, o dati corrotti), non dovrebbe bloccare l'elaborazione degli altri messaggi. La strategia standard prevede:
1.  **Tentativi (Retries):** Il consumer tenta di ri-processare il messaggio per un numero configurato di volte, magari con un intervallo di attesa crescente (exponential backoff).
2.  **Dead Letter Queue (DLQ):** Se tutti i tentativi falliscono, il messaggio viene spostato in una coda speciale chiamata "Dead Letter Queue". Questo previene il blocco della coda principale (fenomeno noto come "poison pill").
3.  **Analisi e Intervento:** Gli sviluppatori possono monitorare la DLQ per analizzare i messaggi falliti, correggere la causa dell'errore e, se necessario, re-inserirli nella coda principale per una nuova elaborazione.

#### Gestione dei Duplicati (Idempotenza)

Molti message broker garantiscono una consegna "at-least-once" (almeno una volta), il che significa che, in rare circostanze (es. a seguito di un errore di rete o di un riavvio del consumer), lo stesso messaggio potrebbe essere consegnato più di una volta.
Il consumer deve essere **idempotente**, ovvero l'elaborazione multipla dello stesso messaggio deve produrre lo stesso risultato della singola elaborazione.

Le tecniche comuni per garantire l'idempotenza includono:
*   **Tracciamento degli ID degli Eventi:** Il consumer salva l'ID di ogni evento processato (l'attributo `id` di CloudEvents è perfetto per questo) in un datastore (es. un database o una cache).
*   **Controllo Preventivo:** Prima di elaborare un nuovo messaggio, il consumer controlla se il suo ID è già presente nel datastore. Se lo è, il messaggio viene ignorato.

## Orchestrazione vs Coreografia

Finora abbiamo descritto un approccio chiamato **Coreografia**. In questo modello, ogni servizio reagisce agli eventi emessi da altri servizi in modo autonomo, senza una guida centrale. Come in una coreografia di danza, ogni ballerino sa cosa fare quando la musica cambia, senza che un direttore d'orchestra glielo dica.
*   **Vantaggi:** Massima autonomia e disaccoppiamento dei servizi.
*   **Svantaggi:** La logica di business complessiva è distribuita e più difficile da visualizzare e monitorare. Gestire processi complessi con più passaggi e possibili errori (e relativi rollback) può diventare molto complicato.

Quando i flussi di lavoro diventano complessi, emerge un altro pattern: l'**Orchestrazione**.

### Orchestrator (Workflow)
Nel pattern dell'orchestrazione, esiste un componente centrale, l'**Orchestrator**, che agisce come un direttore d'orchestra. Questo servizio è responsabile della gestione di un workflow di business specifico, dicendo agli altri servizi cosa fare e quando.
L'orchestrator non esegue la logica di business dei singoli servizi (come l'elaborazione di un pagamento o la preparazione di una pizza), ma si limita a coordinare il flusso, invocando i servizi giusti al momento giusto, spesso tramite comandi o eventi.

#### Gestione del Workflow e Rollback
Il vantaggio principale di un orchestrator è la **centralizzazione della logica del workflow**. Questo rende molto più semplice:
*   **Monitorare lo stato** di un processo di business (es. "a che punto è l'ordine X?").
*   **Gestire errori complessi** e implementare logiche di rollback o compensazione.
Se un passaggio del workflow fallisce, l'orchestrator può eseguire una serie di azioni correttive per annullare le operazioni già completate. Questa operazione è nota come **Saga Pattern**, dove l'orchestrator si assicura che una transazione distribuita venga completata con successo o annullata completamente.

#### Esempio: Ordine di una Pizza

Immaginiamo il workflow per l'ordine di una pizza a domicilio:

1.  **Richiesta dell'Utente:** L'utente invia una richiesta di ordine tramite l'app.
2.  **Invio all'Orchestrator:** La richiesta non viene pubblicata su un bus generico, ma inviata direttamente a un `OrderWorkflowOrchestrator`.
3.  **Inizio del Workflow:** L'orchestrator riceve l'ordine e avvia il workflow, mantenendo internamente lo stato (es. `STATO = IN_CORSO`).
    *   **Passo 1: Pagamento:** Invia un comando `ProcessaPagamento` al servizio di Pagamento.
    *   **Passo 2: Cucina:** Se il pagamento ha successo, invia un comando `PreparaOrdine` al servizio Cucina.
    *   **Passo 3: Consegna:** Una volta che la cucina conferma che l'ordine è pronto, invia un comando `InviaFattorino` al servizio di Logistica.
4.  **Fine del Workflow:** Se tutti i passaggi hanno successo, l'orchestrator imposta lo stato finale a `COMPLETATO`.

**Come gestisce gli errori e le cancellazioni?**

*   **Pagamento Fallito:** Se il servizio di Pagamento risponde con un errore, l'orchestrator lo intercetta. Poiché nessun'altra operazione è stata ancora eseguita, semplicemente imposta lo stato dell'ordine su `FALLITO` e notifica l'utente.
*   **Cancellazione da parte dell'Utente:** L'utente vuole annullare l'ordine. La richiesta di cancellazione viene inviata all'orchestrator.
    *   L'orchestrator controlla lo stato attuale del workflow.
    *   Se l'ordine è ancora in fase di pagamento o non è ancora stato inviato alla cucina, può annullarlo facilmente.
    *   Se l'ordine è già stato inviato alla cucina, l'orchestrator sa che deve eseguire un'azione di compensazione: invia un comando `AnnullaPreparazione` al servizio Cucina e, se il pagamento è già avvenuto, un comando `EmettiRimborso` al servizio Pagamento.

L'orchestrator centralizza la logica, rendendo il processo più trasparente e più facile da gestire, specialmente in caso di fallimenti o richieste di annullamento che richiedono azioni multiple e coordinate.

Esistono diversi framework open-source che implementano questo pattern e forniscono interfacce web per visualizzare e gestire i workflow, come [Temporal](https://temporal.io/) o [Netflix Conductor](https://conductor.netflix.com/).

### Quando usare l'uno o l'altro?

Una regola pratica per decidere quale approccio adottare è la seguente:

*   **Coreografia tra domini di business diversi**: Quando i servizi appartengono a contesti di business separati e devono solo reagire a eventi di alto livello, la coreografia è ideale. Mantiene i domini disaccoppiati e indipendenti.
*   **Orchestrazione all'interno di un singolo dominio di business**: Quando un processo complesso richiede il coordinamento di più servizi *all'interno dello stesso dominio*, un orchestrator centralizza la logica e migliora la visibilità e la gestione degli errori.

In sintesi:
-   La comunicazione tra servizi di domini diversi dovrebbe rimanere asincrona e basata sulla coreografia.
-   All'interno di un dominio, un orchestrator diventa utile per gestire workflow complessi.

Tuttavia, l'introduzione di un orchestrator aggiunge complessità. È consigliabile adottarlo solo quando il processo di business presenta:
-   Molteplici rami decisionali (es. `if/else`).
-   Numerosi casi eccezionali (edge case) da gestire.
-   Logiche di compensazione (rollback) non banali.

Fino a quando la complessità non raggiunge questo livello, è preferibile mantenere il sistema più semplice possibile, favorendo la coreografia.

## Observability

L'osservabilità è la capacità di porre domande a un sistema dall'esterno, anche domande che non si sapeva di dover formulare in anticipo. In un'architettura a eventi, dove la complessità accidentale può facilmente aumentare, l'osservabilità è cruciale.

### Complessità Essenziale vs Complessità Accidentale

Nel progettare sistemi software, è utile distinguere tra due tipi di complessità:

*   **Essential Complexity**: È la complessità intrinseca del problema di business che si sta cercando di risolvere. Queste sono le regole e i processi che non possono essere eliminati, indipendentemente da quanto sia buono il design del software (es. le regole per il calcolo delle tasse, la logica di un workflow di approvazione).
*   **Accidental Complexity**: È la complessità introdotta dagli strumenti, dalle tecnologie e dalle decisioni architetturali che scegliamo. È la complessità che creiamo noi ingegneri. Un'architettura a eventi, sebbene potente, può introdurre una notevole complessità accidentale (es. difficoltà nel tracciare il flusso di un'operazione, gestione degli errori in sistemi distribuiti, deployment complessi).

L'obiettivo di una buona architettura è minimizzare la complessità accidentale, per potersi concentrare sulla gestione della complessità essenziale. Strumenti di osservabilità adeguati sono fondamentali per tenere sotto controllo e mitigare la complessità accidentale introdotta da un'architettura distribuita come la EDA.

I tre pilastri dell'osservabilità sono:
*   **Logs**: Record dettagliati di eventi specifici che si verificano nel tempo.
*   **Metrics**: Dati numerici aggregati che rappresentano lo stato e le prestazioni del sistema (es. latenza, numero di errori).
*   **Traces**: Rappresentano il flusso di una singola richiesta attraverso i vari servizi del sistema.

### Distributed Tracing

Nei sistemi disaccoppiati di una EDA, la relazione causa-effetto non è sempre chiara. Il **Distributed Tracing** è la soluzione principale per ricostruire questa relazione. L'obiettivo è capire il percorso completo di un'operazione di business.

Un `trace` è composto da più `span` (chiamati anche "activity"). Ogni `span` rappresenta un'unità di lavoro all'interno di un servizio (es. la ricezione di un evento, una chiamata a un database). Tutti gli span appartenenti alla stessa operazione condividono un `trace id` univoco.

#### Tecnologie e Standard
*   **OpenTelemetry**: È uno standard open-source (un insieme di API, SDK e strumenti) per l'instrumentazione del codice al fine di generare, raccogliere ed esportare dati di telemetria (metriche, log e trace).
*   **Dapr.io**: Un runtime applicativo distribuito che, se usato insieme a OpenTelemetry, semplifica l'implementazione del distributed tracing. Dapr può, ad esempio, aggiungere automaticamente un `trace id` a ogni evento pubblicato.
*   **CloudEvents Distributed Tracing Extension**: La specifica CloudEvents include un'[estensione per il distributed tracing](https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/distributed-tracing.md) che standardizza come le informazioni di tracciamento (come `traceparent` e `tracestate`) debbano essere propagate all'interno degli eventi.
*   **Jaeger UI**: Un'interfaccia utente open-source per visualizzare e analizzare i trace distribuiti. Permette di vedere l'intero contesto di un messaggio e il suo flusso attraverso i servizi.

#### Span Links vs Trace Propagation
*   **Trace Propagation**: Un `trace` viene propagato attraverso i servizi, creando una catena continua di `span`. Questo è utile per visualizzare un flusso end-to-end *all'interno dello stesso dominio di business*.
*   **Span Links**: Permette di collegare `span` che appartengono a `trace` diversi ma correlati. È l'approccio preferibile quando si osservano processi di business che attraversano *domini diversi*, mantenendo i contesti di tracciamento separati ma collegati.

La regola pratica è analoga a quella tra coreografia e orchestrazione: usa la propagazione della traccia all'interno di un dominio e i link tra span per collegare domini diversi.

### Metrics
Alcune metriche fondamentali da monitorare in una EDA:
*   **Queue Depth**: Il numero di messaggi in attesa in una coda. Un valore in costante crescita è un segnale di allarme.
*   **Published/Consumed Count**: Il numero di messaggi pubblicati e consumati.
*   **Message Age**: Da quanto tempo il messaggio più vecchio è in coda.
*   **Event Type Count**: Il numero di eventi per ciascun tipo, utile per capire i flussi di business più attivi.
*   **Published/Consumed Size (Bytes)**: La dimensione dei messaggi, utile per il capacity planning.
*   **In-flight Latency**: Il tempo che intercorre tra la pubblicazione e il consumo di un evento.
*   **Processing Error Count**: Il numero di errori durante l'elaborazione dei messaggi (es. messaggi finiti in una DLQ).

## Discoverability
Indica la facilità con cui gli sviluppatori e gli altri membri del team possono scoprire quali eventi sono disponibili nel sistema, qual è il loro schema e come utilizzarli.
*   **AsyncAPI**: È una specifica open-source, simile a OpenAPI (Swagger) ma per le API asincrone e basate su eventi. Permette di definire e documentare gli eventi in un formato standard.
*   **Saunter**: Per l'ecosistema .NET, è un pacchetto NuGet che può generare automaticamente una specifica AsyncAPI analizzando il codice.

## Testing in una EDA

Testare un'architettura a eventi presenta sfide uniche a causa della natura asincrona e disaccoppiata dei suoi componenti. Non è possibile fare affidamento solo sui classici test end-to-end sincroni.

### Integration Testing

L'obiettivo dell'integration testing in una EDA è verificare che, dato un certo evento, i servizi consumatori reagiscano correttamente e producano gli effetti collaterali attesi (es. aggiornare un database, pubblicare un nuovo evento).

Un approccio comune è il seguente:
1.  **Setup dell'Ambiente**: Avviare un ambiente di test isolato che includa i servizi da testare e un'istanza del message broker (es. usando Docker Compose).
2.  **Pubblicazione dell'Evento**: Il test pubblica un evento specifico su una coda o un topic.
3.  **Assert sugli Effetti Collaterali**: Il test deve attendere e verificare che l'azione attesa si sia verificata. Questo può richiedere:
    *   **Polling di un altro consumer**: Mettersi in ascolto su un'altra coda per verificare che sia stato pubblicato un evento di risposta.
    *   **Controllo del database**: Verificare che lo stato di una o più tabelle sia stato aggiornato correttamente.
    *   **Chiamata a un'API**: Interrogare un endpoint di uno dei servizi per controllare il suo stato interno.

Questi test sono potenti ma possono essere lenti e fragili a causa della loro dipendenza da un ambiente complesso e dalla natura asincrona delle verifiche.

#### Specifiche di Comportamento (BDD e Gherkin)

La sintassi `Given-When-Then` appartiene a una metodologia chiamata **Behavior-Driven Development (BDD)**. Il linguaggio usato per scrivere queste specifiche si chiama **Gherkin** e i file vengono salvati con estensione `.feature`.

Una tecnica di test che si può usare per testare applicazioni basate su Dapr. Framework come **SpecFlow** (.NET) eseguono questi test.

La struttura è semplice e leggibile anche da persone non tecniche:
*   `Given` (Dato che): Descrive il contesto e lo stato iniziale del sistema prima dell'azione.
*   `When` (Quando): Descrive l'azione o l'evento che scatena il test (es. la pubblicazione di un evento).
*   `Then` (Allora): Descrive il risultato atteso, ovvero gli effetti collaterali da verificare.

**Esempio di file `OrderProcessing.feature`:**

```gherkin
Feature: Processamento Ordini

Scenario: Un nuovo ordine viene processato correttamente
    Given che il servizio di Notifiche è in ascolto per eventi 'OrdineCreato'
    And che nel database non esiste un ordine con ID "123"

    When un evento 'OrdineCreato' per l'ordine "123" viene pubblicato sul message bus

    Then il servizio Ordini dovrebbe salvare l'ordine "123" nel suo database
    And il servizio Notifiche dovrebbe ricevere l'evento e inviare una email di conferma
```

Dietro ogni frase di questo file `.feature` c'è del codice (chiamato "glue code" o "step definition") che esegue l'azione descritta. Per esempio:
*   La step `When` userebbe il client del message broker (o direttamente il client Dapr) per pubblicare un evento di test.
*   La step `Then` si connetterebbe al database per verificare che il record sia stato creato e potrebbe controllare un finto servizio di email (un "mock") per assicurarsi che sia stato chiamato.

### Schema e Contract Testing

Questa è una delle pratiche di testing più importanti in una EDA. Poiché producer e consumer sono disaccoppiati, c'è il rischio che un producer modifichi lo schema di un evento (il "contratto"), rompendo la funzionalità di tutti i suoi consumer senza nemmeno saperlo.

#### Schema Registry
Uno strumento fondamentale per il contract testing è lo **Schema Registry**. È un servizio centralizzato che memorizza tutti gli schemi degli eventi.
*   **Validazione**: I producer validano gli eventi contro lo schema nel registry prima di pubblicarli. I consumer possono usare lo stesso schema per deserializzare e validare gli eventi che ricevono.
*   **Controllo di Compatibilità**: Lo schema registry può imporre regole di compatibilità (es. backward compatibility). Impedisce ai producer di introdurre modifiche "breaking" che potrebbero danneggiare i consumer esistenti. Se una modifica non è compatibile, la registrazione del nuovo schema fallisce, bloccando il processo di CI/CD del producer.

#### Consumer-Driven Contract Testing
Questo approccio sposta la responsabilità della definizione del contratto sul consumer.
1.  **Il Consumer definisce il Contratto**: Durante i suoi test, il consumer genera un file di contratto (es. un file JSON) che dichiara esattamente quali campi e quale struttura si aspetta di ricevere per un dato evento.
2.  **Condivisione del Contratto**: Il contratto viene condiviso con il team del producer (spesso tramite un broker di contratti come Pact Broker).
3.  **Il Producer verifica il Contratto**: Nei test del producer, si verifica che gli eventi generati siano conformi a tutti i contratti pubblicati dai suoi consumer. Se il producer genera un evento che viola anche un solo contratto, il suo test fallisce.

Questo approccio permette ai team di evolvere i propri servizi in modo indipendente e sicuro, con la certezza che le modifiche non romperanno le integrazioni esistenti.

### Testing di Idempotenza

Verificare che l'elaborazione multipla dello stesso evento produca lo stesso risultato della singola elaborazione è fondamentale, data la garanzia di consegna "at-least-once" di molti message broker.

La strategia di test è concettualmente semplice: **inviare lo stesso messaggio due o più volte di seguito e verificare che il sistema si comporti correttamente.**

Un test di idempotenza tipicamente segue questi passi:
1.  **Azione Iniziale**: Inviare un evento per la prima volta.
2.  **Verifica Iniziale (Opzionale ma consigliata)**: Verificare che il sistema abbia raggiunto lo stato corretto dopo la prima elaborazione.
3.  **Azione Duplicata**: Inviare lo **stesso identico evento** (con lo stesso ID univoco) una seconda volta.
4.  **Verifica Finale**: Controllare che lo stato del sistema non sia cambiato in modo errato. Ad esempio, se l'evento doveva creare un record in un database, non deve essere stato creato un secondo record duplicato, né il test deve fallire per un errore di violazione di chiave primaria. L'operazione duplicata deve essere ignorata o gestita senza causare effetti collaterali indesiderati.

## Deployment di una EDA

Il deployment di un'architettura a eventi richiede strategie specifiche per gestire l'evoluzione indipendente dei servizi e la compatibilità degli schemi.

### Pipeline CI/CD Indipendenti
Ogni servizio (producer o consumer) deve avere la sua pipeline di Continuous Integration/Continuous Deployment (CI/CD). Questo è un principio chiave per sfruttare il disaccoppiamento dell'EDA, permettendo ai team di rilasciare aggiornamenti in modo autonomo e frequente.

### Infrastructure as Code (IaC)
Tutta l'infrastruttura necessaria (code, topic, sottoscrizioni del message broker, database, policy di accesso, etc.) deve essere definita e gestita tramite strumenti di Infrastructure as Code come Terraform, AWS CDK o Bicep. Questo assicura che la configurazione sia versionata, ripetibile e coerente tra i vari ambienti (sviluppo, test, produzione).

### Strategie di Deployment e Versioning
Il rilascio di nuove versioni, specialmente quando ci sono modifiche agli schemi degli eventi, deve seguire un ordine preciso per evitare errori.

1.  **Deploy dei Consumer**: Si effettua sempre *prima* il deploy delle nuove versioni dei consumer. Questi devono essere programmati per essere retrocompatibili, ovvero devono poter gestire sia il vecchio che il nuovo formato dell'evento.
2.  **Deploy dei Producer**: Solo *dopo* che tutti i consumer sono stati aggiornati e sono pronti a ricevere il nuovo formato, si può effettuare il deploy del producer che inizia a pubblicare gli eventi con lo schema modificato.

Questo approccio, noto come "Expand and Contract Pattern", garantisce che non ci siano mai consumer che ricevono eventi in un formato che non sono in grado di comprendere. L'uso di uno Schema Registry con regole di compatibilità può forzare questo comportamento a livello di pipeline.

Per i servizi stessi, si possono usare strategie come **Blue-Green Deployment** o **Canary Release** per rilasciare le nuove versioni senza downtime, spostando gradualmente il traffico (o il consumo di eventi) dalle vecchie istanze a quelle nuove.
