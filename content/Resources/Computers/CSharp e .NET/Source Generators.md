## Introduzione
I Source Generators sono una funzionalità del compilatore Roslyn (.NET) che permette agli sviluppatori di ispezionare il codice utente durante la compilazione e generare al volo nuovi file di codice sorgente da aggiungere al progetto.

Questa tecnica si pone come una soluzione intermedia per risolvere il classico compromesso tra performance e manutenibilità del codice, specialmente quando si tratta di scrivere codice ripetitivo o che richiede ottimizzazioni spinte.

### Codice Manuale vs. Reflection vs. Codice Generato

Per risolvere problemi comuni come la serializzazione, la dependency injection o l'implementazione di pattern come `INotifyPropertyChanged`, gli sviluppatori hanno storicamente seguito tre approcci principali, ognuno con i suoi pro e contro:

1.  **Codice Scritto a Mano**:
    *   **Vantaggi**: Offre le massime prestazioni possibili perché è codice C# standard, ottimizzato e compilato nativamente.
    *   **Svantaggi**: È difficile da mantenere, specialmente su larga scala. È soggetto a errori umani (es. dimenticare di aggiornare una mappatura) e richiede la scrittura di molto codice ripetitivo (boilerplate).

2.  **Reflection**:
    *   **Vantaggi**: È flessibile e si adatta automaticamente alle modifiche del codice (es. aggiungendo una nuova proprietà a una classe). Riduce drasticamente gli errori umani e il codice da scrivere.
    *   **Svantaggi**: Le performance sono molto scarse. La reflection opera a runtime, ispezionando i metadati degli assembly, un processo intrinsecamente lento che può causare un notevole overhead.

3.  **Codice Generato (con Source Generators)**:
    *   **Vantaggi**: Unisce il meglio dei due mondi. Offre le **stesse performance del codice scritto a mano** perché il codice viene generato in C# prima della compilazione finale. Al contempo, si **adatta automaticamente alle modifiche** del codice sorgente, proprio come la reflection, eliminando la necessità di manutenzione manuale.
    *   **Svantaggi**: Introduce un nuovo livello di complessità. Scrivere un Source Generator è più difficile che scrivere codice normale, poiché richiede una conoscenza di base del compilatore Roslyn, delle sue API (Syntax Tree, Semantic Model) e della manipolazione di stringhe o template per generare il codice. Inoltre, il generatore stesso diventa un altro pezzo di software da scrivere e mantenere.

In sintesi, i Source Generators sono uno strumento potente per gli sviluppatori di librerie e per chiunque voglia automatizzare la creazione di codice ad alte prestazioni, ma richiedono un investimento iniziale per apprenderne il funzionamento.

### Syntax Tree vs Semantic Model
Nell'analizzare il codice utente, un Source Generator ha due strumenti principali: il **Syntax Tree** e il **Semantic Model**.

#### Syntax Tree
Il Syntax Tree è una rappresentazione fedele della **struttura** del codice, senza comprenderne il significato. È un albero di nodi che descrive il codice sorgente dal punto di vista sintattico: classi, metodi, proprietà, chiamate a metodi, ecc.
- **Vantaggi**: È estremamente **veloce** da analizzare, perché non richiede la compilazione completa del progetto.
- **Svantaggi**: Non ha informazioni sui tipi. Ad esempio, può dirti "c'è una chiamata al metodo `MioMetodo`", ma non può sapere quale overload specifico viene invocato o qual è il suo tipo di ritorno. Se una classe è definita in più file tramite `partial`, esisteranno più syntax tree indipendenti.
Su Rider e Visual Studio posso vedere il syntax tree di un file con la finestra `Syntax Tree Analyzer`.

#### Semantic Model
Il Semantic Model arricchisce il Syntax Tree con informazioni semantiche, ovvero il **significato** del codice. Per ottenerlo, il compilatore deve eseguire un'analisi più approfondita, simile a una compilazione completa.
- **Vantaggi**: Fornisce informazioni complete sui tipi, i simboli e le relazioni. Permette di rispondere a domande come: "Questa classe implementa l'interfaccia `IDisposable`?", "Qual è il namespace completo di questo tipo?" o "Qual è la definizione di questa classe `partial` considerando tutti i suoi file?".
- **Svantaggi**: È molto più **lento** e dispendioso da creare rispetto al solo Syntax Tree.

#### Quando Usare Cosa
La regola generale è massimizzare le prestazioni:
- **Usa il Syntax Tree** per analisi veloci e leggere. È ideale per un primo filtraggio dei nodi di interesse (es. trovare tutte le classi che hanno un attributo, basandosi solo sul nome dell'attributo). Vedi la lambda `predicate`.
- **Usa il Semantic Model** solo quando le informazioni sui tipi sono strettamente necessarie. Vedi la lambda `transform`

Un Source Generator efficiente filtra prima i candidati usando il Syntax Tree e ricorre al Semantic Model solo sui nodi rimanenti per ottenere le informazioni semantiche indispensabili.

### Best Practices
Nel file [`AnalyzerBannedSymbols.txt` di Roslyn](https://github.com/dotnet/roslyn/blob/d834a2e7215b9d2a8783fcc0da4dbddc8c63273d/src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/AnalyzerBannedSymbols.txt) troviamo un serie di regole da seguire durante la scrittura di un analyzer

*   `T:System.Console`; Analyzers should not be reading / writing to the console
*   `T:System.Diagnostics.Process`; Analyzers should not inspect or create processes
*   `T:System.Diagnostics.ProcessStartInfo`; Analyzers should not inspect or create processes
*   `T:System.Environment`; Analyzers should not read their settings directly from environment variables
*   `P:System.Globalization.CultureInfo.CurrentCulture`; Analyzers should use LocalizableResourceString for culture-dependent messages
*   `P:System.Globalization.CultureInfo.CurrentUICulture`; Analyzers should use LocalizableResourceString for culture-dependent messages
*   `T:System.IO.File`; Do not do file IO in analyzers
*   `T:System.IO.Directory`; Do not do file IO in analyzers
*   `M:System.IO.Path.GetTempPath`; Do not do file IO in analyzers
*   `T:System.Random`; Analyzers should be deterministic
*   `M:System.Reflection.Assembly.Load(System.Byte[])`; Analyzers should only load their dependencies via standard runtime mechanisms
*   `M:System.Reflection.Assembly.Load(System.String)`; Analyzers should only load their dependencies via standard runtime mechanisms
*   `M:System.Reflection.Assembly.Load(System.Reflection.AssemblyName)`; Analyzers should only load their dependencies via standard runtime mechanisms
*   `M:System.Reflection.Assembly.Load(System.Byte[],System.Byte[])`; Analyzers should only load their dependencies via standard runtime mechanisms
*   `T:Microsoft.CodeAnalysis.GeneratorInitializationContext`; Non-incremental source generators should not be used, implement IIncrementalGenerator instead
*   `T:Microsoft.CodeAnalysis.GeneratorExecutionContext`; Non-incremental source generators should not be used, implement IIncrementalGenerator instead

## Getting started
Per creare un nuovo progetto `Source generators` la via semplice è `New project -> Roslyin -> Source Generators` ma la stessa cosa di può fare creando una nuova Console Application con le seguenti caratteristiche:
* Deve targettare `netstandard 2.0`
* Includere i pacchetti `Microsoft.CodeAnalysis.CSharp` e `Microsoft.CodeAnalysis.Analyzer`
* Impostare la property `EnforceExtendedAnalyzerRules` a true: questa suggerisce all'IDE che questo progetto è un analyzer.
All'interno del progetto posso avere *n* classi `Generator` (che hanno l'attributo `[Generator]`) che ereditano da `IIncrementalGenerator` e nel metodo `public void Initialize(IncrementalGeneratorInitializationContext context)` generano i file come vedremo successivamente.
Il progetto che vuole utilizzare tale analyzer deve referenziarlo in questo modo
```xml
<ProjectReference Include="XXX\ProjectNameGenerator.csproj" OutputItemType="Analyzer" ReferenceOutputAssembly="false" />
```
In Rider, le classi generate si trovano nel seguente percorso:
`Nome Progetto -> Dependencies -> .NET XX -> Source Generators .> NomeProgettoGenerator -> [vari file XXX.g.cs]`.
Ad ogni `Build` del progetto viene rigenerato il file. Qualora qualcosa non funzionasse in basso a destra c'è l'icona di `Roslyin` dove poter eventualmente ritriggherare la generazione.
![[Pasted image 20250729160217.png]]
Se per un qualsiasi motivo è necessario che i file generati siano fisicamente su disco (magari per policy aziendale devono anch'essi essere committati oppure non sto usando un IDE e voglio vedere cosa sto generando) è necessario aggiungere un ulteriore tag al Generator:
```xml
<EmitCompilerGeneratedFiles>true</EmitCompilerGeneratedFiles>
```
Il file generati saranno in:
`obj -> generated -> NomeProgettoGenerator`.
Se voglio modificare il path dove vengono generati i file in questione la property è
```xml
<CompilerGeneratedFilesOutputPath>Generated\$(TargetFramework)&</CompilerGeneratedFilesOutputPath>
```
e poi rimuoverli dalla compilazione con
```xml
<Compile Remove="$(CompilerGeneratedFilesOutputPath)/**/*.cs"/>
<Folder Include="Generated\**\"/>
```

## Debug
Essendo il codice lanciato compile-time non è immediato effettuare il debugging del codice generator.
Per farlo sono necessarie alcune accortezze:
* Installare `Visual Studio Installer -> Single Components -> .NET Compiler Platform`
* Aggiungere al `csproj` del generator il tag `<IsRoslynComponent>true</IsRoslynComponent>`
* Aggiungere nella cartella `Properties` un file `launchSettings.json` con questo contenuto
```json
{  
  "$schema": "http://json.schemastore.org/launchsettings.json",  
  "profiles": {  
    "ProjectNameGenerator": {  
      "commandName": "DebugRoslynComponent",  
      "targetProject": "..\\ProjectThatUseGenerator\\ProjectThatUseGenerator.csproj"  
    }  
  }}
```
Una volta fatto questo su Rider compare il tasto per debuggare il Generator in questo modo senza fare `Debugger.Launch()`
![[image-13.webp]]
> [!note] Nota bene
> `targetProject` deve puntare al progetto **che usa il generator**.

Maggiori informazioni [qui](https://blog.jetbrains.com/dotnet/2023/07/13/debug-source-generators-in-jetbrains-rider/#debugging-a-source-generator). 

## Scrivere un generator
Adesso che abbiamo fatto tutto il setup possiamo iniziare con scrivere il nostro source generator.
L'idea è avere un marker che permette di identificare una classe o property di cui vogliamo estendere il comportamento.
Una volta trovata tale classe utilizzare il *syntax tree* di Roslyn per ottenere le parti di codice che ci interessano e generarne altre in base alle nostre esigenze.
Come marker la scelta migliore è sempre quella di utilizzare un `Attribute`; che può essere sia generato anch'esso che trovarsi nella soluzione.

### Ottenere le classi da generare

#### Metodo generico
Per ottimizzare le performance, è fondamentale filtrare il più possibile il codice da analizzare. L'approccio migliore consiste nell'usare un `SyntaxProvider`. Questo oggetto espone un metodo `CreateSyntaxProvider` che accetta due funzioni:

1.  **`predicate`**: Una funzione che viene eseguita su ogni nodo della sintassi del progetto. Il suo scopo è fare un filtro rapido e preliminare. Ad esempio, può verificare se un nodo è una dichiarazione di classe che possiede almeno un attributo, senza ancora sapere di quale attributo si tratta. Questo filtro iniziale è molto efficiente perché non richiede informazioni semantiche complesse. Utilizza il `syntax tree`.
2.  **`transform`**: Una funzione che viene eseguita solo sui nodi che hanno superato il `predicate`. Qui si ha accesso al `SemanticModel`, che permette di analizzare il codice in modo più approfondito (es. verificare che l'attributo sia esattamente quello che ci interessa). Il risultato di questa funzione dovrebbe essere una classe o una struct contenente solo i dati minimi indispensabili per la fase di generazione del codice. Estrarre solo le informazioni necessarie (come nomi di classi, tipi di proprietà, ecc.) riduce l'impronta di memoria e mantiene il generatore veloce. Utilizza il `Semantic model`.

```csharp
// Predicato: prendi tutte le classi che hanno almeno un attributo
var provider = context.SyntaxProvider.CreateSyntaxProvider(
    predicate: static (node, _) => node is ClassDeclarationSyntax { AttributeLists.Count: > 0 },
    transform: static (context, _) =>
        {
            // Logica per estrarre i dati minimi
            // ...
            return new ClassToGenerate(/* ... */);
        })
.Where(x => x is not null);
```

#### Metodo basato su attributi
Un approccio ancora più diretto e performante, specifico per i generatori basati su attributi, è offerto dal metodo `context.SyntaxProvider.ForAttributeWithMetadataName`. Questo metodo è un'ottimizzazione del pipeline `predicate`/`transform` e permette di ottenere direttamente tutti i nodi (classi, metodi, proprietà, ecc.) decorati con un attributo specifico, identificato tramite il suo nome completo (es. `"MyProject.MyAwesomeAttribute"`).

Il metodo si occupa internamente di:
1.  Filtrare in modo efficiente solo i nodi sintattici che dichiarano attributi.
2.  Verificare semanticamente che l'attributo corrisponda a quello richiesto.

Questo non solo semplifica notevolmente il codice del generatore, ma garantisce anche prestazioni migliori, poiché Roslyn può applicare ottimizzazioni interne mirate. Il risultato è un `IncrementalValuesProvider<GeneratorAttributeSyntaxContext>`, dove ogni `GeneratorAttributeSyntaxContext` contiene il nodo target, il `SemanticModel` e i dati relativi all'attributo trovato, pronti per essere usati nella fase di generazione.

```csharp
IncrementalValuesProvider<ClassToGenerate> provider = context.SyntaxProvider.ForAttributeWithMetadataName(
        "MyProject.MyAwesomeAttribute",
        predicate: (node, _) => node is ClassDeclarationSyntax,
        transform: (context, _) =>
        {
            // Logica per estrarre i dati minimi
            // ...
            return new ClassToGenerate(/* ... */);
        })
    .Where(x => x is not null);
```

### Scrivere oggetti generati
Il modo più semplice è scrivere un file statico sempre uguale (come per esempio l'attributo marker) usando il metodo `RegisterPostInitializationOutput`.
Per invece oggetti dinamici  si usa il metodo `RegisterSourceOutput` che ha in ingresso un `IncrementalValuesProvider<MySlimStruct?>` e chiama un metodo per ognuno di tali `struct`.

## Testare
Ecco un esempio concreto di una classe helper per i test, che utilizza la libreria `Verify.XUnit` per lo snapshot testing.

```csharp
// ViewModelTester.cs
internal static class ViewModelTester
{
    public static async Task VerifyAsync<T>(string assetClassName) where T : IIncrementalGenerator, new()
    {
        // 1. Istanzio il generator che voglio testare
        var generator = new T();
        
        // 2. Carico il codice sorgente da analizzare come risorsa embedded
        // Questo permette di non avere errori di compilazione
        var viewSyntaxTree = CSharpSyntaxTree.ParseText(await GetEmbeddedResourceAsStringAsync($"{assetClassName}.cs"));
        
        // 3. Per non aggiungere una dipendenza anche al progetto che contiene l'attributo "marker" lo copincollo qui. In .NET 10 si risolve usando gli embedded attribute
        var viewModelAttribute =
            CSharpSyntaxTree.ParseText(await GetEmbeddedResourceAsStringAsync("ViewModelAttribute.cs"));

        // 4. Liste delle reference che mi servono per compilare. Sicuramente l'assembly dove si trova 'System', come vedi sotto, ma potenzialmente anche altro
        IEnumerable<PortableExecutableReference> references =
        [
            MetadataReference.CreateFromFile(typeof(object).Assembly.Location)
        ];

        var compilation = CSharpCompilation.Create(
            assemblyName : nameof(VerifyAsync),
            syntaxTrees  : [viewSyntaxTree, viewModelAttribute],
            references   : references);

        // 5. Eseguo il generator e verifico l'output con Verify
        var driver = CSharpGeneratorDriver.Create(generator).RunGenerators(compilation);

        var settings = new VerifySettings();
        await Verify(driver, settings);
    }

    private static async Task<string> GetEmbeddedResourceAsStringAsync(string resourceName)
    {
        // ... implementazione per caricare le risorse embedded ...
    }
}
```

### La Sfida degli Attributi Marker (The Marker Attribute Challenge)

Una delle principali "accortezze" da considerare è la gestione degli **attributi marker**. Il nostro generatore si attiva quando trova una classe decorata con `[ViewModel]`. Tuttavia, durante i test, la compilazione che creiamo in memoria non conosce questo attributo, perché esiste solo nel progetto principale (o nel generatore stesso).

#### Soluzione con .NET 10

A partire da .NET 10, questo problema è stato risolto in modo più elegante. I Source Generator possono ora "offrire" al compilatore il codice sorgente dei loro attributi marker, che viene aggiunto automaticamente alla compilazione quando necessario.

Questo semplifica enormemente i test. Il codice per caricare l'attributo non sarà più necessario, rendendo l'helper di test più pulito e semplice da mantenere.

Il codice di test si semplificherebbe così:

```csharp
// ...
// Non serve più caricare l'attributo manualmente
// var viewModelAttribute =
//     CSharpSyntaxTree.ParseText(await GetEmbeddedResourceAsStringAsync("ViewModelAttribute.cs"));

var compilation = CSharpCompilation.Create(
    assemblyName : nameof(VerifyAsync),
    syntaxTrees  : [viewSyntaxTree], // Basta passare solo il syntax tree della view!
    references   : references);

var driver = CSharpGeneratorDriver.Create(generator).RunGenerators(compilation);
// ...
```

Il generatore stesso si occuperà di fornire il codice dell'attributo `ViewModelAttribute` al compilatore, sia nel progetto principale che durante i test.

## Diagnostica
I sourcegenerators possono anche fornire errori parlanti qualora gli attributi di loro competenza non siano utilizzati correttamente.
Per esempio vorrei poter imporre di utilizzare un determinato attributo solo su classi `partial`, oppure solo su classi che ereditano da XXX e così via e fornire all'IDE un errore sulla classe in questione.
Questa operazione viene effettuata in questi step:
* Il `record` fornito dal metodo `Transform` deve avere due property in più:
	* `Location`: indica dove nell'IDE verrà sottolineato in rosso il problema
	* `IsValid`: indica se tale classe è valida o meno.
Esempio:
```csharp
// Verifica che la classe sia valida con logica custom
var isValid = CheckIfValid(semanticModel, classSymbol);  
  
// La diagnostica verrà indicata sul nome della classe
var location = classDeclarationSyntax is ClassDeclarationSyntax cds  
    ? cds.Identifier.GetLocation()  
    : classDeclarationSyntax.GetLocation();  
  
return new GenerationItem(new XXX(), location, isValid);
```

Nel metodo `Execute` per prima cosa verrà controllato il `IsValid`: se è false riporto la `Diagnostic` e ritorno in un modo analogo al seguente:
```csharp
if (!generationItem.Value.IsValid)  
{  
    var invalidViewModelAttributeUsage = new DiagnosticDescriptor(id: "IMA0001",  
        title: "[ViewModel<T>] può essere applicato solo a Form o UserControl",  
        messageFormat:  
        "L'attributo [ViewModel<T>] è applicato ad una classe che non eredita da Form o da UserControl.",  
        category: "IMASourceGenerator.ViewModelGenerator", DiagnosticSeverity.Error, isEnabledByDefault: true,  
        description:  
        "L'attributo ViewModel<T> deve essere utilizzato esclusivamente su classi WinForms che ereditano (direttamente o indirettamente) da Form o da UserControl.");  
    context.ReportDiagnostic(Diagnostic.Create(descriptor: invalidViewModelAttributeUsage, generationItem.Value.Location));  
    return;  
}
```

## Tips & Tricks
* Non è detto che voglia estendere la classe a cui ho aggiunto l'attributo usando i dati della classe stessa ma magari da un'altra classe. In questo caso basta passare un `typeof` della classe da cui voglio prendere dei valori come parametro dell'attributo. Per esempio `[MyAwesomeAttribute(typeof(AnotherClass))]`. Una volta ottenuto il `Type` nel source generator potrò usarlo per ottenere tutti i dati che mi servono.
* Posso prendere le informazioni per generare oggetti non solo da una classe decorata ma anche da file esterni: per esempio potrei avere un xml e in base al contenuto di questo ultimo generare varie classi. Per far questo, nel metodo `Initialize` basta usare `context.AdditionalTextsProvider.Where...`. Il  file esterno in questione dovrà essere aggiunto nel `csproj` come `AdditionalFile`.
	* Esempio: avere un xml che mi descrive la struttura del codice che voglio creare e il generator scriverà il primo mock-up del progetto, con tutte le classe. Prese quelle inizio a lavorare.