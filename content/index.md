---
title: Benvenuto nel mio giardino digitale
---
## Aree

* ### [[💵 Money]]
* ### [[Areas/Work/💼 Work]]
* ### [[✍️Blog]]
* ### [[🏘️ Houses]]
* ### [[📝PKM]]
* ### [[🙍Personal]]
* ### [[📚 Learning]]
* ### [[📈 Productivity]]
* ### [[👶Baby]]

## Progetti 

### PKM
```dataview
	TABLE Status FROM #Project and -"Assets/Templates" where Area=[[📝PKM]]
```
### Blog
```dataview
	TABLE Status FROM #Project and -"Assets/Templates" where Area=[[✍️Blog]]
```
### Money
```dataview
	TABLE Status FROM #Project and -"Assets/Templates" where Area=[[💵 Money]]
```
### Work
```dataview
	TABLE Status FROM #Project and -"Assets/Templates" where Area=[[💼 Work]]
```
### Productivity
```dataview
	TABLE Status FROM #Project and -"Assets/Templates" where Area=[[📈 Productivity]]
```

### Learning
```dataview
	TABLE Status FROM #Project and -"Assets/Templates" where Area=[[📚 Learning]]
```
### Personal
```dataview
	TABLE Status FROM #Project and -"Assets/Templates" where Area=[[🙍Personal]]
```

### Work
```dataview
	TABLE Status FROM #Project and -"Assets/Templates" where Area=[[💼 Work]]
```
- 📹Last video tracked
	```dataview
	LIST FROM #video SORT file.cdate DESC LIMIT 5
	```

## Vault Info
- 🔖 Tagged:  favorite 
```dataview
	LIST FROM #favourite
```
- 〽️ Statistiche
	-  😎File totali: `$=dv.pages().length`
	- 💭Aree: `$=dv.pages('#Area').length`
	- 📝Progetti: `$=dv.pages('#Project').length`
	- 📹 Video tracked: `$=dv.pages('#video').length`
	-  ⚛️Atomic notes: `$=dv.pages('').length` 