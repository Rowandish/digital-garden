---
tags:
  - LargeLanguageModels
---
I prompt svolgono un ruolo cruciale nella comunicazione e nel dirigere il comportamento dell'intelligenza artificiale dei [[GPT Model|modelli]] LLM (Large Language Models).
Servono come **input o query che gli utenti possono fornire per ottenere risposte specifiche da un modello**.

## Prompt design

Saper scrivere bene i prompt è essenziale per ottenere i risultati desiderati con i modelli AI LLM. Il prompt engineering, noto anche come prompt design, è un campo emergente che richiede creatività e attenzione ai dettagli. Implica la ==selezione delle parole, delle frasi, dei simboli e dei formati giusti che guidano il modello nella generazione di testi pertinenti e di alta qualità==.

Se hai già sperimentato ChatGPT, puoi vedere come il comportamento del modello cambia drasticamente in base agli input che fornisci. Ad esempio, i seguenti prompt producono output molto diversi:

```
Please give me the history of humans.
```

```
Please give me the history of humans in 3 sentences.
```

Il primo prompt produce un rapporto lungo, mentre il secondo prompt produce una risposta concisa.
Se stavi costruendo un'interfaccia utente con spazio limitato, il secondo prompt sarebbe più adatto alle tue esigenze.
È possibile ottenere un comportamento ulteriormente raffinato aggiungendo ancora più dettagli al prompt, ma è possibile andare troppo oltre e produrre output irrilevanti. In qualità di prompt engineer, devi trovare il giusto equilibrio tra specificità e rilevanza.

Quando lavori direttamente con i modelli LLM, puoi anche utilizzare altri controlli per influenzare il comportamento del modello.
Ad esempio, è possibile utilizzare il parametro della temperatura per controllare la casualità dell'output del modello. Anche altri parametri come top-k, top-p, penalità di frequenza e penalità di presenza influenzano il comportamento del modello.

Diventare un abile promtp engineer richiede una combinazione di conoscenze tecniche, creatività e sperimentazione.
Ecco alcuni suggerimenti:

* **Comprendi i modelli di intelligenza artificiale LLM**: acquisisci una profonda comprensione di come funzionano i modelli di intelligenza artificiale LLM, inclusa la loro architettura, i processi di formazione e il comportamento.
* **Conoscenza del dominio**: acquisire conoscenze specifiche del dominio per progettare prompt che si allineino con gli output e le attività desiderati.
* **Sperimentazione**: esplora diversi parametri e impostazioni per mettere a punto i prompt e ottimizzare il comportamento del modello per attività o domini specifici.
* **Feedback e iterazione**: analizza continuamente gli output generati dal modello e ripeti i prompt in base al feedback degli utenti per migliorarne la qualità e la pertinenza.
* **Rimani aggiornato**: resta al passo con gli ultimi progressi nelle tecniche di prompt engineering, nella ricerca e nelle migliori pratiche per migliorare le tue capacità e rimanere all'avanguardia nel campo.

## Semantic Kernel

[[Semantic Kernel]] è uno strumento prezioso per il prompt engineer perché consente di ==sperimentare diversi prompt e parametri su più modelli diversi utilizzando un'interfaccia comune==.
Ciò consente di confrontare rapidamente gli output di diversi modelli e parametri e di eseguire iterazioni sui prompt per ottenere i risultati desiderati.

Una volta acquisita familiarità con il prompt engineering, puoi anche utilizzare Semantic Kernel per applicare le tue abilità a scenari del mondo reale. Combinando i tuoi prompt con funzioni e connettori nativi, puoi creare potenti applicazioni basate sull'intelligenza artificiale.

Infine, grazie alla profonda integrazione con Visual Studio Code, Semantic Kernel semplifica anche l'integrazione del prompt engineering nei processi di sviluppo esistenti.

