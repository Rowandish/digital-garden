---
tags:
  - CSharp
  - SemanticKernel
  - MachineLearning
---
Chiamiamo questo approccio "goal-oriented AI", rifacendoci ai primi giorni dell'IA, quando i ricercatori aspiravano ai computer per battere il campione di scacchi in carica del mondo.
Quel grande obiettivo è stato raggiunto alla fine, ma con l'insolita competenza dei nuovi [[GPT Model|modelli]] di intelligenza artificiale LLM per fornire indicazioni dettagliate per praticamente qualsiasi obiettivo può essere raggiunto quando sono disponibili i plug-in giusti.

Poiché il planner ha accesso a una libreria predefinita di [[Semantic Kernel - Plugin|plugin]] predefiniti e/o a un insieme di competenze definito dinamicamente, è in grado di soddisfare una richiesta con sicurezza.
Inoltre, il planner fa appello alle [[Memory - SK|memories]] per collocare al meglio il contesto e i [[Connectors - SK|connectors]] della richiesta per richiamare le API e sfruttare altre capacità esterne.

## Qual è il valore dell'IA "orientata agli obiettivi"?

Il movimento "*Jobs To Be Done (JTBD)*" ha reso popolare un cambiamento nel passaggio dai risultati del lavoro ai risultati del lavoro.
Invece di concentrarsi sulle caratteristiche o sulle funzioni di un prodotto o servizio, l'approccio JTBD enfatizza gli obiettivi e i desideri del cliente o dell'utente e il valore o il vantaggio che cercano o si aspettano dall'utilizzo del prodotto o servizio.
Comprendendo e articolando il JTBD del cliente o dell'utente, un prodotto o servizio può essere progettato e fornito in modo più efficace. Devi solo fare la domanda giusta che non sia solo "accendi le luci" e invece un obiettivo più impegnativo come "Voglio una promozione lavorativa".

## Cosa succede se il Planner ha bisogno di una funzione che non è disponibile?

Il planner funzionerà all'interno dei plugin che ha a disposizione. Nel caso in cui una funzione desiderata non esista, il progettista può suggerirti di creare la funzione. Oppure, a seconda del livello di complessità, il kernel può aiutarti a scrivere la funzione mancante. 

## Esempi
* [sequential planner](https://github.com/microsoft/semantic-kernel/blob/main/samples/dotnet/kernel-syntax-examples/Example12_SequentialPlanner.cs)
* [action planner](https://github.com/microsoft/semantic-kernel/blob/main/samples/dotnet/kernel-syntax-examples/Example28_ActionPlanner.cs)
* [custom planner](https://github.com/microsoft/semantic-kernel/blob/main/samples/dotnet/kernel-syntax-examples/Example31_CustomPlanner.cs)
