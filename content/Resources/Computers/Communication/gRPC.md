---
tags:
  - Dometrain
---
Questa nota prende a piene mani dal corso [From Zero to Hero: gRPC in .NET](https://dometrain.com/course/from-zero-to-hero-grpc-in-dotnet/).

## Introduzione
gRPC è un framework di comunicazione open-source sviluppato da Google che permette di costruire API ad alte prestazioni, basate sul protocollo **HTTP/2** e sul formato di serializzazione **Protocol Buffers (Protobuf)**.

A differenza delle tradizionali **RESTful API**, che si appoggiano a JSON su HTTP/1 o 2, gRPC utilizza un approccio fortemente tipizzato e binario, offrendo vantaggi in termini di efficienza, velocità e robustezza.

### Confronto tra gRPC e REST
- **Contratto**: gRPC richiede la definizione esplicita di uno schema tramite file `.proto`, mentre in REST la documentazione è opzionale.
- **Protocollo**: gRPC usa **HTTP/2** nativamente, mentre REST può usare HTTP/1 o HTTP/2.
- **Payload**: gRPC scambia messaggi binari **Protobuf** (più compatti), REST usa JSON (più verboso).
- **Tipizzazione**: gRPC è fortemente tipizzato, REST no.
- **Streaming**: gRPC supporta **client-streaming, server-streaming e bi-direzionale**, REST solo client-server.
- **Generazione client**: gRPC fornisce strumenti integrati, mentre REST si affida a OpenAPI o librerie di terze parti.
- **Sicurezza**: entrambi usano TLS per il trasporto sicuro.
### Quando usare gRPC?

gRPC è particolarmente utile in scenari che richiedono:
- **Microservizi**, dove le comunicazioni tra servizi devono essere veloci e affidabili.
- **Comunicazioni real-time point-to-point**, grazie al supporto nativo per lo streaming.
- **Ambienti poliglotti**, dove diversi linguaggi convivono.
- **Reti a larghezza di banda limitata**, ad esempio su dispositivi mobili.
- **Inter-process communication (IPC)** e **background jobs** (Windows service, CRON).

Per una normale web app il classico JSON è più che sufficiente e performante.
    
## Protocol Buffers

I **Protocol Buffers** (o Protobuf) sono un sistema di serializzazione dei dati creato da Google per permettere comunicazioni veloci, leggere e indipendenti dal linguaggio di programmazione.

Al centro c’è il file **.proto**, che definisce la struttura dei messaggi: in esso si descrivono i campi, i tipi e le regole con una sintassi semplice e precisa.
Le sue caratteristiche sono le seguenti:
- Indipendente dal linguaggio e dalla piattaforma.
- Permette di definire in maniera chiara la struttura dei dati e delle operazioni.
- Fortemente tipizzato
- Supporta compatibilità **forward e backward**, rendendo semplice l’evoluzione delle API.
- È **estensibile** e dispone di **supporto multi-linguaggio**, rendendolo adatto a sistemi complessi e distribuiti.

Un file **`.proto`** è la descrizione del contratto tra sistemi che devono comunicare tra loro. Dentro non c’è codice eseguibile ma solo la definizione dei messaggi, cioè la struttura dei dati, e dei servizi, cioè le operazioni RPC. ==Si può pensare a questo file come a uno schema condiviso che stabilisce in che formato ci si deve parlare==.

Il file da solo non basta: per usarlo si passa attraverso un processo di **code generation**. Lo strumento ufficiale, chiamato `protoc` (Protocol Compiler), legge il `.proto` e genera automaticamente il codice sorgente nel linguaggio che serve al progetto, ad esempio C#, Java o Python. Quel codice contiene le classi per i messaggi e le interfacce o gli stub per i servizi, così lo sviluppatore non deve preoccuparsi di serializzare o deserializzare manualmente i dati: gli basta lavorare con oggetti normali, mentre la libreria Protobuf gestisce tutta la parte binaria.

==È importante capire che il file `.proto` non viene mai scambiato a runtime tra client e server. Entra in gioco soltanto in fase di sviluppo==: il team che definisce l’API lo scrive e lo condivide, poi ogni team, che sia lato client o lato server, genera a partire da quel file il codice nella propria lingua di programmazione. In questo modo entrambi i lati parlano la stessa lingua e interpretano i dati nello stesso modo, senza doversi accordare continuamente sui dettagli di implementazione.

Un esempio pratico chiarisce meglio. Supponiamo di definire in un file `user.proto` un servizio `UserService` con un metodo `GetUser`, che accetta un messaggio `GetUserRequest` e restituisce un `User`. 

```proto
syntax = "proto3";

package myapp;

service UserService {
  rpc GetUser (GetUserRequest) returns (User);
}

message GetUserRequest {
  int32 id = 1;
}

message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}
```

Dal file `.proto` il compilatore genera, in C#, le classi `User` e `GetUserRequest`, più la base `UserServiceBase` che il server deve estendere.
```csharp
public sealed partial class User : pb::IMessage<User> {
    public int Id { get; set; }
    public string Name { get; set; } = "";
    public string Email { get; set; } = "";
}
```
E dal servizio `UserService` otteniamo uno **stub server-side** da implementare:
```csharp
public abstract class UserServiceBase : grpc::BindServiceMethod {
    public virtual Task<User> GetUser(GetUserRequest request, ServerCallContext context) {
        throw new RpcException(new Status(StatusCode.Unimplemented, ""));
    }
}
```
Noi implementiamo il servizio ereditando dalla classe base:
```csharp
public class UserServiceImpl : UserService.UserServiceBase {
    public override Task<User> GetUser(GetUserRequest request, ServerCallContext context) {
        return Task.FromResult(new User {
            Id = request.Id,
            Name = "Alice",
            Email = "alice@example.com"
        });
    }
}
```
Dal `.proto` viene generato anche lo **stub client**, così il client può chiamare il servizio come se fosse un normale metodo:
```csharp
var channel = GrpcChannel.ForAddress("https://localhost:5001");
var client = new UserService.UserServiceClient(channel);

var reply = await client.GetUserAsync(new GetUserRequest { Id = 1 });

Console.WriteLine($"User: {reply.Name} ({reply.Email})");
```

### Struttura del file .proto
#### Well-known types
I **Protocol Buffers** sono molto compatti, ma non hanno nativamente tutti i tipi di dato che spesso servono nello sviluppo. Per questo Google ha introdotto una libreria di **"well-known types"**, che contiene messaggi già pronti da importare nei file `.proto`. Alcuni esempi: `Timestamp`, `Duration`, `Wrappers` (per i nullable), e `Empty`.

Un caso comune è quando dobbiamo definire un **messaggio vuoto**: Protobuf non permette di dichiarare un messaggio completamente senza campi a meno che non sia esplicitamente definito. Google fornisce già `google.protobuf.Empty` per questo scopo.

```proto
syntax = "proto3";

import "google/protobuf/empty.proto";

service UserService {
  // Metodo per resettare la cache
  rpc ResetCache(google.protobuf.Empty) returns (google.protobuf.Empty);
}
```

#### Any
`google.protobuf.Any` è un tipo speciale messo a disposizione da Protobuf per **incapsulare un messaggio arbitrario**.
- Serve quando non conosci a priori quale messaggio dovrai ricevere o inviare.
- Può contenere **qualsiasi tipo di messaggio**, insieme a un riferimento al suo tipo per poterlo ricostruire.
In pratica, è un modo per rendere un campo “dinamico” senza perdere la sicurezza tipica di Protobuf.
`Any` contiene due cose:
1. **`type_url`** → una stringa che identifica il tipo del messaggio originale (es. `"type.googleapis.com/mypackage.User"`).
2. **`value`** → i dati serializzati del messaggio (in formato binario Protobuf).
Quando un client riceve un `Any`, può controllare il `type_url` per capire di che tipo si tratta e fare l’**unpacking** del messaggio corretto.

##### Esempio
```proto
syntax = "proto3";

import "google/protobuf/any.proto";

message User {
  int32 id = 1;
  string name = 2;
}

message Event {
  string id = 1;
  google.protobuf.Any payload = 2;
}
```
Compilando con `protoc`, in C# ottieni le classi `User`, `Event` e la gestione di `Any` tramite `Google.Protobuf.WellKnownTypes.Any`.

##### **Packing** (inserire un messaggio dentro `Any`)
```csharp
using Google.Protobuf.WellKnownTypes;

var user = new User { Id = 1, Name = "Alice" };

// Creiamo un Any che contiene User
Any packedUser = Any.Pack(user);

var evt = new Event
{
    Id = "evt-123",
    Payload = packedUser
};
```

##### **Unpacking** (estrarre il messaggio da `Any`)
```csharp
// Verifica se l'Any contiene davvero un User
if (evt.Payload.Is<User>())
{
    User unpackedUser = evt.Payload.Unpack<User>();
    Console.WriteLine($"User ID: {unpackedUser.Id}, Name: {unpackedUser.Name}");
}
```
## Le 4 tipologie di comunicazione
- **Unary**: 1 richiesta → 1 risposta. È il pattern “classico” tipo REST.
- **Server-streaming**: 1 richiesta → **stream** di risposte. Il server invia più messaggi finché ha dati.
- **Client-streaming**: **stream** di richieste → 1 risposta. Il client invia più messaggi e chiude la stream; il server risponde una sola volta.
- **Bidirectional streaming**: **stream↔stream**. Client e server inviano messaggi indipendentemente e in parallelo finché una delle due parti chiude.
Nel file .proto In _server-streaming_ e _bidirectional_ la parola chiave è `stream` nel tipo **di risposta**; in _client-streaming_ e _bidirectional_ è `stream` nel tipo **di richiesta**.

### Esempio
Questo è un esempio di implementazione in C# di gRPC server che implementa i 4 metodi del `.proto`.  
```csharp
public class DemoServiceImpl : DemoService.DemoServiceBase
{
    // === Unary ===
    public override Task<SumResponse> Add(SumRequest request, ServerCallContext context)
    {
        int result = request.A + request.B;
        return Task.FromResult(new SumResponse { Result = result });
    }

    // === Server-streaming ===
    public override async Task Range(NumbersRequest request, IServerStreamWriter<Number> responseStream, ServerCallContext context)
    {
        for (int i = request.From; i <= request.To; i++)
        {
            await responseStream.WriteAsync(new Number { Value = i });
            await Task.Delay(200); // giusto per simulare streaming progressivo
        }
    }

    // === Client-streaming ===
    public override async Task<UploadSummary> Upload(IAsyncStreamReader<UploadChunk> requestStream, ServerCallContext context)
    {
        ulong totalBytes = 0;

        await foreach (var chunk in requestStream.ReadAllAsync())
        {
            totalBytes += (ulong)chunk.Data.Length;
            // qui potresti calcolare un checksum incrementale
        }

        return new UploadSummary
        {
            BytesReceived = totalBytes,
            Checksum = "dummy-checksum" // fittizio
        };
    }

    // === Bidirectional streaming ===
    public override async Task Chat(IAsyncStreamReader<ChatMessage> requestStream, IServerStreamWriter<ChatMessage> responseStream, ServerCallContext context)
    {
        await foreach (var msg in requestStream.ReadAllAsync())
        {
            Console.WriteLine($"[{msg.User}] {msg.Text}");

            // echo indietro con timestamp
            var reply = new ChatMessage
            {
                User = "Server",
                Text = $"Echo: {msg.Text}",
                SentAtUnix = DateTimeOffset.UtcNow.ToUnixTimeSeconds()
            };

            await responseStream.WriteAsync(reply);
        }
    }
}
```
## Tips & Tricks
* E' buona prassi avere uno o più file `.proto` in un unico file `.csproj`, tipicamente il server, e gli altri progetti che lo utilizzano, come i client, puntano a questo ultimo tramite la sintassi
```xml
<ItemGroup>  
    <Protobuf Include="..\Path\ToFileProto\test.proto" GrpcServices="Client" Link="Protos\test.proto" />  
</ItemGroup>
```
* gRPC supporta nativamente i `CancellationToken` per annullare un'operazione, tipicamente di streaming, dal client o dal server;
* Il channel è la connessione di lunga durata tra client e servizio gRPC, costruita sopra HTTP/2 (o HTTP/3) e riutilizzata per molte chiamate grazie al multiplexing. È lui che si occupa di risoluzione DNS o service discovery, configurazione TLS, keepalive, backoff dopo errori e, quando previsto, bilanciamento lato client. Nelle applicazioni è buona pratica crearne pochi (spesso uno per servizio) e riusarli per tutta la vita del processo.
* In gRPC il significato dell’esito non si legge dallo status HTTP ma da `grpc-status`. Errori applicativi e condizioni note si mappano su codici standard: ad esempio `INVALID_ARGUMENT` per input non valido, `NOT_FOUND` quando una risorsa manca, `DEADLINE_EXCEEDED` per timeout, `CANCELLED` per annullamenti, `UNAVAILABLE` per guasti temporanei e `INTERNAL` per errori non previsti. Conviene convertire in modo uniforme le eccezioni interne in questi codici e aggiungere dettagli nei metadati senza esporre informazioni sensibili.
## HTTP Request - Anatomy
In gRPC ogni chiamata è un POST a un percorso del tipo `/package.Service/Method` con `content-type: application/grpc` e messaggi binari (di solito Protobuf) incapsulati nei frame HTTP/2. Le informazioni di controllo viaggiano negli header iniziali e nei trailer finali; questi ultimi contengono l’esito vero dell’RPC.
### Client -> Server
![[Pasted image 20250825094421.png]]
Il client invia gli header (metodo, path, content-type, `te: trailers`, eventuale `authorization`, timeout con `grpc-timeout`, compressione) e poi il corpo con uno o più messaggi length-prefixed, a seconda che la chiamata sia unary o streaming. La fine dello stream viene segnalata dal flag di chiusura.
### Server -> Client
![[Pasted image 20250825094452.png]]
Il server risponde con header di accettazione e invia il corpo con i messaggi di risposta. La chiusura include i trailer con `grpc-status` e `grpc-message`, oltre a eventuali metadati, che indicano se la chiamata è andata a buon fine o meno.
## Interceptors
Gli interceptor sono “anelli” che avvolgono le chiamate e permettono di inserire comportamenti trasversali come log, tracing, metriche, autenticazione, retry o circuit breaker. A differenza dei middleware HTTP generici, vedono i concetti gRPC (metodo, messaggi, status) e quindi sono lo strumento più adatto per la cross-cutting logic in un servizio gRPC.
* **Client interceptors**: sul client un interceptor può aggiungere token o header, misurare la latenza, arricchire il contesto o applicare politiche di ripetizione controllata prima e dopo l’invocazione.
* **Server interceptors**: sul server l’interceptor incapsula l’handler e consente di centralizzare validazioni, rate limiting, audit e la mappatura coerente degli errori verso gli status di gRPC.
## Client side load balancing
Un channel può conoscere più endpoint dello stesso servizio e scegliere dinamicamente a chi inviare ogni chiamata. Le politiche semplici includono pick-first (si connette al primo server disponibile) e round-robin (distribuisce le chiamate). In contesti avanzati si usano configurazioni via service config o xDS per includere salute dei backend e preferenze di routing, ottenendo failover rapido senza passare per un proxy L7 dedicato.
## Transient-fault handling
I guasti temporanei di rete o di processo si gestiscono con tentativi controllati e tempi d’attesa progressivi, sempre fissando una deadline alla chiamata per evitare di occupare risorse indefinitamente.
### Retry policies
Le politiche di retry definiscono numero massimo di tentativi, backoff iniziale, moltiplicatore e massimo, oltre all’elenco degli status “ritentabili” come `UNAVAILABLE`. Vanno applicate solo a operazioni idempotenti o sicure, in genere su chiamate unary; gli stream richiedono strategie più caute.
![[Pasted image 20250825150256.png]]
### Hedging policy
L’hedging invia più tentativi sfalsati da un piccolo ritardo e accetta la prima risposta valida, annullando le altre. È una tecnica efficace per ridurre la tail latency, ma va riservata a metodi idempotenti per evitare effetti collaterali duplicati.
![[Pasted image 20250825150421.png]]

## Unit tests
Nei test conviene esercitare direttamente gli handler passando messaggi Protobuf finti e simulando il contesto dell’RPC. Per coprire autenticazione, timeout e cancellazioni, si crea un `ServerCallContext` fittizio (o la sua variante di test messa a disposizione dal framework), impostando host, deadline, token di cancellazione e metadati. Gli interceptor si testano invocandoli con un delegato finto e verificando che log, metriche e metadati risultino come atteso.
## Performance
Confronto tra tre approcci d’API — **REST (JSON)**, **GraphQL** e gRPC distribuiti su un **cluster Kubernetes**. L'obiettivo è misurate **latenza (P90)**, **throughput (RPS)**, **CPU**, **memoria** e **rete**.
- **Avvio del test:** senza carico, gRPC risulta leggermente più lento per l’overhead di (de)serializzazione; la situazione cambia con più traffico.    
- **Degrado di GraphQL:** già verso **10.000 RPS** peggiora; intorno a **24.000 RPS** inizia a fallire ed è rimosso dai grafici.    
- **Throughput massimo:**    
    - GraphQL ≈ **32.000 RPS**        
    - REST (JSON) ≈ **66.000 RPS**        
    - gRPC ≈ **90.000 RPS**
- **Latenza:** GraphQL è più lento per via del motore di query. REST e gRPC sono vicini nella prima metà; **sotto ~40% di CPU** REST ha latenza minore, ma **con più carico gRPC è più stabile** — utile per microservizi.    
- **Uso di rete:** il client gRPC consuma **molta meno banda** (impatto sui costi cloud). La rete di GraphQL/REST appare più bassa a fine test solo perché gestiscono meno richieste.    
- **CPU e memoria:** a fine test **CPU di REST e gRPC converge**; **memoria** non è decisiva ma gRPC ha **impronta minore**.        
- **Conclusioni pratiche:**    
    - **Web app:** preferire **REST**.        
    - **Mobile:** se possibile usare **gRPC** per migliore latenza/UX.        
    - **Service-to-service/Microservices:** **gRPC** fortemente consigliato.
Vedi: https://www.youtube.com/watch?v=uH0SxYdsjv4

### Risultato intermedio
Fino a 12k RPS le tre soluzioni sono più o meno equivalenti.
![[Pasted image 20250923143114.png]]
### Risultato finale
Ad RPS molto alto gRPC (90k RPS) è risultato il migliore in tutti i benchmark.
![[Pasted image 20250825155025.png]]