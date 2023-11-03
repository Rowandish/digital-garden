---
tags:
  - Coding
  - Interview
  - PublishedPosts
---


Proseguiamo la serie sulla risoluzione di problemi algoritmici che vengono spesso richiesti durante le interview.
Questo è un classico problema di programmazione in quanto è scrivere un algoritmo per sapere se un numero è palindromo o meno.
Un numero palindromo è un numero che si legge allo stesso modo sia da destra che da sinistra; un esempio è il numero "121" o il numero "12344321".
Per definizione inoltre i numeri minori di 0 non sono mai palindromi mentre lo sono sempre i numeri tra 0 e 9.
Propongo varie soluzioni, tutte in C# in quanto è il linguaggio che mi è più comodo anche se la logica può essere facilmente implementabile anche in altri linguaggi senza alcun problema.

## Stringa

L'idea è convertire il numero in una stringa, poi utilizzare la funzione Reverse() per capovolgere la stringa in modo da poter facilmente confrontare la stringa originale con quella capovolta.
Se sono uguali, il numero è un palindromo, altrimenti non lo è.
```csharp
bool IsPalindrome(int number)
{
    string numberAsString = number.ToString();
    string reversedNumber = new string(numberAsString.Reverse().ToArray());
    return numberAsString == reversedNumber;
}
```

## Array di caratteri
In questa soluzione, il numero viene convertito in un array di caratteri utilizzando il metodo `ToCharArray()`.
Viene quindi utilizzato un ciclo per confrontare i caratteri dell'array a partire dall'inizio e dalla fine: se tutti i caratteri corrispondono, il numero è un palindromo, altrimenti non lo è.
```csharp
bool IsPalindrome(long number)  
{  
    var numberAsCharArray = number.ToString().ToCharArray();  
    var length = numberAsCharArray.Length;  
    for (var i = 0; i < length / 2; i++)  
    {  
        if (numberAsCharArray[i] != numberAsCharArray[length - i - 1])  
            return false;  
    }  
    return true;  
}
```

## Operazioni matematiche

Questo metodo sfrutta le divisioni e operazioni di modulo per andare a creare una versione "invertita" del numero ma senza usare la funzione Reverse() di stringhe.
Una volta costruito il numero invertito basta confrontarlo con il numero originale, se è lo stesso il numero è palindromo.
```csharp
bool IsPalindrome(long number)  
{  
    // Se il numero è negativo, non può essere un palindromo  
    if (number < 0) return false;  
    // Se il numero è inferiore a 10, è sempre un palindromo  
    if (number < 10) return true;  
  
    // Utilizziamo la logica delle operazioni matematiche per isolare ogni cifra del numero  
    long reverse = 0;  
    var original = number;  
  
    while (number > 0)  
    {  
        // Isoliamo l'ultima cifra  
        var lastDigit = number % 10;  
        // Aggiungiamo la cifra isolata alla fine del numero inverso  
        reverse = reverse * 10 + lastDigit;  
        // Rimuoviamo l'ultima cifra dal numero originale  
        number /= 10;  
    }  
  
    // Confrontiamo il numero originale con il numero inverso  
    return original == reverse;  
}
```

## Confronto testa-coda
Questo semplice algoritmo converte prima il numero in stringa in modo che possa accedere facilmente alla cifra n-esima usando le `[]` e poi utilizza due indici,  due indici, uno all'inizio e uno alla fine della stringa, per confrontare le cifre all'inizio e alla fine del numero.
Utilizziamo un ciclo `while` per continuare a confrontare le cifre finché non ci incontriamo a metà. Se troviamo due cifre non uguali, il numero non è un palindromo e quindi restituiamo false; altrimenti restituiremo true.

```csharp
bool IsPalindrome(long number)
{
    // Convertiamo il numero in stringa
    string numString = number.ToString();
    // Inizializziamo due indici, uno all'inizio e uno alla fine della stringa
    int start = 0, end = numString.Length - 1;

    // Continuiamo a confrontare le cifre all'inizio e alla fine della stringa finché non ci incontriamo a metà
    while (start < end)
    {
        // Se le cifre non sono uguali, il numero non è un palindromo
        if (numString[start] != numString[end]) return false;
        // Altrimenti, continuiamo a confrontare le cifre successive
        start++;
        end--;
    }

    // Se non sono state trovate cifre non uguali, il numero è un palindromo
    return true;
}
```