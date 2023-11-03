---
tags:
  - Tutorial
  - Networking
---


## 1. Indirizzi IP Privati

Gli indirizzi IP privati si intendono alcune classi di indirizzi IPv4 riservate alle reti locali allo scopo di ridurre le richieste di indirizzi pubblici.
Chiunque può utilizzare questi indirizzi per la propria rete locale, perché i pacchetti con tali indirizzi non vengono utilizzati per l'indirizzamento e instradamento tramite protocollo IP dai router Internet verso la rete di trasporto, ed il loro riutilizzo su altre reti locali, oltre a ridurre il numero di indirizzi IP utilizzati come da obiettivo originario, non genera conflitti con analoghi indirizzi posti su altre reti locali in quanto non visibili dall'esterno della sottorete locale risultando appunto privati e non indirizzi IP pubblici.
Nel caso occorra connettere ad Internet una rete locale che utilizza queste classi di indirizzi si deve perciò ricorrere al network address translation (NAT) il quale multipla (o mappa) più indirizzi IP privati su un solo indirizzo IP pubblico, visibile all'esterno della sottorete ed utilizzabile per l'instradamento.
La classe di indirizzi privati utilizzabili è:

```
192.168.0.0 – 192.168.255.255
```

## 2. Comunicazione
Per la comunicazione è necessario che tutti i dispositivi che vogliono parlare siano sulla stessa sottorete privata, quindi, per esempio posso scegliere
`192.168.1.X` come range di indirizzi, quindi tutti i dispositivi da `192.168.1.1` a `192.168.1.254` potranno comunicare.
Potenzialmente potrei scegliere anche `192.168.100.X` e così via, non c'è alcuna differenza.
L'importante è impostare come netmask, qualora il valore X sia nell'ultima classe di indirizzi, come quasi sempre è, a `255.255.255.0`.