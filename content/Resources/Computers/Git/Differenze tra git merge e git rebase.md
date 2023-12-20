---
tags:
  - Git
  - PublishedPosts
---


Per spiegare la differenza tra questi due comandi, prendiamo ad esempio queste immagini, prese da [questa](http://stackoverflow.com/questions/16666089/whats-the-difference-between-git-merge-and-git-rebase/16666418#16666418) domanda di Stackoverflow.
Supponiamo di avere un branch con 3 commit, `A`, `B` e `C`

![](http://i.stack.imgur.com/lJRq7.png)

Sullo stesso branch due sviluppatori hanno creato, a partire dal commit comune `C`, un commit `D` e un commit `E` che generano conflitti

![](http://i.stack.imgur.com/pK7Zb.png)

Questi conflitti devono essere risolti in qualche modo, git offre due possibilità.

### Merge
Viene creato un commit di merge `M` che è il frutto dell'unione dei cambiamenti apportati da `D` ed `E`

![](http://i.stack.imgur.com/9Ul5w.png)

I commit `D` ed `E` non vengono eliminati ed ho la formazione di una **struttura a diamante**, che molte persone ritengono confusionaria

### Rebase
Creiamo invece un commit `R` che nei contenuti è **identico** al commit sopra `M`, con la differenza che il commit `E` viene eliminato, come se non fosse mai esistito.

![](http://i.stack.imgur.com/pK7Zb.png)

A causa di questa eliminazione, la copia locale di `E` dello sviluppatore, deve essere immediatamente eliminata e non essere pushata in nessuna altra repository. Il vantaggio di usare rebase è che **evito la struttura a diamante ed la storia della repository mantiene una linea retta molto più chiara**.
Il problema di usare il rebase è che questo **cambia effettivamente la storia di una repository** che potenzialmente potrebbe essere una soluzione pericolosa (per esempio il fatto che il commit E non deve essere pushato).
Genericamente consiglio di usare il merge, a meno che non vi siano casi per cui non se ne possa fare a meno.