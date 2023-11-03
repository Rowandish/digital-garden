<div class="iframe-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/YOUTUBEID" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


* Eliminare Camera e Luci
* Scrivere un testo come spiegato all'inizio di [[Testo 3D in Blender]]
* Impostarne la Depth a 0,01.
* Premere il tasto "ò" e andare TOP
![[Pasted image 20231027182857.png]]
* `Shift + A -> Add Camera`. Comparirà una Camera esattamente sopra il testo
![[Pasted image 20231027183050.png]]
* `Shift + A -> Curve -> Circle`
* `Shift + A -> Light -> Point`
* Allargare di un pelo la circonferenza della luce, lui la crea puntiforme
![[Pasted image 20231027183955.png]]
* Con la luce selezionata: `Constraint -> Add Object Constraint -> Follow Path -> Target` selezioniamo il cerchio inserito prima.
* Selezioniamo il cerchio e giochiamo con la scala in modo che circondi la scritta non allontanandosi mai troppo dai bordi
![[Pasted image 20231027183747.png]]
* Nella finestra dell'animazione impostiamo come end frame 120
![[Pasted image 20231027183947.png]]
* Verificare di essere al frame 1, selezionare il punto luce e fare tasto DX dove c'è offset del `Constraint -> Insert Keyframe`
![[Pasted image 20231027184204.png]]
* Andare all'ultimo frame, scrivere nell'Offset 100 e poi `Tasto dx su offset -> insert keyframe`.
![[Pasted image 20231027184334.png]]
> [!warning] Attenzione
> Prima devo scrivere l'offset e **dopo** fare insert keyframe (che deve essere l'ultima operazione). Se prima inserisco il keyframe e poi scrivo l'offset non funziona nulla.
* Per avere un'anteprima dell'effetto premere in alto a destra sul pulsante `Viewport Shading`
![[Pasted image 20231027185011.png]]
* `World -> Background -> Black`
* `Material -> New -> Metallic -> 1`
* `Render -> Bloom`
![[Pasted image 20231027185505.png]]
* *`Render -> Screen Space Reflections`
* Selezionare la luce -> Power -> 50W
![[Pasted image 20231027185746.png]]
* Spostare la curva della luce un pelo sotto la scritta (usando il solito Transform -> Location -> Z) e facciamola un po' più grande
![[Pasted image 20231027190240.png]]
* (opzionale) Selezionare la luce e farla di un altro colore e potenza 100W
* Selezionare la scritta: `Material -> Roughness -> 0,360`