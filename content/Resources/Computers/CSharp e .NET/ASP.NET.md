---
tags:
  - Coding
  - CSharp
  - DotNET
---
## WebApi
Un approccio alternativo ai Web service basati su SOAP, che è stato proposto negli stessi anni ma è stato riscoperto soltanto negli ultimi tempi, è l’approccio noto come **REST** (Representational State Transfer) e basato su una serie di principi che un’applicazione deve rispettare. In sintesi, nella visione **RESTful** un Web service non definisce una funzione richiamabile da remoto ma mette a disposizone delle risorse su cui è possibile effettuare le classiche operazioni **CRUD** sfruttando i metodi del protocollo HTTP.
Si parla di **Web service** quando si fa riferimento a quelli basati su SOAP e di **Web API** quando ci ispira al modello REST.
Sfruttare WCF per realizzare Web service secondo l’approccio RESTful non è cosa immediata. Con **ASP.NET Web API**, Microsoft ha deciso di cambiare approccio nella realizzazione di Web service RESTful basandoli sul meccanismo di routing di MVC invece di cercare di semplificare la complessità intrinseca del sottosistema WCF.
### Componenti
Una Web API è costituita essenzialmente da **risorse accessibili via Web** tramite una o più rappresentazioni.
Una risorsa è generalmente un’**istanza di una classe che viene inviata al client dopo averla serializzata**. ASP.NET Web API supporta in maniera predefinita la serializzazione in JSON e XML. **Ciascuna risorsa è rintracciabile sul Web tramite uno specifico URI, mappato nel nostro framework sfruttando il meccanismo di routing di ASP.NET**. La gestione dei metodi HTTP applicabili alle risorse è affidata ai **Controller**, un tipo di classe i cui metodi **implementano le richieste giunte all’applicazione via HTTP**.
In sostanza, un client richiede l’esecuzione di un metodo HTTP, ad esempio GET, su una risorsa identificata da un URI. Il framework, interpretando l’URI, individua il controller associato alla risorsa e, in base allo specifico metodo HTTP ed ai parametri specificati dal client, invoca il metodo corrispondente. Il risultato dell’esecuzione del metodo è una risorsa e/o un codice di stato HTTP. Se viene restituita una risorsa, questa viene serializzata in base al formato richiesto dal client tramite l’intestazione HTTP Accept.
### Convenzioni
#### Lo schema dell'URI
La prima convenzione è quella che riguarda lo schema dell’URI per individuare una risorsa. La route definisce uno schema di URL con {controller} e {id} come segnaposto per il controller della risorsa e l’eventuale identificatore.
```
/api/{controller}/{id}
```
Alla ricezione di una richiesta HTTP, il sistema analizzando l’URL andrà alla ricerca di un controller per la risorsa specificata. L’individuazione del controller viene effettuata concatenando al nome indicato al posto di *{controller}* con la parola chiave controller. Quindi, facendo riferimento al nostro esempio, per gestire l’URL */api/items/API*, il sistema cercherà un controller con nome *ItemsController*.
Per capire quale metodo del controller invocare, il sistema fa riferimento al metodo HTTP utilizzato dal client. In pratica, se il client ha utilizzato il metodo GET, il sistema andrà alla ricerca di un metodo del controller il cui nome inizia proprio con get, individuando nel nostro caso il metodo GetItemByTerm(). Lo stesso meccanismo sarà valido per i metodi PUT, POST e DELETE.

* * *

## WCF 4.0
### Introduzione
WCF è l'acronimo di Windows Communication Foundation e rappresenta una delle ultime tecnologie sviluppate da Microsoft per lo sviluppo di applicazioni in ambiente distribuito e per la comunicazione tra applicazioni. Rappresenta un modello di programmazione unificata per la costruzione di **applicazioni orientate ai servizi**.
WCF è una tecnologia che mette insieme ASMX Web Services, *WSE*, *.Net Remoting*, *System Messaging* ed *Enterprise Service*.
### ABC
L'acronimo **ABC (Address Binding Contract)** è la chiave di lettura per capire la composizione di un servizio WCF e del suo funzionamento.

#### Address - Dove si trova il servizio?

Indica la **locazione specifica di un servizio**, il "posto" dove inviare i messaggi. Tutti i servizi WCF sono distribuiti da uno specifico indirizzo rimanendo in ascolto di eventuali richieste. Un indirizzo è normalmente specificato da un URL, dove la prima parte specifica il meccanismo di trasporto mentre la parte restante specifica la locazione univoca del servizio.

Ad esempio l'indirizzo http://www.wcfservices.com/myservices/myfirstservice è un address WCF che utilizza HTTP come protocollo di trasporto, il servizio è presente sul server www.wcfservices.com raggiungibile tramite il percorso univoco myservices/myfirtservice.

#### Binding - Come parlo con il servizio?

Le associazioni (bindings) sono utilizzate per **specificare il dettagli relativi al transport, all'encoding, e al protocol richiesti dal client per poter comunicare con il servizio**. Un binding è costituito da una collezione di elementi dove ogni elemento specifica un aspetto di come il servizio comunica con i client. Un binding deve includere almeno un elemento relativo al **transport** (ad esempio TCP o HTTP), uno all'**encoding** (ad esempio Text o Binary) dei messaggi ed uno al **protocol**. Alcuni dei Bindings forniti "gratis" da WCF sono:

BasicHTTPBinding,WSHTTPBinding, WSDualHttpBinding,WSFederationHttpBinding, NetTcpBinding, NetNamedPipeBinding, NetMsmqBinding, NetPeerTcpBinding e MsqmIntegrationBinding.

#### Contract - Che cosa può fare il servizio per me?

**Un contratto WCF è un insieme di specifiche che definisce l'interfacce di un servizio WCF**. Un servizio WCF comunica con altre applicazioni accordandosi tramite "contratti". Ci sono diversi tipi di contratto: *Service Contract*, *Operation Contract*, *Data Contract*, *Message Contract* e *Fault Contract*.
* **Service Contract**:informa **che cosa il servizio può fare**. Un servizio WCF ha almeno un Service Contract.
* **Operation Contract**: definito all'interno di un Service Contract, **definisce i parametri e i tipi di ritorno di un'operazione**. Un'operazione può prendere in ingresso dati primitivi come ad esempio interi, tipi complessi definiti tramite Data Contract o tipi definiti tramite Message Contract. Un Operation Contract definisce anche altre impostazioni come la direzione (ad esempio one-way o two-way) o il Fault Contract, uno o più errori che possono presentarsi durante l'esecuzione dell'operazione.
* **Message Contracts**: Se un'operazione ha necessità di **passare un messaggio come parametro o ritornare un messaggio**, il tipo di questi messaggi è definito dai Message Contracts. Questo tipo di messaggio definisce alcuni aspetti come quelli legati alla sicurezza o se un determinato elemento deve essere inserito all'interno del body o dell'header del messaggio.
* **Data Contracts**: specificano i tipi di dato del servizio WCF. Tutti i tipi di dato usati dal servizio WCF devono essere descritti dai metadati (tramite il Data Contract) affinché le applicazioni possano interagire con il nostro servizio. Un Data Contract può essere utilizzato da un Operation Contract come parametro o return type, oppure può essere utilizzato da un Message Contract per definire elementi del messaggio.
* **Fault Contract**: specifica un'eventuale errore che può essere ritornato al chiamante del servizio. Ogni operazione di un servizio può avere zero o più Fault Contracts.



### Endpoint

Un Endpoint è un **"posto" dove le comunicazioni sono inviate e/o ricevute** (secondo della configurazione). La comunicazione avviene tra Endpoints. Un servizio può esporre uno o più Application Endpoints (zero o più Inftrastructure Endpoints). Un servizio espone queste informazioni come metadati che le applicazioni processano per generare gli opportuni WCF client da utilizzare per la comunicazione con il servizio. Quando necessario un client genera un Endpoint compatibile con uno degli Endpoints esposti dal servizio. **Ogni Endpoint è descritto ad un indirizzo, un binding ed un Service Contract (WCF ABC)**.

### Hosting

Un servizio WCF è un componente che può essere chiamato da altre applicazioni. Deve essere eseguito in un ambiente per poter essere "scoperto" (discovered) e usato. **L'host WCF è un'applicazione che controlla la vita del servizio**. Come vedremo ci sono diversi modi per eseguire l'hosting di un servizio WCF.

### Self Hosting

Un servizio WCF può essere **self-hosted, ovvero il servizio può girare come applicazione standalone e auto controllare il proprio lifetime**. Questo è il modo più flessibile e semplice di eseguire l'hosting di un servizio WCF, avendo però funzionalità limitate.

### Windows Services Hosting

Un servizio WCF può anche essere **ospitato (hosted) come servizio Windows** (un processo gestito dal sistema operativo e automaticamente fatto partire con l'avvio di esso, se opportunamente configurato).

### IIS Hosting

Uno dei migliori modi di eseguire l'**hosting di un servizio WCF è utilizzare IIS**. Per sua natura IIS ha molti funzionalità utili come process recycling, idle shutdown, process health monitoring, attivazione message-based, high availability, easy manageability, versioning e scenari di deployment, tutte funzionalità richieste da servizi WCF di livello enterprise.

### Metadata

I metadata di un servizio descrivono **le caratteristiche del servizio che un'entità esterna deve conoscere per poter comunicare con il servizio stesso**. I metadata possono essere consumati tramite il ServiceModel Metadata Utility (scvutil.exe) per generare un client WCF e per fornire la configurazione che un'applicazione client deve avere per poter interagire con il servizio. I metadata esposti dal servizio includono XML schema che ne definiscono i Data Contract, documenti WDSL che ne descrivono i metodi. E' possibile nascondere i metadata anche se non è una pratica comune.

## WCF SelfCare.Next
### Trilance.Selfcare.Next.DAL
Contiene le chiamate effettive al DB con gli script "provider", che eseguono effettivamente la query (o la chiamata alla stored). Per esempio TicketProvider ha il metodo getNature() seguente
```c#
public IEnumerable<NaturaReclamo> GetNature()
{
using (var connection = GetOpenSqlConnection())
{
var result = connection.Query<NaturaReclamo>("select IDNatura, Descrizione as DescrizioneNatura from NatureReclami ");
return result;
}
}
```
### Trilance.Selfcare.Next.WCF
Wrapper per il DAL, creando dei Service. In particolare per ogni servizio hoo la creazione di una **interface** e del servizio effettivo figlio dell'interfaccia:

```c#
public interface ITicketService
{
[OperationContract]
IEnumerable<NaturaReclamo> GetNature();
...
}
```

```c#
public class TicketService : ITicketService
{
public IEnumerable<NaturaReclamo> GetNature()
{
return new TicketProvider().GetNature();
}
...
}
```
### Trilance.Selfcare.Next.Web
Comunicazione del server con l'esterno, conoscono solo i ServiceReference. Quando modifico un serviceReference devo aggiornare la firma (tasto destro, aggiorna riferimento al serivizio) in modo che i suoi metodi possano essere visibili anche da quì.
```c#
public static class GestoreElenco
{
public static IEnumerable<NaturaFAQ> GetElencoNature2()
{
TicketServices.TicketServiceClient ticket = new TicketServices.TicketServiceClient();
List<NaturaReclamo> nature = ticket.GetNature().ToList();
...
}
...
}
```

### Trilance.Selfcare.Next.Entities
Classi che rappresentano le tabelle del DB, i loro attributi sono le colonne delle tabelle con getter e setter. Non hanno metodi.
## Trilance.Selfcare.Next.Settings
Soliti settings che valgono per tutta la soluzione (con i transform.zconfig)
## Trilance.Selfcare.Next.Resources


* * *

I generics consentono di personalizzare un metodo, una classe o una struttura in base ai dati precisi su cui interviene.
Ad esempio, invece di usare la classe `Hashtable`, che consente di avere chiavi e valori di ogni tipo, è possibile usare la classe generica `Dictionary<TKey, TValue>` e specificare il tipo concesso per la chiave e quello concesso per il valore. Tra i vantaggi dei generics ci sono **una maggiore riutilizzabilità del codice e l'indipendenza dai tipi**.

## Definizione
I generics sono classi, strutture, interfacce e metodi dotati di **segnaposto (parametri di tipo) per uno o più dei tipi archiviati o usati**.
Una classe di raccolte generiche può usare un parametro di tipo come segnaposto per il tipo di oggetti in essa contenuti. I parametri di tipo vengono visualizzati come i tipi dei relativi campi e i tipi di parametri dei relativi metodi. Un metodo generico potrebbe usare il parametro di tipo come il tipo di valore restituito o come il tipo di uno dei parametri formali.

## Classi
Nel codice seguente viene illustrata una definizione di classe generica semplice.
```c#
public class Generic<T>
{
public T Field;
}
```
Quando si **crea un'istanza di una classe generica, è possibile specificare i tipi effettivi da sostituire per i parametri di tipo**. Ciò consente di stabilire una nuova classe generica, definita come una classe generica costruita, con **tipi prescelti sostituiti a ogni occorrenza dei parametri di tipo**. Il risultato è una classe indipendente dai tipi personalizzata in base alla scelta di tipi, come illustrato nel codice seguente.
```
public static void Main()
{
Generic<string> g = new Generic<string>();
g.Field = "A string";
}
```
## Metodi
Una definizione di metodo generico è un metodo con due elenchi di parametri: **un elenco di parametri di tipo generico e un elenco di parametri formali**. I parametri di tipo possono apparire come tipo restituito o come tipi dei parametri formali, come illustrato nel codice seguente.
```c#
T Generic<T>(T arg)
{
T temp = arg;
//...
return temp;
}
string foo = Generic<string>("a_string");
```

Assumiamo di avere la seguente classe, che possiede 3 attributi (pubblici) con un costruttore che permette di inizializzarne (secondo il vecchio metodo) solo due.
```c#
public class StudentName
{
// Proprietà
public string FirstName { get; set; }
public string LastName { get; set; }
public int ID { get; set; }

//Costratture di default che viene chiamato solo se viene istanziata la classe con l'object initializer
public StudentName() { }

//Costruttore classico
public StudentName(string first, string last)
{
FirstName = first;
LastName = last;
}
}
```
Questa classe può essere istanziata in questi modi
```c#
// Metodo classico
StudentName student1 = new StudentName("Craig", "Playstead");

// Con l'object initializer: viene chiamato il costruttore di default
StudentName student2 = new StudentName
{
FirstName = "Craig",
LastName = "Playstead",
};
// Con l'object initializer posso inizializzare qualsiasi proprietà pubblica della classe
StudentName student3 = new StudentName
{
ID = 183
};
```

* * *

## Routing
In ASP.NET WebApi è usato un routing basato su convenzioni, analogo a quello di Rails, le route vengono definite come attributi quindi sopra una classe e sono principalmente stringhe parametriche. Quando il framework riceve una richiesta, fa un match dell'URI con il template.
Route di esempio:
```c#
public class OrdersController : ApiController
{
[Route("customers/{customerId}/orders")]
[HttpGet]
public IEnumerable<Order> FindOrdersByCustomer(int customerId) { ... }
}
{}
```
In questo esempio, "customers" e "orders" sono stringhe, mentre "customerId" è una variabile, i seguenti URI matchano questo template:
* http://localhost/customers/1/orders
* http://localhost/customers/bob/orders
* http://localhost/customers/1234-5678/orders


### RoutePrefix
Spesso tutte le route di un controller iniziano con lo stesso prefisso, per esempio:
```c#
public class BooksController : ApiController
{
[Route("api/books")]
public IEnumerable<Book> GetBooks() { ... }

[Route("api/books/{id:int}")]
public Book GetBook(int id) { ... }

[Route("api/books")]
[HttpPost]
public HttpResponseMessage CreateBook(Book book) { ... }
}
```
In questo caso posso settare un prefisso comune per tutto il controller usando l'attributo **RoutePrefix**, trasformando così la route nel seguente modo:
```c#
[RoutePrefix("api/books")]
public class BooksController : ApiController
{
// GET api/books
[Route("")]
public IEnumerable<Book> Get() { ... }

// GET api/books/5
[Route("{id:int}")]
public Book Get(int id) { ... }

// POST api/books
[Route("")]
public HttpResponseMessage Post(Book book) { ... }
}
```
Il RoutePrefix può anche includere parametri:
```c#
[RoutePrefix("customers/{customerId}")]
public class OrdersController : ApiController
{
// GET customers/1/orders
[Route("orders")]
public IEnumerable<Order> Get(int customerId) { ... }
}
```

### Vincoli di route
I vincoli di route permettono di scegliere un metodo del controller in base al **tipo** di parametro in ingresso, per esempio
```c#
[Route("users/{id:int}"]
public User GetUserById(int id) { ... }

[Route("users/{name}"]
public User GetUserByName(string name) { ... }
```
La prima route verrà scelta solo per l'ID è un integer, altrimenti verrà scelta la seconda route.
Posso anche includere più vincoli nella stessa route separati dai **:**, per esempio per chiamare una route solo se il parametro in ingresso è un numero intero con valore minimo 1 scrivo:
```c#
[Route("users/{id:int:min(1)}")]
public User GetUserById(int id) { ... }
```

### Parametri opzionali e valori di default
Se aggiungo un punto di domanda al parametro della route, questo diventa opzionale, se un parametro di route è opzionale devo definire un valore di default nel caso in cui questo non sia presente
```c#
public class BooksController : ApiController
{
[Route("api/books/locale/{lcid:int?}")]
public IEnumerable<Book> GetBooksByLocale(int lcid = 1033) { ... }
}
```
In questo caso `/api/books/locale/1033` e `/api/books/locale` forniscono la stessa risorsa

##UnitTest

### Creare un progetto di test
Per prima cosa devo creare un nuovo progetto UnitTest, quindi
```
File -> Aggiungi -> Nuovo Progetto -> Progetto Unit Test -> Scrivere il nome (es. BankTests)
```
Devo ora prendere il riferimento alla soluzione **Bank**, quindi fare
```
Riferimenti -> aggiungi riferimento -> espandere soluzione -> selezionare Bank
```

### Aggiungere le configurazioni
Dato che il progetto UnitTest è un progetto console (autolanciante), non può appoggiarsi a delle configurazioni di un oggetto padre (come per le WebApi che si appoggiano a ApiNext), è necessario quindi aggiungere i file di configurazione analoghi a ApiNext.
Per prima cosa installare ConfigZilla
```
Tasto dx -> gestisci pacchetti NuGet -> sezione Trilance.NuGet -> ConfigZilla.Setty
```
Aggiungere quindi il file di configurazione
```
Aggiungi -> nuovo elemento -> file di configurazione dell'applicazione
```
Chiamandolo *App.ztransform.config*. Ora inserirvi le configurazioni richieste (per le connectionString scrivere:
```xml
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
<connectionStrings>
<add name="Ticketing" providerName="System.Data.SqlClient" connectionString="{{ticketing.connectionString}}" />
</connectionStrings>
</configuration>
```
Creare un nuovo file di configurazione chiamandolo _App.config_ e ** escluderlo dal codice sorgente (file -> controllo del codice sorgeìnte -> escludi _App.config_ dal controllo del codice sorgente).
Ora, compilando la soluzione, tale file dovrebbe essere autocompletato dal plugin Configzilla automaticamente.


### Aggiungere la classe di Test
In Esplora soluzioni selezionare il file _UnitTest1.cs_ nel progetto BankTests, rinominarlo e aggiungere il riferimento alla classe testata
```c#
using BankAccountNS
```

### Scrivere il test
Il metodo da controllare è il seguente:
```c#
public void Debit(double amount)
{
if(amount > m_balance)
{
throw new ArgumentOutOfRangeException("amount");
}
if (amount < 0)
{
throw new ArgumentOutOfRangeException("amount");
}
m_balance -= amount;
}
```
Un primo test potrebbe essere il seguente
```c#
[TestMethod]
public void Debit_WithValidAmount_UpdatesBalance()
{
// arrange
double beginningBalance = 11.99;
double debitAmount = 4.55;
double expected = 7.44;
BankAccount account = new BankAccount("Mr. Bryan Walton", beginningBalance);

// act
account.Debit(debitAmount);

// assert
double actual = account.Balance;
Assert.AreEqual(expected, actual, 0.001, "Account not debited correctly");
}
```

### Compilare la soluzione
Per aprire la finestra di esplorazione test fare
```
Test -> Finestre -> Esplora Test
```
Da qui posso eseguire tutto o solo i test falliti e così via.
Eseguo questa procedura e il test viene superato correttamente.

### Usare il metodo Expecte[[DEX]]ception
Dato che il metodo da testare genera delle eccezzioni posso usare il metodo `Expecte[[DEX]]ception` nel seguente modo
```c#
[TestMethod]
[Expecte[[DEX]]ception(typeof(ArgumentOutOfRangeException))]
public void Debit_WhenAmountIsLessThanZero_ShouldThrowArgumentOutOfRange()
{
// arrange
double beginningBalance = 11.99;
double debitAmount = -100.00;
BankAccount account = new BankAccount("Mr. Bryan Walton", beginningBalance);

// act
account.Debit(debitAmount);

// assert is handled by Expecte[[DEX]]ception
}
```



## Configurare una soluzione con ConfigZilla
Nella soluzione principale, sotto Enviroment c'è un file chiamato **ConfigZilla** dove c'è scritto il path dove andare a prendere le configurazioni, per esempio
```
Trilance.ApiNext.Settings\
```
oppure:
```
Trilance.ApiNext.Settings\trilance\amga\amga-test
```
in tale cartella troviamo delle cartelle e un file chiamato `transform.zconfig` che sarà il file con tutte le configurazioni (JSON) da usare nel progetto, per esempio le connection string:
```json
{
"userEntity": {
"connectionString": "Data Source=magneto;uid=miniAdmin;pwd=miniSchiappa;initial Catalog=dbDatamaxGRN"
},
"centroNotifiche": {
"connectionString": "Data Source=magneto;uid=miniAdmin;pwd=miniSchiappa;initial Catalog=dbDatamaxGRN"
},
}
```
Se ho un path profondo, tipo
```
Trilance.ApiNext.Settings\trilance\amga\amga-test
```
lui prenderà il zconfig del path in questione facendo un **merge con i zconfig dei padri** (in caso di conflitto prenderà il valore del figlio).

### Configurare un ambiente di test
Nel file configZilla indicare la stringa `Trilance.Selfcare.Next.Settings\FO\Trilance`, che indica che il database utilizzato sarà **magneto**. Notare che configZilla è un file che non viene caricato in VSS, ognuno quindi può mettere la configurazione che vuole senza influenzare gli altri.

## Importazione DLL
Per importare una DLL il modo migliore è creare un nuovo pacchetto NuGet con NuGet Package Explorer.
open local package -> \\connor\tools\Trilance.NuGet\nome.lib
Una volta fatto lo pubblico nel path corretto (\\connor\tools\Trilance.NuGet) e quindi questo è accessibile a tutti, per importarlo clicco sul destro nella soluzione che voglio (GestioneRate per esempio), gestione pacchetti nuget, trilance.NuGet, e lo trovo, installo/aggiorno e tutto funziona correttamente.

### Importare configurazioni di una DLL esterna con App.config
Assumo di voler utilizzare una DLL esterno il cui codice sorgente è (in VSS) nel seguente path
```
$/SWDEV/2012/Trilance.ApiNext.root/Trilance.ApiNext
```
In tale path, oltre al codice sorgente, troviamo anche un file **App.config** dove sono indicate le configurazioni necessarie affinchè questa possa funzionare. In particolare è indicata la seguente connection string (richiesta dal pacchetto DLL in questione):
```xml
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
<connectionStrings>
<add name="GestioneRate" connectionString="User ID=miniadmin;Password=miniSchiappa;data source=magneto;persist security info=false;initial catalog=BillingTGRN; min pool size = 50; max pool size = 500;" providerName="System.Data.SqlClient" />
</connectionStrings>
</configuration>
```
Affinchè la DLL possa funzionare, tale ConnectionString deve essere inserita all'interno del progetto principale, per fare ciò utilizziamo il path
```
Trilance.ApiNext/Web.ztransform.config
```
dove sono indicate le connectionStrings da utilizzare nella soluzione, per esempio da questa situazione:
```xml
<connectionStrings>
<add name="OpenCombo" providerName="System.Data.SqlClient" connectionString="{{openCombo.connectionString}}" />
<add name="UserEntity" providerName="System.Data.SqlClient" connectionString="{{userEntity.connectionString}}" />
<add name="CentroNotifiche" providerName="System.Data.SqlClient" connectionString="{{centroNotifiche.connectionString}}" />
</connectionStrings>
```
passo a
```xml
<connectionStrings>
<add name="OpenCombo" providerName="System.Data.SqlClient" connectionString="{{openCombo.connectionString}}" />
<add name="UserEntity" providerName="System.Data.SqlClient" connectionString="{{userEntity.connectionString}}" />
<add name="CentroNotifiche" providerName="System.Data.SqlClient" connectionString="{{centroNotifiche.connectionString}}" />
<add name="GestioneRate" providerName="System.Data.SqlClient" connectionString="{{GestioneRate.connectionString}}" />
</connectionStrings>
```
Notare che le connectionString presenti hanno un placeholder (per esempio `centroNotifiche.connectionString`) che fa riferimento a quello dei **settings**, conseguentemente in `transform.zconfig` troverò:
```json
{
...
"GestioneRate": {
"connectionString": "User ID=miniadmin;Password=miniSchiappa;data source=magneto;persist security info=false;initial catalog=BillingTGRN; min pool size = 50; max pool size = 500;",
"ttl": 0
}
...
}
```
Fatto questo la configurazione è stata eseguita correttamente e la DLL potrà funzionare correttamente.

## Aggiunta di riferimenti

### Utilizzare metodi in altri progetti della stessa soluzione
Esempio classico sono le WebApi che vogliono usare i metodi della DLL con la logica.
Tasto dx sulla cartella riferimenti -> aggiungi riferimento -> Spunta sul progetto da integrare

### Rendere visibile una WebApi
Quando chiamo una WebApi lui fa riferimento sempre alla WebApi principale (per esempio Trilance.ApiNext). Se ho creato una nuova WebApi e voglio renderla visibile tasto destro sulla cartella riferimenti di Trilance.ApiNext -> aggiungi riferimento -> spuntare la WebApi in questione. Nel caso si utilizzi il **ConfigurationManager** che non viene visto ricorda di aggiungere il riferimento col metodo sopra (sotto la cartella *Assembly*
e utilizza la ricerca)

### Risolvere problemi di configurazioni differenti (newtonsoft 4.5)
Nel caso in cui non si riesca a risolvere l'errore HRESULT: 0x80131040 copincollare il seguente codice in _App.config_. Questo sovrascrive in runtime le configurazioni in modo che il compilatore sia ok.
```xml
<runtime>
<assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">
<dependentAssembly>
<assemblyIdentity name="Newtonsoft.Json" publicKey[[Token]]="30ad4fe6b2a6aeed" culture="neutral" />
<bindingRedirect oldVersion="0.0.0.0-6.0.0.0" newVersion="6.0.0.0" />
</dependentAssembly>
<dependentAssembly>
<assemblyIdentity name="System.Web.Http" publicKey[[Token]]="31bf3856ad364e35" culture="neutral" />
<bindingRedirect oldVersion="0.0.0.0-5.0.0.0" newVersion="5.0.0.0" />
</dependentAssembly>
</assemblyBinding>
</runtime>
```

## Parametri in ingresso al controller
Quando un metodo di controller è in post, significa che ha come primo parametro in ingresso un oggetto complesso in POST, gli altri parametri invece sono in query string. Nel caso in cui io abbia due oggetti da passare avrò un oggetto complesso che wrappa i due oggetti complessi in questione.
Se per esempio ho due metodi POST che hanno come primo parametro lo stesso oggetto complesso devo differenziarli (se così non fosse la differenziazione sarebbe automatica) cambiando la route.

### Metodi POST
Nel Body, in raw inserisco il JSON con un l'oggetto complesso che voglio provare.
Esempio:
```json
{
"IDAzienda": 2,
"IDAnagrafica": 42216,
"IDFattura": 626822,
"Importo": 1276706,
"NumeroRate": 5,
"DataPrimaScadenza": "2014-02-10 00:00:00.000",
"IDFrequenza": 1
}
```



## Mappare un oggetto fornito dal DB in un altro
Quando ho delle Stored che restituiscono un oggetto ma le mie specifiche richiedono che l’oggetto che fornisco al frontend sia una rielaborazione di questo, posso fare due classi: una classe entity privata (*TicketConfigurationDB*) che mappa esattamente ciò che è stato fornito dal server e una classe pubblica (*TicketConfiguration *) che sarà la classe fornita dal controller.
La classe privata avrà un metodo (*ToTicketConfiguration()*) che trasformerà tale oggetto nell’oggetto *TicketConfiguration * richiesto dal frontend.

### Entity
```c#
internal class TicketConfigurationDB
{
public int IdReclamoPubblicazione { get; set; }
...
public TicketConfiguration ToTicketConfiguration()
{
newReclamoPubblicazione = IdReclamoPubblicazione,
...
}
}
```
### Chiamata alla Stored e conversione
```c#
var ticketConfigurationDB = connection.Query<TicketConfigurationDB>("Selfcare.GetReclamoPubblicazioneById_V2",
TicketConfiguration ticketConfiguration = ticketConfigurationDB.ToTicketConfiguration();
```

* * *

Quando devo lavorare con degli id costanti, che però ovviamente dipendono dal database con cui sto lavorando, devo creare delle config a livello di WebApi con il seguente metodo

- Verificare a che config punta il `configZilla` e verificare che sia corretto
- Aggiungere la costante nel `transform.zconfig` associato
- Recuperare il valore della costante con il seguente metodo

```c#
ConfigurationManager.AppSettings["padre:figlio"]
```

* * * 

Nel caso in cui vi sia la necessità di eseguire degli update o degli insert su DB conviene eseguirli all'interno di una transazione, nel caso in cui ci siano problemi SQL è possibile eseguire un rollback (
## Gestione standard di una transazione
```c#
var transaction = connection.BeginTransaction();
try
{

transaction.Connection.Query("stored_procedure_name"
, new {}
, transaction: transaction
, commandType: CommandType.StoredProcedure);
...
transaction.Commit();
}
catch (SqlException ex)
{
transaction.Rollback();
}
```