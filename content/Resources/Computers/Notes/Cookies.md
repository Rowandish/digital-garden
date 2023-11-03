---
tags:
  - WebExploitation
  - PicoCTF2021
---


## Problema

Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:17781/

## Risoluzione

Andando sulla pagina provo a mettere la stringa indicata nel *placehodler* e ottengo un cookie con `name=0`. Se non trova nulla mette `name=-1`. Provando `name=1` vedo che compare un altro cookie. Provo tutti i `name` fino a mettere `name=17` e ottengo la chiave.