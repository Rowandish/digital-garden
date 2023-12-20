---
tags:
  - Cryptography
  - PicoCTF2019
---


## Problema
The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?.

## Soluzione

La tabella è la cifratura di Vigenère (https://it.wikipedia.org/wiki/Cifrario_di_Vigen%C3%A8re), per risolverlo utilizzare un decoder online come [questo](https://www.dcode.fr/vigenere-cipher).
Ottengo il messaggio: `CRYPTOISFUN`, che quindi porta alla chiave:
`picoCTF{CRYPTOISFUN}`