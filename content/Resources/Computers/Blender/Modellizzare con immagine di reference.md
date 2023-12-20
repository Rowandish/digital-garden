---
tags:
  - Blender
---
* Usare la visualizzazione dall'alto con `1`.
* Aggiungere immagine di reference con `Shift+A` -> `Reference Image`
* `Data` -> `Depth` -> `Back` in modo che l'immagine sia dietro alla griglia.
* Dove lavoro deve essere al centro dell'origine degli assi, quindi spostare l'immagine con `G+X` in modo che l'asse blu sia centrato verticalmente sul pezzo
![[Pasted image 20231122112405.png]]
* In questo caso il pezzo ha una base tonda, quindi procedo con il creare un cerchio con il solito `Shift+A` e lo sposto e lo scalo in modo che sia coincidente con la base del pezzo.
* Premere `Tab` e lavorare sempre in edit mode.
* Qui è tutto in lavoro di Extrude (`E+Z` in Edit mode) + Scale (`S` in edit mode) + [[Edge loop]] (`Ctrl+R` in edit mode) per rendere più sharp le divisioni tra una sezione e l'altra.
* Aggiungere un [[Subdivision Surface Modifier]] (parametri 3,3 per esempio) e  [[Shade Smooth]].
