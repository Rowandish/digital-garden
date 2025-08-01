## Monoliths
Architettura classica dove tutto è in un unico punto. E' ottima per iniziare un progetto in quanto è semplice da lanciare, da testare e da sviluppare ma può essere un limite se bisogna aggiungere scalabilità il progetto.
E' buona norma partire con un'architettura monolitica nell'ottica di passare, mano a mano che la complessità aumenta, ad un architettura distribuita.
## Layered
In questa architettura ho *n* strati, a partire dal presentation per andare alla business logic fino a livello dei dati dove tipicamente c'è il database.
Può avere senso se l'azienda dove si lavora è strutturata in sviluppatori frontend, backend e database o, in generale, ci sono strutture rigide.
Ha senso quando devo sviluppare una semplice applicazione CRUD.
## Domain Centric
^088b39

Queste architetture hanno come obiettivo **separare la business logic core dalle dipendenze esterne** come la user interface, il database, dipendenze esterne e così via.
Queste sono:
* Hexagonal architecture
* Onion architecture
* [[Clean Architecture]]

L'architettura a strati è quella classica in cui abbiamo i livello di interfaccia che dipende dalla Business Logic la quale dipende dal Data Access che tipicamente è il database.
Anche se questo è l'approccio più comune e utilizzato ha un limite: tutte le frecce, quindi le dipendenze, sono sul database. Potenzialmente anche il lato applicativo dipende e può operare sul database, dipendendo da questo ultimo.

![[Pasted image 20241127111214.png]]Nelle architetture *Damain Centric* il focus viene spostato dal database alla *Business Logic*: tutte le frecce punteranno a quest'ultimo senza questa abbia dipendenze sul *Data Access Layer*.
Nelle architetture *Domain Centric* posso modificare il database senza che questo abbia alcuna influenza sulla business logic.
Esempi sono:
* [[Clean Architecture]]
* Hexagonal/Ports and Adapters Architecture
* Onion Architecture
![[Pasted image 20241127111907.png]]
Come si nota in questo modo io posso sviluppare la parte di *Domain*, quindi la business logic della mia applicazione senza considerare ne la parte di *Presentation* ne quella di accesso al db, qui chiamata *Infrastructure*.

Queste architetture sono da utilizzare quando ho una business logic complessa che cambia spesso e che quindi deve essere centrale nell'applicazione.
## Service Oriented architecture
In questa architettura la funzionalità del sistema è divisa in tanti piccoli servizi ognuno che è responsabile di una singola cosa.
Con l'analogia di una città, che è il nostro software, ogni negozio risponde ad una singola esigenza: la lavanderia lava, il panettiere fornisce il pane e così via.
Questa architettura ha il focus sulla scalabilità e la flessibilità con però l'aggiunta di notevole complessità nel sistema in quanto è necessaria molta coordinazione affinché tutti i servizi comunichino efficacemente insieme.
Ha senso quando ho un'applicazione complessa che potrebbe dover scalare in modo diverso tra i vari componenti, oppure quando l'organizzazione della mia azienda non è la classica frontend/backend ma è invece a team dove ogni team si occupa di un servizio dell'applicazione (esempio order team, payment team, delivery team...).
## Microservices
In un'architettura a microservizi l'applicazione nel suo complesso è divisa in tanti piccoli servizi che fanno una sola piccola cosa e la fanno molto bene.
Si definisce microservizio una unità indipendente deployable.
Con questa architettura posso quindi modificare un singolo servizio senza che modificare nulla del resto e senza nemmeno che gli altri servizi lo sappiano.
La differenza con la Service Oriented Architecture è che questa ultima tende ad avere servizi molto più grossi che fanno tante cose; nei microservices invece ho tanti piccoli elementi che fanno compiti semplici e che interagiscono tra di loro.
### Quando usarli
* I team possono lavorare indipendentemente l'uno dall'altro
* Aumenta la robustezza del sistema in quanto se fa down un servizio non si porta dietro tutti gli altri
* Posso utilizzare tecnologie diverse tra i servizi ed è semplice passare a tecnologie nuove magari solo per alcuni servizi invece di dover aggiornare tutto insieme
### Quando non usarli
* Quando non si conosce bene il dominio o i requisiti dell'applicazione
* Quando non è chiaro come dividere il software e quale team si occuperà di cosa. Refactorare la divisione dei servizi può essere molto doloroso.
* Quando voglio lanciare un nuovo progetto da zero, conviene iniziare col monolitico e poi eventualmente passare ai microservizi una volta che è chiaro cosa fanno gli utenti, come è il team dell'azienda e come è fatto il dominio
* Quando non sono strettamente necessari: non sei Netflix e spesso e volentieri non necessiti di quella complessità.
## [[Event-Driven Architecture]]
Questa architettura è focalizzata sugli eventi: questi sono degli oggetti che indicano che è successo qualcosa di significativo, sono immutabili, successi nel passato e non possono essere modificati successivamente.
Sono tipicamente formati da un header con i metadati e da un body con il payload, quindi con i dati effettivi dell'evento.
L'idea è che se un servizio A deve comunicare con B non comunica direttamente in quanto questo porta ad un forte accoppiamento che non vogliamo, ma comunica solo ad un'entità terza che un certo evento è successo.
Sarà poi il servizio B che comunicherà con questa entità terza per ottenere solo gli eventi che gli interessano e processarli di conseguenza.
La base di queste architettura sono le code (in AWS le [[SQS]]) o i bus (in AWS i [[SNS]]).
## Quale scegliere?
Non è sempre detto che le architetture complesse siano le migliori, per esempio se devo scrivere un'applicazione che deve solo fare delle operazioni CRUD su un database con delle semplici API è inutile aggiungere tutto l'overkill di una struttura Clean Architecture, per esempio.
Molto meglio una layered con 3 livelli classici.
Al contrario al crescere della complessità dell'applicazione che devo sviluppare aumenta il vantaggio nell'usare architetture complesse.