---
tags:
  - Coding
  - CSharp
  - Memory
---
Di seguito spiego i passaggi principali per analizzare la propria applicazione per trovare eventuali leak (in particolare riferiti ad oggetti Halcon) con **DotMemory**.

1. Aprire *DotMemory* (Reshaper - Profile - Run Application Memory Profiling)
2. Selezionare *Local - StandAlone* (non utilizzare Attach To Process altrimenti la funzionalità di conoscere chi crea i vari oggetti (allocation data) è disabilitata)
3. Inserire il path dell'applicativo (per esempio *C:\Users\Paolo\Repository\Imago\mhira3d\src\bin\x64\Debug\Mhira3D.exe*)
4. Spuntare "*Control profiling manually*" con l'impostazione "*Start collecting allocation...*" a true
5. Premere *Run*. L'applicazione indicata verrà lanciata
6. L'interfaccia DotMemory ha due comandi principali:
  - *Collect Allocations*: salva tutti gli stack trace di creazione di tutti gli oggetti.
  - *Get Snapshot*: crea uno snapshot di tutti gli oggetti attualmente caricati in memoria (anche unmanaged).
7. Premere *Get Snapshot*, [fare cose], premere ancora *Get Snapshot*.
8. Uscire dall'applicativo (Kill Process)
9. Ora abbiamo due snapshot da confrontare, premere, in basso, il pulsante *Compare*
10. Raggruppare gli oggetti per assembly (Group by Assembly) cercando `halcondotnet`
11. Aprire l'expander e cercare `HalconDotNet.HObject`
12. Abbiamo due colonne di riferimento: **New objects** e **Dead objects**. Se i due valori corrispondono non ho leak e possono concludere l'analisi. Qualora invece i due valori differiscano (tipicamente New objects > Dead objects) ho un leak.
13. Premere il tasto "+" in alto che copia la finestra corrente in una nuova scheda.
14. In una scheda cliccare su "**New Objects**" e nella seconda su "**Dead objects**"
15. Ora dobbiamo trovare l'oggetto che è presente in una lista e non nella seconda. una volta trovato doppio click.
16. Tramite il menu "Key Retention Paths" posso capire di che oggetto si tratta, mentre tramite il menu "Creation Stack Trace" posso capire chi lo crea e quando.
17. Ora ho tutte le informazioni per risolvere il problema.