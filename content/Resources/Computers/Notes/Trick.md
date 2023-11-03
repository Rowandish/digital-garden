---
tags:
  - Coding
  - SqlServer
---


## Concatenare variabili a stringhe
```sql
@sql = 'foo' + CAST(@variable AS NVARCHAR(MAX)) + 'bar';
```

## Eseguire una query se esiste un valore in una tabella
Letteralmente significa "Ritorna 1 dalla tabella" e viene spesso utilizzato in combinazione con `WHERE EXISTS` in modo da verificare (se la select 1 fornisce un risultato) che la tabella esista.
```sql
SELECT * FROM TABLE1 T1 WHERE EXISTS (
SELECT 1 FROM TABLE2 T2 WHERE T1.ID= T2.ID
);
```
Oppure posso usarlo, genericamente, quando voglio verificare che una tabella esista.

## Verificare la presenza di un parametro in ingresso in una Stored
```sql
IF (ISNULL(@fooInt, 0) = 0)
BEGIN
RAISERROR('Invalid parameter: @fooInt cannot be NULL or zero', 18, 0)
RETURN
END
```

## Verificare se un sp_executesql ha dato risultati
Usare il `@@ROWCOUNT` che indica il numero di righe ritornate dall'ultima query eseguita
```sql
EXEC sp_executesql @sql;
IF @@ROWCOUNT = 0
BEGIN
RETURN;
END
```

## Trasformare il risultato di una select in una stringa (BLOG)
Talvolta può capitare l'esigenza di fornire come risultato di una query non una lista di campi, ma un solo campo formato da una lista concatenata, che sono i valori risultanti della query in questione.

Assumiamo di avere una `SELECT` che mi ritorna una colonna di valori, per esempio
```sql
SELECT Field FROM Table
```
Che fornisce:

| Field |
|--------|
| aaa |
| bbb |
| ccc |
| ddd |

Ora voglio concatenare i risultati di questa query in una stringa separata da virgola:
```
aaa,bbb,ccc,ddd
```
Per ottenere questo risultato è necessario seguire il workaround spiegato in seguito.

Per prima cosa utilizzo la funzione **for XML path** modificando la query nel seguente modo:
```sql
SELECT f
FROM ( SELECT Field FROM TABLE ) AS fields
FOR XML PATH('')
, root('ROOTNODE')
, type
```
In questo modo l'output ora è un file XML:
```xml
<ROOTNODE>
<f>aaa</f>
<f>bbb</f>
<f>ccc</f>
<f>ddd</f>
</ROOTNODE>
```
Ora devo eliminare il tag **\<f\>**, per far ciò modifico la query nel seguente modo:

```sql
SELECT ',' + f
FROM ( SELECT Field FROM TABLE ) AS fields
FOR XML PATH('')
, root('ROOTNODE')
, type
```

Ottenendo così:
```xml
<ROOTNODE>,aaa,bbb,ccc,ddd</ROOTNODE>
```
Ora per eliminare anche il **\<ROOTNODE\>** uso la funzione `value` nel seguente modo:
```sql
SELECT (
SELECT ',' + f
FROM (
SELECT Field
FROM TABLE
) AS fields
FOR XML PATH('')
, root('ROOTNODE')
, type
).value('/ROOTNODE[1]', 'nvarchar(max)')

```
Che mi permette di ottenere:
```xml
,aaa,bbb,ccc,ddd
```
L'ultimo punto è eliminare la prima virgola, per far ciò utilizzo la funzione ** STUFF ** che consente di inserire una stringa in un'altra stringa eliminando un numero di caratteri specificato nella posizione iniziale della prima stringa e inserendo la seconda stringa in tale posizione.
```sql
SELECT STUFF((
SELECT ',' + f
FROM (
SELECT Field
FROM TABLE
) AS fields
FOR XML PATH('')
, root('ROOTNODE')
, type
).value('/ROOTNODE[1]', 'nvarchar(max)'), 1, 1, '')
```
Ottenendo finalmente
```
aaa,bbb,ccc,ddd
```
che è il risultato atteso.

## Usare SplitFn per ottenere una tabella a partire da una stringa
Nel caso in cui io debba gestire dei campi formati da ID (per esempio) separati da virgola, devo avere un modo per trasformare questi in una tabella in modo da poterla poi usare in delle altre query.
Per questa esigenza viene in soccorso la funzione _Selfcare.SplitFn_ che prende in ingresso una stringa e un separatore fornendo una tabella con i risultati separati.
```sql
SELECT * FROM Selfcare.SplitFn('ciao, come, va', ',')
```
| items |
|--------|
|ciao|
|come|
|va|


accogliere i risultati
```sql
CREATE TABLE #tmp (FieldName varchar(max), FieldType varchar(max))
INSERT INTO #tmp (FieldName, FieldType) EXEC sp_executesql @sql;
SELECT * FROM #tmp
```

## Concatenare una lista (anche vuota) ad una query
Con il controlla ISNULL appendo il selettore `IN` solo se la lista non è vuota
```sql
DECLARE @sql NVARCHAR(MAX)
SET @sql = 'DELETE FROM dbo.ReclamiSedi WHERE IDReclamo = ' + CONVERT(VARCHAR(10), @IDReclamo)
IF ISNULL(@ListaSedi, '') <> ''
SET @sql = @sql + ' AND IDSede NOT IN (' + @ListaSedi + ')'
EXEC sp_executesql @sql
```

## Fornire una tabella custom come output con una sola SELECT
Il trucco è sfruttare il comando **AS** del **SELECT**:
Se io ho la seguente query:
```sql
SELECT foo FROM bar
```
Il risultato sarà una tabella monocolonna con *n* righe, in cui il titolo della colonna sarà `foo` e come contenuto dei record ci saranno quelli del campo `foo` della tabella `bar`.
Ora se io invece metto nel **SELECT** delle costanti, cosa succede?
```sql
SELECT 1, foo FROM bar
```
In questo caso avrò due colonne: la prima con valore costante 1, la seconda invece come prima. Non avendo utilizzato il comando AS la prima colonna non avreà nessun nome. Se invece faccio
```sql
SELECT 1 AS costante_uno, foo FROM bar
```
Ottengo che il nome della prima colonna sarà "costante_uno".
Ora assumiamo di avere n query che restituiscono 0 o 1 in base al fatto che esista un record, voglio ritornare questi risultati in una nuova tabella con delle colonne nominate come voglio: la soluzione è usare una **SELECT** nel seguente modo:
```sql
SELECT 0 AS col_1
, CASE 
WHEN EXISTS (
SELECT TOP 1 1
...
)
THEN 1
ELSE 0
END AS col_2
```
Ferrà ritornata una tabella con la prima colonna chiamata `col_1` e la seconda `col_2`.
Allo stesso modo posso ritornare, in una SELECT, i risultati di una altra SELECT.
```sql
SELECT 0 AS col_1
, (SELECT TOP 1 foo from bar) AS col_2
```

## Inserire un valore in una colonna identità
Disattivo temporaneamente i controlli sull'autoincrement con il comando `SET IDENTITY_INSERT table_name ON` ed eseguo l'`INSERT`.
Nota bene che devo **obbligatoriamente** elencare le colonne dopo il nome della tabella
e **deve** essere un `INSERT SELECT` e non un `INSERT VALUES`.
In questo esempio viene anche eseguito un controllo sul 

```sql
SET IDENTITY_INSERT table_name ON
INSERT INTO table_name (col_1, col_2)
SELECT T.*
FROM (
SELECT 999 AS dummy_name, 'bar' AS dummy_name_2
) T
WHERE NOT EXISTS (
SELECT 1
FROM table_name 
WHERE col_1 = 999
);
SET IDENTITY_INSERT table_name  OFF
```

## Eseguire un UNION con ordinamento
Quando eseguo una UNION SQL non vuole che le due SELECT da unire presentino un ordinamento. Per risolvere il problema utilizzo il seguente trucco:
```sql
SELECT *
FROM (
SELECT TOP 1 foo AS col_name
FROM table_name
ORDER BY col ASC
) DummyAlias1

UNION ALL

SELECT *
FROM (
SELECT TOP 100 PERCENT bar AS col_name
FROM table_name_2
ORDER BY col DESC
) DummyAlias2
```

## UPDATE se esiste, altrimenti INSERT
Metodo 1 (da eseguire in una transazione):
```sql
UPDATE foo
SET Name = @Name
WHERE UnitMeasureCode = @UnitMeasureCode
IF (@@ROWCOUNT = 0 )
BEGIN
INSERT INTO foo (UnitMeasureCode, Name)
VALUES (@UnitMeasureCode, @Name)
END
```
Metodo 2 (consigliato):
```sql
-- =============================================
-- MERGE: dichiara la tabella da considerare
-- =============================================
MERGE foo
-- =============================================
-- USING: dichiara le variabili da utilizzare e le associa a source.var_1, socurce.var_2
-- =============================================
USING (
SELECT @UnitMeasureCode, @Name
) AS source(UnitMeasureCode, NAME)
-- =============================================
-- ON: clausola WHERE nella tabella foo
-- =============================================
ON (foo.UnitMeasureCode = source.UnitMeasureCode)
-- =============================================
-- WHEN MATCHED: se la clausola ON da TRUE (IF EXISTS SELECT TOP 1 1 FROM foo WHERE foo.UnitMeasureCode = source.UnitMeasureCode)
-- =============================================
WHEN MATCHED
-- =============================================
-- Aggiorna il nome solo nelle colonne considerate
-- =============================================
THEN
UPDATE
SET NAME = source.NAME
-- =============================================
-- Se invece non trova nessun record esegue il normale inserimento
-- =============================================
WHEN NOT MATCHED
THEN
INSERT (UnitMeasureCode, NAME)
VALUES (source.UnitMeasureCode, source.NAME)
```
* * *

## Utilizzare i valori di ritorno di una Stored Procedure (BLOG)

Spesso vi è la necessità, in una Stored Procedure, di lavorare con dei valori di ritorno forniti da una altra Stored. Per ottenere ciò esistono tre possibili modalità.

ù#### Return Value
All'interno della Stored Procedure posso utilizzare la parola chiave **RETURN**, per esempio:
```sql
CREATE PROCEDURE GetMyInt( @Param int)
AS
DECLARE @ReturnValue int
SELECT @ReturnValue=MyIntField FROM MyTable WHERE MyPrimaryKeyField = @Param
RETURN @ReturnValue
END
```
In questo modo posso chiamare la procedura come:
```sql
DECLARE @SelectedValue int
EXEC @SelectedValue = GetMyInt 999
```
Questo metodo però ha due importanti limitazioni:
- Il `RETURN` può fornire **solo valori interi**, `NULL` è convertito a 0 e le stringhe forniscono un errore di `Conversion failed when converting the varchar value to data type int`.
- Il metodo può fornire **un solo** valore di ritorno

#### Output Parameter
In fase di dichiarazione di una procedura posso dichiararne i parametri di OUTPUT, come nel seguente esempio:
```sql
CREATE PROCEDURE GetMyInt( @Param int, @OutValue int OUTPUT)
AS
SELECT @OutValue=MyIntField FROM MyTable WHERE MyPrimaryKeyField = @Param
END
```
La chiamata avviene nel seguente modo:
```sql
DECLARE @SelectedValue int
EXEC GetMyInt 999, @SelectedValue OUTPUT
```
La differenza fondamentale con il metodo indicato sopra è il valore **può essere di qualsiasi tipo**, anche se può essere comunque un solo valore.

#### Result Set
Questo metodo è particolarmente utile quando voglio **fornire un rowset** come output di una procedura e non un solo valore.
Abbiamo la dichiarazione della procedura nel seguente modo:
```sql
CREATE PROCEDURE GetMyInt(@Param int)
AS
SELECT MyIntField FROM MyTable WHERE MyPrimaryKeyField = @Param
END
```
E' importante notare di come questa sia la procedura più "spoglia", non presenta ne un `RETURN` ne un `OUTPUT`, semplicemente una generica `SELECT`.
Per chiamarla scrivo, per esempio:
```sql
DECLARE @ResultSet table (SelectedValue int)
INSERT INTO @ResultSet (SelectedValue)
EXEC GetMyInt @Param
SELECT * FROM @ResultSet
```
Questo metodo risolve entrambe le limitazioni dei metodi precedenti in quanto:
- Posso ritornare un **qualsiasi numero di righe**
- I valori possono essere di **qualsiasi tipo**

Questo approccio necessità della creazione della tabella temporanea **anche se viene ritornato un solo record**.
