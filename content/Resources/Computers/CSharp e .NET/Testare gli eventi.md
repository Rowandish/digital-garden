---
tags:
  - Coding
  - CSharp
  - Testing
  - PublishedPosts
---


Testare che degli eventi siano stato effettivamente lanciati in C# non è immediato.

Tipicamente è possibile testare che un evento venga lanciato aspettando un [[ManualResetEvent]] che viene settato in un listener dell'evento stesso.

Questo metodo funziona ma risulta un po' macchinoso; Fluent Assertion risolve il problema fornendo dei metodi comodi per testare il tutto.

## Fluent Assertion

[Fluent Assertion](https://fluentassertions.com/) permette di testare che un determinato evento venga lanciato in modo semplice.

Per prima cosa è necessario comunicare a Fluent Assertion che voglio monitorare l'oggetto utilizzando il l'extension `Monitor()`;
```csharp
using var monitoredClass = _myClass.Monitor();
```
e successivamente è possibile utilizzare il check `Should().Raise("EventName")` in questo modo:
```csharp
monitoredClass.Should().Raise(nameof(myClass.MyCustomEvent));
```
E' possibile anche aggiungere dei check sul `sender` e sugli `args` in questo modo:
```csharp
monitoredClass.Should()
            .Raise(nameof(myClass.MyCustomEvent))
            .WithSender(subject)
            .WithArgs<PropertyChangedEventArgs>(args => args.PropertyName == "SomeProperty");
```
> [!tip] Non raisare eventi a costruttore
> Gli eventi a costruttore non possono essere presi da nessuno in quanto non potrò mai fare il +=.

## Esempio completo

Di seguito un esempio completo di una classe di test per gli eventi.
```csharp
using System;
using FluentAssertions;
using Xunit;

namespace Tests;

public class CustomEventArgs : EventArgs
{
    public CustomEventArgs(string param)
    {
        Param = param;
    }

    public string Param { get; }
}

public class ClassToTest
{
    public void MethodThatRaisesEvent()
    {
        // Do something
        RaiseMyCustomEventEvent();
        // Do something else
    }

    public void MethodThatRaisesEventWithArgs(string arg)
    {
        // Do something
        RaiseMyCustomEventWithArgsEvent(arg);
        // Do something else
    }

    public static void MethodThatDoNotRaiseEvent()
    {
        // Do nothing
    }

#region MyCustomEvent

    public delegate void MyCustomEventEventHandler(object sender, EventArgs e);

    public event MyCustomEventEventHandler MyCustomEvent;

    private void RaiseMyCustomEventEvent()
    {
        MyCustomEvent?.Invoke(this, EventArgs.Empty);
    }

#endregion

#region MyCustomEventWithArgs

    public delegate void MyCustomEventWithArgsEventHandler(object sender, CustomEventArgs e);

    public event MyCustomEventWithArgsEventHandler MyCustomEventWithArgs;

    private void RaiseMyCustomEventWithArgsEvent(string arg)
    {
        MyCustomEventWithArgs?.Invoke(this, new CustomEventArgs(arg));
    }

#endregion
}

public class TesterClass
{
    private readonly ClassToTest _myClass = new();

    [Fact]
    public void TestEventIsRaised()
    {
        using var monitoredClass = _myClass.Monitor();
        _myClass.MethodThatRaisesEvent();
        monitoredClass.Should().Raise(nameof(ClassToTest.MyCustomEvent));
    }

    [Fact]
    public void TestEventAndArgsIsRaised()
    {
        const string arg = "foo";
        using var monitoredClass = _myClass.Monitor();
        _myClass.MethodThatRaisesEventWithArgs(arg);
        monitoredClass.Should().Raise(nameof(ClassToTest.MyCustomEventWithArgs))
            .WithSender(_myClass)
            .WithArgs<CustomEventArgs>(args => args.Param == arg);
    }

    [Fact]
    public void TestEventIsNotRaised()
    {
        using var monitor = _myClass.Monitor();
        ClassToTest.MethodThatDoNotRaiseEvent();
        monitor.Should().NotRaise(nameof(ClassToTest.MyCustomEvent));
    }
}
```