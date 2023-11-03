---
tags:
  - Windows
  - Tutorial
---


Per prima cosa effettuiamo una panoramica dei tool che utilizzeremo.

## 1.1. Sysprep

`Sysprep`(*System Preparation*) consente di preparare un’installazione di Windows per la duplicazione, questo eseguibile si trova in _C:\\Windows\\System32\\sysprep_.

Opzioni importanti di sysprep:

|Opzione|Utilizzo|
|-----|-----|
|`/generalize `|Rimuove le informazioni univoche dal PC che voglio clonare in modo che l'immagine sia installabile su altri PC che non siano il PC da cui è stata clonata (quindi sempre il nostro caso).|
|`/oobe `|Fa partire il Windows Welcome al prossimo avvio (quindi chiede di creare un nuovo utente, nominare il PC e così via). Di default non lo vogliamo|
|`/shutdown`|Spegne il computer una volta che sysprep ha completato l'iter.|
|`/unattend:answerfile`|Applica le impostazioni salvate in un answer file (xml) a Windows.|

Il seguente comando è quanto è necessario sempre lanciare:

```powershell
sysprep /generalize /oobe /unattend:<percorso\_e\_nome\_file\_unattend>.xml
```

## 1.2. Diskpart

DiskPart, sostituendo il suo predecessore - fdisk è un'utilità di riga di comando che fornisce la possibilità di gestire dischi, partizioni o volumi nel computer.
In questo caso lo utilizziamo solo per vedere i dischi e i volumi che sono installati sul PC, sopratutto le lettere a cui questi sono associati.

L'utilizzo è semplice, per prima cosa lanciare l'eseguibile con il comando

```powershell
diskpart
```

Una volta lanciato digitare:

| Comando | Utilizzo |
|--------|--------|
|`list disk`|Visualizza tutti i dischi del computer.  Ognuno avrà un numero di disco, a partire da 0. Un asterisco (\*) sotto la riga Gpt significa che il disco è lo stile di partizione GPT. E' necessario indicare a DiskPart quale disco deve essere gestito utilizzando il `select disk`|
|`list volume`|Per visualizzare tutti i volumi su tutti i dischi. Ciascuno avrà un numero di volume, a partire da 0.  E' necessario indicare a DiskPart quale volume deve essere gestito utilizzando il `select disk`.|

### 1.2.1. Comando /s

Il comando `/s` permette di lanciare degli script formati solo da comandi `diskpart`, ogni comando deve essere su una linea del file, non ci deve essere alcuna riga vuota e eventuali commenti sono righe che cominciano con `rem`.

Esempio di utilizzo:

```powershell
diskpart /s initdisk.txt
```

## 1.3. DISM

DISM (_Deployment Image Servicing and Management_) può essere usato per creare una immagine Windows con formato .wim.
I seguenti sono i tre comandi comodi da utilizzare:

| Comando | Funzione |
|--------|--------|
|`/Capture-Image`|Crea una immagine .wim a partire da un disco|
|`/Append-Image`|Appende una immagine di un disco ad una immagine .wim preesistente|
|`/Apply-Image`|Data una immagine .wim la imposta in una partizione|


### 1.3.1. Backup

Esempio di comandi per effettuare un backup

```powershell
Dism /Capture-Image /ImageFile:C:\\my-windows-partition.wim /CaptureDir:C:\ /Name:"C-DRIVE"
Dism /Append-Image /ImageFile:C:\\my-windows-partition.wim /CaptureDir:D:\ /Name:"C+D Drive"
Dism /Append-Image /ImageFile:C:\\my-windows-partition.wim /CaptureDir:E:\ /Name:"C+D+E Drive"
```

Una volta ottenuta l'immagine devo copiarla in una posizione comoda (per esempio su chiavetta o su rete).
Per esempio, per copiarla su share di rete utilizzare:

```powershell
net use N: \\\Server\\Share
md N:\\Images\
copy C:\\my-windows-partition.wim N:\\Images\
```

### 1.3.2. Restore

Per reimpostare una immagine presa con DISM in una nuova partizione utilizzare il comando `/Apply-Image`.

```powershell
dism /apply-image /imagefile:<NOMEIMMAGINE>.wim /index:1 /applydir:<PERCORSO>
```

## **1.4 WinPE**

Windows PE (**WinPE**) per Windows 10 è un sistema operativo di dimensioni ridotte, usato per installare, distribuire e ripristinare Windows.

Preparare una chiavetta per poterci installare **WinPE**

**TODO**