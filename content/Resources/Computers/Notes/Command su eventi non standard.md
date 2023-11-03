---
tags:
  - Coding
  - CSharp
  - WPF
  - ImagoLearning
Date: 2023-10-16
Done: false
---
Nell'MVVM si usa l'interfaccia `ICommand` per prendere un particolare evento e portarlo nel `ViewModel`.
Il problema è che spesso non tutti gli eventi sono supportati, per esempio nel `Button` è supportato il `Click` ma se voglio fare un evento sul `LostFocus` di una `TextBox` (esempio) non ho modo di passare quell'evento al `ViewModel`.
Per risolvere ci sono due metodi

## Sfruttare il cambio di una property bindata
Questo è il classico caso di eventi che si triggerano se qualcosa cambia: per esempio per prendere l'evento di `CheckedChanged` di un `Checkbox` posso bindarmi alla property `IsChecked` e sfruttare, code behind, il metodo partial che si triggera quando questa property viene cambiata (metodo che viene generato con il pacchetto `CommunityToolkit.Mvvm`).
Esempio questa è la property nello XAML
```xml
<CheckBox IsChecked="{Binding MinCheckboxIsChecked}" />
```
e nel `ViewModel` avrò
```csharp
[ObservableProperty] private bool _minCheckboxIsChecked;

partial void OnMinCheckboxIsCheckedChanged(bool value)
{
    BuildAndRefresh(ChartFilter);
}
```

## Pacchetto nuget Microsoft.xaml.behaviors
Questo pacchetto permette di far diventare `Command` qualsiasi evento.
Vediamo, per esempio, il codice per avere come `Command` l'evento di `LostFocus`:
```xml
<TextBox>
    <b:Interaction.Triggers>
        <b:EventTrigger EventName="LostFocus">
            <b:InvokeCommandAction Command="{Binding SearchLostFocusCommand}" />
        </b:EventTrigger>
    </b:Interaction.Triggers>
</TextBox>
```
* `EventName`: nome dell'evento dell'`UserControl` che voglio utilizzare 
* `InvokeCommandAction`: oggetto che lancia il comando passato in `Command`, comando presente nel `ViewModel`.

Con questo pacchetto è possibile anche bindarmi agli eventi del mouse che riguardano l'oggetto, per esempio se come `EventName` scrivo `MouseLeftButtonDown` posso avere un command che si triggera quando l'utente clicca con il mouse sull'`UserControl`.