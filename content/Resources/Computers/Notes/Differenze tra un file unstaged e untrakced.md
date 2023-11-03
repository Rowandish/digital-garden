---
tags:
  - Git
  - PublishedPosts
---


Esistono tre aree distinte in `git`, la **working directory**, che sono tutti i file su cui sto effettivamente lavorando, **l'area di staging** e la **git directory**, che è una cartella *.git/* nella directory attuale in cui vengono salvate tutte le informazioni sulla repository (branch, tag, remote..).
L'area di staging memorizza **tutte le informazioni che verranno salvate nel prossimo commit**.

![](https://qph.is.quoracdn.net/main-qimg-c37b1af0f0854db3e07553803c1c9d77)

Ricapitolando, io lavoro nella working directory, il comando `git add` permette di portare i file modificati nell'area di staging. Il comando `git commit` permette successivamente di portare i file modificati dall'area di staging alla cartella *.git/*.
In una cartelle di lavoro, posso avere i file in tre stati distinti (controllabili tramite il `git status`):

- **untrakced**: il file non era presente nello scorso commit, è stato conseguentemente creato ma **non appartiene ad alcuna repository**. Il file non comparirà nel prossimo commit.
- **unstaged**: il file è presente nella repository ma **non è stato portato nell'area di staging**. Le modifiche non compariranno nel prossimo commit.
- **staged**: il file è stato modificato e questo **si trova nell'area di staging**. Conseguentemente tali modifiche compariranno nel prossimo commit.

Come scrivevo, il comando `git add` permette di far passare un file dall'area dalla working directory all'area di staging, qualora volessi effettuare l'operazione opposta eseguo un `git reset --filename` (per approfondire vedi la prossima sezione).

![](http://i.stack.imgur.com/XwVzT.png)