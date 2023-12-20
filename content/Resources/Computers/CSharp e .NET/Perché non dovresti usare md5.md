---
tags:
  - Coding
  - PublishedPosts
---
## Introduzione

Le [funzioni di hash](https://it.wikipedia.org/wiki/Funzione_di_hash) permettono di ottenere una sequenza di bit tramite l'utilizzo di funzioni matematiche in base ai dati in ingresso; la loro caratteristica fondamentale è che a partire dal loro output è impossibile risalire agli input.

Ne ho già parlato nell'articolo sul funzionamento dei [[Bitcoin]]: lo SHA256 è la base dell'algoritmo di consenso PoW.

Esistono numerose funzioni di hash, i fattori per cui scegliere uno rispetto all'altro sono principalmente 3:

- **Velocità**: maggiore è la velocità maggiori saranno le performance del sistema;
- **Lunghezza**: minore è la lunghezza dell'hash minore è lo spazio su disco richiesto per salvarlo;
- **Sicurezza**: deve essere impossibile risalire alla sequenza di input originaria e inoltre deve essere estremamente difficile avere collisioni, quel problema per cui due sequenze diverse producono la stessa uscita.

I tre algoritmi di hashing più utilizzati sono MD5, SHA1 e SHA256. Il primo produce un output a 16 byte, il secondo 20 byte e il terzo 32 byte.

Ovviamente la probabilità di avere collisioni diminuisce con l'aumentare dei byte dell'hash prodotto, ma anche la velocità ne risente.

## La vulnerabilità di MD5

Nel Marzo 2005 in [questo articolo](http://www.infosec.sdu.edu.cn/paper/md5-attack.pdf) Xiaoyun Wang e Hongbo Yu sono riusciti a rompere l'algoritmo MD5, quindi riuscendo a trovare un algoritmo che permettesse di trovare due sequenze di 128 bytes che forniscono lo stesso hash MD5.

Questo algoritmo può essere usato per creare quindi file diversi che però condividono lo stesso hash MD5 e questo può portare a diverse vulnerabilità (tipicamente l'hash MD5 viene utilizzato per controllare che un file non sia stato contraffatto da una persona terza malevola).

Per approfondire i collisioni attack consiglio la lettura di [questa pagina](https://en.wikipedia.org/wiki/Collision_attack#Chosen-prefix_collision_attack) di Wikipedia; in [questa pagina](https://www.mscs.dal.ca/~selinger/md5collision/) invece trovate altre informazioni e risorse.

## PicoCTF - It is my Birthday

Qualche anno fa PicoCTF ha proposto un problema che si basava proprio sul problema delle collisioni di MD5: l'obiettivo è inserire nella pagina [http://mercury.picoctf.net:11590/](http://mercury.picoctf.net:11590/) due pdf di diverso contenuto con lo stesso hash MD5.

Conoscendo tale vulnerabilità il gioco è stato semplice, basta scaricare due file con lo stesso MD5 ([hello.exe e erase.exe](https://www.mscs.dal.ca/~selinger/md5collision/) o [message1.bin e message2.bin](https://crypto.stackexchange.com/a/1778)), rinominare l'estensione in .pdf e caricarli nell'interfaccia.

Se tutto è stato svolto correttamente comparirà il codice sorgente del server con la chiave aggiunta come commento.

// FLAG: picoCTF{c0ngr4ts\_u\_r\_1nv1t3d\_3d3e4c57}
