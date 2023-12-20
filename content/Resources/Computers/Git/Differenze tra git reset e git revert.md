---
tags:
  - Git
  - PublishedPosts
---


Questo articolo è una libera traduzione di questo [tutorial di atlassian](https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting).

### Reset
Il comando git reset **permette di spostare il puntatore alla testa di un branch ad un commit differente** e questo può essere usato per due scopi:

- per rimuovere dei commit dal mio branch corrente
- per rimuovere i file in staging

Il comando seguente permette di spostare il branch `hotfix` di due commit indietro

```bash
git checkout hotfix
git reset HEAD~2
```

Questo significa che i due commit finali di `hotfix` ora diventano dei commit pendenti, che verrano eliminato dal *[[Garbage Collector]]* di git.
`git reset` è comodo per eliminare cambiamenti, anche committati, **che non sono stati condivisi con nessuno**; questo è inoltre spesso usato per far **tornare i file che sono nell'area di staging, unstaged** (lasciando le modifiche nella working directory) con
```bash
git reset --mixed HEAD
```
oppure per **eliminare tutte le modifiche che non sono state committate**, con
```bash
git reset --hard HEAD
```
Il comando `git reset` può essere usato anche su singoli file, e non sul contenuto di un intero commit, per esempio
```bash
git reset HEAD foo.py
```
porta a unstaged il file *foo.py* (senza modificarlo nela working directory).

Attenzione che il comando `git reset` con un commit diverso da HEAD **riscrive la commit history**, che è un comportamento da evitare nei branch pubblici, mentre è possibile effetuare tale modifica invece nei branch locali.


### Revert
Il `revert` è un comando più "soft" di `reset`, in quanto annulla un commit creando **un nuovo commit**. Questo è un modo sicuro per annullare i cambiamenti apportati (che sono stati già committati) in quanto **non ho la modifica della commit history**.
Per esempio il comando seguente annulla i cambiamenti effettuati negli ultimi due commit creando un nuovo commit che annulla tali modifiche senza modificare i commit precedenti.
```bash
git checkout hotfix
git revert HEAD~2
```
Dato che questo comando non modifica la commit history, è consigliabile usarlo, al posto di `git reset`, in una repository condivisa.
Posso anche pensare a `git revert` come un modo sicuro di annullare modifiche committate, mentre `git reset HEAD` le modifiche non ancora committate.
