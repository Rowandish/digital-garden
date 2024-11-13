### SUMIF

- **Scopo**: Somma le celle di un intervallo che soddisfano un criterio specifico.
- **Sintassi**: `SUMIF(intervallo, criterio, [intervallo_somma])`
    - **intervallo**: L'intervallo di celle da valutare in base al criterio.
    - **criterio**: La condizione che determina quali celle devono essere sommate.
    - **intervallo_somma** (opzionale): L'intervallo di celle da sommare. Se omesso, vengono sommate le celle nell'intervallo stesso.
- **Esempio**: `SUMIF(A1:A10, ">5", B1:B10)` somma i valori nell'intervallo `B1:B10`
    per cui i corrispondenti valori in `A1:A10`  sono maggiori di 5.
### SUMIFS

- **Scopo**: Somma le celle di un intervallo che soddisfano una serie di criteri.
- **Sintassi**: `SUMIFS(intervallo_somma, intervallo_criterio1, criterio1, [intervallo_criterio2, criterio2], ...)`
    - **intervallo_somma**: L'intervallo di celle da sommare (notare che nel `SUMIF` questo è il terzo parametro e non il primo)
    - **intervallo_criterio1**: L'intervallo di celle da valutare in base al primo criterio.
    - **criterio1**: La condizione per il primo intervallo.
    - **intervallo_criterio2, criterio2**, ... (opzionale): Ulteriori intervalli di celle e criteri.
- **Esempio**: `SUMIFS(B1:B10, A1:A10, ">5", C1:C10, "<10")` somma i valori in `B1:B10`  per cui i corrispondenti valori in `A1:A10` sono maggiori di 5 e i corrispondenti valori in `C1:C10` sono minori di 10.

### COUNTIF

- **Scopo**: Conta il numero di celle in un intervallo che soddisfano un criterio specifico.
- **Sintassi**: `COUNTIF(intervallo, criterio)`
    - **intervallo**: L'intervallo di celle da valutare.
    - **criterio**: La condizione che determina quali celle devono essere contate.
- **Esempio**: `COUNTIF(A1:A10, ">5")` conta quante celle in `A1:A10` contengono valori maggiori di 5.

### SUMPRODUCT

- **Scopo**: Moltiplica gli elementi corrispondenti di uno o più array e restituisce la somma dei prodotti, quello che in fisica viene detto prodotto scalare.
- **Sintassi**: `SUMPRODUCT(array1, [array2], [array3], ...)`
    - **array1**: Il primo array (intervallo) di numeri da moltiplicare.
    - **array2, array3**, ... (opzionale): Ulteriori array di numeri da moltiplicare. Tutti gli array devono avere le stesse dimensioni.
- **Esempio**: `SUMPRODUCT(A1:A10, B1:B10)` moltiplica ciascun elemento di A1 per elemento corrispondente in B1 e restituisce la somma di questi prodotti.

#### Aggiungere delle condizioni
Posso sfruttare il fatto che un array di booleani si rappresenti come un array di `[0,1]`, per cui un valore moltiplicato per 0 fornisce 0 mentre per 1 fornisce se stesso, per aggiungere delle condizioni al `SUMPRODUCT`
Per esempio `SUMPRODUCT((A1:A5 > 2), (B1:B5 < 40), C1:C5)` fornisce la somma di tutti gli elementi nel range `C1:C5` che hanno il corrispondente valore nella colonna `A` maggiore di 2 e quello nella colonna `B` minore di 40.
La stessa cosa la posso fare con il `*` in questo modo: `SUMPRODUCT((A1:A5 > 2) * (B1:B5 < 40) * C1:C5)`.

## Funzioni di ricerca

### INDEX

La funzione `INDEX` restituisce ==il valore di una cella all'intersezione di una riga e una colonna specifiche all'interno di un intervallo==.

**Sintassi**: `INDEX(intervallo, numero_riga, [numero_colonna])`

- **intervallo**: L'intervallo da cui recuperare il valore.
- **numero_riga**: Il numero della riga all'interno dell'intervallo.
- **numero_colonna**: (Opzionale) Il numero della colonna all'interno dell'intervallo. Se omesso, verrà restituito il valore nella stessa colonna dell'intervallo specificato.

**Esempio**:

```
=INDEX(A1:C3, 2, 3)
```

Restituisce il valore della cella alla seconda riga e terza colonna dell'intervallo `A1:C3`.
E' comodo quando voglio estrarre il valore di una cella variabile: la cella da estrarre cambia in base a determinati variabili.
Ovviamente se invece voglio estrarre il valore di una cella costante basta fare il classico `=CELLA`.

#### Ultimo valore diverso da vuoto
Voglio scrivere l'ultimo valore diverso da vuoto della riga `A1:A10`.
Sfrutto `counta`, che fornisce il numero di celle non vuote in un certo intervallo, per ottenere la colonna di cui vorrò andare a prendere il valore della cella e costruisco quindi la formula in questo modo.
```
=index(A1:A10;1;counta(A1:A10))
```

### MATCH

La funzione `MATCH` cerca un elemento in un intervallo e restituisce la posizione relativa dell'elemento all'interno dell'intervallo.

**Sintassi**: `MATCH(chiave_ricerca, intervallo, [tipo_correspondance])`

- **chiave_ricerca**: Il valore da cercare.
- **intervallo**: L'intervallo di celle in cui cercare.
- **tipo_correspondance**: (Opzionale) Il tipo di corrispondenza. Può essere 1 (corrispondenza meno di, ordinato in ordine crescente), 0 (corrispondenza esatta) o -1 (corrispondenza più di, ordinato in ordine decrescente).

**Esempio**:

```
=MATCH("Mela", A1:A5, 0)
```

Cerca "Mela" nell'intervallo `A1:A5` e restituisce la posizione relativa.

### INDEX + MATCH

`MATCH` trova la posizione di un valore in un intervallo, mentre `INDEX` utilizza quella posizione per restituire un valore da un altro intervallo.
Supponiamo di avere una tabella con i dati dei dipendenti come segue e devo trovare il dipartimento di un dipendente dato il suo nome.

| A     | B            | C         |
| ----- | ------------ | --------- |
| Nome  | Dipartimento | Stipendio |
| Maria | Marketing    | 50000     |
| Luca  | Vendite      | 55000     |
| Anna  | IT           | 60000     |
| Paolo | HR           | 45000     |
1. Usare `MATCH` per trovare la posizione del nome del dipendente in quanto la funzione `MATCH` cercherà il nome del dipendente nella colonna `A` e restituirà la posizione relativa.
```plaintext
=MATCH("Anna", A2:A5, 0)
```
La formula restituirà `3`, poiché "Anna" è al terzo posto nell'intervallo `A2:A5`.

2. Usare `INDEX` per trovare il valore nel dipartimento corrispondente in quanto la funzione `INDEX` utilizzerà la posizione trovata da `MATCH` per restituire il valore dalla colonna `B`. 
   ```plaintext
   =INDEX(B2:B5, MATCH("Anna", A2:A5, 0))
   ```
La formula restituirà "IT", che è il dipartimento di "Anna".

### XLOOKUP

La funzione `XLOOKUP` cerca un valore in un intervallo e restituisce un valore corrispondente da un altro intervallo.
E' la versione moderna della combinazione tra `INDEX` e `MATCH` detta sopra.

**Sintassi**: `XLOOKUP(chiave_ricerca, intervallo_ricerca, intervallo_restituzione, [valore_se_non_trovato], [modalità_corrispondenza], [modalità_ricerca])`

- **chiave_ricerca**: Il valore da cercare.
- **intervallo_ricerca**: L'intervallo in cui cercare il valore.
- **intervallo_restituzione**: L'intervallo da cui restituire il valore corrispondente.
- **valore_se_non_trovato**: (Opzionale) Il valore da restituire se non viene trovata una corrispondenza.
- **modalità_corrispondenza**: (Opzionale) Specifica il tipo di corrispondenza (esatta o approssimativa).
- **modalità_ricerca**: (Opzionale) Specifica la modalità di ricerca (dall'alto al basso o dal basso all'alto).

**Esempio**:

```
=XLOOKUP("Mela", A1:A5, B1:B5, "Non trovato")
```

Cerca "Mela" nell'intervallo `A1:A5` e restituisce il valore corrispondente dall'intervallo `B1:B5`.

### VLOOKUP

La funzione `VLOOKUP` cerca un valore nella prima colonna di un intervallo e restituisce un valore in una colonna specificata della stessa riga.

**Sintassi**: `VLOOKUP(chiave_ricerca, intervallo, indice_colonna, [is_sorted])`

- **chiave_ricerca**: Il valore da cercare.
- **intervallo**: L'intervallo di celle in cui cercare.
- **indice_colonna**: Il numero della colonna nell'intervallo da cui restituire il valore.
- **is_sorted**: (Opzionale) Indica se l'intervallo è ordinato. TRUE (ordinato) o FALSE (non ordinato).

**Esempio**:
```
=VLOOKUP("Mela", A1:C5, 3, FALSE)
```
Cerca "Mela" nella prima colonna dell'intervallo `A1:C5` e restituisce il valore nella terza colonna della stessa riga.


## Funzioni accessorie

### ROW
La funzione `ROW` restituisce il numero della riga di una cella specificata. Se non viene specificata alcuna cella, restituisce il numero della riga della cella in cui viene inserita la funzione.

**Sintassi**: `ROW([riferimento])`
- **riferimento**: (Opzionale) La cella o l'intervallo di celle di cui si vuole ottenere il numero della riga. Se omesso, si utilizza la posizione della cella che contiene la funzione.

**Esempi**:
```plaintext
=ROW(A5)
```
Restituisce `5`, poiché la cella A5 si trova nella quinta riga.

```plaintext
=ROW()
```
Se inserita nella cella B3, restituisce `3`, poiché la funzione si trova nella terza riga.

### COL
La funzione `COL` restituisce il numero della colonna di una cella specificata. Se non viene specificata alcuna cella, restituisce il numero della colonna della cella in cui viene inserita la funzione.

**Sintassi**: `COL([riferimento])`

- **riferimento**: (Opzionale) La cella o l'intervallo di celle di cui si vuole ottenere il numero della colonna. Se omesso, si utilizza la posizione della cella che contiene la funzione.

**Esempi**:
```plaintext
=COL(C2)
```
Restituisce `3`, poiché la colonna C è la terza colonna.

```plaintext
=COL()
```
Se inserita nella cella D4, restituisce `4`, poiché la funzione si trova nella quarta colonna.

### INDIRECT
La funzione `INDIRECT` restituisce il ==contenuto di una cella specificata come testo==, permettendo di costruire riferimenti dinamici basati sul contenuto di altre celle.

**Sintassi**: `INDIRECT(riferimento_cella, [è_a1])`

- **riferimento_cella**: Una stringa che rappresenta un riferimento di cella.
- **è_a1**: (Opzionale) Un valore booleano che specifica se il riferimento è in formato A1 (TRUE o omesso) o in formato R1C1 (FALSE).

**Esempi**:
```plaintext
=INDIRECT("A1")
```
Restituisce il valore della cella A1. In questo esempio l'utilizzo non ha senso in quanto è identico a fare `=A1` ma invece ha molto più senso quando la stringa di testo contenente la cella viene costruita concatenando altri valori come nell'esempio sotto.
```plaintext
=INDIRECT("B" & 2)
```
Restituisce il valore della cella B2, concatenando la colonna "B" con il numero 2.

### Utilizzo Combinato

L'uso combinato di queste funzioni può risultare molto potente. Ecco alcuni esempi pratici:

1. **Somma di una colonna variabile**:
   Supponiamo di voler sommare tutti i valori di una colonna specificata in una cella, ad esempio nella cella D1.

   **Valore in D1**: `B`

   **Formula per la somma**:
   ```plaintext
   =SUM(INDIRECT(D1 & "1:" & D1 & "10"))
   ```

   Questa formula somma i valori dalla cella B1 alla cella B10, basandosi sul contenuto della cella D1.

2. **Riferimento dinamico con `ROW` e `COL`**:
   Se si desidera creare un riferimento dinamico che cambia in base alla posizione della cella in cui è inserita la formula, si possono usare `ROW` e `COL` insieme a `INDIRECT`.

   Supponiamo di avere una formula nella cella C3 e di voler fare riferimento alla cella che si trova una riga sotto e una colonna a destra.

   **Formula**:
   ```plaintext
   =INDIRECT(ADDRESS(ROW() + 1, COL() + 1))
   ```

   Se inserita in C3, la formula restituirà il valore della cella D4.

3. **Creare un intervallo dinamico per una funzione**:
   Immagina di voler creare un intervallo dinamico che si estende da una cella specifica fino alla fine dei dati in una colonna.

   **Valore di partenza in E1**: `A1`

   **Formula per definire l'intervallo dinamico**:
   ```plaintext
   =INDIRECT(E1 & ":" & "A" & ROW(A:A))
   ```

   Questa formula crea un intervallo che parte da A1 e si estende fino all'ultima riga con dati nella colonna A.

Questi esempi mostrano come combinare `ROW`, `COL` e `INDIRECT` per creare riferimenti e intervalli dinamici in Google Sheets, rendendo i fogli di calcolo più flessibili e potenti.


## Mutuo

### PMT

Permette di ottenere l'ammontare della rata di un prestito basato su tassi di interesse e periodi di ammortamento costanti, come tipicamente un mutuo a tasso fisso classico.
La sintassi della funzione PMT è la seguente:
```css
PMT(tasso, num_rate, valore_attuale, [valore_futuro], [tipo])
```
- **tasso**: Il tasso di interesse per periodo. Se il tasso di interesse è annuale e i pagamenti sono mensili, questo valore non deve essere diviso per 12 ma la formula corretta è $(1+tasso)^{\frac{1}{12}}-1$. Alcune banche (esempio banca Sella) però fanno banalmente diviso 12.
- **num_rate**: Il numero totale di pagamenti del prestito. Se per esempio ho un mutuo di 10 anni con pagamento mensile sarà $10*12 = 120$
- **valore_attuale**: valore del prestito.

#### Tasso variabile

La funzione `PMT` funziona come sopra tranne per alcuni accorgimenti:
* Il primo parametro indica il tasso di interesse al periodo precedente
* Il numero di rate è variabile e descresce col passare del tempo, indica quindi le rate rimanenti e non il numero complessivo
* Il valore attuale indica il debito residuo al periodo precedente
### IPMT

Permette di calcolare l'importo degli interessi pagati di una determinata rata di un prestito ammortizzato.
La sintassi della funzione IPMT è la seguente:
```css
IPMT(tasso, periodo, numero_periodi, capitale, [valore_futuro], [tipo])
```
- **tasso**: Il tasso di interesse per periodo.  Se il tasso di interesse è annuale e i pagamenti sono mensili, questo valore non deve essere diviso per 12 ma la formula corretta è $(1+tasso)^{\frac{1}{12}}-1
- $. Alcune banche (esempio banca Sella) però fanno banalmente diviso 12.
- **periodo**: Il periodo (quindi il numero del pagamento) per cui si vuole calcolare l'interesse. Esempio se voglio la terza rata questo valore sarà 3 (inizia a contare da 1). Deve essere un numero compreso tra 1 e numero_periodi.
- **numero_periodi**: Il numero totale di periodi di pagamento (es. per un prestito di 5 anni con pagamenti mensili, numero_periodi sarà 60).
- **capitale**: L'importo del prestito.

### RATE

Permette di calcolare il tasso di interesse per un periodo specifico, come il tasso di interesse di un prestito o di un investimento.

```css
RATE(periodi, pagam, valore_attuale)
```
- **periodi**: Il numero totale di periodi di pagamento (esempio il numero di mesi) per il prestito o l'investimento.
- **pagam**: Il pagamento effettuato in ciascun periodo. Questo valore rimane costante durante tutta la durata del prestito o dell'investimento e include capitale e interessi, ma non altre spese o tasse. Questo valore deve essere negativo.
- **pv**: Il valore del prestito

### NPER
Permette di determinare il numero di periodi necessari per estinguere un prestito dato un tasso di interesse costante e pagamenti periodici costanti.
```css
NPER(tasso, pagamento, valore_attuale, [valore_futuro], [tipo])
```
- **tasso**: Il tasso di interesse per periodo.
- **pagamento**: L'importo della rata
- **valore_attuale**: L'importo del prestito



