---
tags:
  - Coding
  - SqlServer
  - PublishedPosts
---
Il contenuto di questo articolo è una libera traduzione dell'articolo di Erland Sommarskog trovabile [qui](http://www.sommarskog.se/dynamic_sql.html).
_ _ _
## 1. Introduzione
Esistono tre tipologie di istruzioni che sarebbero molto comode ma non possono essere usate in SQL Server:
```sql
SELECT * FROM @tablename
SELECT @colname FROM tbl
SELECT * FROM tbl WHERE x IN (@list)
```
In tutti questi casi l'unica soluzione è la creazione dinamica della query.
Capire come funziona il dynamic SQL è molto semplice, ma non è assolutamente facile da usare nella maniera corretta.
Uno dei primi esempi che analizzeremo è scrivere una Stored Procedure che prenda una tabella come input, di seguito due esempi dal comportamento analogo:

#### 1.1 Uso i parametri in ingresso di sp_executesql
```sql
CREATE PROCEDURE general_select1 @tblname sysname,
@key varchar(10) AS
DECLARE @sql nvarchar(4000)
SELECT @sql = ' SELECT col1, col2, col3 ' +
' FROM dbo.' + quotename(@tblname) +
' WHERE keycol = @key'
EXEC sp_executesql @sql, N'@key varchar(10)', @key
```

#### 1.2 Concatenazione dei parametri in ingresso
```sql
CREATE PROCEDURE general_select2 @tblname nvarchar(127),
@key varchar(10) AS
EXEC('SELECT col1, col2, col3
FROM ' + @tblname + '
WHERE keycol = ''' + @key + '''')
```
Anche se entrambi gli esempi sono casi di cattiva programmazione (il client non deve conoscere i nomi delle tabelle su DB), il primo presenta molti meno problemi del secondo.
Nel 99.9% dei casi usare `sp_executesql` è una scelta migliore rispetto a `EXEC()`
Il primo punto da analizzare sono i permessi: quando utilizzo Stored Procedure, **l'utente che le esegue non necessità dei permessi per accedere alle tabelle accedute dalle Stored**.
Quando utilizzo le SQL dinamiche invece questo non succede!
Nell'caso sopra, per esempio, l'utente deve avere il permesso di poter eseguire una `SELECT` sulla tabella `@tblname` in quanto **l'SQL dinamica non è parte della stored procedure ma ha uno suo scope, con i suoi permessi associati**.

## 2. sp_executesql
sp_executesql è una procedura di sistema che prende in ingresso due parametri e n parametri opzionali.

- Il primo parametro, `@stmt`, è obbligatorio e contiene un batch di query SQL. Il tipo di questo parametro è `nvarchar(MAX)`.
- Il secondo parametro, `@params`, è opzionale ma lo useremo il 90% delle volte. Questo dichiara i parametri che si troveranno in `@stmt`, la sintassi è esattamente la stessa che troveremo per una lista di parametri in ingresso di una Stored Procedure, possono avere un valore di default e un marker `OUTPUT`.
- Il resto dei parametri sono i parametri dichiarati in `@params` e possono essere passati allo stesso modo con cui vengono passati ad una Stored Procedure, quindi o nominalmente o posizionalmente. Per ottenere un valore come parametro di output devo specificare il parametro OUTPUT, allo stesso modo di quando chiamo una Stored Procedure.

### 2.1 Esempio
Assumiamo di avere in molte tabelle la colonna *LastUpdated*, che mi indica l'ultima volta che è stata modificata una determinata riga.
Voglio trovare quante righe sono state modificate in ogni tabella in un certo lasso di tempo.
Lo script sarà strutturato nel seguente modo:
```sql
DECLARE @tbl sysname,
@sql nvarchar(MAX),
@params nvarchar(MAX),
@count int

DECLARE tblcur CURSOR STATIC LOCAL FOR
SELECT object_name(id) FROM syscolumns WHERE name = 'LastUpdated'
ORDER BY 1
OPEN tblcur

WHILE 1 = 1
BEGIN
FETCH tblcur INTO @tbl
IF @@fetch_status <> 0
BREAK

SELECT @sql =
N' SELECT @cnt = COUNT(*) FROM dbo.' + quotename(@tbl) +
N' WHERE LastUpdated BETWEEN @fromdate AND ' +
N' coalesce(@todate, ''99991231'')'
SELECT @params = N'@fromdate datetime, ' +
N'@todate datetime = NULL, ' +
N'@cnt int OUTPUT'
EXEC sp_executesql @sql, @params, '20060101', @cnt = @count OUTPUT

PRINT @tbl + ': ' + convert(varchar(10), @count) + ' modified rows.'
END

DEALLOCATE tblcur
```
Analizziamo la parte della costruzione della query dinamica passo a passo.
La prima parte consiste nella creazione della query base, ponendo attenzione a:

- Facilità di lettura (usare gli a capo per rendere chiara la lettura)
- Usare la funzione quotename() per nel caso in cui la tabella abbia caratteri particolari
- Far precedere il nome della tabella con il suo schema (dbo), che velocizza le perestazioni
- Precedo le stringhe con **N** per indicare che sono unicode

```sql
SELECT @sql =
N' SELECT @cnt = COUNT(*) FROM dbo.' + quotename(@tbl) +
N' WHERE LastUpdated BETWEEN @fromdate AND ' +
N' coalesce(@todate, ''99991231'')'
```
La seconda è l'esecuzione della query vera e propria.
```sql
SELECT @params = N'@fromdate datetime, ' +
N'@todate datetime = NULL, ' +
N'@cnt int OUTPUT'
EXEC sp_executesql @sql, @params, '20060101', @cnt = @count OUTPUT
```
In questo esempio la SQL dinamica ha tre parametri, uno obbligatorio, uno opzionale e un parametro `OUTPUT`.
In questo caso non specifico il parametro `@todate` in quanto opzionale, ma devo ovviamente chiamare il parametro `@cnt` nominalmente.
Segnalo inoltre che la variabile `@cnt`, come tutte la altre varibili della SQL dinamica, sono visibili solo all'interno della stessa, al contrario non sono visibili le variabili esterne, come `@count`.

## 3. EXEC()
Il comando **EXEC()** prende un solo parametro in ingresso che è una stringa SQL e la esegue.
Il parametro può essere una concatenazione di variabili di stringa, ma non possono racchiudere chiamate a funzioni o altri operatori.
Per casi **molto semplici**, EXEC può essere una soluzione più leggera si `sp_executesql`

## 4. Good Practices
Le query dinamiche rischiano di diventare facilmente disordinate e difficili da gestire, è necessario programmarle in maniera molto ordinata e seguendo alcune semplici indicazioni.

### 4.1 Scrivere un PRINT di DEBUG
Quando sto scrivendo una sotred procedrue che genera SQL dinamico, dovresti **sempre** includere un parametro @debug che permette di printare l'SQL generato, in quanto gli errori di sintassi sono molto frequenti e difficili da trovare.
```sql
CREATE PROCEDURE dynsql_sp @par1 int,
...
@debug bit = 0 AS
...
IF @debug = 1 PRINT @sql
```

### 4.2 Spaziature e formattazione
Un'altra cosa a cui porre attenzione è lo spazio quando concateno parti di una query, prendiamo il seguente esempio:
```sql
EXEC('SELECT col1, col2, col3
FROM' + @tblname + '
WHERE keycol = ''' + @key + '''')
```
Si vede come manca uno spazio dopo il `FROM`. Il problema è che questo codice genera codice SQL **valido**
```sql
SELECT col1, col2, col3
FROMfoo
WHERE keycol = 'abc'
```
in quanto `FROMfoo` è l'alias per `col3`, ed inoltre è legale eseguire un `WHERE` su una `SELECT` anche senza il `FROM`.
Per risolvere questo ed altre problematiche analoghe, è importante utilizzare una buona formattazione. Il metodo migliore è scrivere prima la query come se fosse statica ed in seguito aggiungere i delimitarori di stringa fuori di questa, in modo che anche il PRINT di debug sia efficare e chiaro.

### 5. Casi in cui NON usare SQL dinamiche

#### 5.1 Nomi di tabella o colonna in runtime
```sql
SELECT * FROM @tablename
```
```sql
SELECT * FROM sales + @yymm
```
#### 5.2 Aggiornare il valore di una colonna decisa in run-time
```sql
UPDATE tbl SET @colname = @value WHERE keycol = @keyval
```
Il miglior workaround è
```sql
UPDATE tbl
SET col1 = CASE @colname WHEN 'col1' THEN @value ELSE col1 END,
col2 = CASE @colname WHEN 'col2' THEN @value ELSE col2 END,
...
```
#### 5.3 Determinare il nome in output della colonna in run-time
```sql
SELECT col AS @myname
```
Questa richiesta è gestibile anche senza SQL dinamiche creando una tabella temporanea e poi usando l'`sp_rename` per rinominare la colonna in output in base alla variabile in ingresso.
```sql
DECLARE @mycolalias sysname
SELECT @mycolalias = 'This week''s alias'

CREATE TABLE #temp (a int NOT NULL,
b int NOT NULL)

INSERT #temp(a, b) SELECT 12, 17

EXEC tempdb..sp_rename '#temp.b', @mycolalias, 'COLUMN'

SELECT * FROM #temp
```

#### 5.4 Usare IN con una stringa separata da virgola
Spesso si incorre nell'errore di credere che passando al comando IN una stringa separata da virgola, questo funzioni. Scrivere così
```sql
SELECT * FROM tbl WHERE col IN (@list)
```
In cui `@list='1,2,3,4'`, otterrò un match solo se una colonna contiene la stringa `'1,2,3,4'`.
E' possibile risolvere con l'SQL dinamica ma è una soluzione alquanto debole, inoltre non posso passare `@list` come parametro a` sp_executesql` in quanto dovrei usare un `EXEC()` ed essere aperto a SQL injection.
Ricordo inoltre che `IN` è **estremamente lento per liste di grandi dimensioni**.
Il metodo migliore è eseguire l'unpack della lista in una tabella con una funzione esterna e poi eseguire la sottoquery.

#### 5.5 Ordinamento in run-time
Anche in questo caso posso gestire bene la problematica usando il `CASE` e le SQL statiche.
```sql
SELECT * FROM tbl ORDER BY @col
```
```sql
SELECT col1, col2, col3
FROM dbo.tbl
ORDER BY CASE @col1
WHEN 'col1' THEN col1
WHEN 'col2' THEN col2
WHEN 'col3' THEN col3
END

```
Segnalo che se le colonne di ordinamento non hanno lo stesso tipo, non posso raggrupparle tutte nello stesso `CASE`, invece posso procedere così:
```sql
SELECT col1, col2, col3
FROM dbo.tbl
ORDER BY CASE @col1 WHEN 'col1' THEN col1 ELSE NULL END,
CASE @col1 WHEN 'col2' THEN col2 ELSE NULL END,
CASE @col1 WHEN 'col3' THEN col3 ELSE NULL END
```
