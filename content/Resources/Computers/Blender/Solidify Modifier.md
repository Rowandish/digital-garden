---
tags:
  - Blender
---
Il modifier "Solidify" in Blender permette di aggiungere spessore a una superficie.
Il Solidify Modifier agisce ==creando spessore alla superficie di un oggetto senza alterarne la forma generale==. Può essere regolato per aggiungere spessore verso l'interno o verso l'esterno dell'oggetto, e permette di controllare l'ampiezza dello spessore, l'angolo di piegatura, e altri parametri che possono influenzare l'aspetto del modello.

Questo modifier è particolarmente utile quando ==si lavora con oggetti come pareti, piani o superfici piatte che devono avere un certo spessore per essere visualizzati correttamente in una scena 3D==.
Ad esempio, se si sta creando un muro, anziché creare due superfici separate per rappresentare i lati del muro, si può creare una sola superficie e applicare il Solidify Modifier per aggiungere lo spessore necessario.
Se ho un muro con una sola superfice posso usare un piano da estrudere come al solito, ma se ne ho due (per esempio un muro angolare) e voglio che lo spesso dei due muri sia uguale e vincolato l'uno all'altro il solidify modifier viene in aiuto.
Analogamente se voglio creare due oggetti che hanno lo stesso spessore vincolati gli uni agli altri posso associarne a uno il *solidify modifier* e poi duplicare quest'ultimo con `Shift+D`. Il secondo oggetto avrà la stessa istanza del modifier e conseguentemente alla modifica dello spessore di uno seguirà la modifica dell'altro.

## Esempio
### Creare un muro senza Solidify Modifier:

1. **Senza Solidify Modifier: Metodo manuale**
   - Inizia creando un piano: premi Shift + A → Mesh → Plane.
   - Posiziona il piano dove desideri il muro.
   - Estrudi il piano verso l'alto premendo il tasto "E" sulla tastiera, quindi trascina verso l'alto per creare lo spessore del muro.

2. **Ripetizione dei passaggi:**
   - Se devi creare più muri, dovrai ripetere lo stesso processo per ciascuno di essi e lo spessore dovrai farlo uguale l'uno all'altro a mano.

### Creare un muro con Solidify Modifier:

1. **Con Solidify Modifier:**
   - Inizia creando un piano come fatto precedentemente.
   - Crea il secondo muro relativo al primo entrando in `Edit Mode` -> `2` per selezionare il bordo che voglio estrudere ![[Pasted image 20231121110739.png|150]]
   - `E + y`: estrudo solo il bordo nell'asse `y`
   - ![[Pasted image 20231121110822.png]]
   - Aggiungi il Solidify Modifier all'oggetto: vai alla sezione Properties (proprietà) nell'editor di proprietà e clicca su "Add Modifier" → "Solidify".
![[Pasted image 20231121110946.png|400]]
   - Imposta lo spessore desiderato all'interno delle opzioni del modifier. Puoi regolare l'ampiezza dello spessore e altre opzioni come l'angolo di piegatura.
   - Il muro ora avrà lo spessore definito, senza la necessità di estrudere manualmente e senza dover creare singolarmente ogni singolo muro. Inoltre, è possibile modificare lo spessore in qualsiasi momento regolando semplicemente i parametri del Solidify Modifier.
   ![[Pasted image 20231121111125.png]]

