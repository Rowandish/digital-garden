- Definizione di allucinazione: 
- Perché accadono: 

## Introduzione
Si parla di "allucinazioni" nei modelli di linguaggio (come GPT) quando l'IA genera ==risposte o informazioni che sembrano plausibili ma non sono vere o corrette==. Ad esempio, se chiedi una ricetta inventata, l'IA può produrre una risposta come se fosse reale, anche se non ha basi nei dati su cui è stata addestrata.
Queste accadono in quanto i Language Model sono addestrati a ==completare il testo basandosi su probabilità statistiche, senza un legame diretto con verità oggettive o morali==. In altre parole, il loro scopo principale è proseguire il testo in modo coerente, non fornire risposte vere.
### Cos'è un Language Model?

- È un sistema addestrato su grandi quantità di testo per ==prevedere la sequenza più probabile di parole==. Funziona come una sorta di simulazione di tessuto nervoso, continuando il testo token per token (parola per parola o frammento per frammento).
- Non interagisce davvero con te: Quando parli con un modello come ChatGPT, in realtà non "conversa", ma ==crea una simulazione probabilistica di una conversazione==. Ad esempio, se gli dai un testo con un bot che risponde e poi scrivi "Utente dice: ...", il modello proseguirà anche la parte dell'utente. Capire questo concetto è fondamentale per capire cosa è veramente un Language Model. Ad esempio se chiedi una ricetta inventata (es. della "dammi la ricetta della carbonara della signora Pina"), il modello cerca di proseguire il testo come se quella ricetta esistesse.

Gli LLM possano generare **informazioni plausibili ma errate**, il cosiddetto "nonsense plausibile". Queste non sono bug, ma una caratteristica intrinseca del modo in cui funzionano gli LLM.
#### Le allucinazioni come elemento naturale del modello
- Le allucinazioni non sono un "bug" ma una caratteristica naturale del modello. Il sistema non è progettato per "dire la verità" ma per proseguire il testo in modo statisticamente plausibile.
- Pensare a GPT un modello di linguaggio come una sorta di "compressione dell'Internet" (un enorme file zip): contiene informazioni statistiche su un'enorme quantità di testo, ma non garantisce precisione o verità.
- ==Le "allucinazioni" sono una conseguenza naturale del modo in cui funzionano i modelli di linguaggio, sono connaturate ad essi. Anzi, sono il motivo per cui sono così potenti==. Esse permettono al sistema di essere creativo, ad esempio scrivere un sonetto originale o produrre contenuti in uno stile specifico: senza le allucinazioni sarebbe impossibile fare ciò.
- Limiti e contesto: Le allucinazioni diventano un problema solo quando si cerca di ottenere risposte affidabili o accurate in contesti critici.

### Tipologie

Le allucinazioni possono essere classificate in base alla loro granularità:

1. **Contraddizione nella frase**: Una frase contraddice un'altra. Es.: "Il cielo è blu oggi." -> "Il cielo è verde oggi."
2. **Contraddizione del prompt**: L'output non rispetta la richiesta. Es.: Chiedi una recensione positiva di un ristorante e il modello risponde che il cibo era pessimo.
3. **Errori fattuali**: Dichiarazioni palesemente false, come "Barack Obama è stato il primo presidente degli Stati Uniti."
4. **Informazioni non pertinenti o prive di senso**: Es.: "La capitale della Francia è Parigi. Parigi è anche il nome di un cantante famoso."

## Come si affrontano

Esistono vari approcci per ridurre o gestire le allucinazioni: a monte con il fine tuning, durante il prompt con il RAG o a valle con i guardrails o post-processing

### 1. Fine-tuning e Annotazione
- Il modello viene addestrato ulteriormente su set di dati annotati manualmente con risposte corrette o eticamente appropriate invece che essere addestrato solo su tutto internet senza filtri.
- Esempio: I GPT 3 iniziali potevano rispondere a domande su temi eticamente discutibili senza filtri. Oggi, grazie all'addestramento con testi scritti da annotatori umani, evitano queste risposte.
### 2. Retrieval-Augmented Generation (RAG) (o Grounding)
- Integrare informazioni reali nel processo di generazione.
- Ad esempio, prima di rispondere a una domanda, il sistema esegue una ricerca in archivi o database specifici per ottenere il contesto. Questo contesto viene poi incluso nel prompt per aiutare il modello a rispondere basandosi su informazioni reali.
- Fornendo quindi sia la domanda che la risposta nel prompt il Language Model non deve inventarseli ma deve solo recuperare informazioni che ha già.
### 3. Guardrails (Barriere di sicurezza)
- Si costruiscono barriere intorno al modello, imponendo limiti su certi tipi di risposte.
- Esempio: Prompt che includono regole del tipo "Rispondi solo sulla base di questi contenuti".
### 4. Controllo a valle (Post-processing)
- Una volta generata la risposta, viene controllata per verificarne la coerenza con i dati di partenza.
- Esempio: Si verifica se la risposta è deducibile da un documento specifico o se tocca argomenti sensibili, per bloccarla o correggerla.


## Video
* https://www.youtube.com/watch?v=L6wE5islJ9o