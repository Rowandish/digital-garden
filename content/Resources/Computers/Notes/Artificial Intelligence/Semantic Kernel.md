---
tags:
  - CSharp
  - SemanticKernel
  - ImagoLearning
  - MachineLearning
Date: 2023-06-26
Done: true
---
Semantic Kernel è un SDK open-source che consente di ==combinare facilmente prompt di intelligenza artificiale con linguaggi di programmazione convenzionali come C# e Python== al fine di semplificare lo sviluppo di applicazioni di intelligenza artificiale.

Semantic Kernel è un progetto open source (codice [qui](https://github.com/microsoft/semantic-kernel/)).

Semantic Kernel è stato progettato per consentire agli sviluppatori di ==integrare in modo flessibile l'intelligenza artificiale nelle loro applicazioni esistenti==.
A tal scopo, Semantic Kernel fornisce un insieme di astrazioni che facilitano la creazione e la gestione di prompt, funzioni native, memorie e connettori. È quindi possibile orchestrare questi componenti utilizzando le pipeline di Semantic Kernel per completare le richieste degli utenti o automatizzare azioni.

==Grazie alle astrazioni fornite da Semantic Kernel, è possibile utilizzarlo per orchestrare l'intelligenza artificiale da qualsiasi fornitore. Ad esempio, è possibile utilizzare Semantic Kernel per orchestrare l'intelligenza artificiale da OpenAI, Azure o persino Hugging Face.==

## Gestione dell'AI con Semantic Kernel

Il vero potere di Semantic Kernel, tuttavia, deriva dalla sua capacità di combinare insieme queste componenti.
Utilizzando modelli di intelligenza artificiale multipli, funzioni native e memoria all'interno di Semantic Kernel (vedi [[Semantic Kernel - Plugin|plugin]]), è possibile ==creare pipeline sofisticate che utilizzano l'intelligenza artificiale per automatizzare compiti complessi==.

Ad esempio, con Semantic Kernel, potresti creare una pipeline che aiuta un utente a inviare una email al proprio team di marketing.
Utilizzando la memoria, potresti recuperare informazioni sul progetto e quindi utilizzare il planner per generare automaticamente i passaggi rimanenti (ad esempio, collegare la richiesta dell'utente con i dati di Microsoft Graph, generare una risposta con GPT-4 e inviare l'email). Infine, è possibile visualizzare un messaggio di successo all'utente nella propria applicazione personalizzata.

## Step
Vediamo tutti gli step, dalla richieste del cliente (Ask) fino alla risposta da SK (Response) per un caso complesso.

![[kernel-flow.png]]

| Passaggio | Componente       | Descrizione                                                                                                                                                                                                                                                                          |
| --------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1**     | Ask              | Richiesta da parte dell'utente o dello sviluppatore.                                                                                                                                                                                                                                 |
| **2**     | Kernel           | Il [[Kernel - SK]] orchestra la richiesta dell'utente. Per farlo, esegue una [[Chaining di funzioni - SK|pipeline/chain]] definita dallo sviluppatore. Durante l'esecuzione della chain, il kernel fornisce un `context` comune in modo che i dati possano essere condivisi tra le functions. |
| **2.1**   | Memories         | Con un plugin specializzato, uno sviluppatore può richiamare e memorizzare il `context` in database vettoriali. Ciò consente agli sviluppatori di simulare la [[Memory - SK]] all'interno delle loro applicazioni di AI.                                                                  |
| **2.2**   | Planner          | Gli sviluppatori possono chiedere a Semantic Kernel di creare automaticamente `chains` per affrontare nuove esigenze di un utente utilizzando il planner. Il planner è in grado di utilizzare qualsiasi plugin già caricato nel kernel per creare step addizionali.                  |
| **2.3**   | Connectors       | Per ottenere dati aggiuntivi o eseguire azioni autonome, è possibile utilizzare [[Connectors - SK]] out-of-the-box come Microsoft Graph o crearne di personalizzati.                                                                                                                      |
| **2.4**   | Custom functions | Funzioni personalizzate che vengono eseguite all'interno di Semantic Kernel. Queste possono essere sia prompt LLM ([[Semantic Kernel - PLugin|semantic functions]]) che codice nativo C# o Python (`native functions`).                                                              |
| **3**     | Risposta         | Una volta che il kernel ha terminato, è possibile inviare la risposta all'utente per informarlo che il processo è completo.                                                                                                                                                          |
