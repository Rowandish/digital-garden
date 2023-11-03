---
tags:
  - Forensics
  - PicoCTF2019
---


## Problema
We found this file. Recover the flag. You can also find the file in /problems/c0rrupt_0_1fcad1344c25a122a00721e4af86de13.

## Soluzione

Per prima cosa devo aprire il file con un hex editor, per esempio HxD per Windows.
Ora guardo l'header e il footer e capisco che, a meno di qualche carattere errato, è un file png.
Modifico l'header con
```
89 50 4E 47 0D 0A 1A 0A
```
e ottengo quindi un file png corretto ma che comunque non si apre.

## Funzionamento file PNG

Studiando la struttura dei file png scopro che questi sono divisi nei seguenti chunk:

| Nome | Significato |
|--------|--------|
|IHDR|Contiene le informazioni sul file, come With, Height...|
|sRGB|Se presente, utilizza lo spazio dei colori RGB|
|gAMA||
|pHYs||
|IDAT|Contiene tutti i dati dell'immagine|
|IEND|Chunk terminatore, è sempre uguale a `00 00 00 00 49 45 4E 44 AE 42 60 82`|

Ogni chunk è definito come segue:
- 4 byte che ne indicano la lunghezza
- 4 byte che ne indicano il tipo
- n byte (con n definito dai primi 4 byte) con il valore
- 4 byte di controllo CRC

![[image 11.png]]

Il file in questione è stato corrotto in vari chunk e in alcuni CRC, per risolvere il problema utilizzare il tool [pngcheck](http://www.libpng.org/pub/png/apps/pngcheck.html) che fornisce un po' di debugging comodo.

## Fix corruzione file
Una volta fixato l'header del file lanciando pngcheck ottengo:
```
chunk pHYs at offset 0x00042, length 9: 2852132389x5669 pixels/meter
CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
```
Anche se mi dice che è un errore di CRC, il problema è invece che il chunk pHYs fornisce un valore (`2852132389x5669 pixels/meter`) assurdo, per risolvere prendere un hex di un altro PNG valido e sostituirlo al content del chunk `pHYs`. Ora rilanciando il pngcheck ottengo errore di CRC, come è giusto che sia:
```
chunk pHYs at offset 0x00042, length 9: 3779x3779 pixels/meter (96 dpi)
CRC error in chunk pHYs (computed c76fa864, expected 495224f0)
```
Sostituisco quindi `495224f0` con `c76fa864`.
Ora vi è la parte più complicata: pngcheck fornisce un errore di
```
invalid chunk length (too large)
```
che mi dice poco.
Andando a vedere i chunk mi aspetto di avere ora il chunk `IDAT` contenente tutti i dati, preceduto da 4 byte che ne indicano la lunghezza.
Quello che ho sono 4 byte casuali (dove vi è una lunghezza del chunk esagerata) con 4 byte con `IDAT` corrotto. Sistemando questi in modo che vi sia scritto `IDAT` mi serve sapere la lunghezza di tale chunk.
Con `HxD` seleziono tutti i byte fino in fondo al file (tranne gli ultimi 11 byte, 4 di CRC, 4 di lenght di `IEND` e 4 per `IEND` e il footer finale) e ottengo come lunghezza il valore `31851`.
Ora l'ultimo passo e inserire tale valore nei primi 4 byte del chunk IDAT per poter quindi fixare completamente il file:
```
00 03 18 51
```
* Mystery corrotto*: ![[mystery]]
* Mystery fixato*: ![[mystery.png]]


## CheatSheet

* https://digital-forensics.sans.org/media/hex_file_and_regex_cheat_sheet.pdf
* https://parsiya.net/blog/2018-02-25-extracting-png-chunks-with-go/


