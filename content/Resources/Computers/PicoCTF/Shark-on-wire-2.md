---
tags:
  - Forensics
  - PicoCTF2019
---


## Problema

We found this packet capture. Recover the flag that was pilfered from the network. You can also find the file in /problems/shark-on-wire-2_0_3e92bfbdb2f6d0e25b8d019453fdbf07.

## Soluzione

Apriamo il pacchetto con Wireshark e proviamo a filtrare per porta, per esempio se filtriamo con `udp.port == 22` otteniamo un serie di pacchetti che hanno una cosa strana: tutti il contenuto `Data` è uguale tranne per il primo e ultimo pacchetto che hanno come contenuto `Start` e `End`.
Questo mi fa sospettare che la comunicazione che mi interessa sia contenuta in questi pacchetti.
Questi pacchetti però sono identici in tutto e per tutto tranne per una cosa: la Src Port. Questa cambia per ogni pacchetto e tutte iniziano con 5.
Provo a scrivere tutte le porte trovate senza il 5 iniziale:
```
112 105 99 111 67 84 70 123 112 49 76 76 102 51 114 51 100 95 100 97 116 97 95 118 49 97 95 115 116 51 103 48 125
```
Forse questi numero sono una codifica ASCII del carattere in questione.
Provo a decodificarli e ottengo:
```
picoCTF{p1LLf3r3d_data_v1a_st3g0}
```

