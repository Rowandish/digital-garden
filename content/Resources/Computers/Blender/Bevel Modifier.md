---
tags:
  - Blender
---
Il "Bevel Modifier" è uno strumento che consente di ==smussare o arrotondare gli spigoli (edges) di un oggetto, aggiungendo un certo grado di curvatura o smussatura agli angoli della mesh==.
Questo modifier è utile per creare modelli più realistici, arrotondati e per migliorare l'aspetto visivo di oggetti che altrimenti avrebbero angoli netti.
Esempio prima e dopo l'applicazione.

![[Pasted image 20231121125738.png]]![[Pasted image 20231121125721.png]]
Qui con due segments + [[Shade Smooth]].
![[Pasted image 20231121125917.png]]
### Utilizzo del Bevel Modifier

![[Pasted image 20231121125308.png]]

1. **Aggiunta del modifier:**
   - Seleziona l'oggetto a cui desideri applicare il Bevel Modifier.
   - Nell'editor delle proprietà, clicca su "Add Modifier" (Aggiungi Modificatore) e scegli "Bevel".
2. **Parametri del modifier:**
   - Il Bevel Modifier ha diverse opzioni e parametri regolabili:
     - **Width:** Controlla l'ampiezza della smussatura. Questo determina quanto spazio viene aggiunto tra gli spigoli originali e i nuovi spigoli smussati.
     - **Segments:** Imposta il numero di segmenti che compongono la smussatura. Più segmenti significano una curvatura più fluida e dettagliata.
     - **Profile:** Modifica la forma della curva di smussatura. Puoi ottenere risultati diversi regolando questo parametro.
3. **Controllare gli spigoli smussati:**
   - Una volta applicato il Bevel Modifier, puoi vedere gli spigoli dell'oggetto diventare smussati o arrotondati.
   - Puoi regolare gli angoli smussati regolando i parametri del modifier per ottenere l'effetto desiderato.
4. **Modifiche non distruttive:**
   - Il Bevel Modifier permette di applicare l'effetto di smussatura senza modificare effettivamente la geometria di base dell'oggetto. Questo significa che puoi regolare o rimuovere il modifier in qualsiasi momento senza perdere la geometria originale.

> [!note] Attenzione alla scala
> Il bevel modifier funziona bene se la scala dell'oggetto è 1;1;1 (la scala di un oggetto va sempre modificata in Edit Mode e non in Object Mode).

Per resettare la scala di un oggetto `Ctrl+A -> Apply Scale`

### Applicazioni

- **Modellazione realistica:** È utile per modellare oggetti che devono avere spigoli smussati o arrotondati, come mobili, oggetti di design, dettagli architettonici e molto altro ancora.  
- **Rendering e illuminazione:** Gli spigoli smussati possono interagire con la luce in modo più realistico durante il rendering, migliorando l'aspetto visivo delle superfici.
