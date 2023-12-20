---
tags:
  - Tutorial
  - Windows
---


Questo metodo è utile per effettuare l'unmount di un disco forzatamente, utilizza l'utility `diskpart`.

```powershell 
diskpart
list disk
select disk 1
list volume
select volume 2
remove
```