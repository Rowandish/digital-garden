---
tags:
  - Coding
  - CSharp
  - WPF
---
## Introduzione
Il binding in WPF è il concetto fondamentale in quanto permette di creare una relazione tra le View e un Model/Controller (impostabile tramite il `DataContext`).
**La modifica di una property del model però non si riflette automaticamente nella view**, a meno di esplicitare l'aggiornamento della stessa tramite l'interfaccia `INotifyPropertyChanged`.
Implementando il `INotifyPropertyChanged` viene esposto l'evento `PropertyChanged` che deve essere lanciato con un metodo simile a:
```cs
public event PropertyChangedEventHandler PropertyChanged;
protected void FirePropertyChanged(string propertyName)
{
  PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
}
```
che, tramite la chiamata, ad esempio
```cs
FirePropertyChanged("SelectedFormat");
```
obbliga lo XAMl ad aggiornare i `{Binding SelectedFormat}`

## DataContext
Il `DataContext` è un concetto fondamentale per quanto riguarda il binding di oggetti in WPF in quanto **indica l'origine dei dati** da cui andare a prendere l'oggetto indicato nel Bind.
Tipicamente, alla creazione di una nuova finestra o `UserControl`, viene utilizzato come `DataContext` **this(o self)**, indicando che gli oggetti a cui farò riferimento nel binding appartengono al code behind dell'oggetto stesso.
Quindi se scrivo
```xml
<Label Content="{Binding Name}" />
```
Sto asserendo che il codice xaml.cs avrà una property chiamata `Name` e lo xaml si sta riferendo a quella.

Per evitare che Resharper fornisca degli warning per mancata assegnazione del `Datacontext` nei `binding`, conviene esplicitare sempre il `DataContext` nello XAMl nella dichiarazione della finestra o `UserControl`.

```xml
DataContext="{Binding RelativeSource={RelativeSource Self}}"
```

Spesso può però capitare che io voglia bindare, in oggetti diversi, dati provenienti da più Datacontext diversi. E' possibile overridare il DataContext locale per ogni singolo tag, nel seguente modo:

```xml
<Window x:Name="myWindow"> <!-- DataContext is set to ClassA -->
  <StackPanel> <!-- DataContext is set to ClassA -->

  <!-- DataContext is set to ClassA, so will display ClassA.Name -->
  <Label Content="{Binding Name}" />

  <!-- DataContext is still ClassA, however we are setting it to ClassA.ClassB -->
  <StackPanel DataContext="{Binding ClassB}">

  <!-- DataContext is set to ClassB, so will display ClassB.Name -->
  <Label Content="{Binding Name}" />

  <!-- DataContext is still ClassB, but we are binding to the Window's DataContext.Name which is ClassA.Name -->
  <Label Content="{Binding ElementName=myWindow, Path=DataContext.Name}" /> 
  </StackPanel>
  </StackPanel>
</Window>
```


### Assegnare il DataContext a il valore di una classe statica
Talvolta esiste la necessità di effettuare un binding al valore fornito da una property di una classe statica (come per esempio `Math` o `Startup`).
In questo caso la sintassi è leggermente diversa:
```xml
Text="{Binding Source={x:Static MyNamespace:MyStaticClass.MyProperty}, Mode=OneWay}"
```
Oppure con un esempio pratico:
```xml
<DockPanel Name="Panel" DataContext="{Binding Source={x:Static mhira3D:Startup.UserManager}, Mode=OneWay}">
```

### Aggiornare i valori di un Binding di un diverso DataContext
Se il binding è riferito ad un `DataContext` diverso da this, il normale metodo `OnPropertyChanged` non funziona, in quanto dovrebbe essere lanciato dall'oggetto a cui è riferito il `DataContext`, non da this.
Per risolvere questo problema è obbligare un refresh dei bindings basta eliminare e riassegnare il `DataContext` in questo modo:
```csharp
var dataContext = Panel.DataContext;
Panel.DataContext = null;
Panel.DataContext = dataContext;
```
Effettuare l'assegnazione in una sola riga invece **non funziona**.
```csharp
Panel.DataContext = Panel.DataContext;
```


### Effettuare un multibinding con oggetti appartenenti a due DataContext diversi
Consideriamo il seguente esempio:
```xml
<DockPanel DataContext="{Binding Source={x:Static mhira3D:Startup.UserManager}, Mode=OneWay}">
  <wpfObjects:BlackButton>
  <wpfObjects:BlackButton.IsEnabled>
  <MultiBinding Converter="{StaticResource BooleanAndConverter}">
  <Binding Path="CanUserLoadFormat" />
  <Binding RelativeSource="{RelativeSource FindAncestor, AncestorType={x:Type Window}}" Path="HasSelectedFormat" />
  </MultiBinding>
  </wpfObjects:BlackButton.IsEnabled>
  </wpfObjects:BlackButton>
  </DockPanel>
```
Voglio creare un bottone (`wpfObjects:BlackButton`) che è abilitato secondo due condizioni diverse:

1. L'utente attualmente loggato ha i permessi per eseguire l'operazione
2. Ho selezionato almeno una riga dei formati

Il problema è che i permessi dell'utente loggato sono forniti dalla classe statica `Startup.UserManager` con la property `CanUserLoadFormat`, mentre il fatto che la tabella abbia una riga attualmente selezionata o meno è una property dello *xaml.cs* a cui fa riferimento questo codice:

```cs
public bool HasSelectedFormat => SelectedFormat != null;
```

Conseguentemente ho due property che voglio avere in AND che appartengono a due `DataContext` diversi.

Per risolvere è per prima cosa necessario creare un converter che implementa `IMultiValueConverter` che implementa la logica AND.
```cs
public class BooleanAndConverter : IMultiValueConverter
{
  public object Convert(object[] values, Type targetType, object parameter, CultureInfo culture)
  {
  foreach (var value in values)
  {
  if (value is bool && (bool) value == false)
  {
  return false;
  }
  }
  return true;
  }

  public object[] ConvertBack(object value, Type[] targetTypes, object parameter, CultureInfo culture)
  {
  throw new NotSupporte[[DEX]]ception("BooleanAndConverter is a OneWay converter.");
  }
}
```
Assegnando tale converter al `MultiBinding`:
```xml
<MultiBinding Converter="{StaticResource BooleanAndConverter}">
```
Successivamente creare i due binding utilizzando il comando `RelativeSource` che permette di modificare il `DataContext` di un oggetto, in particolare la scrittura
```xml
RelativeSource="{RelativeSource FindAncestor, AncestorType={x:Type Window}}"
```
indica che mi sto riferendo al `DataContext` della finestra corrente e non del tag contenitore.

## ItemsSource
Alcuni oggetti come `ListBox` o `DataGrid` possiedono la property `ItemsSource` che indica l'insieme degli elementi che devono essere visualizzati nella stessa.
In particolare, se viene bindata una property di tipo `ObservableCollection` l'aggiornamento di questa ultima si riflette automaticamente sugli oggetti.
E' sempre meglio esplicitare l'`ItemsSource` a livello di *XAMl* e non di *CS*, in questo modo:
```xml
<DataGrid ItemsSource="{Binding Formati}"/>
```
Andando a bindare una property del tipo:
```cs
public ObservableCollection<Formato> Formati { get; set; } = new ObservableCollection<Formato>();
```