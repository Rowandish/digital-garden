## Tutorial
```dataview
	LIST FROM "Resources/Cooking/Notes" AND #Tutorial 
```

## 🥓Breakfast
```dataview
	LIST FROM #Recipe and #Colazione
```
## 🍝First courses

### Pasta
```dataview
	LIST FROM #Recipe and #PrimiPiatti and #Pasta
```

### Rice
```dataview
	LIST FROM #Recipe and #PrimiPiatti and #Riso
```

### Soup
```dataview
	LIST FROM #Recipe and #PrimiPiatti and #Zuppe
```

### Other
```dataview
	LIST FROM #Recipe and #PrimiPiatti and -#Riso and -#Pasta and -#Zuppe
```

## 🥩Second courses

```dataview
	LIST FROM #Recipe and #SecondiPiatti
```

## 🍆Sides
```dataview
	LIST FROM #Recipe and #Contorno
```

## 🥮Sweets
### 🍰Standard
```dataview
	LIST FROM #Recipe and #Dolci and !#Light
```
### 🥕Light
```dataview
	LIST FROM #Recipe and #Dolci and #Light
```

## 🍸Cocktail
```dataview
	LIST FROM #Recipe and #Cocktail
```
### ☕Coffe
```dataview
	LIST FROM #Recipe and #Cocktail and #Coffe 
```

## 🔌Devices
```dataview
	LIST FROM "Resources/Cooking/Notes" AND #Devices
```