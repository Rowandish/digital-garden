---
tags:
  - Blender
---
I materiali sono gli elementi che definiscono l'aspetto visuale degli oggetti nella scena 3D. I materiali determinano le proprietà di superficie come colore, riflessività, opacità, trasparenza, rugosità e altri attributi che definiscono come la luce interagisce con un oggetto.
Alcuni materiali (come metallic o tranmission) funzionano molto meglio se usiamo come [[Render Engines]] cycles.

### Aggiungere un nuovo materiale:

Ecco i passaggi per aggiungere un nuovo materiale a un oggetto in Blender:

1. **Entra nella modalità di modifica dell'oggetto:**
   - Seleziona l'oggetto a cui desideri applicare il materiale.
   - Passa alla modalità di modifica premendo il tasto "Tab" sulla tastiera.
2. **Apri l'editor "Properties":**
   - Nell'editor delle proprietà di Blender, vai alla scheda "Material"
3. **Aggiungi un nuovo materiale:**
   - Se non è già presente un materiale per l'oggetto, troverai un pulsante "New" (Nuovo). Cliccaci sopra per creare un nuovo materiale per l'oggetto selezionato.
4. **Modifica le proprietà del materiale:**
   - Dopodiché, puoi regolare le varie proprietà del materiale come colore, riflessività, opacità, texture, ecc.
   - Utilizza l'editor Node (nodi) per creare materiali più complessi e sofisticati utilizzando nodi shader e texture.

### Proprietà

- **Base Color**: Determina il colore principale dell'oggetto.
- **Roughness**: Determina il grado di liscio o rugoso della superficie. Minore è il valore più l'oggetto risulta luci e riflette la luce. A sinistra `roughness` 0 mentre a destra 0,9.
![[Pasted image 20231121151419.png]]![[Pasted image 20231121151440.png]]

- **Metallic**: permette di enfatizzare la componente metallica riflettente dell'oggetto. Tipicamente va messo sempre o a 0 o a 1. A sinistra un oggetto con metallic a 0 (e `rounghness` bassa) e a destra con metallic 1.

![[Pasted image 20231121180116.png]]![[Pasted image 20231121180104.png]]
- **Transimission**: più si avvicina all'oggetto più questo assume un effetto vetro in quanto viene permesso alla luce di passare attraverso l'oggetto.
N.b. transmission funziona solo se `metallic` è impostato a 0.
Per fare l'effetto vetro meglio impostare `Saturation` bassa e `Value` vicino a 1. Con la `transmission` lavoro bene la `roughness`: con `roughness` a 0 ho un vetro brillante perfetto, aumentandola ottengo un effetto vetro opaco, come se fosse di ghiaccio.
![[Pasted image 20231121180951.png]]
![[Pasted image 20231121180832.png|350]]![[Pasted image 20231121180846.png|350]]
* **Transmission roughness**: permette di rendere meno shiny l'oggetto con la luce al suo interno che si diffonde più uniformemente