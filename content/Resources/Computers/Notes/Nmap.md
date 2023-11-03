---
tags:
  - Linux
  - PublishedPosts
---


Nmap è un comodissimo tool per ottenere informazioni sulla propria rete locale. Di seguito un elenco di comandi comodi

| Comando | Utilizzo |
|--------|--------|
|`nmap 192.168.1.1`|Ottiene informazioni su un singolo indirizzo IP|
|`nmap -v 192.168.1.1`|Come sopra ma *verbose*|
|`nmap 192.168.1.0/24`|Scan dell'intera sottorete 0-255|
|`nmap -sn 192.168.1.0/24`|Scan della sottorete indicando quali IP sono up and running|
|`nmap -sn 192.168.1.0/24`|Scan della sottorete indicando quali IP sono up and running|
|`nmap -PR 192.168.1.0/24`|Scan della sottorete con informazioni anche sulle porte|
