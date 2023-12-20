---
tags:
  - Coding
  - CSharp
  - Memory
  - PublishedPosts
---


Talvolta è necessario dover interagire con librerie non gestite (DLL esterne) e accedere a delle loro strutture dati che si trovano nella memoria unmanaged.
Il metodo `PtrToStructure<T>` presentato qui fornisce un modo efficiente per ottenere una struct gestita di tipo `T` da un puntatore `IntPtr` alla memoria non gestita.
Il framework fornisce già il metodo `Marshal.PtrToStructure<T>(IntPtr)` ma, nella sua implementazione interna, utilizza `object` e conseguentemente porta a del boxing con conseguente allocazione sullo [[Heap]].

## Implementazione
Il metodo è molto semplice, utilizza il metodo `Unsafe.AsRef<T>` per eseguire una conversione efficiente senza causare boxing.
```csharp
public static unsafe T PtrToStructure<T>(IntPtr ptr) where T : struct
{
    return Unsafe.AsRef<T>(ptr.ToPointer());
}
```

## Esempio

Supponiamo di avere una libreria non gestita che fornisce una `struct`, ad esempio:
```c
// C code (Unmanaged library)
typedef struct Point {
    int x;
    int y;
} Point;
```

Per utilizzare questa `struct` in un'applicazione C# gestita, definiremo una `struct` corrispondente e useremo il metodo `PtrToStructure<T>` per convertire il puntatore alla memoria non gestita in un oggetto gestito:

```csharp
// C# code (Managed application)

// voglio che i campi vengano disposti in memoria nello stesso ordine in cui sono dichiarati nella struct, quindi prima X, poi Y
[StructLayout(LayoutKind.Sequential)]
public struct Point
{
    public int X;
    public int Y;
}

public static class NativeMethods
{
    [DllImport("unmanaged_library.dll")]
    public static extern IntPtr GetUnmanagedPoint();
}

public class Program
{
    public static void Main()
    {
        IntPtr unmanagedPtr = NativeMethods.GetUnmanagedPoint();
        Point managedPoint = PtrToStructure<Point>(unmanagedPtr);
        Console.WriteLine($"X: {managedPoint.X}, Y: {managedPoint.Y}");
    }
}
```

### L'importanza di `StructLayout Sequential`
L'attributo `StructLayout(LayoutKind.Sequential)` viene utilizzato per controllare la disposizione dei membri di una `struct` in memoria, in particolare garantisce che i **campi della `struct` vengano disposti in memoria nello stesso ordine in cui vengono dichiarati**.
Il compilatore non può quindi riorganizzare i campi per ottimizzare l'allocazione di memoria o per altri motivi.

Questo è particolarmente importante quando si lavora con codice non gestito poiché è necessario garantire che la `struct` gestita corrisponda esattamente alla `struct` non gestita in termini di layout in memoria.

## Potenzialità
- **Prestazioni migliorate**: Il metodo `PtrToStructure<T>` offre un vantaggio in termini di prestazioni rispetto a `Marshal.PtrToStructure<T>(IntPtr)` poiché evita il boxing e conseguentemente non alloca nulla sullo heap.
- **Flessibilità**: Funziona con qualsiasi tipo di struct, rendendolo flessibile e adattabile a diverse situazioni.

## Limiti
- **Sicurezza**: È importante assicurarsi di utilizzare questo metodo solo con puntatori validi e con `struct` correttamente definite; essendo un metodo `Unsafe` ho meno controllo sui casi di errore. Devo essere certo che l'`IntPtr` in questione punti effettivamente al tipo `T` da me richiesto.
- **Compatibilità**: L'utilizzo di `Unsafe.AsRef<T>` potrebbe non essere supportato su tutte le piattaforme o in tutti i contesti.

## AccessViolationException
Dato che il metodo opera a basso livello utilizzando funzionalità "unsafe" devo pensare all'eventualità di una `AccessViolationException`.
Questa eccezione viene generata quando si tenta di leggere o scrivere memoria protetta o non valida. Può verificarsi se il puntatore `IntPtr` fornito al metodo `PtrToStructure<T>` non è valido o se punta a una zona di memoria protetta.

Esempio: Se il puntatore `IntPtr` restituito dalla funzione non gestita punta a una zona di memoria non accessibile, chiamando `PtrToStructure<T>` si otterrà un'eccezione `AccessViolationException`.
```csharp
IntPtr invalidPtr = new IntPtr(0x12345678); // Puntatore non valido
Point managedPoint = PtrToStructure<Point>(invalidPtr); // AccessViolationException
```