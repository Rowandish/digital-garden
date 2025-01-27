#Dometrain 

Amazon Simple Queue Service (SQS) è un servizio di messaggistica completamente gestito che consente la decoupling tra componenti di un'applicazione, è la versione cloud dell'implementazione di una coda producer consumer.
![[Pasted image 20241210164944.png]]
Il servizio è sempre gratuito fino a 1 milione di richieste.

### Cosa è una Queue
Quando un'API viene chiamata, la sua prima operazione, sincrona, è tipicamente la scrittura nel database. Successivamente, può svolgere altre attività asincrone, come inviare email o effettuare chiamate ad altre API.
Per disaccoppiare queste operazioni asincrone dalle responsabilità dell'API principale, si implementa una _queue_. Dopo aver scritto nel database, l'API aggiunge un messaggio alla coda, che è un semplice file JSON di testo.
Un servizio _consumer_ separato si occupa di elaborare i messaggi dalla coda, eseguendo le operazioni richieste in modo indipendente e completamente asincrono. Questo consumer gestisce fallimenti, retry e altre eventuali problematiche, sollevando l'applicazione principale da tali responsabilità.

### Configurazioni
- **Standard vs FIFO**: Le code Standard offrono throughput illimitato e un ordine approssimativo dei messaggi, mentre le FIFO garantiscono l'ordine e la consegna unica a scapito di un limite nel numero di richieste per secondo e una minore scalabilità. La soluzione migliore è sempre *Standard* in quanto eventuali richieste multiple possono essere gestite lato applicazione consumer.
- **Visibility Timeout**: Periodo durante il quale un messaggio estratto dalla coda è nascosto agli altri consumer per evitare elaborazioni simultanee. Consente di completare l'elaborazione in modo sicuro.    
- **Message Retention Period**: Tempo massimo per cui un messaggio rimane nella coda prima di essere eliminato automaticamente se non viene elaborato.    
- **Delivery Delay**: Ritardo configurabile tra l'inserimento di un messaggio nella coda e la sua disponibilità per il consumo. Utile per posticipare l'elaborazione.    
- **Maximum Message Size**: Dimensione massima in byte di un messaggio. Garantisce performance e stabilità limitando i dati trasferibili in un singolo messaggio.    
- **Receive Message Wait Time**: Periodo massimo in cui un consumer aspetta per ricevere un messaggio quando la coda è vuota. Riduce chiamate inutili grazie alla logica di _long polling_.

### Dead Letter Queue
Può capitare che l'elaborazione di un messaggio dalla coda non vada a buon fine: questa cosa non deve bloccare gli altri messaggi della coda che devono essere consumati. Inoltre non devo in loop continuamente riprovare ad elaborare il messaggio (che non sarà stato rimosso dalla coda principale in quanto non elaborato) in quanto probabilmente continuerà a fallire bloccando tutti gli altri.
La soluzione è implementare il pattern `Dead Letter Queue`.
L'idea è provare ad elaborare un messaggio un numero finito di volte, esempio 3. Quindi per tre volte il messaggio non viene rimosso dalla coda principale in quanto magari è un problema temporaneo e ci sta riprovarci.
Dopo l'ennesimo fallimento lo elimino dalla coda principale e lo metto in un'altra coda ad hoc, la `Dead Letter Queue`.
Questa coda verrà gestita manualmente dagli sviluppatori che riceveranno degli alert automatici quando un nuovo messaggio entra in tale coda e verificheranno il da farsi, scoprendo tipicamente bug e così via.

#### AWS

Su AWS basta creare una nuova queue, convenzionalmente con il nome della coda di riferimento con un append di `-dlq`, indicando il massimo valore nel `Message retention period` in quanto, dato che i messaggi verranno controllati a mano, vogliamo che ci stiano il più a lungo possibile.
Una volta creata andare sulla coda originale (nel mio esempio `customers`) e, nelle opzioni, abilitare "dead letter queue" indicando la coda appena creata come coda da inviare i messaggi che vengono ricevuti ma non eliminati `Maximum receives` volte.
Quindi se un messaggio raggiunge tale numero come `receive count` viene inviato alla coda automaticamente.
Inoltre nella coda principale devo modificarla andando nella sezione `Redrive allow policy -> By queue` indicando la `dlq`.
Una volta fatto comparirà un pulsante nell'interfaccia principale della coda chiamato `Start DLQ redrive` che permette di rimettere tutti i messaggi nella `dlq` nella coda principale; questo tipicamente avviene quando nell'applicazione è stato sistemato un bug e conseguentemente voglio riprocessare tutti i messaggi.
Notare che ci sono due opzioni sul numero di messaggi da mandare alla coda principale, il primo, `System optimized` li manda alla massima velocità possibile, il secondo `Custom max velocity` permette di inviarli fino ad un massimo di `x` al secondo in modo da non imballare il sistema se riceve troppi messaggi da processare contemporaneamente.

### Best practice

### Consumer con Lambda
Uno dei modi più puliti per gestire un evento con SQS è usare una [[Lambda]]: invece di deployare un server che bisogna gestire e eventualmente scalare in base alla richieste posso pensare di gestire tutto tramite lambda che è un servizio serverless che si autoscala in base alla richieste e praticamente gratuito.
#### Contract publisher consumer
Dato che tra il publisher e il consumer di una queue c'è un "contract" che indica la struttura  dell'oggetto che viene scambiato non voglio passare direttamente customer in quanto qualora il dominio venisse cambiato dovrei modificare anche il contratto con il consumer, cosa che non voglio essere obbligato a fare.
E' una best practice quindi fornire non l'oggetto del dominio (esempio `Customer`) ma una sua versione stile `CustomerCreated`, cosa che viene fatta da una classe mapper come nell'esempio sotto.
```csharp
public static CustomerCreated ToCustomerCreatedMessage(this Customer customer)  
{  
    return new CustomerCreated  
    {  
        Id = customer.Id,  
        Email = customer.Email,  
        GitHubUsername = customer.GitHubUsername,  
        FullName = customer.FullName,  
        DateOfBirth = customer.DateOfBirth  
    };  
}
```
#### Consumer con ASP.NET Core
Per implementare un consumer in Asp.NET Core è buona norma utilizzare la classe `BackgroundService` dato che permette di far girare servizi in background in modo compatibile con tutto l'ecosistema ASP.NET.
La classe in questione poi viene aggiunta usando il metodo `AddHosterService`, per esempio `builder.Services.AddHostedService<QueueConsumerService>();`

### Esempio
Il pacchetto nuget `Amazon.SQS` fornisce dei metodi comodi per interagire con la coda.
#### Publisher
```csharp
public record CustomerCreated(Guid Id, string FullName, string Email, string GitHubUsername, DateTime DateOfBirth);

var sqsClient = new AmazonSQSClient();

var customer = new CustomerCreated
{
    Id = Guid.NewGuid(),
    Email = "nick@nickchapsas.com",
    FullName = "Nick Chapsas",
    DateOfBirth = new DateTime(1993, 1, 1),
    GitHubUsername = "nickchapsas"
};

var queueUrlResponse = await sqsClient.GetQueueUrlAsync("customers");

var sendMessageRequest = new SendMessageRequest
{
    QueueUrl = queueUrlResponse.QueueUrl,
    MessageBody = JsonSerializer.Serialize(customer),
    MessageAttributes = new Dictionary<string, MessageAttributeValue>
    {
        {
            "MessageType", new MessageAttributeValue
            {
                DataType = "String",
                StringValue = nameof(CustomerCreated)
            }
        }
    },
    
};

var response = await sqsClient.SendMessageAsync(sendMessageRequest);
```
#### Consumer
```csharp
var cts = new CancellationTokenSource();  
var sqsClient = new AmazonSQSClient();  
  
//A partire dal nome della coda fornisce l'URL corretto a cui mandare le richieste  
var queueUrlResponse = await sqsClient.GetQueueUrlAsync("customers");  
  
var receiveMessageRequest = new ReceiveMessageRequest  
{  
    QueueUrl = queueUrlResponse.QueueUrl,  
    AttributeNames = new List<string>{ "All" },  
    MessageAttributeNames = new List<string>{ "All" }  
};  
  
while (!cts.IsCancellationRequested)  
{  
    var response = await sqsClient.ReceiveMessageAsync(receiveMessageRequest, cts.Token);  
  
    foreach (var message in response.Messages)  
    {        Console.WriteLine($"Message Id: {message.MessageId}");  
        Console.WriteLine($"Message Body: {message.Body}");  
  
        // Consumare un messaggio non porta alla sua eliminazione, devo comunicarlo esplicitamente  
        await sqsClient.DeleteMessageAsync(queueUrlResponse.QueueUrl, message.ReceiptHandle);  
    }    await Task.Delay(3000);  
}
```
