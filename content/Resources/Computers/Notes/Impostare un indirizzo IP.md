---
tags:
  - Windows
  - Networking
  - Tutorial
---


Per impostare un indirizzo IP su Windows andare sulle solite connessioni di rete -> tasto dx -> proprietà -> Protocollo internet v4 -> Proprietà.
Si apre una schermata analoga a questa:

![[image 10.png]]

#### Indirizzo IP

Indirizzo da assegnare a quella scheda di rete, esempio 198.168.1.44.

#### Subnet mask

Maschera di sottorete che serve per descrivere la dimensione della rete in cui mi trovo.
Per esempio 255.255.255.0 indica che i primi 3 byte sono costanti, quindi 198.168.1 mentre il quarto è variabile, da 0 a 255 (in verità il primo e l'ultimo non vengono mai usati, quindi in pratica è da 1 a 254).
Questa informazione serve per dire al sistema operativo se una richiesta verso un determinato indirizzo IP deve essere gestita localmente (chiamate ARP a tutti i PC della sottorete con risposta dell'IP chiamato) oppure dal default gateway, tipo il router (esempio chiamate a internet).
Se non indicassi questa maschera il PC non può distinguere un indirizzo IP locale da uno globale.

#### Gateway predefinito

Indirizzo IP a cui mandare i pacchetti che non sono destinati alla mia sottorete (vedi subnet mask). Tipicamente è il router, che si occupa di instradare i pacchetti su internet.
