---
tags:
  - Azure
  - PaaS
---
Azure Policy è un servizio di Azure che consente di definire e applicare ==regole di conformità e governance all'interno dell'ambiente Azure==.
Fornisce un framework per stabilire e far rispettare le regole e le pratiche consigliate per le risorse e i servizi di Azure utilizzati dalle organizzazioni.

Azure Policy consente di definire regole e criteri che specificano ==le condizioni, le restrizioni e le azioni da applicare alle risorse in Azure==. Queste regole possono riguardare diverse aree, come sicurezza, conformità, governance, performance e organizzazione delle risorse.

Ecco alcuni punti chiave delle Azure Policy:
1. **Definizione delle regole**: Azure Policy consente di definire regole personalizzate utilizzando il linguaggio di definizione delle regole di Azure Policy (JSON). Queste regole specificano le condizioni che devono essere rispettate dalle risorse, come l'utilizzo di versioni specifiche di servizi, la configurazione delle impostazioni di rete o l'applicazione di tag.
2. **Applicazione delle regole**: Le regole di Azure Policy possono essere applicate a livelli di ambito specifici, come la sottoscrizione, il gruppo di risorse o le risorse stesse. Le regole vengono valutate in modo continuo per garantire la conformità delle risorse alle condizioni specificate.
3. **Valutazione e rimedio**: Azure Policy valuta le risorse in base alle regole definite e fornisce una valutazione dello stato di conformità. In caso di violazione delle regole, Azure Policy può attivare azioni correttive automatiche o notificare gli amministratori per prendere provvedimenti.
4. **Integrazione con [[Azure Resource Manager]]**: Azure Policy è integrato con Azure Resource Manager, consentendo di applicare le regole durante la distribuzione delle risorse e di garantire che le risorse esistenti siano conformi alle regole definite.
5. **Monitoraggio e reporting**: Azure Policy offre funzionalità di monitoraggio e reportistica per tenere traccia dello stato di conformità delle risorse, identificare le violazioni e generare report per l'audit e la conformità.

Con Azure Policy, le organizzazioni possono applicare e far rispettare le politiche e le regole specifiche, migliorando la sicurezza, la conformità e la governance delle risorse in Azure. Consentono di implementare standard di best practice, evitare configurazioni errate o non sicure e garantire la coerenza e l'organizzazione delle risorse all'interno dell'ambiente Azure.