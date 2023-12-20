---
tags:
  - PersonalKnowledgeManagement
---
## Definizione
Obsidian è un tool per prendere note (fratello di RoamResearch) che ha come caratteristica principale la non gerarchicità delle note e la loro interconnessione.
Non è obbligatoria una struttura a cartelle, anzi è scoraggiata: tutte le note dovrebbero essere nella stessa cartella (un po' come il nostro cervello) e la navigazione avviene tramite i link tra le stesse (Obsidian è un tool **note first**).

Tutti i file sono normali file markdown salvati in locale sul proprio PC.
## Cartelle
Decidere come e quali cartelle utilizzare non è semplice in quanto dipende molto da proprio workflow.
Quello che è sicuro è che bisogna evitare di creare cartelle in base all'argomento: la categorizzazione tramite cartelle e non tramite tag non è lo scopo di Obsidian.
Io strutturo le cartelle come descritto in [[My P.A.R.A.]].
Esistono comunque molti link che spiegano i vari approcci:
* https://forum.obsidian.md/t/advantages-using-folders/10660/26
* https://forum.obsidian.md/t/example-workflows-in-obsidian/1093/24

## Plugin
```dataview
LIST FROM #obsidianPlugin
```
## Formatting

### Resizing images
Impostare la larghezza dell'immagine 100px.
```md
![Engelbart|100](https://history-computer.com/ModernComputer/Basis/images/Engelbart.jpg)
```
### Blockquotes
```md
> Human beings face ever more complex and urgent problems, and their effectiveness in dealing with these problems is a matter that is critical to the stability and continued progress of society.

\- Doug Engelbart, 1961
```
### Task list
```md
[x] #tags, [links](), **formatting** supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [?] this is also a complete item (works with every character)
- [ ] #task this is an incomplete item
- [ ] #task tasks can be clicked in Preview to be checked off
```
### Footnotes
```md
Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: meaningful!

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.
```
### Math
Posso scrivere operazioni singola con il comando `$` come $A=B$ oppure centrate a capo con il doppio `$$` come per esempio
$$A = B$$
## Immagini
Per allegare una immagine basta trascinarla o incollarla direttamente su Obsidian.
L'immagine viene allegata come `![[image.png]]`. Posso modificarne le dimensioni indicando `![[image.png|100x100]]` oppure farlo mantenendo il rapporto d'aspetto indicando solo una dimensione con `![[image.png|100]]`.

## Callouts
```markdown
 [!INFO] [title]
> Here's a callout block.
> It supports **markdown** and [[Internal link|wikilinks]].
```
Al posto di !info posso mettere i seguenti valori, ognuno con il suo stile:
-   note
-   abstract, summary, tldr
-   info, todo
-   tip, hint, important
-   success, check, done
-   question, help, faq
-   warning, caution, attention
-   failure, fail, missing
-   danger, error
-   bug
-   example
-   quote, cite

Posso anche renderlo foldable aggiungendo `+` (default espanda) or `-` (default collassata) dopo le quadre:
```markdown
> [!FAQ]- Are callouts foldable?
> Yes! In a foldable callout, the contents are hidden until it is expanded.
```

## Riferimenti a note o blocchi
* Per riferirsi una una nota si usano le doppie parentesi quadre. `[[]]`;
* Per cambiare il testo visualizzato di un link usare il pipe `|` esempio `[[nota|nome custom della nota]]`;
* Per riferirsi a un blocco di testo all'interno di una nota usare `[[]]^hash` e l'hash lo suggerisce Obsidian con un navigator una volta scritto `^`;
* Per fare l'embeed di una nota o di un blocco di testo di questa in una altra nota aggiungere il punto esclamativo all'inizio. `![[]]^hash`.