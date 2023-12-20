---
tags:
  - Git
  - PublishedPosts
---


Questo articolo è una libera traduzione di [questo post](http://gitolite.com/detached-head.html).

Git ha uno stato chiamato '**detached HEAD**' che all'inizio risulta di difficile comprensione.

L'unica notizia che viene subito fornita ai programmatori è di **non committare su una detached HEAD**. In questo articolo cerchiamo di spiegare meglio il funzionamento di questo dettaglio di git.

## L'oggetto HEAD
Partiamo con la descrizione di **HEAD**: questa è tipicamente un puntatore all'ultimo commit di un branch.

Per visualizzare dove punta l'**HEAD** attuale basta eseguire un
```bash
cat .git/HEAD
>> ref: refs/heads/master
```
che indica che l'**HEAD** attuale punta all'ultimo commit del master.
Ora, quando cambio branch tramite un
```bash
git checkout branchname
```
**HEAD** punterà quindi all'ultimo commit di '*branchname*', e questo significa che il comando eseguito in precedenza fornirà i seguenti risultati:
```bash
cat .git/HEAD
>> ref: refs/heads/branchname
```
Questo è il comportamento standard.

## Detached-HEAD

Ora, assumiamo di voler visualizzare lo stato del codice ad un nodo del grafo che **non è l'ultimo commit di un branch locale**, questo porta al fatto che **HEAD** non è più un puntatore all'ultimo commit di un branch locale, ma è un puntatore allo SHA-1 di un commit specifico.

Questo stato è detto di **detached HEAD**, in quanto **ogni commit che viene eseguito in questo stato non appartiene a nessun branch** (oppure possiamo considerarlo come appartenente ad un **branch anonimo**).

Se così non fosse, un commit eseguito dopo un checkout ad un nodo del grafo che non è l'ultimo, eliminerebbe tutti i nodi successivi.

Per esempio i seguenti comandi portano tutti ad uno stato di **detached HEAD**:
```bash
git checkout master^ # parent of master
git checkout HEAD~2 # grandparent of current HEAD
git checkout origin/master # a non-local branch
git checkout tagname # since you cant commit to a tag!
```

## Recuperare da uno stato di detached HEAD
Qualora incontrassi l'errore tipico di effettuare alcuni commit in uno stato di **detached HEAD** (e quindi su un branch anonimo), posso recuperare facilmente con il seguente comando:
```bash
git checkout -b newbranch
```
che crea un nuovo branch chiamato '*newbranch*' spostando tutti i commit in questo branch. Il branch anonimo ora diventa un branch classico.

## Come recuperare dei commit perduti
Assumiamo ora di non accorgersi di stare committando in un branch anonimo e di cambiare branch:
```bash
git checkout someoldbranch
```
Ora **HEAD** è un riferimento simbolico a '*someoldbranch*' e il suo valore precedente (lo SHA-1 dell'ultimo commit eseguito in **detached HEAD**) è stato sovrascritto.
Per come sono descritte le cose sembra che i commit ora siano definitivamente persi, ma per fortuna così non è.
I commit infatti esistono ancora da qualche parte, bisogna solo andargli a recuperare.
Git possiede un comando chiamato '`reflog`' che permette di recuperare tutto quello che è stato fatto sulla repository negli ultimi 30 giorni, soprattutto lo SHA-1 del commit perduto.
```bash
git reflog show HEAD@{now} -10

dcd215b... HEAD@{5 minutes ago}: commit (amend): 0-terminology: the malloc analogy added, plus
5ce8bfe... HEAD@{11 minutes ago}: commit: 0-terminology: the malloc analogy added, plus
3d93420... HEAD@{11 minutes ago}: rebase -i (pick): updating HEAD
7fdae94... HEAD@{11 minutes ago}: checkout: moving from master to 7fdae94815d6c676742c9984132b7b9e71a57f98
3d93420... HEAD@{13 minutes ago}: rebase -i (squash): updating HEAD
c55900c... HEAD@{13 minutes ago}: rebase -i (pick): updating HEAD
7fdae94... HEAD@{13 minutes ago}: checkout: moving from master to 7fdae94815d6c676742c9984132b7b9e71a57f98
e9955c8... HEAD@{14 minutes ago}: commit: s
97ab644... HEAD@{20 minutes ago}: commit: autogen
c55900c... HEAD@{23 minutes ago}: commit (amend): 0-terminology: the malloc analogy added, plus
```
Una volta trovato lo SHA-1 che mi serviva, andiamo a recuperarlo e inseriamolo in un nuovo branch:
```bash
git branch thank_God_its_safe 7fdae94
git checkout thank_God_its_safe
```