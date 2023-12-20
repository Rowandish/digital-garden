---
tags:
  - Electronics
  - Devices
---
## 1. Introduzione

L’oscilloscopio è un dispositivo che permette di visualizzare come sono fatte realmente le forme d’onda, esso effettua la presentazione sullo schermo dell’andamento **nel tempo (asse X orizzontale)** di una **tensione elettrica (asse Y verticale)**. L’oscilloscopio può essere utile per ottenere:

- La forma del segnale;
- la tensione massima e minima;
- Il periodo della forma d’onda;
- La presenza di eventuali distorsioni;
- La presenza di disturbi e rumore sul segnale
- La componente continua e alternata del segnale

## 2. Comandi comuni

| Comando | Scopo |
|--------|--------|
|`BRIGHT (LUMINOSITA')`| Regola la luminosita' delle tracce.|
|`FOCUS (FUOCO)`| Mette a fuoco le tracce sul display.|
|`GRAT (GRIGLIA)`| Illumina la griglia del display.|
|`TRACE (TRACCIA)`| Seleziona la traccia da visualizzare.|
|`TRIGGER LEVEL (LIVELLO DI TRIGGER)`| Seleziona il livello del trigger.|
|`TRIGGER SOURCE (SORGENTE DEL TRIGGER)`| Seleziona la sorgente del trigger.|
|`TRIGGER MODE (MODO DEL TRIGGER)`| Seleziona come effettuare il trigger.|
|`SLOPE (PENDENZA)`| Seleziona il fronte sul quale effettuare il trigger.|
|`TIMEBASE (BASE TEMPORALE)`| Seleziona la velocita' della scansione orizzontale.|
|`INPUT LEVEL (LIVELLO D'INGRESSO)`| Regola il livello d'ingresso.|
|`VERTICAL POSITION (POSIZIONE VERTICALE)`| Regola la posizione verticale della traccia sul display.|
|`ORIZZONTAL POSITION (POSIZIONE ORIZZONTALE)`|Regola la posizione della orizzontale della traccia sul display.|

### 2.1. BRIGHT (LUMINOSITA’)

Esso regola l’intensita’ luminosa della traccia del display.

### 2.2. FOCUS (FUOCO)

Mette a fuoco le tracce sul display.

### 2.3. GRAT (GRIGLIA)

Questo controllo regola la luminosita’ della luce usata per illuminare la scala dell’Oscilloscopio. Con l’uso di questa scala graduata, e’ possibile misurare l’ampiezza dell’onda sull’asse verticale, e il periodo su quello orizzontale. Quando la manopola e’ regolata al minimo la griglia diventa invisibile.

### 2.4. TRACE (TRACCIA)

Seleziona quale traccia visualizzare. Ci sono di norma due o piu’ possibili opzioni:

- **A** - Visualizza solo la traccia A (canale singolo);
- **B** - Visualizza solo la traccia B (canale singolo);
- **A+B** - Visualizza ambedue le tracce (canale doppio);
- **ADD** - I due canali sono sommati e visualizzati come una singola traccia. Il secondo canale puo’ anche essere invertito. In questo modo e’ possibile visualizzare sia i segnali di modo comune che di modo differenziale;
- **ALT** - Modo ALTERNATE: viene visualizzata alternativamente una scansione la traccia A e l’altra scansione la traccia B. Tale modo e’ utile per visualizzare segnali a frequenza elevata;
- **CHOP** - Modo CHOPPED: nella medesima scansione viene visualizzata un pezzetto di traccia A e un pezzetto di traccia B velocemente e alternativamente. Tale modo e’ utile per visualizzare segnali a bassa frequenza.

Esempio di **ADD** Mode:

![[image 2.png]]

Esempio di **ALT** Mode:

![[image2 1.png]]

Esempio di **CHOP** Mode:

![[image3 1.png]]

### 2.5. TRIGGER LEVEL (LIVELLO DI TRIGGER)

Una traccia che visualizza una forma d’onda senza essere triggerata (sincronizzata) apparira’ come lo schermo di un televisore che non ha il sincronismo orizzontale regolato correttamente (Vedi figura sottostante). Il trigger blocca la scansione orizzontale fino all’inizio della traccia . Cio’ fa si che ogni scansione orizzontale inizia sempre nel medesimo punto dell’onda periodica e la fara’ apparire stabile sul display. La manopola del livello di trigger e’ usata per selezionare il punto della forma d’onda dal quale inizia la scansione orizzontale.

![[image4 1.png]]

### 2.6. TRIGGER SOURCE (SORGENTE DEL TRIGGER)

Seleziona la sorgente del trigger. La maggior parte degli oscilloscopi possono essere triggerati sia sul canale A che sul canale B. Molti oscilloscopi possono ricevere il trigger da una sorgente esterna, in questo caso e’ previsto un ingresso di TRIGGER addizionale sul pannello frontale.

### 2.7. TRIGGER MODE (MODO DEL TRIGGER)

Il modo di trigger ha due posizioni: **AUTO** e **NORM**. Nella posizione **AUTO** la scansione della traccia parte automaticamente anche se la forma d’onda non e’ presente. Nella posizione **NORM** la scansione parte soltanto quando la forma d’onda e’ perfettamente triggerata.

### 2.8. SLOPE (PENDENZA)

Il selettore SLOPE seleziona su quale fronte (di salita o di discesa) triggerare la forma d’onda. La figura sottostante mostra l’uso della funzione SLOPE.

### 2.9. TIMEBASE (BASE TEMPORALE)

La velocita’ del punto luminoso sull’asse orizzontale puo’ essere regolata con il selettore TIMEBASE. Questo ha la scala calibrata in secondi (S/Div), millisecondi (mS/Div), microsecondi (uS/Div) per divisione.

### 2.10. INPUT LEVEL (LIVELLO D’INGRESSO)

Il selettore input level serve a regolare il livello d’ingresso di ciascun canale in maniera che possa entrare nello schermo. Il selettore e’ calibrato in Volts per divisione (V/Div).

### 2.11. VERTICAL POSITION (POSIZIONE VERTICALE)

Regola il livello in continua sull’asse verticale per una visualizzazione migliore. Qualora il segnale viene misurato in DC e dispone di una forte componente continua, esso sparira’ dallo schermo. Mediante tale controllo, e’ possibile riportare la traccia nell’area visibile compensando tale componente continua.

![[image5.png]]

![[image6.png]]

### 2.12. ORIZZONTAL POSITION (POSIZIONE ORIZZONTALE)

Sposta l’inizio della scansione sullo schermo muovendo la forma d’onda in direzione orizzontale.

## 3. OPERAZIONI DI BASE

Come esempio, collegate un filo elettrico all’ingresso A e toccate il conduttore centrale con le dita. Vedrete del rumore a 50 Hz della rete elettrica, captato dal vostro corpo che funzionera’ come un’antenna. Ora regolate la base tempi a 10mS/Div e regolate il livello d’ingresso del canale A. Dovreste vedere una forma d’onda simile a quella mostrata nella figura sottostante.

![[image7.png]]

Scegliere come sorgente di trigger il canale A. Regolare la manopola di TRIGGER lentamente avanti e indietro finche’ la forma d’onda non appare stabile sul display. Se il controllo di TRIGGER dispone della posizione AUTO, selezionatela e sara’ piu’ facile la regolazione del trigger. Se concentriamo ora la nostra attenzione sulla figura precedente e la usiamo come esempio, (e’ piu’ comodo della traccia dell’oscilloscopio), possiamo notare che i due picchi consecutivi dell’onda capitano proprio su due linee verticali rosse. Poiche’ la base tempi e’ stata fissata in 10 mS/Div, il punto luminoso impiega 20 mS per percorrere due divisioni. Il PERIODO della forma d’onda risulta pari a 20 mS (ovvero 0,02). La FREQUENZA sara’ pari a 1 diviso 0,02 = 50 Hz. Se guardiamo la scala verticale, la linea centrale corrisponde a 0 Volts e la traccia si muove di 1,8 divisioni sia sopra che sotto. Poiche’ il livello d’ingresso e’ settato a 1 Volt/div, il segnale d’ingresso avra’ un’escursione di 1,8 v+ 1,8 v = 3,6 volts PICCO-PICCO. Cio’ equivale a 3.6v per 0,35 = (circa) 1,2 volts RMS (efficaci), come quello che misurereste con un volmetro. In questa maniera, potete misurare con buona approssimazione la FREQUENZA e l’AMPIEZZA di una forma d’onda periodica.