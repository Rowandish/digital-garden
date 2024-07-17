---
tags:
  - PublishedPosts
---
Questa nota prende a piene mani dal corso ["From Zero to Hero: Docker for Developers" di Dan Clarke su Dometrain](https://dometrain.com/course/from-zero-to-hero-docker/).
## Introduzione

Nel modo tradizionale di sviluppo le applicazioni giravano su un determinato server utilizzando tutte le risorse che questo metteva a disposizione. Lanciando _n_ applicazioni sullo stesso server c'è il rischio che una utilizzi le risorse togliendole dalle altre applicazioni.

Per risolvere questo problema sono state inventate le Macchine Virtuali, che permettono di avere delle astrazioni dell'hardware fisico del server in quanto ho _n_ VM sullo stesso server ognuna con il suo sistema operativo e hardware assegnato.

![[Pasted image 20240613143546.png|450]]

Risolvo quindi il problema del fatto che una applicazione possa impattare le altre sullo stesso server.

I container portano l'astrazione ad un livello ancora maggiore: **==oltre ad astrarre l'hardware sottostante astraggono anche il sistema operativo==**. In questo modo i container offrono lo stesso livello di isolamento, scalabilità e facilità di gestione di una VM ma senza l'overhead di portarsi dietro un sistema operativo: in questo modo risultano leggere e molto più portabili di una VM.

![[Pasted image 20240613143640.png|450]]
Essendo molto più leggeri di una VM posso averne moltissimi sullo stesso SO, posso gestirli, aggiungerli ed eliminarli in modo estremamente semplice.
Un'altra differenza con le VM è che nelle VM si opera direttamente sul sistema operativo virtualizzato, mentre difficilmente nei container andrò ad operare nel loro SO, ma agirò sui container direttamente dell'host operating system.
Dato che il container non possiede copie del sistema operativo (a differenza di una VM) deve girare sul sistema operativo della piattaforma dove risiede: su questo ultimo deve invece essere installato un **_runtime engine_ che è l'applicazione che permette di far comunicare il container con questo**.

**Il _runtime engine_ più famoso è [Docker](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi8-Myo6tL2AhXBvKQKHQA_B18QFnoECBEQAQ&url=https%3A%2F%2Fwww.docker.com%2F&usg=AOvVaw3p9e1qPvdfjCrUwPYAhUlS)**, sistema open source del 2013 utilizzato in tutto il mondo.

### Containerizzazione

==**La cointanerizzazione (_containerization_ in inglese) è il processo per cui viene "impacchettato" del codice e soprattutto delle sue dipendenze in modo che possa funzionare su ogni infrastruttura.**==

Il codice viene sviluppato su uno specifico ambiente di sviluppo (distro, dipendenze installate…); quando questo viene spostato in un nuovo ambiente è facile avere errori o bug in quanto l'ambiente non è lo stesso e i pacchetti possono o non esistere o avere comportamenti diversi.

La _containerization_ elimina il problema unendo il codice con un relativo file che ne specifica eventuali file di configurazione, librerie e dipendenze.

==In questo modo il software è all'interno di un "container" che lo rende indipendente dal sistema operativo o, in generale, dall'ambiente in cui viene lanciato e conseguentemente portable e bug-free==.

La _containerization_ permette di quindi di scrivere una applicazione una sola volta e poi poterla farla girare ovunque, con tutti i vantaggi del caso.

### Componenti di un container
==Tipicamente ogni container contiene una sola app==, a differenza della virtual machine, creando così un pacchetto self-contained che contiene tutto quello che serve a tale app per girare.
Tipicamente un container contiene:
* **Il processo principale**: l'app che sto sviluppando oppure un'app di terze parti come SQL Server, RabbitMQ e così via;
* **Application Runtime**: il motore che permette alla mia applicazione per girare, per esempio .NET, Node, JVM...;
* **Dipendenze**: I pacchetti che utilizza l'app come DLL...;
* **File di configurazione**;
* **Variabili d'ambiente**.



## Esempi di utilizzo
Un'esempio di utilizzo è la gestione di vari DBMS, uno per ogni cliente.
Senza Docker dovrei avere un'istanza unica del DBMS, esempio SQL Server, e avere al suo interno tutti i database per tutti i clienti, quando magari ognuno ha esigenze diverse.
Inoltre dovrei "sporcare" il mio PC installando SQL Server quando non è necessario.
Questo problema si risolve con docker: io ho un'immagine dedicata a SQL Server e *n* container uno per ogni cliente. In questo modo ogni container è pulito e non ha roba di altri.

## Componenti
Un progetto Docker è formato da:
* **Dockerfile**: file che descrive le dipendenze
* **Image**: snapshot di una installazione, è effettivamente l'installer che contiene tutti i file
* **Container**: parte dall'immagine ma possono averne tanti a partire dalla stessa image, sono le installazioni. Ogni container è isolato e non sa dell'esistenza delle altre. 

### Image

![[Pasted image 20240613145035.png]]

La _container image_ è un file statico presente su disco che contiene tutto ciò che è necessario all'applicazione per funzionare quindi tutte le sue dipendenze, file di configurazione, script, binari e così via.
Da una Image posso creare *n* diversi container, che saranno tutti identici in quanto "istanze" della stessa "Image".
Per esempio se voglio dare ad un mio collega il container che ho appena creato, gli fornirò il file Image e sarà lui a costruirsi la sua istanza, quindi il suo container.

![[Pasted image 20240613145254.png]]
#### Container Registry

Nell'immagine sopra si vede Bob che ha creato un'Image della sua webApp e vuole renderla pubblica: la pusha in un *container registry* (il più famoso è docker hub) e chi vuole la può pullare e crearsi la sua istanza di container esattamente come quella di Bob.
Ci sono vari container registry:
* Docker Hub (nel piano free una sola immagine privata disponibile)
* Azure Container Registry
* Amazon AWS
* Artifact registry di Google Cloud
* Github
* Harbor
Un utilizzo potrebbe essere che colui che pusha l'immagine è un servizio di Continuous Integration mentre colui che pulla un servizio di orchestration di container come Kubertenes.

![[Pasted image 20240619172717.png]]
##### Push
Per mandare la propria immagine su Container Registry, una volta creata la "repository" sull'interfaccia bisogna loggarsi con `docker login`; creare l'immagine con `docker build -f PathDockerFile -t usernameContainerRegistry/NomeRepository .` e infine fare `docker push usernameContainerRegistry/NomeRepository`.

#### Tags

Ogni immagine può avere differenti "versioni" di cui l'ultima si chiama, per convenzione `latest`.
![[Pasted image 20240617163147.png]]
In produzione conviene non usare `latest` ma esplicitare il numero di versione in quanto questi sono immutabili e puntano sempre allo stesso id, `latest` invece cambia con l'uscita di una nuova versione.

#### Layers

![[Pasted image 20240618143457.png]]
Ogni immagine è formata da vari strati, tipicamente si parte da un'immagine di base (esempio `Debian`) e poi si costruiscono altre immagini aggiungendo pacchetti all'immagine in questione.
Ogni layer è messo in cache per cui se scarico due immagini diverse che usano come layer la stessa immagine di `Debian` questa ultima non verrà scaricata nuovamente.


## Docker CLI
Docker fornisce una Command Line Interface con tutti i comandi comodi che possono servire, tutti iniziano con `docker`; vediamone alcuni:
* `docker run`: scarica un'image con `docker pull` e la lancia immediatamente. L'immagine viene messa in una cache in modo che non dovrà essere riscaricata la prossima volta. Il comando `-e` permette di aggiungere una variabile d'ambirente. Se aggiunto il comando `-d` o `--detached`  il container viene lanciato senza rimanere sul terminale ma rimanendo in background in modalità detached;
* `docker pull`: scarica un'image e la aggiorna all'ultima versione se già presente;
* `docker ps`: fa una lista dei container che stanno girando in questo momento, indicandone anche il `container id` che è l'identificativo univoco. Aggiungendo l'opzione `-a` visualizza anche i container che esistono ma non sono attivi.
* `docker stop [CONTAINER ID]`: ferma il container indicato
* `docker rm [CONTAINER ID]`: rimuove il container dalla lista dei container gestiti da docker. Se con l'opzione `-f` rimuove anche un container che sta andando.
* `docker logs [CONTAINER ID]`: mostra i log di un container: comodo se questo è stato lanciato in modalità `detached`. Con l'opzione `-f` la console rimarrà a seguire il log.
* `docker attach [CONTAINER ID]`: si riattacca ad un container in modalità `detached` come se fosse stato lanciato senza l'opzione `-d`.
* `docker images`: lista tutte le immagini scaricate;
* `docker exec -it [CONTAINER ID] [COMANDO]`: permette di lanciare un comando come se fossi nel terminale del container. Se `[COMANDO]`è `sh` o `bash` lancia direttamente il terminale interno del container. Se il container è linux posso lanciare anche comandi di aggiornamento pacchetti come `apt-get` per installare quello che voglio, per esempio editor di testo per modificare file. Ovviamente tutte le modifiche che avvengono sono in quello specifico container e non nell'image da cui è partito.
* `docker build -t nome:tag .`: crea l'immagine a partire da un Dockerfile presente nella cartella corrente (notare il punto `.`). Se `tag` non è specificato usa la cartella corrente;
* `docker tag [SOURCE IMAGE ID] [IMAGE NAME]:[TAG NAME]`: effettua il tag dell'immagine con nome `[IMAGE NAME]` e con id `[SOURCE IMAGE ID]` con il tag `[TAG NAME]`.
* `docker rmi [IMAGE NAME]:[TAG NAME]`: elimina il tag `[TAG NAME]` dell'immagine `[IMAGE NAME]`. Se usato con `docker rmi [IMAGE NAME];` elimina l'immagine e tutti i tag
* `docker compose`:
	* `up`: lancia tutti i container definiti nel file `docker-compose.yaml`
	* `-d`: lancia in modalità detached
	* `ps`: mostra tutti i container lanciati nel docker compose
	* `logs`: mostra i log
	* `down`: elimina i container (a differenza di `CTRL+C` che li ferma e basta)
* 

## Docker Desktop GUI
Docker fornisce anche una GUI come alternativa o supporto alla CLI.

### Container

Nella sezione `Container` vedo i container che stanno girando, simile alla chiamata a `docker ps`.
Cliccando su un container posso vedere numerose altre info e anche entrare in un terminale all'interno di tale container.

### Images

Nella sezione Images posso vedere tutte le immagini che ho scaricato sul mio PC e che posso lanciare.

### Ricerca
Posso cercare un'immagine e scaricarla con il pull o lanciarla direttamente.

## Port mapping
Questa operazione permette di rendere pubblica la porta del container all'host ospitante. Per esempio lancio l'immagine di `nginx` e vado su `localhost` nel browser non vedo niente in quanto la porta di `nginx` non è esposta.
Se lancio il comando `docker run nginx -p 8080:80` posso definire, a sinistra del `:` la porta da cui accederemo da fuori dal container mentre a destra la porta a cui accederemo all'interno del container.
Per esempio con l'istruzione sopra se vado su `http://localhost:8080/` accedo alla porta 80 dell'immagine di `nginx` in Docker.
Posso anche specificarlo più volte per fare il mapping di n porte diverse, per esempio posso scrivere `docker run nginx -p 8080:80 -p 1234:52`.

## Dockerfile
Il Dockerfile è un file contenente una lista di istruzioni da eseguire per poter costruire una image.
La prima istruzione di un Dockerfile è quasi sempre l'istruzione `FROM` che indica la `Base image` da cui partire.
Per esempio l'istruzione seguente indica che devo partire dall'immagine contrenente la .NET 7 SDK.
```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS base
```
Altre alternative classiche sono partire con `Ubuntu` o `Debian`.
Questa istruzione crea una container virtuale temporaneo dove gireranno le istruzioni seguenti.
Le istruzioni seguenti sono custom,, vediamone alcune:
* `WORKDIR`: crea una directory se non esiste e sposta il context al suo interno;
* `COPY ["FROM_PATH", "TO_PATH"]`: copia il file presente in `FROM_PATH` all'interno del container in `TO_PATH`.  `COPY . .` copia tutti i file dal path corrente a dentro il container;
* `RUN command`: lancia il comando in questione all'interno della shell del container;
* `EXPOSE PORT`: aggiunge alla documentazione le porte da usare nell'immagine ma non le espone direttamente;
* `ENTRYPOINT ["eseguibile", "arg1", "arg2"]`: comando che viene sempre lanciato quando un container viene avviato;

### Dockerfile multistage
Nei Dockerfile multistage ho la creazione di immagini Docker più efficienti e leggere in quanto sono separate le fasi di costruzione del software da quelle di esecuzione.
Di seguito, descriverò un esempio di Dockerfile multistage utilizzando il .NET SDK per eseguire `dotnet restore` e `dotnet publish`, e poi una versione più leggera basata su ASP.NET per l'entry point dell'applicazione.
```dockerfile
# Fase 1: Costruzione
# Utilizziamo l'immagine del .NET SDK come base per questa fase. Il tag `AS build` serve a dare un nome a questa fase, che useremo in seguito.
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file di progetto e ripristina le dipendenze
COPY *.csproj ./
RUN dotnet restore

# Compila l'applicazione in modalità Release e pubblica l'output nella directory /out.
COPY . ./
RUN dotnet publish -c Release -o /out

# Fase 2: Runtime
# Utilizziamo l'immagine più leggera di ASP.NET per eseguire l'applicazione.
FROM mcr.microsoft.com/dotnet/aspnet:6.0

# Imposta la directory di lavoro
WORKDIR /app

# Copia l'output dalla fase di costruzione
COPY --from=build /out .

# Espone la porta 80 per permettere al container di accettare connessioni HTTP.
EXPOSE 80

# Definisce il punto di ingresso dell'applicazione, specificando il comando `dotnet` e il nome del file DLL dell'applicazione.
# Quando lancio il container è come se lanciassi "dotnet "NomeTuaApplicazione.dll"
ENTRYPOINT ["dotnet", "NomeTuaApplicazione.dll"]
```


### Ottimizzare il `dotnet restore`
Se sviluppiamo un'applicazione in dotnet possiamo fare un trucco per evitare di scaricare tutti i pacchetti tutte le volte che lanciamo un'immagine docker: l'idea è che prima di copiare tutti i file facciamo un `dotnet restore` basandosi solo sul file `.csproj`; in questo modo lui scaricherà i pacchetti e li metterà nella sua cache e li riscaricherà solo se il file `.csproj` cambia.
```dockerfile
# Copio solo il file csproj che è l'unica cosa che serve per dotnet restore
COPY ["DockerCourseApi/DockerCourseApi.csproj", "DockerCourseApi/"]
# Lancio il comando effettivo
RUN dotnet restore "DockerCourseApi/DockerCourseApi.csproj"
# Copio tutti gli altri file
COPY . .
```

### Esempi

#### Blazor
In questo esempio ho un `Dockerfile` che fa il `publish` di una app blazor e la lancia su un server `nginx` in modo che sia accedibile dal browser.
Per farlo utilizzo un Dockerfile multistage in cui nella prima fase utilizzerà il .NET SDK per eseguire il `dotnet publish`, e la seconda fase utilizzerà un'immagine di Nginx per servire l'applicazione.

```dockerfile
# Fase 1: Costruzione dell'applicazione Blazor
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file di progetto e ripristina le dipendenze
COPY *.csproj ./
RUN dotnet restore

# Copia tutto il codice sorgente e compila l'applicazione
COPY . ./
RUN dotnet publish -c Release -o /out

# Fase 2: Creazione dell'immagine Nginx
FROM nginx:alpine

# Copia i file pubblicati dalla fase di costruzione alla directory di Nginx
COPY --from=build /out/wwwroot /usr/share/nginx/html

# Espone la porta 80
EXPOSE 80

# Definisce il comando di avvio di Nginx
CMD ["nginx", "-g", "daemon off;"]
```

Per costruire e eseguire il container, utilizza i seguenti comandi:
* **Costruzione dell'Immagine Docker**:`docker build -t my-blazor-app .`
* **Esecuzione del Container**:`docker run -d -p 80:80 my-blazor-app`
## Docker compose
Il file `docker-compose.yaml` permette di avere in un unico punto la definizione di tutti i container che servono per fare girare una determinata applicazione e permettere, tramite un unico comando, di lanciare tutti i container in questione.
Dato che questo è un normale file di testo può essere version controllabile facilmente e si ha la certezza che tutti i componenti del team di sviluppo lancino lo stesso ambiente.

### Build delle immagini
Nel file `docker-compose.yml` posso anche fare il build delle immagini prima di lanciarle, questo viene fatto tramite il comando `build` indicando come `context` il path dove si trova il Dockerfile da utilizzare per costruire l'immagine in questione.


Supponiamo che tu abbia una struttura di progetto come segue:

```
my_project/
│
├── app/
│   ├── Dockerfile
│   ├── ... (altri file di applicazione)
│
├── db/
│   ├── Dockerfile
│   ├── ... (altri file di database)
│
└── docker-compose.yml
```
Posso configurare il file `docker-compose.yml` per costruire queste immagini:

**docker-compose.yml**
```yaml
version: '3.8'
# Definisce i servizi che verranno avviati. In questo esempio, ci sono due servizi: `app` e `db`.
services:
  app:
    build:
	  # La directory in cui si trova il `Dockerfile`.
      context: ./app
      # Il nome del file Dockerfile da utilizzare.
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    depends_on:
      - db

  db:
    build:
      context: ./db
      dockerfile: Dockerfile
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: mydatabase
      MYSQL_USER: user
      MYSQL_PASSWORD: password
```

Per avviare i servizi e costruire le immagini utilizza il comando `docker-compose up --build`.


### DNS Entries in Docker Compose

Quando si utilizza Docker Compose per gestire e orchestrare più container, ==Docker crea automaticamente una rete bridge per tutti i servizi definiti nel file `docker-compose.yml`. All'interno di questa rete, ogni servizio può essere raggiunto utilizzando il nome del servizio come hostname, grazie al DNS integrato.==

Questo significa che, invece di utilizzare `localhost` o indirizzi IP statici, puoi semplicemente usare il nome del servizio definito nel file `docker-compose.yml` per accedere a un altro container.

#### Esempio: API e Database SQL Server

Immaginiamo di avere una configurazione con due servizi:
1. Un'API che deve connettersi a un database SQL Server.
2. Un'istanza di SQL Server che funge da database.

##### File `docker-compose.yml`

```yaml
version: '3.8'

services:
  api:
    image: myapi:latest
    environment:
      - ASPNETCORE_ENVIRONMENT=Production
      - ConnectionStrings__DefaultConnection=Server=db;Database=mydatabase;User Id=sa;Password=Your_password123;
    ports:
      - "5000:80"
    # Questa direttiva indica che il servizio `api` deve essere avviato dopo il servizio `db`. Questo garantisce che il database sia in esecuzione prima che l'API tenti di connettersi ad esso.
    depends_on:
      - db

  db:
    image: mcr.microsoft.com/mssql/server:2019-latest
    environment:
      SA_PASSWORD: "Your_password123"
      ACCEPT_EULA: "Y"
    ports:
      - "1433:1433"
```
La stringa di connessione è configurata per connettersi al server `db`, che è il nome del servizio SQL Server definito nel file `docker-compose.yml`: invece di utilizzare `localhost` o un indirizzo IP specifico, l'API può utilizzare `db` come hostname per connettersi al database SQL Server. Questo è possibile grazie alla rete bridge creata automaticamente da Docker Compose, che consente ai container di comunicare tra loro utilizzando i nomi dei servizi come hostname.

### Database seeding
Posso sfruttare `docker-compose` non solo per far partire un'immagine del DBMS che mi serve ma anche per fare il seed.
Il procedimento è molto semplice:
* Nel file `docker-compose.yaml` aggiungere uno step (chiamato per esempio `database-seed` ) che ha `depends-on` il container del DBMS (così sono sicuro che viene eseguito dopo) che lancia il relativo `Dockerfile`
```yaml
services:

  database:
    image: mcr.microsoft.com/mssql/server:2022-latest
    container_name: database
    environment:
      - ACCEPT_EULA=true
      - MSSQL_SA_PASSWORD=Dometrain#123
    ports:
      - 1433:1433

  database-seed:
    depends_on: [ database ]
    build:
      context: Database/
      dockerfile: Dockerfile
    container_name: database-seed
```
* Il Dockerfile del seed avrà una struttura simile a questa:
```dockerfile
# Prendo la stessa immagine del DBMS che mi serve
FROM mcr.microsoft.com/mssql/server:2022-latest

# Copio lo script in shell che utilizza il comando "sqlcmd" da CLI di SQL Server per lanciare il file .sql
COPY ./wait-and-run.sh /wait-and-run.sh
# Copio il file .sql da lanciare
COPY ./CreateDatabaseAndSeed.sql /CreateDatabaseAndSeed.sql
# Lancio lo script
CMD /wait-and-run.sh
```
* Lo script aspetterà che il DBMS sia up e, una volta fatto, lancerà il contenuto del file `CreateDatabaseAndSeed.sql` sul DBMS. Notare che lo script è scritto in shell con comandi unix style in quanto questo ultimo è lanciato all'interno di un container linux. Lo script potrebbe avere codice analogo a:
```sh
#!/bin/bash

# Wait for SQL Server to be ready
echo "Waiting for SQL Server to be ready..."
for i in {1..50};
do
    /opt/mssql-tools/bin/sqlcmd -S database -U sa -P Pwd -Q "SELECT 1" > /dev/null 2>&1
    if [ $? -eq 0 ]
    then
        echo "SQL Server is ready."
        break
    else
        echo "Not ready yet..."
        sleep 1
    fi
done

# Run the SQL script
/opt/mssql-tools/bin/sqlcmd -S database -U sa -P Pwd -d master -i /CreateDatabaseAndSeed.sql
```

## Persistent Storage
Spesso c'è l'esigenza che i container possano accedere a dei file che siano persistenti alla creazione dello stesso, quindi che siano fuori dal container e che sopravvivano alla sua distruzione.
Inoltre questi file potrebbero essere condivisi tra più container contemporaneamente.
Esistono tre tipologie di storage persistente: `bind mount`, `volums` e `tmpfs`.

![[Pasted image 20240620122201.png]]
### Volume
Un `volume` è una directory che è all'interno di Docker ma separato dai container stessi. Questo spazio quindi sopravvive ai container e uno o più container possono utilizzarlo.
Per gestire i volumi si utilizza `docker volume`.
#### Comandi comodi
* `docker volume create XXX`: crea un volume chiamato XXX
* `docker volume ls`: visualizza tutti i `volume` che sono presenti su Docker
* `docker volume inspect VOLUME_NAME`: ottiene informazioni su un singolo volume
* `docker volume rm VOLUME_NAME`: rimuove il volume `VOLUME_NAME`

#### Utilizzare un volume
Una volta che un `volume` è stato creato posso aggiungere l'opzione `-v volume_name:inner_folder` per far sì che tutto ciò che dovrebbe andare in `inner_folder` all'interno del container vada invece nella cartella riferita a `volume_name`.
Questo è un esempio di utilizzo con SqlServer dove i dati del database, che tipicamente sono salvati in `/var/opt/mssql` vengono invece messi nel volume chiamato `sqldb-data` in modo che siano persistenti alla chiusura del container.
```powershell
# Crea un container di Sql Server.
docker run `
  --name sqlserver-withvol `
  -e "ACCEPT_EULA=Y" `
  -e "MSSQL_SA_PASSWORD=Dometrain#123" `
  # Dato che ho -p 1433:1433 significa che se faccio localhost:1433 che è la porta di default di Sql Server, accederò ai dati all'interno del container
  -p 1433:1433 `
  # detached
  -d `
  # In SqlServer i dati del db stanno in "/var/opt/mssql". Scrivendo così creo un link al volume chiamato "sqldb-data"
  # per cui i dati non verranno scritti/letti veramente in /var/opt/mssql ma nel volume "sqldb-data".
  # P.s. facendo docker volume inspect sqldb-data posso andare a vedere la cartella effettiva dove tali dati stanno
  # In questo modo quando spegnerò questo container la cartella contenente il db rimarrà in Docker, riaccendendolo non dovrò più fare il seed in quanto
  # lo storage è sempre quello
  -v sqldb-data:/var/opt/mssql `
  mcr.microsoft.com/mssql/server:2022-latest
```

### Bind Mount
I file in questa cartella sono sul file system del sistema operativo ospitante Docker.

### Tmpfs
Usando un temporary File System i file sono in RAM nel sistema operativo ospitante. Ho un vantaggio di prestazioni ma tali file vengono persi alla chiusura del container che li sta utilizzando.
