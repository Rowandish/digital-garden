### Impostare un video di sfondo

In Elementor è possibile impostare lo sfondo di una sezione come video, utile nelle home page per fare un po' di scena in una hero section.
Questo quindi non è un elemento da aggiungere ad una pagina ma lo sfondo di una sezione.
Passaggi:
* Creare una sezione
* Impostarne l'altezza:
	* Se vogliamo il video a tutto schermo Height -> fit to screen
	* Se vogliamo solo un pezzo min height -> 500px (esempio)
* Style -> Background type -> Background video -> Scegliere un link ad un servizio esterno come YouTube oppure caricare il video nei media e copiarne il link 
* Impostarne Start e End time se il video è più lungo di quello che si vuole (e se si manda in loop)
* Impostare la fallback images che è l'immagine che viene visualizzata qualora il video non andasse 
* Impostare il background overlay qualora il video fosse troppo chiaro: Background overlay -> Color -> Black -> Opacity slider come si vuole
* Per un effettuo ulteriore posso aggiungere un colore di sfondo con opacità al 100% e giocare con il blend mode (esempio Multiply)

## Testo con due colori
Per avere un heading con due colori è necessario per prima cosa aggiungerlo e impostarne il colore principale.
Nel testo racchiudere le parole che voglio con colori diversi con il tag `<span>` con l'indicazione del colore, per esempio  `<span style="color:#fe667b;">Foo</span>`

## Image Hotspot

<div class="iframe-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/GlwuG8DAaDA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Con questo termine si identifica una immagine con dei "punti di interesse" che, su mouse hover o mouse click mostrano delle informazioni.
Per farlo ho bisogno dell' image widget e del flipbox widget.
* Creare una sezione con una colonna e aggiungere l'image widget
* Aggiungere nella stessa colonna un flipbox widget
* Cambiarne l'icona, per esempio un cerchio
* Rimuovere l'heading e description
* Front -> Background -> Color -> Click sul quadrato barrato -> Opacity -> 0
* Advanced -> Layout -> Width -> Custom -> 222px (esempio)
* Position -> Absolute
* Usare l'offset orizzontale e verticale per posizionarlo dove si vuole, importante usare valori in percentuale affinché sia responsive. Per verificarlo la colonna e il flipbox devono resizarsi allo stesso identico modo
* Content -> Back -> Modificare title e heading
	* Rimuovere il button text se non voglio bottoni
	* Background -> Type Classic -> Color -> #FFFFFF
* Style -> Front -> Icon Size -> dimensione che si vuole
* Style -> Back -> Title spacing -> 10 e title e description color -> Colore scuro
* Content -> Settings -> Height -> la dimensione che voglio del contenuto dietro
* Content -> Settings -> Flip Effect -> quello che si vuole, esempio Zoom
* Column -> Custom CSS -> `.selector{ margin: auto; }`
* Provare con la visualizzazione mobile e table e eventualmente giocare con Flipbox -> Settings -> Height custom per mobile o tablet
* \[Opzionale\] Flipbox -> Advanced -> Motion Effects -> Mouse Effects -> Mouse track opposite o direct e speed 0.3
* Duplicare il flipbox per ogni hotspot che voglio

https://elementor.com/help/hotspot-widget-pro/

<div class="iframe-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/WqYyIe6r10c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


### Counter
Questo widget permette di aggiungere dei contatori con i numeri che aumentano al passaggio dell'utente.
Ogni widget corrisponde ad un counter, quindi se ne voglio 4, esempio, devo aggiunger 4 colonne con un widget per ognuno.
Posso impostarne valore iniziale e finale e la durata dell'animazione.
* Number prefix: stringa che viene prefissa sempre, esempio se metto "1" il contatore partirà da 1StartingNumber e finirà a 1EndingNumber
* Number suffix: stringa che viene suffissa sempre (es. "+")
* Title: caption

### Subscribe
Per aggiungere uno spazio per iscriversi alla newsletter basta aggiungere un form (oppure prendere un blocco prefatto e modificarlo).
Per aggiungere la checkbox che verifica che ho letto le condizioni (per il GDPR) aggiungere un nuovo item al form e selezionare il tipo "Acceptance".
Mettendo nel "Acceptance text" un test con dei tag `<a>` posso aggiungere il link alla privacy policy.

## Button trasparente carino
![[Pasted image 20230601112553.png]]
