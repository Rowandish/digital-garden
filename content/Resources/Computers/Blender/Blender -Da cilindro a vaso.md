Assumiamo di avere un cilindro e volerlo modificare in modo che il centro vada verso l'esterno.
* `Tab`
* `Ctrl+R`: creo il nuovo vertice
![[Pasted image 20231121114957.png]]
* `S` (senza vincoli di asse) lo scalo come voglio
![[Pasted image 20231121115310.png]]
* Rimuovo la faccia superiore con `Tab` -> `3` -> Seleziono la faccia superiore -> `x` -> `faces`
![[Pasted image 20231121115437.png]]
* Aggiungere un [[Solidify Modifier]] per modificarne lo spessore e ottenere così un vaso
![[Pasted image 20231121115600.png]]
* Aggiungiamo un [[Subdivision Surface Modifier]] per aumentarne il numero di poligoni e il dettaglio
![[Pasted image 20231121120519.png]]
* Rendiamolo più smooth usando il [[Shade Smooth]] senza aumentarne il numero di poligoni
![[Pasted image 20231121121824.png]]
* Facciamo in modo che non appoggi su un vertice ma su un piano creando una faccia innestata all'interno della faccia inferiore usando [[Inset Face]]
![[Pasted image 20231121124156.png]]