---
tags:
  - DeepLearning
---
Una rete neurale è un modello ispirato al funzionamento del cervello umano, usato per imparare da dati e fare previsioni o decisioni.

![[Pasted image 20240111171808.png]]

## Addestramento

1. **Input**: La rete riceve input, che possono essere dati come numeri, immagini, testo o altro. Questo input viene chiamato [[Train, validation e test set|train set]].
2. **Strati di Neuroni**: La rete è composta da strati di "neuroni" artificiali. Ogni neurone in uno strato riceve input da vari neuroni dello strato precedente.
3. **Pesi e Bias**: Ogni connessione tra neuroni ha un "peso" e ogni neurone ha un "bias". All'inizio sono inizializzati casualmente (o secondo una algoritmo specifico) e poi pesi e bias sono modificati durante l'apprendimento della rete. Sono come regolatori che decidono quanto l'input da un neurone precedente è importante.
4. **[[Funzione di attivazione|Funzioni di attivazione]]**: Ogni neurone applica una funzione di attivazione al suo input. Questa funzione decide se e quanto il neurone "si attiva", cioè quanto fortemente trasmette il segnale ai neuroni successivi.
5. **Elaborazione**: Il segnale passa attraverso la rete, da strato a strato, trasformandosi in base ai pesi, ai bias e alle funzioni di attivazione. Una [[Epoche|epoca]] è un termine che indica un completo ciclo di passaggio di tutti i dati di allenamento attraverso il modello. Se stai addestrando la tua rete neurale a riconoscere le foto di gatti, un'epoca significa che la rete ha visto tutte le diverse foto di gatti che hai. 
6. **Output**: L'ultimo strato della rete produce l'output, che può essere una classificazione (come identificare se un'immagine mostra un gatto o un cane), una previsione (come prevedere il prezzo di una casa), o altro tipo di risultato.
7. **Aggiornamento dei pesi**: Durante questa fase, la rete neurale confronta il suo output con la risposta corretta e regola i pesi e i bias (un processo chiamato "[[Backpropagation]]") per migliorare le sue previsioni o decisioni in futuro. Il numero di dati processati prima di procedere alla backpropagation è detto [[Batch size]]. Gli algoritmi che utilizza per aggiustare tali pesi sono chiamati [[Algoritmi di ottimizzazione]]. La funzione che indica quanto una rete neurale sta lavorando è detta [[Loss function]] o funzione di costo e l'obiettivo è ridurre questo valore durante le varie iterazioni.
8. **Iterazione**: Questo processo di regolazione avviene molte volte ([[Epoche]]) per rendere la rete più precisa e affidabile.

Dopo l'allenamento, il modello è pronto per l'[[Inferenza]], dove viene applicato a nuovi dati (il [[Train, validation e test set|test set]]) per fare previsioni o prendere decisioni basate su ciò che ha appreso.

In questa figura si vedono gli input del modello, l'applicazione dell'algoritmo di ottimizzazione che crea un nuovo modello, nel senso che aggiorna i pesi e i bias del modello iniziale, e la funzione di costo che rappresenta la misura dell'errore del modello rispetto ai dati di addestramento. 
Con il passare delle epoche la funzione di costo deve tendere al minimo.
![[Pasted image 20240202145836.png]]
![[Pasted image 20240202150205.png]]



## Visualizzazione
In questo esempio si vedono i nodi della rete con i livelli di input, nascosti e di output e di come ogni nodo fornisca un risultato in base ad una sua funzione lineare con pendenza i pesi e quota il bias e una funzione di attivazione che fornisce l'output effettivo del nodo che poi viene passato ai nodi successivi.

![[Pasted image 20240402100144.png]]
![[Pasted image 20240402100255.png]]
