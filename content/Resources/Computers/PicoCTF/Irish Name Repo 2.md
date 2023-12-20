---
tags:
  - WebExploitation
  - PicoCTF2019
---


## Problema

There is a website running at [https://2019shell1.picoctf.com/problem/41025/](https://2019shell1.picoctf.com/problem/41025/). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://2019shell1.picoctf.com:41025

## Soluzione

Procedere con un attacco di Sql Injection commentando il controllo password, quindi utilizzare, per esempio,

*  **Username**: `admin'--`
*  **Password**: `qualsiasi stringa va bene`

Ottengo:

`picoCTF{m0R3_SQL_plz_83dad972}`

N.B. Per approfondire il tipo di attacco leggere questo [cheat sheet](https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/).
