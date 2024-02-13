---
tags:
  - DataScience
---
Tipicamente individuiamo i valori mancanti in termini di spazi vuoti nella tabella dei dati oppure come stringhe segnaposto, per esempio valori NaN (Not A Number). 

## Eliminazione

Uno dei modi più semplici per gestire il problema dei valori mancanti consiste nell’eliminare completamente dal dataset le caratteristiche (colonne) o i campioni (righe) corrispondenti; le righe con valori mancanti possono essere eliminate con facilità tramite il metodo `dropna`.
Possiamo eliminare le colonne che hanno almeno un valore NaN in una riga, impostando l’argomento `axis` a 1: `df.dropna(axis=1)`.
Il problema di questo approccio che rischia di rimuovere fin troppi campioni, il che potrebbe pregiudicare del tutto l’affidabilità.
Oppure, se rimuoviamo troppe colonne di caratteristiche, corriamo il rischio di perdere informazioni preziose, delle quali il nostro classificatore ha bisogno per poter discriminare le classi.

## Interpolazione

Spesso, la rimozione dei campioni o l’eliminazione di intere colonne di caratteristiche non è una via percorribile, perché potremmo perdere troppi dati preziosi. In questo caso, possiamo utilizzare varie tecniche di interpolazione per stimare i valori mancanti sulla base degli altri campioni del dataset.
Una delle tecniche di interpolazione più comuni è l’imputazione media, mediante la quale sostituiamo semplicemente il valore mancante con il valore medio dell’intera colonna di caratteri della caratteristica.