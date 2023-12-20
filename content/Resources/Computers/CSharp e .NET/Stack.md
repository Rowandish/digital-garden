---
tags:
  - Coding
  - Memory
---
Lo stack è una **area di archiviazione in RAM sequenziale, in particolare è una "pila" LIFO** (Last in first out) che viene utilizzato per gestire variabili locali, parametri di funzione e informazioni sul controllo del flusso del programma. Quando viene chiamata una funzione, un blocco è riservato nella parte superiore dello stack per le variabili locali e alcuni dati.

Quando quella funzione termina, il blocco diventa inutilizzato e può essere usato alla successiva chiamata di una funzione. La memoria viene quindi allocata e deallocata automaticamente quando le funzioni vengono chiamate e ritornano. 

Questa **allocazione lineare e sequenziale della memoria e viene utilizzata nell'allocazione della memoria statica (variabili passate per valore)**.

**La dimensione dello stack è fissa e decisa dal sistema operativo quando viene creato assegnandolo ad un thread**. Se la dimensione dello stack supera il valore iniziale vi è un errore di stack overflow. Questa eccezione può avvenire, per esempio, nei casi di ricorsione infinita.

## Vantaggi
- **Velocità di allocazione e deallocazione**: Lo stack è generalmente più veloce nell'allocazione e nella deallocazione della memoria rispetto all'[[Heap]]. Questo è dovuto alla sua natura lineare e alla gestione automatica della memoria, che permette di allocare e deallocare semplicemente spostando un puntatore.
- **Gestione automatica della memoria**: Le variabili allocate nello stack vengono automaticamente rimosse quando il blocco di codice che le contiene termina la sua esecuzione. Ciò semplifica la gestione della memoria e riduce il rischio di perdite di memoria (memory leaks) che possono verificarsi quando si utilizza l'heap.
- **Minore frammentazione della memoria**: Poiché la memoria nello stack viene allocata e deallocata in modo lineare, il rischio di frammentazione della memoria è ridotto. Questo contribuisce a mantenere l'efficienza del programma e riduce la necessità di interventi per deframmentare la memoria.
- **Allocazione deterministica**: L'allocazione di memoria nello stack avviene in modo deterministico e prevedibile, il che significa che il comportamento del programma risulta più consistente e più facile da analizzare. Al contrario, l'allocazione di memoria nell'heap può essere più complessa e imprevedibile.
- **Minore overhead**: Le variabili nello stack hanno generalmente un overhead inferiore rispetto a quelle allocate nell'heap. Ciò è dovuto al fatto che non è necessario gestire esplicitamente la memoria o utilizzare strutture dati aggiuntive (come tabelle di allocazione) per tenere traccia delle variabili allocate.

## Limiti
* **Dimensione limitata**: Lo stack ha una dimensione limitata, solitamente molto inferiore rispetto all'heap. Ciò significa che è possibile esaurire lo spazio dello stack rapidamente, specialmente quando si lavora con strutture dati di grandi dimensioni o con ricorsione profonda.
* **Allocazione statica e temporanea**: Le variabili allocate nello stack hanno una durata limitata e vengono automaticamente rimosse quando il blocco di codice che le contiene termina la sua esecuzione. Ciò limita la flessibilità nella gestione della memoria e impedisce l'uso di variabili dinamiche o la persistenza dei dati tra diverse chiamate di funzione.
* **Non adatto per grandi oggetti**: A causa della dimensione limitata dello stack, non è adatto per l'allocazione di oggetti o strutture dati di grandi dimensioni. Al contrario, l'heap offre molto più spazio e flessibilità per gestire oggetti più grandi.
* **Nessuna gestione manuale della memoria**: Sebbene la gestione automatica della memoria nello stack possa sembrare un vantaggio, a volte può essere un limite. L'allocazione e la deallocazione automatica della memoria impediscono al programmatore di gestire direttamente la memoria, il che può essere utile in situazioni in cui è richiesta una maggiore flessibilità o un controllo più preciso sulle risorse.

## Esempio
Il seguente metodo calcola la somma di due numeri interi:
```csharp
int somma(int a, int b) {
    return a + b;
}
```
Ecco il corrispondente codice assembly x86:

```assembly
; Prologo della funzione
somma:
    push ebp        ; Salva il valore corrente di ebp nello stack
    mov ebp, esp    ; Imposta ebp come base dello stack per questa chiamata di funzione

; Corpo della funzione
    mov eax, [ebp+8] ; Carica il valore del primo parametro (a) in eax
    mov ecx, [ebp+12]; Carica il valore del secondo parametro (b) in ecx
    add eax, ecx    ; Esegui la somma tra eax e ecx, e salva il risultato in eax

; Epilogo della funzione
    pop ebp         ; Ripristina il valore di ebp precedentemente salvato nello stack
    ret             ; Ritorna al chiamante, il risultato è in eax
```

### Prologo

Nel prologo della funzione `somma`, si salvano e si aggiornano i registri `ebp` e `esp` nel seguente modo:

1.  `push ebp`: Il valore corrente di `ebp` viene salvato nello stack.
2.  `mov ebp, esp`: Il valore di `esp` viene copiato in `ebp`.

Dopo queste due istruzioni, la situazione sullo stack è la seguente:

```lua
    | ...         |
    +-------------+
ebp | indirizzo di ritorno | <- ebp+4
    +-------------+
    | vecchio ebp | <- ebp
    +-------------+
    | parametro a | <- ebp+8 (viene letto in eax)
    +-------------+
    | parametro b | <- ebp+12 (viene letto in ecx)
    +-------------+
    | ...         |
```

Ora `ebp` punta al vecchio valore di `ebp` salvato sullo stack e `esp` punta alla posizione successiva. Si noti che l'indirizzo di ritorno è posizionato tra il vecchio `ebp` e i parametri `a` e `b` sullo stack. L'indirizzo di ritorno occupa 4 byte (la dimensione di un puntatore nell'architettura x86 a 32 bit).

Quindi, per accedere al primo parametro `a`, si utilizza `ebp+8`, poiché `a` si trova 8 byte più in alto rispetto al valore corrente di `ebp` (4 byte per il vecchio `ebp` e 4 byte per l'indirizzo di ritorno). Analogamente, per accedere al secondo parametro `b`, si utilizza `ebp+12`, poiché `b` si trova 12 byte più in alto rispetto al valore corrente di `ebp` (4 byte per il vecchio `ebp`, 4 byte per l'indirizzo di ritorno e 4 byte per il parametro `a`).

### Corpo
Le istruzioni `mov eax, [ebp+8]` e `mov ecx, [ebp+12]` caricano i valori dei parametri `a` e `b` nei registri `eax` e `ecx`, rispettivamente.
Questi valori sono accessibili tramite `ebp`, che punta alla base dello stack per questa chiamata di funzione.
Successivamente, l'istruzione `add eax, ecx` esegue l'operazione di somma e memorizza il risultato nel registro `eax`.

### Epilogo

1.  `pop ebp`: L'istruzione `pop` legge il valore nella posizione attuale del registro `esp` (che punta al vecchio valore di `ebp` nello stack) e lo copia nel registro `ebp`. Quindi, il registro `esp` viene automaticamente incrementato di 4 byte (la dimensione di un puntatore nell'architettura x86 a 32 bit), puntando ora all'indirizzo di ritorno.
2.  `ret`: L'istruzione `ret` ritorna al chiamante estraendo l'indirizzo di ritorno dalla cima dello stack (attualmente puntato dal registro `esp`). Il registro `esp` viene nuovamente incrementato di 4 byte per ripulire l'indirizzo di ritorno dallo stack. Il risultato della somma, memorizzato nel registro `eax`, viene passato al chiamante.

