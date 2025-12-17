Una **Binary Search Tree** è una struttura dati ad albero binario in cui:
- Ogni nodo ha al massimo due figli: sinistro e destro.    
- Per ogni nodo:    
    - i valori nel **sottoalbero sinistro** sono **minori** del valore del nodo.        
    - i valori nel **sottoalbero destro** sono **maggiori**.      
### 🔹 Implementazione base in C\#

```csharp
public class TreeNode
{
    public int Value;
    public TreeNode Left;
    public TreeNode Right;

    public TreeNode(int value)
    {
        Value = value;
    }

    public void Insert(int newValue)
    {
        if (newValue < Value)
        {
            if (Left == null)
                Left = new TreeNode(newValue);
            else
                Left.Insert(newValue);
        }
        else
        {
            if (Right == null)
                Right = new TreeNode(newValue);
            else
                Right.Insert(newValue);
        }
    }

    public bool Contains(int target)
    {
        if (target == Value)
            return true;
        else if (target < Value)
            return Left?.Contains(target) ?? false;
        else
            return Right?.Contains(target) ?? false;
    }
}
```

### 🔹 Domande correlate:

1. **Come si può evitare che una BST diventi sbilanciata?**  
👉 Utilizzando una **self-balancing BST** come un **AVL Tree** o un **Red-Black Tree**, che riequilibrano l’albero dopo ogni inserimento/rimozione.
2. Qual è la complessità temporale per insert/search?
	1. **BST Bilanciata:** `O(log n)`    
	2. **BST Sbilanciata (es. inserimento ordinato):** `O(n)`
3. . **Come gestiresti i duplicati in una BST?**    
    - Opzioni:        
        - Non permettere duplicati.            
        - Permettere duplicati solo a sinistra o a destra.            
        - Aggiungere un contatore al nodo.            
- **Come elimineresti un nodo in una BST?**    
    - Tre casi:        
        - Nodo senza figli → rimuovi direttamente.            
        - Nodo con un figlio → ricollega il figlio al padre.            
        - Nodo con due figli → trova il **successore in-order** (minimo del sottoalbero destro), copia il valore e rimuovi il nodo duplicato.            
- **Quando una BST è inefficiente?**    
    - Quando è **sbilanciata** (es. inserendo dati ordinati) diventa una lista → `O(n)` in search/insert/delete.        
- **Con quale struttura sostituiresti una BST per avere garanzia di performance?**    
    - **AVL Tree**, **Red-Black Tree**, o **B-Tree** (in ambienti disk-based o database).

## Esercizi
- ✏️ **Scrivi una funzione che restituisca il minimo e massimo valore in una BST.**    
- ✏️ **Scrivi una funzione che restituisca il numero di nodi.**    
- ✏️ **Data una BST e un valore target, restituisci il percorso (lista di valori) fino al nodo.**    
- ✏️ **Scrivi una funzione per verificare se un albero è effettivamente una BST valida.**

