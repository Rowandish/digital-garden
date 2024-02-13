### Separazione di Main
Un modo per separare la costruzione dell'architettura dal suo utilizzo consiste semplicemente di trasferire tutti gli aspetti della costruzione degli oggetti in `main` o in moduli richiamati da `main` e nel progettare il resto del sistema supponendo che tutti gli oggetti siano già stati costruiti e collegati tra di loro in modo appropriato.
L'obiettivo è che la funzione `main` costruisce gli oggetti necessari per il sistema  e poi li passa all'applicazione che li utilizza.
In questo modo l'applicazione non ha alcuna conoscenza del `main` o del processo di costruzione degli oggetti.
![[photo_2024-01-29_16-52-19.jpg]]
Ovviamente non tutti gli oggetti possono essere creati subito, in questo caso posso utilizzare il pattern [[Pattern Factory#^458139|Abstract Factory]]  per dare all'applicazione il controllo sul momento in cui costruire gli oggetti che gli servono ma mantenendo tutti i dettagli di tale costruzione separati rispetto al codice dell'applicazione.
![[photo_2024-01-29_16-52-20.jpg]]

### Dependency Injection
Un potente meccanismo per separare la costruzione degli oggetti dal loro uso è la *Dependency Injection (DI)*: l'idea è che un oggetto non dovrebbe mai assumersi la responsabilità dell'istanziazione delle sue dipendenze, al contrario dovrebbe passare questa responsabilità ad un meccanismo più "autorevole", [[Principi SOLID. Dependency Inversion Principle|invertendo pertanto il controllo]].
Questo meccanismo autorevole si troverà tipicamente in `main` o in un suo modulo, come descritto sopra.
Usando la DI una classe non intraprende alcun passo diretto per risolvere le sue dipendenze (non chiama metodi come `GetObject` per intenderci) ma è completamente passiva: mette a disposizione dei parametri a costruttore o dei metodi `Setter` e assume che questi parametri vengano popolati dal motore di DI nel modo corretto.