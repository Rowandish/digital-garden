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
- **Passaggio 1: Ask**: Richiesta da parte dell'utente o dello sviluppatore.
- **Passaggio 2: Kernel**: Il [[Kernel - SK|Kernel]] orchestra la richiesta dell'utente. Esegue una [[Chaining di funzioni - SK|pipeline/chain]] definita dallo sviluppatore, fornendo un `context` comune per la condivisione dei dati tra le funzioni.
- **Passaggio 2.1: [[Memory - SK|Memories]]**: Un plugin specializzato permette di richiamare e memorizzare il `context` in database vettoriali, simulando la memoria nelle applicazioni AI.
- **Passaggio 2.2: [[Planners - SK|Planners]]**: Semantic Kernel può creare automaticamente `chains` per nuove esigenze dell'utente usando il planner, che utilizza i plugin già caricati nel kernel.
- **Passaggio 2.3: [[Connectors - SK|Connectors]]**: I Connectors out-of-the-box, come Microsoft Graph, o quelli personalizzati, sono usati per ottenere dati aggiuntivi o eseguire azioni autonome.
- **Passaggio 2.4: Custom functions**: Funzioni personalizzate eseguite all'interno del Semantic Kernel, includono sia prompt LLM ([[Semantic Kernel - Plugin#^841aff|semantic functions]]) che codice nativo C# o Python (native functions).
- **Passaggio 3: Risposta**:  Dopo il completamento del processo da parte del kernel, la risposta viene inviata all'utente per informarlo.