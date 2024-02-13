---
tags:
  - Coding
  - BehaviouralDesignPattern
---
Lo Special Case Pattern, introdotto da Martin Fowler nel suo libro "Refactoring: Improving the Design of Existing Code", è un design pattern che gestisce in modo pulito i casi speciali o eccezionali in un sistema senza dover condizionare il codice con verifiche speciali ovunque. L'obiettivo è migliorare la chiarezza del codice, renderlo più manutenibile e ridurre la complessità delle logiche condizionali.

Immaginiamo di dover gestire una lista di oggetti `Order`, e vogliamo calcolare il totale delle vendite. Nel contesto, potrebbe verificarsi un caso speciale se la lista di ordini è vuota.
Invece di gestire questo caso speciale con eccezioni, possiamo utilizzare lo Special Case Pattern.

```csharp
// Interfaccia che rappresenta un oggetto generico
public interface IOrder
{
    decimal GetTotalAmount();
}

// Implementazione concreta di IOrder per il caso normale
public class Order : IOrder
{
    public decimal Amount { get; set; }

    public decimal GetTotalAmount()
    {
        return Amount;
    }
}

// Implementazione concreta di IOrder come special case per il caso vuoto
public class NullOrder : IOrder
{
    public decimal GetTotalAmount()
    {
        // Nel caso speciale, restituiamo 0 come totale
        Console.WriteLine("No orders found. Total amount is 0.");
        return 0;
    }
}

// Servizio per calcolare il totale delle vendite
public class SalesCalculator
{
    public decimal CalculateTotalSales(List<IOrder> orders)
    {
        // Utilizziamo il pattern NullObject per gestire il caso speciale
        IOrder orderObject = orders.Any() ? new Order() : new NullOrder();

        // Calcoliamo il totale delle vendite
        decimal totalAmount = orderObject.GetTotalAmount();

        // Altre operazioni con il totale...

        return totalAmount;
    }
}

class Program
{
    static void Main()
    {
        List<IOrder> orders = new List<IOrder>
        {
            new Order { Amount = 100 },
            new Order { Amount = 150 },
            // Possiamo anche avere un elenco vuoto
        };

        SalesCalculator salesCalculator = new SalesCalculator();
        decimal totalSales = salesCalculator.CalculateTotalSales(orders);
        Console.WriteLine($"Total Sales: {totalSales}");
    }
}
```

L'utilizzo di questo pattern consente di gestire il caso speciale senza dover introdurre eccezioni o verifiche condizionali in tutto il codice.
La logica per il caso speciale è centralizzata nell'implementazione di `NullOrder`, mantenendo il codice pulito e facilmente manutenibile.