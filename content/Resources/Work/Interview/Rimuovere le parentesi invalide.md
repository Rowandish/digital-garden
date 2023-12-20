---
tags:
  - Coding
  - Interview
  - PublishedPosts
---


## Problema

L'obiettivo è rimuovere il minor numero possibile di parentesi  parentesi aperte e non chiuse (e viceversa) di una determinata stringa composta solo da lettere minuscole a-z e da un certo numero di parentesi aperte '( ' e chiuse ')'.
L'algoritmo dovrà restituire una stringa valida dal punto di vista delle parentesi, quindi ad ogni parentesi aperta ce ne sarà sicuramente una chiusa.
Dato che esistono stringhe con più di una soluzione corretta, va bene restituirne una qualsiasi.
Esempi di stringhe con parentesi valide:
* `()`
* `(())`
* `()()`
* `(())()`
* `""`
Esempi di stringhe invalide:
* `)(`
* `(()`
* `()()(`
* `()())`

Per esempio con la stringa `"a(b(c(de)fgh)"` posso avere in uscita una delle seguenti soluzioni:
* `b(c(de)fgh)`
* `a(bc(de)fgh)`
* `a(b(cde)fgh)`
* `ab(c(de)fgh)`

Un altro esempio è la stringa `"((("` che deve dare come soluzione `""`.

## Soluzione
Per risolvere questo problema si può utilizzare uno `Stack` per tenere traccia delle parentesi aperte di cui non ho ancora trovato corrispondenza e una lista di indici per segnarmi a quale indice c'è la parentesi che devo rimuovere.
Dopo il foreach sulla stringa tutti gli elementi che sono rimasti nello `Stack` devono essere aggiunti alla lista degli indici degli elementi da rimuovere e infine ciclare tale lista di indici il carattere corrispondente dalla stringa.
```csharp
static string RemoveInvalidParentheses(string s)  
{  
    // Inizializzo una pila vuota per tenere traccia delle parentesi aperte  
    var stack = new Stack<int>();  
    // Inizializzo una lista vuota per tenere traccia delle parentesi da rimuovere  
    var removeList = new List<int>();  
  
    // Itero attraverso ogni carattere nella stringa  
    for (var i = 0; i < s.Length; i++)  
    {  
        // Se il carattere è una parentesi aperta, la metto in cima alla pila, dovrò verificare di avere una parentesi chiusa  
        if (s[i] == '(')  
            stack.Push(i);  
        // Se il carattere è una parentesi chiusa  
        else if (s[i] == ')')  
        {  
            // Se la pila è vuota, significa che questa parentesi chiusa non ha una corrispondente aperta  
            // quindi la aggiungo alla lista delle parentesi da rimuovere            if (stack.Count == 0)  
                removeList.Add(i);  
            // Altrimenti, significa che ho trovato una coppia di parentesi valida  
            // quindi rimuovo la parentesi aperta corrispondente dalla pila            else  
                stack.Pop();  
        }  
    }  
  
    // Dopo aver controllato tutte le parentesi, rimangono nella pila solo quelle aperte non corrispondenti  
    // quindi aggiungo anche queste alla lista delle parentesi da rimuovere    while (stack.Count > 0)  
        removeList.Add(stack.Pop());  
  
    // Rimuovo tutte le parentesi presenti nella lista dalla stringa originale  
    foreach (var index in removeList)  
        s = s.Remove(index, 1);  
  
    // Restituisco la stringa valida  
    return s;  
}
```