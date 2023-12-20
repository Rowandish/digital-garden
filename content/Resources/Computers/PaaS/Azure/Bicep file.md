---
tags:
  - Azure
  - PaaS
---
I file "Bicep" in [[Azure Resource Manager]] (ARM) sono un linguaggio di descrizione delle risorse (DSL, Domain-Specific Language) basato su un formato dichiarativo che semplifica la creazione e la gestione delle [[Resource - Azure|risorse]] in Azure.
==Bicep è stato sviluppato come un'alternativa più intuitiva e leggibile ai file JSON per la definizione delle risorse di Azure.==

I file Bicep utilizzano un'estensione di file ".bicep" e offrono una sintassi semplificata e più concisa rispetto ai file JSON tradizionali di ARM. Questo linguaggio consente di definire le risorse, le loro proprietà e le dipendenze in modo dichiarativo, facilitando la creazione e la gestione delle risorse in Azure.

Bicep si basa sulla stessa semantica di Azure Resource Manager, consentendo di utilizzare tutti i concetti e le funzionalità disponibili nei modelli ARM tradizionali. Tuttavia, la sintassi Bicep offre numerosi miglioramenti, tra cui:
1. Sintassi più concisa: Bicep riduce la complessità sintattica dei file JSON, semplificando la lettura e la scrittura dei modelli di risorse.
2. Gestione delle dipendenze semplificata: Bicep semplifica la gestione delle dipendenze tra le risorse, consentendo di specificare in modo più chiaro l'ordine di creazione e le relazioni tra le risorse.
3. Riuso del codice: Bicep supporta il riuso del codice attraverso la definizione di moduli, che consentono di creare componenti riutilizzabili e di organizzare il codice in modo modulare.
4. Validazione e compilazione statica: Bicep offre un'esperienza di sviluppo migliorata con validazione e compilazione statica dei file, rilevando errori e suggerendo correzioni durante la fase di sviluppo.

==Per utilizzare i file Bicep, è necessario prima compilare il file Bicep in un file JSON equivalente utilizzando il compilatore Bicep==. Il file JSON risultante può quindi essere distribuito e gestito utilizzando le stesse strumentazioni e meccanismi di distribuzione di Azure Resource Manager.

Complessivamente, i file Bicep semplificano la creazione e la gestione delle risorse in Azure, offrendo una sintassi più leggibile e intuitiva rispetto ai file JSON tradizionali. Consentono agli sviluppatori di definire l'infrastruttura come codice in modo più efficiente, migliorando la produttività e la manutenibilità delle risorse in Azure.

## Esempio

Ecco un esempio di un file Bicep che definisce una risorsa di database MySQL in Azure:

File Bicep (esempio.bicep):

```bicep
param dbName string
param serverName string
param adminLoginName string
param adminLoginPassword securestring

resource mySqlServer 'Microsoft.DBforMySQL/servers@2020-12-01' = {
  name: serverName
  location: resourceGroup().location
  properties: {
    administratorLogin: adminLoginName
    administratorLoginPassword: adminLoginPassword
  }
}

resource mySqlDatabase 'databases@2020-12-01' = {
  name: '${serverName}/${dbName}'
  dependsOn: [mySqlServer]
  properties: {
    charset: 'utf8'
    collation: 'utf8_general_ci'
  }
}
```

Per compilare il file Bicep e ottenere il corrispondente file JSON, puoi utilizzare il compilatore Bicep. Puoi farlo eseguendo il seguente comando da riga di comando:

```bash
bicep build esempio.bicep
```

Il comando di compilazione genererà un file JSON compilato che corrisponde al file Bicep:

File JSON compilato (esempio.json):

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "dbName": {
      "type": "string"
    },
    "serverName": {
      "type": "string"
    },
    "adminLoginName": {
      "type": "string"
    },
    "adminLoginPassword": {
      "type": "securestring"
    }
  },
  "resources": [
    {
      "type": "Microsoft.DBforMySQL/servers",
      "apiVersion": "2020-12-01",
      "name": "[parameters('serverName')]",
      "location": "[resourceGroup().location]",
      "properties": {
        "administratorLogin": "[parameters('adminLoginName')]",
        "administratorLoginPassword": "[parameters('adminLoginPassword')]"
      }
    },
    {
      "type": "databases",
      "apiVersion": "2020-12-01",
      "name": "[concat(parameters('serverName'), '/', parameters('dbName'))]",
      "dependsOn": [
        "[parameters('serverName')]"
      ],
      "properties": {
        "charset": "utf8",
        "collation": "utf8_general_ci"
      }
    }
  ]
}
```

Il file JSON compilato può quindi essere utilizzato per distribuire e gestire la risorsa del database MySQL in Azure utilizzando Azure Resource Manager.