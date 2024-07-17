---
tags:
  - Coding
  - CreationalDesignPattern
  - PublishedPosts
---
Questo pattern è uno dei pattern creazionali più usati che ha lo scopo di garantire che di una determinata classe venga **creata una e una sola istanza**, e di fornire un punto di accesso globale a tale istanza.
E' un pattern estremamente semplice nella sua struttura in quanto è formato da una sola classe, che è la classe in questione.
La classe singleton **ha un unico costruttore privato, in modo da impedire l’istanziazione diretta della classe**.
La classe fornisce inoltre un metodo “getter” statico che restituisce una istanza della classe (sempre la stessa), creandola preventivamente o alla prima chiamata del metodo, e memorizzandone il riferimento in un attributo privato anch’esso statico.
Ogni linguaggio possiede dei trucchi per poter scrivere una classe singleton, il codice indicato qui (preso da http://www.dofactory.com/net/singleton-design-pattern) è ottimizzato per .NET, utilizzando le feature che lo contraddistinguono.


```csharp
private class MainApp
{
/// <summary>
/// Codice Main() della console application.
/// </summary>
private static void Main()
{
//Creo due LoadBalancer e verifico che siano la stessa istanza
LoadBalancer b1 = LoadBalancer.GetLoadBalancer();
LoadBalancer b2 = LoadBalancer.GetLoadBalancer();
if (b1 == b2)
Console.WriteLine("Same instance\n");
}
}

/// <summary>
/// LoadBalancer è la classe singleton che voglio implementare
/// La classe è definita sealed per sottolineare il fatto che non può avere classi derivate
/// </summary>
private sealed class LoadBalancer
{
// Gli attributi statici di una classe sono inizializzati quando la classe è caricata per la prima volta
// Tramite l'attributo readonly impongo che, una volta che viene fatto il load della classe, il valore di _instance non
// possa più essere cambiato (ricordo che readonly agisce al caricamento della classe, il const invece durante la compilazione)
//Inoltre questa operazione è thread safe di default
private static readonly LoadBalancer _instance = new LoadBalancer();

// Attributo della classe: una lista di server
private List<Server> _servers;

//Il costruttore è privato e non può essere chiamato dall'esterno
private LoadBalancer()
{
// Il costruttore istanzia una nuova lista di server
_servers = new List<Server>
{
new Server{ Name = "ServerI", IP = "120.14.220.18" },
new Server{ Name = "ServerII", IP = "120.14.220.19" }
};
}

// Per avere l'istanza della classe utilizzo questo metodo, che non fa altro che ritornare la variabile _instance
public static LoadBalancer GetLoadBalancer()
{
return _instance;
}
}
```

## Problemi
Il problema del pattern singleton è che porta a codice non testabile: come faccio a modificare l'istanza in questione nei test se questa e una e immutabile?
L'utilizzo di tale pattern porta spesso a dei code smell simili a quelli di utilizzare classi statiche o variabili globali.
La soluzione è utilizzare la DI per iniettare a costruttore delle classi normali ed è nella DI che dichiaro tale classe come singleton o meno.
In questo modo posso testare la classe che riceve l'oggetto singleton semplicemente modificando la DI con una nuova istanza da costruire.