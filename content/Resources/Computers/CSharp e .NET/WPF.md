---
tags:
  - WPF
---
## Visual Studio

Il setup per Visual Studio comprende:
* Toolbox: elenco dei componenti (`Control`)che posso usare all'interno della finestra di lavoro (`ListView`, `Combobox`...) e posso mostrarla tramite `View -> Toolbox`

## Nomi

Ogni elemento in XAML può avere un nome in modo che possa essere riferito code-behind. La sintassi è:`x_Name="xxxx"`.
Una convenzione carina per il nome da dare è: `significatoSemanticoNomeControl`.
Per esempio se è un bottone che rappresenta una percentuale il suo nome sarà `percentageButton`.

## Grid

Questa è la struttura fondamentale di XAML, è formata da righe e colonne, ognuna della loro dimensione, con degli elementi che appartengono ad ogni cella.
Property comode:
* `Grid.Row|Column`: a che riga/colonna appartiene l'elemento
* `Grid.Column|Row Span`: quante righe/colonne occupa l'elemento

### Dimensioni

* `Auto`: la larghezza della colonna dipende dal contenuto ed è esattamente il minimo per contenere gli oggetti contenuti. Per esempio se nella colonna ho un Button largo 100 la colonna sarà larga 100. Se non ho nulla sarà larga 0
* `*`: la dimensione è proporzionale al numero di elementi `*`. Per esempio con un solo elemento `*` sarà 100%, con due elementi ognuno sarà 50% e così via.
* `xxx px`: la dimensione è fissa a tali px.

![[Pasted image 20230828105028.png]]

## Stili
Gli stili di una applicazione possono essere definiti con vari scope e essere espliciti o impliciti.
Gli stili espliciti sono degli stili che devono essere poi referenziati dal Control che li vuole utilizzare mediante il comando `StaticResource` o `DynamicResource`.
Gli stili impliciti invece si associano implicitamente ad un tipo di oggetto, per esempio lo stile di tutti i Button dell'applicazione, lo stile di tutte le label e così via.

### Stili Impliciti
Per stilare tutti gli elementi di un determinato tipo devo definire un tag `Style` a livello di `Window` o di `Application` con un attributo `TargetType` che identifica a che `Control` associargli.
In questo esempio associo un determinato stile a tutti i Button e la Label dell'applicazione

```xml
<Style TargetType="Button">
	<Setter Property="Foreground" Value="White"/>
	<Setter Property="FontSize" Value="25"/>
</Style>

<Style TargetType="Label">
	<Setter Property="FontSize" Value="70"/>
</Style>
```

### Stili espliciti
Posso anche definire degli stili che devono essere esplicitamente referenziati tramite l'attributo `x:Key` e lo `{StaticResource}`.
Questi stili possono anche ereditare da un altr
o stile grazie al tag `BasedOn`.
```xml
<Style TargetType="Button" x:Key="operatorButtonsStyle" BasedOn="{StaticResource numberButtonsStyle}">
	<Setter Property="Background" Value="{StaticResource operatorsColor}"/>
</Style>

<Style TargetType="Button" x:Key="additionalButtonsStyle" BasedOn="{StaticResource numberButtonsStyle}">
	<Setter Property="Background" Value="LightGray"/>
	<Setter Property="Foreground" Value="Black"/>
</Style>
```
### Scope
#### Singolo tag
Ogni tag può avere il suo stile esplicitato. Può andare bene solo se quello stile lo ha solo quello specifico elemento
```xml
<Button x:Name="divisionButton" Background="Orange" Foreground="White"/>
```

#### Window
Ogni `Window` può avere  degli stili definiti come `Resources` privati. In questo modo evito di copincollare gli stili per tutta la finestra ma non espongo questi stili al mondo esterno.

Per esempio in questo caso definisco due colori
```xml
<Window.Resources>
	<SolidColorBrush x:Key="numbersColor" Color="#666666"/>
	<SolidColorBrush x:Key="operatorsColor" Color="Green"/>
</Window.Resources>
```
e li referenzio in questo modo:
```xml
<Button Background="{StaticResource operatorsColor}"/>
```

#### Application
E' possibile definire degli stili che siano validi per tutta l'applicazione. Questi vengono definiti nel file `App.xaml` 
```xml
<Application.Resources>
	<SolidColorBrush x:Key="numbersColor" Color="#333333"/>
	<SolidColorBrush x:Key="operatorsColor" Color="Green"/>
	<SolidColorBrush x:Key="foregroundColor" Color="White"/>
</Application.Resources>
```

## Binding

Il binding è il link tra l'`Object` code behind e il `Control UI`.
Il `Data Binding` è la mappatura tra il nome della property dell'oggetto del model e l'attributo del Control.
![[Pasted image 20230829160958.png]]
Ogni Binding ha le seguenti property:
* `Path`: oggetto a cui voglio puntare
* Mode
	* `OneWay` (default): l'UI si popola in base al model ma non il contrario. (es. `Label`)
	* `TwoWay`: l'UI dipendere dal model ma anche il model viene modificato se cambia l'UI (es. una `TextBox`)
	* `TwoWay` e `UpdateSourceTrigger=PropertyChanged`: Come sopra con l'aggiunta che il model viene cambiato ad ogni cambio della property in modo immediato e non quando l'oggetto perde il focus (che è il comportamento di default)
	* `OneWayToSource`: il contrario di `OneWay`, quindi prende il valore dello XAML e lo imposta in C# ma non viceversa.
	* `OneTime`: come`OneWay` ma che avviene solo una volta quando viene settato il `DataContext`.

### Context
Il `Context` è il luogo dove andare a prendere l'oggetto del model. Posso avere context per l'intera finestra e poi overridare questo context nella `Grid` e in ogni eventuale figlio.

![[Pasted image 20230829161145.png]]

## ListView

Questo `Control` è fondamentale per rappresentare un insieme di elementi.
In particolare tramite la sua property `ItemsSource` posso definire la collection (`IEnumerable`) di cui fare il foreach e tramite la sua property ItemTemplate posso definire come il singolo oggetto viene rappresentato.
```xml
 <ListView ItemsSource="{Binding Contacts}">
	<!-- ItemTemplate permette di definire come viene visualizzato ogni elemento della mia ListView-->
	<ListView.ItemTemplate>
		<!-- DataTemplate indica un template che dipende dal binding. Può contenere sia oggetti normali che UserControl custom-->
		<DataTemplate>
			<!-- Qui ho come DataContext il singolo elemento di ItemsSource della ListView-->
			<uc:ContactControl Contact="{Binding}"/>
		</DataTemplate>
	</ListView.ItemTemplate>
</ListView>
```