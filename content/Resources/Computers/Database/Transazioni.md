---
tags:
  - Database
---
Questo articolo utilizza parte delle informazioni trovate in:
- [Introduzione alle transazioni](http://www.sqlteam.com/article/introduction-to-transactions);
- [Proprietà ACID](https://it.wikipedia.org/wiki/ACID);
- [Transazioni innestate](http://www.codeproject.com/Articles/4451/SQL-Server-Transactions-and-Error-Handling).

## 1.Introduzione
Una transazione è detta una sequenza di operazioni effettuate da una singola unità logica di lavoro.

Se la transazione viene eseguita correttamente, viene eseguito il *commit* di tutte le modifiche dei dati apportate durante la transazione e tali modifiche diventano parte permanente del database. Se si verificano errori durante l'esecuzione della transazione ed è necessario annullarla o eseguirne il *rollback*, verranno cancellate tutte le modifiche dei dati.

Una transazione **deve** avere tutte le quattro proprietà chiave dell'acronimo ACID:

- **Atomicità**: la transazione è indivisibile nella sua esecuzione e la sua esecuzione deve essere o totale o nulla, non sono ammesse esecuzioni parziali;
- **Coerenza**: quando inizia una transazione il database si trova in uno stato coerente e quando la transazione termina il database deve essere in un altro stato coerente, ovvero non deve violare eventuali vincoli di integrità, quindi non devono verificarsi contraddizioni (inconsistenza) tra i dati archiviati nel DB;
- **Isolamento**: ogni transazione deve essere eseguita in modo isolato e indipendente dalle altre transazioni, l'eventuale fallimento di una transazione non deve interferire con le altre transazioni in esecuzione;
- **Durabilità**: una volta che una transazione abbia richiesto un commit work, i cambiamenti apportati non dovranno essere più persi.

## 2. Livelli di isolamento
Sono previsti quattro livelli di isolamento, qui elencati dal meno al più sicuro.

- **Read uncommitted**: consente transazioni in sola lettura, senza bloccare in lettura i dati, conseguentemente una transazione può leggere dati sporchi, perché potrebbero sparire se la transazione che li ha generati abortisce. Vedi approfondimento [qui](http://ilprogrammatorepigro.tumblr.com/post/133459425727);
- **Read committed**: prevede il rilascio immediato dei dati in lettura, ritardando quelli in scrittura, conseguentemente previene il fenomeno delle letture sporche;
- **Repeatable read**: vengono bloccati sia i dati in lettura che quelli in scrittura ma solo sulle ennuple della tabella coinvolte. Questa modalità previene la lettura dei dati quando altre transazioni stanno modificando gli stessi, ma non previene operazioni di INSERT, cioè dati che vengono **aggiunti nella transazione corrente da altre transazioni**, conseguentemente ottengo un numero diverso di righe lanciando la stessa query due volte all'interno della stessa transazione. Queste letture vengono dette **phantom reads**;
- **Serializable**: il più alto livello di sicurezza delle transazioni, con l'utilizzo dei **RANGE lock** previene la lettura, la modifica e l'inserimento di nuovi dati fino a che la transazione corrente non è stata correttamente completata.

## 3. Tipologie di istruzioni

### 3.1 Transazioni con autocommit
La più semplice transazione è una singola istruzione di modifica dati, come la seguente:
```sql
UPDATE Autori
SET Nome = 'John'
WHERE IdAutori = 10
```
Questo tipo di transazione è chiamato **Autocommit transaction**, SQL Server esegue questa serie di operazioni:
1. Scrive in un file di log cosa sta per fare;
2. Effettua effettivamente l'istruzione di update;
3. Scrive nel file di log che ha completato l'operazione.

Se il server fallisce **dopo che una transazione è stata scritta nel file di log**. SQl Server utilizzerà tale log per eseguire un *roll forward* di tale transazione quando questa ricomincerà.

### 3.2 Transazioni esplicite
Per rendere le transazioni più utili dobbiamo inserire due o più istruzioni all'interno di queste.
Queste transazioni sono chiamate **Explicit Transaction**, per esempio:
```sql
BEGIN TRANSACTION 

UPDATE Autori
SET Nome = 'John'
WHERE IdAutori = '10'

UPDATE Autori
SET Nome = 'Marg'
WHERE IdAutori = '8'

COMMIT TRANSACTION
```
Dato che la transazione è esplicita, abbiamo un `BEGIN TRANSACTION ` all'inzio del set di istruzioni ed un `COMMIT TRANSACTION ` alla fine.
- **BEGIN TRANSACTION** Contrassegna il punto di inizio di una transazione locale esplicita ed incrementa la funzione `@@TRANCOUNT` di una unità.
- **COMMIT TRANSACTION**: Contrassegna la fine di una transazione esplicita o implicita completata correttamente. Se il valore di `@@TRANCOUNT` è 1, `COMMIT TRANSACTION` rende permanenti nel database **tutte le modifiche dei dati apportate dall'inizio della transazione**, libera le risorse mantenute attive dalla transazione e decrementa il valore di `@@TRANCOUNT` a 0. Se il valore di `@@TRANCOUNT` è maggiore di 1, `COMMIT TRANSACTION` decrementa il valore di `@@TRANCOUNT` di una sola unità e la transazione rimane attiva.

Ogni istruzione all'interno dei due comandi è considerato come una singola unità logica di lavoro.
Se il sistema fallisce per un qualsiasi motivo dopo il primo update, **nessun UPDATE verrà eseguito**.
Il file di log conterrà un `BEGIN TRANSACTION ` ma nessun `COMMIT TRANSACTION `.
Al posto del `COMMIT` posso esplicitare un `ROLLBACK TRANSACTION`, che esegue il **rollback di una transazione implicita o esplicita fino all'inizio della transazione o fino a un punto di salvataggio**.
L'istruzione `ROLLBACK TRANSACTION` consente di cancellare tutte le modifiche dei dati eseguite dall'inizio della transazione o fino a un punto di salvataggio, nonché di liberare le risorse utilizzate dalla transazione.

#### 3.2.1 Stored Procedure
La maggior parte delle transazioni avverranno all'interno di Stored Procedure.
Consideriamo il seguente esempio:
```sql
CREATE PROCEDURE TranTest1
AS
BEGIN TRANSACTION

-- idAutori=10 esiste già su DB
INSERT INTO Autori(idAutori, Nome, Cognome)
VALUES (
10
, 'Gates'
, 'Bill'
)

UPDATE Autori
SET Nome = 'Johnzzz'
WHERE idAutori = 10

COMMIT TRANSACTION
```
Il problema con questa Stored Procedure è che la transazione indicata non verifica che le operazioni siano andate a buon fine o meno, verifica solo che SQL Server non fallisca tra l'`INSERT` e l'`UPDATE`.

Lanciando questa SP, questa proverà ad inserire un record duplicato nella tabella `Autori`, che fornirà un errore di violazione di chiave primaria; inoltre il messaggio avviserà che *the statement has been terminated*.

Il problema è che la transazione è ancora aperta, conseguentemente l'`UPDATE` verrà eseguito correttamente e SQL Server eseguirà il `COMMIT` della transazione, comportamento assolutamente non voluto.

Il modo corretto di scrivere questa SP è il seguente:

```sql
CREATE PROCEDURE TranTest1
AS
BEGIN TRANSACTION

INSERT INTO Autori (
idAutori
, Nome
, Cognome
)
VALUES (
10
, 'Gates'
, 'Bill'
)

IF @@ERROR <> 0
BEGIN
ROLLBACK TRANSACTION

RETURN 10
END

UPDATE Autori
SET Nome = 'John'
WHERE idAutori = 10

IF @@ERROR <> 0
BEGIN
ROLLBACK TRANSACTION

RETURN 11
END

COMMIT TRANSACTION
```
In questo modo abbiamo il controllo di **ogni istruzione** per verificare se questa fallisca o meno. Se l'istruzione in question fallisce (che posso verificare tramite il controllo che `@@ERROR <> 0`) allora eseguiamo un `ROLLBACK` di quanto eseguito e forniamo un `RETURN` che esce dalla stored procedure.

Sottolineiamo ancora che se non controlliamo gli errori dopo **ogni istruzione atomica all'interno della transazione**, potremmo eseguire impropriamente un `COMMMIT` di tale transazione.

### 3.3 Transazioni implicite
Una nuova transazione viene avviata in modo implicito al termine di una transazione precedente, conseguentemente non devo scrivere nulla per indicare l'inizio di una transazione, ma tutte le transazioni vengono terminate in modo esplicito con un'istruzione `COMMIT` o `ROLLBACK`.
Questa è una modalità di lavoro che deve essere impostata dal *Database Engine* utilizzato.

## 4. Transazioni innestate
SQL Server permette l'utilizzo di transazioni innestate: questo significa che **una nuova transazione può iniziare anche se la precedente non è stata ancora completata**.

Questo viene eseguito semplicemente innestando un `BEGIN TRANSACTION` prima di un `COMMIT` o `ROLLABCK`; l'indicatore `@@TRANCOUNT` indica il numero di transazioni attive in questo momento, quindi il livello di nesting.
Andiamo ora ad analizzare il comportamento dei comandi in base al livello di nesting a cui questi vengono lanciati
### 4.1 COMMIT
Il comando di `COMMIT` ha due comportamenti diversi nel caso in cui questo sia lanciato nella transazione più esterna o meno.
Se viene lanciato nell'ultima transazione, allora effettua le scritture effettive su disco, altrimenti si limita a diminuire il valore di `@@TRANCOUNT` di uno.
Conseguentemente una transazione **non è mai commitatta definitivamente fino a che l'ultimo COMMIT non è stato lanciato**.
### 4.2 ROLLBACK
Il comando di `ROLLBACK` invece lavora **independentemente dal livello di nesting** a cui viene lanciato ed esegue un **ROLLBACK di tutte le transazioni**.
### 4.3 L'asimmetria tra COMMIT e ROLLBACK
Anche se sembra controintuitivo, esiste una ottima motivazione per cui SQL Server lavora in questo modo: se un `COMMIT` innestato effettuasse veramente le scritture su disco, tutti i `ROLLBACK` esterni non potrebbero effettuare effettivamente il ripristino di questi cambiamenti in quanto questi **sarebbero già registrati in modo permanente**.

Questa modalità è detta **asimmetria tra COMMIT E ROLLBACK**.
Consideriamo il seguente esempio:
```sql
-- @@TRANCOUNT = 0
BEGIN TRANSACTION
-- @@TRANCOUNT = 1
DELETE table_1
BEGIN TRANSACTION transaction_name
-- @@TRANCOUNT = 2
DELETE table_2
COMMIT TRANSACTION nested
-- Esegue solo una diminuzione di @@TRANCOUNT di uno
-- @@TRANCOUNT = 1
ROLLBACK TRANSACTION
-- @@TRANCOUNT = 0

SELECT * FROM table_2
```
In questo esempio possiamo notare che il comando di `ROLLBACK` ripristina i valori della tabella `table_2` **anche se è stato eseguito un COMMIT su di essa**.

### 4.4 SAVE TRANSACTION
I savepoint sono un meccaniscmo per **eseguire il ROLLBACK solo di una porzione di una transazione**.
I savepoint definiscono un punto nel codice in cui una transazione può ritornare se parte di una transazione viene annullato.
SQL Server permette di identificare un savepoint mediante il comando `SAVE TRANSACTION`, che non aumenta il valore di `@@TRANCOUNT`, inoltre un `ROLLBACK` ad un savepoint non modifica il valore di `@@TRANCOUNT` (a differenza di un `ROLLBACK` ad una transazione).
Un'istruzione di `ROLLBACK` deve esplicitare il nome del savepoint, altrimenti verrà eseguito il rollback dell'intera transazione.