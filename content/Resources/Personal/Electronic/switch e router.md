---
tags:
  - Devices
  - Electronics
---
## 1. Router

Un router un dispositivo di rete che si occupa di instradare i dati, suddivisi in pacchetti, fra sottoreti diverse. Caratteristica fondamentale dei router è l’utilizzo di **indirizzi di livello 3 (rete)** del modello OSI (corrispondente al livello IP dello stack TCP/IP), a differenza dello switch o del bridge che instradano a livello locale sulla base degli indirizzi di livello 2 (collegamento) detti indirizzi MAC e dell’hub che ripete i segnali elettrici del livello fisico (livello 1). Il router inoltre può occuparsi di **assegnare automaticamente indirizzi IP ad ogni dispositivo della rete**. Gli elementi della tabella di instradamento (o routing table) non corrispondono necessariamente a singoli calcolatori ma intere reti (SubNet_ID), ovvero sottoinsiemi anche molto ampi dello spazio di indirizzamento. Per visualizzare l’elenco dei router attraversati durante l’invio di un pacchetto in rete i sistemi operativi mettono a disposizione comandi da digitare nella shell di sistema per l’applicazione di traceroute ovvero tracciamento dei router.

## 2. Switch

Uno switch è un dispositivo di rete che si occupa di commutazione a **livello 2 del modello ISO/OSI**. Lo switch agisce sull’indirizzamento e sull’instradamento all’interno delle reti LAN mediante indirizzo fisico (MAC), **selezionando i frame ricevuti e dirigendoli verso il dispositivo corretto (leggendo il MAC di destinazione)**. L’instradamento avviene per mezzo di una corrispondenza univoca porta-indirizzo.

Quando un nodo A cerca di comunicare con un nodo B, il comportamento dello switch dipende dalla porta cui è collegato B:

- se B è collegato alla stessa porta a cui è collegato A, lo switch ignora il frame;
- se B è collegato a una porta diversa, lo switch inoltra il frame sulla porta a cui è collegato B;
- se lo switch non conosce ancora a quale porta è collegato B, inoltra il frame su tutte le porte.

Normalmente in quest’ultimo caso il nodo destinatario riceverà il pacchetto e risponderà al mittente permettendo allo switch di scoprire a quale porta esso è collegato e così via per tutti gli altri terminali di dislocazione non nota. Alcuni frame hanno un indirizzo destinazione particolare, denominato **broadcast, che indica che sono destinati a tutti i calcolatori della rete**. Uno switch inoltra questi frame su tutte le porte. Per questo si dice che lo switch crea un unico dominio di broadcast. Uno switch è più “intelligente” di un hub Ethernet, che semplicemente ritrasmette i pacchetti fuori da ogni porta dell’hub eccetto la porta su cui è stato ricevuto il pacchetto, incapace di distinguere i diversi destinatari e di ottenere un’efficienza di rete complessivamente inferiore. **Ogni dispositivo collegato a una porta dello switch può trasferire dati a una qualsiasi delle altre porte in qualsiasi momento.** Nella modalità `half duplex`, ogni porta dello switch non può contemporaneamente ricevere e trasmettere al dispositivo a cui è connessa. Al contrario, ciò è possibile nella modalità `full duplex`, assumendo che il dispositivo connesso supporti tale modalità.

## 3. Differenze tra router e switch

Un router ha il compito principale di interconnette più reti insieme e gestire il traffico tra di loro. Principalmente questo fornisce:

- Indirizzamento per tutti i computer della rete
- Firewall
- Gestione del traffico (Quality of Service)
- ACL (Access Control List)
- Accesso alla rete tramite wireless

Uno switch invece connette più computer insieme nella stessa rete e gestisce il traffico tra di loro. Quindi:

- Non fornisce servizi avanzati come firewall e simili
- Sono principalmente usati per espandere la capacità di una rete
- Non forniscono accesso diretto alla rete
- Non sono il punto di contatto tra il tuo pc e la rete esterna
- Sono usati spesso insieme ad un router

Quindi **il router è il “cervello” della rete** e gestisce sicurezza, traffico e altre cose importanti. Uno switch è invece pensato per **trasmettere del traffico nella maniera più veloce possibile senza alcuna analisi dello stesso**. Principalmente vengono usati quando la mia rete ha più porte di quelle che può gestire il mio router.

## 4.Dispositivi gigabit

Gli switch e router più moderni sono detti *gigabit switch* e *gigabit router* in quanto supportano il protocollo di comunicazione **gigabit ethernet**. Questo protocollo (`IEEE 802.3z` su fibra e `IEEE 802.3ab` su rame) è l’evoluzione a *1000 Mbit/s* del protocollo Fast Ethernet (standard `IEEE 802.3u`) operante a *100 Mbit/s*. Uno *switch gigabit* è usato spesso in tandem con uno *gigabit router* per poter permettere alla mia rete locale di raggiungere le velocità offerte dal protocollo. Se uno dei componenti che compongono la mia rete non fosse gigabit, allora l’intera rete sarebbe limitata di 10/100 volte in velocità (collo di bottiglia). Conseguentemente è necessario che tutti i componenti siano “*gigabit*”, compresi i computer. **N.B.**: queste velocità **non** sono le velocità di accesso a internet, ma le velocità di connessione tra i computer presenti nella mia rete locale (trasferimento dati).