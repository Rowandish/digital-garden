---
tags:
  - Coding
  - SqlServer
---


SQL Server ha due grosse categorie di database:
* **Database di sistema**
* **Database utente**

All’ interno dei database di sistema SQL Server memorizza tutte le informazioni e gli oggetti necessari al suo funzionamento.
I database di sistema che SQL Server crea al momento dell’installazione sono quattro:

* **MASTER** contiene le informazioni sul server ad alto livello
* **TEMPDB** contiene le tabelle e gli oggetti temporanei
* **MODEL** contiene il modello per la creazione di un database tipo
* **MSDB** informazioni per il funzionamento di SQL Server Agent (Jobs, Web Assistant, ecc..)

In un DB sono contenuti diversi oggetti:

* **Tables**: Memorizzano i dati che inseriamo nel nostro database, sono tra loro in relazione reciproca. Sono fatte da colonne e da righe. Una tabella può avere fino a 1024 colonne e 8092 bytes per riga.
* **Data Type**: Definiscono i tipi di dati che possono essere inseriti nelle colonne, possono essere definiti dall’utente.
* **Constraint**: Servono a rafforzare l’integrità del database.
* **Default**: Assegna valori predefiniti ad una determinata colonna.
* **Rule**: Definiscono vincoli ai dati che vengono inseriti, servono a rafforzare l’integrità del database.
* **Indici**: Servono ad ottimizzare l’accesso ai dati contenuti nelle tabelle.
* **Viste**: Sono tabelle generate con colonne prese da una o più tabelle.
* **Stored Procedures**: Sono set di istruzioni T-SQL, sono dei veri e propri programmi per i databases.
* **Trigger**: Sono procedure memorizzate che si attivano in modo autonomo in base allo scatenarsi di determinati eventi come INSERT, UPDATE, DELETE.

L’insieme degli oggetti di database che costituiscono il database prende il nome di SCHEMA. La progettazione di tutti questi oggetti rappresenta il modello di dati.

Le informazioni che descrivono gli oggetti del database sono chiamate **metadati**.

Ricordiamoci che il creatore del database ne diventa proprietario cioè: database owner (dbo).

Quando facciamo un riferimento ad uno specifico oggetto di un database, abbiamo diversi modi per identificarlo in modo corretto. La stringa di identificazione completa è:

**server.database.propietario.oggetto >> mioserver.pubs.dbo.authors**
Posso avere quindi:
**select * from mioserver.pubs.dbo.authors = select * from authors**

##Tipi di dati
###Dati binari
* **binary[(n)]**: ha una lunghezza fissa e può contenere fino ad 8000 bytes di dati binari
* **varbinary[(n)]**: ha una lunghezza variabile e può contenere fino ad 8000 bytes di dati binari
### Dati carattere
* **char[(n)]**: ha una lunghezza fissa e può contenere fino ad 8000 caratteri ANSI (cioè 8000 bytes)
* **varchar[(n)]**: ha una lunghezza variabile e può contenere fino ad 8000 caratteri ANSI (cioè 8000 bytes)
* **nchar[(n)]**: ha una lunghezza fissa e può contenere fino a 4000 caratteri UNICODE (cioè 8000 bytes, ricordiamo che per i caratteri UNICODE servono 2 bytes per memorizzare un carattere)
* **nvarchar[(n)]**: ha una lunghezza variabile e può contenere fino a 4000 caratteri UNICODE (cioè 8000 bytes, ricordiamo che per i caratteri UNICODE servono 2 bytes per memorizzare un carattere)
### Dati ora e data
* **datetime**: ammette valori compresi dal 1 gennaio 1753 al 31 dicembre 9999 (precisione al trecentesimo di secondo), occupa uno spazio di 8 byte
* **smalldatetime**: meno preciso del precedente (precisione al minuto), ,occupa uno spazio di 4 byte
### Dati monetari
* **money**: Contiene valori monetari da -922337203685477.5808 a 922337203685477.5807 con una precisione al decimillesimo di unità monetaria, occupa 8 bytes di memoria
* **smallmoney**: Contiene valori monetari da – 214748.3648 a 214748.3647 con una precisione al decimillesimo di unità monetaria, occupa 4 bytes di memoria.
### Dati numerici approssimati
* **float[(n)]**: Contiene numeri a virgola mobile positivi e negativi, compresi tra
2.23E-308 e 1.79E308 per i valori positivi e tra -2.23E-308 e -1.79E308 per i valori negativi, occupa 8 bytes di memoria ed ha una precisione di 15 cifre
* **real**: Contiene numeri a virgola mobile positivi e negativi comprese tra 1.18E-38 e 3.40E38 per i valori positivi e tra -1.18E-38 e -3.40E38 per i valori negativi, occupa 4 bytes di memoria ed ha una precisione di 7 cifre
### Dati numerici esatti
* **decimal[(p[, s])]**
* **numeric[(p[, s])]**: decimal e numeric sono sinonimi per SQL Server 7, possono avere valori compresi tra 10^38 – 1 e – 10^38 -1. La memoria che occupano per essere immagazzinati varia a seconda della precisione che utilizziamo per rappresentarli, da un minimo di 2 bytes a un massimo di 17 bytes
* **p** è la precisione, che rappresenta il numero massimo di cifre decimali che possono essere memorizzate (da entrambe le parti della virgola). Il massimo della precisione è 28 cifre.
* **s** è la scala, che rappresenta il numero di massimo di cifre decimali dopo la virgola e deve essere minore od uguale alla precisione.
* **int**: occupa 4 byte di memoria e memorizza i valori da -2147483648 a 2147483647
* **smallint**: occupa 2 byte di memoria e memorizza i valori da -32768 a 32,767
* **tinyint**: occupa 1 byte di memoria e memorizza i valori da 0 a 255

### Dati speciali
* **bit**: tipicamente è usato per rappresentare i flag, vero/false o true/false o si/no, perché può accettare solo due valori 0 o 1. Occupa un bit ovviamente. Le colonne che hanno un tipo dati bit non possono avere valori nulli e non possono avere indici.
* **cursor**: sono usati come varibili in stored proc oppure come parametri di OUTPUT sempre in stored proc, fanno riferimento ai cursori. Possono essere nulli e non possono essere usati con le istruzioni CREATE TABLE.
* **sysname**: una varchar di 128 caratteri ed occupa 256 bytes, viene usato per assegnare i nomi ad ogggetti del database, come tabelle, procedure, triggere, indici, ecc…
* **timestamp**: occupa 8 bytes ed è un contatore incrementale per colonna assegnato automaticamente da SQL Server 7.
* **UNIQUEIDENTIFIER (GUID)**: E’ un identificatore unico a livello globale di 16 byte di lunghezza chiamato anche GUID. E’ generato (molto lentamente) automaticamente da SQL Server.
### Dati text e image
* **text**: un tipo dati a lunghezza variabile, che può memorizzare fino a 2147483647 caratteri.
* **ntext**: come il precedente ma memorizza caratteri UNICODE, quindi fino alla metà del precedente, cioè 1073741823 caratteri.
* **image**: può memorizzare fino a 2147483647 bytes di dati binari, è solitamente usato per le immagini.

## Operatori
### Matematici
I soliti
###Assegnamento
T-SQL ha un fondamentale operatore di assegnamento l’uguale = che può essere usato sia nelle variabili locali che all’interno di una SELECT

```sql
DECLARE @temp INT
SET @temp = 1
GO
SELECT PrimaColonna = ‘xyz’,
SecondaColonna = ProductID
FROM Products
GO
```

###Comparazione
I soliti
###Logici
I soliti
###Concatenazione
Nel T-SQL per concatenare le stringhe si utilizza l’operatore **+**

##Funzioni
### Funzioni per le stringhe
| Funzioni per il parsing ed il calcolo della lunghezza di una stringa | 
| --------------------- | 
| datalength (char_expr) | Ritorna un intero che indica la lunghezza di una stringa. | 
| substring (expression,start, length) | Ritorna una parte di una stringa. | 
| right (char_exp, int_expr) | Recupera _n_ caratteri (indicati da un numero intero) dalla parte destra di una stringa | 
| left (char_exp, int_expr) | Recupera _n_ caratteri (indicati da un numero intero) dalla parte sinistra di una stringa | 
| upper (char_expr) |Converte tutti i caratteri della stringa in maiscolo| 
| lower (char_expr) |Converte tutti i caratteri della stringa in minuscolo.| 
| space (int_expr) |Crea una stringa di spazi, la sua lunghezza è indicata dal numero intero nell’argomento| 
| replicate (char_expr, int_expr) |Ripete una stringa un certo numero di volte, indicato dal numero intero nell’argomento.| 
| stuff (char_exp1, start, length, char_expr2) |Elinima una determinata porzione di stringa sostituendolo con un’altra, partendo da uno specifico punto di partenza.| 
|reverse (char_expr)|Inverte una stringa.| 
|ltrim (char_expr) e rtrim (char_expr)|Ritorna una stringa dopo averla ripulita degli spazi più a sinistra.| 
|ascii (char_expr)|Ritorna il codice ASCII per il carattere più a sinistra della stringa.| 
|char (int_expr)|Converte un intero rappresentante il codice ASCII in una stringa.| 
|charindex ( expression1 , expression2 [ , start_location ] )|Ritorna la posizione di partenza di una stringa all’interno di un’altra stringa, come numero intero.| 
|Patindex ( ‘%pattern%‘ , expression )|Ritorna la posizione di partenza di una pattern all’interno di un’altra stringa, come numero intero.| 
### Funzioni matematiche
| Sono funzioni scalari utili per fare trasformazioni matematiche su input vari (di tipo numerico). | 
| --------------------- |
|abs (numeric_expr)|Valore assoluto di un numero| 
|ceiling (numeric_expr)|Ritorna l’intero più grande od uguale all’espressione numerica di input| 
|rand ‚ (int_expr)|Ritorna un numero float casuale tra 0 e 1| 
### Funzioni per le date
| Servono a lavorare e soprattutto a manipolare le date: | 
| --------------------- |
|getdate ()|Data corrente.| 
|datename(datepart, date_expr)|Ritorna una specifica parte di una data come nome, il valore è una stringa.| 
|datepart (datepart, date_expr)|Ritorna una specifica parte di una data come numero, il valore è un intero.| 
|datediff (datepart, date_expr1, date_expr2)|Ritorna l’intervallo tra due date, la misurazione fa riferimento alla parte di data specificata.| 
|dateadd (datepart, number, date_expr)|Ritorna una nuova data, creata aggiungendo un valore intero ad un data di input, l’aggiunta fa riferimento alla parte di data specificata| 
### Funzioni di sistema

##Le variabili
###Dichiarazione
Ogni variabile utilizzata all’interno di una stored procedure (o di un batch) deve essere *dichiarata assieme al suo datatype* attraverso una istruzione **DECLARE** ed in seguito possiamo assegnarle un valore attraverso una istruzione **SET** o **SELECT**.
Le variabili possono essere dichiare su riga singola:
```sql
DECLARE @VARIABILE_TESTO AS VARCHAR(300)
```
oppure su più linee:
```sql
DECLARE 
@VARIABILE_NUMERO AS INTEGER,
@VARIABILE_TESTO AS CHAR(300),
@ VARIABILE_TESTOUNICODE NVARCHAR(500)
```
In T-SQL le variabili debbono interdersi come *variabili locali*, cioè hanno significato *solo all’interno del batch* (gruppo o sequenza di istruzioni T-SQL) o della stored procedure nella quale vengono dichiarate , fuori da questo contesto perdono significato. E’ possibile passare variabili da una procedura ad un’altra.
###Assegnamento
Per assegnare un valore ad una variabile dopo averla dichiarata dobbiamo usare una istruzione **SET** o **SELECT**, la cui sintassi è la seguente:
```sql
SELECT { @ variabile_locale = espressione } [ ,...n ]
```
L’espressione può essere una qualsiasi altra variabile un numero , una stringa, una data oppure il valore risultante dalla chiamata di altre funzioni valide per SQL Server.
Posso anche fare degli pseudo cicli all'interno del select, nel caso in cui questo ritorni più righe.
```sql
SELECT @au_lname = @au_lname + ‘,’ + au_lname FROM authors 
```
N.B: SQL server quando recupera righe vuote da una SELECT assegna alla variabile il valore che aveva prima dell’istruzione SELECT usata per l’assegnazione, in questo caso il mio nome.

La differenza tra SET e SELECT è che SET può assegnare solo una variabile alla volta mentre la SELECT anche più variabili.

###Viste
Le viste sono delle QUERY memorizzate con un proprio nome che possono essere considerate simili a tabelle virtuali. Sono una via efficace per mostrare informazioni che arrivano da più tabelle.
Le viste sono tabelle virtuali, una volte create quindi è possibile eseguire operazioni sulle stesse, tramite altri comandi SQL, come per esempio un SELECT:
```sql
SELECT * FROM V_ProdottiPerCategoria.
```
####Creazione di una vista
```sql
CREATE VIEW [ < nome_database > . ] [ < proprietario > . ] nome_vista [ ( colonna [ ,...n ] ) ]
[ WITH < attributi_vista > [ ,...n ] ]
AS
istruzione_SELECT
[ WITH CHECK OPTION ]
```
Esempio:
```sql
CREATE VIEW V_ProdottiPerCategoria 
(NomeCategoria,NomeProdotto,Quantità)
AS
SELECT 
Categories.CategoryName,
Products.ProductName,
Products.QuantityPerUnit
FROM Categories
INNER JOIN Products ON Categories.CategoryID = Products.CategoryI
```
####Modifica di una vista
È possibile anche modificare una vista secondo la seguente sintassi:
```sql
ALTER VIEW [ < nome_database > . ] [ < proprietario > . ] nome_vista [ ( colonna [ ,...n ] ) ]
[ WITH < attributi_vista > [ ,...n ] ]
AS
istruzione_SELECT
[ WITH CHECK OPTION ]
```
####Limiti di una vista
#####Non è possibile usare la clausola ORDER BY senza in TOP
Non è possible specificare un ordinamento tramite la clausola ORDER BY per il ROWSET ritornato da una view a meno che non si utilizzi TOP 100 PERCENT, che significa di prendere tutte le righe ritornate dalla vista.
```sql
...
SELECT TOP 100 PERCENT
Categories.CategoryName,
...
```
#####Non è possibile usare una SELECT INTO in una view
#####Non è possibile usare una clausola COMPUTE o COMPUTE BY
#####Non è possibile fare riferimento a tabelle temporanee o variabili tabella
#####Non è possibile nascondere la definizione di una vista

##Batch SQL (istruzione GO)
Un batch è sempre formato da uno o più comandi SQL che vengono inviati ed eseguiti sul server SQL.
Questo implica una sincronizzazione tra client e server, ogni qualvolta viene inviato un batch di comandi a SQL server è richiesto il riconoscimento del client da parte del server , il parsing dei condi inviati, la loro esecuzione e il ritorno di un codice di stato che identifichi lo stato (positivo e negativo) dell’esecuzione del comando inviato.
Il comando GO non è un vero e proprio comando TSQL, è un comando per il programma che si connette al SQL server indicando che tale programma sta per inviare un insieme di comandi da far eseguire al server.
N.b. GO **non** è una istruzione che lavora in coppia, lavora singolamente per **spezzare il batch**. Quindi se scrivo
```sql
DELETE FROM a
DELETE FROM b
DELETE FROM c
```
Invio al server una singola query formata da 3 linee.
Se invece invio:
```sql
DELETE FROM a
GO
DELETE FROM b
GO
DELETE FROM c
```
Invio al server 3 query da una linea ciascuna
Alcuni comandi devono essere eseguiti nel loro batch altrimenti non funzionano, per esempio non posso droppare una tabella e ricrearla con lo stesso nome in una singolo batch.
Oppure altri comandi devono essere i primi nel loro batch, come CREATE/ALTER PROCEDURE o ADD COLUMN.  

##Stored procedure
Le stored procedure rappresentano il “cuore” della programmazione Transact SQL. Sono *gruppi di istruzioni SQL* compattati in un modulo e memorizzati nella cache per un successivo utilizzo. 
Racchiudere il codice SQL all’interno di procedure memorizzate porta due grossi vantaggi rispetto ai batch di codice SQL tradizionale:
* Aumento nella velocità di esecuzione del codice SQL e quindi delle performance generali delle applicazioni.
* Aumento della leggibilità e della portabilità del codice e quindi della scalabilità delle applicazioni.

###Creazione di Stored Procedure
```sql
CREATE PROC [ EDURE ] nome_procedura [ ; numero] 
[ { @parametro tipo_di_dati } 
[ VARYING ] [ = default ] [ OUTPUT ] 
] [ ,...n ] [ WITH 
{ RECOMPILE | ENCRYPTION | RECOMPILE , ENCRYPTION 
} ] 
[ FOR REPLICATION ] 
AS istruzione_sql [ ...n ]
```
Di seguito vi è un esempio per una procedura **p_sel_autore** nel database **pubs**, che ci servirà per recuperare un autore dalla tabella authors in funzione del proprio ID di identificazione:
```sql
Use pubs
Go /*inizio del batch SQL per la creazione della procedura*/
-- La procedura ha come parametro di ingresso @au_id con valore di default stringa vuota
CREATE PROCEDURE dbo.p_sel_autore ( @au_id VARCHAR(11) = ” ) AS
SELECT 
au_lname + ‘ ‘ + au_fname AS Nome
FROM 
authors 
WHERE 
au_id = @au_id
Go /*fine del batch SQL per la creazione della procedura*/
```
N.b. L'operazione di creazione della procedura deve essere sempre in un batch senza niente altro
###Eseguire una Stored Procedure
Ci sono diversi modi per chiamare una procedura
```sql
CREATE PROCEDURE dbo.p_sel_autore2 ( @state VARCHAR(2) , @contract BIT )
```
Nella modalità implicita il nome del parametro di input non viene specificato ed passato correttamente in funzione del suo ordine di chiamata nella procedura
```sql
EXEC dbo.p_sel_autore2 ‘CA’, ’1′
```
Nella modalità esplicita invece il nome del parametro di input viene specificato e passato senza che l’ordine di chiamata nella procedura sia importante
```sql
EXEC dbo.p_sel_autore2 @state = ‘Ca’, @contract = ’1′
```
####Valori di ritorno
Di default una stored procedure fornisce come codice di uscita 0, se invece si verifica un errore il valore sarà diverso da 0 ovviamente.
Anche noi possiamo assegnare dei valori all’istruzione RETURN, ad esempio RETURN(-100) esce dalla procedura con codice di errore uguale a -100.
###Modificare una Stored Procedure
```sql
...
ALTER PROCEDURE dbo.p_sel_autore ( @au_id VARCHAR(11) = ” ) AS
...
```
###Eliminare una Stored Procedure
```sql
DROP PROCEDURE dbo.p_sel_autore
```
###Procedure di sistema
#### sp_help
Permette di avere informazioni sulla procedura (uso, tipo di parametri, ecc…)
```sql
EXEC sp_help nome_della_procedura
```
#### sp_helptext
Permette di avere informazioni sulla procedura (uso, tipo di parametri, ecc…)
```sql
EXEC sp_helptext nome_della_procedura
```
#### sp_depends
Permette di avere informazioni sulla procedura (uso, tipo di parametri, ecc…)
```sql
EXEC sp_depends nome_della_procedura
```
#### sp_rename
Permette di avere informazioni sulla procedura (uso, tipo di parametri, ecc…)
```sql
EXEC sp_rename vecchio_nome_della_procedura, nuovo_nome_della_procedura
```
#### sp_executesql
Esegue un'istruzione o un batch Transact-SQL che può essere riutilizzato più volte o che è stato compilato in modo dinamico. L'istruzione o il batch Transact-SQL può contenere parametri incorporati.
```sql
EXEC sp_executesql @sql_string,
N'@nome_parametro tipo_parametro, @nome_parametro2 tipo_parametro2',
@nome_parametro = "foo",
@nome_parametro2 = "bar"
```
Per chiamare i parametri in ingresso basta che all'interno della query (stringa) sia presente le variabili @nome_parametro e @nome_parametro2, la sostituzione è automatica

##Trigger
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
###ROLLBACK TRAN
All 'interno di un trigger posso annullare l'operazione di INSERT, UPDATE o DELETE se esistono delle determinate condizioni. In questo caso uso la parola chiave `ROLLBACK TRAN`.
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


## Tabelle Temporanee VS variabili di tabella

### Introduzione
Lavorando con SQL Server capiterà stesso che, per risolvere numerosi problemi, sarà necessario immagazzinare i dati in tabelle temporanee. T-SQL offre due diverse modalità per questo scopo, le varibili di tabella e le tabelle temporanee.

La prima differenza da rilevare tra le due modalità è la sintassi: le tabelle temporanee si scrivono con il prefisso **#** (`#tempTable`), mentre le variabili di tabella come tutte le altre variabili, quindi anteponendo **@** (`@tempTable`).

```sql
declare @tmp table (Col1 int, Col2 int);
create table #tmp (Col1 int, Col2 int);
```

Le tabelle temporanee sono normali tabelle SQL che sono memorizzate nel *tempDB*. L'unica differenza tra queste è una normale tabella è che queste non permettono di definire una chiave esterna su di esse.

La variabili di tabella invece non vengono memorizzate in nessun DB e vengono eliminate una volta terminata la sessione.

Di seguito approfondiamo tutte le differenze tra le due.

#### Scope
Le tabelle `#tempTable` possono essere viste da qualsiasi oggetto che viene lanciato nella stessa sessione: quindi se definisco una tabella `#tempTable` nella procedura A, poi questa chiama la procedura B, la procedura B avrà modo di accedere allo stesso modo alla tabella temporanea.

Una volta che la sessione è terminata, la `#tempTable` associata a questa sessione verrà deallocata (ma rimarrà comunque nel datamase temporaneo).

Le variabili `@tempTable` hanno scope limitato alla procedura che le crea, non possono essere chiamate da un'altra procedura nella stessa sessione.
#### SELECT INTO
Con una tabella temporanea `#tempTable` è possibile catturare i risultati di una `SELECT INTO` in una nuova tabella senza che questa sia definita prima e le cui colonne e tipi sono create runtime.
```sql
SELECT * INTO #temp FROM foo
```
Questo non è possibile con una variabile di tabella `@temp`.

#### Scrittura su disco
Entrambe le modalità scrivono su disco con la stessa velocità.

#### Ricompilazione
La ricompilazione è il maggiore vantaggio per le variabili `@table`. Se il set di dati da cui prendo i valori è piccolo e non cambia, conviene sicuramente usare le `@table` che evitano rallentamenti di ricompilazione.

#### Indici particolari
Se voglio scrivere un indice che non può essere creato implicitamente con i vincoli di `UNIQUE` e `PRIMARY KEY`, allora devo per forza utilizzare le variabili `#table` (esempi di questi indici sono quelli non unique, indici filtrati o indici con colonne `INCLUDED`)

#### Numerose operazioni
Se devo ripetutamente aggiungere e eliminare un grande numero di righe dalla tabella, allora conviene (a livello di prestazioni) usare una tabella `#tempTable`.
Ricordiamo che questa supporta l'istruzione `TRUNCATE` (a differenza della @table) che è più efficente del `DELETE`.

#### Transazioni
Le varibiali `@tempTable` non partecipano alle transazioni, questo significa che sono veloci ma meno sicure, per esempio se faccio un `ROLLBACK` i valori delle variabili `@tempTable` non vengono modificati.

#### Eliminazione
Le `#tempTable` devono essere eliminate dopo l'uso (pratica di buona programmazione), le `@tempTable` no in quanto vengono eliminate automaticamente.

Esempio di eliminazione di una tabella temporanea `#tempTable`:
```sql
IF(OBJECT_ID('tempdb..#tempTable') IS NOT NULL) DROP TABLE #tempTable
```

#### Conclusione
Per concludere, se sto lavorando con **un piccolo insieme di dati (numero di righe minore di 100) e che la sorgente da cui questi dati vengono presi non cambia**, conviene usare le variabili `@tempTable`, in tutti gli altri casi `#tempTable`.


* * *

Le viste *Information Schema* sono uno delle tante modalità offerte da SQL Server per ottenere dei metadati. Il vantaggio di utilizzare tale vista è che è presente in quasi tutti i RDMS (è uno standard ANSI), per esempio *Oracle*, *MySQL* e *Postgres* lo supportano.
Queste viste hanno il vantaggio di fornire informazioni indipendenti dalle tabelle interne utilizzate da SQL server o dal RDBMS di riferimento, stando quindi ad un livello di astraziomne superiore.
In questo post approfondiremo le tre principali viste di *Information Schema*, cioò quelle riguardanti le tabelle, le viste e le colonne

### TABLES
Fornisce **una riga per ogni tabella nel database corrente**, in particolare fornisce le seguenti colonne:
- **TABLE_CATALOG**: Nome del database
- **TABLE_SCHEMA**: Nome dello schema che contiene la tabella
- **TABLE_NAME**: Nome della tabella
- **TABLE_TYPE**: Tipo della tabella, può essere o **VIEW** o **BASE TABLE**

##### Esempio
```sql
SELECT *
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME = N'foo'
```

##### Esempio 2
Per ottenere invece l'informazione su **tutti** i database e non solo il corrente è necessario utilizzare la procedura `sp_msforeachdb` con la `sys.tables` nel seguente modo:

```sql
sp_msforeachdb 'SELECT "?" AS dbname, * FROM [?].sys.tables WHERE name="contratti"'
```

### COLUMNS
Fornisce una riga per ogni colonna nel database corrente, in particolare fornisce le seguenti colonne (indico solo le principali)
- **TABLE_CATALOG**: Nome del database
- **TABLE_SCHEMA**: Nome dello schema che contiene la tabella
- **TABLE_NAME**: Nome della tabella
- **COLUMN_NAME**: Nome della colonna
- **ORDINAL_POSITION**: Numero identificativo della stessa
- **COLUMN_DEFAULT**: Valore di default
- **IS_NULLABLE**: YES se la colonna permette anche valori NULL, NO altrimenti

### VIEWS
Fornisce una riga per ogni vista nel database corrente, in particolare fornisce le seguenti colonne (indico solo le principali)
- **TABLE_CATALOG**: Nome del database
- **TABLE_SCHEMA**: Nome dello schema che contiene la tabella
- **TABLE_NAME**: Nome della tabella
- **VIEW_DEFINITION**: Fornisce la definizione della vista, solo se è lunga meno di 4000 caratteri. Altrimenti NULL

##### Esempio: controllare l'esistenza di una vista
Esistono varie query per verificare l'esistenza di una vista (ed analogamente ogni altro oggetto), la soluzione più portabile in quanto (quasi) agnostica al tipo di database è la seguente:
```sql
SELECT count(*)
FROM INFORMATION_SCHEMA.VIEWS
WHERE table_name = 'View'
AND table_schema = 'Schema'
```