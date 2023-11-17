---
tags:
  - Productivity
  - Minimalism
---
Nel frattempo sto anche sistemando la mia vita digitale: passando almeno 10 ore al giorno al computer o YouTube diventa sempre più necessario rendere l'internet un posto migliore per me.
Ultimamente questo sta diventando un luogo atto più a far perdere tempo e a far guadagnare i pubblicitari che uno strumento utile a creare effettivamente valore.
Ho quindi deciso di impormi le seguenti regole, che devono valere sia su PC desktop che su mobile:
* No pubblicità (tranne nei siti dove esplicitamente la consento per supportare);
* No YouTube Short (Se voglio usare TikTok lo scarico, YouTube deve rimanere YouTube);
* No notifiche (consiglio a tal proposito [[Deep work - Concentrati al massimo]]);
* No app ma solo navigazione con browser (quindi no social network di alcun genere e rimozione di tutte le app se non quelle strettamente necessarie);
* No feed (voglio essere intenzionale in quello che guardo e non far sì che sia un algoritmo a scegliere cosa devo vedere);
* Mantenimento della propria inbox pulita e minimale;
* Ban di siti dannosi (se noto che leggere un sito mi fa perdere tempo (es. gazzetta) o altera il mio umore (es. siti di informazione) ne viene impedito l'accesso).

Dato che per ottenere questo ho bisogno di vari add-on sono passato da Chrome a Firefox come browser: il motivo principale è che Chrome su mobile non permette l'installazione di questi ultimi, che sono invece dei componenti essenziali per ottenere quanto voglio.

Vediamo ora i vari plugin che utilizzo, che valgono con le stesse impostazioni sia su desktop che mobile, a meno che diversamente specificato.

## No Pubblicità
Per rimuovere la pubblicità utilizzo [UBlock Origin](https://github.com/gorhill/uBlock) .
Questo add-on blocca anche i tracker e i siti contenenti malware oltre a permettere una customizzazione dei propri filtri.
Rimando alla loro repository per ulteriori informazioni ma mi collego alla prossima sezione, cioè la rimozione degli YouTube shorts.

## No YouTube Short
Con UBlock Origin è possibile customizzare i filtraggi in modo da rimuovere dei CSS indesiderati in particolari siti come se fossero degli ads.
In [questo sito](https://letsblock.it/filters) potete trovare un elenco di filtri custom comodi e in particolare [questo](https://letsblock.it/filters/youtube-shorts) è il filtro che utilizzo per rimuovere gli short di YouTube.

## No notifiche
Dato che non voglio continuamente essere distratto da algoritmi che cercano di catturare la mia attenzione ho impedito a tutte le app (tranne Telegram con le chat personali e poche altre) di inviarmi notifiche.

## No app social
Utilizzare i social tramite le app porta a numerosi problemi:
* Impossibilità di togliere la pubblicità;
* Impossibilità di togliere gli short su youtube;
* Navigazione più fluida e più bella, quindi più distraente;
* (YouTube) Obbligo di passare attraverso la homepage invece che dalla pagina dei subscribers;
* Consumo maggiore di batteria;
* Notifiche.
Ho quindi volutamente scelto di disinstallare tutti i social che utilizzavo (YouTube in primis ma anche Facebook, Instagram e Twitch) in modo da poterci accedere solo tramite browser.
Ottengo quindi tutti i vantaggi elencati sopra con un fantastico side effect: posso vedere youtube senza pubblicità e perfino con i video in background a cellulare spento!

## No bacheche e feed
Questo è uno dei punti che più mi stanno a cuore: voglio essere io che intenzionalmente decido che video vedere, che persona seguire, che trend analizzare e non permettere ad un algoritmo di scegliere per me.
Fino a poco tempo fa ero anche io del partito "beh alla fine l'algoritmo sceglie quello che piace a me, quindi mi sta bene" anche se, una volta rimossi i feed, mi sono reso conto che il 90% dei contenuti che guardavo suggeriti dall'algoritmo erano spazzatura.
Non voglio alcuna news feed, alcun suggerimento, alcun "credo ti possa piacere XXX", voglio essere io a scegliere.
Per fare questo utilizzo [News feed eradicator](https://github.com/jordwest/news-feed-eradicator) che sostituisce i feed dei siti che indichiamo con delle citazioni (presente solo su desktop).
La mia homepage di Facebook, reddit e soprattutto YouTube sono vuote.
Anche la barra laterale di YouTube è vuota e, una volta abituati, non si torna più indietro.
![[Pasted image 20221014232215.png]]

### YouTube subscribers
Un corollario alla regola descritta sopra è il desiderio di accedere ad una homepage "alternativa" di YouTube che contiene solo ed escusivamente i video dei canali a cui sono iscritto in ordine cronologico.
Questa pagina esiste ed è la [pagina delle iscrizioni](https://www.youtube.com/feed/subscriptions).
Ho creato un link ai preferiti e nell'home screen dello smartphone in modo che youtube si apra sempre su tale pagina e non sulla home.

## No Mail indesiderate
La questione delle troppe mail è un annoso problema sia in ambiente lavorativo che extra. 
A tal proposito consiglio, oltre al sopracitato Deep Work, anche  A World Without Email sempre di Cal Newport.
Il discorso è molto lungo, ma in questa sede suggerisco solo di creare una serie di filtri in Thunderbird (Tools -> Message Filters) che mandano nel cestino tutte le mail con determinate caratteristiche di mittente e oggetto.

## Siti non desiderati
Mentre nei punti precedenti l'obiettivo era ridurre la pubblicità, le distrazioni in questo caso voglio evitare forzatamente di andare su siti che ritengo siano dannosi per me.
Per esempio la gazzetta mi faceva solo perdere tempo, i siti di informazione alteravano negativamente il mio umore, i social mi triggeravano continuamente con la continua ostentazione di vite perfette.
Ho quindi installato [Leechblock](https://addons.mozilla.org/en-US/firefox/addon/leechblock-ng/) che permette di bloccare un elenco di siti a propria scelta (o anche solo dei sottodomini) per un determinato periodo di tempo.
All'inizio avevo bloccato tutto solo in orario lavorativo ma mi sono accorto che non bastava: appena scattavano le 18 ci ricascavo.
Ho quindi esteso il periodo di blocco alle 24h e, per ora, nessun ripensamento.
Un unico appunto: dato che a volte può essere utile accedere ad un sottodomino di instagram o facebook ho utilizzato questa sintassi in Leechblock:
```
+facebook.com/*+
+instagram.com/*+
facebook.com
instagram.com
```
In questo modo instagram.com è bannato ma non lo è https://www.instagram.com/cristiano/, per esempio.

### Aggiornamento 2023
Tra gli obiettivi del 2023 voglio ridurre il tempo che passo a guardare video su YouTube: nonostante tutti i miei blocchi ci ricascavo ancora e perdevo tantissimo tempo.
Certo, almeno non lo perdevo su Instagram o social analoghi ma comunque guardavo una quantità spropositata di video su YouTube al giorno.
Ho quindi aggiunto un limitatore orario su YouTube (solo comunque i singoli video, la home page l'ho già bloccata) che mi permette di guardare video per un massimo di 45 minuti al giorno.
Troppi? Troppo pochi? Lo scopriremo.
La cosa comodissima di Leechblock è l'opzione "Count time spent on these sites only when browser tab is active" che mi permette di non scalare il contatore dei minuti se sto ascoltando un video (per esempio mentre sono in macchina).
![[Pasted image 20230103233850.png]]



