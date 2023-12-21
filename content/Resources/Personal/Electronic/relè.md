---
tags:
  - Electronics
  - Component
---
Il relè è un dispositivo elettrico **comandato dalle variazioni di corrente per influenzare le condizioni di un altro circuito**. In sostanza, il relè è un deviatore che non viene azionato a mano, ma da un elettromagnete. **Tipicamente un relay è formato da 4 pin, due appartengono ad un circuito e due ad un secondo circuito**. Se vi è una differenza di potenziale tra i due pin in alto (24V uno e il meno l’altro) il relay chiude (o apre, nel caso di circuiti normalmente chiusi) il circuito opposto. Due tipologie principali: **elettromeccanico** (vecchio, economico ma con rimbalzo) e **stato solido** (moderno, costoso ma senza rimbalzi).

Questo può essere utile in due situazioni principalmente:

1. Voglio **comandare un circuito a diverso voltaggio**: ho una telecamera (per esempio le lineari) che funziona a 5V, ma il mio alimentatore è a 24V. Alimento la telecamera con un alimentatore da 5V e chiudo o meno il circuito dello stesso (quindi faccio scattare) grazie ad un relay. La potenza alla telecamera è data dall’UPS, in quanto questa è sempre accesa. In questo caso voglio trasferire informazione alla telecamera (comando “scatta”) ma non potenza.
2. **Per alimentare in potenza** da un dispositivo che non ne ha: per esempio il PC ha pochissima corrente (potenza) che può inviare, tipicamente invia informazioni. Se io collego le uscite del PC ad un relay, posso chiudere il circuito di alimentazione degli illuminatori (che invece richiedono molta corrente) e conseguentemente accenderli.

Spesso hanno più di 4 morsetti: con utilizzi più avanzati posso decidere, in base a come collego le cose, se l’interruttore è normalmente aperto o chiuso.

## Immagine

![[IMG_6372_1_.jpg]]

## Contatto pulito

Assumiamo di dover mettere in comunicazione un PC con un PLC: ho l’uscita x del PC che deve essere messo in collegamento con l’ingresso y del PLC. Invece di collegare direttamente i cavi voglio rendere indipendenti i due sistemi, a livello di alimentazione: se io butto 100V, a me arrivano i miei V e non mi brucio. Contatto pulito significa tu dammi il segnale (informazione), poi ci penso io a alimentarmi per gestire questa informazione. Per ottenere questo utilizzo i relè. In questo modo i due circuiti sono optoisolati (l’informazione viene inviata tramite luce e non tramite collegamento fisico).

### Esempio - Trigger PLC - PC

Una applicazione dei relè è fornire un trigger elettrico da PLC agli ingressi del mio PC. Ora, non posso mandare direttamente il segnale dal PLC al mio PC in quanto altrimenti non avrei contatti puliti, i 24V del PLC non sono i 24V miei. Prendiamo lo schema di un relè Phoenix come indicato dalla figura seguente:

![[Esempio_rele_per_wiki.png]]

Questo ha un ingresso A2 per il GND esterno e un ingresso A1 per il trigger esterno, quindi il 24V del PLC. Se eccitato questo chiude il circuito 13+/14 in cui all’ingresso 13+ andò a mettere il 24V del PC e collegherò l’uscita 14 ad un ingresso digitale del PC.