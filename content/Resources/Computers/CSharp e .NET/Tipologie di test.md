![[the-test-pyramid.png]]
* **Unit testing**: permettono di testare una classe, un metodo o anche una linea di codice. Tipicamente ogni unit test testa un singolo metodo e tipicamente ho:
	* No database call
	* No network call
	* No filesystem call
* **Component testing**: una via di mezzo tra unit e integration, tipicamente si testano più metodi insieme come fossero un componente. E' una sorta di unit testing ma con uno scope più grande.
* **Integration testing**: in questa tipologia di test non testo solo il singolo metodo ma anche le sue dipendenze, quindi database, file system, network call e così via. Fornisce una rappresentazione più realistica di come si comporta l'applicazione.
* **E2E testing**: in questo test seguo tutto il flusso dell'applicazione, quindi a partire dalla chiamata dal mondo esterno seguendo tutti i componenti veri non mockati fino alla risposta.
* **Performance testing**: come dice il nome l'obiettivo è capire le performance del sistema a fronte di un carico molto alto: per esempio faccio 1000 richieste API e verifico che il sistema rimanga corretto e risponda in tempi accettabili.

La rappresentazione dei test come unit -> integration -> E2E avviene tipicamente tramite una piramide in quanto più si sale più i test sono lenti e costosi, più si scende più sono veloci ed economici.