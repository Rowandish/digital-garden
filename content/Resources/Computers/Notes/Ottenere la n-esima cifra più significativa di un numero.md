---
tags:
  - Coding
  - Interview
  - Tricks
  - PublishedPosts
---


## Problema

L'obiettivo è ottenere la n-esima cifra più significativa  di un numero, quindi, esempio, con il numero 56891 la prima cifra è 5, la seconda è 6, la terza è 8 e così via.
L'algoritmo si basa per prima cosa sull'ottenere un sotto-numero in cui la cifra che mi interessa è nella porzione delle unità e poi fare % 10.  
Per esempio nel numero 56891, se voglio ottenere la terza cifra (quindi 8) devo prima ottenere 568 e poi con il % 10 ottengo 8 che è il risultato.  
Per ottenere 568 devo dividere il numero per 100, che è genericamente 10 ^ (numero di cifre iniziali (5) - cifra che voglio (3)).

## Soluzione

```csharp
private int PrivateGetNthMostSignificantDigit(int number, int n)  
{  
    // Converto il numero a positivo se negativo  
    number = Math.Abs(number);  
    // Ottengo il numero di cifre nel numero  
    var digitCount = (int) Math.Log10(number) + 1;  
    // Ottengo un divisore in base 10 grande come la porzione di numero che mi interessa  
    var divisor = (int)Math.Pow(10, digitCount - n);  
    // Ottengo una porzione del numero dove la cifra che mi interessa è nella porzione delle unità  
    var numberWhereDigitIsInLastPosition = number / divisor;  
    // Per ottenere qundi la cifra meno significativa di tale porzione di numero basta il normale modulo 10  
    var nthMostSignificantDigit = numberWhereDigitIsInLastPosition % 10;  
    return nthMostSignificantDigit;  
}
```