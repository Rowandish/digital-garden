---
tags:
  - Coding
  - CSharp
  - Memory
  - PublishedPosts
---
L'istruzione `using` fornisce una sintassi utile che garantisce l'utilizzo corretto degli oggetti `IDisposable`.
Cominciamo con un esempio:
```csharp
using (Font font1 = new Font("Arial", 10.0f)) 
{
	byte charset = font1.GdiCharSet;
}
```
`Font` (come `File`) è un classico esempio di un tipo *managed* che accede a risorse *unmanaged*, come handle di file o contesti di dispositivo.

Tutti questi tipi **devono** implementare l'interfaccia `IDisposable`.

Quando si utilizza un oggetto `IDisposable`, è di norma **dichiararlo e crearne un'istanza in un'istruzione using**.

L'istruzione `using` chiama il metodo `Dispose` sull'oggetto nel modo corretto e **fa in modo che l'oggetto stesso esca dallo scope non appena viene chiamato il metodo Dispose**.

All'interno del blocco using, **l'oggetto è di sola lettura** e non può essere modificato né riassegnato.

L'istruzione `using` assicura che venga **chiamato il metodo Dispose anche se si verifica un'eccezione** mentre vengono chiamati metodi sull'oggetto.

È possibile ottenere lo stesso risultato inserendo l'oggetto in un blocco `try` e chiamando il metodo `Dispose` in un blocco `finally`, in quanto l'istruzione `using` viene tradotta in questo modo dal compilatore.

Il codice indicato sopra che utilizza il blocco `using` è esattamente analogo a questo (le parentesi graffe aggiuntive limitano lo scope dell'oggetto):
```csharp
{
Font font1 = new Font("Arial", 10.0f);
try
{
	byte charset = font1.GdiCharSet;
}
finally
{
if (font1 != null)
	((IDisposable)font1).Dispose();
}
}
```
E' possibile inizializzare più istanze nello stesso blocco `using`, cosa che rende estremamente più leggibile il codice:
```csharp
using (Font font3 = new Font("Arial", 10.0f),
font4 = new Font("Arial", 10.0f))
{
// Use font3 and font4.
}
```
E' possibile inizializzare un oggetto e successivamente passare l'istanza al blocco `using`, anche se **non è una pratica consigliata** in quanto l'oggetto rimane nello scope del metodo anche se probabilmente non ha più accesso alle sue risorse *unmanaged* e il tentativo di utilizzarlo al di fuori del blocco `using` potrebbe causare un'eccezione.
```csharp
Font font2 = new Font("Arial", 10.0f);
using (font2) // not recommended
{
// use font2
}
// font2 is still in scope
// but the method call throws an exception
float f = font2.GetHeight();
```