---
tags:
  - PersonalKnowledgeManagement
---


Dataview permette di creare delle tabelle dinamiche a partire da dei metadati nel nostro Vault: in questo modo è possibile creare tabelle complesse e aggiungere molte funzionalità comode a Obsidian.
E' possibile quindi associare dei dati (tags, date, numeri…) ad ogni file markdown e poi effettuare delle query su questi ultimi.
Dataview è composto da due componenti principali:
## Annotation
Dataview effettua continuamente il parse di tutti i file markdown creando un suo indice interno in modo che le query su questi ultimi possano essere molto veloci.
L'annotation può essere effettuata a livello di pagina, sezione o perfino task:
### 1. Markdown formatter
I dati vengono forniti aggiungendo del codice YAML arbitrario racchiuso tra `---` e deve essere posizionato come prima riga del file markdown.
```
---
alias: "document"
last-reviewed: 2021-08-17
thoughts:
  rating: 8
  reviewable: false
---
```
Le seguenti sintassi sono tutte valide:
```
tag: one, two, three
tags: one, two, three
tags: ["#one", "#two", "#three"]
tags:
- one
- two
- three
```
Ricorda sempre di non utilizzare il cancelletto `#` nel metadata a meno di racchiuderlo tra virgolette.
Per aggiungere un link ad una pagina nello yaml è necessario racchiuderlo tra virgolette, quindi:
```
---
author: "[[Patricia Highsmith]]"
---
```
N.b. I valori racchiusi tra virgolette nello YAML frontmatter non sono visti da Obsidian nativo e conseguentemente non compariranno nel grafo, quindi ne i link alle pagine ne i tag saranno visti dai tool di Obsidian ma solo da Dataview.

### 2. Inline fields
Permettono di aggiungere i metadati direttamente nel documento utilizzando la sintassi `Key:: Value`
```
Some text, and then [Inline Field:: Value] [Another Inline Field On The Same Line:: With A New Value!]

Basic Field:: Value
**Bold Field**:: Nice!

- [ ] #task I am a task with [metadata::value]!
  - [X] I am another task with completed::2020-09-15

```
Per esempio se voglio aggiungere il field `author` che è un link ad una pagina esterna posso fare:
```
author:: [[Patricia Highsmith]]
```
Il valore `[[Patricia Highsmith]]` sarà quindi nel field `author` e anche nel field implicito `file.outlinks`.

Dataview aggiunge anche dei field impliciti come `file.name` per il nome del file o `file.size` per la sua dimensione. [Qui](https://blacksmithgu.github.io/obsidian-dataview/data-annotation/) si trovano tutti gli altri tag impliciti.

## Querying

Una volta che le pagine sono state annotate è possibile farne delle query per creare tabelle dinamiche, liste o anche elaborarle con Javascript.
Ci sono quattro modi per farlo:
### 1. Dataview Query Language (DQL)
Sintassi SQL-like che permette di fornire tutti i casi base. 

````
```dataview
TABLE|LIST|TASK|CALENDAR <field> [AS "Column Name"], <field>, ..., <field> FROM <source>
WHERE <expression>
SORT <expression> [ASC/DESC]
... other data commands
```
````

Per esempio voglio una tabella con due colonne: la pagina con il link e il tag *nome_tag* ma solo delle pagine che hanno tag *tag_loog_for*
````
```dataview
TABLE nome_tag WHERE tag = tag_loog_for
```
````

#### Viste
Supporta varie tipologie di vista:
1. **TABLE**: vista classica con una riga per ogni data e *n* colonne in base alle richieste. La prima colonna è sempre un link alla pagina, per ometterlo chiamare `TABLE WITHOUT ID`
2. **LIST**: lista di pagine che matchano la query
3. **TASK**: lista di task delle pagine che matchano la query
4. **CALENDAR**: Vista calendario

#### FROM
Il FROM permette di determinare da quali pagine prendere i dati: omettendolo la query viene effettuata su tutti i file del Vault altrimenti è possibile filtrare per cartelle, per tag per link e così via.

-   **Tags**: Per selezionare un tag e tutti i suoi sottotag utilizzare `FROM #tag`.
-   **Folders**: Per selezionare una cartella e tutte le sue sottocartelle utilizzare `FROM "folder"`.
-   **Single Files**: `FROM "path/to/file"`.
-   **Links**: Puoi selezionare tutte le note che puntano ad un file o che puntano a partire da un file:
	-  Tutte le pagine che linkano a una `[[note]]` usare `FROM [[note]]`.
	-  Tutte le pagine che linkano da una `[[note]]` usare `FROM outgoing([[note]])`.
Questi comandi sono concatenabili, per esempio `#tag and "folder"` ritorneranno tutte le pagine nella cartella `folder` con il tag `#tag`.
Per la negazione utilizzare il carattere `-`, per esempio `-#tag` esclude tutti i file con tag `#tag`.
N.B: il filtraggio per tag deve avvenire nella clausola `FROM` e non in quella `WHERE`.

#### WHERE
Permette di filtrare le pagine ottenute con il FROM su determinati campi, per esempio:
* File modificati nelle ultime 24 ore: `LIST WHERE file.mtime >=date(today) - dur(1 day)`
* Tutti i progetti non completati più vecchi di un mese:
```
LIST FROM #projects
WHERE !completed AND file.ctime <= date(today) - dur(1 month)
```
#### SORT
Ordina i risultati per uno o più campi
```
SORT date [ASCENDING/DESCENDING/ASC/DESC]
```
#### GROUP BY
Raggruppa i risultati su uno o più campi.
```
GROUP BY field
```
#### FLATTEN
Raggruppa un array di valori in una unica riga separata da virgola. Per esempio se ho un libro con n autori posso avere una riga per ogni libro raggruppando tutti gli autori in questo modo:

```
TABLE authors FROM #LiteratureNote
FLATTEN authors
```
#### LIMIT
Limita il numero di output a *n* valori.
```
LIMIT 5
```

### 2. Inline Expressions
Espressioni DQL che possono essere embeddate direttamente nel markdown e che saranno visualizzare in *Preview mode*. Per approfondire vedi [qui](https://blacksmithgu.github.io/obsidian-dataview/query/expressions/).
```
We are on page `= this.file.name`.
```
### 3. DataviewJS
Javascript API che permette di accedere all'indice interno di Dataview per poter fare delle query incredibilmente custom al costo di scrivere codice un po' più a basso livello.
```
```dataviewjs
dv.taskList(dv.pages().file.tasks.where(t => !t.completed));

```
### 4. Inline JS Expressions
Analogamente a sopra è possibile scrivere del Javascript anche inline:
```
This page was last modified at `$= dv.current().file.mtime`.
```

## Tag
Dataview permette di vedere i tag sia nello YAML frontmatter (esempio `tags: todo`) che nel corpo del file (es. `#todo`).
I tag del frontmatter, essendo senza cancelletto, non hanno l'auto completamento, funzione molto comoda di Obsidian per evitare duplicati.
Per dichiarare i tag con il "#" anche nello YAML utilizzare la seguente sintassi:
```
tags: ["#one", "#two", "#three"]
```
La soluzione migliore è aggiungere i tag nell'header del file nel caso di note atomiche mentre conviene aggiungerlo inline nel caso di note lunghe e complesse in quanto vedere parti di frase nella ricerca può essere utile.


## Esempi
### Fornire una quote random dalle note con un determinato tag
Le note con tag `#book` possono avere una o più field chiamati "quote." Voglio recuperare tutti questi field e mostrarne uno a random.

```js
let quotesList = []
// Ottengo tutte le pagine con tag #book e ne prendo i field "quote"
for (let page of dv.pages('#book').map(k => [k.quote]))
{
	// Per qualche motivo la ricerca per tag fornisce dei dati di cui fare [0]
	let quotesInPage = page[0];
	// Se ho almeno una quote le ciclo tutte e le aggiungo alla mia lista
	if (quotesInPage!=undefined)
		for (let quote of quotesInPage)
			quotesList.push(quote)
}
// Scrivo un elemento della lista che dipende dalla data corrente (così ogni giorno è diverso ma non è diverso ogni volta che si refresha la pagina)
dv.paragraph(quotesList[DateTime.now().toFormat("o") % quotesList.length])
```

### Fornire una quote random dalle note di una folder
Voglio come sopra ma tra tutte le note all'interno di una determinata folder.
Le query per folder hanno doppie virgolette, per esempio `dv.pages('"Resources"')`.
```javascript
let quotesList = []
// Non uso map in quanto voglio avere anche le altre property della page, per esempio il link
for (let page of dv.pages('"Resources"')) {
	// Con il metodo pages tutti i field sono aggiunti come property all'oggetto page
	let quotes = page.quote;
	// Se ho almeno una quote aggiundo l'oggetto e il link alla pagina
	if (quotes!=undefined)
		quotesList.push({file: page.file.link, quote:quotes})
}
let dayOfTheYear = DateTime.now().toFormat("o");
let chosenItem = quotesList[dayOfTheYear % quotesList.length];
let chosenFile = chosenItem.file;
let chosenQuote = chosenItem.quote;
// Qualora la pagina abbia un elemento singolo la quote è un elemento, se invece sono due o più è un array. Se è un array ne prendo quindi un elemento random con lo stesso metodo di cui sopra.
if (dv.isArray(chosenQuote))
	chosenQuote = chosenQuote[dayOfTheYear % chosenQuote.length];

dv.paragraph(chosenFile)
dv.paragraph(chosenQuote)
```
