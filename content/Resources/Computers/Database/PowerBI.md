Power BI è una piattaforma di **business intelligence** e analisi dati sviluppata da Microsoft, progettata per raccogliere, elaborare e visualizzare dati in modo intuitivo.
Unisce le funzionalità di **SQL Server Reporting Services** e **Excel**, consentendo di creare report e dashboard interattivi. Gli utenti progettano i report localmente tramite **Power BI Desktop** e li pubblicano nel cloud attraverso il **Power BI Service**, dove possono essere condivisi e visualizzati.
## Versioni e Licenze

Power BI è disponibile in due versioni principali.
La **versione gratuita** offre funzionalità limitate, rendendola poco adatta per utilizzi aziendali. La **versione PRO**, al costo di **9,40€ al mese per utente**, permette il caricamento e l'aggiornamento automatico dei report, la condivisione interna e offre un limite di **1 GB di RAM per modello**.
La licenza è legata a una singola email, consentendo però l’accesso da più dispositivi.

## Acquisizione Dati

### Import vs DirectQuery

Power BI consente due modalità principali di connessione ai dati: **Import** e **DirectQuery**.

- La modalità **Import** è la più utilizzata, poiché preleva i dati statici dai database e li memorizza localmente, aggiornandoli a intervalli programmati (tipicamente notturni). Questo approccio garantisce performance ottimali ed è supportato da tutti i connettori.
- La modalità **DirectQuery**, invece, consente interrogazioni dirette al database in tempo reale, ma presenta limitazioni come supporto parziale dei connettori e potenziali problemi di performance con grandi moli di dati.

### Connettori e Fonti di Dati

Un **connettore** è l’elemento che consente a Power BI di accedere a diverse fonti di dati, come database relazionali, servizi cloud, fogli Excel e API REST. Per accedere ai connettori disponibili, è sufficiente utilizzare l’opzione **Get Data**. Tra le principali fonti supportate vi sono SQL Server, MySQL, PostgreSQL, Azure, Salesforce e file CSV.

### Connessione a un Database

Connettersi a un database con Power BI richiede alcuni semplici passaggi:

1. Scegliere il tipo di connettore in base alla fonte dati.
2. Configurare i dettagli della connessione, inserendo l’indirizzo del server e le credenziali. È possibile specificare una query personalizzata per simulare una vista virtuale.
3. Selezionare le tabelle o le viste da utilizzare.
4. Caricare i dati con l’opzione **Load** o modificarli preliminarmente con **Transform Data**.

## Manipolazione e Trasformazione dei Dati

Power BI offre strumenti avanzati per trasformare e modellare i dati:

- **Power Query** consente di eliminare colonne, modificare tipi di dati e calcolare nuovi campi. Ogni trasformazione è registrata come uno step ripetibile.
- **DAX (Data Analysis Expressions)** permette calcoli avanzati, come la creazione di tabelle di date continue tramite l'operatore `CALENDAR`.
- L’**Editor Relazioni** consente di definire le connessioni tra tabelle per garantire un modello dati coerente e funzionale.

È inoltre possibile aggiungere colonne personalizzate, definite da formule, con la funzionalità **Custom Column**. Il tipo di dato generico assegnato può essere modificato manualmente per esigenze specifiche.


### Date

Power BI richiede che le tabelle di date rispettino i seguenti criteri per funzionare correttamente nei modelli di dati, specialmente per creare visualizzazioni temporali o gestire relazioni tra tabelle:
1. **Date senza buchi**: Ogni giorno deve essere presente, senza interruzioni (ad esempio, dal 1 gennaio al 31 dicembre di un anno, tutte le date devono essere rappresentate).
2. **Date uniche**: Non devono esistere date duplicate nella colonna di riferimento.

Per soddisfare questi requisiti, è consigliabile utilizzare una tabella calendario dedicata che funge da base per analisi temporali.
#### 1. `CalendarAuto`
La funzione **`CalendarAuto`** genera automaticamente una tabella calendario basandosi sui dati già presenti nel modello. Essa determina la **prima data** e l’**ultima data** disponibili nel modello e crea un intervallo continuo.
Non permette di specificare un intervallo personalizzato (utilizza esclusivamente le date esistenti nei dati).
```dax
CalendarTable = CALENDARAUTO()
```

#### 2. `Calendar`
La funzione **`Calendar`** consente di specificare un intervallo personalizzato definendo manualmente la data di inizio e la data di fine. È utile quando si vuole analizzare un periodo temporale che va oltre l'intervallo dei dati presenti (ad esempio, includendo anni futuri).
```dax
Calendario =
VAR dataMin = MIN(Orders[OrderDate]) -- Trova la data più piccola nella tabella Orders
VAR dataMax = MAX(Orders[OrderDate]) -- Trova la data più grande nella tabella Orders
RETURN CALENDAR(dataMin, dataMax)
```

### Misure vs Colonne calcolate
Le **misure** in Power BI sono calcoli dinamici che aggregano o manipolano i dati in base al contesto della visualizzazione in cui vengono utilizzate.
Una misura è sempre calcolata al volo e restituisce un singolo valore come risultato, che cambia in base ai filtri, ai raggruppamenti o al contesto applicato nel report.
```dax
TotaleVendite = SUM(Sales[Amount])
```

Le **colonne calcolate** sono calcoli statici che vengono aggiunti direttamente a una tabella come nuova colonna. Vengono calcolate durante l'elaborazione dei dati (al momento del caricamento o dell'aggiornamento) e il loro risultato è memorizzato nel modello di dati.
```dax
PrezzoTotale = Sales[Quantity] * Sales[Price]
```

#### Differenze tra Misure e Colonne Calcolate

| Caratteristica  | **Misure**                                                         | **Colonne Calcolate**                                           |
| --------------- | ------------------------------------------------------------------ | --------------------------------------------------------------- |
| **Calcolo**     | Dinamico, in tempo reale in base al contesto                       | Statico, calcolato una volta e salvato nel modello              |
| **Memoria**     | Non occupa spazio nel modello, poiché calcolata al volo            | Occupa spazio nel modello (memorizzazione dei valori calcolati) |
| **Contesto**    | Dipendente dal contesto di filtro e di righe nella visualizzazione | Indipendente dal contesto, calcolata riga per riga              |
| **Utilizzo**    | Utilizzata per aggregazioni, calcoli complessi, indicatori KPI     | Utilizzata per calcoli riga per riga o colonne aggiuntive       |
| **Prestazioni** | Efficiente per grandi dataset                                      | Può rallentare il modello con dataset molto grandi              |


## Report

Una volta che i dati sono stati acquisiti e preparati, Power BI consente di creare report altamente interattivi con **oggetti visivi** predefiniti o personalizzabili tramite linguaggi come Python, R o React. Tra gli strumenti più utili c’è lo **Slicer**, che permette di filtrare dinamicamente i dati in base a parametri come date (con slider) o categorie (con checkbox).

Dopo aver progettato il report in Power BI Desktop, il passaggio successivo è la sua **pubblicazione ("push")** nel cloud tramite Power BI Service. Questo processo trasferisce la struttura del report e i dati minimi necessari, lasciando che il cloud recuperi eventuali aggiornamenti direttamente dal database originale.

### Accesso e Visualizzazione

Gli utenti possono accedere ai report pubblicati nel cloud tramite un browser o l'app Power BI Mobile. I report sono organizzati all'interno delle workspace aziendali e possono essere condivisi tramite link diretti. Durante la visualizzazione, è possibile interagire con i grafici, applicare filtri e analizzare i dati nei dettagli, rendendo le informazioni accessibili in modo chiaro e dinamico.

## Report e modello semantico

==Un file di **report** è una combinazione di dati e visualizzazioni==. Contiene sia il modello dati (le tabelle, le relazioni tra di esse, le trasformazioni applicate ai dati, le misure create con DAX) sia le pagine di report dove sono presenti grafici, tabelle e altri elementi visivi che rappresentano quei dati in modo analitico e interattivo. Il report, quindi, è pensato per essere un prodotto completo che consente agli utenti di esplorare e analizzare i dati direttamente.

D'altra parte, ==un **modello semantico** è un file che si concentra esclusivamente sul modello dati, senza includere alcun tipo di visualizzazione==. Il suo scopo è fornire un ==modello dati centralizzato e condiviso che può essere utilizzato da più report==. Quando pubblichi un modello semantico nel servizio Power BI, diventa un dataset che può essere riutilizzato da altri utenti o team per costruire i loro report. Questo approccio è particolarmente utile in ambienti aziendali, dove la coerenza tra i report è fondamentale, poiché garantisce che tutti utilizzino gli stessi dati, trasformazioni e regole aziendali.

## Pagina drill-through
Una **pagina drill-through** in Power BI è una pagina di report progettata per fornire un livello di dettaglio più approfondito su uno specifico elemento o categoria presente in un'altra pagina del report.
==Di solito, queste pagine sono tenute nascoste== o comunque non sono direttamente accessibili all'utente, ma diventano visibili quando qualcuno decide di approfondire un aspetto particolare dei dati.

Il concetto chiave è che, ==quando si accede a una pagina drill-through, tutti i filtri e i contesti applicati sull'elemento selezionato nella pagina principale vengono automaticamente trasferiti alla pagina di dettaglio==.
Ad esempio, se stai visualizzando un riepilogo delle vendite per regione e vuoi vedere i dettagli relativi a una specifica regione, cliccando su quella regione puoi accedere alla pagina drill-through che mostra informazioni più granulari, come i prodotti venduti, i clienti coinvolti o le tendenze temporali.

## Drill-up e drill-down

Il **drill-down** e il **drill-up** in Power BI sono funzionalità che permettono di navigare attraverso diversi livelli di dettaglio in una gerarchia di dati, direttamente all’interno di una visualizzazione, come un grafico o una tabella.

Con il **drill-down**, puoi scendere a un livello più specifico all'interno della gerarchia. Ad esempio, se stai guardando le vendite totali per anno, puoi fare drill-down per vedere le vendite per trimestre, mese o giorno. Questo ti consente di analizzare i dati in modo più granulare, partendo da una visione generale e arrivando fino ai dettagli più minuti.

Al contrario, il **drill-up** ti permette di risalire verso livelli più alti della gerarchia. Se stavi esaminando le vendite per mese e vuoi tornare a una visione più sintetica, puoi fare drill-up per vedere i totali per trimestre o per anno. È il modo per tornare a una prospettiva più ampia dopo aver esplorato i dettagli.

## Best Practices

Per utilizzare Power BI in modo efficiente, è consigliabile centralizzare tutti i dati in un unico DBMS (ad esempio SQL Server) ed evitare connessioni multiple a basi dati diverse, specialmente in presenza di grandi volumi. È preferibile eseguire calcoli e trasformazioni complesse direttamente nel database tramite viste ad hoc, demandando a Power BI esclusivamente la visualizzazione dei dati. Inoltre, è utile pianificare aggiornamenti notturni per garantire che i report siano sempre aggiornati senza impattare sulle performance operative.

## Utilizzare Power BI per visualizzare report dei dati raccolti da macchine di produzione

### Fase 1: Raccolta dei dati dalle macchine
- **Generazione dei dati:**  
    Le macchine di produzione scrivono i dati in un database esterno. Questi dati devono essere discretizzati, ossia campionati in momenti significativi, per ridurre il volume complessivo. L'idea è disaccoppiare il db locale con il db remoto in modo che uno non dipenda dall'altro; lo schema dei due db è diverso e tipicamente sono gestiti da due team diversi.
- **Posizione del database:**  
    Il database può essere interno all’azienda (on-premises) oppure in cloud.
### Fase 2: Configurazione del collegamento a Power BI
- **Installazione del Gateway dei dati:**
    - Per permettere a Power BI di accedere ai dati del database, è necessario installare il **Gateway dei Dati** sulla macchina che ospita il database (o che ha accesso al database).
    - **Modalità di funzionamento del gateway:**
        1. **Modalità Standard:** Consente al gateway di accedere a percorsi di rete, come database SQL Server, PostgreSQL o MySQL. Questa modalità è consigliata per i database centralizzati.
        2. **Modalità Personale:** Funziona solo con file locali, come Excel o CSV, ma è meno adatta a questo scenario poiché non supporta connessioni di rete.
    - **Nota importante:**  
        Se il gateway rimane offline per un lungo periodo, Power BI potrebbe considerarlo non più utilizzabile, costringendo a una riconfigurazione completa.
### Fase 3: Configurazione di Power BI per i report
- **Creazione dell’area di lavoro su Power BI Service:**  
    In Power BI Service (l’interfaccia web), crea una **nuova area di lavoro** (se non esiste già per quel cliente).
- **Preparazione del file report locale:**  
    Sul computer dove gira l'applicazione del cliente locale del cliente, scarica **Power BI Desktop**, metti il nostro report e aggiorna la sorgente dati in modo che punti al database corretto.
- **Pubblicazione su Power BI Service:**  
    Accedi con l’account amministratore e pubblica il report dalla versione desktop di Power BI sull’area di lavoro dedicata al cliente. Durante la pubblicazione, Power BI caricherà:    
    - Il **modello semantico**, che definisce la struttura dei dati.
    - Il **report**, che contiene le visualizzazioni.
### Fase 4: Configurazione dell’app per il cliente
- **Creazione di un’app dedicata:**  
    Una volta che i report sono pubblicati nell’area di lavoro, utilizza Power BI Service per creare una nuova **app**. L’app è un contenitore che consente al cliente di accedere facilmente ai report.    
    - Puoi configurare l’app in modo che includa solo i report e i dataset pertinenti per il cliente.
    - L’app viene condivisa con l’utente tramite un link.
- **Licenza del cliente:**  
    Il cliente può accedere all’app utilizzando un account Power BI con licenza **Pro** (circa 8 euro al mese per utente). Questo consente loro di visualizzare i report pubblicati.    
### Fase 5: Automazione e manutenzione
- **Aggiornamenti automatici:**  
    Configura il refresh automatico dei dati in Power BI Service. In questo modo, i report verranno aggiornati periodicamente con i dati più recenti dal database.    
