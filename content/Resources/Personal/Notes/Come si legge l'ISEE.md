---
tags:
  - INPS
---


L'ISEE è un valore che è il rapporto tra l'indicatore della situazione economica (ISE) con la scala di equivalenza (SE).
Il primo indica, come dice il termine, la situazione economica **del nucleo famigliare** mentre il secondo indica di quanto devo ridurre tale valore in base al numero di componenti di tale nucleo.

## Indicatore situazione economica

L’ISE viene calcolato sommando l'ISR con il 20% dell'ISP, ho quindi una forte predominanza della situazione reddituale odierna rispetto al patrimonio che conta solo per un quinto.
$$ I_{ndicatore}S_{ituazione}E_{conomica}= I_{ndicatore}S_{ituazione}R_{edittuale} + 0,2*I_{ndicazione}S_{ituazione}P_{atrimoniale} $$

### ISR
L' ISR (indicatore situazione reddituale) è la somma tra
* Somma dei redditi dei componenti del nucleo (RC)
* il rendimento del patrimonio mobiliare (RPM)
* detrazioni del canone annuo di locazione o altre spese (DC).

### ISP
L'ISP (indicatore situazione patrimoniale) è la somma del patrimonio immobiliare più il patrimonio mobiliare sottratto di una costante pari a 15493,71. A questi valori vanno eventualmente sottratte delle detrazioni se aventi diritto.

$$I_{ndicazione}S_{ituazione}P_{atrimoniale}=P_{atrimonio}I_{mmobiliare}+(P_{atrimonio}M_{obiliare}-15493,71)$$

### Patrimonio mobiliare del nucleo
Questo valore è la somma diretta dei valori presenti nei conti correnti più gli investimenti.
#### Conti correnti
Nel quadro FC2 sez.1 ho le giacenze medie al 31/12 e la giacenza media dei vari conti.
Viene effettuata la somma A e B; se se la differenza (A-B) è positiva, l’ISEE è calcolato sul saldo; se negativa, sulla giacenza media.
#### Investimenti
Nel quadro FC2 sez.2 vengono indicati le altre forme di patrimonio mobiliare che non è un conto corrente (libretti postali, fondi di investimento, azioni…).
Quindi non ho saldo e giacenza media ma solo il "saldo" al 31/12 che sarà quello che andrò a sommare.
La somma di questi valori per tutti i componenti del nucleo famigliare formerà il valore del patrimonio mobiliare del nucleo.

#### Detrazione patrimonio immobiliare
In questa cella viene sottratto il valore dell'immobile (calcolato come ?) qualora tale immobile coincida con la casa di abitazione corrente (quadro B).
Quindi se oggi vivo nella casa che dichiaro nel quadro FC3 (riferito a 2 anni prima), tale valore verrà detratto con un qualche parametro ancora non chiaro.



## Scala di equivalenza

La scala di equivalenza (SE) è il valore con cui dividere l'ISE per ottenere l'ISEE; questo valore dipende dal numero di componenti nel nucleo famigliare.
| Numero di componenti | Parametro |
| -------------------- | --------- |
| 1                    | 1         |
| 2                    | 1,57      |
| 3                    | 2,04      |
| 4                    | 2,46      |
| 5                    | 2,85      |

A questo valore va sommato 0,2 se ci sono tre figli minorenni, 0,35 se quattro e 0,5 per cinque.
Inoltre si aggiunge 0,2 se ci sono dei figli minorenni nel nucleo famigliare che diventa 0,3 se c'è almeno un figlio con meno di 3 anni e entrambi i genitori hanno lavorato almeno 6 mesi nell'anno di riferimento dell'ISEE.

L'ISEE è quindi:
$$ISEE = \frac{ISE}{SE}$$