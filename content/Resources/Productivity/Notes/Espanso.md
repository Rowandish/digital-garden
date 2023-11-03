---
tags:
  - Productivity
---
[Espanso](https://espanso.org/) è una applicazione che permette di configurare in maniera comoda snippet di testo da sostituire automaticamente quando vengono scritti.

### Configurazione
Una volta installato i file di configurazione si trovano in `C:\Users\paolo\AppData\Roaming\espanso` dove ci sono due cartelle che a loro volta contengono due file, rispettivamente `default.yml` e `base.yml`:
* `config`: I file contenuti nella directory config definiscono COME Espanso dovrebbe eseguire le sue espansioni. Il file `config/default.yml` definisce le opzioni che verranno applicate a tutte le applicazioni per impostazione predefinita, a meno che non sia presente una configurazione specifica per l'app corrente. Ad esempio, potresti voler abilitare gli snippet emoji per tutte le app nel file `config/default.yml`, ma disabilitarli quando usi Slack nel file `config/slack.yml`.
* `match`: definisce COSA dovrebbe fare Espanso. In altre parole, è qui che dovresti specificare tutti gli snippet e le azioni personalizzati (ovvero Matches). Il file principale è `match/base.yml`. Man mano che il numero di snippet aumenta, potresti voler dividere le corrispondenze su più file per semplificarne la gestione. Ad esempio, potresti creare il file `match/emails.yml` con gli snippet che usi mentre scrivi le email.

