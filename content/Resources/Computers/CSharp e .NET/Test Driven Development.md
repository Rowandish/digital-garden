---
tags:
  - Dometrain
---
## Introduzione

La modalità di lavoro Test Driven Development prevede di scrivere prima i test che descrivono il **comportamento** ideale che vorremmo dal nostro codice (che falliranno, red) e solo conseguentemente scrivere il codice che permetta a tale test di funzionare (green).
In questo modo è il codice che si adatta al test, il quale riflette il comportamento ideale, e non il contrario. 
Questo porta tipicamente ad un codice più pulito.

### Processo
* **Red**: Per prima cosa scrivere i test che riflettono il comportamento che vorremo
* **Green**: Fare in modo che questi test ora passino, senza badare troppo al codice.
* **Refactor**: una volta che i test passano refactorare il codice (rimuovere duplicazioni, code smells e così via) monitorando sempre che i test rimangano verdi. La cosa comoda è che questo refactoring risulta più semplice in quanto ci sono i test scritti nella fase precedente.
* Ritornare al red e via

Questo ciclo è molto veloce, si continua a passare dal primo al secondo e dal secondo al terzo step (vedi regole sotto). Non bisogna stare giorni sul primo step, poi giorni sul secondo e infine refactorare tutto ma è un continuo passaggio dai test all'implementazione al refactor in modo molto veloce.

Un buon metodo per iniziare è scriversi su una nota di testo che cosa vorremmo testare a partire dalle specifiche dell'applicazione in modo da avere una lista da cui partire e poi spuntare mano a mano che i test vengono fatti.

Il TDD si applica benissimo agli [[Tipologie di test|unit test e parzialmente agli integration test]], mentre non è la soluzione migliore per gli e2e test.
### 3 regole del TDD
Queste regole sono state introdotte da Robert Martin e dicono:
1. "Write production code only to make a failing test pass": bisogna sempre scrivere codice che sia riferito ad un test che fallisce, se non c'è il test non c'è codice.
2. "Write no more unit tests than sufficient to fail. Compilation failures are failures":  non serve fare tutti i test in una volta sola ma è necessario procedere per step. Per esempio all'inizio scriverò test per codice che non esiste, e quindi non compila: posso subito procede a fare in modo che il codice compili prima di scrivere altri test.
3. "Write only the production code needed to pass the one failing test": scrivi solo il codice per il test che stai guardando che fallisce, non espanderti ad altro codice. Fai piccoli step.

### Database
Per fare test su un database è una buona idea utilizzare [[Docker#^02a678|Docker]]: in questo modo divento agnostico dal PC su cui stanno girando i test utilizzando una sandbox dedicata ai test.

### REST API
Analogamente a sopra voglio creare un ambiente isolato, in questo caso utilizzo la classe `WebApplicationFactory<T>` del pacchetto `Microsoft.AspNetCore.Mvc.Testing`, per approfondimento vedi [[Integration testing in ASP.NET]].

## Errori comuni - Anti-pattern
1. **Testing Private code**: se sento la necessità di testare codice privato significa che sto testando la struttura della classe invece che il suo comportamento e tipicamente questo non va bene. Se un metodo privato è molto complesso per cui vi è la necessità di testarlo piuttosto spostarlo in una classe esterna ad hoc e renderlo pubblico. 
2. **Lanciare un solo test alla volta**
3. **Scrivere principalmente integration-test**: a volte viene naturale scrivere test che coinvolgono vari componenti dell'applicazione assumendo che, se questi passano, significa che tutta l'applicazione funziona. Anche se subito può sembrare una buona idea sul lungo periodo i bug che derivano da parti atomiche di codice non testato possono venire fuori. Conviene sempre avere tutto il codice coperto da unit test e solo successivamente procedere con i test di integrazione.
4. **Scrivere molti test prima dell'applicazione**: TDD non significa che devo scrivere tutti i test che mi vengono in mente e poi sviluppare ma lo sviluppo deve avvenire insieme alla scrittura dei test.
5. **Testare i dettagli implementativi**: Analogamente al punto 1 io dovrei avere pochi metodi public da testare che descrivono il comportamento della classe e molti metodi privati che non devo testare direttamente. Se testo tutto allora ogni modifica al codice sorgente romperà i test e questi risulteranno un peso più che una comodità.
6. **Non fare la fase di refactoring**: spesso per motivi di tempo si passa solo dal red al green senza dedicare tempo al refactoring del codice e dei test, cosa che invece è fondamentale per il design del sistema.
7. **Focalizzarsi solo sulla test-coverage**: guardare come metrica solo la coverage non ha senso in quanto io posso avere 100% di coverage potenzialmente senza nessun assert: non mi dice nulla se e come sto testando. Guardare *mutation testing*.
8. **Fare tutto con TDD**: anche se è comodo esistono altri test (*load testing* o *manual testing*) che devono essere sempre effettuati.
9. **Test inaffidabili**: se non credi nel funzionamento dei test o li reputi inaffidabili conviene eliminarli. I test devono essere la base dello sviluppo, se sono fatti male, vecchi o che non testano nulla conviene piuttosto non averli.
10. **Test troppo lunghi**: se lanciare i test ci mette troppo arriverò al punto dove non li lancio proprio, oppure lancio solo un test alla volta. Test lunghi sono sintomo di problematiche di progettazione e non dovrebbero esserci (vedi la sezione sugli *Adapter* sopra).

## BDD vs ATDD
BDD (Behavioural Driven Development) cerca di risolvere il problema per cui i test sono spesso scorrelati dal mondo reale, nel senso che si focalizzano sul codice ma non sulle specifiche dell'utente finale o del cliente che ha commissionato tale codice.
Nel BDD si usa il linguaggio naturale non tecnico dove sono indicate le specifiche che deve rispettare il codice nella sintassi `Given/When/Then`, per esempio
```
Given I last used the app yesterday
When I use the app
Then I am notified about overdue tasks
```
Anche se usano il linguaggio naturale questi test sono comunque definiti dagli sviluppatori interni al progetto.
Il ATDD (Acceptance Test Driven Development) è simile al BDD (gli Acceptance Test sono le specifiche che devono essere concordate insieme al cliente) con la differenza che nell'ATDD le specifiche vengono scritte non dagli sviluppatori ma dal cliente o reparto commerciale e indicano che cosa il cliente si aspetta dal software che dovrà essere sviluppato.
Tipicamente gli Acceptance Test sono molto lenti in quanto riguardano tutta l'applicazione.

## Mutation Testing
Questa tipologia di test permette di capire la qualità dei nostri test, cosa che non può essere fatta guardando solo la coverage dato che quest'ultima è facilmente "hackerabile".
Il mutation testing è una specie di test per i test: esiste un *mutation tool* che crea dei *mutants* che è versione del codice leggermente diversa e verifica che il test sia resiliente a tali mutazioni.
L'idea è che i test devono rilevare eventuali bug futuri, quindi se io introduco un bug devo avere dei test rossi. Se invece introducendo tale bug i test rimangono verdi significa che non stanno veramente testando tutti i casi.
In .NET questi test si possono fare con il pacchetto nuget `Stryker.NET`.
Per esempio in questo caso il test è stato lanciato modificando il codice con `price <= 0` invece che `price < 0`, mi aspetto che qualche test dia RED. Se invece tutti i test danno ancora GREEN significa che *mutant has survived*
![[Pasted image 20250210155031.png]]
Utilizzare spesso questo tool permette di ottenere una valutazione della qualità dei nostri test e, se usato di frequente, permetterci migliorare nella stesura di tali test.

## Testare sistemi Legacy
Per lavorare sui sistemi legacy devo utilizzare delle tecniche leggermente diverse in quanto tipicamente questi sono delle black box di difficile comprensione.
L'**Approval Testing** (o **Characterization Testing**) è una tecnica di test del software utilizzata per verificare che un sistema si comporti in modo coerente prima e dopo una modifica. Invece di scrivere test basati su risultati attesi noti, questi test catturano l'output attuale del sistema e lo usano come riferimento per confronti futuri.
Utile in sistemi legacy o complessi dove il comportamento non è ben documentato.
In dotnet la libreria principale è `ApprovalTests.NET` anche se funziona bene `Verify.Xunit`.
Il processo è semplice: per prima cosa si scrivono dei test che coprono la maggior parte del codice legacy che voglio sistemare in modo da sapere il suo output, una sorta di cintura di sicurezza.
Questi test sul sistema legacy non stanno "testando" qualcosa ma sono più che altro delle verifiche sull'outout in modo avere a disposizione, dopo il refactor, l'output vecchio e verificare che sia uguale.
Una volta che ho questi test posso proceder col refactor ma con la consapevolezza che non sto rompendo nulla in quanto l'output nuovo è uguale al vecchio.
