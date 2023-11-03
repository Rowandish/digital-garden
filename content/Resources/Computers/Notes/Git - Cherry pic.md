---
tags:
  - Git
  - PublishedPosts
---


Questo articolo è una libera traduzione di quanto trovato in
[questo articolo](http://think-like-a-git.net/sections/rebase-from-the-ground-up/cherry-picking-explained.html)
* * *
Git possiede un comando estremamente potente dal nome singolare: `git cherry pic`.

La documentazione su tale comando è chiara: **dato uno o più commit (qualsiasi) del grafo rappresentante la repository, applica i cambiamenti apportati da ognuno ad un branch, creando un nuovo commit per ognuno di essi**.

Per capire bene il funzionamento è importante sottolineare che **un commit è identificato univocamente sia dal suo contenuto che dalla sua storia**.

Conseguentemente due commit che hanno lo stesso contenuto ma che hanno due padri diversi, per git sono trattati come due commit diversi, senza alcuna relazione tra di loro.

Il comando `cherry pic` prende in ingresso un commit (per semplicità lavoro con un singolo commit, la discussione poi è analoga per *n* commit) e **applica i cambiamenti che questo ha effettuato sul commit padre, ad un qualsiasi nodo foglia del grafo**, creando un nuovo commit con un nuovo SHA-1.

Assumiamo di avere il seguente grafo:

![](http://think-like-a-git.net/assets/images2/reachability-example.png)

Assumiamo che l'**HEAD** punti al nodo **H** del grafo. Effettuando un
```
git cherry-pick E
```
creerò un nuovo nodo del grafo figlio di **H** chiamato **E'**, che apporterà ad **H** i cambiamenti che **E** ha apportato a **D**.

![](http://think-like-a-git.net/assets/images2/cherry-pick-example-1.png)