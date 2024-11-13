---
tags:
  - PublishedPosts
---
Questa nota prende a piene mani dal corso ["From Zero to Hero: Docker for Developers" di Dan Clarke su Dometrain](https://dometrain.com/course/from-zero-to-hero-docker/).

## Introduzione

Docker è una piattaforma progettata per semplificare la creazione, la distribuzione e l'esecuzione di applicazioni tramite container.
==I container consentono a uno sviluppatore di confezionare un'applicazione con tutte le parti di cui ha bisogno, come librerie e altre dipendenze, e di spedire il tutto come un unico pacchetto==.
Questo processo si chiama containerization e permette a tale codice di funzionare su ogni infrastruttura.
I container Docker sono leggeri ed efficienti. Condividono il kernel del sistema host isolando i processi dell'applicazione, riducendo i costi generali rispetto alle tradizionali macchine virtuali. Questa efficienza si traduce in tempi di avvio più rapidi, migliore utilizzo delle risorse e la possibilità di eseguire molti più container sullo stesso hardware.
Un'altra caratteristica fondamentale di Docker è la sua integrazione con strumenti di orchestrazione dei container come Kubernetes. Questi strumenti forniscono una gestione automatizzata delle applicazioni in container, gestendo attività come il ridimensionamento, il load balancinig e l'auto-riparazione. Questa capacità di orchestrazione è fondamentale per le moderne architetture di microservices, in cui le applicazioni sono composte da più servizi interconnessi che devono essere gestiti in modo coeso.

### Container vs Virtual Machines

Nel modo tradizionale di sviluppo le applicazioni giravano su un determinato server utilizzando tutte le risorse che questo metteva a disposizione. Lanciando _n_ applicazioni sullo stesso server c'è il rischio che una utilizzi le risorse togliendole dalle altre applicazioni.

Per risolvere questo problema sono state inventate le Macchine Virtuali, che permettono di avere delle astrazioni dell'hardware fisico del server in quanto ho _n_ VM sullo stesso server ognuna con il suo sistema operativo e hardware assegnato.

![[Pasted image 20240613143546.png|450]]

Risolvo quindi il problema del fatto che una applicazione possa impattare le altre sullo stesso server.

I container portano l'astrazione ad un livello ancora maggiore: **==oltre ad astrarre l'hardware sottostante astraggono anche il sistema operativo==**. In questo modo i container offrono lo stesso livello di isolamento, scalabilità e facilità di gestione di una VM ma senza l'overhead di portarsi dietro un sistema operativo: in questo modo risultano leggere e molto più portabili di una VM.

![[Pasted image 20240613143640.png|450]]
Essendo molto più leggeri di una VM posso averne moltissimi sullo stesso SO, posso gestirli, aggiungerli ed eliminarli in modo estremamente semplice.
Un'altra differenza con le VM è che nelle VM si opera direttamente sul sistema operativo virtualizzato, mentre difficilmente nei container andrò ad operare nel loro SO, ma agirò sui container direttamente dell'host operating system.
Dato che il container non possiede copie del sistema operativo (a differenza di una VM) deve girare sul sistema operativo della piattaforma dove risiede: su questo ultimo deve invece essere installato un **_runtime engine_ che è l'applicazione che permette di far comunicare il container con questo**.

### Vantaggi
* **Consistency**: Docker assicura che la tua applicazione funzioni senza problemi in diversi ambienti impacchettandola in container. Questo risolve il problema "funziona sulla mia macchina".
* **Isolamento**: i container ti consentono di eseguire più applicazioni sullo stesso host senza interferire tra loro.
* **Microservizi**: Docker è ideale per creare architetture di microservizi, consentendo a ogni servizio di essere distribuito e scalato in modo indipendente.
* **Portabilità**: i container possono essere facilmente spostati dalla tua macchina di sviluppo locale ai server di produzione, tra provider cloud e altro ancora.

### Componenti di un container
==Tipicamente ogni container contiene una sola app==, a differenza della virtual machine, creando così un pacchetto self-contained che contiene tutto quello che serve a tale app per girare.
Tipicamente un container contiene:
* **Il processo principale**: l'app che sto sviluppando oppure un'app di terze parti come SQL Server, RabbitMQ e così via;
* **Application Runtime**: il motore che permette alla mia applicazione per girare, per esempio .NET, Node, JVM...;
* **Dipendenze**: I pacchetti che utilizza l'app come DLL...;
* **File di configurazione**;
* **Variabili d'ambiente**.
### Esempio
Un'esempio di utilizzo è la gestione di vari DBMS, uno per ogni cliente.
Senza Docker dovrei avere un'istanza unica del DBMS, esempio SQL Server, e avere al suo interno tutti i database per tutti i clienti, quando magari ognuno ha esigenze diverse.
Inoltre dovrei "sporcare" il mio PC installando SQL Server quando non è necessario.
Questo problema si risolve con docker: io ho un'image dedicata a SQL Server e *n* container uno per ogni cliente. In questo modo ogni container è pulito e non ha roba di altri.

## Componenti
Un progetto Docker è formato da:
* **Dockerfile**: file che descrive le dipendenze
* **Image**: snapshot di una installazione, è effettivamente l'installer che contiene tutti i file
* **Container**: Istanza dell'image di cui sopra: da un'image posso creare *n* container isolato che non sa dell'esistenza degli altri.
### Dockerfile

Un Dockerfile è un documento di testo contenente tutti i comandi che un utente può chiamare sulla riga di comando per assemblare un'image.
Scrivere un Dockerfile è come definire le proprietà e i metodi di una classe. Include l'image di base (la classe padre), pacchetti aggiuntivi da installare (dipendenze), variabili di ambiente (proprietà della classe) e il comando da eseguire all'avvio del contenitore (il metodo principale).

Per costruire e eseguire il container, utilizza i seguenti comandi:
* **Costruzione dell'image Docker**:`docker build -t [APP NAME] -f [DOCKERFILE PATH] .`
* **Esecuzione del Container**:`docker run -d -p 80:80 [APP NAME]`

#### Elementi chiave

* **Image di base (`FROM`)**: specifica il punto di partenza, la `Base image` da cui partire. Simile all'estensione di una classe in OOP.
* **Comandi (`RUN`)**: esegue comandi shell, simili all'impostazione di metodi nella classe che preparano l'oggetto.
* **Copia di file (`COPY`, `ADD`)**: importa file o directory esterni, simile all'inclusione di librerie o risorse esterne. `COPY . .` copia tutti i file dal path corrente a dentro il container;
* **Variabili di ambiente (`ENV`)**: imposta variabili che possono essere utilizzate dall'applicazione in esecuzione, come l'impostazione di valori predefiniti per le proprietà della classe.
* **Comando di esecuzione (`CMD` o `ENTRYPOINT` )**: definisce quale comando eseguire all'avvio del contenitore, simile al metodo principale nella classe che viene eseguito.

#### `ENTRYPOINT` vs `CMD`

In Docker, `ENTRYPOINT` e `CMD` sono due istruzioni che definiscono i comandi da eseguire all'interno di un container.

##### ENTRYPOINT
Specifica un comando fisso che viene sempre eseguito quando il container viene avviato. 
Gli eventuali parametri aggiuntivi **non possono essere sovrascritti** a meno di utilizzare il parametro `-entrypoint` sovrascrivendo completamente l'entrypoint.
  ```dockerfile
  FROM ubuntu
  ENTRYPOINT ["echo"]
  ```
In questo esempio, il container eseguirà sempre il comando `echo` quando viene avviato.

##### CMD
L'istruzione `CMD` può essere utilizzata per **fornire argomenti di default a un `ENTRYPOINT`, oppure per specificare un comando di fallback se non viene fornito alcun comando al momento dell'avvio del container**.
- **Esempio di utilizzo**:
  ```dockerfile
  FROM ubuntu
  CMD ["Hello, World!"]
  ```
  In questo esempio, se si avvia il container senza specificare un comando, Docker eseguirà `echo Hello, World!` (supponendo che l'entrypoint predefinito sia `sh -c`).

##### Combinazione di ENTRYPOINT e CMD
- **Utilizzo insieme**: `ENTRYPOINT` e `CMD` possono essere utilizzati insieme per definire sia il comando che gli argomenti predefiniti.
- **Esempio di combinazione**:
  ```dockerfile
  FROM ubuntu
  ENTRYPOINT ["echo", "hello"]
  CMD ["world"]
  ```
  In questo caso, il comando completo eseguito sarà `echo hello world`. Se si avvia il container con argomenti aggiuntivi, questi sovrascriveranno gli argomenti di `CMD`, ma non l'`ENTRYPOINT`, quindi `hello` verrà sempre scritto mentre `world` potrà essere modificato.

##### Sovrascrittura durante l'avvio del container
- **Sovrascrittura di CMD**: Se si specifica un comando quando si avvia un container, esso sovrascriverà il `CMD`.
  ```sh
  docker run <image> "Different message"
  ```
  In questo caso, verrà eseguito `echo Different message` anziché `echo Hello, World!`.
- **Sovrascrittura di ENTRYPOINT**: È possibile sovrascrivere `ENTRYPOINT` utilizzando l'opzione `--entrypoint` al momento dell'avvio del container.
  ```sh
  docker run --entrypoint /bin/bash <image>
  ```
  In questo caso, il container avvierà una shell bash anziché eseguire il comando specificato in `ENTRYPOINT`.

#### Multistage
Nei Dockerfile multistage ho la creazione di immagini Docker più efficienti e leggere in quanto sono separate le fasi di costruzione del software da quelle di esecuzione.
Di seguito, descriverò un esempio di Dockerfile multistage utilizzando il .NET SDK per eseguire `dotnet restore` e `dotnet publish`, e poi una versione più leggera basata su ASP.NET per l'entry point dell'applicazione.
```dockerfile
# Fase 1: Costruzione
# Utilizziamo l'image del .NET SDK come base per questa fase. Il tag `AS build` serve a dare un nome a questa fase, che useremo in seguito.
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
# Utilizziamo l'image più leggera di ASP.NET per eseguire l'applicazione.
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

#### Trick: Ottimizzare il `dotnet restore`
Se sviluppiamo un'applicazione in dotnet possiamo fare un trucco per evitare di scaricare tutti i pacchetti tutte le volte che lanciamo un'image docker: l'idea è che prima di copiare tutti i file facciamo un `dotnet restore` basandosi solo sul file `.csproj`; in questo modo lui scaricherà i pacchetti e li metterà nella sua cache e li riscaricherà solo se il file `.csproj` cambia.
```dockerfile
# Copio solo il file csproj che è l'unica cosa che serve per dotnet restore
COPY ["DockerCourseApi/DockerCourseApi.csproj", "DockerCourseApi/"]
# Lancio il comando effettivo
RUN dotnet restore "DockerCourseApi/DockerCourseApi.csproj"
# Copio tutti gli altri file
COPY . .
```

#### Esempi

##### Blazor
In questo esempio ho un `Dockerfile` che fa il `publish` di una app Blazor e la lancia su un server `nginx` in modo che sia accedibile dal browser.
Per farlo utilizzo un Dockerfile multistage in cui nella prima fase utilizzerà il .NET SDK per eseguire il `dotnet publish`, e la seconda fase utilizzerà un'image di Nginx per servire l'applicazione.

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

# Fase 2: Creazione dell'image Nginx
FROM nginx:alpine

# Copia i file pubblicati dalla fase di costruzione alla directory di Nginx
COPY --from=build /out/wwwroot /usr/share/nginx/html

# Espone la porta 80
EXPOSE 80

# Definisce il comando di avvio di Nginx
CMD ["nginx", "-g", "daemon off;"]
```

### Image

![[Pasted image 20240613145035.png]]

La _container image_ è un file statico presente su disco che contiene tutto ciò che è necessario all'applicazione per funzionare quindi tutte le sue dipendenze, file di configurazione, script, binari e così via.
Da una Image posso creare *n* diversi container, che saranno tutti identici in quanto "istanze" della stessa "Image".
Per esempio se voglio dare ad un mio collega il container che ho appena creato, gli fornirò il file Image e sarà lui a costruirsi la sua istanza, quindi il suo container.

![[Pasted image 20240613145254.png]]
#### Parallelo con l'OOP

In OOP, le classi servono come progetti per la creazione di oggetti. Definiscono i dati e i comportamenti che possono avere gli oggetti creati dalla classe. Allo stesso modo, ==un'image Docker serve come progetto per la creazione di container.==
Un'image include tutto il necessario per eseguire un'applicazione: il codice o binario, runtime, librerie, variabili di ambiente e file di configurazione.

Una volta creata, un'image Docker è immutabile. ==Pensa a un'image come a un'istantanea di una tua classe in un momento specifico==. Quando vuoi aggiornare la tua applicazione, crei una nuova image con le modifiche. Questo è parallelo a come potresti aggiornare una classe nella tua base di codice per riflettere queste modifiche.

#### Container Registry

Nell'image sopra si vede Bob che ha creato un'Image della sua webApp e vuole renderla pubblica: la pusha in un *container registry* (il più famoso è docker hub) e chi vuole la può pullare e crearsi la sua istanza di container esattamente come quella di Bob.
Ci sono vari container registry:
* Docker Hub (nel piano free una sola image privata disponibile)
* Azure Container Registry
* Amazon AWS
* Artifact registry di Google Cloud
* Github
* Harbor
Un utilizzo potrebbe essere che colui che pusha l'image è un servizio di Continuous Integration mentre colui che pulla un servizio di orchestration di container come Kubertenes.

![[Pasted image 20240619172717.png]]
##### Push
Per mandare la propria image su Container Registry, una volta creata la "repository" sull'interfaccia bisogna loggarsi con `docker login`; creare l'image con `docker build -f PathDockerFile -t usernameContainerRegistry/NomeRepository .` e infine fare `docker push usernameContainerRegistry/NomeRepository`.

#### Tags

Ogni image può avere differenti "versioni" di cui l'ultima si chiama, per convenzione `latest`.
![[Pasted image 20240617163147.png]]
In produzione conviene non usare `latest` ma esplicitare il numero di versione in quanto questi sono immutabili e puntano sempre allo stesso id, `latest` invece cambia con l'uscita di una nuova versione.

#### Layers

![[Pasted image 20240618143457.png]]
Ogni image è formata da vari strati, tipicamente si parte da un'image di base (esempio `Debian`) e poi si costruiscono altre immagini aggiungendo pacchetti all'image in questione.
Ogni layer è messo in cache per cui se scarico due immagini diverse che usano come layer la stessa image di `Debian` questa ultima non verrà scaricata nuovamente.

### Container
==Se un'image Docker è come una classe, allora un container Docker è come un'istanza di quella classe==.
Quando esegui un'image Docker, un container viene creato da quell'image. Questo container è un'istanza in esecuzione dell'image e include il suo file system, un set di processi e un'interfaccia di rete isolata dal sistema host e da altri container.
Puoi avviare, arrestare, spostare ed eliminare un container senza influenzare l'image da cui è stato creato, proprio come puoi manipolare un'istanza di una classe senza modificare la classe stessa.

## Docker compose
Docker Compose funge da ambiente in cui interagiscono più istanze di classi diverse. Se i container Docker sono istanze (definite dal loro Dockerfile), Docker Compose è come un'==applicazione che utilizza vari oggetti (container) per raggiungere un obiettivo più ampio==.
Ti consente di definire ed eseguire applicazioni Docker multi-container, gestendo il ciclo di vita di tali container tramite semplici comandi.
Questo comando permette:
* Definire l'ambiente della tua applicazione con un file `docker-compose.yml`, specificando quali container eseguire, le loro configurazioni, come comunicano e volumi condivisi, in modo simile alla definizione del modo in cui le istanze di classi interagiscono in un'applicazione. Dato che questo è un normale file di testo può essere version controllabile facilmente e si ha la certezza che tutti i componenti del team di sviluppo lancino lo stesso ambiente.
* Avviare, arrestare e ricostruire i servizi collettivamente con comandi come `docker-compose up` e `docker-compose down`, in modo simile all'inizializzazione o allo smantellamento dell'ambiente dell'applicazione.
* Isolare gli ambienti su un singolo host, assicurandoti che diverse istanze (container) non interferiscano tra loro, in modo simile ad avere istanze separate di un'applicazione con il proprio set di oggetti.

### Build delle immagini
Nel file `docker-compose.yml` posso anche fare il build delle immagini prima di lanciarle, questo viene fatto tramite il comando `build` indicando come `context` il path dove si trova il Dockerfile da utilizzare per costruire l'image in questione.

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

### Volumes

#### Standard volume

```yaml
version: '3.8'
volumes:
  myvolume:
	  external: true # indica che il volume è gestito esternamente a Docker Compose, ovvero, non è creato o gestito automaticamente da Docker Compose
services:
  app:
    image: myapp
    volumes:
      - myvolume:/path/inside/container
```

#### Bind Mount
```yaml
version: '3.8'
services:
  app:
    image: myapp
    volumes:
      - /path/on/host:/path/inside/container
```

### Database seeding
Posso sfruttare `docker-compose` non solo per far partire un'image del DBMS che mi serve ma anche per fare il seed.
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
# Prendo la stessa image del DBMS che mi serve
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


## Port mapping
Questa operazione permette di rendere pubblica la porta del container all'host ospitante. Per esempio lancio l'image di `nginx` e vado su `localhost` nel browser non vedo niente in quanto la porta di `nginx` non è esposta.
Se lancio il comando `docker run nginx -p 8080:80` posso definire, a sinistra del `:` la porta da cui accederemo da fuori dal container mentre a destra la porta a cui accederemo all'interno del container.
Per esempio con l'istruzione sopra se vado su `http://localhost:8080/` accedo alla porta 80 dell'image di `nginx` in Docker.
Posso anche specificarlo più volte per fare il mapping di n porte diverse, per esempio posso scrivere `docker run nginx -p 8080:80 -p 1234:52`.
## Persistent Storage

Spesso c'è l'esigenza che i container possano ==accedere a dei file che siano persistenti alla creazione dello stesso, quindi che siano fuori dal container e che sopravvivano alla sua distruzione==.
Inoltre questi file potrebbero essere condivisi tra più container contemporaneamente.
Esistono tre tipologie di storage persistente: `bind mount`, `volums` e `tmpfs`.

![[Pasted image 20240620122201.png]]
### Volume
Un `volume` è una directory che è all'interno di Docker ma separato dai container stessi. Questo spazio quindi sopravvive ai container e uno o più container possono utilizzarlo.
Per gestire i volumi si utilizza `docker volume`.
#### Comandi comodi
* `docker volume create [NAME]`: crea un volume chiamato `NAME`
* `docker volume ls`: visualizza tutti i `volume` che sono presenti su Docker
* `docker volume inspect VOLUME_NAME`: ottiene informazioni su un singolo volume
* `docker volume rm VOLUME_NAME`: rimuove il volume `VOLUME_NAME`

#### Utilizzare un volume
Una volta che un `volume` è stato creato posso aggiungere l'opzione `-v volume_name:inner_folder` al comando `docker run` per far sì che tutto ciò che dovrebbe andare in `inner_folder` all'interno del container vada invece nella cartella riferita a `volume_name`.
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
  # La sintassi è simile a quella del port mapping, a sinstra del : ci sono le cose all'esterno del container e a destra interno del container.
  # per cui i dati non verranno scritti/letti veramente in /var/opt/mssql ma nel volume "sqldb-data".
  # P.s. facendo docker volume inspect sqldb-data posso andare a vedere la cartella effettiva dove tali dati stanno
  # In questo modo quando spegnerò questo container la cartella contenente il db rimarrà in Docker, riaccendendolo non dovrò più fare il seed in quanto
  # lo storage è sempre quello
  # Se il volume esiste già lo utilizza altrimenti lo crea.
  # Posso anche avere più comandi "-v" e utilizzare vari volumi diversi.
  -v sqldb-data:/var/opt/mssql `
  mcr.microsoft.com/mssql/server:2022-latest
```

#### Esempio: backup di un volume
Con questo script posso effettuare il backup del contenuto di  un `volume` in una directory corrente nel proprio file system.
```powershell
docker run `
  --rm `
  -v BackupDemoVolume:/mydata `
  -v ${pwd}:/backup `
  alpine `
  sh -c "cd /mydata && tar cvf /backup/backup.tar *"
```
Il restore avviene con il metodo inverso
```powershell
docker run `
  --rm `
  -v RestoredVolume:/mydata `
  -v ${pwd}:/backup alpine sh `
  -c "cd /mydata && tar xvf /backup/backup.tar"
```

### Bind Mount
I file in questa cartella sono sul file system del sistema operativo ospitante Docker.
La sintassi è uguale a quella dei `volume`, cambia solo che a sinistra dei `:` non ho una stringa ma un path.

```powershell
# Crea un container di Sql Server.
docker run `
  --name nginx-withvol `
  -p 1234:80 `
  # detached
  -d `
  # In Nginx i file contenenti il "sito internet" stanno in "/usr/share/nginx/html". Scrivendo così creo un link al path locale corrente (sintassi ${pwd} di powershell) con /html.
  # I dati non verranno scritti/letti veramente in /usr/share/nginx/html ma in ${pwd}/html.
  -v ${pwd}/html:/usr/share/nginx/html `
  nginx
```

### Tmpfs
Usando un temporary File System i file sono in RAM nel sistema operativo ospitante. Ho un vantaggio di prestazioni ma tali file vengono persi alla chiusura del container che li sta utilizzando.

## Networking

Il networking in Docker è un aspetto cruciale per la gestione e l'orchestrazione dei container, ==consentendo ai container di comunicare tra loro e con il mondo esterno==.
Docker fornisce diversi driver di rete che offrono vari tipi di connettività, ognuno con le proprie caratteristiche e casi d'uso specifici.

### Driver di rete in Docker

Docker supporta diversi driver di rete, ciascuno progettato per soddisfare esigenze specifiche:
1. **Bridge Network**:    
    - È la **rete di default per i container Docker che non specificano una rete diversa**.
    - ==I container connessi alla stessa bridge network possono comunicare tra loro usando il nome del container come hostname==. Docker DNS risolve automaticamente i nomi dei container all'interno della stessa rete.
    - Fornisce isolamento di rete per i container.
    - Ideale per ambienti di sviluppo e test.
2. **Host Network**:    
    - I container che utilizzano il driver host ==condividono la stessa interfaccia di rete dell'host Docker==.
    - Non c'è isolamento tra il container e l'host dal punto di vista della rete.
    - Adatto per applicazioni che richiedono prestazioni di rete elevate e un basso overhead di latenza.
    - Funziona se il sistema operativo su cui è installato Docker è linux.
1. **None Network**:    
    - Disconnette completamente il container dalla rete.
    - Utile per container che non necessitano di connettività di rete.
La lista delle reti disponibili si ottiene con il comando `docker network ls`.
Facendo `docker inspect [CONTAINER ID]` nella sezione `Networks` viene fornito l'indirizzo IP effettivo che avrà tale container.

### Accedere all'IP di un altro container

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

### Custom network
Per creare una rete personalizzata in Docker, è possibile utilizzare il comando `docker network create`.
```cmd
docker network create --driver bridge my_custom_network
```
Una volta creata la rete posso collegarci un container in questo modo:
```cmd
docker run -d --name my_container --network my_custom_network nginx
```
Solo i container che saranno creati collegandosi a questa rete potranno parlare tra di loro, mentre gli altri non si vedranno.

### Docker compose
```yaml
version: '3'
services:
  web:
    image: nginx
    networks:
      - my_custom_network
  db:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: example
    networks:
      - my_custom_network

networks:
  my_custom_network:
    driver: bridge
```

### Trick: accedere a localhost da un container
Può capitare l'esigenza di dover accedere a `localhost` del sistema operativo ospitante docker all'interno di un container.
Per far questo al posto di `localhost` utilizzare `host.docker.internal` come DNS name.

## Sicurezza

### Docker scout

Docker Scout è uno strumento progettato per aiutare gli sviluppatori a gestire le vulnerabilità delle immagini Docker. Fornisce analisi approfondite delle immagini, rilevando problemi di sicurezza e suggerendo correzioni.
Ha molto senso integrare Docker Scout in una pipeline CI/CD per automatizzare l'analisi delle immagini Docker per garantire che solo immagini sicure vengano distribuite in produzione.
Esempio breve con `Gitlab CI` ma che rende l'idea.
```yaml
stages:
  - build
  - scan
  - deploy

build:
  stage: build
  script:
    - docker build -t myapp:latest .
  artifacts:
    paths:
      - myapp:latest

scan:
  stage: scan
  script:
    - docker scout cves myapp:latest > scout_report.txt
  artifacts:
    paths:
      - scout_report.txt
  allow_failure: false

deploy:
  stage: deploy
  script:
    - if grep -q "CRITICAL" scout_report.txt; then echo "Deployment stopped due to critical vulnerabilities"; exit 1; fi
    - docker push myapp:latest
  only:
    - main
```

### Running container as non-root

Dato che il container condivide lo stesso kernel con il sistema operativo che lo sta lanciando, a differenza di una VM, possono essere eseguiti degli attacchi col fatto che l'utente di default che gira nel container è root.
Con le seguenti due righe prima di `ENTRYPOINT` è possibile far girare il container con un utente nuovo, non root, e a cui posso customizzare i permessi per dargliene, potenzialmente, il meno possibile.
```dockerfile
# Change user to non-root (gecos means don't interactively prompt for various info about the user)
RUN adduser --disabled-password --gecos '' appuser
USER appuser
ENTRYPOINT ["COMMAND", "PARAM1"]
```

## Docker CLI
Docker fornisce una Command Line Interface con tutti i comandi comodi che possono servire, tutti iniziano con `docker`; vediamone alcuni:
* `docker run`: scarica un'image con `docker pull` e la lancia immediatamente. L'image viene messa in una cache in modo che non dovrà essere riscaricata la prossima volta.
	* `-e`: permette di aggiungere una variabile d'ambiente.
	* `-d` o `--detached`:  il container viene lanciato senza rimanere sul terminale ma rimanendo in background in modalità detached;
	* `--rm`: rimuove il container quando viene chiuso il terminale invece di fermarlo
	* `--name`: permette di dargli un nome
	* `-it`: lo lancia con terminale interattivo, quindi fornisce una terminale all'interno del container.
	* `--hostname`: permette di definire il nome dell'host che verrà risolto dal DNS nell'indirizzo IP.
* `docker pull`: scarica un'image e la aggiorna all'ultima versione se già presente;
* `docker ps`: fa una lista dei container che stanno girando in questo momento, indicandone anche il `container id` che è l'identificativo univoco. Aggiungendo l'opzione `-a` visualizza anche i container che esistono ma non sono attivi.
* `docker inspect [CONTAINER ID]`: visualizza le informazioni sul container indicato.
* `docker stop [CONTAINER ID]`: ferma il container indicato
* `docker rm [CONTAINER ID]`: rimuove il container dalla lista dei container gestiti da docker. Se con l'opzione `-f` rimuove anche un container che sta andando.
* `docker logs [CONTAINER ID]`: mostra i log di un container: comodo se questo è stato lanciato in modalità `detached`. Con l'opzione `-f` la console rimarrà a seguire il log.
* `docker attach [CONTAINER ID]`: si riattacca ad un container in modalità `detached` come se fosse stato lanciato senza l'opzione `-d`.
* `docker images`: lista tutte le immagini scaricate;
* `docker exec -it [CONTAINER ID] [COMANDO]`: permette di lanciare un comando come se fossi nel terminale del container. Se `[COMANDO]`è `sh` o `bash` lancia direttamente il terminale interno del container. Se il container è linux posso lanciare anche comandi di aggiornamento pacchetti come `apt-get` per installare quello che voglio, per esempio editor di testo per modificare file. Ovviamente tutte le modifiche che avvengono sono in quello specifico container e non nell'image da cui è partito.
* `docker build -t nome:tag .`: crea l'image a partire da un Dockerfile presente nella cartella corrente (notare il punto `.`). Se `tag` non è specificato usa la cartella corrente;
* `docker tag [SOURCE IMAGE ID] [IMAGE NAME]:[TAG NAME]`: effettua il tag dell'image con nome `[IMAGE NAME]` e con id `[SOURCE IMAGE ID]` con il tag `[TAG NAME]`.
* `docker rmi [IMAGE NAME]:[TAG NAME]`: elimina il tag `[TAG NAME]` dell'image `[IMAGE NAME]`. Se usato con `docker rmi [IMAGE NAME];` elimina l'image e tutti i tag
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
Posso cercare un'image e scaricarla con il pull o lanciarla direttamente.

## Docker per unit test

`dotnet.testcontainers` è una libreria per supportare i test con istanze usa e getta di container Docker.
==Questo approccio consente di eseguire test in un ambiente isolato e riproducibile==.
### Vantaggi

* L'ambiente su cui girano i test è identico indipendentemente dal PC che sta lanciando tali test, che sia un PC locale o un sistema di CI/CD.
* In caso di utilizzo per Database: non sporco il mio, eventuale, DBMS locale con database di test che poi devo pulire automaticamente (e sappiamo che non sempre succede…)
* In caso di utilizzo per Database: posso avere test che girano contemporaneamente su istanze del DBMS con versioni diverse: per esempio se un cliente ha il suo DBMS versione X è corretto che i suoi test girino sul DBMS con tale versione e non un mio DBMS aggiornato, mentre, esempio,  test della mia applicazione standard devono funzionare col DBMS all'ultima versione.
### Funzionamento

Una volta installato il pacchetto principale `dotnet.testcontainers` si possono aggiungere pacchetti aggiuntivi per delle immagini specifiche, per esempio per PostgreSQL c'è un pacchetto `Testcontainers.PostgreSql`.
Il sistema scaricherà, solo la prima volta, le immagini che gli servono (sicuramente `testcontainers/ryuk` che è un'immagine che fornisce comandi comodi per eliminare containers/networks/volumes/images con un determinato filtro dopo un determinato delay) e le immagini che servono per i test.
Una volta ottenute le immagini lancerà dei container usa e getta a partire da tali immagini.
Nella classe di test si potranno utilizzare in modo trasparente, nessuno sa che sto comunicando con un container invece che con un servizio effettivo.

### Esempio con PostgreSQL

In questo esempio utilizzo un container PostgreSQL in una classe `Fixture` di `xunit` creando un container che comunica sempre a porta 61342 dall'esterno con database chiamato `label_tracking_test_db`.

```csharp
public class LabelTrackingManagerFixture : IAsyncLifetime
{
    public PostgresDatabaseManagerTestable DatabaseManager { get; private set;}
    public TrackingManager TrackingManager { get; private set; }
    private const int PortNumber = 61342;
    private const int DefaultPostgreSqlPort = 5432;
    private const string DatabaseName = "label_tracking_test_db";
    private readonly PostgreSqlContainer _postgreSqlContainer = new PostgreSqlBuilder().WithPortBinding(PortNumber, DefaultPostgreSqlPort).WithDatabase(DatabaseName).Build();

    public async Task InitializeAsync()
    {
        await _postgreSqlContainer.StartAsync();
        DatabaseManager = new PostgresDatabaseManagerTestable("127.0.0.1", "postgres", "postgres", PortNumber, DatabaseName);
    }

    public Task DisposeAsync()
    {
        return _postgreSqlContainer.DisposeAsync().AsTask();
    }
}
```
