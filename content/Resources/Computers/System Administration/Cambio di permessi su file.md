---
tags:
  - Linux
  - PublishedPosts
---


Questo articolo è una libera traduzione di numerosi post, in particolare segnalo:

* http://blog.servermania.com/a-complete-guide-to-chmod-recursive-force-and-more/
* http://www.tecmint.com/chattr-command-examples/
* http://www.cyberciti.biz/faq/how-to-use-chmod-and-chown-command/

## 1. Introduzione
In questo articolo fornirà una breve spiegazione di tutti i metodi comodi che vengono forniti da linux (o genericamente da sistemi unix-like) per la modifica dei permessi su file o cartelle.

Conoscere bene questi comandi permette di ridurre notevolmente i rischi di sicurezza per i nostri sistemi.

## 2. Chmod
Lo scopo del `chmod` (che sta per Change Mode) è **cambiare i permessi a file o directory**.

La sintassi è analoga ai seguenti pattern:

```shell
chmod [OPTION]… MODE[,MODE]… FILE…
chmod [OPTION]… OCTAL-MODE FILE…
chmod [OPTION]… –reference=RFILE FILE..
```

### 2.1 Opzioni
Si può cominciare con l'opzione che voglio implementare: le più famose sono:

- **-v** (verbose): mostra l'oggetto che sto modificando
- **-R** (recursive): include anche i file presenti nelle sottocartelle
- **-f** (force): ignora gli errori e continua ad applicare il comando anche in presenza di questi.

### 2.2 Modi
In linux, esistono 8 tipi di permessi diversi:

- **0**: nessuna
- **1**: solo esecuzione
- **2**: solo scrittura
- **3**: scrittura ed esecuzione
- **4**: solo lettura
- **5**: lettura ed esecuzione
- **6**: lettura e scrittura
- **7**: lettura, scrittura ed esecuzione

Con `chmod`, questi modalità sono definite in formato ottale, quindi con numeri che vanno da 0 a 7 (come indicato nell'elenco indicato sopra)
Il `chmod` prevende l'inserimento anche di un numero iniziale opzionale che serve per indicare flag speciali e successivamente di tre numeri che indicano rispettivamente **i permessi per il possessore del file, per il gruppo a cui appartiene l'utente e agli utenti che sono fuori a tale gruppo**.

Di seguito qualche esempio utile:

- `400`: Allows read exclusively by the file owner.
- `040`: Allows read exclusively by group members.
- `001`: Allows other users to execute

#### 2.2.1 Il chmod 777
Eseguire un `chmod 777` su un file o una directory può portare a gravi problemi di sicurezza sul server gestito, in quanto fornisce permessi globali a chiunque riesca ad accedere a tale server.

E' molto meglio, per esempio, un `chmod 775` in modo da evitare, eventualmente la scrittura all'utente generico o, ancor meglio, `chmod 774` che fornisce permessi in sola lettura.

#### 2.2.2 Il chmod 664
Questa configurazione di `chmod` è da evitare quando ho a che fare con delle cartelle in quanto ho bisogno **dei permessi di esecuzione per potervi accedere**.

### 2.3 Suggerimenti
Indico qui un elenco di cose da tenere a mente riguardo tale comando:

- Se devo listare cartelle o sottocartelle, necessito del permesso di lettura
- Per accedere ad una cartella ho bisogno dei permessi di esecuzione
- Posso dare permessi diversi a cartelle e file ricorsivamente tramite il comando file (che meriterà un approfondimento a parte in futuro): `find . -type f -exec chmod 640 {} \; for files and find . -type d -exec chmod 750 {} \;`

## 3. chown
Il comando `chown` (Change Ownership) viene utilizzato per **cambiare il possessore di un determinato file, che può essere un utente singolo o un gruppo**.

La sintassi è la seguente:

```shell
chown owner-user file
chown owner-user:owner-group file
chown owner-user:owner-group directory
chown options owner-user:owner-group file
```

Per esempio, assumiamo di avere il file *demo.txt* che, lanciando il comando `ls -l`, fornisce le seguenti informazioni:

```shell
-rw-r--r-- 1 root root 0 Aug 31 05:48 demo.txt
```

che indicano che l'utente proprietario del file è *root*, mentre il gruppo proprietario è allo stesso modo *root*.
Ora cambiamo il proprietario del file, da _root_ a _vivek_:

```shell
chown vivek demo.txt
```

Il file ora si presenta così:

```shell
-rw-r--r-- 1 vivek root 0 Aug 31 05:48 demo.txt
```

Se nel comando chown indichiamo il nome utente, seguito da un due punti e seguito dal nome di un gruppo, posso cambiare sia l'utente che il gruppo, come nel seguente esempio:

```shell
chown vivek:vivek-group demo.txt
```

che fornisce

```shell
-rw-r--r-- 1 vivek vivek-group 0 Aug 31 05:48 demo.txt
```

Per modificare solo il gruppo proprietario e non l'utente, è necessari lasciare vuoto lo spazio prima dei due punti (ma indicarli lo stesso), come nel seguente esempio:

```shell
chown :vivek-group demo.txt
```

Questo comando presenta una opzione per il cambiamento ricorsivo (`-R`), per esempio assumiamo di voler cambiare il proprietario della cartella `/foo` e di tutti i file ivi contenuti:

```shell
chown -R vivek /foo
```

## 4.chattr
`Chattr` (Change Attribute) è un comando che permette di assegnare certi attributi ad un file nei sistemi linux per **evitare che questi possano essere modificati o eliminati, anche se l'utente che cerca di apportare tali modifiche è l'utente root**.

Questo comando è particolarmente utile quando

- voglio **proteggere file sensibili** come passwd o shadow files
- voglio **evitare che un file sia modificato da script o servizi esterni di cui non conosco il comportamento**

Il comando ha la seguente sintassi:

```shell
chattr [operator] [flags] [filename]
```

### 4.1 Attributi e flag
Di seguito indico i principali attributi e flag che possono essere settati o meno usando il comando `chattr`:

- **i** (immutable): il file **non può essere modificato in alcun modo**, quindi non può essere rinominato, linkato, eseguito e scritto. Solo il superuser può rimuovere tale attributo
- **a**: il file può essere **scritto solo per appendere dati a quanto è già presente**, senza che questo possa invece essere toccato in alcun modo, ne eseguito o letto.

### 4.2 Aggiungere un attributo
Come esempio, creiamo la cartella `demo` e il file `important_file.conf`.

La cartella e il file hanno tutti i permessi di lettura e scrittura (`chmod 777`).

```shell
drwxr-xr-x. 2 root root 6 Aug 31 18:02 demo
-rwxrwxrwx. 1 root root 0 Aug 31 17:42 important_file.conf
```

Per settare un attributo utilizziamo il segno **+**, mentre per rimuoverlo utilizziamo il **-**, in questo caso **rendiamo il file immutabile**, prevenendone l'eliminazione anche dall'utente root, tramite il comando `+i`.

```shell
chattr +i demo/
chattr +i important_file.conf
```

Il bit di immutabilità `+i` può essere settato solo dal *superuser* o da un utente con privilegi `sudo`.

Una volta che l'attributo èstato settato, non è possibile in alcun modo **ne modificare ne eliminare il file o la cartella**

```shell
rm: cannot remove demo/: Operation not permitted
mv: cannot move demo/ to demo_alter: Operation not permitted
chmod: changing permissions of important_file.conf: Operation not permitted
```

### 4.3 Rimuovere un attributo
Per rimuovere un attributo basta impostare il comando con il segno **-** al posto del segno **+**.

```shell
chattr -i demo/ important_file.conf
```