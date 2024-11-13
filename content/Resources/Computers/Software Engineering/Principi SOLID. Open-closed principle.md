---
tags:
  - Coding
  - SOLID
  - PublishedPosts
---
Questo è probabilmente il principio più forte, che racchiude tutti gli altri.
## Definizione

Il principio di open-closed afferma che "**una classe dovrebbe essere aperta alle estensioni e chiusa alle modifiche**".

Questo significa che uno software dovrebbe poter permettere **estensioni del suo comportamento senza dover andare a modificare le classi già esistenti**.
Ciò è particolarmente utile nei team di grandi dimensioni in cui più sviluppatori lavorano sulla stessa codebase. Seguendo l'OCP, gli sviluppatori possono aggiungere funzionalità senza intralciarsi a vicenda.

Qualora una piccola modifica ai requisiti porti una notevole rivoluzione nel software sottostante, significa che questo principio non è stato rispettato.

## Come implementarlo

Come insegna uncle Bob, i requisiti di un software continuano a cambiare nel tempo; conseguentemente il software deve potersi adattare a tali modifiche.

La prima idea di Bertrand Mayer per risolvere la questione è usare l'ereditarietà: per estendere il comportamento di un software basta aggiungere una nuova classe figlia che estende il comportamento della classe padre.

Il problema dell'ereditarietà è che questa porta ad un forte accoppiamento tra classe padre e figlia qualora questa ultima dipenda da dei metodi implementati nella classe padre.

Robert Martin infatti definisce il principio usando il polimorfismo e non l'ereditarietà, quindi usando classi figlie di interfacce e il codice può passare da una classe all'altra in base alle sue necessità (pattern Strategy).

Le interfacce sono _closed for modifications_ in quanto non permettono alcuna implementazione al loro interno e obbligano le classi figlie ad implementare quanto serve. Queste sono quindi completamente disaccoppiate in quanto non condividono alcuna riga di codice.

## Point of Variations

Un altro modo di vedere il principio OCP è utilizzare i "_Point of Variation"_ cioè il punti del codice che è probabile debbano cambiare in futuro.

Il principio riformulato dice: _Identifica i punti dove è probabile che verrà effettuata una modifica al codice e costruisci una interfaccia attorno ad essi._

Quindi per rispettare l'OCP è necessario prima identificare i PV e poi costruirci delle astrazioni attorno.

Il problema di questo approccio è cercare di capire i punti dove il codice _probabilmente_ verrà modificato senza averne certezza. I rischi infatti sono due:

- **Aggiungere astrazioni in punti dove il codice non varierà è un costo**. Questo è quanto dice principio [YAGNI (_You aren’t gonna need it_)](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) che suggerisce che un programmatore dovrebbe implementare codice solo quando questo effettivamente gli serve. Aggiungere astrazioni nel codice ha un costo anche di mantenimento e non utilizzarle è un ulteriore costo non necessario.
- **Non trovare i veri Point of Variations**: magari le modifiche richieste saranno completamente diverse da quelle che ci aspettiamo portando quindi alla necessità di dover comunque refactorare il codice.

Il giusto approccio è quindi quello di essere consapevoli di non poter prevedere tutti i punti dove potrebbe essere necessaria una modifica al codice ma che una volta identificati, si è in grado di modificare il codice aggiungendo le giuste astrazioni.

## Limiti

Come abbiamo visto per poter rispettare questo principio è necessario utilizzare l'ereditarietà o, ancora meglio, la composizione introducendo vari livelli di astrazione in modo da ridurre l'accoppiamento tra le classi.

Questo porta a due limiti principali:

- Vi dovrà comunque essere da qualche parte un _if_ o uno _switch_ che permette al software di utilizzare le nuove classi invece delle vecchie e questo switch sarà aggiunto quindi al vecchio codice (un minimo di modifica quindi vi sarà sempre);
- Difficilmente in sede di scrittura del software andremo a creare tutti i possibili metodi con tutti i possibili parametri delle interfacce in modo che l'estensione del comportamento non porti alla modifica delle astrazioni. E' probabile quindi che anche il più perfetto dei codici necessiti delle modifiche al vecchio codice come l'aggiunta di un metodo ad una interfaccia o un parametro a una funzione.

In ogni caso seguire il principio permette di sviluppare codice migliore, con accoppiamento minimo e grande scalabilità.

## Come procedere nel mondo reale

Abbiamo visto come da un lato sia utile seguire l'OCP, dall'altro come spesso non sia semplice individuare i punti dove introdurlo.

Come procedere quindi? Di seguito qualche suggerimento:

- Ricorda sempre il principio KISS (_Keep It Simple Stupid_): prevedere i Point of Variations non è semplice, non perdere tempo nell'introduzione di astrazioni non necessarie;
- Scrivi test automatizzati: i test hanno il vantaggio che, oltre a verificare il funzionamento del codice, permettono di capire il codice dal punto di vista dell'utilizzatore e non solo del programmatore. Se il tuo codice contiene dei metodi difficilmente testabili, tipicamente questi violano l'OCP. In questi casi l'introduzione di astrazioni sarà naturale. Scrivi sempre codice che sia 100% testabile.
- Il downcasting (castare una astrazione in una classe concreta) e sintomo di violazione dell'OCP.
- L'operatore "_is"_ è analogamente sintomo di violazione dell'OCP

## Esempio
In questo esempio, aggiungendo nuove implementazioni della classe ReportGenerator non modifichiamo il codice esistente ma piuttosto aggiungiamo nuovi tipi quando necessario.

```csharp
// Violates OCP
public class ReportGenerator
{
    public void GenerateReport(string reportType)
    {
        if (reportType == "PDF")
        {
            // Generate PDF report
        }
        else if (reportType == "Excel")
        {
            // Generate Excel report
        }
    }
}

// Adheres to OCP
public abstract class ReportGenerator
{
    public abstract void GenerateReport();
}

public class PdfReportGenerator : ReportGenerator
{
    public override void GenerateReport()
    {
        // Generate PDF report
    }
}

public class ExcelReportGenerator : ReportGenerator
{
    public override void GenerateReport()
    {
        // Generate Excel report
    }
}
```