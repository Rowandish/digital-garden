---
tags:
  - Coding
  - Interview
  - PublishedPosts
---


## Problema

Il problema è il seguente: ti vengono dati due numeri rappresentati come liste concatenate di cifre, dove ogni cifra è rappresentata da un nodo della lista.

Le liste rappresentano numeri non negativi e le cifre sono memorizzate in ordine inverso rispetto all'ordine in cui le cifre appaiono nel numero. Il tuo compito è quello di sommare i due numeri e restituire la somma come una lista concatenata.

Esempio: supponiamo che ci siano due numeri da sommare, il primo è rappresentato dalla lista concatenata 2->4->3 e il secondo dalla lista concatenata 5->6->4. Il primo numero corrisponde al numero 342 e il secondo al numero 465. La somma di questi due numeri è 807, che viene rappresentata dalla lista concatenata 7->0->8.

![[addtwonumber1.jpg]]

## Soluzione

La soluzione coinvolge l'iterazione attraverso entrambe le liste e l'esecuzione dell'operazione di somma per ogni cifra portando l'eventuale riporto. Poiché le liste sono rappresentate in ordine inverso, la somma può essere eseguita facilmente con un semplice ciclo while che itera attraverso entrambe le liste contemporaneamente.

Di seguito la soluzione in C# completamente commentata:

```csharp
private class ListNode
{
    public ListNode Next { get; set; } // Riferimento al nodo successivo
    public int Val { get; init; } // Valore del nodo
}

private static ListNode AddTwoNumbers(ListNode l1, ListNode l2)
{
    // Dato che dovrò ritornare una ListNode la creo qui all'inizio per concatenarci i risultati. Alla fine ritornerò dummyHead.Next.
    var dummyHead = new ListNode();
    // Nodo corrente della lista risultato di appoggio
    var current = dummyHead;
    var riporto = 0;
    // Loop finché ci sono nodi da sommare
    while (l1 != null || l2 != null)
    {
        // Valore del nodo corrente della prima e seconda lista. Imposto a 0 se la lista è finita
        var valueList1 = l1?.Val ?? 0;
        var valueList2 = l2?.Val ?? 0;
        // Somma dei due valori più il riporto
        var sum = riporto + valueList1 + valueList2;
        // Aggiorna il riporto: con la divisione per 10 se la somma è di due cifre ottengo la cifra più significativa altrimenti ottengo 0
        riporto = sum / 10;
        // Crea un nuovo nodo mettendo come risultato il resto della somma
        current.Next = new ListNode { Val = sum % 10 };
        // Modifico current in modo che il prossimo nodo lo aggiungo al nodo appena aggiunto
        current = current.Next;
        // Modifico l1 e l2 con i nodi next, se esistono. Altrimenti imposto a null e sopra ho il controllo che un nodo null corrisponde a somma 0
        if (l1 != null)
            l1 = l1.Next;
        if (l2 != null)
            l2 = l2.Next;
    }

    if (riporto > 0) // Se c'è ancora un resto da aggiungere
        current.Next = new ListNode { Val = riporto }; // Crea un nuovo nodo per il resto
    return dummyHead.Next; // Ritorna il riferimento al primo nodo della lista risultato (senza il nodo fittizio)
}
```