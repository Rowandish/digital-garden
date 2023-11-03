---
tags:
  - WPF
  - ImagoLearning
Date: 2023-11-21
Done: false
---
Le animazioni in XAML consentono di aggiungere movimento, transizioni e interazioni visive alle tue applicazioni.
Per definirle conviene utilizzare [[Blend  - Visual Studio]] invece del Classico Visual Studio in quanto è stato progettato proprio per descrivere il design e le animazioni del codice.

### Definire l'Elemento da Animare
Per creare un'animazione, devi avere un elemento dell'interfaccia utente su cui applicarla. In questo esempio, utilizzeremo un semplice pulsante.

```xml
<Button Content="Cliccami" Name="myButton" Width="100" Height="30"/>
```

In questo caso, abbiamo creato un pulsante denominato "myButton" con il testo "Cliccami" e una larghezza e un'altezza specificate. Questo sarà l'elemento su cui applicheremo l'animazione.
### Creare uno Storyboard
Ora che abbiamo un elemento da animare, è il momento di creare l'animazione stessa. XAML offre una varietà di modi per definire animazioni, ma uno dei modi più comuni è utilizzare l'elemento `Storyboard`.
==Il `Storyboard` è un contenitore per animazioni che definisce come e quando verranno eseguite.==

Ecco un esempio di come puoi creare un `Storyboard` per animare il pulsante:

```xml
<Window.Resources>
    <Storyboard x:Key="myAnimation">
        <DoubleAnimation
            Storyboard.TargetName="myButton"
            Storyboard.TargetProperty="Opacity"
            From="1.0" To="0.0"
            Duration="0:0:1" />
    </Storyboard>
</Window.Resources>
```

In questo esempio, abbiamo creato un `Storyboard` denominato "myAnimation". All'interno del `Storyboard`, abbiamo definito una `DoubleAnimation` che cambierà l'opacità del pulsante.
L'animazione farà passare l'opacità dal valore 1.0 (completamente visibile) al valore 0.0 (completamente trasparente) in un secondo (`Duration="0:0:1"`).

#### Configurazione
XAML offre molte opzioni per personalizzare le tue animazioni. Ecco alcune delle opzioni più comuni:

- `Storyboard.TargetName`: Specifica il nome dell'elemento dell'interfaccia utente che verrà animato. Nell'esempio sopra, abbiamo utilizzato "myButton" per riferirci al pulsante.
- `Storyboard.TargetProperty`: Specifica la proprietà dell'elemento dell'interfaccia utente che verrà animata. Nell'esempio, abbiamo utilizzato "Opacity" per cambiare l'opacità del pulsante.
- `From` e `To`: Definiscono i valori di partenza e di arrivo per l'animazione. Nell'esempio, l'opacità inizia da 1.0 e termina a 0.0.
- `Duration`: Specifica la durata dell'animazione. Nell'esempio, abbiamo utilizzato "0:0:1" per un secondo di durata.
- `EasingFunction`: Puoi aggiungere una funzione di easing per controllare come l'animazione cambia nel tempo, ad esempio, accelerando o decelerando. Puoi utilizzare varie funzioni di easing predefinite o crearne una personalizzata.

#### Creare Animazioni Complesse
Le animazioni in XAML possono diventare molto complesse e coinvolgenti. Puoi concatenare più animazioni in un `Storyboard`, utilizzare trigger diversi per attivare le animazioni e persino creare animazioni in base a eventi esterni, come il movimento del mouse o l'input utente.

Ad esempio, ecco come puoi creare un `Storyboard` che cambia l'opacità del pulsante quando il mouse si posiziona sopra di esso:

```xml
<Window.Resources>
    <Storyboard x:Key="mouseOverAnimation">
        <DoubleAnimation
            Storyboard.TargetName="myButton"
            Storyboard.TargetProperty="Opacity"
            To="1.0"
            Duration="0:0:0.5" />
    </Storyboard>

    <Storyboard x:Key="mouseLeaveAnimation">
        <DoubleAnimation
            Storyboard.TargetName="myButton"
            Storyboard.TargetProperty="Opacity"
            To="0.5"
            Duration="0:0:0.5" />
    </Storyboard>
</Window.Resources>

<Button Content="Cliccami" Name="myButton" Width="100" Height="30">
    <Button.Triggers>
        <EventTrigger RoutedEvent="Button.Click">
            <BeginStoryboard Storyboard="{StaticResource myAnimation}" />
        </EventTrigger>
        <EventTrigger RoutedEvent="UIElement.MouseEnter">
            <BeginStoryboard Storyboard="{StaticResource mouseOverAnimation}" />
        </EventTrigger>
        <EventTrigger RoutedEvent="UIElement.MouseLeave">
            <BeginStoryboard Storyboard="{StaticResource mouseLeaveAnimation}" />
        </EventTrigger>
    </Button.Triggers>
</Button>
```

In questo esempio, abbiamo creato due nuovi `Storyboard` per gestire l'animazione quando il mouse entra ed esce dal pulsante. Abbiamo usato gli eventi `UIElement.MouseEnter` e `UIElement.MouseLeave` come trigger per attivare queste animazioni.

### Collegare l'Animazione all'Elemento
Ora che abbiamo definito l'animazione, dobbiamo collegarla al nostro pulsante. Questo viene fatto utilizzando il `Trigger` appropriato, che determinerà quando l'animazione verrà attivata.

In questo esempio, utilizzeremo un `EventTrigger` per attivare l'animazione quando il pulsante viene premuto:

```xml
<Button Content="Cliccami" Name="myButton" Width="100" Height="30">
    <Button.Triggers>
        <EventTrigger RoutedEvent="Button.Click">
            <BeginStoryboard Storyboard="{StaticResource myAnimation}" />
        </EventTrigger>
    </Button.Triggers>
</Button>
```

In questo caso, abbiamo aggiunto un `EventTrigger` al pulsante che si attiverà quando il pulsante viene premuto (`RoutedEvent="Button.Click"`). All'interno del `EventTrigger`, abbiamo utilizzato `<BeginStoryboard>` per collegare l'animazione `myAnimation` al pulsante.

### Animazioni basate su Data Binding
Una delle caratteristiche potenti di XAML è la capacità di creare animazioni basate su data binding. Puoi collegare le proprietà dell'animazione ai dati e far sì che l'animazione risponda dinamicamente ai cambiamenti nei dati. Ad esempio, puoi animare un grafico in base ai dati che cambiano nel tempo.

Per esempio, supponiamo di avere un valore numerico che rappresenta il progresso di un'operazione e desideriamo visualizzare un'animazione di riempimento del progresso in base a questo valore:

```xml
<Window.Resources>
    <Storyboard x:Key="progressAnimation">
        <DoubleAnimation
            Storyboard.TargetName="progressFill"
            Storyboard.TargetProperty="Width"
            To="{Binding Progress, ElementName=mainWindow}"
            Duration="0:0:1">
            <DoubleAnimation.EasingFunction>
                <BounceEase Bounces="2" EasingMode="EaseOut"/>
            </DoubleAnimation.EasingFunction>
        </DoubleAnimation>
    </Storyboard>
</Window.Resources>

<Grid>
    <Rectangle x:Name="progressFill" Fill="Blue" Height="30"/>
    <Button Content="Avvia" Click="StartButton_Click"/>
</Grid>
```

Nell'esempio sopra, abbiamo creato un `Rectangle` chiamato "progressFill" che rappresenta il riempimento del progresso. L'animazione modificherà la larghezza del rettangolo in base a un valore "Progress" che è vincolato all'elemento principale (`ElementName=mainWindow`).

### Avviare Animazioni da Codice
Mentre abbiamo visto come avviare animazioni utilizzando trigger nell'XAML, è anche possibile avviare animazioni da codice C#. Questo ti dà il controllo completo sul momento in cui l'animazione inizia.

Ecco come puoi avviare l'animazione "myAnimation" da codice C#:

```csharp
private void StartAnimation()
{
    Storyboard myStoryboard = (Storyboard)this.Resources["myAnimation"];
    if (myStoryboard != null)
    {
        myStoryboard.Begin();
    }
}
```

Puoi chiamare il metodo "StartAnimation" da un gestore di eventi o da qualsiasi altro punto del tuo codice per avviare l'animazione quando desideri.
### Gestire Eventi di Fine Animazione
A volte è utile sapere quando un'animazione è terminata per poter eseguire azioni successive. Puoi farlo gestendo l'evento `Completed` del `Storyboard`. Ad esempio:

```xml
<Storyboard x:Key="myAnimation" Completed="myAnimation_Completed">
    <!-- Definizione dell'animazione -->
</Storyboard>
```

Nel codice C#, puoi definire il gestore per l'evento "Completed":

```csharp
private void myAnimation_Completed(object sender, EventArgs e)
{
    // Il codice da eseguire quando l'animazione è completata
}
```

In questo modo, puoi eseguire azioni specifiche quando l'animazione è finita.

### Utilizzare Risorse Condivise per Animazioni
Quando hai più elementi nell'interfaccia utente che richiedono la stessa animazione, è utile utilizzare risorse condivise per evitare duplicazione del codice. Puoi definire le tue animazioni all'interno delle risorse dell'applicazione e riutilizzarle su più elementi.

Ecco come puoi creare una risorsa condivisa per un'animazione:

```xml
<Application.Resources>
    <Storyboard x:Key="sharedAnimation">
        <DoubleAnimation
            Storyboard.TargetProperty="Opacity"
            To="0.0"
            Duration="0:0:1" />
    </Storyboard>
</Application.Resources>
```

Ora puoi utilizzare questa animazione su qualsiasi elemento nell'applicazione specificando `Storyboard="{StaticResource sharedAnimation}"` nella definizione dell'animazione.

## Creare una animazione con Blend
Tramite Blend per Visual Studio è possibile creare animazioni direttamente tramite l'IDE invece che fare tutto a mano con lo XAML.
Una volta selezionato l'elemento che ci interessa clicchiamo sul pulsante + verde in alto a destra della finestra `Objects and Timeline`.
![[Pasted image 20231020173124.png]]
Una volta creata la storyboard Blend comincerà a registrare, significa che ogni modifica alle property che effettuo viene registrata nell'animazione.
![[Pasted image 20231020173317.png]]
Le animazioni sono strutturate tramite la definizione di keyframe: ==un keyframe è un punto chiave all'interno di un'animazione che rappresenta uno stato specifico dell'oggetto o dell'elemento che sta cambiando nel corso dell'animazione stessa==.
Questo stato può includere posizione, rotazione, scala, colore, opacità o qualsiasi altra proprietà che è soggetta a cambiamenti nel tempo.
In una sequenza di keyframe, il primo keyframe rappresenta il punto di partenza, l'ultimo il punto finale, e tutti gli altri definiscono gli stati intermedi. Questi stati intermedi vengono interpolati dal software o dall'animatore per creare una transizione fluida tra i keyframe.
Per aggiungere un keyframe in Blend premere questo tasto: le property dell'oggetto in quel keyframe sono le property che deve avere quell'oggetto in quel determinato istante temporale.
![[Pasted image 20231020173642.png]]
Per esempio se voglio una animazione che faccia un *fade in*, quindi l'oggetto passi da opacità 0 a opacità 100 in un secondo avrò due keyframe:
* il primo all'istante 0 con definita l'opacità al 0%
* Il secondo all'istante 1 secondo con definita l'opacità al 100%.
![[Pasted image 20231020174221.png]]
Posso creare vari keyframe ognuno con il set di determinate property, come in questo caso
![[Pasted image 20231020174305.png]]
#### Easing function
Selezionando una animazione a destra nelle property comparirà una finestra per la definizione di eventuali Easing Function
![[Pasted image 20231020174439.png]]
