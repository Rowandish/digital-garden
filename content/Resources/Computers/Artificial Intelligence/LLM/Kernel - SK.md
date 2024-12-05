---
tags:
  - CSharp
  - SemanticKernel
  - MachineLearning
---
Il kernel in [[Semantic Kernel]] è il gestore della domanda (ask) posta dall'utente.
Il kernel soddisfa quanto richiesto dall'utente usando plug-in, le [[Memory - SK]] e i [[Connectors - SK]].
Le caratteristiche principali del kernel che facilitano uno sviluppo più rapido includono:
* **Plugin**: impacchetta i tuoi prompt più utili come componenti completamente riutilizzabili
* **Sviluppo ibrido**: mescola in modo fluido i tuoi prompt AI con il codice nativo convenzionale
* **Orchestrazione**: gestisci i complicati prompt AI LLM con il controllo completo
* **Future-proof**: utilizza più modelli e configurazioni AI LLM con specificità

Il kernel è progettato per incoraggiare il [[Chaining di funzioni - SK]]" che consente agli sviluppatori di combinare e interconnettere l'input e l'output dei plug-in in un'unica pipeline.

Il kernel è istanziato con il comando `Kernel.Builder.Build()`.