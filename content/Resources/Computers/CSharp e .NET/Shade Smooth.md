"Shade Smooth" è una funzione di Blender che cambia il modo in cui vengono visualizzati i poligoni di un oggetto nella scena senza aumentarne di numero.
Quando si applica lo "Shade Smooth" a un oggetto, Blender interpola le normali dei poligoni adiacenti per creare un aspetto più continuo e uniforme.
Questo significa che gli angoli tra i poligoni adiacenti verranno resi più morbidi senza aggiungere effettivamente dettagli aggiuntivi o aumentare la complessità della mesh.

Questa funzione è utile per oggetti che hanno superfici curve o organiche, ma che potrebbero avere una rappresentazione visiva "angolare" a causa della presenza di facce piatte o angoli marcati. ==Lo "Shade Smooth" migliora l'aspetto visivo senza aumentare il numero di poligoni o dettagli effettivi sulla mesh.==

Nell'immagine di sinistra ho un oggetto senza `Shade Smooth` mentre nell'oggetto di destra dopo l'operazione.

![[Pasted image 20231121121739.png]]![[Pasted image 20231121121824.png]]

Per aggiungere lo `Shade Smooth` ad un oggetto basta fare `tasto dx -> Shade Smooth`

![[Pasted image 20231121121934.png]]

### Differenze con il Subdivision Surface Modifier:

- **Shade Smooth:** Cambia l'aspetto visivo senza aggiungere effettivamente più poligoni, interpolando le normali dei poligoni adiacenti per ottenere un aspetto più liscio e continuo.    
- **[[Subdivision Surface Modifier]]:** Aumenta il numero di poligoni sulla mesh effettiva, suddividendo iterativamente la geometria e aggiungendo dettagli effettivi alla superficie del modello.