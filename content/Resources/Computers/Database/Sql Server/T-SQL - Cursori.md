---
tags:
  - Coding
  - SqlServer
  - PublishedPosts
---
Questo articolo segue direttamente quanto indicato sulla documentazione ufficiale Microsoft sull'utilizzo dei cursori, conseguentemente la sintassi indicata è quella TSQL, ma i cursori sono definiti anche in altri tipi di DBMS come MySQL o PostgreSQL.

## Introduzione

Un cursore offre la possibilità di elaborare un set di dati (quindi il risultato di una `SELECT`) una riga alla volta.  
Le istruzioni principali sono le seguenti:

-   **DECLARE CURSOR**: definisce gli attributi di un cursore del server Transact-SQL, ad esempio lo scorrimento e la query utilizzata per compilare il set di risultati su cui agisce il cursore.
-   **OPEN**: esegue il popolamento del set di risultati e l'istruzione `FETCH` restituisce una riga dal set di risultati.
-   **CLOSE**: rilascia il set di risultati corrente associato al cursore.
-   **DEALLOCATE** rilascia le risorse utilizzate dal cursore.

Tipicamente la dichiarazione di un cursore segue questo pattern:
```sql
DECLARE @var1 VARCHAR(max);
DECLARE @var2 VARCHAR(max);

DECLARE Cursor_name CURSOR
FOR
SELECT var1
    , var2
FROM tabel_name

OPEN Cursor_name;

FETCH NEXT
FROM Cursor_name
INTO @var1
    , @var2;

WHILE @@FETCH_STATUS = 0
BEGIN
    FETCH NEXT
    FROM Cursor_name
    INTO @var1
        , @var2;
END;

CLOSE Cursor_name;

DEALLOCATE Cursor_name;
```

## Comandi e funzioni

### `@@FETCH_STATUS`

Restituisce lo stato dell'ultima istruzione `FETCH` eseguita su qualsiasi cursore attualmente aperto dalla connessione.

|Valore restituito | Descrizione|
|----|----|
|0|L'istruzione FETCH ha avuto esito positivo.|
|-1|L'istruzione FETCH ha avuto esito negativo oppure la riga non è compresa nel set di risultati.|
|2|La riga recuperata è mancante.|

Viene spesso usata come condizione di uscita del ciclo WHILE:

```sql
WHILE @@FETCH_STATUS = 0
```

### `@@CURSOR_STATUS`

Funzione scalare che consente al chiamante di una stored procedure di determinare se la procedura ha restituito o meno un cursore e un set di risultati per un determinato parametro.

### `@@CURSOR_ROWS`

Restituisce il numero delle righe attualmente risultanti nell'ultimo cursore aperto sulla connessione.

### `DECLARE CURSOR`

Definisce gli attributi di un cursore del server Transact-SQL, ad esempio lo scorrimento e la query utilizzata per compilare il set di risultati su cui agisce il cursore.  
La dichiarazione standard di un cursore agisce secondo la sintassi seguente:

```sql
DECLARE cursor_name CURSOR
FOR select_statement
```

In cui _select statement_ è l'istruzione `SELECT` standard che definisce il set di risultati del cursore.

### `OPEN`

_Apre un cursore_ server Transact-SQL e popola il cursore mediante l'istruzione Transact-SQL specificata nell'istruzione `DECLARE CURSOR` o `SET cursor_variable`.

OPEN cursor_name

### `FETCH`

Recupera una riga specifica da un cursore server Transact-SQL.  
Solitamente viene usato nel seguente modo:
```sql
FETCH NEXT
FROM cursor_name
INTO @variable_name
```

-   `NEXT`: restituisce la riga del set di risultati successiva alla riga corrente e imposta la riga corrente sulla riga restituita.
-   `INTO @variable_name` consente di inserire in variabili locali i dati delle colonne ottenute da un'operazione di recupero.

Ogni variabile dell'elenco, da sinistra a destra, è associata alla colonna corrispondente nel set di risultati del cursore.  
A ogni variabile deve essere associato lo stesso tipo di dati o un tipo di dati che supporti la conversione implicita dal tipo di dati della colonna corrispondente nel set di risultati.  
Il numero di variabili deve corrispondere al numero di colonne dell'elenco di selezione del cursore.

### `CLOSE`

**Chiude un cursore aperto** rilasciando il set di risultati corrente e liberando i blocchi dei cursori mantenuti attivi sulle righe in cui è posizionato il cursore. L'istruzione `CLOSE` mantiene le strutture dei dati disponibili per successive operazioni di apertura. Le operazioni di recupero e di aggiornamento posizionato, tuttavia, sono consentite solo dopo la riapertura del cursore. È necessario eseguire l'istruzione `CLOSE` su un cursore aperto. L'esecuzione non è consentita su cursori solo dichiarati o già chiusi.

```sql
CLOSE cursor_name
```
### `DEALLOCATE`

**Rimuove un riferimento a un cursore**. Dopo che l'ultimo riferimento al cursore è stato deallocato, le strutture di dati che includono il cursore vengono rilasciate da Microsoft SQL Server.
```sql
DEALLOCATE cursor_name
```