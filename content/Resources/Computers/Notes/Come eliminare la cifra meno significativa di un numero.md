---
tags:
  - Coding
  - Tricks
---


In C#, la notazione `/=` è una forma abbreviato per la divisione seguita dall'assegnazione. Così, la riga `number /= 10` significa `number = number / 10`.

Quindi, la riga `number /= 10` elimina la cifra dal numero perché sta dividendo il numero per 10 e assegnando il risultato alla stessa variabile `number`. In questo modo il numero viene diviso per 10 e la cifra meno significativa viene eliminata.

Per esempio, se number fosse 123, la prima volta che si esegue la riga `number /= 10` il valore di number diventa 12 (cioè 123 diviso 10). La seconda volta che si esegue la riga, il valore di number diventa 1 (cioè 12 diviso 10). In questo modo , il algoritmo è in grado di esaminare ogni cifra del numero una alla volta, partendo dalla cifra meno significativa.