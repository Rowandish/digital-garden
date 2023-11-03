---
tags:
  - Linux
  - PublishedPosts
---


La prima regola per avere un firewall sicuro è droppare tutto il traffico tranne quello che non soddisfa le chain impostate, non il contrario.
Le prime righe di una tabella iptables quindi devono essere le seguenti

```shell
iptables -P INPUT DROP
iptables -P OUTPUT ACCEPT
```
che droppano tutte i pacchetti in ingresso e invece non filtrano i pacchetti in uscita.

Se vogliamo inoltre che il sever faccia da NAT devo permettere l'inoltro di pacchetti con la seguente riga
```shell
iptables -P FORWARD ACCEPT
```

Altrimenti scrivo:
```shell
iptables -P FORWARD DROP
```

Spesso voglio creare un firewall stateful, quindi che accetta tutti i pacchetti relativi ad una connessione già in essere.
Inoltre aggiungo una secoda riga che droppa tutti i pacchetti "invalidi".
Per fare questo scrivo:
```shell
iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP
```

Infine permetto i pacchetti che arrivano da lo (loopback) che possono essere utilizzati da applicazioni e serivizi interni al server

```shell
iptables -A INPUT -i lo -j ACCEPT
```

## Esempi

### Caricamento di script iptables
Spesso può risultare comodo non avere tutti gli script di iptables nello stesso file monolitico, ma dividere in più file che effettuano logiche distinte.
Posso creare una cartella (chiamata per esempio `iptables.d`) in cui inserire regole aggiuntive, e caricarle nello script principale (`/etc/iptables`) con il seguente codice:
```shell
for f in /etc/iptables.d/*
do
  if [[ -x "$f" ]]
  then
  $f
  fi
done
```

### SSH con protezione brute force
Esigenza: voglio potermi connettere dall'esterno ad un determinato indirizzo IP in ssh nella maniera più sicura possibile.

Per prima cosa è necessario evitare di utilizzare la porta 22 in quanto è la classica porta che viene testata per eventuali attacchi. Quindi effettuo un forward dei pacchetti indirizzati verso una porta scelta casualmente (es. 7253) verso la porta 22 di un indirizzo IP interno.
```shell
iptables -t nat -A PREROUTING -d 94.138.169.150 -p tcp --dport 7253 -j DNAT --to-destination 192.168.1.191:22
```
Ora aggiungo un ulteriore livello di protezione permettendo solo 4 **nuove** connessioni al minuto:
```shell
iptables -t filter -A FORWARD -d 192.168.1.191 -p tcp -m tcp --dport 22 -m state --state NEW -m limit --limit 4/min --limit-burst 4 -j ACCEPT
```
però devo indicare che tutti i pacchetti che sono riferiti a connessioni già stabilite possono essere accettati
```shell
iptables -t filter -A FORWARD -d 192.168.1.191 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
```
Tutti i pacchetti invece che non rientrano nelle precedenti due chain devono invece essere droppati:

```shell
iptables -t filter -A FORWARD -d 192.168.1.191 -p tcp -m tcp --dport 22 -j DROP
```

Infine devo rimappare i pacchetti in uscita dal mio indirizzo IP interno con l'indirizzo IP pubblico, altrimenti il ricevitore li droppa sicuramente in quanto non coerenti con l'indirizzo di destinazione.
```shell
iptables -t nat -A POSTROUTING -s 192.168.1.191 -p tcp --sport 22 -j SNAT --to-source 94.138.169.150
```