---
tags:
  - WebExploitation
  - PicoCTF2019
---


## Problema

Check the admin scratchpad! https://2019shell1.picoctf.com/problem/21893/ or http://2019shell1.picoctf.com:21893

## Soluzione

Aprendo il link trovo un posto dove poter inserire un nome utente, una volta premuto invio viene creato un cookie chiamato "jwt".
Noto inoltre che se loggo come "admin" il sito me lo impedisce: questo significa che in qualche modo dovrò creare il cookie "jwt" firmato in modo corretto che abbia come user "admin", in modo da ingannare il sito e ottenere la password.
Sia dal titolo del problema che dal nome del [[Resources/Money/Crypto/Notes/Token]] capisco che è una forma di autenticazione Java Web [[Resources/Money/Crypto/Notes/Token]], serve capire come questa funzioni.
Andando sul sito ufficiale [jwt.io](https://jwt.io/) trovo che un jwt è formato da tre parti divise da ".", l'header, il payload e la firma.
Effettuando il decode di tale jwt dal sito ottengo che il metodo di crittografia è H256 e che il payload contiene un solo valore, che è il nome utente che noi abbiamo inserito.
Ora serve capire il secret, per fare questo il sito ci indica di utilizzare il cracker John The Ripper (link in basso a dx).
Proviamo subito con un attacco al dizionario, se ci va bene risparmieremo un sacco di tempo.
Un dizionario buono è [rockyou](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt).
Scarichiamo John, scarichiamo il [[Resources/Money/Crypto/Notes/Token]] come file e lanciamo il comando:
```
./john.exe [[token]].jwt --wordlist=./rockyou.txt --format=HMAC-SHA256
```
ottengo il secret:
```
ilovepico
```
Ora torno su jwt.io, inserisco nel payload il nome "admin" e nel secret "ilovepico" e ottengo un nuovo jwt:
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s
```
Inserendolo come cookie e aggiornando la pagina trovo la flag:
```
picoCTF{jawt_was_just_what_you_thought_c84a0d3754338763548dfc2dc171cdd0}
```
