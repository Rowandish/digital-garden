---
tags:
  - Database
---
I trigger sono degli oggetti di SQL Sever molto simili alle stored procedures, una sorta di **procedura particolare che si attiva automaticamente dopo un determinato evento**.
Gli eventi per i quali si attiva un trigger sono l’esecuzione di una istruzione INSERT / UPDATE / DELETE su una tabella di SQL Server.
Il trigger viene ancorato ad una tabella e qualora si verifichi un evento tra quelli descritti prima si attiva eseguendo il codice T-SQL contenuto al suo interno, in questa parte è il trigger è del tutto simile ad una stored procedure.
I trigger sono utilizzati per diversi scopi nella progettazione di un database, e principalmente:
* per mantenere l’integrità referenziale tra le varie tabelle
* per mantenere l’integrità dei dati della singola tabella
* per monitorare i campi di una tabella ed eventualmente generare eventi ad hoc
* per creare tabelle di auditing per i record che che vengono modificati o eliminati

Un semplice esempio è il seguente:
```sql
CREATE TRIGGER TR_DEL_Employees
ON Employees
FOR DELETE /* , INSERT, UPDATE più azioni contemporaneamente */
AS
INSERT CrologiaImpiegati
SELECT EmployeeID, FirstName, LastName, ‘Eliminato’ AS Azione
FROM deleted
```
Il trigger si attiverà per ogni DELETE riguardante la tabella Employees.
Quando attivato un trigger **lavora su due tabelle particolari chiamate inserted e deleted**: nel caso di una operazione di DELETE la tabella *deleted* conterrà le righe che sono state appena eliminate al contrario con una INSERT la tabella *inserted* conterrà le righe appena inserite.
Nel caso in cui io abbia un UPDATE invece la *deleted* conterrà i dati prima della modifica (le vecchie righe) mentre la *inserted* conterrà i dati dopo la modifica.
N.B. Il contenuto delle colonne con un tipo dato *ntext*, *text* ed *image* non vengono conderati dai triggers perché le tabelle *inserted* e *deleted* non supportano colonne con simili tipi di dato.

### ROLLBACK TRAN

All 'interno di un trigger posso annullare l'operazione di `INSERT`, `UPDATE` o `DELETE` se esistono delle determinate condizioni. In questo caso uso la parola chiave `ROLLBACK TRAN`.

Un esempio è il seguente:
```sql
Use tempdb
GO
CREATE TRIGGER TR_UPD_test
ON t2
FOR INSERT, UPDATE
AS
IF EXISTS(SELECT 1 FROM inserted WHERE valore=’–’) BEGIN
ROLLBACK TRAN /* quella implicita del trigger */
PRINT ‘Errore il valore — non è permesso!!!’
END
GO
```