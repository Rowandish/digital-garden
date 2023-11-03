---
tags:
  - Coding
  - CSharp
  - Memory
---


La classe `Memory<T>` è una struttura di dati introdotta in C# a partire dalla versione 7.2 nell'ottica di migliorare la gestione e l'allocazione della memoria in .NET, riducendo l'uso dello heap e migliorando le prestazioni delle applicazioni.

==`Memory<T>` è una struttura utilizzata per rappresentare una regione contigua di memoria, che può essere sia sullo heap che sullo stack==. La sua caratteristica principale è di consentire l'accesso a una porzione di memoria senza copiarne i dati, riducendo così l'overhead legato all'allocazione e alla gestione della memoria sullo heap.

`Memory<T>` è particolarmente utile nei contesti in cui si lavora con grandi quantità di dati, ad esempio quando si elaborano buffer o flussi di dati. Inoltre, `Memory<T>` è più flessibile rispetto alla classe `Span<T>`, dato che può essere utilizzata all'interno di metodi asincroni.

## Analogie con Span
1.  Entrambe le classi consentono di lavorare con regioni contigue di memoria senza la necessità di copiare i dati.
2.  Sono utili per migliorare le prestazioni delle applicazioni, specialmente quando si lavora con grandi quantità di dati, come nel caso di buffer o flussi di dati.
3.  Forniscono API simili per accedere e manipolare i dati nella memoria.

## Differenze tra Memory e Span:

1.  `Memory<T>` può essere utilizzato con metodi asincroni, mentre `Span<T>` non può. Questo perché `Span<T>` è una struttura ref, che impedisce la cattura di variabili nello stack in una closure e quindi non è compatibile con metodi asincroni.
2.  `Span<T>` è limitato allo stack, mentre `Memory<T>` può rappresentare sia memoria sullo stack che sullo heap. Di conseguenza, `Span<T>` ha una durata limitata e non può essere conservato in campi di classe, a differenza di `Memory<T>`.
3.  `Span<T>` è più leggero e veloce rispetto a `Memory<T>`, a causa della sua limitazione allo stack e dell'assenza di una classe di implementazione interna.

Quando usare l'una rispetto all'altra:

- Usare `Span<T>` quando si lavora con metodi sincroni e si desidera massimizzare le prestazioni. Poiché è limitato allo stack e non può essere conservato in campi di classe, è ideale per operazioni di breve durata che non richiedono il passaggio di dati tra metodi o thread.
- Usare `Memory<T>` quando si lavora con metodi asincroni o quando si desidera conservare un riferimento a una porzione di memoria in un campo di classe. Poiché può rappresentare memoria sia sullo stack che sullo heap, è più flessibile rispetto a `Span<T>`, ma potrebbe avere un leggero impatto sulle prestazioni.


## Esempio

```csharp
using System;

class Program
{
    static void Main()
    {
        // Allocazione di un array di interi sullo heap
        int[] numbers = new int[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

        // Creazione di un'istanza di Memory<T> che rappresenta una porzione dell'array
        Memory<int> memory = numbers.AsMemory(2, 5);

        // Esempio di utilizzo di un metodo che lavora su Memory<T>
        PrintMemoryContent(memory);
    }

    static void PrintMemoryContent(Memory<int> memory)
    {
        // Ottenimento di uno Span<T> dall'oggetto Memory<T>
        Span<int> span = memory.Span;

        // Stampa del contenuto dello Span<T>
        for (int i = 0; i < span.Length; i++)
        {
            Console.WriteLine(span[i]);
        }
    }
}
```
In questo esempio, viene allocato un array di interi sullo heap e successivamente viene creato un oggetto `Memory<int>` che rappresenta una porzione di tale array. Il metodo `PrintMemoryContent` accetta un parametro di tipo `Memory<int>` e stampa il contenuto della regione di memoria rappresentata dall'oggetto. Nota che non viene effettuata alcuna copia dei dati dell'array, ma viene semplicemente condivisa la stessa regione di memoria.

### Esempio asincrono

In questo esempio, stiamo leggendo un'ampia porzione di dati in modo asincrono utilizzando `MemoryStream`: poiché `Memory<T>` è compatibile con le operazioni asincrone, possiamo utilizzarlo per creare una vista sull'array di byte.
Se avessimo utilizzato `Span<T>`, non saremmo stati in grado di utilizzare `ReadAsync` e avremmo dovuto utilizzare un approccio sincrono.

```csharp
static async Task Main()
{
	// Creiamo un array di byte di grandi dimensioni
	byte[] data = new byte[100_000];

	// Inizializziamo l'array con dati casuali
	var random = new Random();
	random.NextBytes(data);

	// Utilizziamo Memory<T> per creare una vista sull'array di byte
	Memory<byte> memoryData = data;

	// Leggiamo una parte dell'array in modo asincrono
	byte[] buffer = new byte[10_000];
	await ReadBytesAsync(memoryData, buffer);

	// Facciamo qualcosa con il buffer, ad esempio scriverlo su console
	for (int i = 0; i < buffer.Length; i++)
	{
		Console.Write(buffer[i] + " ");
	}
}

static async Task ReadBytesAsync(Memory<byte> memoryData, byte[] buffer)
{
	// Creiamo uno stream di memoria basato sull'array di byte
	using var memoryStream = new MemoryStream(memoryData.ToArray());

	// Leggiamo una parte dell'array in modo asincrono
	await memoryStream.ReadAsync(buffer, 0, buffer.Length);
}
```