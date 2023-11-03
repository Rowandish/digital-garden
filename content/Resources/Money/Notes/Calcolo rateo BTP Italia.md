---
tags:
  - Bond
  - Finance
---


Documento: https://www.dt.mef.gov.it/it/debito_pubblico/dati_statistici/coefficienti_di_indicizzazione_btp_italia/esempi_calcolo/

## 📺 Video
<div class="iframe-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/rQbxKgsAIHY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Calcolo della cedola

Il BTP Italia funziona fornendo un "cedolone" in quanto in ogni cedola incorpora sia la cedola base che la parte di rivaluzazione del capitale.

Per prima cosa è necessario sapere di quanto è variato l’indice dei prezzi giornaliero di riferimento (indice Foi) **rispetto allo stacco cedola precedente**.
Dato che il BTP Italia ha stacco cedola semestrale il delta dell'indice Foi si guarda sempre con i 6 mesi precedenti.
Per esempio se durante lo scorso stacco cedola era 109,2 e ora è 114,66 ottengo il Coefficiente di Indicizzazione (CI) come il loro rapporto, quindi
$$CI=\frac{114,66}{109,2}=1,05$$
Questo valore lo utilizzo sia per il calcolo della nuova cedola $C$ che per al rivalutazione del capitale ($CR$).

### Diminuzione indice Foi
Può succedere anche che l'inflazione diventi negativa, quindi che l'indice Foi diminuisca, per esempio passa da 109,2 a 107,016.
$$CI=\frac{109,2}{107,016}=0,98$$
In questo caso il CI viene impostato forzatamente a 1 e non c'è alcuna rivalutazione del capitale.
Possiamo quindi definire la formula completa per il calcolo dell'$CI$ come:
$$CI=Max(\frac{Foi_{oggi}}{Foi_{oggi-6Mesi}},1)$$
C'è un ulteriore clausola: qualora nel semestre successivo l'inflazione torni ad essere positiva il governo si "ricorda" di quanto ha abbonato il semestre con inflazione negativa (doveva usare $0,98$ di $CI$ e invece ha usato 1) e lo scala dal calcolo del semestre successivo.
Per esempio se l'indice CI è 1,03 ma al semestre precedente avevo $0,98$ ottengo il vero indice CI come $1,03-(1-0,98)=1,01$ che poi per motivi di interesse composto è $1,00940$.

### Cedola
$$C=\frac{TassoCedolareMinimo}{2}*CapitaleSottoscritto*CI$$
Esempio assumendo la cedola minima 1,6% e un capitale di 1000€ ottengo
$$C=\frac{0,016}{2}*1000*1,05=8,40\unicode{x20AC}$$
### Capitale rivalutato

Il capitale rivalutato si calcola banalmente incrementando il capitale investito del coefficiente di indicizzazione:
$$CR=CapitaleSottoscritto*(CI-1)$$
Per esempio assumendo sempre di aver investito 1000€ ho
$$CR=1000*(1,05-1)=50\unicode{x20AC}$$

### Totale

La cedola complessiva è quindi $C+CR$, quindi nell'esempio sopra sarà 58,40€.

## Indice Foi
Per sapere quanto sono cresciuti i prezzi viene utilizzato l'indice Foi, il problema è che l'Istat ci mette qualche settimana per calcolarlo; viene infatti rilasciato ogni mese e riferito al mese precedente.
Come faccio però a calcolarlo qualora venda il BTP Italia oggi? Mi serve per sapere quale rateo rimborsare al proprietario precedente.
Questo valore teorico viene calcolato per interpolazione tra il Foi di 2 mesi prima e quello di 3 mesi prima.