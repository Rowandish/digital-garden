---
tags:
  - Coding
  - Blog
---


Questi principi seguono quanto indicato nell'ottimo libro **Head First Design Patterns** (ISBN-13: 978-0596007126).

## 1. Separa le parti che cambiano da quelle che rimangono costanti
Durante il design di un'applicazione, è necesaario essere in grado di **individuare le parti del codice che variano** (o potrebbero variare in futuro) ed **incapsularle in modo che siano indipendenti da quelle che tendono a rimanere costanti**.
In questo modo, quando devo effettuare una modifica a tali parti, queste modifiche saranno molto più semplici e dovrò andare a modificare solo il codice che effettivamente cambia.

## 2. Scegli la composizione invece dell'ereditarietà
Questa regola si può riassumere come: **HAS-A è meglio di IS-A**.
Quando collego due classi insieme, inserendo una come attributo dell'altra sto operando una **composizione** (HAS-A).
Tipicamente fare in modo che un oggetto **abbia una caratteristica esterna ad esso è meglio di creare è un oggetto intrinsicamente possiede tale caratteristica**.
L'esempio più semplice è la classe animale. Il comportamento dell'animale può sia essere scritto come metodo della classe ma è una pratica di buona programmazione fare sì che il comportamento sia **un insieme di oggetti esterni all'animale** ma che viene posto in composizione con questo ultimo.
Questo ha il vantaggio, oltre di rendere il codice più manutenibile, che posso **cambiare il comportamento a runtime**, rendono così il codice estremamente flessibile.

## 3.Programma ad interfacce, non a implementazioni
In questo caso il concetto di interfaccia non significa solo l'Interface di Java o C#, ma significa **utilizzare il polimorfismo utilizzando superclassi** (astratte o interfacce) al posto di classi concrete.
Vediamo un esempio:
Il seguente codice segue la programmazione per implementazione:
```
Dog d = new Dog();
d.bark();
```
Come si può notare questo codice è estremamente debole, in quanto se voglio cambiare animale dovrei cambiare entrambe le righe, e devo cambiarne una invece se voglio cambiare il verso.
Questo perchè aver dichiarato `d` come `Dog` ci obbliga ad utilizzare solo i metodi della classe concreta
Il codice seguente invece segue la programmazione a interfacce:
```
Animal a = new Dog();
a.makeSound();
```
in quanto io so che è un `Dog`, ma lo dichiaro con la sua superclasse astratta `Animal` che implementerà il metodo astratto `makeSound()`. In questo modo qualora volessi cambiare animale, cambierei solo il nome dell'istanza, facendo rimanere invece costante tutto il resto.
Ancora meglio è astrarre ulteriormente evitando l'istanziazione di una classe concreta hard-code, utilizzando un metodo che assegna l'istanza della variabile a runtime.
```
Animal a = getAnimal();
a.makeSound();
```
in questo caso il grado di astrazione è massimo: noi vogliamo che sia un animale e che sappia emettere suoni, poi che animale sia e come fa ad emetterli non è un problema di questa classe.

## 4.Principio dell'accoppiamento minimo
Due oggetti si dicono **minimamente accoppiati quando sono in grado di interagire fra di loro pur conoscendo il minimo possibile della struttura reciproca**.
Questo significa che

- sono flessibili all'aggiunta o alla rimozione di oggetti correlati
- per modificare un oggetto non devo modificare anche l'oggetto a questo correlato
- possiamo riusare un oggetto o l'altro in maniera indipendente tra di loro

Strutturare il codice secondo questo principio ci permette di costruire sistemi OO flessibili che possono facilmente gestire il cambiamento reciproco.

## 5. Le classi devono essere aperte all'estensione ma chiuse alla modifica
Un buon design deve creare delle classi che sono:

- **aperte all'estensione**: gli oggetti devono essere fatti in modo che sia il più facile estenderli al fine di incorporare una nuova funzionalità
- **chiusi alla modifica**: una volta che un oggetto funziona correttamente senza bug, ogni sua modifica rischia di immetterne di nuovi. Un buon design deve fare in modo che le modifiche al codice esistente su una funzionalità vecchia siano ridotte al minimo

Il nostro obiettivo è qunidi quello di crare classi che siano **facilmente estendibili al fine di incorporare un nuovo comportamento, senza che questo comportui la modifica del codice pre-esistente**.
Qualora vi sia la necessità di cambiare una funzionalità vecchia, il codice deve essere sufficentemente flessibile da poter **incoporare la modifica con il minor numero possibile di modifiche, ma solo aggiunte**.
Attenzione però, usare questo principio dovunque potrebbe portare ad un aumento di complessità non necessario e a del codice difficile da comprendere. Scegliere con cura le parti gli oggettia cui applicare questo principio.

## 6. Dipendi dalle classi astratte, non concrete
Questo principio è anche detto il *Dependency Inversion Principle* e significa che **i componenti ad alto livello non devono mai dipendere dai componenti a basso livello e nemmeno il contrario**.
Infatti **entrambi devono dipendere da componenti astratti**.
Un componente si dice ad alto livello quando il suo comportamento è definito in termini di altri componenti a basso livello.
Le seguenti linee guida aiutano a strutturare bene il codice secondo questo principio:

- **Nessuna variabile deve essere istanziata con l'operatore `new`**. Meglio usare una factory!
- **Le classi concrete non dovrebbero avere figli**. Se derivo da una classe concreta, significa che dipendo da una classe concreta. **E' sempre meglio dipendere da astrazioni**.
- Non si **dovrebbe mai eseguire un override di un metodo implementato dalla propria superclasse**: se per poter eseguire il mio codice devo eseguire un override dalla superclasse, significa che questa non era un'astrazione corretta. I metodi implementati nelle superclassi dovrebbero essere condivisi fra tutte le sottoclassi senza mai cambiare.

## 7. Principio della conoscenza minima
Il principio di minima conoscenza ci obbliga a sviluppare codice in cui **gli oggetti comunicano solo con i loro "amici vicini"**.
In poche parole, ogni oggetto deve **comunicare con il minor numero possibile di oggetti diversi e quindi possiede la minima conoscenza possibile del sistema**.
Se così non fosse avremmo molte classi tutte correlate fra di loro e il cambiamento di una porterebbe al cambiamento di molte altre.
L'esempio classico di design errato sono metodi concatenati come il seguente:
```csharp
a.getB().getC().getD()
```
Tipicamente ogni oggetto dovrebbe invocare solo metodi che appartengono a:

- l'oggetto stesso;
- oggetti passati come parametro ad un metodo dell'oggetto
- oggetti creati o istanziati da un suo metodo
- un componente dell'oggetto (relazione HAS-A)

## 8. Il principio di Hollywood
Il principio di Hollywood si può riassumere con la seguente frase:
```
Non chiamarmi, ti chiamo io
```
Questo principio ci aiuta ad evitare l'anello di dipendenze, per cui se una classe di alto livello dipende da un componenete di basso livello il quale dipende da uno di alto livello, ho una catena di componenti che rendono il sistema complesso da analizzare.
Nel principio di Hollywood permettiamo ai componenti di basso livello di agganciarsi a dei componenti di alto livello, **ma saranno loro a decidere quando questi sono necessari e come** (che spiega la frase "non chiamarmi, ti chiamo io").
Esempi di pattern che seguono questo principio sono il `Factory`, l'`Observer` e il `Template`.

## 9.Principio di singola responsabilità
Un modo alternativo per definire questo principio è: **una classe deve avere un solo motivo per cambiare**.
Il principio afferma che è necessario **assegnare ad ogni classe una ed una sola responsabilità, nel senso che si deve occupare solo di una cosa, un'azione o un oggetto**.
In un sistema ben strutturato, al momento del cambiamento, ogni oggetto cambia per solo un aspetto, non di più.