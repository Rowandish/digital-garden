---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


## 1.Introduzione
Definire le **proprietà di modifica di un oggetto** è molto importante per una buona programmazione orientata agli oggetti.
In questo capitolo definiamo le propietà che si possono definire agli oggetti per limitarne la loro modifica.
## 2. Variabili const e readonly
Per definire variabili che non cambiano mai di valore, il C# fornisce due possibilità, **const** e **readonly**.
Un campo const viene valutato quando il programma **viene compilato** e quindi una sola volta, per esempio la seguente variabile
```csharp
const long MS_PER_DAY = 1000 * 60 * 60 * 24;
```
viene sostituita dal valore `864000000` quando il programma viene compilato, conseguentemente la moltiplicazione viene eseguita una sola volta.
La parola chiave **readonly** invece è più generica, può essere applicata ad ogni tipologie di variabile e valutata sempre una sola volta **runtime**.
Tipicamente, un campo **readonly** viene valutata o quando ho il _class loading_ (nel caso di attributi statici) oppure quando creo una nuova istanza della classe.
Non devo usare il **readonly** solo per i campi che assumono valore costante _a priori_, posso definire **readonly** tutti i campi che **una volta che il loro valore è stato assegnato, non possono essere più cambiati**, anche se questo valore può variare ad ogni istanza dell'applicativo.

## 3. Classi sealed e metodi virtual
Analogamente alle variabili, anche i metodi possono essere definiti come immutabili.
Dato che, a differenza del Java, nel C# è **obbligatorio usare la parola chiave virtual per poter derivare da un metodo** (nella programmazinoe ad oggetti, un *override* di un metodo è analogo ad un cambiamento dello stesso), **tutti i metodi che non sono virtual sono implicitamente non modificabili**.
Per specificare che una classe intera non può essere modificata, utilizzo la parola **sealed**, che indica che **nessuna classe può derivare da quest'ultima**.
Anche se può sembrare ordinato scrivere più classi possibili **sealed** e meno metodi possibile **virtual** (analogamente a rendere più oggetti possibile **private**), spesso non è la soluzione migliore.
Una classe **sealed**, come un metodo **non virtual**, non potranno essere derivati, conseguentemente **nessun programmatore potrà migliorare o riutilizzare il codice scritto nella propria libreria**. Dato che spesso non si sa la direzione che prenderà il codice o il progetto, è sempre necessario prestare attenzione all'utilizzo di questi modificatori.

## 4. Approfondimento: Differenza tra abstract e virtual
Per poter comprendere meglio questo articolo, espongo qui la differenza tra un metodo **virtual** e uno **abstract**.
Una funzione astratta tipicamente **non ha corpo, ne ovviamente funzionalità**. in pratica sto dicendo che la classe figlia **deve fornire la sua versione del metodo** in quanto implementarlo nella classe padre è impossibile.
Una funzione virtuale invece significa che **esiste una funzionalità anche a livello di classe padre** che, nel caso in cui non vi sia un _override_ verrà utilizzata, ma che questa potrebbe essere non sufficentemente completa per le implementazioni delle classi figlie, conseguentemente la classe padre permette un eventuale _override_.
Conseguentemente **un metodo astratto è conseguentemente virtuale**.
Una conseguenza di questo è che **un metodo astratto può essere indicato solo in una classe astratta** (il compilatore fornisce errore se dichiaro un metodo astratto in una classe non astratta); **un metodo virtuale invece può essere dichiarato sia in una classe normale che astratta**.