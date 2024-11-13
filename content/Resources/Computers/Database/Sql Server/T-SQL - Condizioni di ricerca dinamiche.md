---
tags:
  - Coding
  - SqlServer
  - PublishedPosts
---
_ _ _
Il contenuto di questo articolo è una traduzione dell'articolo di Erland Sommarskog trovabile [qui](http://www.sommarskog.se/dyn-search.html).
_ _ _
## 1.Introduzione
E' molto comune dover scrivere query dove la ricerca viene eseguita secondo un diverso numero di criteri diversi a seconda dei parametri in ingresso.
Quando bisogna implementare tali funzionalità è necessario porre attenzione a due cose principalmente:
- Produrre i risultati corretti
- Buone performance

Il punto principale è che non c'è un singolo piano di esecuzione che è buono per tutti i criteri di ricerca, anzi tendenzialmente vorrei che il query plan sia differente in base all'input dell'utente.
Ci sono due modi per ottenere questo: il primo è scrivere una query statica e aggiungere il campo OPTION (RECOMPILE) che obbliga l'SQL Server a compilare la query ogni volta che viene lanciata; il secondo è creare costruire la query dinamicamente in base all'input dell'utente.
## 2.Query statiche
### 2.1 Usare gli IF
Assumiamo per esempio di avere un campo di ricerca di un utente in cui questo può cercare secondo varie condizioni di ricerca, oppure secondo condizioni mutuamente esclusive (posso cercare per nome utente o per id o per codice).
Per questo esempio molto semplice, obbligare il server a ricompilare ogni volta può risultare pesante, sopratutto se le ricerche sono frequenti. la costruzione dinamica della query allo stesso modo rischia di essere troppo complicata.
La soluzione migliore e leggera è usare delle clausole IF nel seguente modo:
```sql
IF @custno IS NOT NULL
SELECT ... FROM customers WHERE custno = @custno
ELSE IF @natregno IS NOT NULL
SELECT ... FROM customers WHERE natregno = @natregno
ELSE IF @custname IS NOT NULL
SELECT ...
FROM customers
WHERE custname LIKE @custname + '%'
ORDER BY custname
ELSE
RAISERROR('No search condition given!', 16, 1)
```
Se volessi ritornare dei dati a partire da altre tabelle è consigliabile **non ripetere il JOIN** all'interno di ogni `IF`, ma piuttosto creare una tabella temporanea ed inserire i risultati della query per poi eseguire un solo join in un secondo momento sulla tabella temporanea.

```sql
IF @custno IS NOT NULL
INSERT @cust (custno) VALUES (@custno)
ELSE IF @natregno IS NOT NULL
INSERT @cust (custno) SELECT custno FROM customers WHERE natregno = @natregno
ELSE IF @custname IS NOT NULL
INSERT @cust (custno)
SELECT TOP (200) custno
FROM customers
WHERE custname LIKE @custname + '%'
ORDER BY custname
ELSE
RAISERROR('No search condition given!', 16, 1)

SELECT ...
FROM @cust c
JOIN customers cst ON cst.custno = c.custno
JOIN ...
```
### 2.2 Usare gli OR
Come alternativa alla proliferazione di clausole `IF`, possiamo inserire tutto in una stessa query utilizzando gli `OR` in `AND` con **AND @var IS NOT NULL**
```sql
SELECT TOP 200 ...
FROM customers
WHERE (custno = @custno AND @custno IS NOT NULL) OR
(natregno = @natregno AND @natregno IS NOT NULL) OR
(custname LIKE @custname + '%' AND @custname IS NOT NULL)
ORDER BY custname
```

### 2.3 Caso complesso
Analizziamo ora un caso più complesso, cioè il caso di una proccedura con molti termini di ricerca.
Assumiamo di avere una classica tabella `Orders`, `Customers` e `Products`.
Una prima implementazione di questa SP è la seguente:
```sql
CREATE PROCEDURE search_orders
@orderid int = NULL,
@fromdate datetime = NULL,
@employeetbl intlist_tbltype READONLY AS

SELECT o.OrderID, o.OrderDate, od.UnitPrice, od.Quantity,
p.ProductName, p.UnitsInStock, p.UnitsOnOrder, o.EmployeeID
FROM Orders o
JOIN [Order Details] od ON o.OrderID = od.OrderID
JOIN Customers c ON o.CustomerID = c.CustomerID
JOIN Products p ON p.ProductID = od.ProductID
WHERE ???
ORDER BY o.OrderID
```
I parametri in ingresso di questa SP sono tutte le modalità di ricerca che può fare l'utente, dall'`@orderid`, al `@fromdate` fino al `@minprice` e così via.
La `search_orders` così fatta non è complicatissima: ogni condizione può essere implementata usando una singolo comando `>`, `<` o `LIKE`. In applicazioni reali spesso esistono vincoli più complessi:
- L'utente può scegliere l'ordinamento di output
- In base ai parametri in ingresso devo poter accedere a tabelle e colonne differenti.
- Gli utenti possono anche poter scegliere gli operatori di paragone, come per esempio `@country = 'Germany'` o `@country != 'Germany'`.

### 2.4 OPTION (RECOMPILE)
Scrivere query statiche può risultare comodo per questi motivi
- Finchè le condizioni di ricerca sono moderatamente complesse, il codice ottenuto è compatto e facile da mantenere;
- visto che la query è compilata ogni volta, ottengo un query plan ottimizzato esattamente per le condizioni di ricerca in input;
- Non devo preoccuparmi sui permessi: funziona esattamente coma una SP, l'utente può non avere permessi di modifica di tabelle.

Anche se bisogna porre attenzione alle seguenti problematiche:
- Quando i requisiti crescono in complessità, la complessità della query cresce in maniera non lineare;
- Se la chiamata viene eseguita numerose volte, la continua ricompilazione della SP può sovraccaricare il server.

La tecnica base è la seguente
```sql
SELECT o.OrderID
, o.OrderDate
, od.UnitPrice
, od.Quantity
...
FROM Orders o
JOIN [Order Details] od ON o.OrderID = od.OrderID
...
WHERE ( o.OrderID = @orderid OR @orderid IS NULL )
AND (o.OrderDate >= @fromdate OR @fromdate IS NULL )
...
AND ( c.CompanyName LIKE @custname + '%' OR @custname IS NULL )
AND ( c.City = @city OR @city IS NULL)
...
AND (p.ProductName LIKE @prodname + '%' OR @prodname IS NULL)
ORDER BY o.OrderID
OPTION (RECOMPILE)
```
L'effetto di tutti i `@x IS NULL` è che se un parametro in ingresso è NULL, allora la sua condizione in AND fornisce sempre TRUE, conseguentemente non viene applicato nessun filtro.
Quindi gli unici filtri che hanno effetto sono quelli che hanno parametro in ingresso non nullo.
Vi è una grande differenza di performance con o senza l'ultima linea:
```sql
OPTION (RECOMPILE)
```
Senza questa istruzione infatti, SQL Server produce un piano di esecuzione che verrà messo un cache e riusato all'occorrenza, conseguentemente tale piano deve funzionare con **tutti i possibili parametri in ingresso**, quindi generalmente lento.
Se invece aggiungiamo l'`OPTION (RECOMPILE)` SQL Server esegue una ricompilazione della query ad ogni chiamata in base ai parametri in ingresso: per esempio chiamando la procedura nel seguente modo:
```sql
EXEC search_orders_3 @orderid = 11000
```
SQL Server ottimizzeràla clausola `WHERE` in questo modo:
```sql
WHERE (o.OrderID = 11000 OR 11000 IS NULL)
AND (o.OrderDate >= NULL OR NULL IS NULL)
AND (o.OrderDate <= NULL OR NULL IS NULL)
...
```
Successivamente SQL Server rimuoverà tutte le clausole **NULL IS NULL** dalla query ottenendo una clausola **WHERE** ottimizzata per la richiesta.

### 2.5 Il problema del COALESCE
Invece di utilizzare l'`OR` come indicato sopra, alcune persone preferiscono usare il comando `COALESCE` o `ISNULL` nel seguente modo:

```sql
o.orderID = coalesce(@orderid, o.OrderID)
o.orderID = isnull(@orderid, o.OrderID)
```
`COALESCE()` è una funzione che prende una lista di valori come parametro e fornisce il primo valore non nullo, oppure `NULL` se tutti i parametri in ingresso sono `NULL`.
Conseguentemente, se `@orderid` è `NULL`, allora il filtro sarà `o.OrderID = o.OrderID` che è analogo a scrivere `1=1`.
Il codice così scritto è più compatto e ancora più chiaro ma porta ad un problema di non poco conto: se la colonna in questione contiene un valore `NULL` e il parametro in ingresso è `NULL` allora il comando
```sql
c.Region = coalesce(@region, c.Region)
```
diventa
```sql
NULL=NULL
```
Ma in SQL **NULL non è uguale a NULL**. NULL indica "valore sconosciuto" e il suo paragone con NULL non porta ne a **true** ne a **false**, ma a **unknown**.
Conseguentemente nessuna riga viene ritornata.
Per evitare questa cosa è possibile scrivere
```sql
coalesce(c.Region, '') = coalesce(@region, c.Region, '')
```
ma è assolutamente poco intuitivo.
La morale della favola è **evitare di usare il COALESCE per eseguire questi controlli**.
### 2.6 Parametri in ingresso stringhe separate da virgola
Aggiungiamo due nuovi parametri in ingresso che non avevamo trattato prima per semplicità che hanno lo stesso scopo: fornire solo gli ordini per dei specifici *employees*.
- `@employeestr`: stringa separata da virgola con indicati gli IDs degli *employees*
- `@employeetbl`: parametro table valued (vedi [documentazione](https://msdn.microsoft.com/en-us/library/bb675163))

Per aggiungere questi filtri nella clausola `WHERE` il modo più semplice è il seguente:
```sql
AND (o.EmployeeID IN (SELECT number FROM intlist_to_tbl(@employeestr)) OR
@employeestr IS NULL)
AND (o.EmployeeID IN (SELECT val FROM @employeetbl) OR @hasemptbl = 0)
```
dove `intlist_to_tbl` è una funzione che trasforma una lista separata da virgola in una tabella e `@hasemptbl` è una variabile locale `BIT` che indica se la variabile `@employeetbl` ha record o meno.
Vi è una differenza fondamentale tra questi parametri e i normali parametri scalari: mentre per i parametri scalari l'ottimizzatore conosce esattamente la loro esistenza e il loro valore, per questi parametri così non è: delle variabili di tabella conosce il numero di righe, mentre della stringa separata da virgole non conosce assolutamente nulla.
Un modo per risolvere questo problema è l'idea che spesso l'utente vuole cercare fino a due o tre valori alla volta. Quindi, se ci sono fino a 4 elementi nella lista, la procedura utilizza il comando IN, altrimenti utilizza una variabile di tabella.
La procudura avrà quindi il seguente codice all'inizio:
```sql
DECLARE @rowc int,
@emp1 int,
@emp2 int, 
@emp3 int,
@emp4 int,
@emptbl bit = 0

IF @employeestr IS NOT NULL
BEGIN
INSERT @employeetbl (rowno, employeeid)
SELECT row_number() OVER(ORDER BY (SELECT 1)), number
FROM intlist_to_tbl(@employeestr)
SELECT @rowc = @@rowcount

IF @rowc BETWEEN 1 AND 4
BEGIN
SELECT @emp1 = employeeid FROM @employeetbl WHERE rowno = 1
SELECT @emp2 = employeeid FROM @employeetbl WHERE rowno = 2
SELECT @emp3 = employeeid FROM @employeetbl WHERE rowno = 3
SELECT @emp4 = employeeid FROM @employeetbl WHERE rowno = 4
END
ELSE IF @rowc > 4
SELECT @emptbl = 1
END
```
Questo metodo, se `@employeestr` è valorizzato, esegue l'unpack della lista e la inserisce in una variabile di tabella con le righe numerate. Se ci sono 4 o meno righe allora popoliamo le variabili da `@emp1` a `@emp4` altrimenti settiamo la variabile booleana `@hasemptbl` a 1.
Le ultime due righe della clausola WHERE saranno quindi
```sql
AND (o.EmployeeID IN (@emp1, @emp2, @emp3, @emp4) OR @emp1 IS NULL)
AND (o.EmployeeID IN (SELECT employeeid FROM @employeetbl) OR @hasemptbl = 0)
```
Usando questo metodo la query risulta estremamente più veloce, sopratutto nel caso in cui vengano forniti meno di 4 IDs.

### 2.8 Scelta dell'ordinamento
Se vogliamo dare all'utente la possibilità di scegliere l'ordinamento, questo può essere facilmente eseguito con query SQL statiche.
Qeusto è il pattern base da utilizzare:
```sql
ORDER BY CASE @sortcol
WHEN 'OrderID'
THEN o.OrderID
WHEN 'EmployeeID'
THEN o.EmployeeID
WHEN 'ProductID'
THEN od.ProductID
END
, CASE @sortcol
WHEN 'CustomerName'
THEN c.CompanyName
WHEN 'ProductName'
THEN p.ProductName
END
, CASE @sortcol
WHEN 'OrderDate'
THEN o.OrderDate
END
```
Ho un parametro in ingresso che mi dice la colonna per cui ordinare e poi utilizzo il **CASE** per selezionare tale variabile.
La cosa importante da osservare è che **tutti i rami del CASE devo avere lo stesso tipo di dato**. In questo caso ho tre rami in quanto voglio eseguire tre ordinamenti di tipo diverso: `int`, `string` e `datetime`.
Mescolando invece i tipi di dato, per le regole di precedenza di SQL server, otterrei errori di conversione.
Se utilizziamo l'opzione `OPTION (RECOMPILE)` il comkpilatore è in grado di ridurre l'`ORDER BY` ad una singola colonna in base al parametro in ingresso.
Se inoltre voglio gestire l'ordinamento ascendente e discendente, devo **duplicare ogni cosa**.
```SQL
ORDER BY CASE WHEN @isdesc = 1 THEN
CASE @sortcol WHEN 'OrderID' THEN o.OrderID
WHEN 'EmployeeID' THEN o.EmployeeID
WHEN 'ProductID' THEN od.ProductID
END DESC,
CASE WHEN @isdesc = 0 THEN
CASE @sortcol WHEN 'OrderID' THEN o.OrderID
WHEN 'EmployeeID' THEN o.EmployeeID
WHEN 'ProductID' THEN od.ProductID
END ASC
```
Usare questo metodo porta alla crescita della procedura in maniera non lineare.
Conseguentemente usare l'SQL statica va bene solo se consideriamo un solo possibile ordinamento e se tutte i tipi di ordinamento possibili hanno lo stesso tipo. In caso contrario conviene procede in maniera diversa con una SQL dinamica o gestendo l'ordinamento lato client.

### 2.9 Tabelle opzionali
Talvolta voglio poter accedere ad una determinata tabella solo ad una determinata condizione.
Aggiungiamo un nuovo parametro `@suppl_country` alla nostra procedura che indica che la nostra procedura fornirà informazioni solo sui prodotti il cui fornitore viene da un determinato stato.
Il modo migliore per implementare questo, invece che andare in **JOIN** sulla tabella `Suppliers` possiamo utilizzare la clausola **EXISTS** in questo modo:
```sql
AND (@suppl_country IS NULL OR EXISTS (SELECT *
FROM Suppliers s
WHERE s.SupplierID = p.SupplierID
AND s.Country = @suppl_country))
```
Se non trovo la @suppl_country l'EXISTS mi fornirà 0 e quindi il risultato verrà filtrato, altrimenti procederà. In questo modo filtro i risultati solo per lo stato che ho inserito in ingresso, inoltre usando questo trucco è possibile verificare che l'SQL Server è capace di evitare di accedere a `Suppliers` anche senza l'`OPTION(RECOMPILE)`

### 2.10 Tabelle alternative
Un ulteriore scenario potrebbe essere quello di dover leggere da tabelle differenti in base ad un determinato parametro.
Per esempio, assumiamo che esista un parametro `@ishistoric` che, se impostato a 1, va in join con la tabella `HistoricOrders`, altrimenti da `HistoricOrderDetails`.
Il modo più corretto per eseguire questa cosa è il seguente:
```sql
FROM (SELECT o.OrderID, o.OrderDate, od.UnitPrice, od.Quantity,
od.CustomerID, od.ProductID
FROM Orders o
JOIN [Order Details] od ON o.OrderID = od.OrderID
WHERE @ishistoric = 0
UNION ALL
SELECT o.OrderID, o.OrderDate, od.UnitPrice, od.Quantity,
od.CustomerID, od.ProductID
FROM HistoricOrders o
JOIN HistoricOrderDetails od ON o.OrderID = od.OrderID
WHERE @ishistoric = 1) AS u
JOIN Customers c ON o.CustomerID = u.CustomerID
JOIN Products p ON p.ProductID = u.ProductID
```
Ho rimosso il `JOIN` esplicito tra `Orders` e `OrderDetails` con una tabella derivata che è un **UNION ALL tra due query di JOIN in cui entrmabe hanno una clausola WHERE sulla variabile booleana in ingresso**.
Usando `OPTION(RECOMPILE)` solo un insieme di tabelle ordini verrà acceduto a run-time.
E' facile notare come la query ha delle ripetizioni, la lista in `SELECT` e le condizioni di `JOIN`. Più le tabelle alternative aumentano, più conviene utilizzare una costruzione SQL dinamica rispetto a questa statica.

## 3. Costruzione dinamica della query
A differenza delle query statiche, le query dinamiche sono uno strumento molto potente ma rischiano di creare codice non mantenibile e difficile da comprendere. E' necessario conseguentemente utilizzarle con cautela.
I vantaggi principali delle SQL dinamiche sono:
- Sono più flessibili: la complessità della query cresce **linearmente** con la complessità dei requisiti
- I query plan sono messi in cache dalla stringa di query, quindi i criteri di ricerca crescenti non causeranno inutili ricompilazioni
Gli svantaggi invece:
- Poca disciplina nella scritture del codice porta questo ad essere difficile da mantenere
- Introducono un ulteriore livello di difficoltà dall'inizio
- Il test è molto più difficile

### 3.1 Gestire i parametri ingresso
Ci sono due modi per gestire i parametri in ingresso inviati dall'utente:
- Concatenarli alla query string (`' AND col = ' + convert(varchar, @value)'`)
- Usare query parametriche usando i parametri in ingresso di `sp_executesql` (`' AND col = @value'`)

Nel 99.9% dei casi è **estremamente consigliato** usare query parametriche con `sp_executesql`

### 3.2 Costruzione della query
Dichiariamo la variabile `@sql` che conterrà la mia query string.
```sql
DECLARE @sql nvarchar(MAX);
DECLARE paramlist nvarchar(4000);
```
Di seguito dichiariamo il nucleo della SQL dinamica che deve essere la query (funzionante) da lanciare quanto **non viene passato alcun parametro in ingresso**.
Per le tabelle usare sempre la notazione `schema.nome_tabella`, per ragioni di performance.
La condizione `WHERE 1 = 1` alla fine permette di appende tutte le altre condizini come `AND qualcosa` senza incorrere in errori di sintassi.
```sql
SELECT @sql =
'SELECT o.OrderID, o.OrderDate, od.UnitPrice, od.Quantity,
c.CustomerID, c.CompanyName, c.Address, c.City,
c.Region, c.PostalCode, c.Country, c.Phone,
p.ProductID, p.ProductName, p.UnitsInStock,
p.UnitsOnOrder, o.EmployeeID
FROM dbo.Orders o
JOIN dbo.[Order Details] od ON o.OrderID = od.OrderID
JOIN dbo.Customers c ON o.CustomerID = c.CustomerID
JOIN dbo.Products p ON p.ProductID = od.ProductID
WHERE 1 = 1'
```
Di seguito controlliamo ogni parametro in ingresso, se questo è non nullo aggiungere il filtro per tale parametro alla query string.
```sql
...
IF @country IS NOT NULL
SELECT @sql += ' AND c.Country = @country'
IF @employeestr IS NOT NULL
SELECT @sql += ' AND o.EmployeeID IN' +
' (SELECT number FROM intlist_to_tbl(@employeestr))'
IF @prodid IS NOT NULL
SELECT @sql += ' AND od.ProductID = @prodid' +
' AND p.ProductID = @prodid'
...
```
Sottolineo che i parametri che sono presenti in più tabelle (ottenuti da clausole di **JOIN**), come per esempio `@prodid` è consigliabile aggiungere la condizione su **entrmabe le tabelle** in quanto aiutano notevolemente l'ottimizzatore nel caso in cui **non esistano vincoli di foreing key**.

### 3.3 PRINT di debug
Una volta costruita la query, prima di lanciarla con il `sp_executesql` scriviamo:
```sql
IF @debug = 1
PRINT @sql
```
Questo permette, se un parametro in ingresso è impostato a 1, di printare la query generata. **Non dimenticare mai di aggiungere questo parametro quando lavoro con query generate dinamicamente**.
Uno degli svanataggi principali delle query dinamiche è che la concatenazione può portare ad errori di sintassi difficili da rilevare: trovare l'errore guardando il codice che genera la SQL dinamica è difficile, ma una volta vista la query generata è invece molto più semplice.
Se la query supera i 4000 caratteri verrà troncata dal print, per risolvere invece di usare la funzione print scriviamo:
```sql
IF @debug = 1
SELECT @sql FOR XML PATH(''), TYPE
```
che non ha limiti di caratteri.

### 3.4 Eseguire la query
Per eseguire la query ho bisogno di due parti distinte, il set up della lista dei parametri e l'esecuzione effettiva della query.
Assegnazione della variabile `@paramlist`:
```sql
SELECT @paramlist = '@orderid int,
@fromdate datetime,
@todate datetime,
@minprice money,
@maxprice money,
@custid nchar(5),
@custname nvarchar(40),
@city nvarchar(15),
@region nvarchar(15),
@country nvarchar(15),
@prodid int,
@prodname nvarchar(40),
@employeestr varchar(MAX),
@employeetbl intlist_tbltype READONLY'
```
Esecuzione della query:
```sql
EXEC sp_executesql @sql, @paramlist,
@orderid, @fromdate, @todate, @minprice,
@maxprice, @custid, @custname, @city, @region,
@country, @prodid, @prodname, @employeestr, @employeetbl
```
Di seguito analizziamo la procedura `sp_executesql`: questa ha due parametri in ingresso, il primo parametro è la stringa SQL, la seconda è la lista dei parametri impiegati come stringa separata da virgole. Gli altri parametri sono i parametri della variabile `@sql`.
Per capire questa procedura basti pensare come la `sp_executesql` crei una procedura virtuale con il seguente scheletro:
```sql
CREATE PROCEDURE sp @paramlist AS
@sql
go
EXEC sp orderid, @fromdate, @todate, @minprice...
```
la lanci e poi la elimini.

### 3.5 Compilazione e caching

Abbiamo detto che la `sp_executesql` definisce una procedura senza nome e la esegue direttamente. Questa procedura **non** è salvata sul database, ma è **salvato il suo query plan**. Quindi la prossima volta che un utente chiama tale stored procedura con esattamente lo stesso insieme di parametri in ingresso, SQL Server riutilizzerà tale piano di esecuzione trovato in cache

### 3.6 Scelta dell'ordinamento
Sembra che questa cosa possa essere eseguita semplicemente scrivendo:
```sql
@sql += ' ORDER BY ' + @sortcol
```
Il client però così scrivendo dovrà inviare `'CustomerID, OrderID DESC'` come parametro in ingresso, che viola la regola principale per cui **il client non deve conoscere nulla della query che sta chiamando**.
Inoltre porta a svariati problemi di coerenza col model, SQL injection e così via.
Il modo migliore è utilizzare un **CASE** che mappi il valore di inpput con una colonna ordinabile nel seguente modo:
```sql
SELECT @sql += ' ORDER BY ' +
CASE @sortcol WHEN 'OrderID' THEN 'o.OrderID'
WHEN 'EmplyoeeID' THEN 'o.EmployeeID'
ELSE 'o.OrderID'
END + CASE @isdesc WHEN 0 THEN ' ASC' ELSE ' DESC' END
```
Rispetto alla query statica questa procedura è molto più semplice: non dobbiamo creare più CASE in base al tipo di dato da ordnare, ma possiamo fare tutto in una singola query

### 3.7 Tabelle alternative
Andare in join su tabelle diverse è molto più semplice con SQL dinamiche, seguendo l'esempio sopra possiamo scrivere:
```sql
FROM dbo.' + CASE @ishistoric
WHEN 0 THEN 'Orders'
WHEN 1 THEN 'HistoricOrders'
END + ' o
JOIN dbo.' + CASE @ishistoric
WHEN 0 THEN '[Order Details]'
WHEN 1 THEN 'HistoricOrderDetails'
END + ' od
```
Anche in questo caso è **assolutamente sconsigliato farci passare il nome della tabella come parametro**: devo essere libero di rinominare il backend senza dover fare modifice al frontend, inoltre questo non deve sapere nulla della struttura del database.

## 4. Conclusioni
Abbiamo visto che vi sono due modi per implementare condizioni di ricerca dinamiche: SQL statiche o dinamiche.
Le soluzioni con le SQL statiche devono (quasi) sempre includere OPTION(RECOMPILE) tranne nei casi mlto semplici, sono più semplici da implementare se i requisiti sono moderatamente complessi.
Le query dinamiche invece sono più difficili da usare ma hanno potenzialità molto maggiori.