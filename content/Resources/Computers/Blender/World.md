---
tags:
  - Blender
---
Il pulsante `World` permette di definire lo sfondo dell'oggetto che voglio renderizzare.
![[Pasted image 20231121142926.png]]

## Sfondo nero
Qualora volessi uno sfondo nero basta andare su Color e impostare nero. In questo modo l'oggetto renderizzato avrà tale colore di sfondo.

## Sky Texture
Per avere uno sfondo più realistico con anche la luce solare posso utilizzare `Sky Texture`
![[Pasted image 20231121143014.png]]
Ottengo qualcosa di analogo a questo (visualizzando in render view ovviamente)
![[Pasted image 20231121143357.png]]
Posso modificare l'altezza e l'intensità del sole, la sua dimensione e rotazione in modo che la luci arrivi coerentemente con quello che voglio.
Per visualizzare bene il render con il cielo e il sole ho bisogno di Cycles come [[Render Engines]] che è molto lento ma più realistico e usare `Ctrl+B` per limitare l'area dove fa il render in modo da rendere il processo più veloce (solo in modalità visualizzazione telecamera, quindi tasto `0`)

![[Pasted image 20231121144602.png]]