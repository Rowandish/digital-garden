---
tags:
  - SqlServer
---
Questo articolo è una parziale traduzione all'originale che trovate [qui](http://sqlserverplanet.com/tsql/yet-another-temp-tables-vs-table-variables-article).

___
## Introduzione

Lavorando con SQL Server capiterà stesso che, per risolvere numerosi problemi, sarà necessario immagazzinare i dati in tabelle temporanee. T-SQL offre due diverse modalità per questo scopo, le varibili di tabella e le tabelle temporanee.

La prima differenza da rilevare tra le due modalità è la sintassi: le tabelle temporanee si scrivono con il prefisso **#** (`#tempTable`), mentre le variabili di tabella come tutte le altre variabili, quindi anteponendo **@** (`@tempTable`).

```sql
DECLARE @tmp TABLE (Col1 INT, Col2 INT);
CREATE TABLE #tmp (Col1 INT, Col2 INT);
```

Le tabelle temporanee sono normali tabelle SQL che sono memorizzate nel _tempDB_. L'unica differenza tra queste è una normale tabella è che queste non permettono di definire una chiave esterna su di esse.

La variabili di tabella invece non vengono memorizzate in nessun DB e vengono eliminate una volta terminata la sessione.

Di seguito approfondiamo tutte le differenze tra le due.

## Scope

Le tabelle `#tempTable` possono essere viste da qualsiasi oggetto che viene lanciato nella stessa sessione: quindi se definisco una tabella `#tempTable` nella procedura A, poi questa chiama la procedura B, la procedura B avrà modo di accedere allo stesso modo alla tabella temporanea.

Una volta che la sessione è terminata, la `#tempTable` associata a questa sessione verrà deallocata (ma rimarrà comunque nel datamase temporaneo).

Le variabili `@tempTable` hanno scope limitato alla procedura che le crea, non possono essere chiamate da un'altra procedura nella stessa sessione.

## SELECT INTO

Con una tabella temporanea `#tempTable` è possibile catturare i risultati di una `SELECT INTO` in una nuova tabella senza che questa sia definita prima e le cui colonne e tipi sono create runtime.

```sql
SELECT * INTO #temp FROM foo
```

Questo non è possibile con una variabile di tabella `@temp`.

## Scrittura su disco

Entrambe le modalità scrivono su disco con la stessa velocità.

## Ricompilazione

La ricompilazione è il maggiore vantaggio per le variabili `@table`. Se il set di dati da cui prendo i valori è piccolo e non cambia, conviene sicuramente usare le `@table` che evitano rallentamenti di ricompilazione.

## Indici particolari

Se voglio scrivere un indice che non può essere creato implicitamente con i vincoli di `UNIQUE` e `PRIMARY KEY`, allora devo per forza utilizzare le variabili `#table` (esempi di questi indici sono quelli non unique, indici filtrati o indici con colonne `INCLUDED`)

## Numerose operazioni

Se devo ripetutamente aggiungere e eliminare un grande numero di righe dalla tabella, allora conviene (a livello di prestazioni) usare una tabella `#tempTable`.  
Ricordiamo che questa supporta l'istruzione `TRUNCATE` (a differenza della @table) che è più efficente del `DELETE`.

## Transazioni

Le varibiali `@tempTable` non partecipano alle transazioni, questo significa che sono veloci ma meno sicure, per esempio se faccio un `ROLLBACK` i valori delle variabili `@tempTable` non vengono modificati.

## Eliminazione

Le `#tempTable` devono essere eliminate dopo l'uso (pratica di buona programmazione), le `@tempTable` no in quanto vengono eliminate automaticamente.

Esempio di eliminazione di una tabella temporanea `#tempTable`:

```sql
IF(OBJECT_ID('tempdb..#tempTable') IS NOT NULL) DROP TABLE #tempTable
```

## Conclusione

Per concludere, se sto lavorando con **un piccolo insieme di dati (numero di righe minore di 100) e che la sorgente da cui questi dati vengono presi non cambia**, conviene usare le variabili `@tempTable`, in tutti gli altri casi `#tempTable`.