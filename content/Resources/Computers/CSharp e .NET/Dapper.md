---
tags:
  - Dometrain
---
Questa nota prende a piene mani dal corso [From Zero to Hero: Dapper in .NET](https://dometrain.com/course/from-zero-to-hero-dapper-in-dotnet/).
## Introduzione
### Cos’è un ORM?

Un **ORM (Object Relational Mapper)** è una libreria che permette di lavorare con un database relazionale tramite oggetti e classi C#, evitando di scrivere direttamente SQL per ogni operazione.  
Esempi: **Entity Framework**, **NHibernate**.
Con un ORM completo:
- le entità C# vengono mappate automaticamente sulle tabelle del DB,
- le query possono essere scritte in LINQ,
- vengono gestiti **tracking delle entità**, **migrations**, **validazioni**, ecc.
### Cos’è un _Micro ORM_?
Un **micro ORM** è una versione “leggera” di ORM: non gestisce tutte le funzionalità avanzate (change tracking, migrations, ecc.), ma si concentra sulle **operazioni di mapping veloce** tra oggetti e database.
**Dapper** è il micro ORM più diffuso in .NET:
- Estende `IDbConnection` con metodi di estensione (`Query`, `Execute`, ecc.).
- Mappa automaticamente i risultati di query SQL su oggetti C#.
- Non sostituisce SQL → lo sviluppatore deve scrivere query, ma con mappatura e performance estremamente veloci.
### Quando usare **Dapper**
- Quando hai bisogno di **massime performance** (è uno dei più veloci in assoluto).
- Quando **controlli tu le query SQL** e non ti serve un motore che le generi al posto tuo.
- In contesti **data-centric** o microservizi dove le entità sono semplici DTO.
- Quando non serve gestire lo **state tracking** (libreria “stateless”).
Esempio tipico: API che devono fare molte query veloci e ottimizzate.
### Quando usare Entity Framework
- Quando preferisci lavorare con **LINQ** invece di SQL puro.
- Quando hai bisogno di funzionalità avanzate come:
    - **Change Tracking** → rilevare le modifiche sugli oggetti e generare automaticamente UPDATE/DELETE.
    - **Code First Migrations** → gestione dello schema DB tramite codice.
    - **Lazy Loading / Eager Loading** per la gestione delle relazioni.
- Quando lo **sviluppo rapido** e la produttività contano più delle prestazioni pure.
Esempio tipico: applicazioni business complesse con molte relazioni e necessità di astrazione dal DB.
## Cheat-Sheet

- **`Execute` / `ExecuteAsync`** → esegue un comando SQL (`INSERT/UPDATE/DELETE`) e ritorna il numero di righe interessate.
- **`ExecuteScalar<T>` / `ExecuteScalarAsync<T>`** → esegue un comando SQL o una `SELECT` e ritorna il valore della **prima colonna della prima riga** (es. `COUNT(*)`).
- **`Query<T>` / `QueryAsync<T>`** → esegue una `SELECT` e ritorna una collezione di oggetti `T` (anche vuota se nessun record).
- **`QuerySingle<T>` / `QuerySingleAsync<T>`** → ritorna **esattamente una riga**; eccezione se 0 o più di 1.
- **`QuerySingleOrDefault<T>` / `QuerySingleOrDefaultAsync<T>`** → ritorna **una riga o default/null** se nessuna; eccezione se più di 1.
- **`QueryFirst<T>` / `QueryFirstAsync<T>`** → ritorna la **prima riga**; eccezione se nessuna.
- **`QueryFirstOrDefault<T>` / `QueryFirstOrDefaultAsync<T>`** → ritorna la **prima riga o default/null** se nessuna.
- **`QueryMultiple` / `QueryMultipleAsync`** → esegue una query che produce più `ResultSet` e permette di leggerli separatamente.
## Reader
Il reader permette di avere una specie di `Cursor` che itera su tutte le righe ottenute da una query di `SELECT`. Questo permette di avere più controllo sull'operazione e può avere senso quando voglio precisione, velocità e controllo avanzato.
In particolare per:
* **Custom mapping**: ho dei dati dinamici e il mapping automatico di Dapper non è sufficiente.
* **Performance**: il mapping automatico di Dapper utilizza le reflection che possono essere lente: se ho una query di cui ho la necessità di ottimizzare al massimo le performance posso usare un reader per evitare le reflection
* **Streaming dei dati**: possono esserci casi in cui devo caricare un enorme set di dati e non voglio caricarli tutti nella ram ma utilizzarli al bisogno
* **Risultati multipli**: posso avere delle Stored Procedure che ritornano più di un set di risultati 
Svantaggi:
* Maggiore complessità
* Gestione manuale dei null
* Gestione manuale dell'ordine di ogni colonna
* Conversione manuale dei tipi di dato
## Gestire relazioni in JOIN
Assumiamo di avere una tabella `Order` a cui sono associati *n* oggetti `Items`.
In SQL ottengo questa cosa con una classica query di `JOIN` che “appiattisce” padre + figli in righe ripetute:
```sql
SELECT 
  o.Id, o.Numero, o.Data,             -- campi dell'Order (padre)
  i.Id, i.OrderId, i.Sku, i.Qta       -- campi dell'Item (figlio)
FROM Orders o
LEFT JOIN OrderItems i ON i.OrderId = o.Id
WHERE o.Id = @orderId
ORDER BY o.Id, i.Id;
```
L'obiettivo è usare Dapper per popolare due entity di questo tipo
```csharp
public class Order
{
    public int Id { get; set; }
    public string Numero { get; set; }
    public DateTime Data { get; set; }

    // relazione 1 → N
    public List<OrderItem> Items { get; set; } = new ();
}

public class OrderItem
{
    public int Id { get; set; }
    public int OrderId { get; set; }
    public string Sku { get; set; }
    public int Qta { get; set; }
}
```

Questo avviene con il multi-mapping integrato nella funzione `QueryAsync` con il parametro `splitOn`: questo dice a Dapper **da quale colonna inizia il nuovo oggetto** nella riga risultante.  
Qui il primo blocco di colonne è l’**Order**, il secondo è l’**Item**; lo split avviene sul **primo Id del secondo oggetto** (`i.Id`):

```csharp
var sql = @"SELECT o.Id, o.Numero, o.Data,
                   i.Id, i.OrderId, i.Sku, i.Qta
            FROM Orders o
            LEFT JOIN OrderItems i ON i.OrderId = o.Id
            WHERE o.Id = @orderId
            ORDER BY o.Id, i.Id;";

using var conn = new SqlConnection(cs);

var lookup = new Dictionary<int, Order>(); // per consolidare i figli

// Primo parametro: classe padre. Secondo: classe associata. Terzo: dove rimappo, quindi nella classe padre.
var orders = await conn.QueryAsync<Order, OrderItem, Order>(
    sql,
    (o, i) =>
    {
        if (!lookup.TryGetValue(o.Id, out var agg))
        {
            agg = o;
            agg.Items = new List<OrderItem>();
            lookup.Add(agg.Id, agg);
        }
        if (i != null && i.Id != 0) // con LEFT JOIN potrebbe non esserci figlio
            agg.Items.Add(i);
        return agg; // ignorato, usiamo lookup.Values
    },
    new { orderId },
    splitOn: "Id" // è l'Id del *secondo* tipo mappato (OrderItem.Id)
);

var order = lookup.Values.Single();
```

### Tips & Tricks
- Se hai più livelli (`Order`, `Customer`, `Item`) useresti `splitOn: "CustomerId,Id"` (Customer comincia su `CustomerId`, Item su `Id`).    
- Dapper di default usa `"Id"` come punto di split se non specifichi; **non affidarti al default** quando i nomi non sono standard.
- **Ordina** per chiave padre (e poi figlio) per migliori performance di streaming.    
- Usa `LEFT JOIN` se i figli sono opzionali (e filtra `i != null`).    
- Evita SELECT `*`: sii esplicito sull’ordine delle colonne.    
- Per insiemi grandi, valuta `buffered: false` per stream    
- Se devi deduplicare proprietà calcolate/complessità, il **`lookup`** è il modo giusto: ogni riga “arricchisce” lo stesso oggetto padre.

## Unbuffered
Dapper, oltre alla modalità standard di lettura dei dati, supporta anche una modalità **unbuffered** che può essere abilitata passando `buffered: false` ai metodi `Query`.
Per default, quando esegui una query con Dapper (`connection.Query<T>(...)`), i risultati vengono **caricati interamente in memoria** (buffered) in una lista prima di essere restituiti. Con `buffered: false`, invece, i risultati vengono **streammati uno alla volta** man mano che il `DataReader` legge dal database.
In pratica, ottieni un **`IEnumerable<T>` “lazy”** che produce record mentre scorri la collezione, senza caricare tutto subito in memoria.
### Quando si utilizza
- Quando ci si aspetta un **numero molto grande di righe** e non è pratico/possibile caricarle tutte in RAM.
- Quando serve iniziare ad elaborare i dati **subito** mentre la query è ancora in corso (pipeline processing).
- In scenari batch o ETL dove i dati vanno consumati progressivamente (es. scrittura su file, trasformazioni a blocchi, ecc.).

Esempio:
```csharp
using (var connection = new SqlConnection(connectionString))
{
    var sql = "SELECT * FROM BigTable";
    
    // Risultati in streaming (unbuffered)
    var rows = connection.Query<MyEntity>(sql, buffered: false);

    foreach (var row in rows)
    {
        // Elaboro i record uno alla volta
        Process(row);
    }
}
```

### Pro e contro

#### Vantaggi
- **Riduce l’uso di memoria** → non viene caricata tutta la result set in RAM.
- **Permette di elaborare stream di dati enormi** che altrimenti saturerebbero la memoria.
- **Risposta immediata** → puoi iniziare ad elaborare i risultati senza aspettare che la query termini del tutto.
#### Svantaggi
- **Connessione aperta più a lungo**: finché non hai finito di enumerare i risultati, la connessione rimane occupata.
- **Una sola enumerazione**: essendo un `IEnumerable<T>` lazy, non puoi scorrerlo più volte senza riallacciare al DB.
- **Maggiore fragilità**: se il consumer dimentica di enumerare fino in fondo o interrompe bruscamente, la connessione rimane occupata.
- **Prestazioni diverse**: per dataset piccoli/medi conviene il buffering perché il caricamento unico è più rapido.

## Dapper Plus
Dapper Plus (**DapperPlus** o **Z.Dapper.Plus**) è una libreria commerciale della **Z.EntityFramework Extensions** che estende [Dapper](https://github.com/DapperLib/Dapper) aggiungendo funzionalità avanzate per la manipolazione dei dati ad alte prestazioni, in particolare operazioni di **Bulk** (insert, update, delete, merge/upsert).
E' gratuito per testare ma a pagamento a livello commerciale.
Il vantaggio principale è che consente di eseguire operazioni in massa su un database **molto più velocemente** rispetto all’uso di INSERT/UPDATE multipli tramite Dapper puro, sfruttando internamente tecniche ottimizzate e `SqlBulkCopy` (per SQL Server).
Supporta vari provider (SQL Server, MySQL, PostgreSQL, Oracle, ecc.).
Per usare DapperPlus con le entità, è necessario dichiarare il **mapping** tra la classe C# e la tabella del database. Questo si fa tipicamente all’avvio dell’applicazione, così DapperPlus sa come mappare correttamente le proprietà con le colonne.
```csharp
// Mapping tra entità e tabella
DapperPlusManager.Entity<Customer>().Table("Customers");
// E' possibile specificare la chiave primaria
DapperPlusManager.Entity<Customer>().Table("Customers").Key(x => x.CustomerID);
```
### Funzionalità principali
- **BulkInsert** → inserisce rapidamente molte entità.
- **BulkUpdate** → aggiorna molte entità in una sola chiamata.
- **BulkMerge (Upsert)** → inserisce nuove righe e aggiorna quelle esistenti.
- **BulkDelete** → cancella in massa.

### Esempi di utilizzo

#### Bulk Insert
```csharp
using (var connection = new SqlConnection(connectionString))
{
    var customers = new List<Customer>
    {
        new Customer { Name = "Mario" },
        new Customer { Name = "Luigi" }
    };

    connection.BulkInsert(customers);
}
```

#### Bulk Update
```csharp
using (var connection = new SqlConnection(connectionString))
{
    var customers = GetCustomersFromSomewhere();
    customers.ForEach(c => c.Name += " (Updated)");

    connection.BulkUpdate(customers);
}
```

#### Bulk Merge (Upsert)
```csharp
using (var connection = new SqlConnection(connectionString))
{
    var customers = new List<Customer>
    {
        new Customer { CustomerID = 1, Name = "Mario Rossi" }, // esistente → update
        new Customer { CustomerID = 0, Name = "Nuovo Cliente" } // nuovo → insert
    };

    connection.BulkMerge(customers);
}
```

## Tips & tricks
* Puoi passare direttamente una `List<T>` a `ExecuteAsync` con parametri nominati → Dapper esegue un `INSERT` per ogni oggetto.  Non è un vero bulk insert: genera tanti comandi quanti sono gli elementi.  