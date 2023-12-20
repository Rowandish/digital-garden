---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


Nella programmazione ad oggetti spesso può crearsi il dubbio sulla differenza tra un'interfaccia e una classe astratta e sulle modalità per cui sia necessario utilizzare una a discapito dell'altra.  
Vediamo per prima cosa cosa sono entrambe per poi fare delle considerazioni sul loro utilizzo.

## 1. Interfacce

Un'interfaccia è un tipo di dato (paragonabile ad una classe) con le seguenti caratteristiche:

-   Risulta **composta solo da metodi astratti**;
-   ogni metodo dichiarato in un'interfaccia **deve essere implementato nella sottoclasse**;
-   **Non ha attributi** e quindi non può avere uno stato;
-   Permette l'ereditarietà multipla, in quanto una classe può essere **figlia di più interfacce**

Un'interfaccia può essere vista come punto di incontro tra componenti simili che hanno una struttura interna diversa.

## 2. Classi astratte

Citando Wikipedia, la classe astratta da sola non può essere istanziata, viene progettata soltanto per svolgere la funzione di **classe base** e da cui le classi derivate possono ereditare i metodi. Le caratteristiche “incomplete” della classe astratta vengono condivise da un gruppo di sotto-classi figlie, che vi aggiungono caratteristiche diverse, in modo da colmare le “lacune” della classe base astratta.  
Una classe astratta possiede le seguenti caratteristiche:

-   Non può essere istanziata;
-   Contiene almeno un metodo astratto;
-   Può avere attributi e quindi avere uno stato;
-   Una classe può essere figlia di una sola classe astratta.

Questo processo di astrazione ha lo scopo di **creare una struttura base** che semplifica il processo di sviluppo del software o che indirizza la programmazione delle classi figlie.  
Utilizzando una classe astratta è possibile inoltre definire delle implementazioni di default di metodi nel caso in cui i figli non le implementino.

## 3. Classe astratta o interfaccia?

Quando definiamo una classe astratta stiamo definendo le caratteristiche generiche di un oggetto (**cosa un oggetto è**), che saranno implementate genericamente dalle classi figlie. Nel caso invece di un'interfaccia definiamo **ciò che un oggetto può fare**, e siamo conseguentemente obbligati a definire, nella classe figlia, le implementazioni a questa capacità.  
Quindi un oggetto **è solo di un tipo** (può essere figlio di una sola classe astratta) ma **può avere tante abilità diverse** (può ereditare da diverse interfacce).  
Per esempio la classe `string` (in C#) ha la seguente dichiarazione:

Come si può notare le interfacce indicano **tutte le cose che questo oggetto può fare**, le capacità che deve implementare per poter essere definito **string**.

Usare una interfaccia quando voglio un contratto per chi implementa l'interfaccia sul comportamento che questo deve avere. Una interfaccia è un guscio vuoto, molto leggero a livello di CPU, che non può fare nulla, è solo un pattern.  
Le classi astratte sono effettivamente classi, possono sia definire dei comportamenti generici (metodi astratti) che un comportamento di default (metodi concreti).