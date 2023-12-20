---
tags:
  - Cryptography
  - PicoCTF2019
---


## Problema

Lets decrypt this: ciphertext? Something seems a bit small.

![[ciphertext.txt]]

## Soluzione

Aprendo il file vedo che e=3.
Da Wikipedia scopro che se e è piccolo posso effettuare la radice cubica di ciphertext e ottenere già il messaggio decrittato senza considerare N.
Con questo algoritmo in Python ottengo il valore in questione:
![[cube_root.py]]
Per verificare che il metodo si possa applicare correttamente devo verificare che tale numero sia minore di n. Dato che è minore posso procedere.
Converto il valore in HEX (usando [questo] https://www.rapidtables.com/convert/number/decimal-to-hex.html) e successivamente in ASCII usando [questo](https://www.rapidtables.com/convert/number/hex-to-ascii.html) e ottengo:
`picoCTF{n33d_a_lArg3r_e_0a41ef50}`
