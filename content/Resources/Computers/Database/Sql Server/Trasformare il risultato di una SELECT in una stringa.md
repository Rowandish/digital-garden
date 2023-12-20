---
tags:
  - SqlServer
  - PublishedPosts
---
Talvolta può capitare l'esigenza di fornire come risultato di una query non una lista di campi, ma un solo campo formato da una lista concatenata, che sono i valori risultanti della query in questione.

Assumiamo di avere una `SELECT` che mi ritorna una colonna di valori, per esempio
```sql
SELECT Field FROM Table
```
Che fornisce:

| Field |
| --- |
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
Ora devo eliminare il tag **f**, per far ciò modifico la query nel seguente modo:
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

Ora per eliminare anche il **ROOTNODE** uso la funzione `value` nel seguente modo:
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
```
,aaa,bbb,ccc,ddd
```

L'ultimo punto è eliminare la prima virgola, per far ciò utilizzo la funzione **STUFF** che consente di inserire una stringa in un'altra stringa eliminando un numero di caratteri specificato nella posizione iniziale della prima stringa e inserendo la seconda stringa in tale posizione.
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