Azure offre quattro livelli di scope che consentono di definire loscope delle risorse e delle azioni all'interno dell'ambiente Azure.
Puoi applicare impostazioni di gestione a uno qualsiasi di questi livelli di ambito: ==il livello che selezioni determina l'estensione in cui l'impostazione viene applicata;
I livelli inferiori ereditano le impostazioni dai livelli superiori==.
Ad esempio, quando si applica una [[Azure policy]] alla sottoscrizione, la policy viene applicata a tutti i gruppi di risorse e alle risorse nella sottoscrizione. Quando si applica una policy sul gruppo di risorse, quella policy viene applicata al gruppo di risorse e a tutte le sue risorse. Tuttavia, un altro gruppo di risorse non ha quell'assegnazione di policy.

![[scope-levels.png]]

Questi livelli di scope sono:
1. **Management groups**: L'ambito di gestione è il livello più alto nell'organizzazione di Azure e rappresenta l'intera directory o tenant di Azure. In questo ambito, è possibile creare e gestire più sottoscrizioni Azure, stabilire criteri di gestione, assegnare ruoli di amministratore e monitorare l'utilizzo e le spese complessive dell'organizzazione.
2. **Subscriptions**: L'ambito di sottoscrizione rappresenta una singola sottoscrizione Azure all'interno di un ambiente di gestione. All'interno di un'ambito di sottoscrizione, è possibile creare e gestire risorse come macchine virtuali, servizi di archiviazione, database e così via. È possibile applicare criteri di gestione specifici dell'ambito di sottoscrizione e assegnare ruoli di amministratore che si applicano a tutte le risorse all'interno della sottoscrizione.
3. **Resource groups**: L'ambito di gruppo di risorse è un livello intermedio tra l'ambito di sottoscrizione e l'ambito di risorsa. Un gruppo di risorse è un contenitore logico che tiene insieme le risorse correlate per un'applicazione o un progetto specifico. All'interno di un gruppo di risorse, è possibile gestire le risorse come un'unità coesa e applicare criteri, ruoli e autorizzazioni specifici per quel gruppo di risorse.
4. **Resources**: L'ambito di risorsa rappresenta una singola risorsa all'interno di un gruppo di risorse. Ad esempio, una macchina virtuale, un servizio di archiviazione o un database sono risorse individuali che esistono all'interno di un gruppo di risorse. L'ambito di risorsa definisce l'unità minima di gestione e può essere utilizzato per applicare autorizzazioni e politiche specifiche per quella risorsa.

