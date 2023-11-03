---
tags:
  - Coding
  - SqlServer
  - PublishedPosts
---


## Cercare tutti gli oggetti modificati meno n giorni fa da me
```sql
SELECT o.modify_date
, o.NAME
FROM sys.objects AS o
INNER JOIN sys.sql_modules AS m ON o.[object_id] = m.[object_id]
WHERE o.modify_date >= DATEADD(day, - 20, GETDATE())
AND m.DEFINITION LIKE '%guglielmini%'
ORDER BY o.modify_date DESC
```

## Cercare tutti gli oggetti modificati meno n giorni fa
Come da titolo, questa query permette di avere informazioni su tutti gli oggetti (quindi viste, stored procedure...) che sono stati modificati meno di un numero arbitrario di giorni fa, nell'esempio seguente 20:
```sql
SELECT o.modify_date, o.name, m.definition
FROM sys.objects AS o
INNER JOIN sys.schemas AS s ON o.[schema_id] = s.[schema_id]
INNER JOIN sys.sql_modules AS m ON o.[object_id] = m.[object_id]
WHERE o.modify_date >= DATEADD(day,-20, GETDATE())
```

## Cercare tutti gli oggetti che contengono una stringa
Quante volte può capitare di dover ricercare nel DB tutti gli oggetti che utilizzano una determinata stored, oppure gli oggetti che contengono un commento **TODO** o **TOFIX**.
Esistono numerosi tool per eseguire tali ricerce ma spesso la soluzione più veloce e semplice è la conoscenza delle tabelle di sistema.
```sql
SELECT o.NAME AS Object_Name
, o.type_desc
, o.modify_date
FROM sys.sql_modules m
INNER JOIN sys.objects o ON m.object_id = o.object_id
WHERE m.DEFINITION LIKE '%usp_Config_GetByID%'
ORDER BY o.modify_date DESC
```

## Cercare tra i nomi di tutte le colonne
Analogamente a quanto descritto sopra, spesso non ho la necessità di sapere se esiste una colonna con un tal nome all'interno del mio DB (sopratutto se questo è di dimensioni molto grandi e difficilmente consultabile).
Per ottenere questa informazione utilizziamo le viste Information Schema, che meriteranno un approfondimento a parte.
```sql
SELECT COLUMN_NAME, TABLE_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME LIKE '%column_name%'
```

## Cercare tutti i processi lanciati da me in questo momento
Lavorando con query complesse spesso nasce la necessità di voler avere sottocontrollo i processi aperti e quante risorse questi stanno utilizzando sul server.
Per poter fare ciò sono dipsonibili delle stored procedure di sistema, come `sp_who`, `sp_who2` e `sp_who4`.
Il codice seguente inserisce i valori forniti dalla stored `sp_who2` in una tabella, in modo che questi possano essere facilmente interrogati con una query.
```sql
DECLARE @ResultSet TABLE (SPID INT, STATUS VARCHAR(100), LOGIN VARCHAR(100), HostName VARCHAR(100), BlkBy VARCHAR(100), DBName VARCHAR(100), Command VARCHAR(100), CPUTime INT, DiskIO INT, LastBatch VARCHAR(100), ProgramName VARCHAR(100), SPID2 INT, REQUESTID INT)
INSERT INTO @ResultSet EXEC sp_who2
SELECT * FROM @ResultSet AS rs WHERE rs.HostName = 'NBPGUGLIELMINI' AND rs.ProgramName = 'Microsoft SQL Server Management Studio - Query'
```

## Confrontare le colonne della stessa tabella tra due differenti database
Talvolta può capitare di dover verificare eventuali disallineamenti di colonne per la stessa tabella tra due database diversi (solitamente tra il database di staging e il database di produzione).
Per trovare le differenze a livello di colonne tra due diversi database viene in aiuto la seguente query.
```sql
DECLARE @table_name varchar(50);
SET @table_name = 'calendarioFatturazione';
SELECT 'BillingTLP.dbo.' + c2.table_name AS 'Tabella di riferimento'
, c2.COLUMN_NAME, CAST(c2.data_type AS varchar(30)) + '(' + CAST(c2.character_maximum_length AS varchar(20)) + ')' AS Column_type
FROM BillingTLP.INFORMATION_SCHEMA.COLUMNS c2
WHERE table_name = @table_name
AND c2.COLUMN_NAME NOT IN (
SELECT column_name
FROM BillingTLP_QTYbis.INFORMATION_SCHEMA.COLUMNS
WHERE table_name = @table_name
)
UNION
SELECT 'BillingTLP_QTYbis.dbo.' + c2.table_name AS 'Tabella di riferimento'
, c2.COLUMN_NAME, CAST(c2.data_type AS varchar(30)) + '(' + CAST(c2.character_maximum_length AS varchar(20)) + ')' AS Column_type
FROM BillingTLP_QTYbis.INFORMATION_SCHEMA.COLUMNS c2
WHERE table_name = @table_name
AND c2.COLUMN_NAME NOT IN (
SELECT column_name
FROM BillingTLP.INFORMATION_SCHEMA.COLUMNS
WHERE table_name = @table_name
)
```

## Trasformare i risultati di una query in coppia chiave/valore
In questo brevissimo articolo spiegherò come trasformare i risultati di una qualsiasi query in una coppia chiave/valore, dove la chiave è il nome della colonna e il valore il valore effettivo.
Questa può essere utile nel caso abbia una tabella che abbia valorizzato dei campi con **nomi di colonne** di un'altra tabella, e abbia la nece3ssità di andare in **JOIN** su queste.
Prendiamo ora la seguente query, molto semplice:
```sql
SELECT Foo FROM Bar
```
Che fornisce

| Foo |
|--------|
|100|
|200|
|300|
|400|
|500|

Per trasformare questo risultato in una coppia chiave valore, utilizzo la funzione **UNPIVOT** (che eventualmente spiegherò in un altro post).
```sql
SELECT Key, Value
FROM Bar
UNPIVOT(Valore FOR Chiave IN (Foo))
```
| Chiave | Valore |
|--------|--------|
|Foo|100|
|Foo|200|
|Foo|300|
|Foo|400|
|Foo|500|

## Script onnicomprensivi T-SQL

## SELECT
```sql
SELECT
-- =============================================
-- selezione di colonna standard
-- =============================================
foo
-- =============================================
-- Selezione di colonna cambiando il nome della colonna ritornata
-- =============================================
, foo_2 AS changed_name_col
-- =============================================
-- colonna impostata sempre a 'const'
-- =============================================
, 'const' AS const_col
-- =============================================
-- colonna impostata sempre a NULL
-- =============================================
, NULL AS Nome
-- =============================================
-- concatenare campi string con campi interi
-- =============================================
, string_field + CAST(int_field AS VARCHAR(20)) + '$' + CAST(int_field_2 AS VARCHAR(20)) + '$'
-- =============================================
-- colonna booleana che dipende dall'esistenza o meno di un valore in una altra tabella
-- =============================================
, CASE 
WHEN EXISTS (
SELECT TOP 1 1
FROM bar
WHERE foo = 1
)
THEN 1
ELSE 0
END AS boolean_col_exists
-- =============================================
-- valore booleano nel caso in cui una colonna non sia null e una seconda colonna sia LIKE una variabile
-- =============================================
, CASE 
WHEN field_name IS NOT NULL
AND (field_name_2 LIKE '%' + @var + '%')
THEN 1
ELSE 0
END AS boolean_col_like
-- =============================================
-- colonna che viene popolata tramite un SELECT da una altra tabella
-- =============================================
, (
SELECT TOP 1 foo
FROM bar
) AS select_col
-- =============================================
-- il valore della colonna è una concatenazione di valori di colonna con costanti
-- =============================================
, field + CASE another_field
WHEN 2
THEN ' [chiuso]'
WHEN 3
THEN ' [riaperto]'
ELSE ''
END AS concatenated_col
-- =============================================
-- conversione da NULL/stringa a booleani 0/1
-- =============================================
, CASE 
WHEN field_that_could_be_null IS NULL
THEN 0
ELSE 1
END AS boolean_col_if_null
-- =============================================
-- cambio il valore della colonna in base al valore della sua prima lettera
-- =============================================
, CASE 
WHEN LEFT(field_name, 1) = '!'
THEN SUBSTRING(field_name, 2, LEN(field_name) - 1)
ELSE field_name
END AS first_letter_col
-- =============================================
-- colonna stringa booleana (M/F) in base al valore di una sottostringa di un campo iniziale
-- =============================================
, CASE 
WHEN CAST(SUBSTRING(field_name, 10, 2) AS INT) > 40
THEN 'F'
ELSE 'M'
END AS
-- =============================================
-- metto i valori di un campo o di un altro in base all'uguaglianza o meno di due variabili
-- =============================================
, CASE 
WHEN (@var_1 = @var_2)
THEN field_name_1
ELSE field_name_2
END AS col_that_depends_on_var_values
-- =============================================
-- Solo quando l'app name è un determinato valore (Connection string: Application Name=fo;)
-- =============================================
, CASE 
WHEN app_name() = 'fo'
THEN foo
ELSE NULL
END AS Utente
-- =============================================
-- il valore della colonna è la concatenzazione dei valori da una altra tabella
-- =============================================
, (
SELECT STUFF((
SELECT ',''' + CAST(field_to_concatenate AS VARCHAR) + ''''
FROM table_with_field_that_have_to_be_concatenated
FOR XML PATH('')
, root('ROOTNODE')
, type
).value('/ROOTNODE[1]', 'nvarchar(max)'), 1, 1, '')
) AS concatenated_col
FROM bar
-- =============================================
-- confronto il valor di un campo in base al valore di una variabile
-- =============================================
WHERE bar_2 = CASE 
WHEN @local_var = 10
THEN 1
ELSE 0
END
-- =============================================
-- il valore del campo non deve esistere in una altra tabella
-- =============================================
AND (
field_name NOT IN (
SELECT foo
FROM bar
)
)
-- =============================================
-- confronto date validità con la data attuale
-- =============================================
AND GetDate() BETWEEN ValidoDal
AND ValidoAl
-- =============================================
-- Ordinamento custom: Quelle che si chiamano 'Aperto' vanno per prime, e così via
-- =============================================
ORDER BY CASE col
WHEN 'Aperto'
THEN 1
WHEN 'Chiuso'
THEN 2
ELSE 3
END
```

### SP_EXECUTESQL
```SQL
DECLARE @sql NVARCHAR(MAX)

-- =============================================
-- @ListaSedi può essere NULL o una stringa di valori separati da virgola
-- =============================================
SET @sql = 'DELETE FROM dbo.ReclamiSedi WHERE IDReclamo = ' + CONVERT(VARCHAR(10), @IDReclamo)
IF ISNULL(@ListaSedi, '') <> ''
SET @sql = @sql + ' AND IDSede NOT IN (' + @ListaSedi + ')'

-- =============================================
-- popolo la SELECT con i campi (separati da virgola) ottenuti da una seconda query
-- =============================================
SET @sql = 'SELECT IDReclamo ,' + (
SELECT STUFF((
SELECT ',' + f
FROM (
SELECT FieldName AS f
FROM aid_indiciconfig
WHERE desttable = 'AID_Ticket'
AND @IdMotivoReclamo IN (
SELECT *
FROM Selfcare.SplitFn(FilterKey, ',')
)
UNION
SELECT NomeCampoDb AS f
FROM dbo.ReclamiPubblicazioneVoceWeb
WHERE IdReclamoPubblicazione = @IdReclamoPubblicazione
) AS fields
FOR XML PATH('')
, root('ROOTNODE')
, type
).value('/ROOTNODE[1]', 'nvarchar(max)'), 1, 1, '')
) + ' FROM dbo.AID_Ticket WHERE IDReclamo = ' + CAST(@IDReclamo AS NVARCHAR(MAX));


-- =============================================
-- esecuzione monoriga, parametri:
-- 1 - query (in cui le varibili vengono impostate con il @)
-- 2 - definizione del tipo delle variabili 
-- 3..n - assegnazione dei valori alle varibili
-- =============================================
EXEC sp_executesql N' INSERT INTO AID_ContrattiRighe(IDRigaContratto,DATUMO,RecessoInviato) SELECT @p2, GETDATE(), @p1'
, N'@p1 int,@p2 int'
, @p1 = @RecessoInviato
, @p2 = @IDRigaContratto

EXEC sp_executesql @sql
```

### IF
```sql
-- =============================================
-- se esiste alemno un record in una tabella
-- =============================================
IF EXISTS(SELECT TOP 1 1 FROM foo WHERE bar = @var)
-- =============================================
-- Se una variabile è uguale al risultato di una SELECT
-- ============================================= 
IF @var_2 = ( SELECT TOP 1 foo FROM bar WHERE field_= @var )
-- =============================================
-- controllo l'esistenza di variabili
-- =============================================
IF ISNULL(@string_var, '') = ''
IF ISNULL(@int_var, 0) = 0
-- =============================================
-- controlla se i risultati di un SELECT sono un sottoinsieme dei risultati di una seconda query
-- =============================================
IF (SELECT foo FROM bar WHERE field_name = 'string') IN (SELECT DISTINCT field_1 From bar_1 where id = @var)
-- =============================================
-- Se una variabile non è settata la setto a 1 se esiste una config corrispondente, altrimenti 0
-- =============================================
IF ISNULL(@bool_var, 0) = 0
BEGIN
SET @bool_var = CASE WHEN EXISTS (SELECT TOP 1 1 FROM dbo.Config WHERE IDConfig = 'OENext_BancheMultiple' AND VConfig = '1') THEN 0 ELSE 1 END;
END
-- =============================================
-- Se il numero di record forniti da una query è > di k
-- =============================================
IF ( SELECT COUNT(*) FROM foo WHERE bar=@var ) > 10
-- =============================================
-- Se il valore di ritorno di una SELECT è null
-- =============================================
IF ( SELECT TOP 1 ISNULL(field_that_could_be_null, '') FROM bar ) = ''
-- =============================================
-- Confronto una parte di una stringa con un intero
-- =============================================
IF(CAST(SUBSTRING(@CFisc, 10, 2) AS INT) > 40)
```

### TRANSACTION
```sql
BEGIN TRANSACTION;
BEGIN TRY
...
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
ROLLBACK TRANSACTION;
END CATCH
```

### CASE
```sql
SET @ContactType = CASE 
-- Check for employee
WHEN EXISTS (
SELECT *
FROM HumanResources.Employee AS e
WHERE e.BusinessEntityID = @BusinessEntityID
)
THEN 'Employee'
-- Check for vendor
WHEN EXISTS (
SELECT *
FROM Person.BusinessEntityContact AS bec
WHERE bec.BusinessEntityID = @BusinessEntityID
)
THEN 'Vendor'
END;

SELECT CASE GenereShort
WHEN 'M'
THEN 'Male'
WHEN 'F'
THEN 'Female'
END AS Genere CASE 
WHEN ListPrice = 0
THEN 'Mfg item - not for resale'
WHEN ListPrice < 50
THEN 'Under $50'
ELSE 'Over $50'
END AS Prezzo CASE 
WHEN TelephoneSpecialInstructions IS NULL
THEN 'Any time'
ELSE TelephoneSpecialInstructions
END AS
FROM Employees
```