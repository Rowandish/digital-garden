---
tags:
  - Azure
  - PaaS
---
Nell'ambito di [[Azure Resource Manager]] (ARM), un "ARM template" (modello ARM) è un file che definisce l'infrastruttura e le risorse desiderate all'interno di un ambiente Azure utilizzando la [[Declarative syntax]].

Un ARM template è scritto in formato JSON (JavaScript Object Notation) o YAML (YAML Ain't Markup Language) e ==descrive le risorse da creare, configurare e distribuire, insieme alle relative proprietà e dipendenze. Il modello definisce l'intera topologia dell'applicazione o dell'infrastruttura da implementare, inclusi servizi, reti, macchine virtuali, database, account di archiviazione e altro ancora==.

Un template ARM può essere utilizzato per automatizzare il provisioning e la gestione delle risorse in Azure. Attraverso l'uso di un template, è possibile definire l'intera infrastruttura come codice, consentendo una distribuzione consistente, prevedibile e ripetibile. Inoltre, i template ARM offrono vantaggi come il tracciamento delle modifiche, la gestione del ciclo di vita delle risorse e la possibilità di versionare e condividere il codice del modello.

Un esempio di un template ARM potrebbe includere la definizione di una rete virtuale, una macchina virtuale e un servizio di bilanciamento del carico, insieme alle relative configurazioni, come ad esempio gli indirizzi IP, le subnet, le immagini delle macchine virtuali e le porte di bilanciamento del carico.

Utilizzando uno strumento come Azure Portal, Azure CLI o PowerShell, è possibile distribuire un modello ARM nel proprio account Azure. Durante la distribuzione, il template viene interpretato da Azure Resource Manager, che crea e configura le risorse specificate nel modello. In caso di modifiche o aggiornamenti alle risorse, è possibile apportare modifiche al template e distribuirlo nuovamente per applicare le modifiche in modo coerente.

Complessivamente, gli ARM template offrono un modo potente per automatizzare e gestire l'infrastruttura e le risorse in Azure, consentendo una distribuzione coerente, scalabile e prevedibile delle applicazioni e dei servizi cloud.

## Esempio di ARM Template per un db MySql

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "databaseName": {
      "type": "string",
      "metadata": {
        "description": "Il nome del database MySQL."
      }
    },
    "serverName": {
      "type": "string",
      "metadata": {
        "description": "Il nome del server MySQL."
      }
    },
    "administratorLogin": {
      "type": "string",
      "metadata": {
        "description": "Il nome utente amministratore del server MySQL."
      }
    },
    "administratorLoginPassword": {
      "type": "securestring",
      "metadata": {
        "description": "La password per l'utente amministratore del server MySQL."
      }
    }
  },
  "resources": [
    {
      "type": "Microsoft.DBforMySQL/servers",
      "apiVersion": "2020-12-01",
      "name": "[parameters('serverName')]",
      "location": "[resourceGroup().location]",
      "properties": {
        "administratorLogin": "[parameters('administratorLogin')]",
        "administratorLoginPassword": "[parameters('administratorLoginPassword')]"
      },
      "resources": [
        {
          "type": "databases",
          "apiVersion": "2020-12-01",
          "name": "[concat(parameters('serverName'), '/', parameters('databaseName'))]",
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
  ]
}

```
