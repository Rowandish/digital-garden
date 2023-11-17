---
tags:
  - Learning
---
ANKI è un software open-source progettato per aiutare gli utenti a memorizzare informazioni attraverso il metodo di [[spaced repetition]]. Questo metodo si basa sull'idea che ==la memoria di lungo termine può essere migliorata attraverso la ripetizione graduale di informazioni nel tempo==.
ANKI utilizza un algoritmo che determina quando ripetere specifiche informazioni in base alla facilità con cui l'utente le ricorda.
Le carte ANKI (chiamate flashcards) sono gli elementi fondamentali del sistema. Ogni ==flashcard contiene una coppia di domanda-risposta o un concetto e il suo significato==.
⬆️⬇️⬆️
## Basic
Queste carte contengono la domanda su un lato e la risposta sull'altro. Sono utilizzate per memorizzare informazioni specifiche, come fatti, definizioni o concetti.
## Basic (and Reverse card)
Per ogni carta creata ne vengono create 2: una che da un lato mostra l'altro e l'altra come viceversa. In questo modo non creo una connessione one-way ma two-way tra i due concetti

## Cloze Deletion
Una parte della domanda è omessa, e l'utente deve completarla. In questo caso non ho un front e back ma solo il front (oscurato) e il back è di fatto il front senza omissioni. Per oscurare una parte del testo premiamo `Ctrl + Shift + C`. Se aggiungo due oggetti diversi `Cloze` genererò due cards, una con uno oscurato e l'altra con l'altro. Ecco come si presenta una Cloze deletion: `{{c1:risposta::hint}}`. Il testo `hint` permette di aumentare la relazione tra il testo e la risposta in modo che sia esplicito cosa sto chiedendo e lo capisca anche fra 1 anno.

### Extra
Come extra posso aggiungere delle immagini o testo aggiuntivo per comprendere meglio di cosa si sta parlando una volta risposto.
Questo permette di memorizzare molto meglio l'informazione.
![[Pasted image 20231113180127.png]]

## Image Occlusion
Questo è un addon da installare ma è fondamentale in quanto permette, data un'immagine, di doverne indovinare parte del contenuto.
Utile per memorizzare grafici, mappe, definizioni...
Va benissimo per esempio se devo studiare anatomia e ho un'immagine con delle frecce indicanti i nomi delle parti del corpo, posso oscurare queste ultime e farle diventare delle flashcards.

![[Pasted image 20231113180613.png]]
## Settings
Anki ha sia delle opzioni generali ma anche delle opzioni sui deck (accessibili mediante il pulsante ingranaggio affianco al nome del deck).
Per ANKI una card è in stato `New Card` se non è stata ancora imparata dall'utente, secondo l'algoritmo. Una volta che per ANKI è stata imparata passa allo stato di `Learned` e compare molto di meno. Se una card `Learned` viene sbagliata ritorna nello stato di `New card`.

![[Pasted image 20231113181343.png]]
![[Pasted image 20231113181357.png]]


### New cards

#### Learning steps
Il campo `Learning steps` indica ogni quanto mostrare una carta in base a cosa ha risposto l'utente, in particolare se l'utente preme `Again` ricomparirà nella prima cifra, se preme `Good` nell'ultima.
Nello screenshot sopra se premo `Again` comparirà dopo 1 minuto mentre `Good` dopo 15 minuti. Le altre risposte saranno una interpolazione di questi due valori.

#### Graduating interval
Una carta subisce il `graduate` (quindi viene considerata come imparata) dopo che viene impostata come Easy per due volte.

#### Recommended settings
Il primo intervallo temporale è 15 minuti, se la segno come Good 1 giorno e se la segno ancora come Good 6 giorni e infine 15 giorni.
Dopo questo tempo viene graduate.
Se una card viene marcata come easy significa che probabilmente non ha senso nemmeno come card in quanto è un concetto che so benissimo, ergo metto 60 giorni.

![[Pasted image 20231113182644.png]]![[Pasted image 20231113183136.png]]
![[Pasted image 20231113183146.png]]

## Quando usare le flashcards
