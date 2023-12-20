---
tags:
  - Azure
  - PaaS
---
Azure Resource Manager (ARM) è il servizio di gestione di risorse di Azure che fornisce un framework coerente per la creazione, la distribuzione e la gestione delle risorse nell'ambiente Azure.

## Vantaggi

Con Azure Resource Manager, puoi:

- Gestire la tua infrastruttura tramite modelli dichiarativi anziché script.
- Distribuire, gestire e monitorare tutte le risorse della tua soluzione come gruppo, anziché gestire singolarmente queste risorse.
- Ridistribuire la tua soluzione durante tutto il ciclo di vita dello sviluppo e avere la certezza che le risorse siano distribuite in uno stato coerente.
- Definire le dipendenze tra le risorse in modo che vengano distribuite nell'ordine corretto.
- Applicare il controllo degli accessi a tutti i servizi, poiché il controllo degli accessi basato sui ruoli di Azure (Azure RBAC) è nativamente integrato nella piattaforma di gestione.
- Applicare tag alle risorse per organizzare logicamente tutte le risorse nella tua sottoscrizione.
- Chiarire la fatturazione della tua organizzazione visualizzando i costi per un gruppo di risorse che condividono lo stesso tag.

## Consistent management layer 
Una delle caratteristiche chiave di ARM è il "Consistent management layer" (strato di gestione coerente).

Lo strato di gestione coerente di Azure Resource Manager si riferisce ==all'approccio uniforme e standardizzato per la gestione delle risorse in Azure. Fornisce un modello comune per la descrizione, la distribuzione, l'aggiornamento e la gestione delle risorse, indipendentemente dal tipo di servizio o risorsa utilizzata==. Ciò semplifica notevolmente l'amministrazione dell'infrastruttura e delle applicazioni in Azure, riducendo la complessità e migliorando l'efficienza operativa.

Quando invii una richiesta tramite una qualsiasi delle API, strumenti o SDK di Azure, Resource Manager riceve la richiesta: autentica e autorizza la richiesta prima di inoltrarla al servizio Azure appropriato.
Poiché tutte le richieste vengono gestite tramite la stessa API, ottieni risultati e funzionalità coerenti in tutti gli strumenti differenti.
Tutto quello che faccio sul portale di Azure posso farlo anche tramite PowerShell, Azure CLI, REST APIs e SDK.


![[consistent-management-layer.png]]

Ecco alcune caratteristiche chiave dello strato di gestione coerente di ARM:

1. [[Declarative syntax]]: ARM utilizza modelli di definizione delle risorse ([[ARM Template]] basati su JSON (JavaScript Object Notation) o YAML (YAML Ain't Markup Language) per descrivere le risorse e le relative dipendenze. Questa approccio dichiarativo consente di definire l'intera infrastruttura come codice, consentendo una gestione automatizzata, ripetibile e prevedibile.
2. Distribuzione consistente: ARM consente la distribuzione coerente delle risorse in base ai modelli di definizione delle risorse. Le distribuzioni possono essere effettuate attraverso Azure Portal, Azure CLI, PowerShell o tramite API, consentendo una flessibilità di distribuzione su larga scala.
3. Gestione delle risorse: ARM offre un set completo di strumenti per la gestione delle risorse, tra cui la possibilità di creare, modificare, aggiornare e eliminare le risorse. Consente anche di organizzare le risorse in gruppi di risorse logici per una gestione più efficiente e unificata.
4. Gestione dei cicli di vita: ARM gestisce i cicli di vita delle risorse in modo coerente, consentendo di effettuare azioni come l'aggiornamento, l'eliminazione e il rollback delle risorse in modo controllato. Ciò semplifica la gestione delle modifiche e facilita la manutenzione delle risorse nel tempo.
5. Controllo degli accessi: ARM offre un sistema di controllo degli accessi basato su ruoli (Role-Based Access Control, RBAC) che consente di assegnare autorizzazioni granulari alle risorse e di limitare l'accesso solo alle persone autorizzate. Ciò garantisce la sicurezza e la conformità delle risorse.

Grazie allo strato di gestione coerente di ARM, gli utenti possono sfruttare la potenza e la flessibilità del cloud di Azure senza dover affrontare la complessità di gestione delle risorse individuali. L'approccio standardizzato semplifica l'automazione, la distribuzione e la gestione delle risorse, consentendo di ottenere un'efficienza operativa superiore e una maggiore agilità nello sviluppo e nella distribuzione delle applicazioni in Azure.
