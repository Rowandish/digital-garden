---
tags:
  - Coding
  - CSharp
  - Memory
---
L'Array Pooling è una tecnica che permette di ==riutilizzare gli array invece di crearne di nuovi ogni volta che ne hai bisogno== nell'ottica di ridurre la pressione sul [[Garbage Collector]] e migliorare così le prestazioni del tuo programma.

C# fornisce una classe `ArrayPool<T>` nel namespace `System.Buffers`, che gestisce un pool di array condiviso.

## Esempio

```csharp
// Ottenere un'istanza dell'ArrayPool<int>
ArrayPool<int> pool = ArrayPool<int>.Shared;

// Richiedere un array dal pool di lunghezza 100
int[] array = pool.Rent(100);

try
{
	// Inizializzare l'array: gli array restituiti al pool potrebbero contenere dati precedenti, quindi è necessario inizializzare l'array prima di utilizzarlo.
    Array.Clear(array, 0, array.Length);
	// Utilizzare l'array come necessario, in questo caso riempiendolo con valori e stampandoli
	for (int i = 0; i < array.Length; i++)
		array[i] = i * 2;

	// Stampa il contenuto dell'array
	for (int i = 0; i < array.Length; i++)
		Console.WriteLine(array[i]);
}
finally
{
	// Restituire l'array al pool
	pool.Return(array);
}
```

## Funzionamento interno

Internamente, la classe gestisce una serie di buckets che contengono gli array di diverse dimensioni.
Quando ==richiedi un array, la classe `ArrayPool<T>` cerca un array disponibile nel bucket corrispondente alla dimensione richiesta: Se ne trova uno, lo restituisce; altrimenti, ne crea uno nuovo==.
Quando restituisci un array al pool, viene inserito nel bucket corrispondente per essere riutilizzato in seguito.
Di seguito un esempio semplificato del funzionamento di un `ArrayPool<T>`

```csharp
public class SimpleArrayPool<T>
{
    private readonly Dictionary<int, Stack<T[]>> _buckets;

    public SimpleArrayPool()
    {
        _buckets = new Dictionary<int, Stack<T[]>>();
    }

    public T[] Rent(int length)
    {
        // Cerca una bucket corrispondente alla lunghezza richiesta
        if (_buckets.TryGetValue(length, out Stack<T[]> bucket))
        {
            // Se c'è un array disponibile nel bucket, rimuovilo e restituiscilo
            if (bucket.Count > 0)
                return bucket.Pop();
        }

        // Se non è stato trovato un array disponibile, creane uno nuovo
        return new T[length];
    }

    public void Return(T[] array)
    {
        // Cerca un bucket corrispondente alla lunghezza dell'array
        if (!_buckets.TryGetValue(array.Length, out Stack<T[]> bucket))
        {
            // Se il bucket non esiste, crealo
            bucket = new Stack<T[]>();
            _buckets.Add(array.Length, bucket);
        }

        // Inserisci l'array nel bucket corrispondente
        bucket.Push(array);
    }
}
```

Tuttavia, la classe `ArrayPool<T>` fornita dal framework .NET è molto più ottimizzata e gestisce vari scenari come il trimming degli array inutilizzati, il thread-safety e il supporto per array di dimensioni variabili.