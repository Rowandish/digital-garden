#Dometrain 

AWS Lambda è un servizio [[Serverless vs Server|serverless]] che esegue del codice in risposta a eventi, senza dover gestire l'infrastruttura sottostante (per questo è detto servizio *serverless*).
Gli sviluppatori possono caricare codice scritto in diversi linguaggi come Python, C#, JavaScript e Go, e Lambda si occupa del provisioning e della scalabilità.
Queste funzioni sono il collante tra i vari servizi AWS in quanto possono essere triggerate in maniera automatica da eventi (esempio un nuovo evento in una [[SQS]] o [[SNS]], una modifica ad un dato in [[DynamoDB]] se ho abilitato gli streams e così via).
Questo servizio è sempre gratis fino a 1M di richieste al mese.
## CLI

### AWS

Una volta installata la CLI di aws sono disponibili delle funzioni per gestire le lambda, in particolare questa per elencare le lambda che ho dichiarato
```bash
aws lambda list-functions
```
E il seguente per lanciare tali lambda
```bash
aws lambda invoke --function-name [FUNCTION-NAME] --cli.binary-format raw-in-base64-out --payload '{...}'
```

### .NET
.NET offre una sua CLI dedicata per sviluppare con le funzioni lambda.
Per prima cosa è necessario installare `Amazon.Lambda.Tools`
```bash
dotnet tool install -g Amazon.Lambda.Tools
```
e poi lanciando il comando `dotnet lambda` si ottiene la lista delle operazioni che posso effettuare.
Per esempio se voglio invocare una lambda posso scrivere
```bash
dotnet lambda invoke-funcion [NomeFunzione] --payload '{}'
```
Questa CLI è più user-friendly e comoda rispetto a quella nativa di AWS, per cui è consigliata.
Inoltre è possibile installare i template per nuovi progetti .NET per iniziare a scrivere delle lambda con .NET
```bash
dotnet new -i Amazon.Lambda.Templates
```


## Triggers and Destinations
Una volta creata la lambda su AWS Console è possibile aggiungere tutti i trigger che devono lanciare tale funzione che le eventuali destinazioni.
I trigger sono fondamentali e si usano sempre, al contrario delle destinazioni.
Un trigger può essere qualsiasi cosa, da Alexa a fornitori esterni a risorse AWS come SQS, SNS e DynamoDb.
In base ai trigger che vogliamo la lambda deve avere i permessi per farlo, per esempio se vogliamo ascoltare uno stream da DynamoDb dobbiamo aggiungere nelle policy della lambda i permessi per leggere tale stream, in particolare il json:
```json
{
  "Sid": "APIAccessForDynamoDBStreams",
  "Effect": "Allow",
  "Action": [
    "dynamodb:GetRecords",
    "dynamodb:GetShardIterator",
    "dynamodb:DescribeStream",
    "dynamodb:ListStreams"
  ],
  "Resource": "arn:aws:dynamodb:eu-west-2:413211719643:table/customers/stream/*"
}
```

## .NET
Posso creare sia funzioni classiche da triggerare che un'API vera e propria. In questo ultimo caso l'API verrà caricata in un bucket S3 e verrà detta `serverless` (nei template si chiama `Lambda.Empty.Serverless`).
Per fare il deploy din una lambda posso usare il comando `dotnet lambda deploy-function [NOME]` mentre per eliminarla `dotnet lambda delete-function [NOME]`
In questo ultimo caso verrà fornito un URL da chiamare con metodo GET o POST che effettuerà delle cose.
Invece di  `deploy-function` posso usare `deploy-serverless` che è un comando che distribuisce un'intera applicazione serverless che può includere una o più funzioni AWS Lambda, endpoint API Gateway, risorse DynamoDB, S3 e così via.
Abbiamo quindi costruito sfruttando le lambda una REST API gestire effettivamente il server in cui questa ultima gira.

### Debugging

Per debug di una Lambda in locale con [**AWS Lambda Test Tool**](https://github.com/aws/aws-lambda-dotnet/tree/master/Tools/LambdaTestTool), prima assicurati che il tuo progetto abbia il pacchetto `Amazon.Lambda.TestTool-6.0` installato.
Installalo con 
```bash
dotnet tool install -g Amazon.Lambda.TestTool-9.0
```
Avvia il test tool con il comando:
```bash
dotnet lambda-test-tool-6.0
```
Questo avvierà un server locale, di default su `http://localhost:5050`, dove potrai testare la funzione Lambda inserendo input JSON direttamente nell'interfaccia web e visualizzando i risultati e i log.

Puoi aggiungere breakpoint nel codice Lambda e collegarti con Rider tramite **Debug > Attach to Process**, scegliendo il processo del test tool.
Un trucco per evitare l'attach di process è creare un nuovo `Edit Configuration` -> `.NET Executable` con: 
* `exe path` il path dove è stato installato il `lambda test tools`, tipicamente in `[utente]/.dotnet/tools/dotnet-lambda-test-tool-6,0.exe`
* `Working Directory`: il path dove sta il codice sorgente che voglio debuggare
* `Runtime`: .NET/.NET Core


In questo modo quando lancio tale configurazione viene lanciato automaticamente il browser da cui triggerare la richiesta.