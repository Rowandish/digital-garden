---
tags:
  - Coding
  - SOLID
  - PublishedPosts
---


Il Liskov Substitution Principle è il terzo principio di SOLID introdotti nel libro Clean Architecture di Robert Martin, tradotto anche in italiano da Apogeo.

## Definizione

Il principio definisce che **gli oggetti della superclasse devono essere sostituibili con oggetti delle sue classi figlie senza rompere l'applicazione**. Questo significa che gli oggetti della sottoclasse devono comportarsi allo stesso modo della superclasse.

Quindi ovunque nel mio codice ho uno `new ClassePadre()`, devo poter sostituire questo codice con `new ClasseFiglia()` senza che si rompa nulla nella mia applicazione.

**Questo principio limita l'utilizzo dell'ereditarietà a cose che si comportano in modo uguale, non che hanno le stesse proprietà.**

L'esempio classico è il quadrato figlio di rettangolo: nel mondo reale il quadrato è una forma di rettangolo, quindi sembra corretto fare sì che questo erediti da questo ultimo, ma il comportamento è diverso: il quadrato ha i lati uguali, il rettangolo no.

**Il principio di LPS indica che se se le specifiche della superclasse (Rettangolo) indicano che altezza e larghezza devono essere modificate in modo indipendente, allora un quadrato non potrà mai essere figlio di rettangolo.**

Se invece le specifiche del mio progetto dicono che il rettangolo è immutabile nelle dimensioni, allora il quadrato può esserne un sottotipo.

**E' tutta una questione delle classi figlie che mantengono lo stesso comportamento delle classi padri.**

## Implementazione

Non è semplice fornire un esempio in quanto spesso per poter rispettare il LSP è necessario l'introduzione di varie interfacce al fine di descrivere, tramite queste ultime, il comportamento desiderato dei vari componenti e fare in modo che ogni figlio non abbia dei comportamenti ereditati non voluti.

Nell'esempio del quadrato e del rettangolo, per esempio, dovrò introdurre una interfaccia che indica che la larghezza e la altezza devono essere uguali e fare in modo che il quadrato erediti da questa ultima.

Dovrò introdurre una altra interfaccia che indichi una figura con larghezza che altezza che verrà ereditata sia da rettangolo che quadrato.

## Limiti

Per rispettare l'LSP spesso è necessaria l'introduzione di numerose classi e non sempre questo ne vale la pena.

Questo ultimo può infatti diventare un anti-pattern quando, per rispettarlo, devo riempire il mio codice di astrazioni confusionarie che non aggiungono nulla tranne la complicazione.
