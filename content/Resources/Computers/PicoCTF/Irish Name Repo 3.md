---
tags:
  - WebExploitation
  - PicoCTF2019
---


## Problema
There is a secure website running at https://2019shell1.picoctf.com/problem/45112/ (link) or http://2019shell1.picoctf.com:45112. Try to see if you can login as admin!

## Soluzione

Dall'Html vedo il codice HTML:
`<input type="hidden" name="debug" value="0">`
Matto il valore 1 e vedo la password printata e la query eseguita.
Dato che mettendo n lettere uguali ottengo n lettere diverse uguali è un cifrario di cesare, online trovo che è a passo 13.
Ora semplicemente procedo con la cifratura dell'injection a passo 13.

`' or '1'='1` -> `' be '1'='1`

Risolto!

Flag: `picoCTF{3v3n_m0r3_SQL_9a2f17b3}`


