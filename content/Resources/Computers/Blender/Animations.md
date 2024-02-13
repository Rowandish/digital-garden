---
tags:
  - Blender
---
In Blender si può animare qualsiasi property di qualsiasi oggetto usando il concetto di keyframe: Un keyframe è un frame della nostra animazione in cui imponiamo un valore di una determinata proprietà. Dati due keyframe in cui la stessa proprietà deve assumere due valori definiti, Blender si occuperà dell'interpolazione.
Le due interfacce fondamentali sono la `Timeline view` (`Shift+F12`) e il  `Graph Editor` (`Shift+F6`): la prima permette di visualizzare i keyframe e far partire l'animazione, la seconda per gestire il processo di interpolazione.

Il numero di frame complessivi, come gli fps, li posso impostare nelle [[Esportare un video|output properties]].
## Impostare un keyframe
Per esempio assumiamo di avere 180 frame (che a 25fps corrispondono a 7.2 secondi) e di voler ruotare di 360° un oggetto sull'asse Z.
Usare la `Timeline view` per spostarci nel frame di interesse (in questo caso il primo frame), modifichiamo il valore di Z di Rotation a quello che vogliamo e poi, sulla property, `tasto dx -> Insert Keyframe`. 
![[Pasted image 20240111111243.png]]
Andiamo ora all'utlimo frame, in questo caso 180, e sommiamo 360 al valore di Z precedente e aggiungiamo il keyframe anche qui.
Ora premendo il tasto Play vedremo il nostro oggetto che ruota di 360° lungo tutti i 180 frame con un interpolazione non lineare ma `Bezier`.

## Modificare l'interpolazione
Spesso può risultare necessario modificare l'interpolazione dei frame ad una più congeniale.
Per farlo premere `Shift+F6` e andare in `Graph View`.
Espandendo l'animazione si vede di cosa è composta: in questo caso è una animazione di rotazione che è composta solo dalla Z (che si vede nel grafico) mentre X e Y sono rette piatte.
![[Pasted image 20240111111903.png]]
Per modificare l'animazione selezionare tutti i keyframe con `A` e fare `tasto DX -> Interpolation Mode`.
![[Pasted image 20240111112141.png]]
Attenzione che se non si selezionano i keyframe non succede nulla.