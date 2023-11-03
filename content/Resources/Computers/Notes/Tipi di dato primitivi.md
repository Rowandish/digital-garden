---
tags:
  - Coding
  - CSharp
  - Basics
---


Un tipo di dato primitivo è un costrutto fondamentale nei linguaggi di programmazione che rappresenta una quantità di memoria allocata e specifica il formato dei dati contenuti in quella memoria.
I tipi di dato primitivi di solito riflettono i tipi di dati di base supportati dal processore dell'architettura su cui il linguaggio di programmazione viene eseguito.
Ogni tipo di dato primitivo ha un'allocazione di memoria fissa e una gamma di valori consentiti.

## Tipi di Dato Primitivi in C#

C# fornisce un set di tipi di dato primitivi ben definiti, che coprono una vasta gamma di necessità di programmazione.
Di seguito, una tabella Markdown che elenca alcuni dei tipi di dato primitivi più comuni in C# e il numero di bit che li compongono:

| Tipo di Dato | Numero di Bit |
|--------------|--------------|
| bool         | 1 bit        |
| byte         | 8 bit        |
| sbyte        | 8 bit        |
| char         | 16 bit       |
| short        | 16 bit       |
| ushort       | 16 bit       |
| int          | 32 bit       |
| uint         | 32 bit       |
| long         | 64 bit       |
| ulong        | 64 bit       |
| float        | 32 bit       |
| double       | 64 bit       |
| decimal      | 128 bit      |

## Descrizione dei Tipi di Dato Primitivi

1. **bool**: Il tipo di dato bool rappresenta un valore booleano che può essere vero (true) o falso (false). È il tipo più semplice e richiede solo 1 bit di memoria.
2. **byte**: Il tipo di dato byte rappresenta un intero a 8 bit senza segno, consentendo valori compresi tra 0 e 255.
3. **sbyte**: Il tipo di dato sbyte rappresenta un intero a 8 bit con segno, coprendo un intervallo di valori da -128 a 127.
4. **char**: Il tipo di dato char rappresenta un singolo carattere Unicode a 16 bit, come ad esempio lettere, numeri o simboli.
5. **short**: Il tipo di dato short, anche noto come int16, è un intero a 16 bit con segno. La sua gamma di valori va da -32,768 a 32,767.
6. **ushort**: Il tipo di dato ushort, anche noto come uint16, è un intero a 16 bit senza segno, consentendo valori compresi tra 0 e 65,535.
7. **int**: Il tipo di dato int, anche noto come int32, è un intero a 32 bit con segno, che copre una vasta gamma di valori da -2.147.483.648 a 2.147.483.647.
8. **uint**: Il tipo di dato uint, anche noto come uint32, è un intero a 32 bit senza segno, con una gamma di valori da 0 a circa 4 miliardi.
9. **long**: Il tipo di dato long, anche noto come int64, è un intero a 64 bit con segno, consentendo valori estesi da -9 quintilioni a 9 quintilioni.
10. **ulong**: Il tipo di dato ulong, anche noto come uint64, è un intero a 64 bit senza segno, con una gamma di valori da 0 a circa 18 quintilioni.
11. **float**: Il tipo di dato float rappresenta un numero a virgola mobile a precisione singola a 32 bit. È ideale per calcoli che richiedono precisione limitata.
12. **double**: Il tipo di dato double rappresenta un numero a virgola mobile a precisione doppia a 64 bit, che offre una maggiore precisione rispetto al float.
13. **decimal**: Il tipo di dato decimal rappresenta un numero a virgola mobile a precisione estesa a 128 bit, ideale per calcoli finanziari e altre situazioni in cui la precisione è essenziale.