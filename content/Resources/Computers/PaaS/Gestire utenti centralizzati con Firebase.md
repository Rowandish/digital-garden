---
tags:
  - PaaS
  - Firebase
  - ImagoLearning
Date: 2024-05-20
Done: true
---
Google Firebase permette di gestire sul cloud gli utenti di una determinata applicazione o servizio.
In questo modo si delega tutta la parte di salvataggio utenti, recupero pwd, blocchi e analytics.

## Cosa è Firebase Authentication
Firebase Authentication è uno dei servizi principali offerti dalla piattaforma Firebase di Google. Si tratta di un servizio di autenticazione completamente gestito che semplifica l'implementazione dell'accesso e della registrazione degli utenti all'interno delle applicazioni, sia per le piattaforme web che per quelle mobile.

Ecco alcuni aspetti chiave di Firebase Authentication:

1. **Diversi metodi di autenticazione**: Firebase Authentication offre vari metodi per l'autenticazione degli utenti, tra cui email e password, autenticazione tramite account Google, autenticazione tramite account Facebook, autenticazione tramite telefono, autenticazione tramite Twitter e altro ancora.
2. **Integrazione semplice**: L'integrazione di Firebase Authentication è semplice e richiede solo pochi passaggi. Gli sviluppatori possono utilizzare SDK dedicati per diverse piattaforme (iOS, Android, web) e fornire una UI di autenticazione predefinita o personalizzata.
3. **Sicurezza**: Firebase Authentication garantisce la sicurezza dell'autenticazione e della gestione delle credenziali degli utenti. Utilizza tecniche di crittografia avanzate e migliori pratiche di sicurezza per proteggere le informazioni sensibili degli utenti.
4. **Recupero delle credenziali**: Firebase Authentication fornisce funzionalità per il recupero delle credenziali degli utenti, consentendo agli utenti di reimpostare la password o recuperare l'accesso all'account in caso di smarrimento delle credenziali.
5. **Gestione utenti**: Gli sviluppatori possono gestire gli utenti registrati, visualizzarne i dettagli, effettuare azioni come il reset della password o la disabilitazione dell'account direttamente dalla console Firebase.
6. **Accesso con un solo clic**: Firebase Authentication supporta l'accesso con un solo clic attraverso l'utilizzo di account social (come Google, Facebook, Twitter) o altre opzioni di autenticazione senza la necessità di inserire manualmente una password.
7. **Integrazione con altri servizi Firebase**: Firebase Authentication può essere facilmente integrato con altri servizi Firebase, consentendo una gestione centralizzata degli utenti e consentendo l'accesso a funzionalità avanzate come l'autorizzazione basata su ruoli.
8. **Monitoraggio delle attività degli utenti**: È possibile monitorare e registrare le attività degli utenti, come i tentativi di accesso e le modifiche alle credenziali, per garantire una maggiore sicurezza e controllo.


## Creare un progetto
Per prima cosa è necessario creare un generico progetto Firebase, questo progetto comprende non solo l'autenticazione ma anche la gestione di database, analytics e varie altre funzionalità.
Una volta creato un progetto andiamo su Authentication -> Sign-in method e abilitiamo quello che ci serve, per esempio il classico "Email/Password".
In questo modo servizio permette di autenticare gli utenti nel modo classico, poi ci sono anche altre modalità come autenticazione con cloud e così via.
Un elemento fondamentale è l'API KEY, che servirà al servizio che andremo a costruire per autenticarsi.
Questa la trovo in `Project Overview -> Project settings -> Web API Key`.
![[Pasted image 20231005122539.png]]
Per capire quali sono le API da utilizzare posso leggere la documentazione che si trova [qui](https://firebase.google.com/docs/reference/rest/auth?hl=en) dove ci sono tutti gli url da chiamare per registrare un nuovo utente, fare login e così via.
Il metodo più semplice è autenticazione con email e password e l'url è il seguente
```
https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=[API_KEY]
```
passandogli come body `email`, `password` e `returnSecureToken=true`.
```json
{
  "idToken": "[ID_TOKEN]",
  "email": "[user@example.com]",
  "refreshToken": "[REFRESH_TOKEN]",
  "expiresIn": "3600",
  "localId": "tRcfmLH7..."  
}
```

## Script
Di seguito un semplice script che descrive come utilizzare i semplici metodi di login e signup.
```c#
using System;  
using System.Net.Http;  
using System.Text;  
using System.Threading.Tasks;  
using Newtonsoft.Json;  
  
public class Program  
{  
    public const string FirebaseApiKey = "AIzaSyA_Aj_KkpUz73JyobvL689IElSd7Ioi2ag";  
  
    public static async Task Main(string[] args)  
    {        while (true)  
        {            Console.WriteLine("Benvenuto! Scegli un'opzione:");  
            Console.WriteLine("0. Login");  
            Console.WriteLine("1. Signup");  
            Console.WriteLine("2. Esci");  
  
            var choice = Console.ReadLine();  
  
            switch (choice)  
            {                case "0":  
                    await LoginAsync();  
                    break;  
                case "1":  
                    await SignupAsync();  
                    break;  
                case "2":  
                    return;  
                default:  
                    Console.WriteLine("Opzione non valida. Riprova.");  
                    break;  
            }        }    }  
    private static async Task LoginAsync()  
    {        Console.Write("Email: ");  
        var email = Console.ReadLine();  
        Console.Write("Password: ");  
        var password = Console.ReadLine();  
  
        try  
        {  
            var localId = await FirebaseAuthentication.LoginAsync(email, password);  
            Console.WriteLine($"Login avvenuto con successo per l'utente {email} (localId: {localId})");  
            Console.WriteLine("Premi un tasto per fare logout.");  
            Console.ReadKey();  
        }        catch (Exception ex)  
        {            Console.WriteLine($"Errore durante il login: {ex.Message}");  
        }    }  
    private static async Task SignupAsync()  
    {        Console.Write("Email: ");  
        var email = Console.ReadLine();  
        Console.Write("Password: ");  
        var password = Console.ReadLine();  
  
        try  
        {  
            await FirebaseAuthentication.RegisterAsync(email, password);  
            Console.WriteLine("Registrazione avvenuta con successo!");  
        }        catch (Exception ex)  
        {            Console.WriteLine($"Errore durante la registrazione: {ex.Message}");  
        }    }}  
  
public static class FirebaseAuthentication  
{  
    private static readonly HttpClient client = new();  
  
    public static async Task<string> LoginAsync(string email, string password)  
    {        var payload = BuildPayload(email, password);  
        return await SendRequestAsync("signInWithPassword", payload);  
    }  
    public static async Task<string> RegisterAsync(string email, string password)  
    {        var payload = BuildPayload(email, password);  
        return await SendRequestAsync("signUp", payload);  
    }  
    private static object BuildPayload(string email, string password)  
    {        return new  
        {  
            email,            password,            returnSecureToken = true  
        };  
    }  
    private static async Task<string> SendRequestAsync(string endpoint, object payload)  
    {        var content = new StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json");  
        var response = await client.PostAsync($"https://identitytoolkit.googleapis.com/v1/accounts:{endpoint}?key={Program.FirebaseApiKey}", content);  
  
        if (response.IsSuccessStatusCode)  
        {            var resultJson = await response.Content.ReadAsStringAsync();  
            var result = JsonConvert.DeserializeObject<FirebaseResult>(resultJson);  
            return result.localId;  
        }  
        var errorJson = await response.Content.ReadAsStringAsync();  
        var error = JsonConvert.DeserializeObject<FirebaseError>(errorJson);  
        throw new Exception(error.error.message);  
    }}  
  
public class FirebaseResult  
{  
    public string kind { get; set; }  
    public string idToken { get; set; }  
    public string email { get; set; }  
    public string refreshToken { get; set; }  
    public string expiresIn { get; set; }  
    public string localId { get; set; }  
}  
  
public class ErrorDetails  
{  
    public int code { get; set; }  
    public string message { get; set; }  
}  
  
public class FirebaseError  
{  
    public ErrorDetails error { get; set; }  
}
```
