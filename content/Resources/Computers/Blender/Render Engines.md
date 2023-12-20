---
tags:
  - Blender
---
In Blender, ci sono diversi "render engine" o motori di rendering, ognuno con le proprie caratteristiche, pregi e limitazioni.
### Cycles Render Engine:

- **Ray Tracing avanzato:** Cycles è un motore di rendering basato su ray tracing, che simula realisticamente l'illuminazione, i riflessi, le ombre e gli effetti di rifrazione. È ideale per la produzione di rendering fotorealistici.  
- **Materiali avanzati:** Supporta materiali complessi e realistici utilizzando il node-based shader editor di Blender, permettendo di creare superfici complesse con texture e effetti avanzati.  
- **Illuminazione globale:** Cycles supporta l'illuminazione globale, inclusi ambient occlusion e environment lighting, permettendo di ottenere scene luminose e realistiche.

### Eevee Render Engine:

- **Rendering in tempo reale:** Eevee è un motore di rendering in tempo reale progettato per offrire un'anteprima veloce e interattiva. È ottimo per la visualizzazione e la creazione di animazioni in tempo reale.  
- **Effetti grafici avanzati:** Supporta effetti come luci volumetriche, bloom, motion blur e altri effetti visivi che sono utili soprattutto per la visualizzazione in tempo reale.  
- **Rendering rapido:** Rispetto a Cycles, Eevee offre tempi di rendering molto più veloci ma con un livello di realismo leggermente inferiore.

### Utilizzi principali:

- **Cycles:** È preferito per la produzione di immagini statiche fotorealistiche, scene architettoniche, design di prodotti e rendering di alta qualità.  
- **Eevee:** È ideale per l'anteprima in tempo reale, la visualizzazione interattiva, animazioni, giochi, e progetti che richiedono una resa rapida e un'anteprima fluida.

## Come impostarli
Per impostare un render Engine andare su `Render properties` e impostare il render che vogliamo.
Per `Cycles` consigliatissimo impostare `GPU Compute` come device e verificare che nelle opzioni siano state correttamente rilevate le schede grafiche.
![[Pasted image 20231121144900.png]]

![[Pasted image 20231121145009.png]]

## Velocizzazione
Cycles è molto lento, per velocizzarlo posso limitare il render solo ad una parte dell'immagine qualora sia in `Camera view` (numpad `0`).
Per farlo una volta entrati in `Camera view` premere `Ctrl+B` e selezionare l'area che vogliamo renderizzare.
Ora ogni volta che entreremo in tale modalità di visualizzazione verrà effettuato il render solo di quell'area.