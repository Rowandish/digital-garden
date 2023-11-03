---
tags:
  - CSharp
  - WPF
---
Talvolta capita che il designer crashi prima di fare la preview di una finestra senza specificarne il motivo, oppure indicando uno stack trace ridotto.
Assumiamo di avere il designer di Rider che crasha.
Per debuggarlo aprire una finestra di Visual Studio senza codice, poi andare su `Debug -> Attach To Process`, cercare `dotnet` e, tra i risultati, selezionare quello che ha qualcosa come `Features.X`.
![[Pasted image 20231025172531.png]]
Premere Attach e andare su Rider.
Aprire il file XAML incriminato. Il debugger attachato in VS dovrebbe crashare e mostrare il vero stack trace.