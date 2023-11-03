---
tags:
  - Azure
  - PaaS
  - ImagoLearning
Date: 2023-11-06
Done: false
---
Azure Storage Account è una  [[Resource - Azure|resource]] che consente di archiviare in modo flessibile e affidabile un'ampia varietà di dati, inclusi file, tabelle, code e oggetti binari, in modo scalabile ed economicamente efficiente.
È progettata per supportare applicazioni e carichi di lavoro diversificati, offrendo allo stesso tempo una robusta sicurezza e un elevato livello di disponibilità. 
## Caratteristiche
1. **Multi-Protocol Support**: Una Storage Account di Azure supporta più protocolli come HTTP, HTTPS e SMB (Server Message Block), consentendo agli sviluppatori di accedere e gestire i dati in vari modi a seconda delle esigenze dell'applicazione.
2. **Scalabilità e Performance**: La Storage Account di Azure offre una scalabilità incredibile, consentendo di aumentare o diminuire le risorse di archiviazione e di elaborazione in modo dinamico per adattarsi ai cambiamenti nei carichi di lavoro. Ciò assicura alte prestazioni anche con un aumento significativo del traffico dati.
3. **Ridundanza e Affidabilità**: Azure Storage Account garantisce la ridondanza e l'affidabilità dei dati mediante la replica automatica delle informazioni tra più data center all'interno di una regione o addirittura su diverse regioni. Ciò riduce il rischio di perdita di dati e assicura la disponibilità continua.
4. **Sicurezza avanzata**: La Storage Account di Azure offre funzionalità di sicurezza avanzate come l'autenticazione basata su token, la crittografia dei dati in transito e a riposo, l'accesso condizionale e il controllo degli accessi in base al ruolo (RBAC), garantendo la protezione dei dati sensibili.
5. **Integrazione con Altri Servizi**: La Storage Account di Azure si integra senza problemi con altri servizi di Azure, come Azure Functions, Azure Logic Apps, Azure Machine Learning, consentendo la creazione di soluzioni complesse e scalabili.
6. **Tipi di Archiviazione**: Azure Storage Account offre diverse opzioni per l'archiviazione dei dati, tra cui:
   - **Blob Storage**: Per l'archiviazione di oggetti e file di grandi dimensioni.
   - **File Storage**: Per la condivisione di file in modo semplice e scalabile utilizzando il protocollo SMB.
   - **Table Storage**: Per l'archiviazione di dati strutturati in una tabella non relazionale.
   - **Queue Storage**: Per la gestione delle code e la comunicazione asincrona tra i componenti dell'applicazione.
7. **Costi Flessibili**: Azure Storage Account offre opzioni di prezzi flessibili, tra cui il pagamento in base al consumo, che consente di pagare solo per le risorse effettivamente utilizzate.
8. **Strumenti di Gestione e Monitoraggio**: Azure fornisce strumenti e portali di gestione centralizzati che consentono di monitorare le prestazioni, gestire l'accesso e il controllo degli utenti, nonché ottimizzare l'utilizzo delle risorse.

## Tipologie di container

All'interno di una Azure Storage Account, è possibile creare e gestire diversi tipi di container: i container sono strutture di alto livello utilizzate per organizzare e separare i dati in base ai diversi scopi e utilizzi.

### Blob Container
Il Blob Container è uno dei tipi di container più comuni in Azure Storage. È progettato per archiviare oggetti di grandi dimensioni, noti come "blob" (binary large objects). Questi blob possono essere file di immagini, video, documenti, backup o qualsiasi altro tipo di dati binari. I blob possono essere accessibili tramite HTTP/HTTPS e supportano tre tipi di accesso: pubblico, privato o condiviso con firma dell'account. I blob possono essere organizzati all'interno dei container utilizzando una struttura ad albero di directory.

### File Share
Il File Share è un tipo di container progettato per consentire la condivisione di file tra diverse macchine virtuali, servizi e applicazioni. Funziona come un sistema di file tradizionale, consentendo l'accesso tramite il protocollo SMB (Server Message Block). È particolarmente utile quando è necessario condividere dati tra macchine virtuali, creare un ambiente di condivisione dei file distribuito o supportare applicazioni legacy che richiedono accesso ai file tramite SMB.

### Table
Il Table Container è un tipo di container utilizzato per l'archiviazione di grandi quantità di dati non strutturati, organizzati in tabelle. Ogni tabella può contenere un numero elevato di entità (righe), ognuna con un insieme di proprietà (colonne). Questa struttura è ottimizzata per query veloci e distribuite su grandi volumi di dati. È particolarmente adatto per applicazioni che richiedono un modello di dati flessibile, scalabile e senza schema fisso.

### Queue
Il Queue Container è un tipo di container utilizzato per implementare code di messaggi. Le code consentono la comunicazione asincrona tra i diversi componenti di un'applicazione. È possibile inserire messaggi in una coda da un'applicazione e elaborarli in modo separato da un'altra. Questo modello è ampiamente utilizzato per implementare processi di lavorazione dei messaggi o per garantire la scalabilità e la resistenza dei sistemi distribuiti.

## Gestione dei container
Per poter creare un container per prima cosa creiamo una risorsa di tipo "Storage Account", poi andiamo su Container e creiamone uno nuovo.
Per fase di test è comodo che sia pubblicamente visibile dall'esterno, quindi impostiamo su "allow anonymous users" a true e creiamolo public.
### Url
Ogni container è contraddistinto da un URL, che è comodo per poterci accedere tramite API.
Per accedere all'URL di un Container, una volta creato, andare sulle sue property in questo modo
![[Pasted image 20231013171151.png]]
e copiarsi l'url
![[Pasted image 20231013171207.png]]


## Script

Questa console application è progettata per interagire con un account di archiviazione di Azure attraverso l'utilizzo delle librerie Microsoft.Azure.Storage e Microsoft.Azure.Storage.Blob.
L'utente può scegliere tra quattro azioni principali: caricare un file, eliminare un file, scaricare un file o uscire dall'applicazione.

1. **Upload File**: Consente all'utente di caricare un file nel container denominato "notes" all'interno dell'account di archiviazione di Azure. L'utente inserisce il nome e il contenuto del file, che vengono quindi caricati come un blob nel container.
2. **Delete File**: Permette all'utente di eliminare un file specifico dal container "notes" nel suo account di archiviazione di Azure. L'utente fornisce il nome del file da eliminare, e se esiste, il blob corrispondente viene rimosso dal container.
3. **Download File**: Consente all'utente di scaricare un file specifico dal container "notes" nell'account di archiviazione di Azure. L'utente fornisce il nome del file da scaricare, e se esiste, il blob corrispondente viene scaricato e salvato sul desktop dell'utente.
4. **Exit**: Permette all'utente di uscire dall'applicazione.

```c#
using System.Text;  
using Microsoft.Azure.Storage;  
using Microsoft.Azure.Storage.Blob;  
  
// Questa stringa si trova in Resource -> Access Keys -> Connection string  
const string storageConnectionString = "DefaultEndpointsProtocol=https;AccountName=st0r4geaccountt3st;AccountKey=Vy1PPN4c3uqIAcxbcozmn5cHTYKVSy5Bx7sSgRskd5FY+gzPCR2w+yrF9IE2q3ZRzwuyG+EiHO/A+AStwkMXqg==;EndpointSuffix=core.windows.net";  
var exitRequested = false;  
while (!exitRequested)  
{  
    Console.WriteLine("Choose an action:");  
    Console.WriteLine("1. Upload file");  
    Console.WriteLine("2. Delete file");  
    Console.WriteLine("3. Download file");  
    Console.WriteLine("4. Exit");  
    Console.Write("Enter your choice: ");  
  
    if (int.TryParse(Console.ReadLine(), out var choice))  
    {        switch (choice)  
        {            case 1:  
                Console.Write("Enter the file name: ");  
                var fileName = Console.ReadLine();  
  
                Console.Write("Enter the content: ");  
                var content = Console.ReadLine();  
  
                if (fileName != null && content != null)  
                    await UploadTextToBlobAsync(fileName, content);  
                break;  
            case 2:  
                Console.Write("Enter the file name to delete: ");  
                var fileToDelete = Console.ReadLine();  
  
                if (fileToDelete != null)  
                    await DeleteBlobAsync(fileToDelete);  
                break;  
            case 3:  
                Console.Write("Enter the file name to download: ");  
                var fileToDownload = Console.ReadLine();  
  
                if (fileToDownload != null)  
                {                    var desktopPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop),  
                        fileToDownload);                    await DownloadBlobAsync(fileToDownload, desktopPath);  
                }  
                break;  
            case 4:  
                exitRequested = true;  
                break;  
            default:  
                Console.WriteLine("Invalid choice. Please choose 1, 2 or 3.");  
                break;  
        }    }    else  
    {  
        Console.WriteLine("Invalid input. Please enter a valid numeric choice.");  
    }
}  
  
return;  
  
  
async Task UploadTextToBlobAsync(string fileName, string content)  
{  
    try  
    {  
        // Retrieve storage account from connection string.  
        var storageAccount = CloudStorageAccount.Parse(storageConnectionString);  
  
        // Create the blob client.  
        var blobClient = storageAccount.CreateCloudBlobClient();  
  
        // Get a reference to the container.  
        var container = blobClient.GetContainerReference("notes");  
  
        // Create the container if it doesn't exist.  
        await container.CreateIfNotExistsAsync();  
  
        // Set the permissions so the blobs are public.  
        var containerPermissions = new BlobContainerPermissions  
        {  
            PublicAccess = BlobContainerPublicAccessType.Container  
        };  
        await container.SetPermissionsAsync(containerPermissions);  
  
        // Get a reference to the blob.  
        var blockBlob = container.GetBlockBlobReference(fileName);  
  
        // Convert the content to bytes.  
        var contentBytes = Encoding.UTF8.GetBytes(content);  
  
        // Upload the content as a stream.  
        using (var stream = new MemoryStream(contentBytes))  
        {            await blockBlob.UploadFromStreamAsync(stream);  
        }  
        Console.WriteLine($"File uploaded successfully to: {blockBlob.Uri}");  
    }    catch (Exception ex)  
    {        Console.WriteLine($"An error occurred: {ex.Message}");  
    }
}  
  
async Task DownloadBlobAsync(string fileName, string destinationPath)  
{  
    try  
    {  
        // Retrieve storage account from connection string.  
        var storageAccount = CloudStorageAccount.Parse(storageConnectionString);  
  
        // Create the blob client.  
        var blobClient = storageAccount.CreateCloudBlobClient();  
  
        // Get a reference to the container.  
        var container = blobClient.GetContainerReference("notes");  
  
        // Get a reference to the blob.  
        var blockBlob = container.GetBlockBlobReference(fileName);  
  
        if (await blockBlob.ExistsAsync())  
        {            // Download the blob to the specified destination path.  
            await blockBlob.DownloadToFileAsync(destinationPath, FileMode.Create);  
            Console.WriteLine($"File downloaded successfully to: {destinationPath}");  
        }        else  
        {  
            Console.WriteLine("Blob not found.");  
        }    }    catch (Exception ex)  
    {        Console.WriteLine($"An error occurred: {ex.Message}");  
    }
}  
  
  
async Task DeleteBlobAsync(string blobName)  
{  
    try  
    {  
        // Retrieve storage account from connection string.  
        var storageAccount = CloudStorageAccount.Parse(storageConnectionString);  
  
        // Create the blob client.  
        var blobClient = storageAccount.CreateCloudBlobClient();  
  
        // Get a reference to the container.  
        var container = blobClient.GetContainerReference("notes");  
  
        // Get a reference to the blob.  
        var blockBlob = container.GetBlockBlobReference(blobName);  
  
        if (await blockBlob.ExistsAsync())  
        {            await blockBlob.DeleteAsync();  
            Console.WriteLine("Blob deleted successfully.");  
        }        else  
        {  
            Console.WriteLine("Blob not found.");  
        }    }    catch (Exception ex)  
    {        Console.WriteLine($"An error occurred: {ex.Message}");  
    }
}
```