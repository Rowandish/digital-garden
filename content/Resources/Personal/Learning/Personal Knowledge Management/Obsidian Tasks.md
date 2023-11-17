---
tags:
  - Productivity
---
Questo plugin permette di gestire i task sparsi per le varie note in Obsidian potendoli raggruppare con delle query dinamiche.
Questo plugin permette di effettuare delle query sulle checklist che hanno un determinato tag (chiamato *global filter*) o, se tale tag è vuoto, tutte le checklist nel vault.
La sintassi markdown per i task è elenco puntato con parentesi quadre separate da spazio:
`- [ ] #task take out the trash`.
Per creare un task con la modale basta evidenziare il testo del task e premere `ctrl + alt + t`.

I comandi obsidian task utilizzano la sintassi:
```
    ```tasks
    [comando]
    ```
```
Per il toggle del task posso usare `ctrl + enter` se sono in edit mode, in preview invece basta il click.

## Priorità
Ogni task può avere una priorità che viene identificata tramite una delle seguenti emoji:
* ⏫ alta priorità
* 🔼 Priorità media
* 🔽 Bassa priorità
Lo scopo è ovviamente permette di filtrare i task in base alle priorità.

## Date
Ho tre possibilità:
* **📅 Due**: task che hanno una data entro la quale devono essere completati. Per farlo è necessario aggiungere l'emoji 📅 seguita dalla data nel formato `YYYY-MM-DD`. Esempio: `- [ ] #task take out the trash 📅 2021-04-09`. La maggior parte dei task utilizzeranno al massimo la due date.;
* **⏳ Scheduled**: task che hanno delle date in cui hai pianificato che dovranno essere fatti.  Per farlo è necessario aggiungere l'emoji ⏳ seguita dalla data nel formato `YYYY-MM-DD`. Tipicamente possono avere delle date schedulate per un task che siano, ovviamente, inferiori alla due date. Esempio: `- [ ] #task take out the trash ⏳ 2021-04-09`.
* **🛫 Start**: Può capitare che è impossibile iniziare un task prima di una certa data o che non voglio vedere un task prima di una certa data. Per farlo è necessario aggiungere l'emoji 🛫 seguita dalla data nel formato `YYYY-MM-DD`.

## Task ripetuti
E' possibile creare dei task ricorrenti che si ripetono ogni tot giorni.
Per fare questo è necessario usare l'emoji 🔁 seguita dalla parola chiave `every` e da una keyword.
Per esempio `🔁 every weekday` fa ripetere il task tutti i giorni della settimana dal lunedì a venerdì.
Quando un task ricorrente viene marcato come completato **viene creato un task ulteriore con la nuova data sopra il task completato**.
Per esempio se ho il seguente task:
```
- [ ] #task take out the trash 🔁 every Sunday 📅 2021-04-25
```
Quando viene completato viene creato un nuovo task sopra nel seguente modo:
```
-   [ ] take out the trash 🔁 every Sunday 📅 2021-05-02
-   [x] take out the trash 🔁 every Sunday 📅 2021-04-25 ✅ 2021-04-24
```
Assumiamo che un task sia da lanciare ogni settimana ma io salto una settimana dal completarlo. Una volta fatto il task successivo quando viene creato? 
**Di default viene creato una settimana dopo l'originale, indipendentemente da quando il task è stato completato.**
Se invece vogliamo che il nuovo task sia creato una settimana dopo **la data di completamento** devo aggiungere la keyword `when done`.
In questo esempio il nuovo task è creato una settimana dopo il primo.
```
- [ ] #task sweep the floors 🔁 every week ⏳ 2021-02-13
- [x] sweep the floors 🔁 every week ⏳ 2021-02-06 ✅ 2022-02-13
```
In questo esempio invece una settimana dopo la data di completamento.
```
- [ ] #task sweep the floors 🔁 every week when done ⏳ 2022-02-20
- [x] sweep the floors 🔁 every week when done ⏳ 2021-02-06 ✅ 2022-02-13
```
Esempi:
-   `🔁 every 3 days`
-   `🔁 every 10 days when done`
-   `🔁 every weekday` (tutti i giorni da lunedì a venerdì)
-   `🔁 every week on Sunday`
-   `🔁 every 2 weeks`
-   `🔁 every 3 weeks on Friday`
-   `🔁 every 2 months`
-   `🔁 every month on the 1st`
-   `🔁 every month on the last`
-   `🔁 every 6 months on the 2nd Wednesday`
-   `🔁 every January on the 15th`
-   `🔁 every February on the last`
-   `🔁 every April and December on the 1st and 24th` ( ogni primo aprile e 24 dicembre)
-   `🔁 every year`
## Query
Le query sono formate da *n* righe con i filtri in AND (l'AND è sottointeso).
Per aggiungere altri operatori come `NOT`, `AND`, `OR`, `AND NOT`, `OR NOT` li devi aggiungere sulla stessa riga raggruppati tra parentesi.
````
```tasks
not done
(due after yesterday) AND (due before in two weeks)
(tags include #inbox) OR (path includes Inbox) OR (heading includes Inbox)
```
````
### Filtraggio per date
Per filtrare le date posso prendere questi esempi:
-   `2021-05-25`
-   `yesterday`
-   `today`
-   `tomorrow`
-   `next monday`
-   `last friday`
-   `14 days ago`
-   `in two weeks`
#### Done date
-   `done`
-   `not done`
-   `no done date`
-   `has done date`
-   `done (before|after|on) <date>`
#### Due date
-   `no due date`
-   `has due date`
-   `due (before|after|on) <date>`
#### Scheduled date
-   `no scheduled date`
-   `has scheduled date`
-   `scheduled (before|after|on) <date>`
#### Start date
-   `no start date`
-   `has start date`
-   `starts (before|after|on) <date>`
#### Happens (Due or Scheduled or Start)
* `happens before tomorrow`: tutti i task che sono schedulati, partono o devono essere fatti entro domani.

### Description
Permette di matchare la stringa del task.
* `description (includes|does not include) <string>`
* `description (regex matches|regex does not match) /<JavaScript-style Regex>/`
### Priorità
-   `priority is (above|below)? (low|none|medium|high)`
### Status
-   `done`
-   `not done`
### Tags
* `tags (include|do not include) <tag>`
* `tags (regex matches|regex does not match) /<JavaScript-style Regex>/`
### Nome file
* `filename (includes|does not include) <filename>`

## Ordinamento
L'ordinamento di default viene effettuato secondo un criterio di "urgenza" [calcolato dal plugin](https://obsidian-tasks-group.github.io/obsidian-tasks/advanced/urgency/).
Per modificare tale ordinamento è possibile utilizzare la keyword `sort by`.
Esempi:
* `status`
* `priority`
* `due`
* `path` 

## Esempio: Task da fare nei prossimi 7 giorni
Voglio tutti i task che dovranno essere eseguiti entro i prossimi 7 giorni (può essere utile in un template di un weekly plan).
P.s. per testare una query conviene creare delle "suite di test" con dei task fittizzi per capire costa sto matchando o no.
Quindi voglio i task con due date (quindi keyword  `due`) e prima di una certa data, quindi `before in` .
Conseguentemente il filtro corretto è: 
````
```tasks
not done
due before in 7 days
```
````
## Notifiche
E' possibile far arrivare le notifiche quando bisogna fare un task utilizzando [obsidian-reminder](https://github.com/uphy/obsidian-reminder).
Una volta installato controllare che ci sia abilitata l'opzione "enabled the tasks plugin format".
Il plugin si basa sulla reminder date che deve essere messa sempre immediatamente prima della due date.
```
- [ ] #task #task task name ⏰ YYYY-MM-DD HH:mm 📅 YYYY-MM-DD ⏫ 🔁 every week 🛫 YYYY-MM-DD ⏳ YYYY-MM-DD
```