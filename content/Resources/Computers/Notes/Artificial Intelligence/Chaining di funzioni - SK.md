---
tags:
  - CSharp
  - SemanticKernel
  - LargeLanguageModels
---


SK è stato sviluppato con lo spirito delle pipeline di UNIX per prendere un comando e effettuare lo streaming del suo output al comando successivo.
Questo concetto si vede dall'uso del parametro `$INPUT`.

Ad esempio, possiamo creare tre [[Semantic Kernel - Plugin|semantic functions]] concatenate e mettere in stringa i loro output nell'input successivo.
```csharp
string myJokePrompt = """
Tell a short joke about {{$INPUT}}.
""";

string myPoemPrompt = """
Take this "{{$INPUT}}" and convert it to a nursery rhyme.
""";

string myMenuPrompt = """
Make this poem "{{$INPUT}}" influence the three items in a coffee shop menu. 
The menu reads in enumerated form:
1.
""";

var myJokeFunction = myKernel.CreateSemanticFunction(myJokePrompt, maxTokens: 500);
var myPoemFunction = myKernel.CreateSemanticFunction(myPoemPrompt, maxTokens: 500);
var myMenuFunction = myKernel.CreateSemanticFunction(myMenuPrompt, maxTokens: 500);

var myOutput = await myKernel.RunAsync(
    new ContextVariables("Charlie Brown"),
    myJokeFunction,
    myPoemFunction,
    myMenuFunction);

Console.WriteLine(myOutput);
```
E il risultato sarà
```
1. Charlie Brown's Surprise - A sweet and creamy latte with a hint of caramel 
2. Good Grief! - A bold espresso with a dash of cinnamon 
3. Wide Smile - A smooth cappuccino with a sprinkle of nutmeg
```

Se invece togliamo l'utlima funzione:
```csharp
var myOutput = await myKernel.RunAsync(
    new ContextVariables("Charlie Brown"),
    myJokeFunction,
    myPoemFunction);
```
Otterremo
```
Charlie Brown got a present one day
He said "Oh good grief!" in dismay
He opened it up with a smile so wide
But it wasn't what he had in mind
```