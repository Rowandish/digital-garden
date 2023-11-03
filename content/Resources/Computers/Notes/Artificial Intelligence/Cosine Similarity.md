---
tags:
  - LargeLanguageModels
---
## Introduzione
La cosine similarity è una misura del grado di similarità tra due vettori in uno spazio multidimensionale.
Viene comunemente utilizzata nell'intelligenza artificiale e nell'elaborazione del linguaggio naturale per confrontare [[Embeddings]], che sono rappresentazioni numeriche di parole o altri oggetti in modo indipendente dalla loro lunghezza e dimensione.
La similarità cosinusoidale tra due vettori viene calcolata prendendo il prodotto scalare dei due vettori e dividendo il risultato per il prodotto delle loro magnitudini. Ciò produce un valore compreso tra -1 e 1, dove 1 indica che i due vettori sono identici, 0 indica che sono ortogonali (cioè non hanno correlazione) e -1 indica che sono opposti.
La similarità cosinusoidale è particolarmente utile quando si lavora con dati ad alta dimensionalità, come gli [[embeddings|embedding]] di parole, perché tiene conto sia della magnitudine che della direzione di ogni vettore. Ciò la rende più robusta rispetto ad altre misure come la distanza euclidea, che considera solo la magnitudine.

## Calcolo della similarità
Per calcolare la similarità del coseno tra due vettori, è necessario eseguire i seguenti passaggi:
1. Normalizzare i vettori: è importante normalizzare i vettori per rimuovere le differenze di lunghezza. Questo può essere fatto dividendo ciascun vettore per la sua norma euclidea.
2. Calcolare il prodotto scalare: moltiplicare i vettori componente per componente e sommare i risultati.
3. Calcolare le norme dei vettori: calcolare la norma euclidea dei due vettori.
4. Applicare la formula della similarità del coseno: dividere il prodotto scalare ottenuto per il prodotto delle norme dei vettori.

La formula per calcolare la similarità del coseno tra due vettori 𝑎 e 𝑏 è la seguente:
```
similarita' = 𝑎 • 𝑏 / (‖𝑎‖ × ‖𝑏‖)
```

## Casi d'uso

* **Parole simili**. Ad esempio, dato un embedding per "gatto", possiamo utilizzare la cosine similarity per trovare altre parole con embeddings simili, come "gattino" o "felino". Ciò può essere utile per compiti come la classificazione del testo o l'analisi del sentiment, dove vogliamo raggruppare parole semanticamente correlate.
* **Sistemi di raccomandazione**: Rappresentando gli elementi (ad esempio, film, prodotti) come vettori, possiamo utilizzare la similarità cosinusoidale per trovare elementi simili tra loro o a un particolare elemento di interesse. Ciò ci consente di fornire raccomandazioni personalizzate basate sul comportamento o sulle preferenze passate dell'utente.
* **Riconoscimento di immagini**: la similarità cosinusoidale può essere utilizzata per confrontare gli incorporamenti di due immagini, il che può aiutare nei compiti di riconoscimento delle immagini.  
- **Elaborazione del linguaggio naturale**: la similarità cosinusoidale può essere utilizzata per misurare la similarità semantica tra due frasi o paragrafi confrontando i loro vettori di incorporamento.    
- **Clustering**: la similarità cosinusoidale può essere utilizzata come metrica di distanza per algoritmi di clustering, aiutando a raggruppare insieme punti dati simili.    
- **Rilevamento di anomalie**: la similarità cosinusoidale può essere utilizzata per identificare anomalie in un [[dataset]] trovando punti dati che hanno una bassa similarità cosinusoidale con gli altri punti dati nel dataset.

Nel complesso, la similarità cosinusoidale è uno strumento essenziale per gli sviluppatori che lavorano con intelligenza artificiale e embeddings. La sua capacità di catturare sia la magnitudine che la direzione la rende adatta per dati ad alta dimensionalità, e le sue applicazioni nell'elaborazione del linguaggio naturale e nei sistemi di raccomandazione la rendono uno strumento prezioso per la creazione di applicazioni intelligenti.
