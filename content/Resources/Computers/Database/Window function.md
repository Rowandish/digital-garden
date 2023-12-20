---
tags:
  - Coding
  - PublishedPosts
  - Database
---
## 1. Introduzione
Sviluppando query complesse nasce la necessità di **partizionare ed eventualmente ordinare un set di righe prima dell'applicazione di una funzione**. SQL Server (e PostgreSQL) forniscono la clausola **OVER** e **PARTITION BY** per poter raggruppare i dati secondo **un set di righe specificato dall'utente**. Successivamente una funzione **calcola un valore per ogni riga del set**.
Non tutti i DBMS offrono le *window function*, per esempio MySQL non le supporta, ma esistono delle [alternative](http://explainextended.com/2009/03/10/analytic-functions-first_value-last_value-lead-lag/).

È possibile utilizzare la clausola **OVER** con le funzioni per calcolare i valori aggregati, ad esempio medie, aggregazioni cumulative, totali parziali o i primi *N* risultati per gruppo.

Segue la definizione (da documentazione) di come utilizzare tale comando.

```sql
OVER ( 
[ <PARTITION BY clause> ]
[ <ORDER BY clause> ] 
[ <ROW or RANGE clause> ]
) 
```
- **PARTITION BY**: **Suddivide il set di risultati della query in partizioni** (raggruppamenti). La funzione viene applicata a ogni singola partizione e **il calcolo viene effettuato per ogni partizione**. Si deve specificare la colonna (o più colonne) secondo la quale il risultato della query viene partizionato (raggruppato). Il **PARTITION BY** è analogo al **GROUP BY**, segue le sue stesse regole.
- **ORDER BY**: E' possibile definire l'ordine logico delle righe di ogni partizione. Quindi specifica l'ordine logico secondo il quale la funzione viene eseguita.
- **ROWS | RANGE**: Limita ulteriormente le righe all'interno della partizione specificando i punti iniziali e finali. La clausola **ROWS** limita le righe all'interno di una partizione specificando un numero fisso di righe precedenti o successive alla riga corrente. In alternativa, la clausola **RANGE** limita logicamente le righe all'interno di una partizione specificando un intervallo di valori rispetto al valore nella riga corrente.

E' importante notare come le righe considerate da una *window function* sono quelle della tabella virtuale prodotta dalla query filtrata per **WHERE** e **GROUP BY**, per esempio una riga rimossa dal **WHERE** non viene in alcun modo vista dalla *window function*.


## 2. OVER vs GROUP BY
La differenza con le funzioni di aggregazione (**GROUP BY**) è che **una window function non raggruppa i risultati in una singola riga**, ma questi rimangono separati in entità distinte.

Consideriamo, per esempio, la seguente tabella in cui vi è un misuratore che rileva il `Consumo` di energia

```sql
SELECT IDConsumoMisuratori, IDMisuaratore, Consumo
FROM ConsumoMisuratori
WHERE IDMisuaratore = 999
```

|IDConsumoMisuratori |IDMisuaratore | Consumo |
|--------|--------|--------|
|1|999|NULL|
|2|999|31.0|
|3|999|18.0|
|4|999|NULL|
|5|999|NULL|

La seguente è una classica query per il calcolo della media del `Consumo` con il **GROUP BY**

```sql
SELECT IDMisuaratore, AVG(Consumo) AS ConsumoMedio
FROM ConsumoMisuratori AS gl
WHERE IDMisuaratore = 999
GROUP BY IDMisuaratore

```

| IDMisuaratore | ConsumoMedio |
|--------|--------|
|999|24.500000|

La seguente invece usa l'**OVER PARTITION** (sempre raggruppando per `IDMisuaratore`)

```sql
SELECT IDMisuaratore
, AVG(Consumo) OVER (PARTITION BY IDMisuaratore) AS ConsumoMedio
FROM ConsumoMisuratori AS gl
WHERE IDMisuaratore = 999
```

| IDMisuaratore | ConsumoMedio |
|--------|--------|
|999|24.500000|
|999|24.500000|
|999|24.500000|
|999|24.500000|
|999|24.500000|

Come si può notare l'**OVER PARTITION** esegue la media sui risultati raggruppati dalla clausola **PARTITION BY** ma senza unire i risultati in una unica riga ma mantenendoli su righe distinte.

### 3.1 OVER()
La chiamata di **PARTITION BY** non è obbligatoria: se la mia partizione sono **tutte** le righe posso omettere la dichiarazione:
Nell'esempio seguente eseguo un filtro sull'`IDMisuaratore` (`WHERE IDMisuaratore = 999`).
Conseguentemente dichiarare la **PARTITION** (`OVER (PARTITION BY IDMisuaratore)`) o ometterla `OVER ()` fornisce lo stesso identico risultato

```sql
SELECT IDMisuaratore
, AVG(Consumo) OVER () AS ConsumoMedio
FROM ConsumoMisuratori AS gl
WHERE IDMisuaratore = 999
```

| IDMisuaratore | ConsumoMedio |
| ------------- | ------------ |
| 999           | 24.500000    |
| 999           | 24.500000    |
| 999           | 24.500000    |
| 999           | 24.500000    |
| 999           | 24.500000    |

Se invece non ho un filtraggio sull'IDMisuaratore la media dei consumi sarà su tutta la tabella

```sql
SELECT IDMisuaratore
, AVG(Consumo) OVER () AS ConsumoMedio
FROM ConsumoMisuratori AS gl
```

| IDMisuaratore | ConsumoMedio |
|--------|--------|
|999|-289.5|
|999|-289.5|
|999|-289.5|
|...|...|

### 3.2 ORDER BY
Ora aggiungiamo un **ORDER BY** al **PARTITION BY**:
```sql
SELECT IDConsumoMisuratori, IDMisuaratore
, AVG(Consumo) OVER (PARTITION BY IDMisuaratore ORDER BY IDConsumoMisuratori) AS ConsumoMedio
FROM ConsumoMisuratori AS gl
WHERE IDMisuaratore = 999
```
Ottengo il seguente risultato:

|IDConsumoMisuratori | IDMisuaratore | Consumo |Metodo eseguito|
|---------|--------|--------|--------|--------|
|1|999|NULL|-->|AVG(NULL)|
|2|999|31.0|-->|AVG(NULL, 31)|
|3|999|24.50|-->|AVG(NULL, 31, 18)|
|4|999|24.50|-->|AVG(NULL, 31, 18, NULL)|
|5|999|24.50|-->|AVG(NULL, 31, 18, NULL, NULL)|

Come si può notare viene eseguita una specie di cumulata, la funzione **AVG** utilizza come parametro di ingresso **non** tutta la partizione, ma iterativamente la completa inserendo record ordinati con l'**ORDER BY**.
Ricordo che l'**ORDER BY** della partition non deve necessariamente corrispondere con l'**ORDER BY** della query.
Analogamente a sopra, eseguendo un filtraggio sull'`IDMisuaratore` posso omettere di eseguire il partizionamento, scrivendo quindi
```sql
OVER ( ORDER BY IDMisuaratore )
```
ottenendo lo stesso risultato.
Se elimino il filtraggio sull'`IDMisuaratore` posso ottenere come varia la media al crescere dell'`IDMisuaratore` (la partizione è tutta la tabella).
```sql
SELECT IDMisuaratore
, AVG(Consumo) OVER ( ORDER BY IDMisuaratore ) AS ConsumoMedio
FROM ConsumoMisuratori AS gl
```

| IDMisuaratore | ConsumoMedio |
|--------|--------|
|111|NULL|
|999|24.500000|
|999|24.500000|
|333|58.600000|
|100030|55.375000|
|...|...|

## 3. Window frame
Un altro concetto importante associato alle *window function* è quello di *window frame*, spesso la funzione che lavora sulle partizioni non lavora su tutta la partizione, ma solo su un suo sottoinsieme.
Le window function sono permesse solo dentro la `SELECT`, se ho la necessità invece di raggruppare righe **dopo** che il calcolo della window function è stato eseguito devo usare una **sottoquery**.

### 3.1 Esempi

#### 3.1.1 Associare IDMisuaratore ai primi n consumi
Per prima cosa scrivo una query che mi fornisca, per ogni `IDMisuaratore`, il massimo del `Consumo`.
Questa query è facilmente esprimibile con un **GROUP BY**:
```sql
SELECT IDMisuaratore, max(Consumo) AS ConsumoMassimo
FROM ConsumoMisuratori AS gl
GROUP BY IDMisuaratore
```

| IDMisuaratore | ConsumoMassimo |
|--------|--------|
|111|NULL|
|999|31.0|
|333|156.0|

Ora provo ad ottenere gli stessi risultati utilizzando una *window function* invece che un **GROUP BY**.
Per prima cosa creo un rowset che associa, per ogni `IDMisuaratore`, il suo `Consumo`, ordinata per Consumo con la funzione **RANK()**:
```sql
SELECT IDMisuaratore
, Consumo
, RANK() OVER ( PARTITION BY IDMisuaratore ORDER BY Consumo DESC ) AS Pos
FROM ConsumoMisuratori AS gl
```
Che ottiene

| IDMisuaratore | ConsumoMassimo | Pos |
|--------|--------|--------|
|111|NULL|1|
|999|31.0|1|
|999|18.0|2|
|999|NULL|3|
|...|...|...|

Come si può notare a *Pos=1* corrisponde il valore massimo.
Posso inserire questa query con subquery nel seguente modo:
```sql
SELECT IDMisuaratore
, Consumo AS ConsumoMassimo
FROM (
SELECT IDMisuaratore
, Consumo
, RANK() OVER (
PARTITION BY IDMisuaratore ORDER BY Consumo DESC
) AS Pos
FROM ConsumoMisuratori AS gl
)
WHERE Pos = 1
```
Mettendo il filtro a `Pos = 1` ottengo esattamente lo stesso risultato della query con il** GROUP BY** e il **MAX**

| IDMisuaratore | ConsumoMassimo |
|--------|--------|
|111|NULL|
|999|31.0|
|333|156.0|

Usare le window function per calcolare il massimo è ovviamente inutile, però assumiamo per esempio di calcolare i **due** valori più alti (o genericamente gli **n** valori più alti), e non solo il massimo. Con il **MAX** e **GROUP BY** è impossibile, ma così non è con le **PARTITION**.
Basta estendere la precedente query con `Pos < 3` e ottengo, per ogni `IDMisuaratore`, i primi due valori per il `Consumo` (se esistono)

| IDMisuaratore | ConsumoMassimo |
|--------|--------|
|111|NULL|
|999|31.0|
|999|18.0|
|333|156.0|
|333|66.0|
|...|...|

Genericamente scrivendo `Pos < n` ottengo i primi n valori del `Consumo`, per ogni `IDMisuaratore`.

#### 3.1.2 JOIN solo su un sottoset di dati
Assumiamo di avere una relazione 1-n tra la tabella `Container` e la tabella `Images`.
Ora voglio selezionare tutti i `Container` insieme alle prime 3 `Images` ivi contenute. Questo problema è risolto con le *window function*, in quanto vado a fare il `JOIN` non su `Images`, ma su una tabella virtuale partizionata solo con in cui ad ogni `Images` è associato il suo `ROW_NUMBER()`.

Posso poi quindi partizionare solo le Images con `ROW_NUMBER() <= 3`, conseguentemente eseguo il `JOIN` solo sulle prime 3 immagini.
```sql
SELECT img.*, Container.*
FROM Container
INNER JOIN (
SELECT *
, ROW_NUMBER() OVER (
PARTITION BY Container_id ORDER BY creatioon_date
) AS rn
FROM Images
) AS img ON img.Container_id = Container.id
AND img.rn <= 3
```

#### 3.3 Correlare dati tra tabelle con il ROW_NUMBER
Le window function sono un argomento molto ampio e meriteranno un approfondimento in un articolo ad hoc, ma riassumendo queste funzioni permettono di **partizionare ed eventualmente ordinare un set di righe prima dell'applicazione di una funzione**.
La clausola **OVER** definisce un set di righe specificato dall'utente all'interno di un set di risultati della query. Successivamente una funzione **calcola un valore per ogni riga del set**.

##### 3.3.1 Definizione del dataset

Ora lavoriamo sulle seguenti tabelle, che sono delle tabelle provvisorie create ad hoc, queste sono una parte di dei raggruppamenti per la colonna `Foo` e filtrate per `Foo=2183098`.
```sql
SELECT * INTO #temp_table_1
FROM (
SELECT N'2183098' AS Foo, N'142230' AS Bar UNION ALL
SELECT N'2183098' AS Foo, NULL AS Bar UNION ALL
SELECT N'2183098' AS Foo, NULL AS Bar ) t;
```

| Foo | Bar |
|--------|--------|
|2183098|142230|
|2183098|NULL|
|2183098|NULL|


```sql
SELECT * INTO #temp_table_2
FROM (
SELECT N'2183098' AS Foo, N'142228' AS Bar UNION ALL
SELECT N'2183098' AS Foo, N'142229' AS Bar UNION ALL
SELECT N'2183098' AS Foo, N'142230' AS Bar UNION ALL
SELECT N'2183098' AS Foo, N'142231' AS Bar UNION ALL
SELECT N'2183098' AS Foo, N'142232' AS Bar UNION ALL
SELECT N'2183098' AS Foo, N'142233' AS Bar ) t;
```

| Foo | Bar |
|--------|--------|
|2183098|142228|
|2183098|142229|
|2183098|142230|
|2183098|142231|
|2183098|142232|
|2183098|142233|

Il mio obiettivo è associare le due tabelle (come se ci fosse una specie di JOIN) per ottenere il seugente risultato

| Foo | Bar tabella 1 | Bar tabella 2 |
|--------|--------|--------|
|2183098|142230|142228|
|2183098|NULL|142229|
|2183098|NULL|142230|

Questo può essere utile in caso di update o di confronto dati tra le due tabelle e così via.

##### 3.3.2 Estrazione del ROW_NUMBER
Analizzando approfonditamente il problema, si nota che quello che voglio fare è associare le tabelle per numero di riga: è necessario conseguentemente eseguire un `SELECT` sulle tabelle che aggiunga anche il numero di righe al dataset ottenuto dalle tabelle.

Per fare questo utilizzo la funzione di rango `ROW_NUMBER` che restituisce il numero sequenziale di una riga all'interno di una partizione di un set di risultati, a partire da 1 per la prima riga di ogni partizione.
```sql
SELECT row_number() OVER (
PARTITION BY Foo ORDER BY Foo
) AS Riga_1
, *
FROM #temp_table_1
```
ed analogamente anche sulla seconda tabella.
I risultati che ottengo sono i seguenti:

|Riga_1| Foo | Bar |
|--------|--------|--------|
|1|2183098|142230|
|2|2183098|NULL|
|3|2183098|NULL|

|Riga_2| Foo | Bar |
|--------|--------|--------|
|1|2183098|142228|
|2|2183098|142229|
|3|2183098|142230|
|4|2183098|142231|
|5|2183098|142232|
|6|2183098|142233|

Il `PARTITION BY Foo` è superfluo in questo semplice esempio, in quanto ho già precedentemente filtrato per `Foo=2183098`, ma in un caso reale così non è.

##### 3.3.3 Associazione dei dati
Una volta fatto ciò, l'associazinoe risulta immediata con un JOIN in questo modo:
```sql
SELECT T1.Foo
, T1.Bar AS [Bar tabella 1]
, T2.Bar AS [Bar tabella 2]
FROM (
... prima query
) AS T1
INNER JOIN (
... seconda query
) AS T2 ON T1.Riga_1 = T2.riga_2
```
Che mi permette di ottenere quanto voluto.

| Foo | Bar tabella 1 | Bar tabella 2 |
|--------|--------|--------|
|2183098|142230|142228|
|2183098|NULL|142229|
|2183098|NULL|142230|


#### 3.4 INSERT INTO tabella senza identity
Se stiamo lavorando su tabelle legacy o non architettate al meglio, può capitare di avere una colonna chiave primaria senza identity, conseguentemente quando si ha la necessità di eseguire insert massivi devo utilizzare un trucco per associare ad ogni record inserito il valore della chiave primaria incrementale.
Per poter eseguire questa cosa, vengono ancora una volta in aiuto le window function.
Prendiamo come esempio la tabella `TableNoIdentity` ha `IDTable` chiave primaria ma senza alcuna identity impostata su di essa.
Per prima cosa salvo in una variabile il valore massimo della chiave primaria inserito nella tabella.
```sql
DECLARE @maxIdTable int;
SELECT @maxIdTable = max(IDTable) FROM TableNoIdentity
```
Per l'inserimento con la `INSERT INTO SELECT` utilizzo, come prima colonna della `SELECT`, un `OVER (ORDER BY ( SELECT 1 ) )`, che mi fornisce un numero crescente per ogni riga e vi vado a sommare il valore massimo trovato prima.
```sql
INSERT INTO TableNoIdentity (...)
SELECT @maxIdTable + row_number() OVER (ORDER BY ( SELECT 1 ) ), foo_field, ...
FROM foo_table
```
In questo modo ottengo un inserimento con id crescente coerente con la chiave primaria.

## 4. Funzioni di rango
Le funzioni di rango restituiscono un valore di rango per ogni riga di una partizione. In base alla funzione utilizzata, è possibile che venga assegnato lo stesso valore a più righe.

| Row Number | Rank | Dense Rank | Quartile |
|--------|--------|--------|--------|
|1 |1 |1 |1 |
|2 |1 |1 |1 |
|3 |1 |1 |2 |
|4 |1 |1 |2 |
|5 |1 |1 |3 |
|6 |6 |2 |3 |
|7 |6 |2 |4 |

### 4.1 RANK
Restituisce il rango di ogni riga all'interno della partizione di un set di risultati. Il valore di rango di una riga è uno più il numero di ranghi che precedono la riga in questione. Se due o più righe hanno un valore equivalente per un rango, ogni riga equivalente riceve lo stesso rango. La funzione **RANK** **non restituirà sempre valori interi consecutivi**.
### 4.2 DENSE_RANK
Restituisce il rango delle righe nella partizione di un set dei risultati, senza vuoti tra i ranghi. Se due o più righe hanno un valore equivalente per un rango nella stessa partizione, alle righe con valori equivalenti viene assegnato lo stesso rango. I numeri restituiti dalla funzione **DENSE_RANK** sono pertanto **sempre consecutivi e senza gap**.
### 4.3 ROW_NUMBER
Restituisce il numero sequenziale di una riga all'interno di una partizione di un set di risultati, a partire da 1 per la prima riga di ogni partizione.
### 4.4 NTILE
Distribuisce le righe di una partizione ordinata in un numero specificato di gruppi. Utile per suddividere le righe ottenute da una **SELECT** in n gruppi in base ad un determinato parametro (`Consumo`, fattura, data...).
Per esempio la seguente query divide le letture (`IDConsumoMisuratori`) per un determinato `IDgasMisuratori` in base al ``Consumo``.
```sql
SELECT IDConsumoMisuratori, Consumo
, NTILE(4) OVER (
ORDER BY Consumo DESC
) AS Quartile
FROM ConsumoMisuratori AS gl
WHERE IDMisuaratore = 100002
```

| IDConsumoMisuratori | Consumo | Quartile |
|--------|--------|--------|
|325|5713.000|1|
|11|4095.000|1|
|124|3817.000|1|
|240|2990.000|2|
|1592|2976.000|2|
|4|2972.000|2|
|262|2691.000|3|
|1594|2604.000|3|
|1595|2498.000|3|
|3|1907.000|4|
|158|1722.000|4|
|1602|1722.000|4|

