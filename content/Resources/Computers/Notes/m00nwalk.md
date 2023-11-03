---
tags:
  - Forensics
  - PicoCTF2019
---


## Problema

Decode [this](https://2019shell1.picoctf.com/static/76eac1f05b962c507fc0a3c81306de26/message.wav) message from the moon. You can also find the file in /problems/m00nwalk_3_03dab5f4d1deab675e80ee603fb02236.

## Soluzione

Dall'indizio e dal nome del programma vedo che si tratta di come venivano spedite le immagini durante il viaggio sulla Luna.
Approfondendo scopro che le immagini venivano inviate come file audio .wav con una tecnologia chiamata SSTV (Slow-Scan Television); basta quindi trovare un programma che sappia decodificarlo opportunamente.
Per approfondire consiglio: [stenografia audio](https://medium.com/@sumit.arora/audio-steganography-the-art-of-hiding-secrets-within-earshot-part-2-of-2-c76b1be719b3).
Per decodificare esiste un software chiamato qsstv, una volta installato (solo ubuntu purtroppo) ottengo una immagine dove vi è scritta la chiave:
```
picoCTF{beep-boop-im-in-space}
```
