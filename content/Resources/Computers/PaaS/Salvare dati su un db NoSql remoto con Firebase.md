---
tags:
  - PaaS
  - Firebase
  - ImagoLearning
Date: 2023-10-23
Done: false
---
Google Firebase permette di utilizzare un db NoSql sul cloud completamente black box gli utenti di una determinata applicazione o servizio.

## Firebase Realtime Database
Firebase Realtime Database è un servizio di database in tempo reale offerto da Firebase, una piattaforma di sviluppo di applicazioni mobile e web di proprietà di Google. Si tratta di un ==database cloud NoSQL che consente agli sviluppatori di creare applicazioni reattive e collaborative che possono sincronizzare e condividere dati in tempo reale tra diversi client==.

Il database è organizzato in modo gerarchico utilizzando una struttura ad albero di dati JSON (JavaScript Object Notation). Questo consente di organizzare i dati in un modo intuitivo e flessibile, rendendoli facili da leggere e scrivere. Le operazioni sul database come la lettura, la scrittura e l'aggiornamento dei dati possono essere effettuate in modo asincrono tramite API fornite da Firebase.

Firebase Realtime Database offre un sistema di sincronizzazione in tempo reale che permette a tutti i client connessi di ricevere automaticamente aggiornamenti in tempo reale quando i dati vengono modificati. Questo è particolarmente utile per applicazioni in cui è necessario visualizzare immediatamente i cambiamenti apportati dai diversi utenti.

L'autenticazione e l'autorizzazione sono integrate nel servizio, consentendo agli sviluppatori di definire regole di accesso basate su ruoli e autorizzazioni per proteggere i dati sensibili. Questo assicura che solo gli utenti autorizzati possano accedere e modificare i dati nel database.

Firebase Realtime Database offre anche funzionalità avanzate come le transazioni atomiche per garantire la coerenza dei dati in ambienti multithreading e multiutente. Le transazioni consentono di eseguire operazioni multiple in modo sicuro, garantendo che se una operazione fallisce, tutte le altre vengano annullate.

L'interfaccia utente per il database può essere personalizzata con Firebase SDK per diverse piattaforme, tra cui iOS, Android e il web. Inoltre, Firebase fornisce funzionalità di analisi e monitoraggio delle prestazioni, consentendo agli sviluppatori di ottenere insight sull'utilizzo del database e migliorare le prestazioni dell'applicazione.

Un altro vantaggio di Firebase Realtime Database è la scalabilità automatica, che significa che il servizio può gestire automaticamente picchi di traffico senza richiedere interventi manuali da parte degli sviluppatori. Questo assicura che l'applicazione rimanga affidabile e performante anche con un numero crescente di utenti.

## Creazione db
Per creare il database bisogna andare nel menu laterale `Build -> Realtime Database -> test mode`. 
Una volta fatto verrà fornito un url per poter accedere, tramite API al db.
![[Pasted image 20231005152842.png]]
Questo è l'unica cosa che serve per accedere al db dall'esterno, in test mode non serve nemmeno l'api key.

## Esempio

### Specifiche
In questo esempio ho  una Console Application che aggiunge ad un realtime database delle note che appartengono a uno o più notebook (stile Evernote).
In particolare posso
1. Creare un notebook
2. Creare una nota in un notebook (1)
3. Leggere una nota in un notebook (2)
4. Eliminare una nota in un notebook (3)
5. Eliminare un notebook (4).

La struttura del db sarà un Json come il seguente
```json
{
  "notebooks": {
    "test": {
      "Name": "test",
      "notes": {
        "nuova nota": {
          "Content": "nuova nota bellissima!!",
          "Title": "nuova nota"
        }
      }
    }
  }
}
```
![[Pasted image 20231005165350.png]]
### Codice
```c#
class Notebook  
{  
    public string Name { get; set; }  
}  
  
class Note  
{  
    public string Title { get; set; }  
    public string Content { get; set; }  
}  
  
class Program  
{  
    private const string FirebaseDatabaseUrl = "https://authentication-test-68caa-default-rtdb.europe-west1.firebasedatabase.app/";  
  
    private static readonly HttpClient Client = new HttpClient();  
  
    static async Task Main(string[] args)  
    {        while (true)  
        {            Console.WriteLine("Opzioni:");  
            Console.WriteLine("0. Creare un notebook");  
            Console.WriteLine("1. Creare una nota in un notebook");  
            Console.WriteLine("2. Leggere una nota in un notebook");  
            Console.WriteLine("3. Eliminare una nota in un notebook");  
            Console.WriteLine("4. Eliminare un notebook");  
            Console.Write("Scelta: ");  
  
            if (!int.TryParse(Console.ReadLine(), out var choice) || choice < 0 || choice > 4)  
            {                Console.WriteLine("Scelta non valida. Riprova.");  
                continue;  
            }  
            switch (choice)  
            {                case 0:  
                    await CreateNotebookAsync();  
                    break;  
                case 1:  
                    await CreateNoteAsync();  
                    break;  
                case 2:  
                    await ReadNoteAsync();  
                    break;  
                case 3:  
                    await DeleteNoteAsync();  
                    break;  
                case 4:  
                    await DeleteNotebookAsync();  
                    break;  
            }        }    }  
    private static async Task SendRequestAsync(string endpoint, string method, string content = null)  
    {        var request = new HttpRequestMessage(new HttpMethod(method), FirebaseDatabaseUrl + endpoint);  
        if (content != null)  
            request.Content = new StringContent(content);  
  
        var response = await Client.SendAsync(request);  
        response.EnsureSuccessStatusCode();  
    }  
    private static async Task CreateNotebookAsync()  
    {        Console.Write("Inserisci il nome del notebook: ");  
        var notebookName = Console.ReadLine();  
  
        var notebook = new Notebook { Name = notebookName };  
        var json = JsonConvert.SerializeObject(notebook);  
        await SendRequestAsync($"notebooks/{notebookName}.json", "PUT", json);  
  
        Console.WriteLine("Notebook creato con successo.");  
    }  
    private static async Task CreateNoteAsync()  
    {        Console.Write("Inserisci il nome del notebook: ");  
        var notebookName = Console.ReadLine();  
  
        Console.Write("Inserisci il titolo della nota: ");  
        var noteTitle = Console.ReadLine();  
  
        Console.Write("Inserisci il contenuto della nota: ");  
        var noteContent = Console.ReadLine();  
  
        var note = new Note { Title = noteTitle, Content = noteContent };  
        var json = JsonConvert.SerializeObject(note);  
        await SendRequestAsync($"notebooks/{notebookName}/notes/{noteTitle}.json", "PUT", json);  
  
        Console.WriteLine("Nota creata con successo.");  
    }  
    private static async Task ReadNoteAsync()  
    {        Console.Write("Inserisci il nome del notebook: ");  
        var notebookName = Console.ReadLine();  
  
        Console.Write("Inserisci il titolo della nota: ");  
        var noteTitle = Console.ReadLine();  
  
        var response = await Client.GetStringAsync($"{FirebaseDatabaseUrl}notebooks/{notebookName}/notes/{noteTitle}.json");  
        if (response != "null")  
        {            var note = JsonConvert.DeserializeObject<Note>(response);  
            Console.WriteLine("Nota trovata:");  
            Console.WriteLine($"Titolo: {note.Title}");  
            Console.WriteLine($"Contenuto: {note.Content}");  
        }        else  
        {  
            Console.WriteLine("Nota non trovata.");  
        }    }  
    private static async Task DeleteNoteAsync()  
    {        Console.Write("Inserisci il nome del notebook: ");  
        var notebookName = Console.ReadLine();  
  
        Console.Write("Inserisci il titolo della nota: ");  
        var noteTitle = Console.ReadLine();  
  
        await SendRequestAsync($"notebooks/{notebookName}/notes/{noteTitle}.json", "DELETE");  
        Console.WriteLine("Nota eliminata con successo.");  
    }  
    private static async Task DeleteNotebookAsync()  
    {        Console.Write("Inserisci il nome del notebook: ");  
        var notebookName = Console.ReadLine();  
  
        await SendRequestAsync($"notebooks/{notebookName}.json", "DELETE");  
        Console.WriteLine("Notebook eliminato con successo.");  
    }}
```