---
tags:
  - Blender
---
## 📺 Video
<div class="iframe-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/6oXkRIN_t0Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div class="iframe-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/3eJmISziyIY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


Spesso può risultare utile creare un video di un modello 3D che ruota in una su uno o più assi.
Per farlo basta seguire i seguenti passi
* Aprire il modello 3D con blender (eliminare il cubo di default che compare)
* Importare il modello 3D
* Spostare la telecamera e la luce vicino al modello (non riesco a farlo col mouse, per farlo modificare le coordinate degli oggetti con l'interfaccia che compare premendo N)
![[Pasted image 20231025170424.png]]
* Dato che a volta il modello 3D è formato da *n* parti distinte, conviene unirle tutte in un unico livello in modo che poi si muovano in modo solidale, per farlo selezionare tutto, tasto dx -> Join ![[Pasted image 20231025170558.png]]
* Selezionare l'oggetto `Object -> Set Origin -> Geometry To Origin `
![[Pasted image 20231025174508.png]]
* Selezionare quindi il modello 3D, premere N, andare nell'asse che si vuole ruotare (es. X, Y, Z o anche più di uno) e scrivere `#frame`. In questo modo il valore del campo dipende dal frame e non è un valore assoluto. Se si vuole rallentare si può fare `frame/30` o il valore che si vuole.
* Verificare con il navigatore sotto il modello che questo si muova come ci aspettiamo
* Andare nella finestra laterale nell'icona per l'output e impostare i valori indicati
![[Pasted image 20231025170944.png]]. Il frame end va calcolato in modo che la rotazione sia completa alla fine del video.
* Esportare il video andando su `Render -> Render Animation`. Mentre fa l'animazione la esporta e dopo qualche secondo ci sarà nel path indicato. ![[Pasted image 20231025171128.png]]
* Per fare in modo che lo sfondo del video sia del colore che voglio (tipicamente nero) andare su `World -> Color -> RGB`.
* ![[Pasted image 20231025171827.png]]