---
tags:
  - Devices
  - Electronics
---


## 1. Introduzione

![[Senza_titolo-1.jpg]]

![[photo_2022-07-21_13-32-01.jpg]]

### 1.1 Le porte in basso

Tipicamente un tester ha in basso 3 porte: * **COM**: sta per Common e si usa per connettere il “-” o il GND di un circuito. Convenzionalmente il ground è associato al nero. * **10A**: è una porta speciale che si utilizza per misurare grandi correnti (maggiori di 200mA. * **mAVΩ**: è la porta dove convenzionalmente è cablato il puntalino rosso e serve per misurare i "+* di un circuito. La porta permette di misurare la corrente (fino a 200mA), voltaggio (V) e resistenza (Ω).

## 2. Funzionalità

### 2.1 Misurare il voltaggio

Il 99.9% delle volte in cui si usa un tester è per sapere la differenza di potenziale (voltaggio) tra due punti di un circuito in un determinato momento. Per fare questo per prima cosa è necessario impostare il tester nell’icona della corrente continua (DC), cioè quella indicata sopra. Alcuni tester hanno una unica modalità per DC e AC, per cambiare da una all’altra è necessario premere un pulsante (tipicamente SEL) in modo che sullo schermo compaia DC. L’immagine seguente è un esempio analogo.

![[image 3.png]]

Una volta fatto questo mettere il puntalino nero nel - e il rosso nel + e leggere il voltaggio.

### 2.2 Conoscere il valore di una resistenza

Le resistenze normali hanno un codice colore che indica il loro valore (esistono calcolatori online per ottenere tale informazione). Qualora comunque servisse i tester possono calcolare anche il valore di una resistenza, impostando la loro modalità a “Ω”.

### 2.3 Misurare una corrente

Questa è una misura particolarmente complessa in un circuito in quanto bisogna mettere il tester in serie. Se serve approfondire a parte.

### 2.4 Continuità

La continuità è tecnicamente il test per sapere la resistenza che vi è tra due punti. Se la resistenza è particolarmente bassa significa che i due punti sono connessi elettricamente e verrà emesso un suono. Questo test serve per verificare che due punti siano correttamente connessi elettricamente, o, genericamente, se due punti appartengano allo stesso filo.

## How-to

### Conoscere connessione cablatura pin

Per fare questo test è necessario misurare la **continuità** tra i due fili. Dato un cavo in cui da un lato ho dei pin e dall’altro dei fili spaiati, il mio obiettivo è conoscere a quale pin corrisponde quale filo. Per far ciò prendere il tester, impostarlo in modalità suono (quarto scatto dalla sinistra e pressione di FUNC) connettere da un lato un puntale a uno dei pin, dall’altro il puntale con i vari fili. Quando il tester suona significa che il filo e il pin sono connessi con lo stesso cavo.

### Conoscere se un morsetto è connesso a terra

Per fare questo test è necessario misurare la **continuità** tra i due il punto in questione e la terra. Spesso può capitare di dover individuare un morsetto connesso direttamente a terra, o, in generale, un morsetto che ha lo stesso potenziale **non alimentato** di un altro. Per fare ciò impostare il tester in modalità suono e connettere il puntale nero a terra (o dove ho il - di riferimento) e il puntale rosso nel morsetto. Se suona significa che sono allo stesso potenziale.

**ATTENZIONE**: questo procedimento funziona **solo** se i morsetti non sono alimentati, altrimenti faccio un corto. Quindi **prima** di testare se il morsetto X è connesso a terra è necessario verificare che **non** sia alimentato, quindi con il tester in modalità corrente continua, verificare che il voltaggio sia tendente a 0 e poi testare in modalità suono.