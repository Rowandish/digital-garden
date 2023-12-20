---
tags:
  - Coding
  - CSharp
  - Testing
  - PublishedPosts
---


Per lo sviluppo di codice di buona qualità è necessario associare il proprio codice a dei test, che siano unit test, integration test o end to end test.

Uno dei primi problemi a cui si incorre è capire come effettuare il naming del progetto di test, la classe e i test stessi.

Assumiamo di avere un progetto chiamato `MyMathLibrary` che contiene una classe chiamata `MyMath` di funzioni matematiche custom della mia applicazione.

## Naming del progetto

Per prima cosa è importante sottolineare che tutti i progetti di test devono essere raggruppati in una cartella ad hoc, in modo che non siano confusi con il codice effettivo; è una buona idea collocare il proprio codice in `src` e i test in `test`.

Una volta creata la cartella è necessario creare il progetto di test per `` `MyMathLibrary` ``, in particolare il nome deve dipendere dalla tipologia di test:

<table><tbody><tr><td><strong>Tipologia di test</strong></td><td><strong>Nome</strong></td></tr><tr><td>Unit</td><td><code><code>MyMathLibrary</code></code>.<code>Tests.Unit</code></td></tr><tr><td>Integration</td><td><code><code>MyMathLibrary</code></code>.<code>Tests.Integration</code></td></tr><tr><td>End to End</td><td><code><code>MyMathLibrary</code></code>.<code>Tests.E2E</code></td></tr></tbody></table>

Come si vede il progetto di test è estremamente parlante in quanto indica il progetto testato e la tipologia di test che possiamo trovare al suo interno.
![[immagine-2.png]]

## Naming della classe

La classe che testa `MyMath` si può chiamare `MyMath.Tests` in modo che sia esplicito già dal nome la classe che sto testando.

## Naming del test

Il nome del test deve seguire lo stile `Metodo_Should_When`", in particolare dovrà quindi indicare dopo lo `Should` cosa dovrebbe fare e dopo il `When` in che caso dovrebbe fare quanto indicato.

Assumiamo che all'interno della mia classe `MyMath` vi sia il metodo `Log` che fa un logaritmo; il nome del test dovrebbe essere analogo a: `Log_ShouldCalculateLogOfANumber_WhenIntegerNumberIsGiven`.

![[immagine-3.png]]

Esempio di metodo e del suo test con [xUnit](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjQqu-l99_2AhWNwQIHHcY0CpAQFnoECAYQAQ&url=https%3A%2F%2Fxunit.net%2F&usg=AOvVaw03TH1vZafC4jC9G3dZZS6d)
