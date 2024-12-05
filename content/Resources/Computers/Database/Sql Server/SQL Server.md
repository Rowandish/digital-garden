SQL Server è un sistema di gestione di database relazionali sviluppato da Microsoft, progettato per archiviare, recuperare e gestire efficacemente grandi quantità di dati utilizzando il linguaggio SQL.
Vantaggi:
* Robustezza
* Performance
* Maturità
* Presenza sul mercato
* Integrazione con sistemi terzi
* Facilità di impiego
* Bassi costi di manutenzione
* Economico
* Ambia divulgazione e documentazione
* Costante crescita

## Componenti

1. **Database Engine**
   - Il componente principale di SQL Server che gestisce l’archiviazione, la gestione e l’elaborazione dei dati.
2. **Server Agent**
   - Strumento di automazione che consente di programmare ed eseguire operazioni di manutenzione, backup e monitoraggio in SQL Server. Assomiglia al `cron` di linux.
3. **Reporting Services**
   - Componente che permette di sviluppare report basati sui dati presenti in SQL Server.
   - Oggi è considerato quasi obsoleto, poiché altre soluzioni di reportistica e visualizzazione dati sono diventate più avanzate e diffuse.
4. **Analysis Services**
   - Strumento per creare e gestire strutture multidimensionali (come cubi o ipercubi) che contengono dati già aggregati provenienti da altre origini.
   - Un tempo molto utile per velocizzare le query analitiche, ma oggi il suo utilizzo è diminuito, grazie a hardware sempre più potente che permette l’elaborazione diretta dei dati senza necessità di pre-aggregazioni.

## Edizioni

- **Enterprise**
    - L’edizione più completa di SQL Server, con funzionalità avanzate.
    - Raramente utilizzata, poiché spesso eccede le necessità della maggior parte delle applicazioni aziendali.
- **Standard**
    - Rappresenta circa il 99% degli utilizzi, offrendo un buon equilibrio tra funzionalità e costo.
    - Limiti di risorse: supporta fino a **25 core** e **256 GB di RAM**.
    - Disponibile con due opzioni di licenza:
        - **Licenza per core**: costa circa 1.500€ per core, con un minimo di 2 core.
        - **Licenza per utente**: costa 250€ per utente, a cui bisogna aggiungere 1.000€ per il motore SQL.
- **Developer**
    - Edizione gratuita destinata agli sviluppatori per creare e testare applicazioni.
    - Molto simile alla Standard in termini di funzionalità, ma non può essere utilizzata in ambienti di produzione.
- **Express**
    - Edizione gratuita, pensata per piccoli progetti e applicazioni di base.
    - Limiti di risorse:
        - Massimo di **10 GB di storage**.
        - Non supporta le query in parallelo.
    - Sconsigliata per ambienti di produzione con grandi quantità di dati, a causa delle limitazioni di performance.

## Istanze

In SQL Server, è possibile avere una o più istanze del database server installate sulla stessa macchina. Questo offre una grande flessibilità, soprattutto in ambienti in cui diverse applicazioni richiedono versioni differenti o configurazioni specifiche di SQL Server.
### Istanza predefinita vs. Named Instance

1. **Istanza predefinita (Default Instance)**:    
    - Quando si installa SQL Server, si può scegliere di installare un'istanza predefinita. Quest'istanza è accessibile semplicemente usando l'indirizzo IP della macchina o il suo nome di rete, senza dover specificare ulteriori dettagli.
    - Di solito, l'istanza predefinita utilizza la porta 1433 per le connessioni TCP/IP, che è anche la porta standard per SQL Server. Se non viene modificata, qualsiasi connessione in arrivo verso questa porta verrà automaticamente instradata verso l'istanza predefinita.
    - Un'istanza predefinita è utile quando si desidera un accesso rapido e semplice, senza la necessità di specificare ulteriori informazioni nel nome del server.
2. **Named Instances (Istanze nominate)**:    
    - Quando si desidera installare più di una versione o configurazione di SQL Server sulla stessa macchina, è necessario ricorrere alle istanze nominate. Ogni istanza nominata deve avere un nome univoco, scelto dall’utente durante l’installazione (ad esempio `ServerName\InstanceName`).
    - Per accedere a un'istanza nominata, è necessario specificare sia il nome della macchina sia il nome dell'istanza (ad esempio `192.168.1.10\NomeIstanza`).
    - Le istanze nominate generalmente utilizzano una porta diversa dalla porta 1433 per evitare conflitti con l'istanza predefinita.

## File di dati e log

Microsoft SQL Server utilizza un'architettura in cui i dati e i log delle transazioni sono separati in file distinti per garantire l'integrità e la sicurezza del database. In pratica, il database SQL Server memorizza i **dati** in file con estensione `.MDF` (Master Data File) e `.NDF` (Secondary Data File), mentre le **operazioni di log** vengono salvate in un file con estensione `.LDF` (Log Data File).
### Funzionamento

1. **Scrittura nel Log di Transazione (LDF)**    
    - Quando un’applicazione scrive o modifica dati nel database, la modifica viene prima registrata nel **log delle transazioni** (file `.LDF`).
    - Il log delle transazioni registra ogni operazione di modifica (ad esempio, `INSERT`, `UPDATE`, `DELETE`) sotto forma di eventi di transazione.
    - In questo modo, ogni modifica al database è tracciata e sequenzialmente memorizzata nel log prima di essere applicata al file di dati (file `.MDF`).
2. **Conferma della Transazione e Persistenza nei Dati (MDF)**    
    - Dopo che la modifica è stata registrata nel log delle transazioni, SQL Server conferma all’applicazione che l’operazione è stata completata. Questo processo è detto **commit** della transazione.
    - Solo in un secondo momento, in modo asincrono, SQL Server applica effettivamente le modifiche ai file di dati `.MDF` tramite un’operazione di scrittura chiamata **checkpoint**.
    - Durante un checkpoint, il sistema sincronizza il contenuto dei file di dati con il log delle transazioni, assicurandosi che tutte le modifiche registrate nel log siano state applicate anche ai dati.
3. **Recupero in Caso di Interruzioni (Recovery)**    
    - In caso di interruzioni del servizio, come un arresto improvviso del server o un’interruzione di corrente, SQL Server può utilizzare il log delle transazioni per mantenere l’integrità del database.
    - Quando il server si riavvia, SQL Server esamina il log delle transazioni e applica qualsiasi modifica che era stata registrata nel log ma non ancora scritta nel file di dati. Questo processo è chiamato **recovery**.
    - Poiché tutte le modifiche sono prima registrate nel log, SQL Server è in grado di ripristinare il database allo stato esatto in cui si trovava prima dell'interruzione, riducendo il rischio di corruzione dei dati.

Per visualizzare il file di log posso usare la query:
```sql
SELECT * FROM fn_dialog(NULL, NULL)
```

## Tipologie di database

SQL Server ha due grosse categorie di database:
* **Database di sistema**
	* **master**: database di sistema che deve necessariamente esistere che include varie informazioni di sistema, tra le quali: gli account di accesso, i server collegati e le impostazioni di configurazione di sistema. Vengono anche registrare le posizioni di tutti gli altri db collegati e le informazioni di inizializzazione di SQL Server.
	* **tempdb**: database temporaneo utilizzato non solo quando finisce la RAM ma anche per caching o operazioni particolari. Viene ricreato ad ogni riavvio di SQL Server.
	* **model**: database modello che viene utilizzato quando creo un nuovo database.
	* **msdb**: sono contenuti tutti i [[T-SQL - Jobs|Jobs]], alert e procedure automatiche avviate dall'agent.
* **Database utente**

## Tipi di dati
### Dati carattere

Il più usato è `nvarchar`, che ha sia una lunghezza variabile che la gestione di caratteri Unicode.

| Tipo     | Descrizione                             | Range di lunghezza                     | Archiviazione                   |
| -------- | --------------------------------------- | -------------------------------------- | ------------------------------- |
| char     | Stringa a lunghezza fissa               | 1 - 8,000 caratteri                    | Fissa, 1 byte per carattere     |
| varchar  | Stringa a lunghezza variabile           | 1 - 8,000 caratteri o `varchar(max)`*  | Variabile, 1 byte per carattere |
| nchar    | Stringa a lunghezza fissa (Unicode)     | 1 - 4,000 caratteri                    | Fissa, 2 byte per carattere     |
| nvarchar | Stringa a lunghezza variabile (Unicode) | 1 - 4,000 caratteri o `nvarchar(max)`* | Variabile, 2 byte per carattere |

### Dati ora e data

I più usati sono `smalldatetime` o `datetime` se voglio una precisione al millisecondo.

| Tipo           | Range                                                                                  | Precisione        | Archiviazione                             |
| -------------- | -------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------- |
| date           | 0001-01-01 to 9999-12-31                                                               | Giorno            | 3 byte                                    |
| datetime       | 1753-01-01 00:00:00.000 to 9999-12-31 23:59:59.997                                     | 3.33 millisecondi | 8 byte                                    |
| datetime2      | 0001-01-01 00:00:00.0000000 to 9999-12-31 23:59:59.9999999                             | 100 nanosecondi   | Da 6 a 8 byte (dipende dalla precisione)  |
| smalldatetime  | 1900-01-01 00:00 to 2079-06-06 23:59                                                   | 1 minuto          | 4 byte                                    |
| time           | 00:00:00.0000000 to 23:59:59.9999999                                                   | 100 nanosecondi   | Da 3 a 5 byte (dipende dalla precisione)  |
| datetimeoffset | 0001-01-01 00:00:00.0000000 to 9999-12-31 23:59:59.9999999 (con offset di fuso orario) | 100 nanosecondi   | Da 8 a 10 byte (dipende dalla precisione) |
### Dati numerici

I dati più utilizzati sono `int` per gli interi e `decimal` per i numeri reali. 

| Tipo     | Range                 | Intervallo                                 | Archiviazione                                           |
| -------- | --------------------- | ------------------------------------------ | ------------------------------------------------------- |
| bigint   | -2^63 to 2^63 - 1     | 64 bit                                     | 8 byte                                                  |
| int      | -2^31 to 2^31 - 1     | 32 bit                                     | 4 byte                                                  |
| smallint | -2^15 to 2^15 - 1     | 16 bit                                     | 2 byte                                                  |
| tinyint  | 0 to 255              | 8 bit                                      | 1 byte                                                  |
| bit      | 0 or 1                | 1 bit                                      | 1 bit                                                   |
| decimal  | -10^38 +1 to 10^38 -1 | Fino a 38 cifre decimali (18,6 più usato). | Da 5 a 17 byte (dipende dalla precisione). Più usato 9. |

## Comandi comodi

* [[T-SQL - Cursori]]
* [[T-SQL - Common Table Expression]]
* [[T-SQL - Merge]]
* [[T-SQL - Rollup]]
 * `SET ROWCOUNT`
  - Limita il numero di righe restituite da una query in SQL Server.
  - Sintassi: `SET ROWCOUNT number`
  - Per ripristinare tutte le righe: `SET ROWCOUNT 0`.
  - Differenza con `TOP`: `SET ROWCOUNT` influisce su tutte le query successive finché non viene reimpostato.
* `SET NOCOUNT ON`
  - Disattiva il conteggio automatico delle righe modificate da ogni istruzione SQL.
  - Utile nelle stored procedure per migliorare le prestazioni.
  - Sintassi: `SET NOCOUNT ON`
- `NULLIF`
  - Restituisce `NULL` se due espressioni sono uguali, altrimenti restituisce la prima espressione.
  - Sintassi: `NULLIF(expression1, expression2)`
- `HAVING`
  - Permette di applicare filtri su aggregazioni (`GROUP BY`), non possibili con `WHERE`.
  - Esempio:
    ```sql
    SELECT IDTipoMovimento, SUM(PrezzoTotale)
    FROM contrattirighe
    GROUP BY IDTipoMovimento
    HAVING SUM(PrezzoTotale) > 100000.00;
    ```
- `OUTPUT`
  - Ritorna informazioni sulle righe modificate da istruzioni `INSERT`, `UPDATE`, `DELETE` o `MERGE`.
  - Utile per tracciare modifiche o archiviare cambiamenti.
- `CHOOSE`
  - Restituisce un valore corrispondente a un indice in una lista.
  - Esempio:
    ```sql
    SELECT CHOOSE(3, 'Manager', 'Director', 'Developer', 'Tester')
    ```
- `UNION`
  - Combina i risultati di più query in un unico set, eliminando i duplicati (per includere i duplicati usa `UNION ALL`).
  - Le query devono avere lo stesso numero e tipo di colonne.
  - Sintassi:
    ```sql
    query1
    UNION
    query2
    ```
- `SELECT INTO`
  - Crea una nuova tabella con i risultati di una query già tipizzata con i nomi dei campi.
  - Sintassi:
    ```sql
    SELECT column1, column2
    INTO NewTable
    FROM SourceTable;
    ```

- `INSERT + SELECT` e `SELECT INTO`
  - `INSERT + SELECT`: inserisce risultati di una query in una tabella esistente.
    ```sql
    INSERT INTO MyTable (column1, column2)
    SELECT column1, column2 FROM SourceTable;
    ```
  - `SELECT INTO`: crea automaticamente una nuova tabella con i risultati della query, utile per tabelle temporanee.
    ```sql
    SELECT column1, column2
    INTO #TempTable
    FROM SourceTable;
    ```


## Importare DB
Esistono due principali modalità per importare un database in SQL Server:
1. **Importazione tramite script SQL**
2. **Restore tramite file binario compresso**

### 1. Importazione tramite script SQL
Per importare un database utilizzando uno script SQL:
- Apri il file dello script SQL in SQL Server Management Studio (SSMS).
- Premi il tasto `F5` per eseguire lo script e importare il database.

### 2. Restore tramite file binario (es. file `.bak`)
La seconda opzione consiste nel ripristinare un database utilizzando un file binario compresso, solitamente un file di backup con estensione `.bak`. Questo file contiene i dati del database, incluse le parti principali:
   - File `.mdf` (contiene i dati principali)
   - File `.ldf` (contiene i log delle transazioni)

#### Procedura di restore in SQL Server:
1. In SQL Server Management Studio, fai clic destro su **Database**.
2. Seleziona **Restore Database**.
3. Nella finestra di ripristino, scegli **Device** e quindi **File**.
4. Naviga per selezionare il file `.bak` da importare.

> **Nota sulle cartelle visibili:** Le cartelle visibili nel selettore dipendono dai permessi dell'utente con cui si è effettuato l’accesso:
   - Se hai effettuato l'accesso con autenticazione SQL Server, vedrai solo alcune cartelle specifiche, come la cartella di SQL Server in **Program Files**.
   - Non saranno visibili altre cartelle utente (ad esempio, `C:\Users\paolo...`) o cartelle di rete, a meno che l'utente con cui sei loggato non abbia i permessi su quei percorsi.

## Alias e sinonimi

- **Sinonimi**: Un sinonimo è un nome alternativo per un oggetto di database (come una tabella, una vista o una stored procedure) che si trova nello stesso database o in un altro database. I sinonimi facilitano l'accesso a oggetti esterni o a oggetti con nomi complessi, permettendo di fare riferimento a un oggetto con un nome più semplice o locale senza modificare la struttura delle query. Supponiamo di avere una tabella `Products` in un database remoto chiamato `InventoryDB`. Creiamo un sinonimo per questa tabella nel nostro database corrente: `CREATE SYNONYM MyProducts FOR InventoryDB.dbo.Products;`
- **Alias**: Un alias è un nome temporaneo assegnato a una colonna o a una tabella all'interno di una singola query per migliorarne la leggibilità o per evitare conflitti di nomi. Gli alias sono specifici della query e non esistono al di fuori di essa. Per esempio, in una `SELECT` puoi creare un alias per una tabella o per una colonna (`AS`) per facilitare la scrittura della query. N.b. : non funzionano gli alias di colonna nella clausola `WHERE`.

## Viste

Le **viste** in SQL Server sono query salvate che agiscono come tabelle virtuali. Una vista rappresenta un set di risultati derivati da una query su una o più tabelle o altre viste. Le viste possono semplificare l'accesso ai dati, migliorare la sicurezza (limitando l’accesso a determinate colonne) e permettere una gestione più semplice delle query complesse.

**Buona norma**: evitare di creare "viste di viste" (cioè, viste basate su altre viste), poiché ciò può ridurre le prestazioni e aumentare la complessità, rendendo più difficile il debug e la manutenzione del database.

### Limiti
* Non è possibile usare la clausola `ORDER BY` senza in `TOP`
* Non è possibile usare una `SELECT INTO` in una view
* Non è possibile usare una clausola `COMPUTE` o `COMPUTE BY`
* Non è possibile fare riferimento a tabelle temporanee o variabili tabella
* Non è possibile nascondere la definizione di una vista

## Stored Procedure

Le **stored procedure** sono blocchi di codice SQL salvati nel database che possono essere eseguiti come un singolo comando. Sono usate per eseguire operazioni complesse, come inserimenti, aggiornamenti, cancellazioni e selezioni di dati, con la possibilità di includere logica condizionale (come `IF` e `WHILE`) e parametri di input/output.
Sono utilizzate su database importanti in quanto sono estremamente più veloci di scrivere codice utilizzando magari un Orm per accedere al DB.
Quindi **non sono il male assoluto** come può sembrare, ma devono essere utilizzate con ragionevolezza nei casi in cui siano indispensabili per avere ottime performance su enormi basi di dati.
Il loro svantaggio è che sono difficilmente versionabili e mantenibili ma se utilizzate con razionalità permettono di ottenere delle performance incredibili, soprattutto su basi di dati importanti.
Esempi:
* Script che girano di notte che sistemano dati e mandano mail nel caso di errori;
* Script che fanno polling su tabelle temp e in base a quello che leggono fanno cose;

### Utilizzare i valori di ritorno

Di default una stored procedure fornisce come codice di uscita 0, se invece si verifica un errore il valore sarà diverso da 0 ovviamente.
Anche noi possiamo assegnare dei valori all’istruzione RETURN, ad esempio RETURN(-100) esce dalla procedura con codice di errore uguale a -100.
Spesso vi è la necessità, in una Stored Procedure, di lavorare con dei valori di ritorno forniti da una altra Stored. Per ottenere ciò esistono tre possibili modalità.

#### Return Value
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

## Variabili
### Dichiarazione
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
In T-SQL le variabili debbono interdirsi come *variabili locali*, cioè hanno significato *solo all’interno del batch* (gruppo o sequenza di istruzioni T-SQL) o della stored procedure nella quale vengono dichiarate , fuori da questo contesto perdono significato. E’ possibile passare variabili da una procedura ad un’altra.

### Assegnamento

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

## Batch SQL e l’istruzione `GO`

Un **batch SQL** è un insieme di comandi SQL inviati come gruppo al server SQL per l’esecuzione. Ogni batch comporta:
- Sincronizzazione tra client e server.
- Parsing, esecuzione dei comandi e invio di un codice di stato di successo o errore al client.

Il comando `GO` non è un'istruzione T-SQL, ma un segnale per il client che separa i comandi in batch distinti, da inviare uno per volta al server.

**Nota**: `GO` funziona singolarmente, dividendo i comandi in batch. Ad esempio:
```sql
DELETE FROM a
DELETE FROM b
DELETE FROM c
```
invio una singola query con tre comandi al server. Invece:
```sql
DELETE FROM a
GO
DELETE FROM b
GO
DELETE FROM c
```
invio tre batch distinti, uno per ogni comando `DELETE`.

Alcuni comandi richiedono un batch dedicato per funzionare correttamente. Ad esempio:
- **`DROP TABLE` e `CREATE TABLE`** (se usati sullo stesso nome).
- Comandi come `CREATE/ALTER PROCEDURE` o `ADD COLUMN` devono essere i primi nel loro batch.

## Profiler
Esiste un profiler che permette di visualizzare tutte le query che vengono effettuate su un determinato database.
Si accede tramite `Tools -> Sql Server Profiler`.
Per debuggare i tempi di esecuzione di una query posso fare `Query -> Include Execution Plan` che aggiunge una terza tab dopo l'esecuzione di una query che mostra ogni operazione della query quanto tempo ci mette.

## Trick

### Concatenare variabili a stringhe
```sql
@sql = 'foo' + CAST(@variable AS NVARCHAR(MAX)) + 'bar';
```

### Eseguire una query se esiste un valore in una tabella
Letteralmente significa "Ritorna 1 dalla tabella" e viene spesso utilizzato in combinazione con `WHERE EXISTS` in modo da verificare (se la select 1 fornisce un risultato) che la tabella esista.
```sql
SELECT * FROM TABLE1 T1 WHERE EXISTS (
SELECT 1 FROM TABLE2 T2 WHERE T1.ID= T2.ID
);
```
Oppure posso usarlo, genericamente, quando voglio verificare che una tabella esista.

### Verificare la presenza di un parametro in ingresso in una Stored
```sql
IF (ISNULL(@fooInt, 0) = 0)
BEGIN
RAISERROR('Invalid parameter: @fooInt cannot be NULL or zero', 18, 0)
RETURN
END
```

### Verificare se un sp_executesql ha dato risultati
Usare il `@@ROWCOUNT` che indica il numero di righe ritornate dall'ultima query eseguita
```sql
EXEC sp_executesql @sql;
IF @@ROWCOUNT = 0
BEGIN
RETURN;
END
```

### Trasformare il risultato di una select in una stringa
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
L'ultimo punto è eliminare la prima virgola, per far ciò utilizzo la funzione `STUFF` che consente di inserire una stringa in un'altra stringa eliminando un numero di caratteri specificato nella posizione iniziale della prima stringa e inserendo la seconda stringa in tale posizione.
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

### Usare SplitFn per ottenere una tabella a partire da una stringa
Nel caso in cui io debba gestire dei campi formati da ID (per esempio) separati da virgola, devo avere un modo per trasformare questi in una tabella in modo da poterla poi usare in delle altre query.
Per questa esigenza viene in soccorso la funzione _Selfcare.SplitFn_ che prende in ingresso una stringa e un separatore fornendo una tabella con i risultati separati.
```sql
SELECT * FROM Selfcare.SplitFn('ciao, come, va', ',')
```

| items |
| ----- |
| ciao  |
| come  |
| va    |

### Concatenare una lista (anche vuota) ad una query
Con il controlla ISNULL appendo il selettore `IN` solo se la lista non è vuota
```sql
DECLARE @sql NVARCHAR(MAX)
SET @sql = 'DELETE FROM dbo.ReclamiSedi WHERE IDReclamo = ' + CONVERT(VARCHAR(10), @IDReclamo)
IF ISNULL(@ListaSedi, '') <> ''
SET @sql = @sql + ' AND IDSede NOT IN (' + @ListaSedi + ')'
EXEC sp_executesql @sql
```

### Fornire una tabella custom come output con una sola SELECT
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

### Inserire un valore in una colonna identità
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

### Eseguire un UNION con ordinamento
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

### UPDATE se esiste, altrimenti INSERT
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
### Cercare tutti gli oggetti modificati meno n giorni fa da me
```sql
SELECT o.modify_date
, o.NAME
FROM sys.objects AS o
INNER JOIN sys.sql_modules AS m ON o.[object_id] = m.[object_id]
WHERE o.modify_date >= DATEADD(day, - 20, GETDATE())
AND m.DEFINITION LIKE '%myName%'
ORDER BY o.modify_date DESC
```

### Cercare tutti gli oggetti modificati meno n giorni fa

Come da titolo, questa query permette di avere informazioni su tutti gli oggetti (quindi viste, stored procedure...) che sono stati modificati meno di un numero arbitrario di giorni fa, nell'esempio seguente 20:
```sql
SELECT o.modify_date, o.name, m.definition
FROM sys.objects AS o
INNER JOIN sys.schemas AS s ON o.[schema_id] = s.[schema_id]
INNER JOIN sys.sql_modules AS m ON o.[object_id] = m.[object_id]
WHERE o.modify_date >= DATEADD(day,-20, GETDATE())
```

### Cercare tutti gli oggetti che contengono una stringa

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

### Cercare tra i nomi di tutte le colonne
Analogamente a quanto descritto sopra, spesso non ho la necessità di sapere se esiste una colonna con un tal nome all'interno del mio DB (sopratutto se questo è di dimensioni molto grandi e difficilmente consultabile).
Per ottenere questa informazione utilizziamo le viste Information Schema, che meriteranno un approfondimento a parte.
```sql
SELECT COLUMN_NAME, TABLE_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME LIKE '%column_name%'
```

### Cercare tutti i processi lanciati da me in questo momento

Lavorando con query complesse spesso nasce la necessità di voler avere sottocontrollo i processi aperti e quante risorse questi stanno utilizzando sul server.
Per poter fare ciò sono dipsonibili delle stored procedure di sistema, come `sp_who`, `sp_who2` e `sp_who4`.
Il codice seguente inserisce i valori forniti dalla stored `sp_who2` in una tabella, in modo che questi possano essere facilmente interrogati con una query.
```sql
DECLARE @ResultSet TABLE (SPID INT, STATUS VARCHAR(100), LOGIN VARCHAR(100), HostName VARCHAR(100), BlkBy VARCHAR(100), DBName VARCHAR(100), Command VARCHAR(100), CPUTime INT, DiskIO INT, LastBatch VARCHAR(100), ProgramName VARCHAR(100), SPID2 INT, REQUESTID INT)
INSERT INTO @ResultSet EXEC sp_who2
SELECT * FROM @ResultSet AS rs WHERE rs.HostName = 'NBMYNAME' AND rs.ProgramName = 'Microsoft SQL Server Management Studio - Query'
```

### Confrontare le colonne della stessa tabella tra due differenti database
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

### Trasformare i risultati di una query in coppia chiave/valore
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
| ------ | ------ |
| Foo    | 100    |
| Foo    | 200    |
| Foo    | 300    |
| Foo    | 400    |
| Foo    | 500    |
### Script onnicomprensivi T-SQL

#### SELECT
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
#### IF
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

## Extra

* [[T-SQL - Condizioni di ricerca dinamiche]]
* [[T-SQL - Tabelle temporanee VS variabili di tabella]]
* [[T-SQL - Usare variabili @ in query]]
* [[T-SQL Information schema]]
* [[T-SQL Ricerca full-text]]

