---
tags:
  - Coding
  - CSharp
  - Memory
---


`stackalloc` è una parola chiave in C# che permette di allocare un blocco di memoria sullo [[stack]], invece che sull'[[heap]]. Poiché la memoria allocata sullo stack viene automaticamente rilasciata quando il metodo corrente termina, l'utilizzo di `stackalloc` può ridurre la pressione sul garbage collector e migliorare le prestazioni dell'applicazione.

## Quando utilizzarlo

L'utilizzo principale di `stackalloc` è come ==alternativa all'allocazione di memoria sull'heap per gli array==, specialmente per array di piccole dimensioni e quando si cerca di ottenere un miglioramento delle prestazioni.
Ecco 10 casi d'uso in cui `stackalloc` può essere utile:
1.  **Allocazione di array temporanei**: Se hai bisogno di un array temporaneo per eseguire un'operazione specifica e la dimensione dell'array è piccola, `stackalloc` può essere utilizzato per creare l'array sullo stack, migliorando le prestazioni.
2.  **Interoperabilità con codice non gestito**: `stackalloc` può essere utilizzato per allocare rapidamente memoria sullo stack quando si lavora con codice non gestito (ad esempio, chiamate a funzioni di librerie native), per passare dati tra codice gestito e non gestito.
3.  **Strutture dati temporanee**: `stackalloc` può essere utile per creare strutture dati temporanee per eseguire un'operazione specifica, senza dover allocare memoria sull'heap.
4.  **Buffer per I/O**: `stackalloc` può essere utilizzato per creare rapidamente buffer temporanei per eseguire operazioni di input/output (ad esempio, leggere o scrivere dati da file o socket).
5.  **Calcolo di hash**: Durante il calcolo di hash su una sequenza di dati, `stackalloc` può essere utilizzato per allocare un buffer temporaneo sullo stack per memorizzare l'hash calcolato.
6.  **Codifica e decodifica**: `stackalloc` può essere utilizzato per allocare buffer temporanei per eseguire operazioni di codifica e decodifica (ad esempio, conversione tra codifiche di caratteri, codifica/decodifica base64, ecc.).
7.  **Compressione e decompressione**: Quando si lavora con algoritmi di compressione o decompressione, `stackalloc` può essere utilizzato per allocare buffer temporanei per gestire i dati compressi/decompressi.
8.  **Crittografia**: `stackalloc` può essere utilizzato per allocare buffer temporanei per eseguire operazioni di crittografia e decrittografia, ad esempio quando si lavora con algoritmi simmetrici o asimmetrici.
9.  **Elaborazione di immagini**: Durante l'elaborazione di immagini, `stackalloc` può essere utilizzato per allocare buffer temporanei per contenere i dati dell'immagine o per eseguire operazioni come la convoluzione o il filtraggio.
10.  **Gestione delle matrici**: Quando si lavora con matrici, `stackalloc` può essere utilizzato per allocare matrici temporanee per operazioni come la trasposizione, la moltiplicazione o la decomposizione.

## Come utilizzarlo
Quando si utilizza `stackalloc`, si alloca un blocco di memoria sullo stack che può essere utilizzato per memorizzare un insieme di elementi di tipo valore. Tuttavia, `stackalloc` ==restituisce un puntatore a tale blocco di memoria==, che può comportare rischi in termini di sicurezza e stabilità se non viene gestito correttamente.
Posso utilizzare la classe `Span<T>` (vedi [[Span e ReadOnlySpan]]; `Span<T>` è un tipo di struttura che rappresenta una vista contigua di memoria di una collezione di elementi di tipo `T`) per creare una ==vista sicura e gestita del blocco di memoria allocato sullo stack==.
`Stackalloc` può essere usato per inizializzare un oggetto `Span<T>` che rappresenta il blocco di memoria allocato.
```csharp
// Utilizzo di stackalloc per allocare un blocco di memoria sullo stack
// In questo caso utilizzo Span<T> in quanto prevedo che tali debbano essere modificati
Span<int> data = stackalloc int[256];
// Se l'array è in sola lettura posso usare ReadOnlySpan
ReadOnlySpan<int> data = stackalloc int[256];
```

## Limitazioni

Le limitazioni di `stackalloc` sono principalmente dovute alla natura dello stack e alle sue implicazioni per la gestione della memoria. Di seguito sono elencate alcune delle principali limitazioni associate all'uso di `stackalloc` in C#:
1.  **Dimensione limitata dello stack**: Lo stack ha generalmente una dimensione molto più piccola rispetto all'heap. Di conseguenza, l'allocazione di grandi quantità di memoria sullo stack può causare un'eccezione `StackOverflowException`. Pertanto, è importante utilizzare `stackalloc` solo per blocchi di memoria di dimensioni ridotte e per brevi periodi.
2.  **Compatibilità solo con tipi di valore senza riferimenti**: `stackalloc` può essere utilizzato solo con tipi di valore che non contengono riferimenti, come i tipi primitivi (ad es. `int`, `float`, `double`, ecc.) e le `struct` che contengono solo tipi di valore. Se si tenta di utilizzare `stackalloc` con un tipo di valore che contiene riferimenti, verrà generato un errore di compilazione.
3.  **Vita breve degli oggetti allocati**: Gli oggetti allocati con `stackalloc` hanno una durata limitata al metodo corrente. Non è possibile restituire un riferimento a un oggetto allocato sullo stack al chiamante del metodo, in quanto la memoria verrà automaticamente rilasciata alla fine del metodo. Per ovviare a questo problema, è possibile utilizzare `Span<T>` o copiare il contenuto dell'oggetto allocato sullo stack in un oggetto allocato sull'heap.

## Esempio

Nell'esempio seguente, mettiamo a confronto due versioni di un metodo `CalculateSumOfSquares` che calcola la somma dei quadrati di un intervallo di numeri interi. Nel primo esempio, utilizziamo `stackalloc` per allocare l'array temporaneo sullo stack. Nel secondo esempio, invece, allocchiamo l'array sull'heap.

### Esempio con `stackalloc`

```csharp
public static long CalculateSumOfSquares(int start, int end)
{
    int length = end - start + 1;

    // Utilizzo di stackalloc per allocare un array temporaneo sullo stack
    Span<int> squares = length <= 256 ? stackalloc int[length] : new int[length];

    for (int i = start; i <= end; i++)
    {
        squares[i - start] = i * i;
    }

    long sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += squares[i];
    }

    return sum;
}
```

### Esempio senza `stackalloc`

```csharp
public static long CalculateSumOfSquares(int start, int end)
{
    int length = end - start + 1;

    // Allocazione di un array temporaneo sull'heap
    int[] squares = new int[length];

    for (int i = start; i <= end; i++)
    {
        squares[i - start] = i * i;
    }

    long sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += squares[i];
    }

    return sum;
}
```