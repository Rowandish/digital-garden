---
tags:
  - Blender
---
L'opzione "Edge Loop" o "Loop cuts" in Blender è una funzione che consente di selezionare o creare un insieme di spigoli (edges) che formano un loop continuo lungo una mesh.
Questa funzione è utile per ==selezionare, modificare o creare geometrie più facilmente lungo una determinata sezione di un modello==.
Permettono di definire delle sottofacce alla mia mesh in modo che siano modificabili indipendentemente dalla mesh originale.
Per esempio prendiamo la mesh di un muro e vogliamo farne un buco rettangolare in una determinata posizione: per farlo dobbiamo quindi definire dei bordi all'interno della mia mesh in modo che siano modificabili indipendentemente dalla mesh originale.
Questa definizione di sottomesh a partire da una mesh originale si ha tramite gli `Edge Loop`.
Procedimento.
* `Tab`: entro in edit mode
* `Ctrl + R`: entro in modalità `Edge Loop` e definisco dove voglio inserire la mia sotto-mesh
* Una volta cliccato il punto con il mouse posso aggiustare bene dove la voglio
![[Pasted image 20231121112702.png|300]]
* Ora abbiamo aggiunto più definizione alla nostra mesh, questa ha più edge, facce e vertici da modificare indipendentemente gli uni dagli altri. Per esempio qui ho selezionato solo la faccia sopra il mio nuovo Edge, cosa impossibile prima.
![[Pasted image 20231121112827.png|300]]

## Esempio - Creare una finestra
Usiamo gli `Edge Loop` per creare una finestra nel muro dell'esempio sopra.
Aggiungiamo un altro Edge premendo ancora `Ctrl+R` e andando a definire la parete sinistra, destra e superiore del foro che che voglio fare.
![[Pasted image 20231121113124.png|300]]
Posso selezionare e spostare i bordi con i soliti tasti `G` vincolando gli assi che mi servono.
* Una volta descritto il rettangolo che voglio eliminare posso selezionarlo usando la modalità di selezione faccia
![[Pasted image 20231121113336.png|300]]
* Eliminarla premendo `X`
![[Pasted image 20231121113423.png|300]]


Ecco come puoi utilizzare l'Edge Loop in Blender:

### Selezione di un Edge Loop:

1. **Modalità di selezione:**
   - Entra in modalità di selezione spigoli (Edge Mode) premendo il tasto "2" sulla tastiera numerica o selezionando l'icona dell'Edge Mode nell'area di lavoro di Blender.

2. **Selezionare un Edge Loop:**
   - Posiziona il cursore del mouse sopra uno spigolo dell'edge loop che desideri selezionare.
   - Premi "Alt" e clicca con il pulsante sinistro del mouse: questo selezionerà automaticamente l'intero edge loop basato sul flusso dell'edge loop dalla posizione del cursore.

3. **Modifiche all'Edge Loop selezionato:**
   - Una volta selezionato, puoi eseguire molte azioni su questo loop, come spostarlo, estrarre una parte di esso, modificare le proprietà o applicare modifier specifici su di esso.

### Creazione di un Edge Loop:

1. **Utilizzo del Loop Cut and Slide:**
   - Entra nella modalità di modifica della mesh (Edit Mode) premendo il tasto "Tab" sulla tastiera.
   - Seleziona l'opzione "Loop Cut and Slide" dal menu degli strumenti laterali o premi "Ctrl + R".
   - Piazza il cursore sullo spigolo in cui desideri creare l'edge loop e clicca.
   - Muovi il mouse per spostare la posizione dell'edge loop e clicca di nuovo per confermare la posizione. Puoi anche digitare il numero di tagli desiderati prima di confermare la posizione.

### Utilizzi principali:

- **Modellazione dettagliata:** Per creare dettagli specifici su una mesh.
- **Deformazione e animazione:** Per controllare la deformazione su una determinata sezione della mesh.
- **Applicazione di modifiche localizzate:** Per applicare modifier, come il "Bevel" o il "Subdivision Surface", solo su parti specifiche della mesh.

L'uso di Edge Loops in Blender è fondamentale per la modellazione dettagliata e per il controllo preciso della geometria in determinate parti di un modello 3D.

