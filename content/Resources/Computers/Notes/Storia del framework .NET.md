---
tags:
  - Coding
  - CSharp
  - DotNET
  - PublishedPosts
---


La rivoluzione che sta portando avanti Microsoft con il suo framework sta portando parecchia confusione nei programmatori: .NET Standard o .NET Core? .NET Framework o .NET e basta?

Per cercare di fare chiarezza tra tutte queste definizioni è necessario partire dalle basi e andare ad approfondire la storia del framework di programmazione più famoso di Microsoft: .NET.

## .NET Framework

Nel 2002 Microsoft ha inventato il framework .NET, che era una piattaforma dove poter sviluppare applicazioni utilizzando vari linguaggi (il più diffuso era sicuramente C#, ma anche VB o F#) solo per Windows. Esso era composto dai compilatori, dal CLR e da varie librerie.

Quando compilo il mio codice (scritto in uno o più linguaggi) il compilatore crea quello che si chiama "[Common Intermediate Language" CIL](https://it.wikipedia.org/wiki/Common_Intermediate_Language): questo è un linguaggio linguaggio assembly orientato agli oggetti **intermedio "comprensibile" alla piattaforma .NET**; in questo modo io posso avere codice in vari linguaggi diversi convertiti tutti in un unico linguaggio intermedio.

Quando vi è la necessità di eseguire il codice CIL questo viene poi compilato in codice macchina al volo da un Jit (compilatore just-in-time) e poi eseguito. Il compilatore Jit di Microsoft si chiama [Common Language Runtime (CLR)](https://it.wikipedia.org/wiki/Common_Language_Runtime).

![[400px-CLR_diag.svg.png]]

Il programmatore ovviamente non si accorge di questa complessità che è completamente mascherata; anzi ha un vantaggio: può scrivere la sua applicazione in più linguaggi differenti in base ai suoi scopi, per esempio può scrivere delle librerie F# se ha bisogno di un linguaggio funzionale e delle altri in C#.

Vi è da fare sempre una **distinzione tra la versione del linguaggio e la versione del Framework**: come abbiamo visto il Framework è completamente scorporato dal linguaggio e conseguentemente una versione di C# è supportata solo da alcune versioni di .NET Framework (il compilatore deve essere in grado di leggere le specifiche del linguaggio)

Questo è il motivo per cui le versioni di C# non corrispondono uno a uno con le versioni del .NET Framework.

![[DotNet.svg.png]]

## .NET Core

Il .NET Framework ha 20 anni, in questi anni sono successe infinite cose nel mondo dell'informatica, sono cambiati i PC; le architetture, i sistemi operativi, i linguaggi… Il framework ha sempre rincorso questi cambiamenti con fix su fix, e retrocompatibilità innumerevoli.

Questo però ha portato ad un sistema sempre più lento.

Microsoft ha avuto l'idea di cominciare a scorporarsi sempre di più dal .NET Framework ormai lento e legacy per creare una nuova architettura completamente da zero.

Nel 2016 Microsoft ferma il Framework .NET (versione 4.8) e inizia quindi il processo chiamato .**NET Core, che è una rivisitazione di tutti i livelli di astrazione sotto il linguaggio di programmazione**: al programmatore non cambierà nulla ma sotto il cofano avverrà la rivoluzione.

Il Common Language Runtime ora si chiama **Core Language Runtime** e non è una cambio solo di nome: è stato completamente **rivoluzionato soprattutto togliendo tutta una serie di retrocompatibilità che si portava dietro il Framework .NET** che ora non servono più a nulla.

Questo ha portato ad un notevole incremento di velocità, sia per il refactor del codice ma soprattutto per la rimozione di tutte le zavorre di 20 anni di architetture che impedivano, di fatto, di avere un prodotto moderno e funzionante.

Dato che è cambiato tutto il motore sottostante ma il linguaggio è rimasto lo stesso, al programmatore un aggiornamento a .NET Core risulterà estremamente semplice (a meno dell'aggiornamento delle librerie di terze parti).

Microsoft ha successivamente fatto uscire .NET Core 2, 2,1 e 3 portando sempre più cose dal mondo .NET Framework al mondo .NET Core in modo da poter riuscire a sostituire completamente i due framework offrendo agli sviluppatori le stesse funzionalità.

Non tutto è stato portato in .NET Core, per esempio [WCF](https://docs.microsoft.com/it-it/dotnet/framework/wcf/whats-wcf) esiste solo in .NET Framework (che Microsoft non ha intenzione di cancellare, anzi il 4.8 rimarrà supportato ancora per anni).

## .NET Standard

A questo punto è risultato necessario introdurre un altro concetto: .NET Standard.

L'idea è che ci sono vari livelli di astrazione differenti: non solo quelli di .NET Framework e .NET Core, ma anche Xamarin ha il suo, come Unity o Mono. Ognuno di questi prende il linguaggio e lo compila a modo suo.

L'idea è creare un "ponte" che permetta di convertire il prodotto di questi ultimi in un unico codice standard CIL uguale per tutti; questo ponte è .NET Standard.

![[platforms-netstandard.png]]

## .NET

Una volta arrivati alla versione .NET Core 3.1 la successiva sarebbe stata la versione .NET Core 4; questo però avrebbe portato a parecchia confusione tra il .NET Framework 4.x e il .NET Core 4.

Già la situazione era complessa, utilizzare per entrambi i framework la versione 4 sarebbe stato un delirio: Microsoft ha ben pensato quindi di evitare la versione .NET Core 4 e quindi di passare direttamente alla 5. Inoltre hanno deciso di non utilizzare più il termine "Core" in quanto dalla versione 5 in poi non è più solo una versione alternativa del framework che fa le stesse cose in modo più veloce, è una versione che va oltre offrendo numerose nuove possibilità ai programmatori.

Detto questo è importante sottolineare una cosa: la vera rivoluzione nei livello di astrazione sottostanti è avvenuta **solo una volta**, tra .NET Framework e .NET Core. **Tra .NET Core 3.1 e .NET 5 non vi è alcuna rivoluzione nel motore del framework, è un cambio solo ed esclusivamente di naming**.

![[core.png]]

Inoltre con .NET si è persa l'utilità di utilizzare .NET Standard: con .NET infatti c'è stata una fusione di tutti i framework e i diversi livelli di astrazione in un unico che è quindi in grado di compilare e gestire codice per applicazioni su Windows, su mobile, su Mac e così via.

Questo non vuol dire che tutti i programmi sono compatibili con tutti i dispostivi: per esempio una applicazione Windows Form utilizzerà librerie presenti sono su Windows e non disponibili quindi su Mac. Anche se il motore è lo stesso, una applicazione WF quindi non funzionerà se non su Windows.

## Differenze

| .NET Core                     | .NET Framework                                    |
| ----------------------------- | ------------------------------------------------- |
| Multipiattaforma              | Solo windows                                      |
| Open source                   | Accesso a APIs legacy                             |
| Migliori performance          | Solo una versione può essere installata           |
| Packed nell'applicazione      | L'app utilizza la versione installata in macchina |
| Accesso a tutte le nuove APIs |                                                   |
