---
tags:
  - CSharp
  - SemanticKernel
  - MachineLearning
---


![[221739773-cf43522f-c1e4-42f2-b73d-5ba84e21febb.png]]
Una plugin (ex skill) si riferisce a un dominio di competenza messo a disposizione del kernel come ==una singola funzione o come un gruppo di funzioni correlate al plugin==.
Il design delle competenze SK ha dato la priorità alla massima flessibilità per lo sviluppatore per essere sia leggero che estensibile.

## Cosa è un plugin?

![[221742673-3ee8abb8-fe10-4669-93e5-5096d3d09580-1.png]]
Una funzione è il mattone base di un plugin. Questa può avere da una a *n* funzioni.
Una funziona può essere espressa come:
1. **Prompt LLM**: In questo caso viene detta *semantic function*
2. **Codice**: In questo caso viene detta *native function*

Anche quando si usa codice normale, è possibile comunque chiamare prompt LLM, questo quindi significa che ci sono funzioni che sono degli ibridi tra semantic e native function.

Le funzioni possono essere connesse tra di loro in modo da ottenere risultati più interessanti.
Se le funzioni sono pure LLM prompt (*semantic function*) allora il termine *function* o *prompt* possono essere usati in modo interscambiabile.

## Semantic Functions

Le `semantic functions` sono banalmente dei prompt LLM con un loro file di configurazione.
Si può pensare con una struttura ad albero stile file system dove i plugin sono le cartelle e le ==semantic functions altre cartelle all'interno di esse==.
```
TestPlugin
│
└─── SloganMaker
|    |
│    └─── skprompt.txt
│    └─── [config.json](../howto/configuringfunctions)
│   
└─── SummarizeBlurb
     |
     └─── skprompt.txt
     └─── [config.json](../howto/configuringfunctions)
```

Ogni function è una directory che avrà due file, `skprompt.txt` e `config.json`, questi  sono utilizzati per configurare il comportamento e le specifiche delle richieste e delle risposte del sistema di intelligenza artificiale basato su SK.

### skprompt.txt

Il file `skprompt.txt` è un file di testo che viene utilizzato per ==specificare i prompt o le istruzioni che vengono fornite al sistema SK==. Queste istruzioni guidano il comportamento del sistema e definiscono le richieste specifiche da effettuare al fine di ottenere le risposte desiderate.
Il file `skprompt.txt` può contenere prompt multipli, uno per riga, e viene utilizzato per indicare l'input o la domanda da porre al sistema.

#### Esempio di `skprompt.txt` per un plugin che fa riassunti

```
[SUMMARIZATION RULES]
DONT WASTE WORDS
USE SHORT, CLEAR, COMPLETE SENTENCES.
DO NOT USE BULLET POINTS OR DASHES.
USE ACTIVE VOICE.
MAXIMIZE DETAIL, MEANING
FOCUS ON THE CONTENT

[BANNED PHRASES]
This article
This document
This page
This material
[END LIST]

Summarize:
Hello how are you?
+++++
Hello

Summarize this
{{$input}}
+++++
```
### config.json

Il file `config.json` è un file di configurazione (opzionale) che ==definisce i parametri e le impostazioni per le funzioni specifiche del Semantic Kernel==.
Questo file permette di ==personalizzare il comportamento del sistema SK in base alle esigenze dell'applicazione o del caso d'uso specifico==. Alcuni dei parametri comuni che possono essere configurati nel file `config.json` includono:
- `max_tokens [16]`:  Specifica il numero massimo di [[token]] che possono essere generati come output. Il numero di token del prompt in ingresso + `max_token` non può eccedere il numero massimo di token ammessi nel modello. Molti modelli hanno 2048 token come massimo tranne `davinci` che ha 4096.
- `temperature [1]`: Definisce il livello di casualità nella generazione di risposte, controllando la diversità delle risposte generate. Valori più alti significano che il modello prenderà più rischi: esempio con 0,9 si avranno applicazioni più creative e 0  per quelle con una risposta ben definita. Generalmente conviene di modificare questo o `top_p` ma non entrambi.
- `top_p [1]`: un'alternativa al campionamento con la temperatura, chiamata *nucleus sampling*, in cui il modello considera i risultati dei token con *probability mass* `top_p`. Quindi 0,1 significa che vengono considerati solo i token che comprendono la *probability mass* del 10% superiore. Generalmente consigliamo di modificare questa o la temperatura, ma non entrambe.
- `presence_penalty [0]`: Numero compreso tra -2,0 e 2,0. I valori positivi penalizzano i nuovi token in base alla loro **presenza nel testo fino a quel momento**, aumentando la probabilità del modello di parlare di nuovi argomenti.
- `frequency_penalty [0]`:  Numero compreso tra -2,0 e 2,0. I valori positivi penalizzano i nuovi token in base alla loro **frequenza esistente nel testo fino a quel momento**, diminuendo la probabilità del modello di ripetere la stessa riga alla lettera.

#### Esempio di `config.json` per un plugin che fa slogan
```
{
  "schema": 1,
  "type": "completion",
  "description": "a function that generates marketing slogans",
  "completion": {
    "max_tokens": 1000,
    "temperature": 0.0,
    "top_p": 0.0,
    "presence_penalty": 0.0,
    "frequency_penalty": 0.0
  }
  "input": {
    "parameters": [
      {
        "name": "input",
        "description": "The product to generate a slogan for",
        "defaultValue": ""
      }
    ]
  }
}
```


### Templated prompt
La cosa interessante delle `semantic functions` è che il loro prompt può essere concatenato uno all'altro o comunque con del codice iniettabile.

Tali templated prompt includono ==variabili e chiamate di funzione che possono modificare dinamicamente il contenuto e il comportamento di un prompt==.

In un prompt templated, le doppie `{{` parentesi graffe `}}` indicano a Semantic Kernel che c'è qualcosa da iniettare all'interno del prompt, questo può essere:
* Variabili
* Chiamate a funzioni esterne
* Passaggio di parametri a tali funzioni

#### Variabili

Per passare un input a un prompt, facciamo riferimento alla variabile di input predefinita `$INPUT` e, allo stesso modo, se abbiamo altre variabili con cui lavorare, anche queste inizieranno con il simbolo del dollaro `$`.

Per esempio assumiamo di dover fare una semantic function che riassume un testo passato in ingresso in due frasi: questa potrebbe avere il file `skprompt.txt` così:
```
Summarize the following text in two sentences or less. 
---Begin Text---
{{$INPUT}}
---End Text---
```

Posso anche creare altre variabili e nominarle, per esempio:

```
Write me a marketing slogan for my {{$BUSINESS}} in {{$CITY}} with 
a focus on {{$SPECIALTY}} we are without sacrificing quality.
```

Esempio completo di utilizzo di SK con i templated prompt assumendo di avere la seguente struttura di cartelle
```
MyAppSource
│
└───MyPluginsDirectory
    │
    └─── TestPluginFlex
        │
        └─── SloganMakerFlex
        |    |
        │    └─── skprompt.txt
        │    └─── config.json
        │   
        └─── SummarizeBlurbFlex
             |
             └─── skprompt.txt
             └─── config.json
```

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.KernelExtensions;
using Microsoft.SemanticKernel.Orchestration;

// ... instantiate a kernel as myKernel

var myPlugin = myKernel.ImportSemanticSkillFromDirectory("MyPluginsDirectory", "TestPluginFlex");

var myContext = new ContextVariables(); 
myContext.Set("BUSINESS", "Basketweaving Service"); 
myContext.Set("CITY", "Seattle"); 
myContext.Set("SPECIALTY","ribbons"); 

var myResult = await myKernel.RunAsync(myContext,myPlugin["SloganMakerFlex"]);

Console.WriteLine(myResult);
```

#### Chiamate a native functions

Per chiamare una funzione esterna ed embeddarne il risultato nel testo usare la sintassi `{{namespace.functionName}}`.
Per esempio se ho una funzione che fornisce le previsioni del tempo per un determinato luogo posso chiamare la funzione `weather.getForecast` scrivendo:
```
The weather today is {{weather.getForecast}}.
```

Dato che il metodo ha un parametro in ingresso utilizzerà di default il contenuto della variabile `input`, la scrittura sopra è infatti equivalente a:

`The weather today is {{weather.getForecast $input}}.`

#### Parametri delle native functions

Per chiamare una funzione esterna passandogli un parametro posso usare la sintassi `{namespace.functionName $varName}`.
Per esempio se voglio passare diversi parametri alla funzione di previsioni del tempo di cui sopra posso scrivere

```
The weather today in {{$city}} is {weather.getForecast $city}.
The weather today in {{$region}} is {weather.getForecast $region}.
```

### Esempio
Esempio di `skprompt.txt` per generare una risposta ad una data mail
```
My name: {{msgraph.GetMyName}}
My email: {{msgraph.GetMyEmailAddress}}
Recipient: {{$recipient}}
Email to reply to:
=========
{{$sourceEmail}}
=========
Generate a response to the email, to say: {{$input}}

Include the original email quoted after the response.
```
Se invece dovessi scrivere questo codice ma in c# dovrei scrivere una cosa analoga a:
```csharp
async Task<string> GenResponseToEmailAsync(
    string whatToSay,
    string recipient,
    string sourceEmail)
{
    try {
        string name = await this._msgraph.GetMyName();
    } catch {
        ...
    }

    try {
        string email = await this._msgraph.GetMyEmailAddress();
    } catch {
        ...
    }

    try {
        // Use AI to generate an email using the 5 given variables
        // Take care of retry logic, tracking AI costs, etc.
        string response = await ...

        return response;
    } catch {
        ...
    }
}
```

## Native functions

Le native functions sono dei normali file .cs (a differenza delle semantic functions che sono delle cartelle).
Ogni file può contenere da una a n native functions che sono associate ad una skill.

```
MyAppSource
│
└───MyPluginsDirectory
    │
    └─── MySemanticFunctions (a directory)
    |   │
    |   └─── MyFirstSemanticFunction (a directory)
    |   └─── MyOtherSemanticFunction (a directory)
    │
    └─── MyNativeFunction.cs (a file)
    └─── MyOtherNativeFunction.cs (a file)
```

### `SKFunction`
Ogni native function deve avere il decorator `SKFunction`, per esempio
```csharp
public class MyCSharpPlugin
{
    [SKFunction("Return a string that's duplicated")]
    public string DupDup(string text) => text + text;
}
```

### `SKContext`
Posso usare il decorator `SKContext` per passare le variabili del context in modo automatico alla funzione.
Esempio:

```csharp
public class MyCSharpPlugin
{
    [SKFunction("Joins a first and last name together")]
    [SKFunctionContextParameter(Name = "firstname", Description = "Informal name you use")]
    [SKFunctionContextParameter(Name = "lastname", Description = "More formal name you use")]
    public string FullNamer(SKContext context)
    {
        return context["firstname"] + " " + context["lastname"];
    }
}
```

### Native functions asincrone
Posso avere anche delle native functions che non ritornano subito ma solo in modo asincrono (esempio se chiamano una API esterna).
```csharp
public class MyCSharpPlugin
{
    [SKFunction("Return the second row of a qwerty keyboard")]
    [SKFunctionName("Asdfg")]
    public async Task<string> AsdfgAsync(string input)
    {
        await ...do something asynchronous...
        return "asdfghjkl";
    }
```
Dato che le funzioni asincrone devono terminare con `Async` nel nome metodo ma questo le legge meno leggibili nel prompt uso il tag `SKFunctionName` per poterci accedere dal prompt con il nome senza `Async`.

### Chiamare semantic functions

E' possibile chiamare delle funzioni semantiche all'interno delle funzioni native.
Posso usare:
```csharp
public class MyCSharpPlugin
{
    [SKFunction("Tell me a joke in one line of text")]
    [SKFunctionName("TellAJokeInOneLine")]
    public async Task<string> TellAJokeInOneLineAsync(SKContext context)
    {
        // Fetch a semantic function previously loaded into the kernel
        ISKFunction joker1 = context.Func("funPlugin", "joker");

        var joke = await joker1.InvokeAsync();

        return joke.Result.ReplaceLineEndings(" ");
    }
}
```
O anche:
```csharp
public class MyCSharpPlugin
{
    [SKFunction("Tell me a joke in one line of text")]
    [SKFunctionName("TellAJokeInOneLine")]
    public async Task<string> TellAJokeInOneLineAsync(SKContext context)
    {
        // Fetch a semantic function previously loaded into the kernel
        ISKFunction joker2 = context.Skills.GetSemanticFunction("funPlugin", "joker");

        var joke = await joker2.InvokeAsync();

        return joke.Result.ReplaceLineEndings(" ");
    }
}
```


## Core Plugin
Nella repository posso trovare già delle skill già fatte (Core Skill).
Esempi di plugin già fatti:
- `ConversationSummarySkill`: Riassume una conversazione
- `FileIOSkill`: Legge e scrive su file system
- `HttpSkill`: Chiama una API
- `MathSkill`: Effettua operazioni matematiche
- `TextMemorySkill`: Memorizza e recupera testo dalla memoria
- `TextSkill`: Manipola stringhe
- `TimeSkill`: Ottiene il tempo del giorno o altre informazioni sulla data
- `WaitSkill`: Sleep per un determinato tempo

### Esempio con semantic function
```csharp
using Microsoft.SemanticKernel.CoreSkills;

// ( You want to instantiate a kernel and configure it first )

myKernel.ImportSkill(new TimeSkill(), "time");

const string ThePromptTemplate = @"
Today is: {{time.Date}}
Current time is: {{time.Time}}

Answer to the following questions using JSON syntax, including the data used.
Is it morning, afternoon, evening, or night (morning/afternoon/evening/night)?
Is it weekend time (weekend/not weekend)?";

var myKindOfDay = myKernel.CreateSemanticFunction(ThePromptTemplate, maxTokens: 150);

var myOutput = await myKindOfDay.InvokeAsync();
Console.WriteLine(myOutput);
```
Output:
```json
{
  "date": "Monday, February 20, 2023",
  "time": "01:27:44 PM",
  "period": "afternoon",
  "weekend": "not weekend"
}
```
### Esempio con native function
In questo esempio utilizzo SK solo per lavorare con le stringhe senza chiamare alcuna AI, allo scopo di dimostrare la semplicità della concatenazione dei plugin.
In questo esempio prendo una stringa, la trimmo e la metto in upper case.
```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Orchestration;
using Microsoft.SemanticKernel.CoreSkills;

var myKernel = Kernel.Builder.Build();

var myText = myKernel.ImportSkill(new TextSkill());

SKContext myOutput = await myKernel.RunAsync(
    "    i n f i n i t e     s p a c e     ",
    myText["TrimStart"],
    myText["TrimEnd"],
    myText["Uppercase"]);

Console.WriteLine(myOutput);
```
Output:
```
I N F I N I T E S P A C E
```
