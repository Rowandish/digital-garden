---
tags:
  - CSharp
  - SemanticKernel
  - MachineLearning
---
Le Memory sono un modo potente per fornire un contesto più ampio per la tua domanda nel [[Semantic Kernel]].
Storicamente, abbiamo sempre invocato la memoria come componente fondamentale per il funzionamento dei computer: pensa alla RAM del tuo laptop. Perché con solo una CPU in grado di scricchiolare i numeri, il computer non è così utile a meno che non sappia quali numeri ti interessano.
La memoria fornisce ciò che rende il calcolo rilevante per il compito da svolgere.

Possiamo fornire memoria al SK in tre modi:
* **Coppie chiave-valore convenzionali**: proprio come si imposta una variabile d'ambiente nella shell, lo stesso può essere fatto quando si utilizza il kernel semantico. La ricerca è "convenzionale" perché è una corrispondenza uno a uno tra una chiave e la tua query.
* **Archiviazione locale convenzionale**: quando si salvano informazioni in un file, queste possono essere recuperate con il relativo nome file. Quando hai molte informazioni da archiviare in una coppia chiave-valore, è meglio tenerle su disco.
* **Ricerca di memoria semantica**: puoi anche rappresentare le informazioni di testo come un lungo vettore di numeri, noto come "[[Embeddings]]". Ciò ti consente di eseguire una ==ricerca "semantica" che confronta significato con significato con la tua query==.

## Come funziona la memoria semantica

==Gli [[Embeddings]] sono un modo per rappresentare parole o altri dati come vettori in uno spazio ad alta dimensione==.
I vettori sono come frecce che hanno una direzione e una lunghezza. Alta dimensionale significa che lo spazio ha molte dimensioni, più di quanto possiamo vedere o immaginare.
==L'idea è che parole o dati simili avranno vettori simili e parole o dati diversi avranno vettori diversi (vedi [[Cosine Similarity]]). Questo ci aiuta a misurare quanto siano correlati o non correlati e anche a eseguire operazioni su di essi==, come addizione, sottrazione, moltiplicazione, ecc.
Gli [[Embeddings]] sono utili per i [[GPT Model|modelli]] di intelligenza artificiale perché ==possono catturare il significato e il contesto di parole o dati in un modo che i computer possono comprendere ed elaborare==.

Quindi in pratica prendi una frase, un paragrafo o un'intera pagina di testo e quindi generi il vettore di [[Embeddings]] corrispondente.
E quando viene eseguita una query, ==la query viene trasformata nella sua rappresentazione di embedding, quindi viene eseguita una ricerca attraverso tutti i vettori di incorporamento esistenti per trovare quelli più simili==.
Questo è simile a quando effettui una query di ricerca su Bing e ti fornisce più risultati che sono prossimi alla tua query. È improbabile che la memoria semantica ti fornisca una corrispondenza esatta, ma ti fornirà sempre una serie di corrispondenze classificate in base alla somiglianza della tua query con altre parti di testo.

## Perché gli embedding sono così importanti?

Poiché un prompt è un testo che diamo come input a un modello AI per generare un output o una risposta desiderati, dobbiamo considerare la lunghezza del testo di input in base al limite di [[Token (LLM)]] del modello che scegliamo di utilizzare. Ad esempio, GPT-4 può gestire fino a 8.192 token per input, mentre GPT-3 può gestire solo fino a 4.096 token. Ciò significa che i testi più lunghi del limite del token del modello non si adatteranno e potrebbero essere tagliati o ignorati.

Sarebbe bello se potessimo utilizzare un intero manuale operativo di 10.000 pagine come contesto per il nostro prompt, ma a causa del vincolo del limite di token, ciò è impossibile.
Pertanto, ==gli embeddings sono utili per suddividere quel testo di grandi dimensioni in parti più piccole==.
Possiamo farlo riassumendo ogni pagina in un paragrafo più breve e quindi generando un vettore di incorporamento per ogni riepilogo. ==Un embedding vector è una rappresentazione compressa del testo che ne preserva il significato e il contesto==.
Quindi possiamo confrontare gli embedding vectors dei nostri riepiloghi con il embedding vector del nostro prompt e selezionare quelli più simili.
Possiamo quindi aggiungere quei riepiloghi al nostro testo di input come contesto per il nostro prompt. In questo modo, possiamo ==utilizzare gli embeddings per aiutarci a scegliere e adattare testi di grandi dimensioni come contesto entro il limite di token del modello==.