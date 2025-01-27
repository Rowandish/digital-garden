---
tags:
  - Coding
  - SOLID
  - PublishedPosts
---
Il principio di inversione delle dipendenze (DIP) è un principio di progettazione del software che mira a ==ridurre l'accoppiamento tra le classi e a promuovere una struttura di codice più modulare==. L'idea di base è quella di invertire le dipendenze tra classi ad alto e basso livello, in modo che entrambe ==dipendano da astrazioni invece che da implementazioni concrete==. Per astrazioni si intende **interfaccie** (anche le classi astratte sono astrazioni ma non sono mockabili facilmente rendendo il codice meno testabile).

Il DIP può essere sintetizzato in due asserzioni principali:

1. ==Le classi ad alto livello non dovrebbero dipendere dalle classi a basso livello==. Entrambe dovrebbero dipendere dalle astrazioni.
2. ==Le astrazioni non dovrebbero dipendere dai dettagli==. I dettagli dovrebbero dipendere dalle astrazioni.

## Perché è importante

Il DIP è importante perché aiuta a ridurre l'accoppiamento tra i moduli, migliorando la modularità, la manutenibilità e la testabilità del software.
Un alto grado di accoppiamento tra i moduli può portare a problemi come:

1. **Difficoltà nella manutenzione:** Quando i moduli sono strettamente accoppiati, modifiche in un modulo potrebbero richiedere cambiamenti in altri moduli, rendendo la manutenzione del software complessa e dispendiosa in termini di tempo.
2. **Ridotta testabilità:** I moduli strettamente accoppiati possono rendere difficile isolare e testare singole parti del software, poiché i test potrebbero richiedere la configurazione e l'esecuzione di numerosi moduli dipendenti.
3. **Rigidità nell'architettura:** Un'elevata dipendenza tra i moduli può rendere difficile la sostituzione o l'estensione di parti del software senza influenzare altri moduli, limitando la flessibilità dell'architettura.

Dipendendo dalle astrazioni anziché dalle implementazioni concrete, si promuove l'uso di dependency injection e di inversion of control (IoC) containers.
Ciò rende la tua codebase più adattabile alle modifiche, poiché puoi facilmente sostituire le implementazioni senza modificare le classi dipendenti.
DIP facilita anche migliori unit test, poiché le dipendenze possono essere facilmente mockate.

## Come applicarlo

Data una classe per applicare il principio basta rilevare quali sono le classi concrete che vengono utilizzate e sostituirle da interfacce che tipicamente vengono fornite a costruttore o tramite factory o automaticamente con [[Dependency Injection Framework]].
Tutto qui.
La classe risulterà così facilmente testabile in quanto il test creerà un mock per l'interfaccia e la passerà a costruttore della classe, modificando così il comportamento della stessa.
Se invece voglio cambiare il comportamento runtime posso, invece di passare l'oggetto a costruttore, passarlo tramite property (a patto che il suo tipo sia sempre un'astrazione) seguendo il pattern strategy.

## Limiti

1. **Complessità aggiuntiva**: L'applicazione del DIP può introdurre una complessità aggiuntiva nel sistema, poiché richiede la creazione di astrazioni (per separare le dipendenze tra classi di alto e basso livello.
2. **Sovraprogettazione**: Il DIP può portare alla sovraprogettazione se gli sviluppatori cercano di applicarlo in ogni situazione, anche quando non è strettamente necessario.

## Esempi

### Esempio 1

Ecco un esempio in C# per illustrare il concetto:

1.  Creiamo un'interfaccia per definire un'astrazione comune:

```csharp
// Interfaccia che rappresenta un generico servizio di notifica
public interface INotificationService
{
    // Metodo per inviare una notifica
    void SendNotification(string message);
}
```

2.  Implementiamo l'interfaccia con classi concrete:
```csharp
// Implementazione concreta del servizio di notifica tramite email
public class EmailNotificationService : INotificationService
{
    public void SendNotification(string message)
    {
        // Logica per inviare l'email con il messaggio
    }
}

// Implementazione concreta del servizio di notifica tramite SMS
public class SmsNotificationService : INotificationService
{
    public void SendNotification(string message)
    {
        // Logica per inviare l'SMS con il messaggio
    }
}
```

3.  Creiamo una classe ad alto livello che utilizzi il servizio di notifica:

```csharp
// Classe ad alto livello che rappresenta un'applicazione
public class Application
{
    // Dipendiamo dall'interfaccia, non dalle implementazioni concrete
    private readonly INotificationService _notificationService;

    // Usiamo l'iniezione di dipendenza per passare un'implementazione concreta dell'interfaccia
    public Application(INotificationService notificationService)
    {
        _notificationService = notificationService;
    }

    // Metodo che utilizza il servizio di notifica
    public void NotifyUser(string message)
    {
        _notificationService.SendNotification(message);
    }
}

```

4.  Infine, nel nostro programma principale, creiamo un'istanza della classe Application e passiamo un'implementazione concreta del servizio di notifica:

```csharp
public static void Main()
{
    // Creiamo un'istanza del servizio di notifica via email
    INotificationService emailNotificationService = new EmailNotificationService();

    // Creiamo un'istanza dell'applicazione e passiamo il servizio di notifica desiderato
    Application app = new Application(emailNotificationService);

    // Usiamo il metodo NotifyUser per inviare una notifica
    app.NotifyUser("Ciao, questo è un messaggio di prova!");
}
```

In questo esempio, abbiamo seguito il Dependency Inversion Principle creando un'interfaccia comune `INotificationService` e facendo **dipendere la classe ad alto livello `Application` dall'interfaccia, invece che dalle implementazioni concrete**. Inoltre, abbiamo utilizzato l'iniezione di dipendenza per passare un'implementazione concreta dell'interfaccia alla classe `Application`.

### Esempio 2

```csharp
// Violates DIP
public class User
{
    private SqlContext _context;

    public User(SqlContext context)
    {
        _context = context;
    }

    public void Add(string userName)
    {
        _context.AddUser(userName);
    }
}

// Adheres to DIP
public interface IContext
{
    void AddUser(string userName);
}

public class SqlContext : IContext
{
    public void AddUser(string userName)
    {
        // Add user to SQL database
    }
}

public class User
{
    private IContext _context;

    public User(IContext context)
    {
        _context = context;
    }

    public void Add(string userName)
    {
        _context.AddUser(userName);
    }
}
```