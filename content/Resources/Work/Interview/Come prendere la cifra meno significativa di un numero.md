---
tags:
  - Tricks
  - Coding
---
Per ottenere la cifra meno significativa di un numero devo utilizzare l'operatore modulo `%` che restituisce il resto di una divisione tra due numeri.
Poiché vogliamo estrarre l'ultima cifra del numero originale, utilizziamo l'operatore modulo per ottenere il resto della divisione tra il numero originale e 10: il risultato è l'ultima cifra del numero originale.
Ad esempio, se il numero originale fosse `321`, l'operazione `321 % 10` fornisce `1`, che è l'ultima cifra del numero originale.