---
tags:
  - Computers
  - WebExploitation
  - PicoCTF2021
---


## Problema

There is some interesting information hidden around this site [http://mercury.picoctf.net:44070/](http://mercury.picoctf.net:44070/). Can you find it?

## Risoluzione

La chiave si trova nell'`html`, `css`, `robots.txt` e `.htaccess` (`http://mercury.picoctf.net:44070/.htaccess`). Per capire `.htaccess` c'è scritto in robots.txt che il server è **Apache**. Poi comunica che è anche su Apple quindi provo il file `.DS_Store` e completo la chiave.