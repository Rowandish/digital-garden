---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


Il contenuto di questo articolo è una libera traduzione dell’articolo di Jon Skeet trovabile [qui](http://csharpindepth.com/Articles/General/Strings.aspx).
* * *

## 1.Introduzione

Il tipo `System.String` (abbreviato in `string`) è uno dei tipi più importanti del .NET e, purtroppo, non viene usato spesso correttamente.
In questo articolo troveremo tutte le caratteristiche base del tipo, oltre ad un approfondimento su come concatenare stringhe usando lo `StringBuilder`.

### 1.1 Cosa è una stringa?
Una stringa è una sequenza di caratteri. Ogni carattere è un `Unicode` nel range che parte da `U+0000` a `U+FFFF`. Il tipo string ha le seguenti caratteristiche:

- è un **reference type**: data la sua immutabilità (vedi il punto successivo), spesso viene confuso con un _value type_ in quanto si comporta in maniera analoga (vedi approfondimento [qui](http://ilprogrammatorepigro.tumblr.com/post/136494335256/passaggio-di-parametri)).
- è **immutabile**: il contenuto di una stringa nonn può mai essere cambiato. A causa di questo spesso non viene cambiato il contenuto, ma la **variabile**. Per esempio, il `codice s = s.Replace ("foo", "bar");` non cambia il contenuto della stringa `s` di origine, ma cambia il **valore** di `s` ad una nuova stringa, che è una copia di quella vecchia con "_foo_" sostituito da "_bar_"
- **Può contenere valori a null**: un programmatore di C è abituato al fatto che le stringhe sono sequenze di caratteri terminati da `\0`, il carattere `null`. In C#, a differenza del C, le stirnghe possono contenere più caratteri null, però altre classi spesso considerano una stringa terminata al primo valore `null`, quindi all'atto pratico è come il C.
- **Sovrascrive l'operatore**: quando viene usato l'operatore **===** per confrontare due stringhe, viene chiamato il metodo `Equals`, che controlla l'uguaglianza del contenuto delle due stringhe invece della loro referenza (cosa che invece avviene con l'utilizzo di **===** con altri tipi di dato). Conseguentemente `"hello".Substring(0, 4)=="hell"` è uguale a true anche se i puntatori delle due stringhe sono ovviamente diversi.

### 1.2 Letterali (literals)
I literlas sono il modo in cui una stringa viene hard codata nel codice. Vi sono due tipi di letterali in C#

- **Letterali regolari**: cominciano e terminano con `"` ed alcuni caratteri (come `"`, `\`, CF e LF) devono essere escapati al suo interno
- **Letterali verbatim**: permettono qualsiasi letterale all'interno della stringa e si distinguono per avere una chiocciola @ prima della virgoletta iniziale

| Letterali regolari | Letterali verbatim | Risultato |
|--------|--------|--------|
|"Hello"|@"Hello"|Hello |
|"Backslash: \\"|@"Backslash: \"|Backslash: \|
|"Quote: \""|@"Quote: """|	Quote: "|
|"CRLF:\r\nPost CRLF"|@"CRLF: <br> Post CRLF"|CRLF: <br> Post CRLF|

## 2. Concatenazione di stringhe in .NET
Il contenuto di questo articolo è una libera traduzione dell’articolo di Jon Skeet trovabile [qui](http://www.yoda.arachsys.com/csharp/stringbuilder.html).
* * *
Uno dei primi consigli di efficenza che un programmatore .NET riceve è usare `StringBuilder` per concatenare le stringhe a causa del problema descritto nella sezione successiva.

### 2.1 Problema
Il problema di presenta quando devo costruire una stringa con grandezza crescente, come nell'esempio seguente
```csharp
string x = "";
for (int i=0; i < 100000; i++)
{
x += "!";
}
```
Un'operazione del genere impiega circa 10 secondi, raddoppiando il numero di iterazioni anche un minuto. Questo perchè le stringhe, come indicato nella sezione introduttiva, sono **immutabili**: il fatto di usare `+=` non significa che ho un append dinamico del carattere "!" alla stringa, infatti `x += "!"` è identico a `x = x+"!"`, che significa **creare una stringa completamente nuova, allocare sufficente memoria per tutto, copiare tutti i valori di `x` alla nuova variabile aggiungendo un "!" alla fine**.
Mano a mano che la stringa cresce, crescono anche i dati da copiare da una variabile all'altra.
Questo metodo è ovviamente inefficente, e quì viene in aiuto lo `StringBuilder`.

### 2.2 Soluzione
L'esempio indicato sotto è analogo nel comportamento a quello della sezione precedente ma con l'utilizzo dello `StringBuilder`.
```csharp
StringBuilder builder = new StringBuilder();
for (int i=0; i < 100000; i++)
{
builder.Append("!");
}
string x = builder.ToString();
```
Questo metodo impiega 40ms con milioni di iterazioni, un incremento di performance notevole.
Questo accade in quanto non ho la copia continua di dati: solo la stringa che stiamo appendendo viene copiata in quanto StringBuilder ha un suo buffer interno e i nuovi caratteri vengono aggiunti a questo buffer. Questo viene ingrandito (solitamente raddoppiato) solo se non può contenere più dati.
Qualora conoscessimo la lunghezza finale della stringa (ed è questo il caso) possiamo rendere il metodo sopra ancora più efficente inserendola a costruttore dello `StringBuilder`: in questo caso non ho la copiatura di alcun dato.

### 2.3 Quando usare lo StringBuilder
Non sempre è vero che per concatenare le stringhe la soluzione migliore sia lo `StringBuilder`, dipende caso per caso.
Per esempio, consideriamo il seguente codice, che utilizza la normale concatenazione:
```csharp
string name = firstName + " " + lastName;
Person person = new Person (name);
```
confrontato con il seguente che invece usa lo `StringBuilder`:
```csharp
// Bad code! Do not use!
StringBuilder builder = new StringBuilder();
builder.Append (firstName);
builder.Append (" ");
builder.Append (lastName);
string name = builder.ToString();
Person person = new Person (name);
```
Avere un codice incredibilmente meno leggibile per ottenere un guadagno di prestazioni così marginale è sicuramente sbagliato, ammettendo che la seconda versione sia comunque più efficente. Il problema è che così non è!
La prima versione (assumendo che firstName e lastName siano vere variabili e non costanti) compila con `String.Concat` nel modo seguente:
```csharp
string name = String.Concat (firstName, " ", lastName);
Person person = new Person (name);
```
`String.Concat` prende un insieme di stringhe in ingresso e le concatena. Ora, `String.Concat` può sapere la lunghezza delle stringhe da concatenare prima che questa avvenga, conseguentemente non è encessaria nessuna copiatura inutile in quanto i dati sono copiati nella nuova stirnga che è esattamente della lunghezza giusta.
`StringBuilder` invece non conosce la grandezza del buffer da utilizzare e probabilmente, in questo caso, utilizzerà un buffer di grandezza maggiore di quello necessario, oltre all'overhead dovuto dall'utilizzo di un oggetto aggiuntivo (lo `StringBuilder` stesso).
La differenza fondamentale tra i due esempi è che in questo caso ho a disposizione tutte le stringhe da passare allo `String.Concat`, senza passare per stringhe intermedie. `StringBuilder` invece è utile come contenitore per gestire numerose stringhe intermedie ed eviatare conseguentemente il processo di copia.

### 2.4 Costanti
Le cose diventano più intricate quando si lavora con stringhe costanti (letterali, e `const string`).
Per esempio, cosa succede con questa operazione?
```csharp
string x = "hello" + " " + "there";
```
Ci si aspetta che ci sia una chiamata a `String.Concat`, ma così non è. Questo codice viene compilato esattamente allo stesso modo del codice
```csharp
string x = "hello there";
```
in quanto il compilatore conosce che tutte le parti della stirnga sono costanti, conseguentemente esegue tutte le concatenazioni durante la compilazione del codice, memorizzando la stirnga completa nel codice compilato.
Convertire il codice sopra con uno `StringBuilder` è inefficente di memoria e velocità, oltre a ridurre la leggibilità del codice.

### 2.5 Conclusioni
Ricapitoliamo quando usare lo `StringBuilder` e quando invece la concatenazione normale:

- Usare sempre lo `StringBuilder` quando sto effettuando delle **concatenazioni all'interno di cicli (non banali)**, specialmente quando **non conosco quante operazioni effettuerà il ciclo**. Per esempio, leggere un file un carattere alla volta e creare una stringa con il `+=` è un suicidio.
- Usare la concatenazione quando posso specificare tutto quello che deve essere concatenato in una sola riga di codice (se ho un array considerare `String.Concat` o `String.Join`)
- Non preoccuparsi di rompere i letterali in più pezzi concatenati, al fine di una maggiore leggibilità. Il risultato, a livello di performance, sarà lo stesso