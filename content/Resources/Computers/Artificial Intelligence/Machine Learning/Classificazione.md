---
tags:
  - MachineLearning
---
Un problema di classificazione è un tipo di problema nell'ambito del machine learning dove l'obiettivo è quello di ==assegnare un'etichetta o una classe a una determinata osservazione in base alle sue caratteristiche==. In altre parole, il compito consiste nel creare un modello che possa imparare a distinguere tra diverse categorie o classi.

Per esempio, immagina di avere un insieme di dati che contengono informazioni su vari tipi di frutta come mele, banane e arance. Ogni frutto ha diverse caratteristiche come colore, forma, dimensioni e peso. Un problema di classificazione consisterebbe nel creare un modello di machine learning che possa guardare queste caratteristiche e decidere a quale categoria appartiene ciascun frutto.

Quindi, il modello di classificazione potrebbe essere addestrato utilizzando i dati esistenti, con frutti già etichettati correttamente (ad esempio, mele etichettate come "mele", banane etichettate come "banane", ecc.).
Una volta addestrato, il modello può essere utilizzato per fare previsioni su nuovi frutti, assegnando loro un'etichetta o una classe in base alle caratteristiche che il modello ha imparato durante l'addestramento.

## Tipologie
* **Classificazione binaria**: l’algoritmo di apprendimento automatico impara un insieme di regole con lo scopo di distinguere fra due possibili classi;
* **Classificazione multiclasse**: l’insieme delle etichette delle classi non deve necessariamente avere una natura binaria ma multidimensionale.

## Algoritmi

^84ab24

La scelta di un algoritmo di classificazione appropriato per risolvere un determinato problema richiede pratica: nessuno dei classificatori opera al meglio in tutte le situazioni possibili.
### Machine Learning

Nel machine learning tradizionale, si utilizzano algoritmi più semplici e classici come
* [[Regressione logistica]]: il più semplice e classico
* [[Support Vector Machines (SVM)]]
* [[Decision tree]]
* [[Random Forests]]
* Naive Bayes

Questi algoritmi si basano su regole matematiche e statistiche per separare i dati in diverse categorie in base alle loro caratteristiche. Sono spesso utilizzati quando si ha un numero limitato di dati e quando le relazioni tra le caratteristiche e le etichette di classificazione sono relativamente semplici.
Ecco alcuni esempi di algoritmi di machine learning.
```python
clf1 = GradientBoostingClassifier()
clf2 = RandomForestClassifier(class_weight='balanced')
clf3 = LGBMClassifier(class_weight='balanced')
clf4 = XGBClassifier()
```
Tipicamente non si usa solo un classificatore ma, per lo stesso problema, si provano vari classificatori al fine di capire quello che funziona meglio.
Esistono anche tecniche di [[Ensemble Learning|ensambling]] per combinare diversi classificatori e metterli insieme tramite votazione.