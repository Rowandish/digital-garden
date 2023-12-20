---
tags:
  - Blender
---
Blender è un programma per la modellazione di oggetti 3D.
In particolare permette di definire l'[[Lighting|illuminazione]] della scena, i [[Materials|materiali]] degli oggetti, lo [[world|sfondo]] e permette di esportare un'immagine o un [[Esportare un video|video]] della scena in questione.
Il processo di renderizzazione viene personalizzato tramite le [[render properties]] e avviene con un motore chiamato [[render engines]].
La creazione degli oggetti avviene tramite il processo di modellizzazione che può avvenire a mano libera oppure tramite una [[Modellizzare con immagine di reference|immagine di reference]].
## Modifier

I modifier sono strumenti che consentono di apportare modifiche non distruttive agli oggetti o alle mesh, influenzando la forma, la disposizione o altre caratteristiche senza modificare direttamente i dati sottostanti.

* [[Solidify Modifier]]
* [[Subdivision Surface Modifier]]
* [[Bevel Modifier]]

## Interfaccia

Premendo in alto a sinistra nelle varie sezioni posso visualizzare la finestra che voglio, per esempio al posto degli Outliner potrei avere una seconda vista del modello 3D e così via.
![[Pasted image 20231113161905.png]]

Posso inoltre aggiungere una seconda visualizzazione della stessa scena premendo con il mouse nell'angolo in alto a dx della vista e trascinando verso sinistra.
![[Pasted image 20231121141321.png]]
![[Pasted image 20231121141337.png]]
Per esempio posso premere `0` sulla finestra di destra e visualizzare quello che vede la telecamera mentre sullo schermo di sinistra lavorare.
![[Pasted image 20231121141507.png]]
Un classico è avere a destra la `Render View` di Camera con [[Render Engines]] cycles e `Ctrl+B` per limitare il render ad un'area e a sinistra la `Object View` per modificare e visualizzare la scena.
![[Pasted image 20231121152504.png]]
### Outliner
![[Pasted image 20231113161658.png]]
In alto a destra c'è una interfaccia chiamata "Outliner" dove sono indicati tutti gli oggetti che sono presenti nel progetto con una icona indicante la loro tipologia.

## Opzioni 

![[Pasted image 20231113171630.png]]

### Orbit around Selection
Con questa opzioni quando mi muovo con il mouse mi muovo relativamente all'oggetto selezionato e non relativamente al centro.
Molto comodo.

### Zoom to mouse position
Invece di zoomare sempre verso il centro con questa opzioni zoomo dove ho il mouse. Molto comodo.




## Modalità di visualizzazione viste
Premendo i questi pulsanti posso modificare la modalità di visualizzazione delle viste.
![[Pasted image 20231121142141.png]]
In particolare ho
* `Wireframe mode`
* `Solid mode`: default
* `Viewport shading mode`
* `Render view`: visualizzazione degli oggetti renderizzati, quindi con la presenza delle luci
## Modalità di gestione oggetti

In Blender esistono due modalità di gestione/visualizzazione:
* **Object mode (default)**. Questa è la modalità di default, permette di selezionare e modificare oggetti nella loro totalità (es. una curva totale).
* **Edit mode**: permette di modificare i singoli pezzi di un oggetto, per esempio di una curva posso selezionare i punti e modificarli.
### Edit mode
Dato un oggetto lo posso modificare entrando in `Edit mode` premendo il tasto `Tab`.
In questa modalità posso selezionare ogni singolo vertice di un oggetto (ricordo che un oggetto tridimensionale non è altro che un insieme di vertici), ma anche facce o bordi.
Per impostare la modalità di selezione posso cliccare su queste piccole icone in alto a sinistra
![[Pasted image 20231121104550.png]]
oppure premendo i numeri `1` (Vertex), `2` (Edge) o `3` (Face) (numeri normali, non tastierino) quando sono in edit mode.
Una volta selezionato l'oggetto che voglio modificare premo il tasto `G` come al solito aggiungendo tipicamente l'asse di modifica.
Per esempio assumiamo che voglio rendere più bassa questa mensola.
![[Pasted image 20231121105119.png|300]]
* `Tab`: entro in edit mode
* `3`: entro in modalità selezione faccia per selezionare la faccia superiore
![[Pasted image 20231121105218.png|300]]
* `G + z`: modifico l'oggetto con `G` vincolandolo solo all'asse `z`.
![[Pasted image 20231121105323.png|300]]
* Con il mouse lo alzo e lo abbasso a piacimento

## Modifiche mesh

* [[Edge loop]]
* [[Inset Face]]


## Esempi

* [[Blender -Da cilindro a vaso]]
* [[Testo 3D in Blender]]
## Shortcut

### Varie
* `T`: Mostra o nasconde la sidebar sinistra
* `N`: Mostra o nasconde la finestra di gestione della posizione, rotazione e scala di un oggetto
* `H`: Nasconde l'oggetto selezionato
* `Alt + H`: Mostra l'oggetto nascosto
* `Shift + Click`: Seleziona multipli oggetti
* `X`: Elimina l'oggetto selezionato
* `A`: Seleziona tutto
* `Shift + A`: Apri interfaccia aggiunta oggetto
* `Ctrl + A`: Apri interfaccia applica trasformazione
* `Shift + D`: Duplica oggetto
* `Taso destro durante operazione`: Annulla operazione
* `Tab`: toggle edit mode
* `Ctrl+R`: crea un Edge Loop
* `Ctrl+I`: selezione inversa
* `I` (su selezione faccia): [[Inset Face]]
* `Ctrl+B`: Crea un render boundary, quindi impongo di renderizzare solo all'interno del rettangolo definito al fine di veloccizzare il processo.
* `E`: Extrude (in edit mode)

### Visualizzazioni
* `hold and drag mouse middle mouse`:  Muoviti intorno all'oggetto con la vista
* `Shift + mouse middle`: Pan della vista 
* `Mouse Wheel`: Zoom in e out
* `1 (tastierino)`: mettiti in front view 
* `3 (tastierino)`: mettiti in side view 
* `7 (tastierino)`: mettiti in top view 
* `0 (tastierino)`: Mostro quello che sta vedendo la telecamera (toggle camera view) 
* `Alt+Z`: toggle visualizzazione X-Ray

### Movimento

* `Ctrl durante movimento/rotazione`: Modifca l'oggetto a step discreti (es. 5°). 

#### Lineare

* `G`: Muovi l'oggetto selezionato fino alla prossima pressione di `G`. Se premo `tasto dx` del mouse annullo lo spostamento corrente.
* `G + X`: Muovi l'oggetto solo sull'asse `X`
* `G + Y`: Muovi l'oggetto solo sull'asse `Y`
* `G + Z`: Muovi l'oggetto solo sull'asse `Z`
* `Alt + G`: Resetta l'oggetto alla sua posizione originale
* `R + * + Shift`: Permette di giocare di fino con il movimento

#### Rotatorio

* `R`: Ruota l'oggetto selezionato 
* `R + X`: Ruota l'oggetto solo sull'asse `X`
* `R + Y`: Ruota l'oggetto solo sull'asse `Y`
* `R + Z`: Ruota l'oggetto solo sull'asse `Z`
* `Alt + R`: Resetta l'oggetto alla sua rotazione originale
* `R + * + Shift`: Permette di giocare di fino con la rotazione 

#### Scale
* `S + drag`: Aumenta o diminuisce la dimensione dell'oggetto 
* `S + X`: Scala l'oggetto solo sull'asse `X`
* `S + Y`: Scala l'oggetto solo sull'asse `Y`
* `S + Z`: Scala l'oggetto solo sull'asse `Z`
* `Alt + S`: Resetta l'oggetto alla sua scala originale
* `S + * + Shift`: Permette di giocare di fino con la scala 


## Trick

### Posizionare correttamente la telecamera
Per posizionare la telecamera in modo che inquadri esattamente quello che voglio senza andare a caso sperando di beccare giusto seguire i seguenti passaggi:
* Premere `0` per entrare in modalità visualizzazione tlc
* Usare i comandi `G` e `R` per spostare la tlc dove si vuole. Combinare i comandi insieme a `X`, `Y` o `Z` al fine di spostare la tlc solo lungo l'asse di interesse

### Trasformare un oggetto 3D in un piano
Può capitare di dover ricominciare da 0 nella costruzione di un oggetto 3D (esempio voglio che la sua thickness sia definita tramite [[Solidify Modifier]]) e non tramite il normale Extrude.
* Selezionare il piano che voglio salvare con `Tab` + `3` + selezione
![[Pasted image 20231121114532.png]]
* `Ctrl+I` per selezionare tutto tranne quel piano
![[Pasted image 20231121114610.png]]
* `X` e selezionare `Faces`
![[Pasted image 20231121114643.png]]

### Duplicare un oggetto ma che rimanga lo stesso
Quando duplico un oggetto con `Shift+D` ottengo un oggetto diverso indipendente dall'oggetto originale.
Talvolta però vorrei duplicare un oggetto ma senza che sia un oggetto diverso, ma che abbia gli stesso modifier e altri attributi dell'oggetto originale.
In questo modo, per esempio, se modifico la Thickness di un Solidify modifier di un oggetto viene modificato anche quello dell'altro.
==Posso fare questo semplicemente duplicando l'oggetto in Edit Mode e non in Object Mode==.
* `Tab`
* `A` per selezionare tutto l'oggetto
* `Shift+D` per duplicare l'oggetto ma non creando un nuovo oggetto
* `X|Y|Z` per spostarlo secondo l'asse desiderato.