---
tags:
  - Azure
  - PaaS
---
==In Azure, il concetto di "Resource" si riferisce a qualsiasi risorsa gestita all'interno dell'ambiente Azure.==
Una risorsa può essere qualsiasi elemento che venga creato, distribuito e gestito in Azure, come ad esempio una macchina virtuale, un database, un'applicazione Web, una rete virtuale, un servizio di archiviazione, un'applicazione di logica e molti altri.

Ogni risorsa in Azure viene gestita da un oggetto chiamato "[[Azure Resource Manager]]". Questo oggetto contiene tutte le informazioni associate alle risorse, come il tipo di risorsa, le impostazioni di configurazione, gli attributi e i metadati.
Il Resource Manager consente di organizzare e gestire le risorse in modo logico e coerente, fornendo funzionalità di gestione unificate per l'intero ciclo di vita delle risorse.
Il "motore" che effettivamente lavora sotto il cofano di una risorsa è il [[Resource Provider]].
Ogni risorsa si può descrivere mediante la "[[Declarative syntax]]" che consente di  dichiarare lo stato desiderato dell'ambiente tramite file JSON o YAML.

**Ogni risorsa in Azure è identificata da un nome univoco all'interno di una sottoscrizione Azure e viene assegnata a un gruppo di risorse (resource group)**.
==Un resource group è un contenitore logico che tiene insieme le risorse correlate per un'applicazione o un progetto specifico==. Ad esempio, se si sta creando un'applicazione web, si potrebbero avere risorse come una macchina virtuale, un database e un servizio di archiviazione, e tutte queste risorse possono essere collocate nello stesso gruppo di risorse per una gestione più semplice.

Le risorse in Azure possono essere create, modificate, aggiornate e eliminate utilizzando l'interfaccia utente di Azure Portal, la riga di comando di Azure (Azure CLI) o le API di Azure. Inoltre, Azure offre servizi aggiuntivi come la gestione delle identità e degli accessi, il monitoraggio delle risorse, la sicurezza e la conformità per garantire la sicurezza e la disponibilità delle risorse.


