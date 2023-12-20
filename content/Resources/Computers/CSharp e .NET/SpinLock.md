---
tags:
  - Coding
  - CSharp
  - Multithreading
---


Lo struct `SpinLock` permette di mettere in pausa un Thread in caso di accesso a risorse condivise utilizzando lo spinning, quindi facendogli fare del lavoro inutile in loop.

Viene utilizzato negli stessi casi del costrutto `lock` (anche se in questo caso non ho la sintassi comoda), quindi quando voglio evitare un accesso contemporaneo alla stessa risorsa.
```csharp
var spinLock = new SpinLock(true);
var lockTaken = false;
try
{
    // lockTaken rimane a false dopo aver chiamato Enter se e solo se
    // il metodo Enter lancia una Eccezione e il lock non era stato ancora preso da nessuno
    spinLock.Enter(ref lockTaken);
    // Accesso a risorse critiche...
}
finally
{
    // Esco dallo SpinLock se lo ho preso
    if (lockTaken)
        spinLock.Exit();
}
```