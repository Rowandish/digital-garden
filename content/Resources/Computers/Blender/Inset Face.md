---
tags:
  - Blender
---
Quando stai selezionando una faccia di un oggetto e premi il tasto `I`, questo attiva la funzione "Inset Faces".
Questa funzione permette di ==creare una nuova faccia all'interno di un poligono selezionato, creando un'area interna al poligono originale== (una sorta di [[Edge loop]]. Questa operazione comporta l'aggiunta di una nuova faccia all'interno della faccia selezionata, creando un inset space.

Per utilizzare questa funzione:

1. **Seleziona una faccia:**
   - Entra nella modalità di modifica dell'oggetto (Edit Mode) premendo il tasto "Tab" sulla tastiera.
   - Seleziona la faccia su cui desideri eseguire l'inset.
2. **Premi "I":**
   - Dopo aver selezionato la faccia desiderata, premi il tasto "I" sulla tastiera. Questo attiverà l'operazione di inset.
3. **Regola l'inset:**
   - Dopo aver premuto "I", puoi muovere il mouse per regolare l'ampiezza dell'inset.
   - Puoi anche premere "I" di nuovo o utilizzare la barra spaziatrice per accedere al menu e regolare i parametri dell'inset tramite il menu contestuale.
4. **Conferma o annulla l'inset:**
   - Una volta ottenuto l'inset desiderato, puoi confermarlo cliccando con il mouse o premendo "Enter".
   - Per annullare l'inset e tornare alla situazione precedente, premi "Esc".

Questa funzione è utile per creare dettagli o geometrie interne all'interno di un poligono, come cornici, rilievi o altre forme, che possono essere utili durante il processo di modellazione per aggiungere dettagli a un modello senza dover aggiungere manualmente nuove facce o geometrie.

### Esempio

Questo vaso appoggia sulla mensola con vertice a punta, voglio invece che la superficie sia più piana.
![[Pasted image 20231121123417.png|350]]
* Seleziono la faccia di appoggio della superficie originale (`Tab` e `Alt+Z` per toggle X-Ray
![[Pasted image 20231121123320.png]]
* Premere `I`
* Creare una faccia ulteriore all'interno della faccia preesistente
![[Pasted image 20231121124037.png]]
* Questo rende il punto di appoggio dell'oggetto nel piano non più un vertice ma un piano.
![[Pasted image 20231121124156.png]]