## Git log - Trovare i commit perduti
#Coding #Git #PublishedPosts

Quante volte è successo di voler recuperare un commit ma non ricordarsi quando o chi lo ha effettuato? **Git log** viene in aiuto! Questo comando permette di ottenere una lista di commit filtrati secondo una determinata condizione.

La [documentazione ufficiale](https://git-scm.com/docs/git-log) è completa ma estremamente prolissa, di seguito una lista di comandi comodi per la vita di tutti i giorni.

## Commit con un determinato messaggio
```bash
git log --all --grep='foo'
```

Qualora il commit sia "dangling" quindi non connesso a nessun altro commit è possibile cercare anche con il `reflog` quindi utilizzare il comando:
```bash
git log -g --grep='foo'
```

Ricordo che l'argomento di grep accetta anche espressioni regolari.

## Commit con un determinata aggiunta o rimozione

Qualora voglia cercare tutti i commit dove la parola _foo_ è stata aggiunta o rimossa (per essere precisi dove il numero di occorrenze della parola _foo_ è cambiata.
```bash
git log -G "foo"
```

### Solo in un determinato file

Aggiungendo il nome del file alla fine posso filtrare solo per quello. Questo comando può essere utile qualora voglia ottenere tutti i commit che hanno modificato una determinata riga.
```bash
git log -G "foo" file.js
```

## Commit dello stesso autore
```bash
git log --author="foo"
```

## Estetica

I risultati di **git log** possono essere mostrati in vari modi diversi in base alle esigenze.

| Flag | Significato |
|--|--|
|`--oneline`|Mostra solo l'hash e il messaggio di commit|
|`--decorate`|Mostra eventuali tag e branch|
|`--stat`|Mostra il numero di righe aggiunte e rimosse per ogni commit|
|`--graph`|Mostra un grafico ASCII visualizzante la struttura dei branch|

## Per approfondire

Per approfondire consiglio il seguente libro, in italiano di Ferdinando Santacroce: [Git: Guida per imparare a gestire, distribuire e versionare codice](https://amzn.to/3IsPCLG).