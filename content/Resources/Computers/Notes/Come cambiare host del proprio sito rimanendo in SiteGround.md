---
tags:
  - Draft
---

Per l'hosting di questo sito utilizzo SiteGround, un servizio molto affidabile ma estremamente costoso dopo il primo anno: tipicamente questo fornisce delle ottime offerte (soprattutto durante il black Friday) a prezzi come 2€ al mese circa per poi caricare dall'anno successivo a 13€ al mese + IVA:
![[Pasted image 20221121165200.png]]
![[Pasted image 20221121165212.png]]
L'idea è puntare sulla pigrizia delle persone nel cambiare hosting e sul tacito rinnovo automatico: per fortuna la carta che aveva memorizzato non aveva fondi altrimenti una settimana prima del termine avevo scalato il prezzo per l'intero anno!
La cosa interessante è che, almeno questo anno, mi ha proposto la stessa offerta dell'anno scorso per la creazione di un nuovo piano di hosting: con 2€ al mese ho 1 anno di hosting con tutti i servizi di SiteGround. Mica male!
Dopo aver accettato l'offerta la mia situazione è la seguente:
![[Pasted image 20221121165029.png]]
Conseguentemente devo cercare il modo più semplice possibile per passare tutti i dati del sito dal vecchio al nuovo hosting e, una volta completata l'operazione, il gioco è fatto!
### Superfast WordPress Automigration
SiteGround offre un servizio comodissimo di migrazione che permette in pochi click di migrare tutto il contenuto di un sito WordPress da un host all'altro.
Andiamo sul nuovo hosting e premiamo "Set up site" creando un dominio temporaneo.
Cliccare su "Migrate Website" e "Superfast WordPress Automigration".
![[Pasted image 20221121172528.png]]
Verrà fornito un token da copiare.
Andare sul `wp-admin` del vecchio sito, installare il plugin *SiteGround Migrator*, inserire il token e premere *Start migration*.
Verrà fornito un warning indicante che il dominio è diverso (ovviamente), premere *continue*.
Il migrator farà tutto in autonomia.
![[Pasted image 20221121172326.png]] 
Una volta completato verrà fornito un url temporaneo
![[Pasted image 20221121173559.png]]
Una volta fatto questo bisogna procedere con l'eliminazione del vecchio sito e cambiare il primary domain del nuovo.
Conviene cancellare i cookie e rifare il login per evitare problemi di permessi.
Successivamente serve reinstallare SSL Site tools -> SSL Manager -> install Let's encrypt


### Backup
Questo blog è un sito creato con Wordpress e per effettuare il backup basta scaricare tutti i dati del sito e il database.
#### Backup del sito
Il backup del sito è tutto il contenuto della cartella `public_html`, per scaricarlo andare su site tools -> File manager -> selezionare tutto il contenuto di public_html -> archive -> scrivere un nome a scelta.
Questa operazione creerà un file zip nella stessa cartella con il nome che gli abbiamo dato: scarichiamolo.
Una volta fatto eliminare lo zip dal server che non serve più a nulla.
#### Backup del database
Ora serve anche il backup del database, per farlo andiamo su
Site tools -> MySQL -> PhpMyAdmin -> Access PhpMyAdmin.
In alto a sinistra clicchiamo sul database di cui vogliamo effettuare il backup
![[Pasted image 20221121164516.png]]
Clicchiamo in alto su "Export", lasciamo le impostazioni di default (SQL e quick) e premiamo "Go": verrà scaricato un file chiamato localhost.sql.
### Restore
Andiamo sul nuovo hosting e premiamo "Set up site". Creiamo un dominio temporaneo.

![[Pasted image 20221121175102.png]]