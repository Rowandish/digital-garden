---
tags:
  - Forensics
  - PicoCTF2019
---
## Problema

I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!

![[whitepages.txt]]

## Soluzione

Aprendo il file con HxD ottengo una file con vari elementi ripetuti.
Ad una attenta analisi ottengo che i valori che si ripetono sono:
`E2 80 83` e `20`.
Questo si nota andando verso la metà del file dove ho il valore 20 ripetuto n volte.
Quindi ho blocchi di coppie di valori, come regex possiamo scrivere: `[E2 80 83]*[20]*`.
Coppie di valori mi fanno pensare a valori binari, quindi provo con sublime text a sostituire `E2 80 83` con `0` e `20` con `1`.
Ottengo un numero booleano enorme che convertito in stringa con [questo](https://www.convertbinary.com/to-text/) mi fa ottenere la chiave:
`picoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}`
 
