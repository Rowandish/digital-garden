---
tags:
  - Git
  - PublishedPosts
---


Questo articolo è una libera traduzione di quanto [trovato sula documentazione di git](https://git-scm.com/book/en/v1/Git-Tools-Stashing) a riguardo.

## 1. Introduzione
Spesso quando si sta lavorando ad un progetto, si potrebbe avere la **necessità di cambiare branch in breve tempo**.
Il problema è che git impedisce di cambiare branch se ho effettuato dei cambiamenti al codice non committati, per evitare che questi vadano persi nel cambio.
Allo stesso modo è scomodo e sbagliato committare un lavoro eseguito a metà solo per avere la possibilità di cambiare un branch.
Per risolvere questi problemi viene in aiuto git con il suo comando `stash`.
**Lo stashing prende tutto quello che è presente nella mia working directory** (quindi le modifiche tracked e i file nell'area di staging) **e li salva in uno "stash" di cambiamenti in sospeso**, che potranno essere recuperati in qualsiasi momento.
## 2. Aggiunta, visualizzazione e applicazione dello stash
Ora, assumiamo di aver lavorato su dei file nella working directory e di essere in questo stato:
```bash
$ git status
#
#
#
#
```
Ora, io voglio cambiare branch ma non voglio effettuare un commit di queste modifiche, effettuo quindi uno stash.
```bash
$ git stash
Saved working directory and index state \
"WIP on master: 049d078 added the index file"
HEAD is now at 049d078 added the index file
(To restore them type "git stash apply")
```
Ora la mia working directory è pulita:
```bash
$ git status
nothing to commit, working directory clean
```
Ora posso tranquillamente cambiare branch.
Per visualizzare tutti gli stash che ho memorizzato, basta utilizzato il `git stash list`:
```bash
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```
In questo caso ho tre stash memorizzati, posso applicare in qualsiasi di questi stash al commit attuale tramite il
```bash
git stash apply
```
che di default applica l'ultimo stash aggiunto alla lista.
Se volessi applicare invece uno degli stash più vecchi, posso specificarlo tramite il suo nome nel seguente modo:
```bash
git stash apply stash@{2}
```
Posso anche applicare uno stash ad un branch che non è il suo branch di origine, ci pensa git ad effettuare un merge eventuale dei conflitti.
Per eliminare uno stash posso usare il metodo:
```bash
git stash drop stash@{0}
```
con il nome dello stash da rimuovere.