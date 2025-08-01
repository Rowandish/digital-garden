---
tags:
  - Dometrain
---
Questa nota prende a piene mani dal corso [From Zero to Hero: JetBrains Rider](https://dometrain.com/course/from-zero-to-hero-jetbrains-rider/).

## Shortcut

### Big Three
Ci sono centinaia di shortcut ma i più usati son:
* `Ctrl + T`: ricerca di qualsiasi cosa, anche settings
* `Alt + Enter`: triggera il suggerimento di fix o refactor
* `Alt + Ins`: apre menu a tendina per creare costruttore, metodi, override e così via
### Others
* `Ctrl + Alt + S`: apre la finestra dei setting
* `Ctrl + Tab`: permette di passare da un file all'altro tra i file aperti
* `F12`: entra nella definizione di un metodo. Analogo a `Ctrl + Click`
* `Shift + F12`: mostra i chiamanti di un metodo
* `Alt + Home`: vai al metodo della superclasse
* `Alt + End`: vai all'override del metodo, se esiste
* `Alt + up/down`: passa da un metodo all'altro in un file
* `Ctrl + Alt + Shift + up/down`: sposta un metodo prima/dopo il precedente/successivo
* `Ctrl + -`: permette di passare alla posizione precedente, sia che sia in un file dove ero prima con il cursore sia che sia nel file visualizzato precedentemente. Analogo alla freccia "indietro" a grafica.
* `Ctrl + G`: go to line
* `Ctrl + Shift + R`: apre il menu di refactor dell'oggetto
* `Ctrl + Alt + Shift + A`: ispeziona il metodo
	* *Incoming calls*: versione più potente di `Shift + F12` dove si vede una specie di call stack di tutti i chiamanti del metodo e dei chiamanti dei chiamanti e così via
* `Ctrl + Shift + F`: find in files
* `Ctrl + Shift + H`: replace in files
	* `Alt + E`: preserve case
* `Ctrl + R + R`: rinomina oggetto
* `Ctrl + R + S`: modifica la signature di un metodo
* `Ctrl + R + M`: estrae il codice selezionato in un metodo
* `Ctrl + Shift + Enter`: crea le parentesi dopo un `if` o dopo un ciclo e sposta il cursore all'interno
* `Ctrl + E + C`: apre la finestra per il cleanup del file o progetto, quindi sistema using, tab, spazi e così via.
## Bookmarks
I bookmarks permettono di contrassegnare linee di codice specifiche per un rapido accesso e navigazione.
Consentono quindi di poter passare molto velocemente da una riga all'altra nel codice che sto sviluppando permettendomi così di essere molto più efficace e produttivo.
Esistono due tipi di segnalibri: mnemonici, identificati da numeri o lettere, e anonimi, senza identificatori.
Ogni bookmark può essere rinominato in modo da avere chiaro ognuno a cosa punta.
### Shortcut
* `Ctrl+KK` : Toggle bookmark in una riga di codice;
* `Ctrl+KW` : Apre una piccola finestra di gestione dei bookmarks e permette di passare da uno all'altro
* `Alt+2`: Apre la finestra di gestione dei bookmarks/breakpoint;
* `Ctrl+Shift+[0-9]`: Toggle bookmark mnemonico con il numero indicato;
* `Ctrl+[0-9]`: Vai al bookmark mnemonico con il numero indicato.

## Debugging

### Ispezionare LINQ concatenate
La combinazione **Alt + Click** su una variabile o un'espressione ti permette di **Valutare rapidamente il valore** di una variabile o anche di un'intera espressione direttamente nel codice, **senza aprire manualmente la finestra di valutazione**.
Quando lavori con **espressioni LINQ complesse** (es. `.Where(...).Select(...).OrderBy(...)`), usare **Alt + Click** è comodissimo per vedere **il risultato parziale** di ogni step nella catena (es. solo il `Where`, solo il `Select`, ecc.).    

### `[DebuggerDisplay]`
L’attributo **`[DebuggerDisplay]`** ti permette di **personalizzare come viene mostrato un oggetto nel debugger**, rendendo il debug **più chiaro e leggibile**.
```csharp
[DebuggerDisplay("User: {Name}, Age: {Age}")]
public class User
{
    public string Name { get; set; }
    public int Age { get; set; }
}
```
Quando fermi il debugger su un oggetto `User`, invece di vedere solo il nome della classe, vedrai ad esempio:
```
User: Alice, Age: 30
```

### Freeze Threads
Nel debugger di Rider, usare **"Freeze Thread"** ti permette di **bloccare l'esecuzione di un thread specifico**, lasciando che gli altri continuino. Questo è utile quando vuoi analizzare **lo stato esatto di un thread senza che cambi sotto i tuoi occhi**, soprattutto in situazioni di concorrenza.
Al contrario, **"Freeze Other Threads"** congela tutti gli altri tranne quello attivo, così puoi **focalizzarti su un singolo flusso di esecuzione** senza interferenze. È molto utile per capire il comportamento in scenari multithread complessi, dove i problemi sono spesso legati alla sincronizzazione o all’ordine delle operazioni.
Lo posso fare nella finestra di debugging quando sono fermo su un breakpoint facendo tasto destro sul thread in questione.
![[Pasted image 20250328102037.png]]

### Set data breakpoint
**"Set Data Breakpoint"** ti permette di dire al debugger: _"Fermati quando questo valore cambia."_  
È utile quando non sai **dove** o **quando** una variabile viene modificata, ma vuoi scoprirlo.
Funziona solo su **campi di istanza** (non variabili locali) e Rider interromperà l'esecuzione **appena quel campo cambia**, mostrandoti **chi l'ha modificato** e in quale contesto.  
Perfetto per bug misteriosi dove "qualcosa cambia ma non so dove".
Per impostarlo:
1. **Avvia il debugging**    
2. Fermati in un punto in cui hai accesso all’**istanza dell’oggetto** che contiene il campo (ad esempio in una watch o nella finestra _locals_).    
3. Nella finestra di **Variables** (o _Watches/Locals_), trova il campo che vuoi monitorare (es: `account.Balance`).    
4. Fai **click destro** sul campo → seleziona **"Set Data Breakpoint"**.
![[Pasted image 20250328102728.png]]
## Git

TODO

## Tests

### Shortcut
* `Ctrl + U + L`: lancia tutti i test nella soluzione
* `Ctrl + U + F`: lancia tutti i test falliti della scorsa run
### Test Session
Se voglio concentrarmi su un sottoinsieme di test particolare posso creare una nuova "Test Session" facendo tasto dx su un oggetto nella tab dei test e `Create New Session`; questo aprirà una nuova tab con i test selezionati. A questi posso aggiungerne altri con sempre con tasto dx e `Append Tests to Session`.
### Continuous Testing
In alcuni casi può essere utile avere i test che continuano a girare durante lo sviluppo del codice in modo che sia chiaro subito se sto rompendo qualcosa o invece se lo sto sistemando.
Ovviamente questo appesantisce comunque l'IDE quindi ha senso non farlo su tutti i test ma solo su un loro sottoinsieme rilevante per me.
Per farlo basta selezionare i test in questione e premere `Set|Append Selected Tests To Continuous Testing Session`. Questo aprirà una nuova tab con solo i test selezionati e questi verranno lanciati ogni volta che si salva il file.
Per abilitare che si lanciano al salva andare nei setting e cercare `Trigger Continuous Testing on -> Save`.
### Flaky Tests
Può succedere di avere test che hanno risultati non sempre definiti, a volte falliscono ma in situazioni non chiare (esempio in ambienti di multithreading).
Molto utile in questi casi il comando `Run/Debug Unit Tests Until Fail` che, come dice il nome, continua a lanciare il test fino a quando fallisce.
### Diff tra file generati dai test
Se il test genera dei file posso mostrare nell'interfaccia dei risultati dei test un comodo diff che apre il difftool di rider.
Vedi: https://www.jetbrains.com/help/rider/Analyze_test_results.html#compare-files-from-test-output

## Dependency Diagram

### Project Dependency Diagram
Permettono di visualizzare l'albero delle dipendenze di un determinato progetto.
Abilitando la "coupling analysis" viene analizzato anche se una dipendenza è davvero necessario o si può rimuovere, come nell'esempio sotto dove `IMAMultilanguage` è una dipendenza di `IMAUser` ma non necessaria.

![[Pasted image 20250703104657.png]]

### Type Dependency Diagram
Permette di visualizzare la dipendenza tra i tipi di un determinato progetto o anche solo di alcune classi.
A differenza del `Project Diagram` questo può anche partire da un singolo tipo e poi si può fare drag and drop dei tipi che si vogliono analizzare. Ha quindi vari livelli di scope.
Anche quando si fa il `Find Usages` o il `Show Derived types` si può cliccare sull'icona pr mostrare tali dipendenze in questo diagramma.
Alcune shortcut comode:
* `Ctrl+Mouse Wheel`: zoom
* `Alt`: area zoom
* `Ctrl+Click`: pan
* `Click`: show usages 

## HTTP Client integrato
L'HTTP Client si basa su file `.http` o `.rest` che contengono le definizioni delle richieste HTTP. Questi file sono semplici file di testo con una sintassi intuitiva per specificare il metodo HTTP/GRPC, l'URL, gli header, il corpo della richiesta e altre opzioni.
Quando esegui una richiesta da questi file (tramite un pulsante "Play" che compare accanto ad essa), Rider invia la richiesta e visualizza la risposta in una finestra dedicata, completa di stato, header e corpo della risposta.

```http
### Get a list of posts
GET https://jsonplaceholder.typicode.com/posts

### Create a new post
POST https://jsonplaceholder.typicode.com/posts
Content-Type: application/json

{
  "title": "foo",
  "body": "bar",
  "userId": 1
}
```

### Cosa sono gli Environment

Gli environment (ambienti) sono un concetto fondamentale per gestire diverse configurazioni delle richieste, ad esempio per sviluppo, staging e produzione. Invece di modificare manualmente l'URL di base o le chiavi API ogni volta, puoi definire variabili specifiche per ciascun ambiente.

Per esempio, potresti avere un ambiente "Development" con `{{baseUrl}} = http://localhost:8080` e un ambiente "Production" con `{{baseUrl}} = https://api.yourcompany.com`. Nel tuo file `.http`, useresti `GET {{baseUrl}}/users` e al momento dell'esecuzione potresti selezionare l'ambiente desiderato dal dropdown in alto.

Gli environment sono definiti in file `.env` o `.private.env` (per variabili sensibili che non dovrebbero essere committate nel controllo versione) e possono contenere coppie chiave-valore. Rider supporta anche variabili dinamiche e la possibilità di includere file esterni.

## Remote development

L'idea è delegare ad un server remoto la parte di calcolo e avere in locale solo un'IDE leggero che può girare anche su un PC con scarse performance.
Step per l'installazione:
1. Installa OpenSSH Server sulla VM Windows: per prima cosa, dovrai abilitare le connessioni SSH sulla tua VM Windows. Scarica l'installer di OpenSSH Server dal repository ufficiale di GitHub. Puoi trovarlo qui: https://github.com/PowerShell/Win32-OpenSSH/releases. Esegui l'installer sulla tua VM.    
2. Configura il Firewall di Windows: dopo l'installazione di OpenSSH, è fondamentale assicurarsi che il firewall di Windows consenta le connessioni in entrata sulla porta 22, che è la porta standard per SSH. Aggiungi una regola in entrata per permettere queste connessioni.    
3. Verifica il Funzionamento di SSH: per confermare che il server SSH sia configurato correttamente e in ascolto, puoi utilizzare telnet dal tuo computer locale. Apri un prompt dei comandi o PowerShell e digita `telnet <IndirizzoIPdellaVM> 22`. Se la connessione ha successo (vedrai una schermata vuota o un messaggio di benvenuto), significa che SSH è attivo sulla VM.    
4. Scarica JetBrains Toolbox App sul Tuo PC Locale: sul tuo computer locale, scarica e installa la JetBrains Toolbox App.    
5. Stabilisci la Connessione SSH tramite JetBrains Toolbox: apri la JetBrains Toolbox App sul tuo PC locale. Premi `Alt + 2` per accedere alla sezione SSH. Qui, inserisci il l'indirizzo IP e le credenziali per la VM Windows. È normale che la fase di "connecting" duri circa 10 minuti; sii paziente.   
6. Installazione di Rider sulla VM Remota: una volta stabilita la connessione, seleziona "Rider" dall'elenco. La JetBrains Toolbox installerà una versione di Rider (un "backend" headless) sulla VM remota e un client leggero (JetBrains Client) sul tuo PC locale, solitamente in `\AppData\`. Questo client locale è l'interfaccia con cui interagirai, mentre tutte le operazioni pesanti avvengono sulla VM.   
7. Clonazione di Progetti e Inizio Sviluppo: dalla JetBrains Toolbox App, apri JetBrains Rider. Inizialmente, non vedrai alcun progetto. Utilizza l'opzione "Clone from Repo" e fornisci le credenziali per il tuo provider di repository. Il progetto verrà clonato sulla VM remota, tipicamente in `C:\Users\<nomeutente>\RiderProjects`.
8. Gestione dei File di Compilazione: è importante notare che tutti i file di compilazione, i file temporanei e i risultati del processo di build saranno creati e gestiti interamente sulla VM remota. Il tuo PC locale non archivierà alcun file relativo alla compilazione.

### Applicazioni con interfaccia grafica
Quando avvii una connessione SSH con JetBrains Gateway (o il Toolbox App), la macchina remota ospita un **backend di Rider** che viene eseguito in modalità **headless**. Ciò significa che non ha un'interfaccia utente grafica. Questo backend si occupa di tutte le operazioni intensive come l'indicizzazione del codice, la build, il debug e l'analisi.

Sulla tua macchina locale, invece, gira un **client leggero (JetBrains Client)**. Questo client ti fornisce l'interfaccia utente completa dell'IDE, ma comunica costantemente con il backend sulla VM remota tramite un protocollo RPC dedicato.

**Un aspetto cruciale da ricordare è che questo flusso non include il forwarding delle finestre di applicazioni grafiche.** Ciò significa che se il tuo codice dovesse tentare di visualizzare una finestra (ad esempio, chiamando `ShowDialog()` o aprendo qualsiasi finestra WPF), questa operazione verrebbe eseguita nella sessione remota senza un display e **non** verrebbe visualizzata sul tuo client SSH locale lanciando un'eccezione di `Impossibile visualizzare un form o una finestra di dialogo modale quando l'applicazione è in esecuzione in una modalità diversa da UserInteractive`.

## Integrazione con database
Rider ha un gestore di DMBS integrato.
Nella sezione `Database -> Connect to database` e inserire i dati necessari.

Nella finestra della gestione database di fianco agli oggetti c'è un piccolo quadratino con scritto, esempio "1 su 6".
![[Pasted image 20250716161746.png]]
Cliccandoci sopra posso modificare l'oggetto che sto visualizzando.
Facendo doppio click sull'oggetto del database posso visualizzarlo e inoltre:
* Aggiungere un filtro sopra le colonne stile Excel
* Visualizzare grafici sui dati impostando asse X e Y
* Visualizzare uno o più righe come record in un'interfaccia ad hoc

### Attach Data Source
Una funzionalità molto potente è poter lavorare con il syntax highlight e intellisense sulle query anche in un file non `.sql` ma, esempio, un normale file `.NET`.
Per fare questo fare tasto dx sulla query e premere `Attach Data Source`
![[Pasted image 20250716170433.png]]
In alto a dx comparirà una combobox per selezionare il database e lo schema a cui appartiene tale query e questo permette di avere l'intellisense e il syntax highlight.
![[Pasted image 20250716170543.png]]

## Terminal
Su Rider posso avere uno o più finestre terminali, sia `cmd` classico che `Powershell`.
Posso aprire direttamente la finestra oppure fare `tasto dx -> Open In -> Terminal`.
Di default non viene visualizzata l'estetica custom della PowerShell di sistema (esempio se si utilizza `Oh My Posh` come plugin. Per abilitare tale estetica fare `tasto dx -> Prompt Style -> Shell Prompt (PS1)`).
![[Pasted image 20250716173121.png]]

## Tips & Tricks

* **Preserve case**: spesso devo fare un replace di una stringa con un altra ma tale stringa potrebbe avere vari case diversi, esempio `handler` e `Handler` e vorrei che il case venisse preservato. Nella finestra di replace (`Ctrl + Shift + H`) se premo `Alt + E` (o l'incona con due "A" a destra della textbox di replace) il replace preserverà il case originario
* **Local History**: Rider tiene traccia di tutte le modifiche che sono avvenute in un file o in un progetto in delle sue strutture dati e le mantiene per 5 giorni (modificabili sa setting). Questo può essere utile se non ho git oppure se ho fatto troppe modifiche tra un commit e l'altro e temo di aver perso qualcosa. Data una modifica posso anche crearne facilmente una patch in modo che sia condivisibile con altri componenti del team.


