---
tags:
  - PersonalKnowledgeManagement
  - Learning
---
Questo plugin permette di implementare le tecniche di [[Spaced repetition]] per la memorizzazione in Obsidian.
L'idea è creare dei deck i quali sono dei contenitori di flashcards. Ogni flashcards è un concetto da memorizzare e di cui deve esserne fatto il recall.
La review delle cards o dei concetti avviene in modo incrementale in base a quanto conosco il concetto (conosco bene, prossima review lontana, conosco male, prossima review vicina) e quanto tempo fa ho effettuato la precedente review.
In particolare dopo la review di ogni concetto questo viene marcato come:
- `Hard`: non ricordo la risposta (prossima recall a breve)
- `Good`: ricordo bene la risposta (prossima recall fra un po')
- `Easy`: ricordo senza alcun problema la risposta (prossima recall fra molto tempo)

Il calcolo della prossima data viene effettuato da un algoritmo.

## Deck
Una nota può essere indicata come "deck" contenente *n* flashcards. Per indicare che una nota è un deck è necessario aggiungere il tag `#flashcards`.
Esiste anche il concetto di subdeck, basta utilizzare il tag
`#flashcards/subdeck/subdeck`.
Se ho una struttura a cartelle gerarchiche il plugin automaticamente utilizzerà i path per creare deck e subdeck.
i.e. `Folder/sub-folder/sub-sub-folder` ⇔ `Deck/sub-deck/sub-sub-deck`

## Flashcards
Una nota può contenere una o più flashcard, la quale può essere creata in vari modi:

### Tipologie di card

#### Single-line Basic
La domanda e la risposta possono essere separate da `::` (configurabile).
`the question goes on this side::answer goes here!`

#### Single-line Reversed
In questo caso creo due cards: `side1:::side2` e `side2:::side1`
La domanda e la risposta possono essere separate da `:::` (configurabile).
`the question/answer goes on this side:::question/answer goes here!`

#### Multi-line Basic
Questo metodo è comodo per creare cards lunghe, il separatore è il `?`
```
As per the definition
of "multiline" the prompt
can be on multiple lines
?
same goes for
the answer
```

#### Multi-line Reversed
In questo caso creo due cards: `side1??side2` e `side2??side1` multiriga.
```
As per the definition
of "multiline" the prompt
can be on multiple lines
??
same goes for
the answer
```

#### Cloze cards
E' possibile creare anche cloze deletion cards (la *cloze deletion* è una frase dove del testo importante è sostituito da "..." e tale frase è il testo da indovinare).
In questo caso il testo evidenziato o in grassetto diventa una cloze deletion (nei setting posso indicare se voglio solo l'evidenziato o solo il grassetto).

### Titolo
Se la nota da cui arrivano le cards ha degli heading, questi vengono utilizzati come titolo (context) della card.
Per esempio se ho una nota strutturata come segue:
```md
#flashcards
## Capitals
### Africa
Kenya::Nairobi
### North America
Canada::Ottawa
```
La flashcard `Kenya::Nairobi` avrà `Trivia > Capitals > Africa` come titolo.

### Review
Una volta che la card è stata controllata viene aggiunto un commento HTML che indica la data della prossima review:
```
<!--SR:!2021-08-20,13,290-->
```
Essendo un commento HTML non è visibile in modalità preview della card. Per le card single-line è possibile configurare il plugin in modo che il commento venga aggiunto in una riga separata.
Shortcut:
- `Space/Enter` => Mostra la risposta
- `0` => Resetta i progressi effettuati sulla card
- `1` => Review come  `Hard`
- `2` o `Space` => Review come `Good`
- `3` => Review come `Easy`
- `S` => Skip

## Blog
Ho scritto un post qui: [[Spaced Repetition con Obsidian]].