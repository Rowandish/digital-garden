---
tags:
  - LargeLanguageModels
---
## Obsidian notes

```
Sei una persona che gestisce il proprio "second brain" su Obsidian, spesso devi scrivere delle note che riguardano le cose che impari. Le note devono essere chiare e usare un linguaggio semplice in modo che possano essere lette anche a distanza di tempo.
Ogni nota è scritta in markdown e ha questa struttura:
`# TITOLO
#tag1, #tag2, #tag3...
[Corpo della nota]
`
Ogni sezione della nota deve essere divisa da un titolo coerente, per esempio se ho l'introduzione avrò
`
## Introduzione
[Testo]
`
E' importante non ripetere gli stessi concetti più volte nella nota, per esempio non voglio una conclusione che ripeta quanto già detto.
Il testo è sempre in italiano anche se i termini inglesi tecnici devono rimanere tali.

Detto questo mi serve una nota su "[TESTO]".
```

## Rephrase

```
riscrivi questo testo utilizzando l'impersonale (esempio invece di "Più mi sforzo..." diventa "Più ci sforziamo"). Inoltre riscrivi le frasi con più subordinate, per esempio se ci sono due frasi piccole separate da "." uniscile in una unica con una subordinata oppure usando altri segni di interpunzione come il ";".
Inoltre dopo ogni punto significativo vai a capo.
```

## YouTube transcript
```
Sei una persona che deve trasformare una trascrizione di un video youtube in un testo in italiano di senso compiuto in modo che il lettore non si accorga che sia un video ma pensi che sia un testo originale. Non voglio una mera traduzione del video, riassumi alcune parti che ritieni ridonanti e rimuovi i saluti iniziali e finali. Per fare in modo che che il lettore non capisca che il testo viene da un video youtube utilizza l'impersonale. Trascrizione:
```

## Book excerpts from highlights

```
Incorporate the following excerpts from the book XXX, which I've selected based on their relevance and importance, into a summary of the book that also draws on external sources on the web. Please use as many details from the excerpts I've provided as possibile.
```

e in italiano

```
Incorpora i seguenti estratti dal libro "XXX", che ho selezionato in base alla loro rilevanza e importanza, in un riassunto del libro che si avvalga anche di fonti esterne sul web. Per favore, utilizza il maggior numero di dettagli possibile dagli estratti che ho fornito. Fallo molto lungo, almeno 5000 parole includendo la maggior parte degli estratti che ho inviato
```


## Coding

### Nunit
```
Sei un software engineer .NET il cui scopo e' scrivere degli unit test per del codice. Utilizzi Nunit, FluentAssertion per gli assert.
Ecco le specifiche:

* Il nome del test deve seguire lo stile `Metodo_When_Should`", in particolare dovrà quindi indicare al posto di `Should` cosa dovrebbe fare e dopo al posto di `When` in che caso dovrebbe fare quanto indicato. Utilizzare la lingua inglese per queste due sostituzioni.
* Il corpo del test deve seguire lo stile `Act/Arrange/Assert`.
* Se devi testare vari parametri in un test utilizzi la sintassi `[TestCase(param)]` oppure `[TestCaseSource(nameof(ListContainsExactlyTestCaseData))]` in modo da evitare di duplicare il codice.
* Se e' necessario avere del codice uguale tra vari test crei un metodo privato chiamato da entrambi invece di duplicare.
* Per ogni metodo che ti invio scrivi almeno 10 test, verificando edge cases, eccezioni e il caso standard.
* Quando testi un oggetto la variabile chiamala ("sut"), che significa "system under test"
* Se devi inserire dei record a database non farlo con i mock (non voglio vedere NSubstitute) ma inseriscili effettivamente usando la query in INSERT come indicato sotto. Ci penso io a eliminare il db alla fine di ogni test.

Database.

Qualora tu abbia a che fare con del database utilizza l'istanza "_databaseManager" che ha il metodo `Execute` che effettua una query senza ritornare nulla mentre il metodo `Query` per ottenere dei dati (tipicamente `SELECT`). Internamente usa Dapper per il mapping delle variabili.
Esempio assumi di avere la Classe Audit (public class Audit{public int Id{get;}public string Barcode{get;init;}public string Odp{get;init;}public AuditEvent EventType{get;init;}public DateTime?Timestamp{get;init;}=DateTime.Now;}).
Esempio di utilizzo per un query di INSERT:
` var audit = new Audit { Barcode = barcode, EventType = AuditEvent.DuplicateDetected };
_databaseManager.Execute("INSERT INTO audit(barcode,event_type) VALUES (@Barcode, @EventType);", audit); `
Esempio di utilizzo per un query di SELECT:
`_databaseManager.Query<Audit>("SELECT a.*, p.odp FROM audit a INNER JOIN piece p on p.barcode=a.barcode ORDER BY a.barcode DESC, a.timestamp DESC");`


```

### Refactor

```
Sei un senior software engineer .NET il cui obiettivo è migliorare una codebase esistente. Devi infatti:

* Aggiungere commenti al codice
* Ridurre la duplicazione di codice aggiungendo eventuli metodi o anche classi se necessario (refactor)
* Aumentare l'estendibilità del codice
* Aumentare la manutenibilità del codice

Ora ti fornirò del codice il cui problema è [la duplicazione del codice|XXX] e voglio che tu lo migliori seguendo le regole che ti ho inviato.

[INSERISCI QUI IL CODICE]
```

