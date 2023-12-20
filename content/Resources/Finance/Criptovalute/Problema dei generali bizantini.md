---
tags:
  - Crypto
  - Definition
  - PublishedPosts
---
Il problema dei generali bizantini è una allegoria per descrivere una classe di problemi in cui può intercorrere un sistema distribuito. In particolare sono quei problemi per cui un insieme di attori del sistema non riescono a sincronizzarsi, portando così al crollo del sistema decentralizzato.

Le [[Blockchain]] sono progettate come sistemi decentralizzati che operano su un [[Distributed Ledger]] mantenuto dai vari nodi della rete.
Affinché il sistema stia in piedi i nodi devono concordare regolarmente sull’attuale stato della blockchain, ovvero devono raggiungere il consenso.

Il problema si pone qualora alcuni nodi possono fallire nella comunicazione di informazioni o perfino agire in modo disonesto.

## Il problema

![[Byzantine_Generals.webp]]

Se tutti i generali decidono di attaccare la battaglia è vinta, se alcuni dicono di voler attaccare ma si ritirano la battaglia è persa

Il Problema dei Generali Bizantini [è stato ideato nel 1982](https://www.microsoft.com/en-us/research/uploads/prod/2016/12/The-Byzantine-Generals-Problem.pdf): supponiamo di avere dei generali bizantini con una propria armata che devono decidere se attaccare o meno una città. Alcuni generali preferiranno attaccare mentre altri preferiranno ritirarsi, il problema è che qualora non siano tutti sincronizzati sull'attacco o sulla ritirata perderanno la battaglia.

La comunicazione tra i generali avviene con un messaggero, che quindi può perdere i messaggi, farli arrivare in ritardo o modificarli a suo piacimento. Inoltre alcuni generali, i traditori, potrebbero inviare un messaggio modificato in base alle proprie preferenze: potrebbero dire ad alcuni membri del gruppo che desiderano fare una cosa e dire agli altri membri del gruppo il contrario.

Un sistema robusto a questo problema deve garantire che:

- Tutti i generali leali devono concordare e agire con lo stesso piano
- Tutti i generali leali non devono seguire il piano errato suggerito dai traditori
- Tutti i generali leali devono trovare un accordo univoco e ragionevole indipendentemente da quello che dicono i traditori e questo accordo deve essere quello corretto per la vittoria

### Esempio

Prendiamo un esempio in cui vi sia un generale e tre tenenti. Assumiamo che il primo voglia inviare il messaggio _"**V**_" ai tre tenenti. In questo algoritmo ogni tenente invia il messaggio ricevuto a tutti gli altri.

**Qualora un tenente ricevesse messaggi diversi, eseguirà quello ricevuto più volte.**

![[1_IVMEKaA35NAM6sjKT_R2aA-1024x411.webp]]

Il generale invia il messaggio "_**V"**_ a tutti ma il tenente 3 è un traditore e invia il messaggio _"**X**"_.

Il generale e il tenente 1 hanno ricevuto solo "_**V"**_ e quindi concordano su tale valore.

Il tenente 2 ha ricevuto V,V,X ma, essendo "_**V"**_ il valore che ha ricevuto più volte, sceglierà "_**V"**_ .

La maggioranza dei nodi concorda quindi sul solo valore "_**V"**_, la rete ha quindi ottenuto il consenso.

Assumiamo ora che il generale sia il traditore per cui invia x,y,z ai tre tenenti. Anche in questo caso il consenso verrà raggiunto.

![[1_FqWerJdheG1CJoMquKKieg-1024x538.webp]]

L1 riceve [x,y,z], come L2 e come L3. Dato che tutti e 3 ricevono gli stessi messaggi l'output della funzione "risultato più frequente" sarà lo stesso, quindi si tratta di un fallback, assumiamo ERROR.

Tutti i nodi della rete concordano quindi sullo stesso valore (ERROR), raggiungendo quindi anche in questo caso il consenso.

In questo algoritmo viene raggiunto il consenso se almeno 2/3 dei nodi della rete è leale. Se più di un terzo dei partecipanti è un traditore non verrà raggiunto il consenso e la battaglia verrà persa.

## Fuori di metafora

In qualsiasi ambiente di elaborazione distribuito, ovvero in un ambiente in cui più utenti, applicazioni, server o altri tipi di nodi compongono l'ambiente, c'è il rischio che delinquenti o attori inaffidabili possano corrompere il sistema.

Per essere affidabile, un ambiente di calcolo distribuito deve essere progettato in modo tale da risolvere il problema dei generali bizantini fornendo ciò che è noto come BFT. E quale sistema distribuito è più calzante per questo esempio di una blockchain?

Ciascun generale rappresenta un nodo del network e i nodi devono raggiungere il consenso sull’attuale stato del sistema, anche se alcuni nodi cercano di corrompere il sistema con azioni malevoli.

Dato che **non c'è alcuna autorità in grado di correggere gli errori, questi non devono mai poter capitare** in modo automatico.

## Byzantine fault tolerance (BFT)

La Byzantine fault tolerance (BFT) è **la proprietà di un sistema per cui questo ultimo riesce a resistere alla classe di fallimenti derivata dal Problema dei Generali Bizantini**. Questo significa che un sistema BFT è in grado di continuare ad operare anche se alcuni nodi falliscono o agiscono in modo disonesto.

Questa proprietà di un sistema distribuito è la _fault tolerance_ più difficile da raggiungere proprio perché non vi sono assunzioni ne sul funzionamento tecnico della rete, ne sul funzionamento "morale" dei nodi.

Nella blockchain il BFT viene raggiunto tramite gli algoritmi di consenso, i quali sono dei meccanismi attraverso cui un network blockchain raggiunge un consenso condiviso e una sincronizzazione su come far procedere la blockchain.

Esistono vari algoritmi di consenso, i due più famosi sono:

- [[Bitcoin#^ca85ef|Proof of Work]]: Per aggiungere blocchi alla blockchain è necessaria potenza computazionale. Un nodo traditore dovrebbe avere almeno il 51% della potenza computazionale di tuti i nodi della blockchain per poter inserire blocchi invalidi, cosa impossibile per blockchain abbastanza grandi.
- [[Proof of Stake (PoS)]]: Per aggiungere blocchi alla blockchain è necessario possedere valuta da impegnare. Più valuta si possiede più si ha la probabilità di poter aggiungere nodi. Se vengono aggiunti nodi malevoli viene persa la valuta impegnata. In questo modo chi ha molti soldi impegnati non ha nulla da guadagnare nel validare nodi malevoli.
