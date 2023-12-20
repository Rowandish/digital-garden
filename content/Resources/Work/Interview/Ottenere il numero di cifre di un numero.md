---
tags:
  - Tricks
  - Coding
---
Per ottenere il numero di cifre di cui è composto un numero in modo estremamente semplice basta utilizzare il logaritmo a base 10: questo infatti  restituisce il numero di volte che è necessario moltiplicare 10 per ottenere quel numero.
Una volta ottenuto il risultato del logaritmo basta castarlo a intero (quindi un floor) e sommarci 1.
Ad esempio, il logaritmo base 10 di 987 è 2.99, perché 10^2.99 = 987. Castando 2.99 a intero ottengo la cifra 2 e sommando 1 ottengo 3, che è il numero di cifre di cui è composto il numero 
```csharp
var numberOfDigit = (int) Math.Log10(num) + 1;
```

