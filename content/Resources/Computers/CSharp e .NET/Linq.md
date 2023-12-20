---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


LINQ (Language-Integrated Query) rappresenta un set di funzionalità introdotto in Visual Studio 2008 che migliora la gestione delle query nella sintassi dei linguaggi C# e Visual Basic.
## Select
```c#
int[] numbers = new int[7] { 0, 1, 2, 3, 4, 5, 6 };
var numQuery =
from num in numbers
where (num % 2) == 0
select num;

//L'esecuzione della query avviene qui!
foreach (int num in numQuery)
{
Console.Write("{0,1} ", num);
}
```
La variabile di query **numQuery** non esegue mai una query, questa viene effettivamente eseguita solo quando la query viene chiamata. Tale variabile è di tipo **IEnumerable\<T\>**, quindi facilmente ciclabile con un **foreach**.
## Funzioni di aggregazione
Alla variabile di query posso applicare funzioni di aggregazione, come **Count**, **Max**, **Average** e **First**. Queste istruzioni eseguono la query e restituiscono un solo valore, non un **IEnumerable**.
```c#
int evenNumCount = numQuery.Count();
```
## Esecuzione immediata
Se voglio eseguire immediatamente una query e salvare i risultati in cache conviene utilizzare il metodo **ToArray();**.
```c#
var numQuery3 =
(from num in numbers
where (num % 2) == 0
select num).ToArray();
```
## Esempi

### Creazione della sorgente dei dati
Creiamo la sorgente dei dati:

```c#
public class Student
{
public string First { get; set; }
public string Last { get; set; }
public int ID { get; set; }
public List<int> Scores;
}

// Create a data source by using a collection initializer.
static List<Student> students = new List<Student>
{
new Student {First="Svetlana", Last="Omelchenko", ID=111, Scores= new List<int> {97, 92, 81, 60}},
new Student {First="Claire", Last="O'Donnell", ID=112, Scores= new List<int> {75, 84, 91, 39}},
new Student {First="Michael", Last="Tucker", ID=122, Scores= new List<int> {94, 92, 91, 91} }
};
```
### Studenti il cui punteggio nel primo test era superiore a 90
```c#
IEnumerable<Student> studentQuery =
from student in students
where student.Scores[0] > 90 && student.Scores[3] < 80
select student;
```
Si noti che, poiché viene selezionato l'intero oggetto Student (`select student`) il tipo della query è quindi `IEnumerable<Student>`.
Se io facessi invece `select student.Last` (che è una stringa), il tipo della query sarebbe `IEnumerable<string>`.
Per eseguire la query è necessario scrivere il ciclo **foreach**
```c#
foreach (Student student in studentQuery)
{
Console.WriteLine("{0}, {1}", student.Last, student.First);
}
```
### Ordinamento dei risultati
Sarà più semplice analizzare i risultati se vengono ordinati. È possibile ordinare la sequenza restituita in base a qualsiasi campo accessibile negli elementi di origine. Ad esempio, la clausola **orderby** riportata di seguito ordina i risultati alfabeticamente dalla A alla Z in base al cognome di ogni studente. Aggiungere alla query la clausola **orderby**, subito dopo l'istruzione where e prima dell'istruzione select:
```c#
orderby student.Last ascending
```
### Raggruppamento dei risultati
Il raggruppamento è una funzionalità potente nelle espressioni di query. Una query con una clausola **group** genera una **sequenza di gruppi e ogni gruppo contiene un oggetto Key e una sequenza costituita da tutti i membri di tale gruppo**. Nella nuova query riportata di seguito gli studenti vengono raggruppati utilizzando la prima lettera del cognome come chiave.
```c#
var studentQuery2 =
from student in students
group student by student.Last[0];
```
Il tipo della query è stato ora modificato. Vengono ora generate una **sequenza di gruppi con il tipo char come chiave e una sequenza di oggetti Student**. Poiché il tipo della query è stato modificato, nel codice seguente viene **modificato anche il ciclo di esecuzione foreach**:
```c#
foreach (var studentGroup in studentQuery2)
{
Console.WriteLine(studentGroup.Key);
foreach (Student student in studentGroup)
{
Console.WriteLine("{0}, {1}", student.Last, student.First);
}
}
```
### Utilizzare le variabili in modo implicito
Codificare in modo esplicito IEnumerables di IGroupings può risultare noioso. È possibile scrivere la stessa query e il ciclo foreach in modo notevolmente più pratico utilizzando **var**. La parola chiave **var** non modifica i tipi degli oggetti ma **indica solo al compilatore di dedurre i tipi**.

### Ordinare i gruppi in base al valore della chiave
Quando si esegue la query precedente, i gruppi non sono in ordine alfabetico. Per modificare questo comportamento, è necessario fornire la clausola orderby dopo la clausola group. Per utilizzare la clausola orderby, è necessario però utilizzare prima un identificatore che funga da riferimento ai gruppi creati dalla clausola group. Fornire l'identificatore utilizzando la parola chiave into, come segue:
```c#
var studentQuery4 =
from student in students
group student by student.Last[0] into studentGroup
orderby studentGroup.Key
select studentGroup;
```
È possibile utilizzare la parola chiave **let** per **introdurre un identificatore per qualsiasi risultato dell'espressione di query**. Questo identificatore può risultare utile come nell'esempio seguente o può migliorare le prestazioni archiviando i risultati di un'espressione in modo da non doverla calcolare più volte.
```c#
var studentQuery5 =
from student in students
let totalScore = student.Scores[0] + student.Scores[1] +
student.Scores[2] + student.Scores[3]
where totalScore / 4 < student.Scores[0]
select student.Last + " " + student.First;

foreach (string s in studentQuery5)
{
Console.WriteLine(s);
}
```

### Gestione dei valori di ritorno delle SP
#### FirstOrDefault()
Restituisce il primo elemento di una sequenza o un valore predefinito se la sequenza non contiene elementi. Da usare (quasi sempre) quando ho un solo record di ritorno da una SP.
#### Single()
Restituisce il singolo elemento di una sequenza e genera un'eccezione se nella sequenza non è presente esattamente un elemento.
#### SingleOrDefault()
Restituisce il singolo elemento di una sequenza o un valore predefinito se la sequenza è vuota; questo metodo genera un'eccezione se esiste più di un elemento nella sequenza.
#### toList()
Crea un oggetto List\<T\> da un oggetto IEnumerable\<T\>. Da usare quando una SP restituisce più di un record.

### Lamda syntax
Come parametro in ingresso alle funzioni linq (principalemente firstOrDefault()) posso scrivere delle lamda espressioni.
Assumendo di avere il seguente array:
```c#
string[] names = { "Tom", "Dick", "Harry", "Mary", "Jay" };
```
La seguente espressione
```c#
string query =
names.FirstOrDefault (name => name.EndsWith ("y"));
```
indica:
- FirstOrDefault(): voglio **solo** un elemento
- `name => name.EndsWith ("y")` l'elemento che voglio deve terminare per "y". è la stessa cosa della sintassi di ruby `array.map{|a| a.ends_with("y")}`. Invece di "name" posso scrivere anche "n" o quello che voglio, serve come riferimento per l'esecuzione della lamda espressione.

Il risultato sarà infatti:
```c#
string query = "Harry"
```
Allo stesso modo se cambio l'espressione in:
```c#
IEnumerable<string> query =
names.Where (name => name.EndsWith ("y"));
```
Ottengo:
```c#
string[] names = { "Harry", "Mary", "Jay" };
```
#### Esempi
Ho la seguente SP che mi ritorna un elenco di `AidMotivoReclamo` (funzione `ToList()`)
```c#
var aidReclami = connection.Query<AidMotivoReclamo>("Selfcare.GetAIDIndiciConfig", new { IdMotivo = idMotivo, IdReclamoPubblicazione = idReclamoPubblicazione }, commandType: CommandType.StoredProcedure).ToList();
```
###### Controllare se esiste un record con un determinato campo valorizzato
Voglio vedere se esiste almeno un `aidReclami` che abbia il campo `XMLConfig_Aid` con un valore non nullo
```c#
if (aidReclami.Any(r => !string.IsNullOrEmpty(r.XMLConfig_Aid)))
```
###### Selezionare il primo record che ha un determinato campo valorizzato
Allo stesso modo di prima ho:
```c#
var aid = aidReclami.FirstOrDefault(r => !string.IsNullOrEmpty(r.XMLConfig_Aid));
```
##### Ciclare tutti i valori che hanno una determinata caratteristica
```c#
foreach (var aid in aidReclami.Where(aid => !string.IsNullOrEmpty(aid.SqlDropDown))){}
```

###### Ticket.Fields
```c#
var List<UtilityItem> ticket.Fields
```
con `UtilityItem` formato da `string Codice` e `string Descrizione`
```c#
UtilityItem itemToCheck = ticket.Fields.SingleOrDefault(f =>f.Descrizione.Equals("test");
```