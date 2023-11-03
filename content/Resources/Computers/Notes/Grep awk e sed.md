---
tags:
  - Linux
  - PublishedPosts
---


In questo articolo tratto in maniera estremamente introduttiva i tre comandi fondamentali per l'elaborazione dei file in Linux, estremamente utili per la ricerca e l'elaborazione di file tramite terminale.

## 1. Grep
`Grep` viene utilizzato per **cercare un termine specifico all'interno di un file**.

Questo comando è molto utile quando voglio cercare velocemente **le linee di un file (o genericamente di uno stream in uscita da un comando) che matchano una certa espressione**.

Può fornire inoltre informazioni aggiuntive, come il numero di righe, il numero di match, il nome del file e così via.

Per esempio posso scrivere

```shell
$ grep This file.txt
Every line containing "This"
Every line containing "This"
```

che cerca tutte le linee contenute nel file `file.txt` che contengono la parola `This`.

E' importante sottolineare che **il comando grep supporta nativamente le espressioni regolari**.

E' possibile evitare l'escaping dei caratteri speciali per le regexp usando l'opzione `-E`.

### 1.1 Opzioni utili

| opzione | significato |
|--------|--------|
|`-i`|Case insensitive|
|`-w`|whole word: cerca solo parole intere e non sottostringhe|
|`-R`|ricerca ricorsiva tra i file di un path|
|`-v`|Inverso: mostra le linee che **non** matchano|
|`-c`|Count: conta le linee che matchano|
|`-l`|mostra solo il nome del file che matcha|
|`-o`|Mostra solo il contenuto matchato e non tutta la linea|
|`-n`|Mostra anche il numero di linea oltre che all'output standard|
|`-E`|Extended regexp: permette l'utilizzo di caratteri per regexp [`()...`] senza usare l'escape|

Un esempio di comando grep comodo è il

```shell
grep -Rin pattern path/to/search
```

che permette di ricercare ricorsivamente tra tutti i file e le sottodirectory del path indicato, un determinato pattern, case insensitive ed indicandone il numero di riga.

## 2. Awk

`awk` (come `sed`) è completamente diverso da grep in quanto è un processore di testo: conseguentemente non ha solo l'abilità di trovare una espressione che sto cercando all'interno di un testo, ma possono anche **rimuovere, aggiungere e modificare il testo del file stesso.

awk viene usato in particolare per estrarre dati e reportistica**.

In particolare `awk` è un **intero linguaggio di programmazione** costruito originariamente attorno ai file CSV, è **molto potente ma è complesso da usare**, soprattutto per i task semplici.
Un esempio è il seguente

```shell
$ awk '{print $2}' file.txt
```
che permette di printare la seconda colonna del file `file.txt`.

`awk` permette di eseguire compiti molto complessi, per esempio assumiamo di avere il file `file.txt` che contiene i numeri 10, 20, 60.

Il seguente codice permette di ottenere il valore medio dei numeri contenuti in tale file

```shell
$ awk 'BEGIN {sum=0; count=0; OFS="\t"} {sum+=$2; count++} END {print "Average:", sum/count}' file.txt
Average: 30
```

## 3. Sed

`sed` (come `awk`) è un processore di testo. Risulta molto utile quando voglio **eseguire dei cambiamenti nel contenuto di un file secondo una determinata espressione regolare**.

E' meno espressivo di awk ma è più semplice da usare, soprattutto per i compiti piccoli.

Per esempio il seguente codice
```shell
$ sed -i 's/cat/dog/' file.txt
```
permette di sostituire tutte le occorrenze di "cat" con "dog".