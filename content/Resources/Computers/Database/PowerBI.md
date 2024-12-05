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
## Best Practices

Per utilizzare Power BI in modo efficiente, è consigliabile centralizzare tutti i dati in un unico DBMS (ad esempio SQL Server) ed evitare connessioni multiple a basi dati diverse, specialmente in presenza di grandi volumi. È preferibile eseguire calcoli e trasformazioni complesse direttamente nel database tramite viste ad hoc, demandando a Power BI esclusivamente la visualizzazione dei dati. Inoltre, è utile pianificare aggiornamenti notturni per garantire che i report siano sempre aggiornati senza impattare sulle performance operative.