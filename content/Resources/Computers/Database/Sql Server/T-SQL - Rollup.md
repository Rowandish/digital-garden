---
tags:
  - Coding
  - SqlServer
  - PublishedPosts
---
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
