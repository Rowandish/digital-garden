Assumiamo di avere un progetto chiamato `MyMathLibrary` che contiene una classe chiamata `MyMath` di funzioni matematiche custom della mia applicazione.

### Naming del progetto
Per prima cosa è importante sottolineare che tutti i progetti di test devono essere raggruppati in una cartella ad hoc, in modo che non siano confusi con il codice effettivo; è una buona idea collocare il proprio codice in una cartella `src` e i test in una cartella in `test`.

Una volta creata la cartella è necessario creare il progetto di test per `` `MyMathLibrary` ``, in particolare il nome deve dipendere dalla tipologia di test:

| Tipologia di test | Nome                              |
| ----------------- | --------------------------------- |
| Unit              | `MyMathLibrary.Tests.Unit`        |
| Integration       | `MyMathLibrary.Tests.Integration` |
| End to End        | `MyMathLibrary.Tests.E2E`         |
Come si vede il progetto di test è estremamente parlante in quanto indica il progetto testato e la tipologia di test che possiamo trovare al suo interno.

### Naming della classe

La classe di test si chiamerà con lo stesso nome della classe originale con la stringa `Tests` in fondo, quindi nel caso di `MyMath` questa si chiamerà `MyMathTests`.

### Naming del test

#### .NET
Il nome del test deve seguire lo stile `Method_Should_When`", in particolare dovrà quindi indicare dopo lo `Should` cosa dovrebbe fare e dopo il `When` in che caso dovrebbe fare quanto indicato.

Assumiamo che all'interno della mia classe `MyMath` vi sia il metodo `Log` che fa un logaritmo; il test sarà così scritto.
```csharp
[Fact]  
public void Log_ShouldCalculateLogOfANumber_WhenIntegerNumberIsGiven()  
{  
    // Test  
}
```

#### ASP.NET
Nel caso di integration testing di API in ASP.NET il nome sarà `HttpMethod_ReturnsXXX_WhenYYY`, quindi prima va il nome del protocollo, poi il codice di ritorno (200, 404...) o l'oggetto ritornato e infine quando questo accade:
```csharp
[Fact]  
public void Get_ReturnsNotFound_WhenIntegerNumberIsGiven()  
{  
    // Test  
}
```

### System Under Test
Per convenzione l'oggetto che viene testato si chiama "System Under Test", abbreviato con `sut`.
```csharp
private readonly ClassToTest _sut = new();
```