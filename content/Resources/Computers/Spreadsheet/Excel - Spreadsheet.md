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



