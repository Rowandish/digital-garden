---
tags:
  - Blender
---
Il Subdivision Surface Modifier in Blender ==suddivide la geometria esistente, aumentando il numero di poligoni e rendendo la superficie più liscia e dettagliata==.

## Esempio

* Assumiamo di avere questo vaso che vogliamo rendere più dettagliato.
![[Pasted image 20231121115600.png]]
* Aggiungiamo il `Subdivision Surface`
![[Pasted image 20231121120341.png]]
* Quello che ottengo è un aumento del numero di poligoni che il software crea interpolando i vertici esistenti
![[Pasted image 20231121120519.png]]
* Ho due opzioni che sono
	* `Levels Viewport`: il numero di vertici che voglio manovrare in modalità normale. in questo modo posso velocizzare il software dovendo gestire meno vertici mentre lavoro
	* `Render`: numero di vertici in render mode.
In questo modo posso regolare la visualizzazione della suddivisione senza alterare la geometria di base durante la fase di modifica (Viewport) e poi aumentare il numero di suddivisioni per il rendering per ottenere un modello più dettagliato al momento del rendering finale.
In questo esempio ho impostato a 2 e a 6 i livelli in ViewPort (i livelli render li vedo solo in render mode).
![[Pasted image 20231121120756.png]]![[Pasted image 20231121120846.png|307]]

- Alcuni bordi potrebbero diventare troppo arrotondati a causa della suddivisione. Per controllare questo effetto, puoi aggiungere [[Edge loop]] vicino ai bordi che desideri mantenere più nitidi.

Premendo `Tab` posso visualizzare la maschera dell'oggetto originale senza i modifier applicati, come si vedere qui.

![[Pasted image 20231121122302.png]]

### Vantaggi
- **Rendere la superficie più liscia:** Applicare questo modifier permette di creare superfici più lisce e uniformi, ideali per oggetti come personaggi, oggetti organici o superfici curve.  
- **Aggiungere dettagli:** Il modifier può essere utilizzato per aumentare il livello di dettaglio di un modello senza dover aggiungere manualmente molti poligoni.
- **Modellazione non distruttiva:** Questo modifier permette di mantenere la geometria originale del modello mentre ne visualizzi una versione più dettagliata, il che significa che puoi modificarne la struttura di base senza perdere i dettagli aggiunti.

### Differenze con il Shade Smooth:

- **[[Shade Smooth]]:** Cambia l'aspetto visivo senza aggiungere effettivamente più poligoni, interpolando le normali dei poligoni adiacenti per ottenere un aspetto più liscio e continuo.    
- **Subdivision Surface Modifier:** Aumenta il numero di poligoni sulla mesh effettiva, suddividendo iterativamente la geometria e aggiungendo dettagli effettivi alla superficie del modello.