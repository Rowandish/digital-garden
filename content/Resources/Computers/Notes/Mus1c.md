---
tags:
  - GeneralSkill
  - PicoCTF2019
---


## Problema

I wrote you a song. Put it in the picoCTF{} flag format

## Soluzione

Leggendo il testo della canzone vedo che ci sono molte parole ripetute, cercando le parole `Put` e `shout` su google scopro che è un linguaggio chiamato [Rockstar](https://codewithrockstar.com/).
Usando il [decoder](https://codewithrockstar.com/online) ottengo una serie di numeri.
Data la loro dimensione sembra ASCII, proviamo a decodificarli e ottengo `rrrocknrn0113r`.
La flag sarà quindi
`picoCTF{rrrocknrn0113r}`
