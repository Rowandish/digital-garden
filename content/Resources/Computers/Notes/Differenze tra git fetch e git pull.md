---
tags:
  - Git
  - PublishedPosts
---


Un `git pull` è banalmente **un git fetch che viene successivamente seguito da un git merge**.
Quando uso un `git fetch`, git **raccoglie tutti i commit da un branch che non esiste nel tuo branch di riferimento e li salva nella repository locale** (che è la cartella *.git/*). Questo però senza fare il merge di tale branch remoto con il mio branch attuale (non modifica nulla nell'working tree, che è tutto ciò che non in *.git/*).
Questo comportamento è particolarmente utile quando voglio mantenere la mia repository aggiornata, ma il lavoro che sto facendo potrebbe rompere qualcosa se io unissi il contenuto remoto con il contenuto locale. Per integrare i commit scaricati al mio branch, devo eseguire un `git merge`.
Quando uso il `git pull` invece, **git prova automaticamente a fare il merge dei commit recuperati tramite il fetch nel mio branch locale** (quindi prima aggiorna la local repository *.git/* e successivamente anche il working tree), senza prima farmi vedere quello che sta effettivamente unendo. A meno che non abbia una frequente analisi dei branch, **il pull può portare a numerosi conflitti**.