---
tags:
  - Azure
  - PaaS
---
Nell'ambito di [[Azure Resource Manager]] (ARM), "declarative syntax" (sintassi dichiarativa) si riferisce a un approccio per descrivere le risorse e la configurazione dell'infrastruttura in Azure utilizzando modelli basati su JSON o YAML.

==Invece di specificare dettagliatamente le operazioni da eseguire per creare o configurare le risorse, la sintassi dichiarativa consente di dichiarare lo stato desiderato dell'ambiente. In altre parole, si descrive cosa si vuole ottenere, piuttosto che come farlo==.

Il file descrittivo si chiama [[ARM Template]]; questo file, ad esempio, può descrivere la creazione di una macchina virtuale, una rete virtuale, un'istanza di database e così via, insieme alle relative impostazioni e configurazioni.

Ecco un esempio di un frammento di codice JSON che rappresenta una risorsa di macchina virtuale in un ARM template:

```json
{
  "type": "Microsoft.Compute/virtualMachines",
  "name": "myVirtualMachine",
  "apiVersion": "2022-03-01",
  "location": "westus",
  "properties": {
    "hardwareProfile": {
      "vmSize": "Standard_DS2_v2"
    },
    "storageProfile": {
      "imageReference": {
        "publisher": "MicrosoftWindowsServer",
        "offer": "WindowsServer",
        "sku": "2019-Datacenter",
        "version": "latest"
      },
      "osDisk": {
        "name": "osdisk",
        "caching": "ReadWrite",
        "createOption": "FromImage"
      }
    },
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "[resourceId('Microsoft.Network/networkInterfaces', 'myNetworkInterface')]"
        }
      ]
    }
  }
}
```

Utilizzando la sintassi dichiarativa, è possibile definire in modo strutturato e leggibile le risorse, le proprietà e le relative configurazioni all'interno di un modello ARM. Questo modello può quindi essere utilizzato per distribuire e gestire in modo coerente e ripetibile l'infrastruttura e le applicazioni in Azure.

L'approccio dichiarativo offre vantaggi come la tracciabilità delle modifiche, la possibilità di versionare e gestire il codice del modello, la riproducibilità delle distribuzioni e la facilità di automazione e gestione del ciclo di vita delle risorse.

Complessivamente, la sintassi dichiarativa nell'ottica di Azure Resource Manager consente di definire l'ambiente Azure desiderato in modo chiaro e conciso, promuovendo una gestione efficiente e scalabile delle risorse in Azure.