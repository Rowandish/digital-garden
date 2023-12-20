---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


La concatenazione di stringhe è una delle operazioni più frequenti nello sviluppo. In C# esistono numerosi modi per concatenare stringhe, vediamone qualcuno.

## Operatori `+` e `+=`

Questi operatori permettono di concatenare in modo chiaro due stringhe, anche se spesso l'interpolazione risulta ancora più leggibile.

## Interpolazione 

L'interpolazione permette di ottenere lo stesso risultato della concatenazione ma il codice risulta molto più chiaro e parlante.

## `String.Format`

Questo metodo permette di esplicitare le variabili che voglio inserire nella stringa. Può essere utile per gestire il multilingua.

## `StringBuilder`

Lo StringBuilder viene utilizzato quando voglio costruire una stringa complessa che prevede tanti passaggi (tipicamente per mezzo di un for). In caso di applicazioni molto veloci questo metodo è da preferire.

## `String.Join`

Questo utilissimo metodo permette di ottenere una stringa unica a partire da una lista. I vari elementi della lista vengono uniti da un separatore impostato come primo parametro dello `string.Join`.

### Aggregate

Il seguente metodo lo scrivo per completezza ma, dato che internamente non utilizza `StringBuilder`, ha prestazioni orribili.

## E ora… quale utilizzare?

Come abbiamo visto esistono vari modi per concatenare stringhe in C#, da questo [interessante post](https://www.chinhdo.com/20070929/stringbuilder-part-2/) otteniamo le seguenti regole:

-   Quando voglio concatenare 4 o meno stringhe conviene utilizzare la concatenazione tradizionale
-   Quando voglio concatenare più di 5 stringhe conviene `StringBuilder`
-   Quando voglio concatenare una stringa molto grande formata da varie frasi conviene utilizzare o il carattere `@` prima della stringa o il `+` inline.
-   Quando utilizzi lo `StringBuilder` indica la capacità iniziale il più vicino possibile alla dimensione finale della stringa.

## Approfondimento

Per approfondire le stringhe in C# rimando al mio articolo [[Le stringhe in C#]].