---
tags:
  - Coding
  - SqlServer
  - PublishedPosts
---
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