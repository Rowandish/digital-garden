
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