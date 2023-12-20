---
tags:
  - Azure
  - PaaS
---
In Azure, un "Resource Provider" (Fornitore di Risorse) è un servizio che implementa e gestisce le operazioni su un determinato tipo di [[Resource - Azure|Resource]].
==Ogni tipo di risorsa in Azure è associato a un Resource Provider specifico che fornisce le operazioni per creare, gestire e interagire con quella risorsa==.

Ogni Resource Provider definisce il modo in cui le risorse di un determinato tipo possono essere create, configurate, aggiornate o eliminate. Ad esempio, il Resource Provider `Microsoft.Compute` gestisce le operazioni per la creazione e la gestione delle macchine virtuali, mentre il Resource Provider `Microsoft.Storage` gestisce le operazioni per la creazione e la gestione dei servizi di archiviazione.

==Quando si interagisce con una risorsa in Azure, sia tramite l'interfaccia utente di Azure Portal, la riga di comando di Azure (Azure CLI) o le API di Azure, si comunica effettivamente con il Resource Provider corrispondente. Il Resource Provider si occupa di elaborare la richiesta e di eseguire le operazioni specifiche per quella risorsa.==

Inoltre, Azure supporta sia Resource Provider forniti da Microsoft che Resource Provider personalizzati creati dagli utenti. I Resource Provider personalizzati consentono agli utenti di estendere Azure aggiungendo nuovi tipi di risorse che soddisfano le esigenze specifiche delle loro applicazioni o soluzioni.