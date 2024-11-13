---
tags:
  - Coding
  - SqlServer
---
In SQL Server, la ricerca full-text consente a utenti e applicazioni di eseguire q**uery full-text su dati di tipo carattere in tabelle di SQL Server**.
Affinché le query full-text possano essere eseguite in una determinata tabella, l'amministratore del database deve prima **creare un indice full-text nella tabella in questione**.
L'indice full-text include **una o più colonne** basate su caratteri nella tabella. In queste colonne possono essere presenti i seguenti tipi di dati: char, varchar, nchar, nvarchar, text, ntext, image, xml, o varbinary(max) e FILESTREAM. Ogni indice full-text consente di **indicizzare una o più colonne della tabella** e ciascuna colonna può essere utilizzata con una lingua specifica.
**Attraverso le query full-text è possibile eseguire ricerche linguistiche rispetto ai dati di testo contenuti negli indici full-text, utilizzando parole e frasi in base alle regole di una determinata lingua**, come ad esempio l'inglese o il giapponese.
Le query full-text possono contenere semplici parole e frasi oppure più forme di una parola o frase. Una query full-text restituisce **qualsiasi documento contenente almeno una corrispondenza** (nota anche come **riscontro**).
Si ottiene una corrispondenza quando un documento di destinazione contiene **tutti i termini** specificati nella query full-text e soddisfa qualsiasi altra condizione di ricerca, come ad esempio **la distanza entro i termini corrispondenti**.

## Funzionalità della ricerca fulltext

Dopo l'aggiunta delle **colonne a un indice full-text**, gli utenti e le applicazioni possono eseguire **query full-text sul testo contenuto all'interno delle colonne**. Queste query possono consentire la ricerca degli elementi seguenti:
* Una o più parole o frasi specifiche (termine semplice)
* Parola o frase in cui le parole iniziano con il testo specificato (termine di prefisso)
* Forme flessive di una parola specifica (termine di generazione)
* Una parola o frase vicina a un'altra parola o frase (termine vicino)
* Sinonimi di una parola specifica (thesaurus)
* Parole o frasi che utilizzano valori ponderati (termine ponderato)
Nelle query full-text viene utilizzato un set ridotto di predicati (**CONTAINS** e **FREETEXT**) e funzioni (**CONTAINSTABLE** e **FREETEXTTABLE**).

## Creazione e gestione di indici full-text

Le informazioni contenute negli indici full-text vengono utilizzate dal motore di ricerca full-text per compilare query full-text che consentono di cercare rapidamente parole o combinazioni di parole specifiche in una tabella. **In un indice full-text vengono archiviate informazioni su parole significative e sulla relativa posizione all'interno di una o più colonne di una tabella di database**. Un indice full-text è un tipo speciale di indice funzionale basato su token compilato e gestito dal motore di ricerca full-text per SQL Server. Il processo di compilazione di un indice full-text è diverso da quello di altri tipi di indici. Anziché costruire una struttura ad albero B basata su un valore archiviato in una determinata riga, il motore di ricerca full-text compila una struttura con indici invertito, in pila e compresso basata su singoli token dal testo indicizzato. La dimensione di un indice full-text è limitata solo dalle risorse di memoria disponibili del computer in cui viene eseguita l'istanza di SQL Server.
È consentito un solo indice full-text per tabella. Per creare un indice full-text su una tabella, quest'ultima deve contenere una colonna singola, univoca e non Null. È possibile compilare un indice full-text su colonne di tipo **char**, **varchar**, **nchar**, **nvarchar**, **text**, **ntext**, **image**, **xml**, **varbinary** e **varbinary(max)**.
Il processo di creazione e gestione di un indice full-text è definito **popolamento** (noto anche come ricerca per indicizzazione). Sono disponibili tre tipi di popolamento dell'indice full-text:
* popolamento completo
* popolamento basato sul rilevamento delle modifiche
* popolamento incrementale basato su timestamp

### Pattern creazione indice
```sql
CREATE FULLTEXT index ON table_name(fields_name_separates_with comma) KEY index index_name
```
*index_name* è (quasi) sempre la primary key.
Esempio:
```sql
CREATE FULLTEXT index ON table_name(field_1, field_2...) KEY index PK_table_name
```

##### FREETEXTTABLE
È una funzione utilizzata nella clausola FROM di un'istruzione SELECT di Transact-SQL per eseguire una ricerca full-text SQL Server in colonne indicizzate full-text che contengono tipi di dati basati su caratteri. Questa funzione restituisce una tabella con 0 o più righe per le colonne contenenti valori che corrispondono al significato e non solo all'esatta formulazione (grazie al fulltext), del testo specificato in *freetext_string*.
Le query che utilizzano **FREETEXTTABLE** restituiscono **un valore di classificazione per pertinenza (RANK) e una chiave full-text (KEY) per ogni riga**.

```sql
FREETEXTTABLE(table, (column_list), 'freetext_string', top_n_by_rank)
```
Esempio:
```sql
SELECT * FROM FREETEXTTABLE(AnaContatti, (nome, cognome), 'Chiara', 1000)
```
