---
tags:
  - Coding
  - Interview
  - PublishedPosts
---
## Problema

L'obiettivo di questo problema è invertire un numero (es. 123 -> 321) senza usare le stringhe (altrimenti la soluzione sarebbe banalmente `number.ToString().Reverse()`).
La soluzione è molto semplice a patto di conoscere alcune semplici operazioni matematiche di modulo e divisione.

## Soluzione

L'idea è creare una variabile di appoggio dove andremo a inserire le varie cifre del numero originale moltiplicandola per 10 in base alla posizione dove vorremo andare ad inserire la cifra all'interno del numero.
```csharp
int RevertNumber(int number)  
{  
    // 123 -> 321  
    // 3 * 100 + 2*10 + 1*1
    var outputNumber = 0;  
    while (number > 0)  
    {  
        // Prendo la cifra meno significativa  
        var digit = number % 10;  
        // Moltiplicare per 10 il numero permette "shiftare" il numero verso sinistra in modo da accogliere il nuovo numero come cifra meno significativa  
        outputNumber = 10 * outputNumber + digit;  
        // Rimuovo la cifra meno significativa dal numero  
        number /= 10;  
    }  
  
    return outputNumber;  
}
```

## Ricorsiva

La soluzione ricorsiva è sicuramente più interessante.
Il piede della ricorsione è che se un numero è minore di 10 esso è già invertito e la ricorsione esce.
Di seguito l'algoritmo come al solito estrare la cifra meno significativa ([[Come prendere la cifra meno significativa di un numero]]) e la moltiplica per `100^lunghezza del numero - 1`.
Per ottenere la lunghezza del numero utilizzo la tecnica del logaritmo a base 10 ([[Ottenere il numero di cifre di un numero]]).
Per esempio se devo invertire 987 devo creare la somma 700 + 80 + 9, quindi `7*10^2 + 8*10^1 + 9*10^0`.

```csharp
// Esempio 987  
int ReverseNumber(int num)  
{  
    // Se il numero è minore di 10, significa che abbiamo raggiunto l'ultima cifra  
    if (num < 10) {  
        return num;  
    }  
  
    // Calcoliamo la lunghezza del numero originale.  
    // 987 -> 3
    var numLength = (int)Math.Log10(num) + 1;  
    // Estraggo l'ultima cifra del numero originale  
    // 987 -> 7
    var extractedDigit = num % 10;  
    // Aggiungiamo la cifra estratta al numero inverso moltiplicandola per la potenza corretta  
    // 987 -> 700
    var reversedNum = extractedDigit * (int)Math.Pow(10, numLength - 1);  
    // Chiamiamo nuovamente la funzione passando come argomento il numero originale diviso per 10  
    // 700 + 80 + 7
    return reversedNum + ReverseNumber(num / 10);  
}
```