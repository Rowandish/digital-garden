#Dometrain 

AWS Secrets Manager è un gestore di chiavi private come credenziali di database, API Keys e password.
Oltre allo storage offre la possibilità di versionare i segreti, quindi mantenerne uno storico e di ruotarli, quindi ogni tot tempo questi vengono automaticamente modificati tramite una [[Lambda]]. in questo modo anche se un secret viene leakato dopo poco tempo si invalida e viene automaticamente ruotato con uno nuovo.
Questo ha l'obiettivo di evitare di includere credenziali nei codici sorgenti.
## Pricing
Free trial di 30 giorni e poi 40 cent per secret e 0.05€ ogni 10k API call.

## ASP.NET
L'obiettivo è avere il secrete nelle mie `Ioptions` come se fossero nel file `appsettings.json` senza che il secret ci sia effettivamente.
Per prima cosa creo il secret in AWS con la sintassi
`{ASPNETCORE_ENVIRONMENT}_{AssemblyName}_{ChiaveAppSettings.json}:{SottoChiaveAppSettings.json}`.
* L'environment lo si trova in `Properties/launchsettings.json` con chiave `environmentVariables->ASPNETCORE_ENVIRONMENT` e per esempio assume il valore `Development`.
* `AssemblyName` è il nome del progetto, per esempio `Weather.Api`
* `ChiaveAppSettings.json` è il nome della chiave in `appsettings.json` qualora il secret sia lì. in questo modo il codice utilizzatore sarà identico che la chiave sia in `appsettings.json` o in `AWS Secrets Manager`. Esempio `OpenWeatherMapApi`
* `SottoChiaveAppSettings.json` all'interno della chiave sopra ci sarà una chiave, che è questa, il cui valore è la `key` in questione che sto cercando. Esempio `ApiKey`.


Per fare questo utilizzo il pacchetto nuget `Kralizek.Extensions.Configuration.AWSSecretsManager` e aggiungo queste righe per fare il mapping.
Se invece di `IOptions` utilizzo `IOptsionsMonitor` posso usare anche la rotazione, impostando un `PollingInterval` ogni tot viene richiesto il valore del secret ad AWS ed eventualmente aggiornato.

```csharp
builder.Configuration.AddSecretsManager(configurator: options =>
{
    options.SecretFilter = entry => entry.Name.StartsWith($"{env}_{appName}");
    options.KeyGenerator = (_, s) => s
        .Replace($"{env}_{appName}_", string.Empty);
    options.PollingInterval = TimeSpan.FromMinutes(10);
});
```
