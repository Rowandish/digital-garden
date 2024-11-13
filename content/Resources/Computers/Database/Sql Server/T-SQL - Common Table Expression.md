---
tags:
  - Coding
  - SqlServer
  - PublishedPosts
---
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
