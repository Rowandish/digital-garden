---
tags:
  - PersonalKnowledgeManagement
---
L''obiettivo è pubblicare un Digital Garden basato su un vault di Obsidian (non tutte le pagine ma solo quelle selezionate) usando come host [Github pages](https://levelup.gitconnected.com/build-a-personal-website-with-github-pages-and-hugo-6c68592204c7) e come builder del sito [Quartz](https://quartz.jzhao.xyz/). Useremo un [custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).

## Configurazione iniziale

* Aggiorniamo `Node` e `npm` su Windows all'ultima versione.
* Fork della repository di Quartz sul nostro Github in quanto i file Markdown di Obsidian saranno nella mia cartella `content` di quartz (che nella repository ufficiale è ovviamente vuota a meno di un file `index.md`.
* Clonare la nuova repository forkata e inizializzare un nuovo quartz
```
git clone https://github.com/Rowandish/digital-garden.git
cd quartz
npm i
npx quartz create
```
Questo codice principalmente creerà, oltre alle varie configurazioni, una cartella `content` dove dovranno essere collocati i file di Quartz da pubblicare.
* Testare in locale basta lanciare il comando
```
npx quartz build --serve
```
Questo  crea un sito a partire dal contenuto della cartella `content` su `localhost:8080` (il sito effettivo si trova nella cartella `public`).

## Import del proprio Obsidian Vault

* Tagliare e incollare all'interno di `content` il contenuto del proprio vault di Obsidian
* Modificare il file `quartz.config.ts ` con le proprie preferenze (soprattutto indicando in `ignorePatterns` le cartelle/file che non vogliamo che siano buildate nel sito)
* Lanciare il comando `npx quartz build --serve`  fino a quando il risultato non è soddisfacente
* Modificare il file `.gitignore` in modo da evitare di pushare su repo pubblica file privati

## Opzioni
Le configurazioni di Quartz si possono trovare nei file `quartz.config.ts` mentre per il layout in `quartz.layout.ts`.

## Frontmatter
Quartz supporta 4 frontmatter nativamente, che tipicamente possono/devono essere aggiunti a tutte le note che vogliamo gestire.
```
---
title: Example Title
draft: false
tags:
  - example-tag
---
 
The rest of your content lives here. You can use **Markdown** here :)
```

## Cose da sapere
* Quartz non supporta file con emoji nel nome
* 