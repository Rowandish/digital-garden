Questa nota prende a piene mani dal corso [Cloud Fundamentals: AWS Services for C# Developers](https://courses.dometrain.com/courses/take/cloud-fundamentals-aws-services-for-csharp-developers).

## Introduzione

Amazon Web Services (AWS) è una piattaforma cloud leader che offre oltre 200 servizi completi per il calcolo, lo storage, il networking, il machine learning e altro ancora.

### Piani gratuiti
1. **Prova gratuita (free trial)**: Questo piano è disponibile per determinati servizi AWS e consente agli utenti di accedere a funzionalità premium per un periodo limitato, di solito 30 o 60 giorni.
2. **12 mesi gratuito (12 months free)**: Questo piano offre accesso gratuito a diversi servizi AWS per i primi 12 mesi dall'iscrizione.
3. **Sempre gratuito (always free)**: questo piano include servizi e risorse che rimangono gratuiti per sempre, indipendentemente dalla durata dell'account.
### Autenticazione

#### Root user
Esiste la possibilità di autenticare il PC come root, quindi qualsiasi azione che viene da tale PC viene effettuata senza chiedere le credenziali come admin (qualsiasi Console Application non necessiterà quindi di alcuna autenticazione).
Questa è la soluzione più comoda ma non è una best practice; può essere utilizzata temporaneamente durante lo sviluppo.
Per farlo fare i seguenti passaggi:
* AWS Console -> Access keys -> Create Access Key
* Scaricare la CLI di AWS
* `aws configure`
* Scrivere l'Access Key ID, il Secret Access Key, la region di riferimento e l'output format (json)

## SQS

Amazon Simple Queue Service (SQS) è un servizio di messaggistica completamente gestito che consente la decoupling tra componenti di un'applicazione.
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

### SNS

Amazon Simple Notification Service (SNS) è un servizio di messaggistica basato su pubblicazione/sottoscrizione. Permette di inviare notifiche a una vasta gamma di destinatari, inclusi email, SMS, e funzioni Lambda.
SNS è altamente scalabile e supporta casi d'uso come notifiche push per dispositivi mobili, avvisi di sistema e aggiornamenti in tempo reale.
Il servizio è gratis fino a 1 milione di publisher.

I topic di SNS fungono da hub centralizzati per inoltrare messaggi a più sottoscrittori in modo asincrono. È possibile configurare politiche di accesso granulari per garantire la sicurezza.

### DynamoDB

Amazon DynamoDB è un database NoSQL completamente gestito, progettato per supportare carichi di lavoro ad alte prestazioni e latenza bassa e prevedibile. DynamoDB è particolarmente adatto per applicazioni che richiedono scalabilità elastica, come giochi, e-commerce e IoT.
Gratis fino a 25FB di storage.
Supporta tabelle, chiavi primarie e indici secondari per ottimizzare le query. Con funzionalità come DynamoDB Streams e capacità on-demand, il servizio è flessibile e permette di gestire grandi volumi di dati senza complessità operativa.

### S3

Amazon Simple Storage Service (S3) è un servizio di storage scalabile e durevole progettato per archiviare e recuperare qualsiasi quantità di dati.
Il servizio fornisce 5GB gratis per 12 mesi.
S3 offre classi di storage come Standard, Intelligent-Tiering e Glacier per ottimizzare i costi in base alla frequenza di accesso ai dati. I bucket di S3 supportano controlli di accesso granulare e versioning per la gestione dei dati. È ideale per casi d'uso come backup, archiviazione, distribuzione di contenuti e analisi dei dati. L'integrazione con altri servizi AWS lo rende estremamente versatile.

### Secrets Manager

AWS Secrets Manager aiuta a proteggere segreti come credenziali di database, chiavi API e password. Consente di ruotare, gestire e recuperare segreti in modo sicuro attraverso le sue API. Secrets Manager elimina la necessità di includere credenziali nei codici sorgenti, migliorando così la sicurezza.
Nel free tier ha un trial di 30 giorni.
Con l'integrazione nativa con altri servizi AWS come Lambda e RDS, Secrets Manager automatizza la gestione delle credenziali. Offre anche audit dettagliati delle operazioni per garantire la conformità.

### Lambda

AWS Lambda è un servizio serverless che esegue il codice in risposta a eventi, senza dover gestire l'infrastruttura sottostante. Gli sviluppatori possono caricare codice scritto in diversi linguaggi come Python, JavaScript e Go, e Lambda si occupa del provisioning e della scalabilità. Lambda è perfetto per automazioni, elaborazione dati in tempo reale e back-end di applicazioni.
Questo servizio è sempre gratis fino a 1M di richieste al mese.
Grazie alla sua integrazione con altri servizi AWS, è possibile attivare funzioni Lambda da eventi come modifiche a S3, messaggi SQS o notifiche SNS.