---
tags:
  - Linux
  - PublishedPosts
---
Questo articolo è una libera traduzione di quanto è possibile trovare in [questa domanda](http://askubuntu.com/questions/187888/what-is-the-correct-way-to-completely-remove-an-application) di askubuntu.com

I comandi per rimuovere applicazioni o binari su ubuntu sono molteplici, in questo articolo ne tratterò i più utilizzati.

Il comando segue la seguente sintassi:

```shell
apt-get remove packagename
```

e permette di rimuovere i file binari, ma non i file di configurazione o altri tipologie di dati.
Inoltre lascerà i pacchetti che dipendono dal pacchetto `packagename` installati.

Faccio notare che questo comando può avere in ingresso un'espressione regolare, come per esempio:

```shell
sudo apt-get remove "^application.*"
```

che permette di rimuovere tutti i pacchetti il cui nome comincia con '`application`'.

Il comando ha due sintassi equivalenti:

```shell
apt-get purge packagename
```

o

```shell
apt-get remove --purge packagename
```

A differenza del comando indicato sopra, rimuove tutti i file che riguardano l'applicazione, ma non le dipendenze installate con essa.

Questo comando risulta particolarmente interessante quando voglio riinizializzare un'applicazione a causa di configurazioni sbagliate.

Questo comando rimuove tutti i pacchetti orfani, cioè pacchetti installati che sono stati installati come dipendenze di qualche altro pacchetto che ora non esiste più.

Questo comando viene usato quindi successivamente alla rimozione di un pacchetto per eliminarne anche le dipendenze a cui non sono più interessato.

Esiste anche la versione '`purge`' di questo comando, che permette di rimuoverne anche i corrispettivi file diconfigurazione

```shell
apt-get --purge autoremove
```

Per poter avere una rimozione completa di un pacchetto in un solo comando, quindi che rimuove il binario, le dipendenze e i file di configurazione, utilizzare il seguente:

```shell
sudo apt-get purge --auto-remove packagename
```
