---
tags:
  - Coding
  - SqlServer
---
## 1. JOIN
I join consentono di **recuperare dati da due o più tabelle in base alle relazioni logiche esistenti tra le tabelle stesse**.
Una condizione di join definisce il modo in cui due tabelle sono correlate in una query in base agli elementi seguenti:
* L'impostazione della colonna di ogni tabella da utilizzare per il join. In una condizione di join tipica viene specificata **una chiave esterna di una tabella e la chiave associata nell'altra tabella**.
* L'impostazione dell'**operatore logico** (ad esempio = o <>) da utilizzare per il confronto dei valori delle colonne.

È possibile specificare le condizioni di join sia nelle clausole **FROM** sia nelle clausole **WHERE**. È tuttavia **consigliabile utilizzare la clausola FROM**.
La sintassi per la definizione di un join nella clausola **FROM** è la seguente:
```sql
FROM first-table join-type second-table [ON (join_condition)]
```
*join-type specifica il tipo di join da eseguire*, ovvero inner join, outer join o cross join. join-condition definisce il predicato da valutare per ogni coppia di righe unite in join. Di seguito è riportato un esempio di definizione di join nella clausola **FROM**:
```sql
SELECT pv.ProductID, v.BusinessEntityID, v.Name
FROM Purchasing.ProductVendor AS pv
JOIN Purchasing.Vendor AS v
ON (pv.BusinessEntityID = v.BusinessEntityID)
WHERE StandardPrice > $10
AND Name LIKE N'F%';
```

L'istruzione **SELECT** restituisce informazioni sul prodotto e sul fornitore per ogni combinazione di prodotti con prezzo maggiore di $ 10 fornito da una società il cui nome inizia con la lettera F.

### Tipologie
I join sono suddivisi nelle categorie seguenti:
* **Inner join**: Gli inner join utilizzano un operatore di confronto che abbina le righe di due tabelle in base ai valori delle colonne disponibili in entrambe le tabelle.
* **Outer join**:
- **LEFT JOIN o LEFT OUTER JOIN**: Il set di risultati di un left outer join include **tutte le righe della tabella di sinistra specificata nella clausola LEFT OUTER, non solo le righe in cui esiste una corrispondenza tra le colonne unite in join**. Se a una riga della tabella di sinistra non corrisponde alcuna riga nella tabella di destra, la riga associata nel set di risultati include un valore **Null per tutte le colonne dell'elenco di selezione provenienti dalla tabella di destra**.
- **RIGHT JOIN o RIGHT OUTER JOIN**: Un right outer join è l'opposto di un left outer join, ovvero restituisce tutte le righe della tabella di destra. Per la tabella di sinistra viene restituito un valore Null ogni volta che a una riga della tabella di destra non corrisponde alcuna riga della tabella di sinistra.
- **FULL JOIN o FULL OUTER JOIN**: Un full outer join restituisce **tutte le righe delle tabelle di destra e di sinistra**. Se a una riga di una tabella non corrisponde alcuna riga dell'altra tabella, le colonne dell'elenco di selezione che provengono dalla tabella priva di corrispondenze includono un valore Null. Se invece viene rilevata una corrispondenza tra le due tabelle, l'intera riga del set di risultati include i valori delle tabelle di base.
* **Cross join**: I cross join restituiscono tutte le righe della tabella a sinistra. **Ogni riga della tabella a sinistra viene combinata con tutte le righe della tabella a destra**. I cross join sono detti anche **prodotti cartesiani**.


### Subquery
Una sottoquery è una **query nidificata** in un'istruzione SELECT, INSERT, UPDATE o DELETE o in un'altra sottoquery. È possibile **utilizzare una sottoquery in qualsiasi posizione in cui è consentito inserire un'espressione**
Molte istruzioni Transact-SQL che includono sottoquery possono essere formulate anche come join.
Nell'esempio seguente vengono illustrate un'istruzione SELECT con una sottoquery e un'istruzione SELECT con un join che restituiscono lo stesso set di risultati:
```sql
/* SELECT statement built using a subquery. */
SELECT Name
FROM AdventureWorks2008R2.Production.Product
WHERE ListPrice =
(SELECT ListPrice
FROM AdventureWorks2008R2.Production.Product
WHERE Name = 'Chainring Bolts' );

/* SELECT statement built using a join that returns
the same result set. */
SELECT Prd1. Name
FROM AdventureWorks2008R2.Production.Product AS Prd1
JOIN AdventureWorks2008R2.Production.Product AS Prd2
ON (Prd1.ListPrice = Prd2.ListPrice)
WHERE Prd2. Name = 'Chainring Bolts';
```

* * *

## 2. COALESCE
Il comando **COALESCE** (Standard ANSI) è un comando estremamente comodo che valuta gli argomenti seguendo l'ordine e restituisce il valore corrente della prima espressione che inizialmente non restituisce `NULL`.

```sql
COALESCE ( expression [ ,...n ] )
```
L'espressione `COALESCE` è una **scorciatoia sintattica dell'espressione CASE**. Il codice di `COALESCE(expression1,...n)` viene quindi riscritto da Query Optimizer come la seguente espressione `CASE`:
```sql
CASE
WHEN (expression1 IS NOT NULL) THEN expression1
WHEN (expression2 IS NOT NULL) THEN expression2
...
ELSE expressionN
END
```

Ciò significa che i valori di input (`expression1`, `expression2`, `expressionN` e via di seguito) saranno valutati più volte. Inoltre, in conformità con lo standard SQL, un'espressione di valori che contiene una sottoquery è considerata non deterministica e la sottoquery viene valutata due volte. In entrambi i casi, è possibile che tra la prima valutazione e quelle successive i risultati siano diversi.

#### 2.1 Esempi
##### 2.1.1 Esempio 1
Nell'esempio seguente viene illustrato il modo in cui `COALESCE` seleziona **i dati dalla prima colonna in cui è presente un valore non Null**.
```sql
SELECT Name, COALESCE(Class, Color, ProductNumber) AS FirstNotNull
FROM Product;
```

##### 2.1.2 Esempio 2
COALESCE può essere utilizzato per eseguire query leggermente più complesse come la seguente: ho una tabella `pagamenti` che include tre colonne con informazioni sulla retribuzione annua dei dipendenti, ovvero retribuzione oraria, stipendio e commissione. Un dipendente tuttavia riceve un solo tipo di paga, gli altri due valori saranno impostati correttamente a **NULL**.
Per determinare l'importo totale pagato a tutti i dipendenti, utilizzare la funzione `COALESCE` per ottenere *solo i valori non **NULL*** delle colonne `paga_oraria`, `salario` e `commissione`.

| id | paga_oraria | salario | commissione | numero_vendite |
|--------|--------|--------|--------|--------|
|1 |10 |NULL |NULL |NULL |
|2 |NULL |10000 |NULL |NULL |
|3 |NULL |NULL |15000 |3 |

```sql
SELECT CAST(COALESCE(paga_oraria * 40 * 52, salario, commissione * numero_vendite) AS money) AS 'Salario emesso' FROM pagamenti;
```
Ottengo quindi il seguente output (solo prima colonna)

| Salario emesso ||Spiegazione|
|--------|--------|--------|
|20800,00| -> |10 \* 40 * 52 |
|10000,00| -> |10000|
|45000,00| -> |15000 * 3|


* * *

## 3. I CURSORI (BLOG)
Questo articolo segue direttamente quanto indicato sulla documentazione ufficiale Microsoft sull'utilizzo dei cursori.

### 3.1 Introduzione

Un cursore offre la possibilità di elaborare un set di dati (quindi il risultato di una `SELECT`) una riga alla volta.
Le istruzioni principali sono le sueguenti:

- **DECLARE CURSOR**: definisce gli attributi di un cursore del server Transact-SQL, ad esempio lo scorrimento e la query utilizzata per compilare il set di risultati su cui agisce il cursore.
- **OPEN**: esegue il popolamento del set di risultati e l'istruzione FETCH restituisce una riga dal set di risultati.
- **CLOSE**: rilascia il set di risultati corrente associato al cursore.
- **DEALLOCATE** rilascia le risorse utilizzate dal cursore.

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

### 3.2 Comandi e funzioni
#### 3.2.1 @@FETCH_STATUS
Restituisce lo stato dell'ultima istruzione **FETCH** eseguita su qualsiasi cursore attualmente aperto dalla connessione.

| Valore restituito | Descrizione |
| ------------------------------- |
|0 |L'istruzione FETCH ha avuto esito positivo.|
|-1|L'istruzione FETCH ha avuto esito negativo oppure la riga non è compresa nel set di risultati.|
|-2|La riga recuperata è mancante.|

Viene spesso usata come condizione di uscita del ciclo WHILE:
```sql
WHILE @@FETCH_STATUS = 0
```

##### 3.2.2 @@CURSOR_STATUS
Funzione scalare che consente al chiamante di una stored procedure di determinare se la procedura ha restituito o meno un cursore e un set di risultati per un determinato parametro.
##### 3.2.3 @@CURSOR_ROWS
Restituisce il numero delle righe attualmente risultanti nell'ultimo cursore aperto sulla connessione.

##### 3.2.4 DECLARE CURSOR
*Definisce gli attributi di un cursor*e del server Transact-SQL, ad esempio lo scorrimento e la query utilizzata per compilare il set di risultati su cui agisce il cursore.
La dichiarazione standard di un cursore agisce secondo la sintassi seguente:
```sql
DECLARE cursor_name CURSOR
FOR select_statement
```
In cui *select statement* è l'istruzione SELECT standard che definisce il set di risultati del cursore.
##### 3.2.5 OPEN
*Apre un cursore* server Transact-SQL e popola il cursore mediante l'istruzione Transact-SQL specificata nell'istruzione DECLARE CURSOR o SET cursor_variable.
```sql
OPEN cursor_name
```
##### 3.2.6 FETCH
Recupera una riga specifica da un cursore server Transact-SQL.
Solitamente viene usato nel seguente modo:
```sql
FETCH NEXT
FROM cursor_name
INTO @variable_name
```
- **NEXT**: restituisce la riga del set di risultati successiva alla riga corrente e imposta la riga corrente sulla riga restituita.
- **INTO @variable_name** consente di *inserire in variabili locali i dati delle colonne ottenute da un'operazione di recupero*.

Ogni variabile dell'elenco, da sinistra a destra, è associata alla colonna corrispondente nel set di risultati del cursore.
A ogni variabile deve essere associato lo stesso tipo di dati o un tipo di dati che supporti la conversione implicita dal tipo di dati della colonna corrispondente nel set di risultati.
Il numero di variabili deve corrispondere al numero di colonne dell'elenco di selezione del cursore.

##### 3.2.7 CLOSE
**Chiude un cursore aperto** rilasciando il set di risultati corrente e liberando i blocchi dei cursori mantenuti attivi sulle righe in cui è posizionato il cursore. L'istruzione **CLOSE** mantiene le strutture dei dati disponibili per successive operazioni di apertura. Le operazioni di recupero e di aggiornamento posizionato, tuttavia, sono consentite solo dopo la riapertura del cursore. È necessario eseguire l'istruzione **CLOSE** su un cursore aperto. L'esecuzione non è consentita su cursori solo dichiarati o già chiusi.
```sql
CLOSE cursor_name
```
##### 3.2.8 DEALLOCATE
**Rimuove un riferimento a un cursore**. Dopo che l'ultimo riferimento al cursore è stato deallocato, le strutture di dati che includono il cursore vengono rilasciate da Microsoft SQL Server.
```sql
DEALLOCATE cursor_name
```

## 4. SYNONIM
Un sinonimo è un oggetto di database che viene utilizzato per gli scopi seguenti:
* Fornisce un nome alternativo per un altro oggetto di database, definito oggetto di base, presente su un server locale o remoto.
* Fornisce un livello di astrazione che consente di proteggere un'applicazione client dalle modifiche apportate al nome o alla posizione dell'oggetto di base.

Ad esempio, si consideri la tabella **Employee** di **Adventure Works**, che si trova sul server **Server1**.
Per farvi riferimento da un altro server, **Server2**, un'applicazione client dovrebbe utilizzare il nome composto da quattro parti **Server1.AdventureWorks.Person.Employee**. Inoltre, se la tabella venisse spostata in un altro server, sarebbe necessario *modificare l'applicazione client in modo da riflettere la modifica della posizione*.
Per risolvere entrambi i problemi, è possibile creare su **Server2** il sinonimo **EmpTable** per la tabella **Employee** che si trova su **Server1**.
Per fare riferimento alla tabella **Employee**, l'applicazione client dovrà quindi utilizzare unicamente il nome composto da una parte, **EmpTable**. Inoltre, se la posizione della tabella **Employee** viene modificata, per puntare alla nuova posizione della tabella **Employee** sarà necessario *modificare solo il sinonimo*, **EmpTable**.
Poiché *non esiste un'istruzione ALTER SYNONYM*, è necessario innanzitutto eliminare il sinonimo, **EmpTable**, e quindi *ricrearlo con lo stesso nome ma puntando alla nuova posizione della tabella Employee*.
Un sinonimo appartiene a uno schema e, come gli altri oggetti di uno schema, deve avere un* nome univoco*.
È possibile creare sinonimi per le Stored Procedure, le funzioni e le viste.

L'associazione tra un sinonimo e il relativo oggetto di base avviene *unicamente in base al nome*.
Tutti i controlli relativi all'esistenza, al tipo e alle autorizzazioni per l'oggetto di base sono rimandati alla fase di esecuzione.
L'oggetto di base può pertanto essere *modificato, eliminato o eliminato e sostituito da un altro oggetto con lo stesso nome dell'oggetto di base originale*.
Si consideri, ad esempio il sinonimo **MyContacts** che fa riferimento alla tabella **Person.Contact** di **Adventure Works**. Se la tabella **Contact** viene eliminata e sostituita da una *vista* denominata **Person.Contact**, il sinonimo **MyContacts** farà riferimento alla *vista* **Person.Contact**.
I riferimenti a sinonimi non sono associati a schemi e pertanto è possibile eliminare un sinonimo in qualsiasi momento.
Se si elimina un sinonimo, si corre tuttavia il rischio di lasciare riferimenti inesatti al sinonimo eliminato, che verranno trovati solo in fase di esecuzione.

#### Recupero di informazioni sui sinonimi
La vista del catalogo **sys.synonyms** contiene *una voce per ogni sinonimo incluso in un database specifico*. La vista del catalogo espone i metadati dei sinonimi, ad esempio il nome del sinonimo e il nome dell'oggetto di base.

#### Creare sinonimi
Nell'esempio seguente viene creato un sinonimo per una tabella esistente nel database **AdventureWorks2012**
```sql
GO
CREATE SYNONYM MyAddressType
FOR AdventureWorks2012.Person.AddressType;
GO
```
Nell'esempio seguente viene inserita una riga nella tabella di base cui fa riferimento il sinonimo **MyAddressType**.
```sql
GO
INSERT INTO MyAddressType (Name)
VALUES ('Test');
GO
```
Nell'esempio seguente viene illustrato il modo in cui è possibile fare riferimento a un sinonimo in un'istruzione nel linguaggio SQL dinamico.
```sql
GO
EXECUTE ('SELECT Name FROM MyAddressType');
GO
```

## 6. SET ROWCOUNT
Provoca l'arresto dell'elaborazione della query in SQL Server dopo che è stato restituito il numero di righe specificato.
```sql
SET ROWCOUNT number
```
Per disattivare questa opzione in modo che vengano restituite tutte le righe, specificare **SET ROWCOUNT 0**.
Questa istruzione è analoga a **TOP**, con la differenza che **TOP** deve essere scritto in **tutte** le query, **SET ROWCOUNT** viene invece chiamato su tutte le query sottostanti al comando fino ad una chiamata di **SET ROWCOUNT 0** che ripristina le condizioni iniziali.

## 7. SET NOCOUNT ON
Spegne l'automatismo del count delle righe affette da SQL, da usare sempre nelle SP o comunque in qualsiasi codic che prevede molti SELECT.
```sql
SET ROWCOUNT ON|OFF
```
## 8. WITH - Common Table Expression (BLOG)
Le *Common Table Expression* forniscono una sintassi alternativa per evitare l'accumularsi di query innestate: permettono di creare delle tabelle temporanee basandosi sui risultati di una query, in modo che possano poi essere utilizzati successivamente.
L'espressione di tabella comune è derivata da una query semplice e definita all'interno dell'ambito di esecuzione di un'istruzione `SELECT`, `INSERT`, `UPDATE` o `DELETE`.
```sql
WITH Sales_CTE (
SalesPersonID
, SalesOrderID
, SalesYear
)
AS (
SELECT SalesPersonID
, SalesOrderID
, YEAR(OrderDate) AS SalesYear
FROM Sales.SalesOrderHeader
)
SELECT SalesPersonID
, COUNT(SalesOrderID) AS TotalSales
, SalesYear
FROM Sales_CTE
GROUP BY SalesYear

```

Il vantaggio di usare una CTE invece di una sottoquery è che **il codice prodotto risulta molto più semplice da scrivere e da debuggare**. Inoltre risulta estremamente risuabile nel caso in cui i risultati della CTE vengano usati più volte nella procedura.

### CTE per eseguire una media raggruppata
Per esempio, voglio ottenere il valore medio delle vendite raggruppate per persona. Invece di utilizzare una sottoquery posso rendere più chiaro il procedimento nel seguente modo:
```sql
WITH Sales_CTE (
SalesPersonID
, NumberOfOrders
)
AS (
SELECT SalesPersonID
, COUNT(*)
FROM Sales.SalesOrderHeader
WHERE SalesPersonID IS NOT NULL
GROUP BY SalesPersonID
)
SELECT AVG(NumberOfOrders) AS "Average Sales Per Person"
FROM Sales_CTE;
```


### CTE Ricorsive
Una CTE offre anche la possibilità di poter fare riferimento a se stessa, creando pertanto un'**espressione di tabella comune ricorsiva**.
Questa modalità viene usata spesso per gestire **tabelle che hanno indici riferiti a se stesse**.
Una CTE ricorsiva è costituita da tre elementi:
- **Chiamata della routine**: La prima chiamata della CTE ricorsiva è costituita da uno o più elementi *CTE_query_definitions* uniti in join dagli operatori `UNION ALL`, `UNION`, `EXCEPT` o `INTERSECT`. Poiché queste definizioni di query formano il set di risultati di base della struttura della CTE, vengono dette membri non ricorsivi. Tutte le definizioni di query dei **membri non ricorsivi devono essere posizionate prima della prima definizione del membro ricorsivo** ed è necessario utilizzare un operatore `UNION ALL` per unire in join l'ultimo membro non ricorsivo con il primo membro ricorsivo.
- **Chiamata ricorsiva della routine**: La chiamata ricorsiva include uno o più elementi *CTE_query_definitions* uniti in join tramite operatori `UNION ALL` che fanno riferimento alla CTE stessa. Queste definizioni di query sono dette membri ricorsivi.
- **Controllo della chiusura**: Il controllo della chiusura è implicito. La ricorsione viene arrestata quando dalla chiamata precedente non vengono restituite righe.

#### Pseudocodice
```sql
WITH cte_name ( column_name [,...n] )
AS
(
CTE_query_definition –- Anchor member is defined.
UNION ALL
CTE_query_definition –- Recursive member is defined referencing cte_name.
)
-- Statement using the CTE
SELECT *
FROM cte_name
```
La semantica dell'esecuzione ricorsiva è la seguente:
1. Dividere l'espressione CTE in membri non ricorsivi e ricorsivi.
2. Eseguire il membro o i membri non ricorsivi creando la prima chiamata o set di risultati di base (*T0*).
3. Eseguire il membro o i membri non ricorsivi con *Ti* come input e *Ti+1 *come output.
4. Ripetere il passaggio 3 fino a quando viene restituito un set vuoto.
5. Restituire il set di risultati. Si tratta di un'operazione **UNION ALL di *T0* a *Tn***.

#### Esempio
Nell'esempio seguente viene mostrato un semplice esempio di CTE ricorsiva, con due piedi di ricorsione.
Abbiamo una tabella che indica, per ogni persona, l'ID del suo padre e della sua madre. L'ID si riferisce ad un record della stessa tabella.
```sql
CREATE TABLE #Person (ID INT, NAME VARCHAR(30), Mother INT, Father INT);

INSERT #Person
VALUES (1, 'Sue', NULL, NULL),
(2, 'Ed', NULL, NULL),
(3, 'Emma', 1, 2),
(4, 'Jack', 1, 2),
(5, 'Jane', NULL, NULL),
(6, 'Bonnie', 5, 4),
(7, 'Bill', 5, 4);
```
Voglio creare una procedura che, dato il nome di una persona, fornisca l'elenco ricorsivo di tutti i suoi antenati. La spiegazione della procedura è indicata nei commenti SQL.
```sql
DECLARE @name VARCHAR(30);
SET @name = 'Emma';
-- =============================================
-- Generation è una tabella ricorsiva che contiene una sola colonna: ID
-- Ha due piedi di ricorsione, il padre e la madre
-- =============================================
WITH Generation (ID)
AS (
-- =============================================
-- Piede #1 della ricorsione: madre
-- =============================================
SELECT Mother
FROM #Person
WHERE NAME = @name

UNION

-- =============================================
-- Piede #1 della ricorsione: padre
-- =============================================
SELECT Father
FROM #Person
WHERE NAME = @name

UNION ALL

-- =============================================
-- Prima ricorsione: ottengo il padre della scorsa generazione
-- =============================================
SELECT #Person.Father
FROM Generation AS g
INNER JOIN #Person ON g.ID = #Person.ID

UNION ALL

-- =============================================
-- Seconda ricorsione: ottengo la madre della scorsa generazione
-- =============================================
SELECT #Person.Mother
FROM Generation AS g
INNER JOIN #Person ON g.ID = #Person.ID
)

-- =============================================
-- Chiamata alla ricorsione
-- =============================================
SELECT #Person.ID, #Person.NAME, #Person.Mother, #Person.Father
FROM Generation AS g
INNER JOIN #Person ON g.ID = #Person.ID

IF OBJECT_ID('tempdb..#Person') IS NOT NULL DROP TABLE #Person
```


## 9. NULLIF
Se le due espressioni non sono uguali, la funzione `NULLIF` restituisce il primo argomento `expression`. Se le espressioni sono uguali, `NULLIF` restituisce un valore **NULL** del tipo del primo argomento expression.

```sql
NULLIF ( expression , expression )
```
`NULLIF` è equivalente a un'espressione `CASE` avanzata in cui le due espressioni sono uguali e l'espressione risultante è **NULL**.

```sql
SELECT NULLIF(MakeFlag,FinishedGoodsFlag) AS 'Null if Equal'
FROM Product
```

```sql
SELECT 'Null if Equal' =
CASE
WHEN MakeFlag = FinishedGoodsFlag THEN NULL
ELSE MakeFlag
END
FROM Product
```

* * *

## 10. HAVING
Specifica una **condizione di ricerca per un gruppo o una funzione di aggregazione**. Può essere specificata solo nell'istruzione `SELECT` e viene sempre inclusa in una clausola `GROUP BY`.
```sql
[ HAVING <search condition> ]
```

```sql
SELECT IDTipoMovimento, SUM(PrezzoTotale)
FROM contrattirighe
GROUP BY IDTipoMovimento
HAVING SUM(PrezzoTotale) > 100000.00
ORDER BY IDTipoMovimento ;
```

## 11. OUTPUT
Restituisce le informazioni da (o le espressioni basate su) ogni riga interessata da un'istruzione `INSERT`, `UPDATE`, `DELETE` o `MERGE`. Questi risultati possono essere restituiti all'applicazione di elaborazione per l'utilizzo nei messaggi di errore, l'archiviazione e altri scopi simili dell'applicazione. I risultati possono anche essere inseriti in una tabella o in una variabile di tabella. Inoltre, è possibile acquisire i risultati di una clausola OUTPUT in un'istruzione nidificata INSERT, UPDATE, DELETE o MERGE e inserire tali risultati in una vista o tabella di destinazione.

## 12. MERGE (BLOG)
Esegue operazioni di inserimento, aggiornamento o eliminazione in una tabella di destinazione in base ai risultati di un join con una tabella di origine. È possibile ad esempio sincronizzare due tabelle inserendo, aggiornando o eliminando righe in una tabella in base alle differenze trovate nell'altra tabella.
Uno scenario comune prevede l'**aggiornamento di una o più colonne di una tabella nel caso in cui sia presente una riga corrispondente oppure l'inserimento dei dati come nuova riga nel caso in cui la riga corrispondente non sia presente**. Con l'istruzione `MERGE` è possibile eseguire entrambe le attività in un'**unica istruzione**.
##### UPDATE - INSERT
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

## 13.CHOOSE
Viene restituito l'elemento in corrispondenza dell'indice specificato di un elenco di valori in SQL Server.
Può essere usato per eseguire un mapping tra un numero fornito da una colonna e una determinata stringa: per esempio, assumiamo che abbia una tabella `mesi` definita così
```sql
SELECT CHOOSE ( 3, 'Manager', 'Director', 'Developer', 'Tester' )
--> Developer

```
| Mese |
|--------|
|1|
|2|
|3|
|4|
|5|
|6|
|7|
|8|
|9|
|10|
|11|
|12|

E voglio restituire il nome del mese associato al numero. Invece di fare un `CASE` lunghissimo posso operare nel seguente modo:
```sql
SELECT CHOOSE(Mese, "Gennaio", "Febbraio", "Marzo", ..., "Dicembre" ) from mesi
```
E otterrei una tabella in cui cui al posto dei numeri posso trovare la stringa corrispondente al mese.

* * *
L'istruzione **LIKE** è estremamente usata in T-SQL, spesso però viene limitata all'uso del carattere **%** per indicare una qualsiasi stringa composta da 0 o più caratteri, ignorando che ha alcune potenzialità in più (anche se non raggiunge minimamente la profondità delle espressioni regolari. Per aggiungere le regex ad un SQL Server è necessario usare funzioni CLR come spiegato [qui](http://justgeeks.blogspot.it/2008/08/adding-regular-expressions-regex-to-sql.html)).

I caratteri jolly presenti in T-SQL sono i seguenti

| Carattere | Descrizione |
|--------|--------|
|%|Stringa composta da zero o più caratteri|
|_|Carattere singolo|
|[a-f]|Carattere singolo compreso nell'intervallo (**[a-f]**) o nel set (**[abcdef]**) specificato|
|[^a-f]|Carattere singolo non compreso nell'intervallo (**[^a-f]**) o nel set (**[^abcdef]**) specificato|

Di seguito qualche esempio preso dalla [documentazione ufficiale](https://msdn.microsoft.com/it-it/library/ms179859.aspx)

| Simbolo | Significato |
|--------|--------|
|LIKE '[a-cdf]'|a, b, c, d oppure f|
|LIKE '[ [ ]'|[|
|LIKE 'abc[def]'|abcd, abce e abcf|
|LIKE 'M[^c]'|Comincia con *M* e non è seguito da *c*|

## Pattern in OR
Se devo controllare il match con un pattern o con un altro devo spezzare il like in più chiamate, dato che non esiste il carattere `|`, che invece troviamo nelle regex, la soluzione più semplice è concatenare i filtri in OR a livello di query.
```sql
SET @filter_1 = '%test%'
SET @filter_2 = '%foo%'

SELECT *
FROM BAR
WHERE var LIKE @filter_1
OR var LIKE @filter_2
```

* * *
## 15. NOLOCK: Gli hint di tabella (BLOG)
Gli hint di tabella consentono di modificare il comportamento predefinito di Query Optimizer per la durata dell'istruzione DML (Data Manipulation Language) specificando un metodo di blocco, uno o più indici, un'operazione di elaborazione di query, quale un'analisi di tabella (Table Scan) o una ricerca nell'indice (index Seek), oppure altre opzioni [[1]](https://msdn.microsoft.com/it-it/library/ms187373.aspx).
La sintassi è la seguente:
```sql
WITH ( <table_hint> ) [ [, ]...n ]
```
#### NOLOCK (READUNCOMMITTED)
Questo comando permette di evitare il blocco dei dati dovuti ad una transazione non chiusa.
Spieghiamo il funzionamento di questo comando con un esempio:
La query seguente ritorna tutti i record della tabella `Contact`
```sql
SELECT * FROM Person.Contact
```
Ora assumiamo che vi sia un secondo utente che lancia la query sopra in una transazione (**senza chiuderla**). La query viene completata e i record aggiornati, ma non essendo stata committata i **record su DB sono LOCKED**.
```sql
SELECT * FROM Person.Contact
BEGIN TRAN
UPDATE Person.Contact SET Suffix = 'B'
-- ROLLBACK or COMMIT
```
Conseguentemente se io lancio ancora la query di UPDATE indicata sopra, **questa non terminerà mai**, in quanto l'UPDATE non è stato committato.
Per verificare questo posso usare la stored procedure `sp_who2`
```sql
EXEC sp_who2
```
Che fornisce una serie di informazioni sui processi in atto sul server, in questo caso mi permette di vedere che l'istruzione `SELECT` è stata bloccata (`AWAITING COMMAND`).
Devo o cancellare l'esecuzione della query o eseguire un `COMMIT` o `ROLLBACK` dell'istruzione appena eseguita.
Per evitare il problema dei record bloccati prima di un commit posso usare un` WITH (NOLOCK)` che completerà la query **anche se** i record in questione sono bloccati in quanto un'altra transazione è in esecuzione.
```sql
SELECT * FROM Person.Contact WITH (NOLOCK)
```
Questa operazione esegue una *lettura sporca* (Dirty read) in quanto sto leggendo dei dati che non so se esistono veramente (all'update seguirà un `commit`) o no (all'update seguirà un `rollback`).
Quindi se sto banalmente mostrando dei record posso usare il `NOLOCK` senza preoccupazioni, se però devo lavorare con dei dati **consistenti** allora questa soluzione mi espone al rischio di lavorare con dei dati falsi.
Il comando `NOLOCK` è un sinonimo di `READUNCOMMITED` e possono essere usati equivalentamentemente.
```sql
SELECT * FROM Person.Contact WITH (READUNCOMMITTED)
```
E' da sottolineare il fatto che questi comandi sono compatibili **solo** con un istruzione di `SELECT`.
#### Effetti del NOLOCK
- **Lettura sporca**: come indicato sopra, posso leggere dati che non esistono
- **Righe mancanti**: altre transazioni possono muovere che non hai ancora letto in un posto in cui hai invece appena letto, perdendo conseguentemente tali dati
- **Righe duplicate**: simmetricamente a quanto indicato sopra, posso leggere due volte la stessa riga
- **Leggere versioni multiple della stessa riga**
- **Errori in lettura**: dato che posso poter leggere dei dati che sono stati spostati durante la lettura, potrei incorrere in questo errore: `Could not continue scan with NOLOCK due to data movement.`

Per approfondire consiglio i seguenti articoli:
- http://blogs.sqlsentry.com/aaronbertrand/bad-habits-nolock-everywhere/
- http://sqlperformance.com/2015/04/t-sql-queries/the-read-uncommitted-isolation-level


* * *

## 16. UNION
Combina i risultati di due o più query in un singolo set di risultati che include tutte le righe delle query combinate (in DISTINCT). L'operazione **UNION** è diversa dall'utilizzo di join che combinano le colonne di due tabelle. Per poter fare una operazione di **UNION** è necessario:
* Tutte le query devono includere lo stesso numero di colonne nello stesso ordine.
* I tipi di dati devono essere compatibili.
```sql
query
UNION [ ALL ]
query
```
Se viene aggiunto **ALL** dopo UNION allora anche i duplicati vengono inseriti. 

* * *
## SELECT INTO
L'istruzione **SELECT INTO** consente di creare una nuova tabella e di popolarla con il set di risultati dell'istruzione **SELECT**. Tramite l'istruzione **SELECT INTO** è possibile inserire in un'unica tabella i dati di più tabelle o viste, nonché creare una nuova tabella contenente i dati selezionati da un server collegato.
La struttura della nuova tabella viene definita in base agli attributi delle espressioni dell'elenco di selezione.
Nell'esempio seguente per la creazione della tabella dbo.EmployeeAddresses vengono selezionate sette colonne di diverse tabelle relative a dipendenti e indirizzi.
```sql
SELECT c.FirstName, c.LastName, e.JobTitle, a.AddressLine1, a.City,
sp.Name AS [State/Province], a.PostalCode
INTO dbo.EmployeeAddresses
FROM Person.Person AS c
JOIN HumanResources.Employee AS e
ON e.BusinessEntityID = c.BusinessEntityID
JOIN Person.BusinessEntityAddress AS bea
ON e.BusinessEntityID = bea.BusinessEntityID
JOIN Person.Address AS a
ON bea.AddressID = a.AddressID
JOIN Person.StateProvince as sp
ON sp.StateProvinceID = a.StateProvinceID;
```

 * * *

## INSERT + SELECT e SELECT INTO
Tramite la sottoquery **SELECT** dell'istruzione **INSERT** è possibile inserire in una tabella i valori di una o più tabelle o viste. La sottoquery **SELECT** consente inoltre di inserire più righe contemporaneamente.
```sql
CREATE TABLE MySalesReason (
SalesReasonID int NOT NULL,
Name nvarchar(50),
ModifiedDate datetime);
GO
INSERT INTO MySalesReason
SELECT SalesReasonID, Name, ModifiedDate
FROM AdventureWorks2008R2.Sales.SalesReason
WHERE ReasonType = N'Marketing';
GO
```
Utilizzando **INTO** è possibile snellire notevolmente il processo in quanto non è necessario dichiarare prima la tabella, che verrà automaticamente formata in base ai risultati del **SELECT** (istruzione molto comoda per la creazione di tabelle temporanee). Questo metodo non funziona con le variabili di tabella (@table) ma solo con le tabelle temporanee (#table)
```sql
Select FieldA...FieldN
into #MyTempTable
from MyTable
```

* * * 
## CREATE TABLE
```sql
CREATE TABLE [dbo].[ReclamiPubblicazioneManager] (
[IdReclamoPubblicazioneManager] [int] NOT NULL IDENTITY(1, 1)
, [IdReclamoPubblicazione] [int] NOT NULL
, [IDManager] [int] NOT NULL
)

-- =============================================
-- chiave primaria
-- =============================================
ALTER TABLE [dbo].[ReclamiPubblicazioneManager] ADD CONSTRAINT PK_ReclamiPubblicazioneManager_IdReclamoPubblicazioneManager PRIMARY KEY (IdReclamoPubblicazioneManager)

-- =============================================
-- chiave esterna
-- =============================================
ALTER TABLE [dbo].[ReclamiPubblicazioneManager] ADD CONSTRAINT FK_ReclamiPubblicazioneManager_IDManager FOREIGN KEY ([IDManager]) REFERENCES [dbo].[TRManager] ([IDManager])

-- =============================================
-- vincolo di unicità a coppie
-- =============================================
ALTER TABLE [dbo].[ReclamiPubblicazioneManager] ADD CONSTRAINT UC_ReclamiPubblicazioneManager_IdReclamoPubblicazione_IDManager UNIQUE (
IdReclamoPubblicazione
, IDManager
);
```

* * *
Il seguente articolo utilizza come esempi codici trovati sull'internet, talvolta ripetuti anche in più siti diversi.

Cominciamo con una rapida descrizione del comdando `CASE` in T-SQL; questo ha due comportamenti principali:

### Confronto di un valore con n
Ho l'espressione da valutare subito dopo il `CASE` e i valori con cui confrontarli dopo il `WHEN`
```sql
CASE expression
  WHEN value1 THEN result1
  WHEN value2 THEN result2
  ...
  WHEN valueN THEN resultN
  [
    ELSE elseResult
  ]
END
```
### Espressioni booleane indipendenti
Invece di specificare una singola espressione dopo il CASE, contiene una serie di valori booleani indipendenti tra di loro nelle clausole WHEN
```sql
CASE
  WHEN booleanExpression1 THEN result1
  WHEN booleanExpression2 THEN result2
  ...
  WHEN booleanExpressionN THEN resultN
  [
    ELSE elseResult
  ]
END
```
Di seguito illustriamo esempi di utilizzo del comando `CASE` nel mondo reale:

## Esempi applicativi
### Migliorare l'output di una SELECT
Il caso più semplice dell'utilizzo del `CASE` è migliorare l'outoput di una `SELECT`. Per esempio, assumiamo di avere una colonna che indica il sesso di un dipendente: **M** per maschio e **F** per femmina.
Posso migliorare il risultato di uscita andando a scrivere '*Male*' e '*Female*' utilizzando il `CASE` nel seguente modo:
```sql
SELECT
  FirstName, LastName,
  Salary, DOB,
  CASE Gender
    WHEN 'M' THEN 'Male'
    WHEN 'F' THEN 'Female'
  END
FROM Employees
```
### Fornire descrizioni descrittive
Per esempio, assumiamo di avere una colonna prezzo e voler offrire delle descrizioni parlanti in base al range in cui si trova tale prezzo.
Questo obiettivo può essere facilmente raggiunto con l'istruzione `CASE` nel seguente modo:
```sql
SELECT   ProductNumber, Name, 'Price Range' =
      CASE
         WHEN ListPrice =  0 THEN 'Mfg item - not for resale'
         WHEN ListPrice < 50 THEN 'Under $50'
         WHEN ListPrice >= 50 and ListPrice < 250 THEN 'Under $250'
         WHEN ListPrice >= 250 and ListPrice < 1000 THEN 'Under $1000'
         ELSE 'Over $1000'
      END
FROM Production.Product
ORDER BY ProductNumber;
```
### Fornire un risultato nel caso di valore NULL
Talvolta devo lavorare con colonne che possono essere più o meno valorizzate. Nel caso in cui assumano valore `NULL`, spesso può essere non adeguato fornire in uscita valore `NULL`, meglio gestirlo con una stringa parlante.
```sql
SELECT FirstName, LastName, TelephoneNumber, 'When to Contact' =
     CASE
          WHEN TelephoneSpecialInstructions IS NULL THEN 'Any time'
          ELSE TelephoneSpecialInstructions
     END
FROM Person.vAdditionalContactInfo;
```

### Useguire il CASE con un istruzione di UPDATE
Voglio aggiornare il valore di alcune righe in base al valore delle stesse.
Un primo esempio è una query per il passaggio da abbreviazione a stringa estesa per i valori di una colonna
```sql
UPDATE Customer
SET StateCode = CASE StateCode
          WHEN 'MP'
               THEN 'Madhya Pradesh'
          WHEN 'UP'
               THEN 'Uttar Pradesh'
          WHEN 'DL'
               THEN 'Delhi'
          ELSE NULL
          END
```
Un secondo caso è l'impostazione del valore di determinate colonne in base al valore che avevano prima le stesse. In particolare, se il campo `VacationHours - 10` mi fornisce un valore negativo, allora aumento tale campo di 40, altrimenti solo di 20.

```sql
UPDATE HumanResources.Employee
SET VacationHours =
    ( CASE
         WHEN ((VacationHours - 10.00) < 0) THEN VacationHours + 40
         ELSE (VacationHours + 20.00)
       END
    )
OUTPUT Deleted.BusinessEntityID, Deleted.VacationHours AS BeforeValue,
       Inserted.VacationHours AS AfterValue
WHERE SalariedFlag = 0;
```
La clausola `OUTPUT` viene utilizzata per visualizzare i valori precedenti e successivi alle ferie.

### Usare l'istruzione SET con CASE
Voglio assegnare una variabile in base all'esistenza o meno di un valore in una `SELECT`. Invece di usare il comando `IF` posso scrivere tutto in una sola riga con il comando `CASE`.
```sql
SET @ContactType =
        CASE
            -- Check for employee
            WHEN EXISTS(SELECT * FROM HumanResources.Employee AS e
                WHERE e.BusinessEntityID = @BusinessEntityID)
                THEN 'Employee'

            -- Check for vendor
            WHEN EXISTS(SELECT * FROM Person.BusinessEntityContact AS bec
                WHERE bec.BusinessEntityID = @BusinessEntityID)
                THEN 'Vendor'
        END;
```

### Utilizzare la clausola ROLLUP (BLOG)
Talvolta voglio eseguire una query che mi fornisca dei risultati aggregati di media, min, max... ma anche dei risultati sull'intero rowset senza aggregazione.
Per avere questo risultato SQL Server (ma anche PostgreSQL e MySQL) posso usare la clausola ROLLUP.
Per esempio assumiamo di avere la classica relazione dipartimento, impiegati e salari, vogliamo, per prima cosa, ottenere, per ogni dipartimento, la media dei salari.
Utilizzo la classica clausola GROUP BY in questo modo:
```sql
SELECT Department, AVG(Salary) as AvgSalary
FROM Employees
GROUP BY Department
```
Ottenendo:

| Department | AvgSalary |
|--------|--------|
|Sales|78,500.00|
|Marketing|81,250.00|
|IT|55,000.50|
|Executive|91,900.75|

Voglio, nella stessa query, sapere quale è il salario medio per l'intera compagnia su tutti i dipartimenti: utilizzo la parola chiave `ROLLUP` per eseguire il comando (`AVG` in questo caso) su **tutti i dati indipendentemente dal raggruppamento**.
```sql
SELECT Department, AVG(Salary) as AvgSalary
FROM Employees
GROUP BY Department
WITH ROLLUP
```

| Department | AvgSalary |
|--------|--------|
|Sales|78,500.00|
|Marketing|81,250.00|
|IT|55,000.50|
|Executive|91,900.75|
|NULL|76,662.81|

Notare che è stata aggiunta un'ultima riga che identifica la media totale senza raggruppameno, la cui chiave, che identifica il dipartimento, è **NULL**.
Posso rilevare questa riga e sostituire il NULL con una descrizione più parlante utilizzando, nella `SELECT`, il comando `GROUPING(columnName)` che fornisce valore 1 quando la colonna selezionata è un raggruppamento.
Usando quindi il comando `CASE` posso ottenere l'output desiderato:
```sql
SELECT
CASE
WHEN GROUPING(Department) = 1 THEN 'Company Average'
ELSE Department
END AS Department,
AVG(Salary) as AvgSalary
FROM Employees
GROUP BY Department
WITH ROLLUP
```

| Department | AvgSalary |
|--------|--------|
|Sales|78,500.00|
|Marketing|81,250.00|
|IT|55,000.50|
|Executive|91,900.75|
|Company Average|76,662.81|

* * *

In SQL Server, la ricerca full-text consente a utenti e applicazioni di eseguire q**uery full-text su dati di tipo carattere in tabelle di SQL Server**. Affinché le query full-text possano essere eseguite in una determinata tabella, l'amministratore del database deve prima **creare un indice full-text nella tabella in questione**. L'indice full-text include **una o più colonne** basate su caratteri nella tabella. In queste colonne possono essere presenti i seguenti tipi di dati: char, varchar, nchar, nvarchar, text, ntext, image, xml, o varbinary(max) e FILESTREAM. Ogni indice full-text consente di **indicizzare una o più colonne della tabella** e ciascuna colonna può essere utilizzata con una lingua specifica.
**Attraverso le query full-text è possibile eseguire ricerche linguistiche rispetto ai dati di testo contenuti negli indici full-text, utilizzando parole e frasi in base alle regole di una determinata lingua**, come ad esempio l'inglese o il giapponese. Le query full-text possono contenere semplici parole e frasi oppure più forme di una parola o frase. Una query full-text restituisce **qualsiasi documento contenente almeno una corrispondenza** (nota anche come **riscontro**). Si ottiene una corrispondenza quando un documento di destinazione contiene **tutti i termini** specificati nella query full-text e soddisfa qualsiasi altra condizione di ricerca, come ad esempio **la distanza entro i termini corrispondenti**.

## Funzionalità della ricerca fulltext
Dopo l'aggiunta delle **colonne a un indice full-text**, gli utenti e le applicazioni possono eseguire **query full-text sul testo contenuto all'interno delle colonne**. Queste query possono consentire la ricerca degli elementi seguenti:
* Una o più parole o frasi specifiche (termine semplice)
* Parola o frase in cui le parole iniziano con il testo specificato (termine di prefisso)
* Forme flessive di una parola specifica (termine di generazione)
* Una parola o frase vicina a un'altra parola o frase (termine vicino)
* Sinonimi di una parola specifica (thesaurus)
* Parole o frasi che utilizzano valori ponderati (termine ponderato)
Nelle query full-text viene utilizzato un set ridotto di predicati (**CONTAINS** e **FREETEXT**) e funzioni (**CONTAINSTABLE** e **FREETEXTTABLE**).

##Creazione e gestione di indici full-text
Le informazioni contenute negli indici full-text vengono utilizzate dal motore di ricerca full-text per compilare query full-text che consentono di cercare rapidamente parole o combinazioni di parole specifiche in una tabella. **In un indice full-text vengono archiviate informazioni su parole significative e sulla relativa posizione all'interno di una o più colonne di una tabella di database**. Un indice full-text è un tipo speciale di indice funzionale basato su [[Token]] compilato e gestito dal motore di ricerca full-text per SQL Server. Il processo di compilazione di un indice full-text è diverso da quello di altri tipi di indici. Anziché costruire una struttura ad albero B basata su un valore archiviato in una determinata riga, il motore di ricerca full-text compila una struttura con indici invertito, in pila e compresso basata su singoli [[Token]] dal testo indicizzato. La dimensione di un indice full-text è limitata solo dalle risorse di memoria disponibili del computer in cui viene eseguita l'istanza di SQL Server.
È consentito un solo indice full-text per tabella. Per creare un indice full-text su una tabella, quest'ultima deve contenere una colonna singola, univoca e non Null. È possibile compilare un indice full-text su colonne di tipo **char**, **varchar**, **nchar**, **nvarchar**, **text**, **ntext**, **image**, **xml**, **varbinary** e **varbinary(max)**.
Il processo di creazione e gestione di un indice full-text è definito **popolamento** (noto anche come ricerca per indicizzazione). Sono disponibili tre tipi di popolamento dell'indice full-text:
* popolamento completo
* popolamento basato sul rilevamento delle modifiche
* popolamento incrementale basato su timestamp

### Pattern creazione indice
```sql
CREATE FULLTEXT index ON table_name(fields_name_separates_with comma) KEY index index_name
```
*index_name* è (quasi) sempre la primary key.
Esempio:
```sql
CREATE FULLTEXT index ON table_name(field_1, field_2...) KEY index PK_table_name
```

##### FREETEXTTABLE
È una funzione utilizzata nella clausola FROM di un'istruzione SELECT di Transact-SQL per eseguire una ricerca full-text SQL Server in colonne indicizzate full-text che contengono tipi di dati basati su caratteri. Questa funzione restituisce una tabella con 0 o più righe per le colonne contenenti valori che corrispondono al significato e non solo all'esatta formulazione (grazie al fulltext), del testo specificato in *freetext_string*.
Le query che utilizzano **FREETEXTTABLE** restituiscono **un valore di classificazione per pertinenza (RANK) e una chiave full-text (KEY) per ogni riga**.

```sql
FREETEXTTABLE(table, (column_list), 'freetext_string', top_n_by_rank)
```
Esempio:
```sql
SELECT * FROM FREETEXTTABLE(AnaContatti, (nome, cognome), 'Chiara', 1000)
```

* * *

