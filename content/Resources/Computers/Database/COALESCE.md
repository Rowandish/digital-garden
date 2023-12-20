---
tags:
  - PublishedPosts
  - Database
---
Il comando **COALESCE** (Standard ANSI, SQL-92 compatibile) è un comando estremamente comodo che valuta gli argomenti seguendo l'ordine e restituisce il valore corrente della prima espressione che inizialmente non restituisce `NULL`.

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

## Esempi

### Esempio 1

Nell'esempio seguente viene illustrato il modo in cui `COALESCE` seleziona **i dati dalla prima colonna in cui è presente un valore non Null**.

```sql
SELECT Name, COALESCE(Class, Color, ProductNumber) AS FirstNotNull
FROM Product;
```

### Esempio 2

COALESCE può essere utilizzato per eseguire query leggermente più complesse come la seguente: ho una tabella `pagamenti` che include tre colonne con informazioni sulla retribuzione annua dei dipendenti, ovvero retribuzione oraria, stipendio e commissione. Un dipendente tuttavia riceve un solo tipo di paga, gli altri due valori saranno impostati correttamente a **NULL**.  

Per determinare l'importo totale pagato a tutti i dipendenti, utilizzare la funzione `COALESCE` per ottenere _solo i valori non **NULL**_ delle colonne `paga_oraria`, `salario` e `commissione`.

| id | paga_oraria | salario | commissione | numero_vendite |
|----|-------------|---------|-------------|----------------|
|1|10|NULL|NULL|NULL|
|2|NULL|10000|NULL|NULL|
|3|NULL|NULL|15000|3|

```sql
SELECT CAST(COALESCE(paga_oraria * 40 * 52, salario,
commissione * numero_vendite) AS money) AS 'Salario emesso' FROM pagamenti;
```

Ottengo quindi il seguente output (solo prima colonna)

| Salario emesso |  | Spiegazione|
|----|-------------|---------|
|20800,00|->|10 \* 40 \* 52|
|10000,00|->|10000|
|45000,00|->|15000 \* 3|