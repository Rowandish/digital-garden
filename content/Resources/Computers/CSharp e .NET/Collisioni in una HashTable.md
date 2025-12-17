In una hashtable, due chiavi diverse possono produrre lo **stesso hash**. Questo si chiama **collisione**.
Una hashtable è una “rubrica” che associa **chiavi** a **valori**. Dato un _codice_ (la chiave), puoi recuperare subito l’oggetto collegato (il valore) senza scorrere tutta la lista.  
Sotto il cofano usa una **tabella hash**: dalla chiave calcola un numero (hash), lo “mappa” in una **cella** (bucket) e lì mette/trova la coppia.
Internamente le hashtable sono degli array con una determinata dimensione e la struttura dati si occupa di popolare alcuni dei campi di quell'array con i valori passati in ingresso mediante un mapping:  nella sua versione più semplice è l'hashdella chiave in modulo con la lunghezza dell'array interno: devo quindi poter gestire le collisioni: gli hash sono infiniti ma devono essere mappati su un array di dimensione finita.
Le due tecniche più comuni per gestire le collisioni in una tabella hash sono **chaining** (a catena) e **open addressing** (indirizzamento aperto).

### Chaining
Nel **chaining**, ogni posizione della tabella hash (l'array interno) contiene una linked list. Quando due chiavi hashano (hash chiave modulo lunghezza array) allo stesso indice , entrambe vengono inserite nella lista associata a quel particolare indice.
**Pro e contro di Chaining:**
- **Pro**: È semplice da implementare e non è necessario ridimensionare la tabella troppo frequentemente.
- **Contro**: L'uso della memoria può essere maggiore, in quanto ogni posizione della tabella richiede uno spazio per la lista collegata.    

### Open Addressing
Nel **open addressing**, quando si verifica una collisione, il dizionario cerca una nuova posizione nella tabella, secondo un certo schema (ad esempio, linear probing, quadratic probing o double hashing). In questo caso, tutte le chiavi sono memorizzate direttamente nella tabella hash, e non vengono usate strutture dati ausiliarie come le liste.
**Pro e contro di Open Addressing:**
- **Pro**: L'uso della memoria è più efficiente rispetto al chaining, poiché non sono necessarie strutture dati aggiuntive.
- **Contro**: Le collisioni possono degradare le performance, e il ridimensionamento della tabella è più complicato. Inoltre, con il carico elevato, la performance può diminuire significativamente a causa delle numerose ricerche per trovare una posizione libera.
    
## Hashtable in .NET

**`Dictionary<TKey, TValue>`** è la **struttura moderna** in C# che implementa una hashtable e l'hash (nella sua versione base) viene calcolato usando il metodo `GetHashCode()` che hanno tutti i tipi di dato.
Le collisioni accadono più o meno spesso e dipende da:
- Qualità della funzione hash (`GetHashCode()`)    
- Numero di elementi nella tabella    
- Dimensione della tabella (numero di "bucket")    
- Load factor (percentuale di occupazione)

Una **buona funzione hash** con tabella ben dimensionata ha **pochissime collisioni** (< 1%).Se metti **molti elementi (>70%)** in una tabella **senza resize**, le collisioni aumentano.
    
Nel codice sorgente del `Dictionary`, le collisioni sono gestite in modo che ogni bucket possa contenere più di un elemento in caso di collisione. Però, a differenza di una classica implementazione di **chaining**, che usa una struttura di dati separata come una lista collegata per ogni bucket, qui il comportamento è un ibrido:
1. **Tutti gli elementi sono memorizzati nell'array di entries**    
    - Gli **entry** sono memorizzati nello stesso array (`_entries`), proprio come nell'**open addressing**.        
    - Ogni entry ha un campo `next` che **punta al prossimo elemento nella stessa tabella**. Quindi, se più chiavi hanno lo stesso hash, vengono "collegate" tramite il campo `next` nell'array stesso, creando una catena all'interno dello stesso array, anziché usare una struttura separata.        
2. **Collisions e gestione della "catena"**:    
    - Se c'è una collisione (due chiavi hanno lo stesso valore di hash), l'elemento successivo non va in un altro array o struttura dati separata. Invece, l'entry successiva è "linkata" all'interno dello stesso array di entry, e si passa al successivo tramite il campo `next`. 
 ```csharp
    i = entries[i].next;  // Si passa al prossimo elemento nella "catena"
 ```
Negli screenshot sotto si vedono due elementi del Dictionary che ha capacità 3 che hanno portato ad una collisione (entrambi hanno hashCode a 0).
Si vede che il secondo (`key="b"`) ha il campo `next` che punta al primo (`Key="a"`).       
![[Pasted image 20251015164844.png]]
![[Pasted image 20251015165205.png]]