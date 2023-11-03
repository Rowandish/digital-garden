---
tags:
  - Coding
  - SqlServer
  - PublishedPosts
---


## 1.Introduzione
Gli indici progettati in modo non corretto e la mancanza di indici costituiscono le cause principali dei colli di bottiglia delle applicazioni di database. La progettazione di indici efficienti è fondamentale per ottenere buone prestazioni del database e dell'applicazione.

Un indice è una struttura su disco associata a una tabella o a una vista che consente di recuperare in modo rapido le righe della tabella o della vista. L'indice contiene chiavi costituite da una o più colonne della tabella o della vista. Queste chiavi vengono archiviate in una struttura (albero binario) che consente a SQL Server di individuare con rapidità ed efficienza la riga o le righe associate ai valori di chiave.

La selezione degli indici adatti a un database e al relativo carico di lavoro è un'operazione complessa che comporta la ricerca di un equilibrio tra velocità delle query e costi di aggiornamento. Gli **indici limitati**, ovvero con poche colonne nella chiave di indice, richiedono meno spazio su disco e overhead di gestione. Gli **indici estesi**, d'altra parte, coprono più query. Potrebbe essere necessario sperimentare diverse soluzioni prima di trovare l'indice più efficiente.

Il mondo della progettazione degli indici migliori per le tabelle di un databse è molto complesso, in questo articolo ci limitiamo a descrivere i due principali tipi di indici: clustered e non-clustered, seguendo [questo articolo](https://www.mssqltips.com/sqlservertip/1206/understanding-sql-server-indexing).

Nella sua definizione più semplice, un indice *clustered* è un indice che **immagazzina i dati (valore)** mentre un indice *non-clustered* è solo un insieme di **puntatori a tale dato (riferimento)**.
Una tabella può avere un solo indice *clustered* e fino a 249 indici non-clustered.
Se una **tabella non ha indici clustered si può definire come uno heap** (struttura dati basata sugli alberi che soddisfa la "proprietà di heap": se A è un genitore di B, allora la chiave di A è ordinata rispetto alla chiave di B conformemente alla relazione d'ordine applicata all'intero heap).

La ragione principale per cui gli indici vengono creati è per fornire tempi di accesso più rapidi su particolari tipi di dati, sia per gli indici *clustered* che *non-clustered*. Senza gli indici, una query deve leggere **tutti** i dati di una tabella per trovare le righe che la soddisfano.

## 2. Clustered o non-clustered?
Vedremo la differenza tra le tipologie di indici con query diverse.
Nella spiegazione farò riferimento ai seguenti concetti:
- **index Seek**: funzionalità di ricerca degli indici per recuperare righe da un indice cluster. In pratica ottengo i *Row ID* associati al cognome in ingresso. Costo di ricerca: 1%.
- **RID Lookup**: ricerca in un albero heap utilizzando un *Row ID*. Il *Row ID* è incluso in un indice non-clustered per trovare i dati da un albero heap. Visto che una tabella heap è una tabella senza un indice clustered disordinata, è richiesto un `Row ID` per eseguire la correlazione. Costo di ricerca: 99%.
- **Clustered index Seek**: funzialità ri ricerca su tabelle con indici clustered. Costo: 99%.
- **Key Lookup**: ricerca analoga alla `RID Lookup` (quindi che avviene dopo un `index Seek`) con la differenza che avviene su una tabella con indice clustered.

### 2.1 Esempio 1
In questo primo esempio voglio cercare tutti i record che hanno come cognome "*Adams*".
```sql
SELECT * FROM Contatti WHERE Cognome = 'Adams'
```
#### 2.1.1 Nessun indice
Se non è definito nessun indice, SQL Server esegue una *Table Scan* su tutte le righe per determinare quelle che hanno il cognome sopra citato, fornendo un *Estimated Subtree Cost* di 0.437103.

#### 2.1.2 Indice non-clustered sul campo di ricerca
Ora, assumiamo di avere creato un indice non-clustered sulla colonna `Cognome`, per ottenere i dati indicati sopra, SQL Server utilizza una ***index Seek* con *RID Lookup***, portando un *Estimated Subtree Cost* a 0.263888.

#### 2.1.3 Indice non-clustered sul campo di ricerca e clustered sull'Id
In questo caso SQL Server sostituisce la *RID Lookup* con una *Clustered index Seek*, fornendo un tempo di 0.264017.

#### 2.1.4 Indice clustered sul campo di ricerca
Dato che un indice clustered punta direttamente ai dati nella tabella, per ritrovare le righe in questione basta fare un ***index Seek* senza *RID Lookup***, il cui costo è 0.0044572. Questo è senza dubbio il metodo più veloce di reperimento dei dati per questo tipo di query.

### 2.2 Esempio 2
In questo secondo esempio voglio cercare solo la colonna `Cognome`.
```sql
SELECT Cognome FROM Contatti WHERE Cognome = 'Adams'
```
#### 2.2.1 Indice non-clustered sul campo di ricerca
Visto che in questa query ho che l'oggetto dell'indice è uguale all'oggetto della mia ricerca (*covering query*), SQL Server non deve accedere alla tabella, non ho quindi nessuna *RID Lookup*. Il costo è pari a 0.0033766.

#### 2.2.2 Indice clustered sul campo di ricerca
Il costo in questo caso è pari a 0.0044572, che è esattamente identico al caso in cui io volessi reperire tutte le colonne e non solo la colonna `Cognome`, come è intuibile.

### 2.3 Conclusione
Da questi esempi si possono vedere i benefici di usare gli indici.
Intuitivamente si potrebbe pensare di avere un indice clustered sul campo più ricercato (posso avere un solo indice clustered per tabella) e indici non-clustered su tutte le altre colonne.
Allo stesso modo per cui questo metodo risulta veloce quando devo reperire dei dati, allo stesso modo aggiungere overhead alle istruzioni di `INSERT`, `UPDATE` e `DELETE`, in quanto devo andare anche a modifica l'indice, oltre che la tabella.
La scelta dell'indice quindi è una attività complessa che dipende molto dal tipo di interazioni che eseguo su una tabella e dal database su cui opero.

## 3. Scelta dell'indice clustered
Dato che, per ogni tabella, è possibile definire **un solo indice clustered**, la scelta su quale colonna definirlo non è banale.
Spesso sono semplicemente la chiave primaria unique `ID`; questo può essere un buon inizio quando non si ha bene idea di come i dati sono acceduti ma, una volta che sono disponbili statistiche sull'utilizzo del database, è possibile tornare indietro e verificare se la scelta fatta sia la migliore possibile.
### 3.1 Definizione della tabella
Lavoriamo sulla tabella `Indirizzo` che ha chiave primaria e identity `IndirizzoID`, oltre che un indice clustered su tale campo.
Abbiamo inoltre un indice *non-clustered* sulla coppia (`LineaIndirizzo1`, `LineaIndirizzo2`) e uno sulla colonna `StatoProvinciaID`.
### 3.2 Query di esempio
Assumiamo di dover fare la seguente query
```sql
SELECT LineaIndirizzo1, LineaIndirizzo2
FROM Indirizzo
WHERE StatoProvinciaID = 1
```
Questa query esegue un:
- **index Seek**: cerca nell'indice non-clustered i record che hanno `StatoProvinciaID = 1`. Costo 4%.
- **Key Lookup**: ricerca il dato trovato tramite l'indice clustered. Costo 96%.

Ora, se nel nostro database la maggior parte della query sulla tabella Indirizzo esegue una ricerca sullo `StatoProvinciaID`, possiamo evitare il *Key Lookup* e mettere l'indice clustered della tabella direttamente sulla colonna `StatoProvinciaID` in modo che venga effettuato solo un `Clustered index Seek` che è estremamente veloce.

## 4. Ottenere informazioni sull'uso degli indici
Abbiamo visto che per decidere i corretti indici da utilizzare sul nostro server, è necessario per prima cosa conoscere come le tabelle su cui lavoriamo vengono lavorate.
Risulta quindi necessario avere dei modi per capire come gli indici creati vengono usati; per ottenere ciò esistono le seguenti viste: `sys.dm_db_index_operational_stats` e `sys.dm_db_index_usage_stats`.
Le query che indico sono state fornite da [questo ottimo sito](https://www.mssqltips.com/sqlservertip/1239/how-to-get-index-usage-information-in-sql-server/).


### 4.1 sys.dm_db_index_operational_stats
Questa vista fornisce informazioni sul numero di insert, update e delete che occorrono su un particolare indice. Le colonne più interessanti vengono fornite dalla seguente query.
```sql
SELECT OBJECT_NAME(A.[OBJECT_ID]) AS [OBJECT NAME]
, I.[NAME] AS [index NAME]
, A.LEAF_INSERT_COUNT
, A.LEAF_UPDATE_COUNT
, A.LEAF_DELETE_COUNT
FROM SYS.DM_DB_index_OPERATIONAL_STATS(NULL, NULL, NULL, NULL) A
INNER JOIN SYS.indexES AS I ON I.[OBJECT_ID] = A.[OBJECT_ID]
AND I.index_ID = A.index_ID
WHERE OBJECTPROPERTY(A.[OBJECT_ID], 'IsUserTable') = 1
ORDER BY 1
```

### 4.2 sys.dm_db_index_usage_stats
Questa vista fornisce informazioni generiche sui metodi di accesso agli indici definiti, in particolare il numero di *index seek*, *index scan*, *index lookup* e *user_updates* (insieme di insert, update, delete).
```sql
SELECT OBJECT_NAME(S.[OBJECT_ID]) AS [OBJECT NAME]
, I.[NAME] AS [index NAME]
, USER_SEEKS
, USER_SCANS
, USER_LOOKUPS
, USER_UPDATES
FROM SYS.DM_DB_index_USAGE_STATS AS S
INNER JOIN SYS.indexES AS I ON I.[OBJECT_ID] = S.[OBJECT_ID]
AND I.index_ID = S.index_ID
WHERE OBJECTPROPERTY(S.[OBJECT_ID], 'IsUserTable') = 1
ORDER BY (USER_UPDATES - USER_LOOKUPS - USER_SCANS - USER_SEEKS) DESC
```
In particolare i risultati vengono ordinati rispetto alla differenza tra quanto un indice viene aggiornato (`USER_UPDATES`) e quanto invece viene interrogato (*scan*, *seek*, *lookups*). Se un indice viene molto interrogaato e poco aggiornato allora è un ottimo indice, al contrario rallenta il sistema senza offrire nulla.
