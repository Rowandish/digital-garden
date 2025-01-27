#Dometrain 

Amazon Simple Notification Service (SNS) è un servizio di messaggistica basato su pubblicazione/sottoscrizione. Permette di inviare notifiche a una vasta gamma di destinatari, inclusi email, [[SQS]], SMS, e funzioni Lambda.
SNS è altamente scalabile e supporta casi d'uso come notifiche push per dispositivi mobili, avvisi di sistema e aggiornamenti in tempo reale.
Il servizio è gratis fino a 1 milione di publisher.

L'idea di base di SNS è estendere il concetto di [[SQS]] creando *n* code invece che una sola in modo che ogni `consumer` utilizzi solo la coda sui messaggi che lo riguardano.
Il `producer` invierà i messaggi ad un unico punto chiamato `topic` il quale funge da hub centralizzato per inoltrare messaggi a più sottoscrittori in modo asincrono, per esempio a più [[SQS]].
Ogni topic sarà associato a *n* `subscriptions` che saranno i servizi (esempio [[SQS]]) a cui inviare i messaggi.
I `consumer` utilizzeranno una [[SQS]] esattamente come l'esempio sopra senza sapere che dietro c'è questo ulteriore layer di disaccoppiamento.
![[Pasted image 20241210165010.png]]Vantaggi:
* Ogni consumer processerà tutti i messaggi della coda, senza implementare filtri per capire se è un messaggio inviato a lui o meno.
* Posso inviare lo stesso messaggio anche a più code insieme, se la mia applicazione lo necessita
* Ogni singola coda avrà la sua dead letter queue separata dalle altre: per esempio se ho un bug nell'applicativo che invia le mail non voglio che tali messaggi, che andranno nella DLQ, siano mescolati ad altri messaggi di altri bug di altri applicativi.

### AWS

#### Creare Topic e Subscription

Per prima cosa è necessario creare un `topic` che è l'hub dove verranno inviati i messaggi. Poi si dovrà scegliere tra `Standard` e `FIFO` e, come per le [[SQS]], è meglio scegliere `Standard` e gestire lato applicativo l'idempotenza.
Una volta creato il `topic` è necessario creare almeno una `subscription` in modo che sappia dove inviare il messaggio.
Nell'interfaccia di creazione della `subscription` dovrò fornire il `topic`, il protocollo (esempio Amazon [[SQS]]) e la coda di destinazione che devo aver già creato in precedenza.
#### Raw Message Delivery
SNS di default wrappa il messaggio originale in un suo formato stile Notification, cosa che tipicamente non voglio in quanto voglio che il mio messaggio sia inoltrato così come è alle varie `subscriptions` senza essere modificato in alcun modo.
Questo può essere indicando selezionando la checkbox `Raw Message Delivery`.

#### Permessi
Per ultima cosa devo indicare alla coda che esiste un topic SNS che può scriverci dentro, altrimenti quest'ultimo, non avendo i permessi per farlo, non funzionerà.
Per farlo devo andare nella `Queue Policies` e aggiungere un nuovo `Statement`.

```json
{
  "Version": "2012-10-17",
  "Id": "__default_policy_ID",
  "Statement": [
    {
      "Sid": "__owner_statement",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::412381757397:root"
      },
      "Action": "[[SQS]]:*",
      "Resource": "arn:aws:[[SQS]]:eu-west-3:412381757397:customers"
    },
    // Da qui in poi è lo statement che permette al topic di scriverci dentro
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sns.amazonaws.com"
      },
      "Action": "[[SQS]]:SendMessage",
      "Resource": "arn:aws:[[SQS]]:eu-west-3:412381757397:customers", //ARN della coda in questione
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:sns:eu-west-3:412381757397:customers" // ARN del topic SNS
        }
      }
    }
  ]
}
```

#### In-app filter
Una delle feature principali di SNS è permettere automaticamente di inoltrare i messaggi alle code in base a dei criteri in modo che ogni coda riceva solo i messaggi che la riguardano e non tutti i messaggi.
Per farlo bisogna andare nella `subscription`, sezione `Subscription filter policy` dove posso specificare una policy basata sull'attributo del messaggio oppure anche su alcune caratteristiche del body, il tutto tramite un json.
Per esempio questo json filtra solo i messaggi che hanno come attributo `MessageType` il valore `CustomerCreated`.
```json
{
  "MessageType": [
    "CustomerCreated"
  ]
}
```

### Esempio
Il pacchetto nuget per lavorare con SNS è `Amazon.SimpleNotificationService`, una volta aggiunto i metodi sono molto simili a quelli di [[SQS]] con la differenza nella terminologia.
#### Publisher
```csharp
var customer = new CustomerCreated  
{  
    Id = Guid.NewGuid(),  
    Email = "nick@nickchapsas.com",  
    FullName = "Nick Chapsas",  
    DateOfBirth = new DateTime(1993, 1, 1),  
    GitHubUsername = "nickchapsas"  
};  
  
var snsClient = new AmazonSimpleNotificationServiceClient();  
  
var topicArnResponse = await snsClient.FindTopicAsync("customers");  
  
var publishRequest = new PublishRequest  
{  
    TopicArn = topicArnResponse.TopicArn,  
    Message = JsonSerializer.Serialize(customer),  
    MessageAttributes = new Dictionary<string, MessageAttributeValue>  
    {        {            "MessageType", new MessageAttributeValue  
            {  
                DataType = "String",  
                StringValue = nameof(CustomerCreated)  
            }        }    }};  
  
var response = await snsClient.PublishAsync(publishRequest);
```
#### Consumer
Il consumer è identico a quello implementato per la [[SQS]] in quanto per lui è una normale coda, non sa che dietro c'è un sistema SNS.