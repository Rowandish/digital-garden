---
tags:
  - Coding
  - Tricks
---


La riga `int digit = c - '0';` serve per convertire il carattere della stringa in un numero intero.
In C#, i caratteri sono rappresentati come codici ASCII e `0` ha il codice ASCII `48`. Sottraendo `0` dal carattere del numero (quindi è equivalente a fare `c - 48`), si ottiene un numero intero corrispondente alla cifra del numero.
Per esempio, se il carattere è `3` la sua rappresentazione in ASCII è 51, sottraendo 48 si ottiene 3.