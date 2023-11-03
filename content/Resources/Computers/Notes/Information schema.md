---
tags:
  - SqlServer
  - PublishedPosts
---


Le viste _Information Schema_ sono uno delle tante modalità offerte da SQL Server per ottenere dei metadati. Il vantaggio di utilizzare tale vista è che è presente in quasi tutti i RDMS (è uno standard ANSI), per esempio _Oracle_, _MySQL_ e _PostgreSQL_ lo supportano.

Queste viste hanno il vantaggio di fornire informazioni indipendenti dalle tabelle interne utilizzate da SQL server o dal RDBMS di riferimento, stando quindi ad un livello di astrazione superiore.

In questo post approfondiremo le tre principali viste di _Information Schema_, cioè quelle riguardanti le tabelle, le viste e le colonne

### TABLES

Fornisce una riga per ogni tabella nel database corrente, in particolare fornisce le seguenti colonne:

- `TABLE_CATALOG`: Nome del database
- `TABLE_SCHEMA`: Nome dello schema che contiene la tabella
- `TABLE_NAME`: Nome della tabella
- `TABLE_TYPE`: Tipo della tabella, può essere o `VIEW` o `BASE TABLE`

### COLUMNS

Fornisce una riga per ogni colonna nel database corrente, in particolare fornisce le seguenti colonne (indico solo le principali)

- `TABLE_CATALOG`: Nome del database
- `TABLE_SCHEMA`: Nome dello schema che contiene la tabella
- `TABLE_NAME`: Nome della tabella
- `COLUMN_NAME`: Nome della colonna
- `ORDINAL_POSITION`: Numero identificativo della stessa
- `COLUMN_DEFAULT`: Valore di default
- `IS_NULLABLE`: YES se la colonna permette anche valori NULL, NO altrimenti

### VIEWS

Fornisce una riga per ogni vista nel database corrente, in particolare fornisce le seguenti colonne (indico solo le principali)

- `TABLE_CATALOG`: Nome del database
- `TABLE_SCHEMA`: Nome dello schema che contiene la tabella
- `TABLE_NAME`: Nome della tabella
- `VIEW_DEFINITION`: Fornisce la definizione della vista, solo se è lunga meno di 4000 caratteri. Altrimenti NULL

### Esempi

Di seguito qualche query che utilizza `INFORMATION_SCHEMA`

##### Ottenere informazioni di una determinata tabella
```Sql
SELECT \*
FROM INFORMATION_SCHEMA.TABLES --VIEWS, COLUMNS
WHERE TABLE_NAME = N'foo'
```
##### Ottenere informazioni per la stessa tabella su tutti i database

Per ottenere invece l'informazione su tutti i database e non solo il corrente è necessario utilizzare la procedura `sp_msforeachdb` con la `sys.tables` nel seguente modo:
```sql
sp_msforeachdb 'SELECT "?" AS dbname, \* FROM \[?\].sys.tables WHERE name="foo"'
```

##### Controllare l'esistenza di una vista

Esistono varie query per verificare l'esistenza di una vista (ed analogamente ogni altro oggetto), la soluzione più portabile in quanto (quasi) agnostica al tipo di database è la seguente:
```sql
SELECT count(\*)
FROM INFORMATION_SCHEMA.VIEWS
WHERE table_name = 'View'
AND table_schema = 'Schema'
```