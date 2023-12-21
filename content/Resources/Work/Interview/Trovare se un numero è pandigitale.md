---
tags:
  - Coding
  - Interview
  - PublishedPosts
---
Con questo post inauguro una serie di post sulla risoluzione di problemi algoritmici che vengono spesso richiesti durante le interview.
Il primo problema che affronto è scrivere un algoritmo per sapere se un numero è pandigitale che un numero che contiene tutte le cifre da 0 a 9 senza ripetizioni.
Propongo varie soluzioni, tutte in C# in quanto è il linguaggio che mi è più comodo anche se la logica può essere facilmente implementabile anche in altri linguaggi senza alcun problema.

## Array di booleani

In questa soluzione si evita l'utilizzo del dizionario utilizzando un array di booleani di dimensione 10. Questo array è quindi "automaticamente" popolato dalle cifre da 0 a 9 che sono gli indici di tale array.
L'obiettivo è marchiare l'elemento corrispondente dell'array come true.
Alla fine dell'iterazione per sapere se un numero è pandigitale basta verificare che tutti gli elementi dell'array siano veri.

```csharp
static bool IsPandigital(int number) {  
    //dichiarazione e inizializzazione dell'array di booleani  
    var digits = new bool[10];  
    //ciclo che esamina ogni cifra del numero  
    while (number > 0) {  
        var digit = number % 10;  
        //se la cifra è già stata incontrata in precedenza il numero non è pandigitale  
        if (digits[digit]) {  
            return false;  
        }  
        //segno la cifra come incontrata  
        digits[digit] = true;  
        //elimino la cifra dal numero  
        number /= 10;  
    }  
  
    // Se l'array di booleani è tutto a true significa che il numero è pandigitale  
    return digits.All(b => b);  
}
```

### Complessità spaziale e temporale
La complessità spaziale di questa soluzione è O(1) poiché utilizziamo solo un array di dimensioni fisse. La complessità temporale è O(n), dove n è il numero di cifre del numero dato in ingresso.

## Lista
```csharp
// Funzione che verifica se un numero è pandigitale  
bool IsPandigital(int n)  
{  
    // Creiamo una lista di lunghezza 10 per contenere le frequenze delle cifre  
    // inizializziamo tutte le posizioni a 0
    var frequencies = new List<int>(new int[10]);  
  
    // Fintanto che il numero non è 0  
    while (n != 0)  
    {  
        // Prendiamo l'ultima cifra del numero  
        var lastDigit = n % 10;  
  
        // Se la frequenza è già stata incrementata una volta, ritorniamo false  
        if (frequencies[lastDigit] > 0)  
            return false;  
  
        // Altrimenti incrementiamo la frequenza della cifra  
        frequencies[lastDigit]++;  
  
        // Rimuoviamo l'ultima cifra dal numero dividendo per 10  
        n /= 10;  
    }  
    // Tutti gli altri elementi dell'array delle frequenze devono avere valore diverso da 0  
    return frequencies.All(t => t != 0);  
}
```

## HashSet

Questo metodo sfrutta la proprietà degli `Hashset` in quanto una ottima struttura dati per la verifica di elementi unici perché non permette elementi duplicati.
L'algoritmo inizializza quindi un `HashSet` di interi allo scopo di sapere quali cifre ho trovato nel numero.
Alla fine dell'iterazione se la dimensione del set è 10 significa che ho tutte le cifre da 0 a 9.
```csharp
static bool IsPandigital(int n)  
{  
    // Creiamo un insieme per verificare la presenza di ciascuna cifra  
    var digits = new HashSet<int>();  
    // Per ogni carattere nella stringa del numero n  
    foreach (var c in n.ToString())  
    {  
        // convertiamo il carattere in un numero intero  
        var digit = c - '0'; // equivalente a (int) c - 48  
        // se il numero è minore di 1 o maggiore di 9 oppure se l'insieme contiene già il numero, restituiamo false        if (digit is < 0 or > 9 || !digits.Add(digit))  
            return false;  
    }  
    // Se l'HashSet ha dimensione 10 significa che contiene tutte le cifre  
    return digits.Count == 10;  
}
```
Per ciclare tutte le cifre di un numero converto prima il numero in stringa con il metodo `ToString()`, poi ne effettuo il foreach in modo da ciclare `char` per `char` e infine riconverto il `char` in `integer`.

### Complessità spaziale e temporale
La complessità spaziale di questa soluzione è O(1) poiché utilizziamo solo un set di dimensioni fisse. La complessità temporale è O(n), dove n è il numero di cifre del numero dato in ingresso.

### Singola riga

```csharp
static bool IsPandigital(int n)  
{  
    return new HashSet<char>(n.ToString().ToCharArray()).Count == 10;  
}
```
Grazie al costruttore di `HashSet` posso inserire già il numero come array di char con lo skip automatico di eventuali duplicati.
Converto quindi il numero intero in ingresso in un array di caratteri con il metodo `ToString()ToCharArray().`
Ora devo solo verificare che l'HashSet contenga esattamente 10 elementi (quindi sono presenti tutte le cifre).