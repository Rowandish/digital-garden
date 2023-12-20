---
tags:
  - Git
  - PublishedPosts
---
Il **master** è il **branch di default** che viene creato quando creo una nuova repository, questo è a tutti gli effetti un branch quindi può anche essere eliminato (anche se è un caso estremamente remoto).

Tipicamente il master locale segue il master remoto e corrisponde alla vista attuale della mia applicazione al mondo.
**HEAD** è un puntatore al commit più recente del branch sui cui sto lavorando. Tipicamente **HEAD** punta all'ultimo commit di un branch, ma può anche essere diverso qualora abbia eseguito dei *checkout* su particolari commit.

**Origin** è il nome di default che git fornisce alla repository remota. Tipicamente il programmatore lavora su una repository locale, per poi pushare su una repository remota a cui tutti lavorano.