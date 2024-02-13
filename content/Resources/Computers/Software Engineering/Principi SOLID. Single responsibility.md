---
tags:
  - Coding
  - SOLID
  - PublishedPosts
---

L'open-closed principle è il primo principio di SOLID.

La mia idea è scrivere un articolo per ognuno dei 5 principi, iniziamo oggi con il primo, il principio di Single responsibility.

## Definizione

Il principio di single responsibility afferma che "**una classe deve avere uno e uno solo motivo per cambiare**" o anche "**una classe deve essere responsabile di un unico attore**". Genericamente una classe dovrebbe avere una sola responsabilità completamente incapsulata al suo interno, dedicarsi esclusivamente a quella e conseguentemente cambiare solo se tale responsabilità cambia e per nessun altro motivo.

Inoltre una classe dovrebbe rispondere ad un solo "attore" e per attore si intende una entità astratta che ha delle necessità all'interno del mio software.

## Perché implementarlo

Come insegna uncle Bob, i requisiti di un software continuano a cambiare nel tempo; conseguentemente devono essere modificare le responsabilità di almeno una classe. Maggiori sono le responsabilità della classe in questione più spesso vi sarà il bisogno di cambiarla.

Il problema è che se una classe ha più di una responsabilità, la modifica di parte del codice di una si riflette automaticamente sull'altra, in quanto appartenente alla stessa classe.

Per esempio se la classe fa X e Y e per modificare X devo, per esempio, aggiungere un parametro al costruttore della classe, questa modifica porterà anche a dei cambiamenti sulle classi che la utilizzano per la responsabilità Y che non centra nulla con X.

Più una classe ha responsabilità più spesso dovrà essere modificata e di riflesso verranno modificate le classi che dipendono da questa ultima, quindi tutte le sue dipendenze.

Queste dovranno essere ricompilate e subiranno delle modifiche anche se non centrano nulla con la responsabilità che è effettivamente cambiata.

Per evitare tutti questi problemi è indispensabile che ogni classe abbia una e una sola responsabilità e, come dice uncle Bob, **uno e un solo motivo per cambiare**.

## Non esagerare

Alcuni programmatori prendono il principio all'estremo e arrivano al punto di implementare classi con una sola funzione. Questo ovviamente porta ad una proliferazione di classi che porta solo confusione all'interno del codice.

Il principio di singola responsabilità deve essere usato con criterio secondo la propria esperienza.


## Come capire se una classe viola il SRP
Ci sono varie euristiche per capire se una classe viola il SRP:
* Il nome della classe contiene parole come `Manager` o `Processor` o comunque nomi che indicano che tale classe gestisce varie cose;
* Non è semplice definire il nome della classe stessa (che dovrebbe invece descrivere l'unica responsabilità della classe) o il nome che vorremmo dare contiene `and`;
* Presenta dei metodi privati che si applicano solo ad un piccolo sottoinsieme di metodi della classe;
* La classe non è [[Clean Code#^b19092|coesa]];

## Esempio

Assumiamo di avere una classe "Dipendente" con tre metodi:

- `CalcolaPaga`: fornisce la paga da dare al dipendente
- `ReportHours`: indica il numero di ore lavorate
- `Save`: Salva i dati del dipendente sul database

Questi tre metodi sono responsabili di tre attori differenti: il primo metodo viene usato dal settore contabilità, il secondo dal settore risorse umane e il terzo al direttore tecnico.

Avendo i tre metodi nella stessa classe che dipendono da attori diversi può capitare che una modifica delle esigenze dell'uno si rifletta, senza volerlo, anche sugli altri due.

Per esempio qualora il metodo `ReportHours` e `CalcolaPaga` utilizzino lo stesso metodo sottostante per calcolare il numero di ore lavorate, una modifica a questo metodo richiesta dall'ufficio paghe porta, di riflesso, ad una modifica non richiesta al metodo `ReportHours` gestito dall'ufficio risorse umane.

La soluzione è porre ogni metodo in una sua classe dedicata e la classe Dipendente conterrà solo le interfacce di queste classi, senza quindi alcuna riga di codice al suo interno. Il calcolo delle ore lavorate sarà quindi completamente scorporato
