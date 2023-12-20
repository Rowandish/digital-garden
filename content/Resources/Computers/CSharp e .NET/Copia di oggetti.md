---
tags:
  - Coding
  - CSharp
  - Memory
  - PublishedPosts
---


## 1. Introduzione
Spesso vi è la necessità di eseguire una copia dell'istanza della classe con cui si sta lavorando, ovvero la **creazione di una nuova istanza di una classe con lo steso valore di un'istanza esistente**.

La procedura di copia non è un'operazione banale che **non può essere fatta con un assegnamento**, in quanto le classi sono tipi di riferimento e conseguentemente, per esempio, questa operazione

```csharp
object a = new object {foo="bar"}
object b = a
b.foo = "new bar" //anche a.foo = "new bar"
```
porta alla modifica dell'attributo `foo` sia dell'oggetto `a` che dell'oggetto `b`.

## 2. Il metodo Object.MemberwiseClone()

Questo metodo è un metodo di `Object` e, conseguentemente, può assere applicato a tutti gli oggetti del nostro sistema.

In particolare il `MemberwiseClone` metodo **crea una copia superficiale (shallow copy)** creando un nuovo oggetto e quindi **copiando i campi non static dell'oggetto corrente al nuovo oggetto**.

Se un campo è di tipo:

- **Valore**: viene eseguita una copia bit per bit del campo;
- **Riferimento**: viene copiato solo il riferimento pertanto sia l'oggetto originale che il suo clone fanno riferimento allo stesso oggetto.

Questo metodo è il metodo base di tutti i metodi `clone()`, e viene utilizzato per la fase iniziale di *shallow copy*.

A questo metodo deve spesso seguire un'implementazione personalizzata al fine di ottenere la copia come desiderato (*deep copy*).

## 3. L'interfaccia ICloneable
Quando ho la necessità di implementare un metodo `clone()` che effettui una *deep copy* e che, conseguentemente, estenda il metodo `MemberwiseClone` di `object` posso **implementare l'interfaccia `ICloneable` che contiene un solo metodo, `Clone`, il quale fornisce un supporto della clonazione aggiuntivo a quello di `Object.MemberwiseClone`**.

L'interfaccia `ICloneable` **richiede semplicemente che l'implementazione del valore restituito dal metodo `Clone` ritorni una copia dell'istanza dell'oggetto corrente**.

Non specifica se l'operazione di duplicazione esegue una copia completa, una copia superficiale, o una via di mezzo, né richiede che tutti i valori della proprietà dell'istanza originale vengano copiati nella nuova istanza.

Tipicamente la struttura di una classe che implementa questa interfaccia è la seguente

```csharp
public class ClassToClone : ICloneable
{
public object Clone()
{
ClassToClone clone = (ClassToClone) this.MemberwiseClone();
// logica di copia dei tipi di riferimento

return clone;
}
}
```
In ultima istanza specifico che **il metodo `clone` ritorna un tipo `object`, come anche il metodo `MemberwiseClone`**, conseguentemente la loro chiamata deve **sempre essere preceduta da un cast** del tipo di variabile che si sta clonando.