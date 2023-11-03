---
tags:
  - Finance
---


Utilizzare un investimento già esistente in un determinato asset come collaterale (dare questo strumento ad un intermediario finanziario che lo tiene come garanzia) per ricevere dei soldi in prestito con il quale comprare lo stesso asset.
In questo modo sono esposto all'investimento con una cifra maggiore rispetto a quella che effettivamente ho amplificando quindi sia le perdite che i guadagni.
Il problema di questo approccio è la [[Liquidazione del collaterale (margin call)]] che avviene in caso di notevoli drowdown dell'asset.
Se veniamo liquidati i nostri soldi sono venduti al minimo portando quindi a delle perdite secche.

## Loan to Value (LTV)

Indica la percentuale del prestito rispetto al valore del collaterale in un determinato momento. In base alla volatilità del collaterale posso avere un valore dal 50% (collaterale molto volatile, es btc) all'80% (collaterale poco volatile, es una casa).
Dato che questo valore cambia nel tempo al variare del valore del sottostante, viene definito un suo valore massimo che, se superato, porta alla liquidazione del capitale. Per esempio se ho un LTV del 50% significa che se ad un determinato momento il valore del collaterale è il 53% del prestito, il 3% viene venduto in modo da stare sempre al 50% ripagando un po' il debito.
Alcuni intermediari liquidano anche aggiungendo una penalità.
Nel caso dell'apertura di un [[Mutuo]] l'LTV identifica la percentuale di finanziabilità concessa dalla banca. Un basso LTV può garantire uno sconto sul tasso (in genere lo sconto è a scaglioni (<50%,<70%,<80%). Di norma la quota massima finanziata sui mutui è 80% ma si possono ottenere deroghe. Più è alto il loan to value e più il rischio della banca si eleva.
E’ chiaro che chi acquista una casa con LTV 100% non rischia nulla di proprio e quindi viene penalizzato sulle condizioni applicate. In questo caso la casa la sta comprando la banca a suo rischio e pericolo. Il rischio è che, se il valore dell'immobile scende sotto la soglia dell'importo del mutuo concesso, il mutuatario può essere tentato dal non pagare più e lasciare la banca al suo destino. E purtroppo dopo il 2008, il crollo del valore degli immobili ha portato molti casi del genere.

## Esempio
Se metto come collaterale 10k€ in BTC l'intermediario offre un LTV del 50% quindi mi da in prestito 5k€. Se BTC perde il 50% di valore l'intermediario ha 5k€ di valore effettivo a fronte di 5k€ di prestito.
Il prestito non è sufficientemente coperto, il collaterale viene immediatamente venduto estinguendo il prestito.
Paolo Coletti ha creato uno spreadsheet che ho commentato qui: https://docs.google.com/spreadsheets/u/0/d/18RFdHFEuAQFkMmozOIP-j3eKEYgrCfZ3

