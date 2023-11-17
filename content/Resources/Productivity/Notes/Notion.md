Notion è una piattaforma che permette di organizzare note, task, eventi e così via.
Questo collegamento tra dati condivisi, compiti, eventi del calendario, risorse informative e altri asset digitali permette di ottenere un nuovo livello di performance personale e professionale, eliminando la ridondanza dell'informazione in luoghi diversi.
A differenza di altri strumenti, Notion non fornisce una struttura predefinita: La sua potenza e, al contempo, fonte di frustrazione per i nuovi utenti, risiede nella libertà di progettare il proprio sistema. Ciò richiede non solo di imparare il software, ma anche di padroneggiare la progettazione del sistema.

Vediamo alcuni concetti:
* **Workspace**: macrocontenitore di oggetti. Ogni account parte con un solo workspace ma mano a mano che l'ecosistema si ingrandisce si possono gestire vari workspace in base al topic (personal, work) e/o in base alle persone con cui si condividono
* **Sidebar**: pannello di controllo laterale con varie categorie. Compaiono le pagine di top level e le pagine preferite.
* **Page**: Notion è organizzato in `pages` che possono essere sia contenuto che contenitori di altre `subpages`. Le pagine di top level appaiono nella sidebar.
## Block

Una pagina è formata da vari blocchi chiamati appunto `block`.
Con questi mattoncini posso fare varie cose come si vede nell'immagine.
Ogni cosa in Notion è un `block`, dai database alle viste al semplice testo e ogni `block` può essere gestito indipendentemente dagli altri.

![[Pasted image 20231102100237.png]]

Un `block` inoltre essere trasformato facilmente in un blocco di un altro tipo.

![[Pasted image 20231102105533.png]]

### Block comodi
* `Reminder`: permette di segnarsi qualcosa da fare con un reminder ad una certa data/ora
* `To do list`: permette di inserire una lista di checkbox spuntabili
* `Embedd`: permette di embeddare qualsiasi cosa, per esempio un video YouTube.
* `Toggle`: permette di avere del testo nascosto da mostrare alla pressione del mouse

## Column
Notion permette una divisone del contenuto di una pagina in colonne, per ottenerla basta selezionare gli oggetti che vogliamo e con il mouse spostarli verso i lati della pagina.
Notion creerà così una struttura a colonne molto comoda per la visualizzazione.

## Link
Notion permette di scrivere link che vanno da una pagina all'altra (stile Obsidian) in modo molto semplice.
Se vogliamo linkare una pagina basta scrivere `[[` e con l'autocompletamento selezionare la pagine che vogliamo.
Dato che non solo le pagine ma anche i `block` sono linkabili posso referenziarli in maniera semplice facendo `tasto dx -> copy link to block` e incollare tale link nella pagina in cui voglio referenziarlo.
In particolare, una volta incollato, posso fare 3 cose:
* `Dismiss`: incolla il link grezzo
* `Paste and sync`: scrive esattamente il contenuto del blocco referenziato ma sincronizzandolo, quindi se il blocco in questione cambia, vedrò il cambiamento anche in questa pagina
* `Mention block`: aggiunge solo un link di referenza al blocco (come per una pagina) ma senza mostrarne il contenuto.

## Database
I database sono degli elementi fondamentali che corrispondono a degli `Spreadsheet`, analogamente come le `pages` corrispondono a dei file Word.
Ogni colonna è una property del database che può essere di vario tipo (es. testo, tag, data...).
La cosa importante da sottolineare è che ==ogni riga di un database è di fatto una pagina==, con tutte le caratteristiche della pagina stessa.

### Visualizzazioni
Ogni database può essere visto sia nella modalità standard come spreadsheet (visualizzazione `Table` che in altre modalità, per esempio Board o Calendar.
![[Pasted image 20231102155821.png|250]]
Dato che sono solo delle diverse View della stessa cosa, posso averne più di una contemporaneamente. Dato un database posso aggiungere una nuova View tramite il tasto `+` in alto come si vede nell'immagine.
![[Pasted image 20231102160301.png]]
Per ogni visualizzazione posso anche decidere di visualizzare solo un sottoinsieme di colonne tramite le opzioni.

#### Calendar
Per esempio se scegliamo Calendar questo verrà mostrato seguendo una property del database di tipo Datetime.
Per esempio la visualizzazione in modalità Calendar di questo database
![[Pasted image 20231102160042.png]]
è questa 
![[Pasted image 20231102160115.png|350]]

#### Board
Visualizza il database come se fosse una Kanban, tipicamente visualizzando gli oggetti tramite colonne che sono i loro tag.

#### Esempio
In questa immagine si vede bene un esempio di come poter utilizzare un database, in questo caso che descrive i prossimi video da girare
![[Pasted image 20231102160519.png]]
Posso avere le view Calendar dove vedo sul calendario delle property DateTime, come per esempio quando devo pubblicare o quando devo filmare; posso avere una view Board per visualizzare lo stato dei vari video e sposarli da uno stato all'altro e così via.


### Linked view of Database
Posso creare delle view di un database non solo nella pagina del db stesso ma anche in altre pagine che servono solo per quella specifica pagina.
Per esempio nella pagina "compleanni" posso creare una linked view di un db contenente la mia rubrica visualizzando solo nome e compleanno.

### Relation

Analogamente al concetto di FK nei DBMS, posso linkare due database (che di fatto solo due tabelle) tramite una colonna di tipo `Relation`.
![[Pasted image 20231102164546.png|400]]

![[Pasted image 20231102164706.png|400]]

### Rollup
Questa colonna prende come riferimento una colonna di tipo `Relation` e effettua dei calcoli in base a quello che scegliamo.
![[Pasted image 20231102164935.png|350]]

### Formula
Formula è una tipologia di colonna che permette di aggiungere degli script in modo da visualizzare dei dati calcolati.
Può essere banalmente da una stringa convertirla in emoji ma anche cose complesse come calcolare l'età di una persona a partire dalla data di nascita e così via.

### Filters
Di un database posso creare dei filtraggi personalizzati (come fossero dei `WHERE` in modo che possano essere riutilizzati anche in futuro.
Ogni view di un database può contenere solo un filter cliccabile.

## Templates

Come dice il titolo permettono di creare dei template comuni in modo da velocizzare la creazione di contenuti senza copincollare nulla.
Per esempio assumiamo di voler scrivere un video di YouTube, posso creare un template che mostra tutti gli step da fare, cosa dire, le thumbnail, chi contattare... in modo da avere una roadmap pronta e dover solo "completare" gli step, che sono standard e ben definiti.
![[Pasted image 20231102165452.png|300]] ![[Pasted image 20231102165511.png|300]]
Posso anche prendere Template fatti da altri presenti sull'internet.

## Button
Tra i vari comandi di Notion c'è anche la possibilità di aggiungere un pulsante che permette di fare cose, per esempio aggiungere del testo, delle pagine, andare ad una determinata pagina e così via.
![[Pasted image 20231102170058.png]]
Per esempio assumiamo di avere una pagina che contiene tutti i daily highlight: ogni giorno dovremo duplicare il blocco del giorno precedente, cancellare il testo e inserirne di nuovo.
Posso invece creare un button che, una volta premuto, inserisce sopra di esso il template per il daily highlight, già pronto per essere completato.


## Shortcut comodi
* `ctrl+P`: cerca globale
* `Shift+Enter`: va a capo ma mantenendo il blocco corrente senza crearne uno nuovo
* `/`: apre la finestra di scelta dei block
* `ctrl+\d`: Trasforma il blocco nell'heading corrispondente
* `[[`: permette di inserire il link ad una pagina o ad un blocco, stile Obsidian

## Apption.co

[Apption](https://apption.co/)  fornisce una collezione di widget embeddabili in Notion, per esempio orari, grafici social, tempo metereologico e così via.
Per esempio potrei embeddare il mio Google Calendar.

## Creare siti
Posso creare anche interi siti web in Notion usando la piattaforma [Super.so](https://super.so/): basta creare una pagina su Notion e poi condividerla. [Posso creare anche blog](https://super.so/guides/how-to-create-a-blog-with-super-and-notion).
Un'alternativa è [Simple.ink](https://www.simple.ink/).
Per un confronto vedi [questo link](https://super.so/blog/simple-ink-alternative) e [questo](https://www.simple.ink/super-alternative).


## Resonance Calendar
Posso creare Database in Notion contenente una lista di cose interessanti che trovo su internet o ascolto/vedo.
Per quello che leggo su internet posso usare il Notion Web Clipper, per quello che consumo con il cellulare posso fare `Shape -> Notion` (assumendo di avere Notion installato) e aggiungere il contenuto sempre allo stesso database.
### Notion Web Clipper
Questo plugin per Chrome permette di creare una pagina in Notion a partire da una pagina Web.
Per esempio potrei creare un database contenente tutti le pagine che voglio salvare con questo plugin e linkarlo a questo ultimo, in questo modo quando leggo qualcosa di interessante posso portarlo direttamente in questo database in Notion.

## Youtuber
Per quanto riguarda Notion son 3 gli youtuber principali:
* [August Bradley](https://www.youtube.com/@augustbradley/)
* [Ali Abdaal](https://www.youtube.com/@aliabdaal)
* [Thomas Frank](https://www.youtube.com/@Thomasfrank)

## Link utili

* [Template notion di Ali Abdaal](https://aliabdaal.notion.site/Ali-Abdaal-s-Skillshare-HQ-d6c16b42c87e4581a29c4b2171c04f34)
* [Pillars Pipeline and Vaults di August Bradley](https://lifedesignstudio.notion.site/Pillars-Pipelines-Vaults-PPV-Notion-Resources-18141b8394694b3a910dbe7c89a901b9)



