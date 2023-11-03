---
tags:
  - Git
  - PublishedPosts
---


Questo articolo è una traduzione del [famoso post di Vincent Driessen](http://nvie.com/posts/a-successful-git-branching-model/) che espone un pattern di branching per strutturare nel modo migliore lo sviluppo di un progetto usando git.
![driessen model](http://nvie.com/img/git-model@2x.png)

## 1. Introduzione
Git (e questo modello di lavoro) lavorano bene con questo schema di sviluppo:

![driessen model](http://nvie.com/img/centr-decentr@2x.png)

Questo modello consiste in una repository remota centrale effettiva (chiamata **origin** per convenzione) e ogni sviluppatore esegue dei pull e dei push a tale repository.
Ma oltre ai push-pull centralizzati, ogni sviluppatore può inoltre **eseguire dei pull/push da latri sviluppatori direttamente**: questo può essere utile se, per esempio, due o più sviluppatori stanno lavorando su una grande feature nuova e vogliono collaborare senza pushare sull'*origin* prematuramente.
Tecnicamente questa cosa viene fatta tramite **il setup di un _remote_ alla repository (locale) di un altro sviluppatore**.
Quindi Alice, in questo caso, e definito un **git remote** che punta ala repository di Bob e viceversa.

## 2. I branch principali
Il modello di sviluppo classico prevede due branch principali che non devono essere mai eliminati: **master** e **develop**.
Consideriamo **origin/master** il branch principale remoto, dove **HEAD punta sempre al commit di produzione attuale**.
Consideriamo **origin/develop** il branch dove **HEAD riflette lo stato con gli ultimi sviluppi conclusi che verranno portati in produzione alla prossima release**.
Quando il codice del branch **develop** raggiunge un punto stabile ed è pronto ad essere rilasciato, tuti i cambiamenti devono essere mergiati sul **master** e taggati con un numero di release.

![](http://nvie.com/img/main-branches@2x.png)

Sottolineo che **ogni cambiamento che avviene sul master riflette anche l'aggiornamento della versione in produzione**.
E' prassi comune infatti avere un deploy su server dopo il merge di un qualsiasi branch sul master (Heroku, per esempio, fornisce questo comportamento nativamente).

## 3. I branch di supporto
Parallelamente ai nostri due branch principali, il modello di sviluppo prevede una varietà di **branch di supporto** per permettere uno sviluppo parallelo di codice tra i vari membri del team.
A differenza dei due branch principali, questi **branch hanno sempre vita limitata** e dovranno essere eliminati prima o poi.
Esistono tre tipologie di branch:

- **Feature branches**
- **Release branches**
- **Hotfix branches**

Ogni tipologia di branch ha uno scopo specifico e deve seguire una serie di convenzioni.

### 3.1 Feature branch
Questa tipologia di branch **deve partire dal develop e ritornare nel develop** e può chiamarsi in qualsiasi modo **tranne master, develop, release-\*, o hotfix-\***.

![](http://nvie.com/img/fb@2x.png)

Questi branch sono usati per **sviluppare nuove feature per release a breve o lungo termine**.
Il branch di feature esiste fintantoché la feature di riferimento è in sviluppo, ala fine del suo ciclo di vita questo verrà o mergiato nel develop oppure scartato.
I branch di feature tipicamente **esistono solo nelle repository locali degli sviluppatori, non nell'origin**.

#### 3.1.1 Codice
Per cominciare a lavorare su una nuova feature, creiamo un branch dal develop col seguente comando:
```bash
$ git checkout -b myfeature develop
Switched to a new branch "myfeature"
```
Una volta terminato lo sviluppo eseguo un merge del branch sul develop in modo che siano pronti per la successiva release.
```bash
$ git checkout develop
Switched to branch 'develop'
$ git merge --no-ff myfeature
Updating ea1b82a..05e9557
(Summary of changes)
$ git branch -d myfeature
Deleted branch myfeature (was 05e9557).
$ git push origin develop
```
L'opzione `--no-ff` porta il merge a creare sempre un nuovo commit di merge ed **evita che vengano perse informazioni riguardo l'esistenza storica del branch di feature** raggruppando insieme i commit che hanno portato alla creazione della feature.
![](http://nvie.com/img/merge-without-ff@2x.png)
Se il merge viene eseguito senza l'opzione `--no-ff` è impossibile per git sapere distinguere quali commit sono stati mergiati dal branch di feature e conseguentemente eseguirne un revert è complesso (è necessario andare a leggere i log uno ad uno).

### 3.2 Release branche
Questi branch **partono dal develop e devono essere mergiati o sia sul develop che sul master** e si chiamano, per convenzione, **release-\***.
Questi branch supportano **la preparazione di una nuova release in produzione, permettono piccoli bug-fix e preparano i meta-dati per la release** (numero di versione, date di build...).
Eseguendo tutto questo lavoro su un branch di release, sono libero di utilizzare il branch di develop solo per ricevere le feature per la nostra prossima release.
Il momento giusto per far partire un nuovo branch di release dal develop, è quando **questo riflette quasi totalmente lo stato dell'applicazione per la prossima release**. Tutte le feature che devono essere rilasciate per la prossima versione devono essere mergiate nel develop a questo punto.
E' esattamente alla creazione di un nuovo branch di release che a questa viene assegnata un numero di versione, non prima: il numero di versione da scegliere dovrà seguire le regole di progetto per il cambiamento dei numeri di versione.

#### 3.2.1 Creazione del branch di release
I branch di release sono creati dal branch di develop. Assumiamo, per esempio, che il branch di release abbia versione 1.1.5, alla creazione del branch di release devo decidere se far passare alla versione 1.1.6 o 1.2 o perfino 2.0.
Per esempio, assumiamo di aver scelto 1.2.
```bash
$ git checkout -b release-1.2 develop
Switched to a new branch "release-1.2"
$ ./bump-version.sh 1.2
Files modified successfully, version bumped to 1.2.
$ git commit -a -m "Bumped version number to 1.2"
[release-1.2 74d9424] Bumped version number to 1.2
1 files changed, 1 insertions(+), 1 deletions(-)
```
Dopo aver creato il nuovo branch lanciamo `bump-version.sh`, uno script di Shell che deve essere fatto ad-hoc che cambia i file per riflettere la nuova versione.
La nuova versione è poi commitata.
Questo branch può esistere per un periodo di tempo limitato, durante il quale **possono esservi applicati dei bug-fix** (invece che sul branch di develop) ma **l'aggiunta di nuove feature è assolutamente proibita**.

#### 3.2.2 Concludere un branch di release
Quando lo stato del branch di release è pronto per diventare le release finale, devo eseguire alcune azioni che descrivo qui.
Per prima cosa, il branch di release deve essere mergiato sul master (ricordo che ogni commit sul master **è una nuova release** per definizione).
Successivamente, il commit sul master deve essere taggato per poterlo referenziare in futuro.
```bash
$ git checkout master
Switched to branch 'master'
$ git merge --no-ff release-1.2
Merge made by recursive.
(Summary of changes)
$ git tag -a 1.2
```
Alla fine i cambiamenti effettuati nel branch di release devono essere mergiati indietro nel develop, così anche le release future conterranno tali bug-fix.
```bash
$ git checkout develop
Switched to branch 'develop'
$ git merge --no-ff release-1.2
Merge made by recursive.
(Summary of changes)
```
Per concludere definitivamente le release, il branch di release viene eliminato.
```bash
$ git branch -d release-1.2
Deleted branch release-1.2 (was ff452fe).
```

### 3.3 Hotfix branche
Questi branch sono gli unici branch che **partono dal master e vengono rimergiati sia sul master che sul develop**. Per convenzione si chiamano **hotfix-\***.
I branch di hotfix sono molto simili ai branch di release, con la differenza che non sono previsti.
Questi rispondono ala necessità di risolvere immediatamente ad un problema che si riscontra in produzione (e quindi sul master).

![hotfixbranch](http://nvie.com/img/hotfix-branches@2x.png)

#### 3.3.1 Creazione di un branch di hotfix
La creazione di un branch di hotfix è analoga a quella di un branch di release, con la differenza che questa parte dal master.
```bash
$ git checkout -b hotfix-1.2.1 master
Switched to a new branch "hotfix-1.2.1"
$ ./bump-version.sh 1.2.1
Files modified successfully, version bumped to 1.2.1.
$ git commit -a -m "Bumped version number to 1.2.1"
[hotfix-1.2.1 41e61bb] Bumped version number to 1.2.1
1 files changed, 1 insertions(+), 1 deletions(-)
```
Una volta che ho fixato il bug, eseguo un commit di quanto effettuato:
```bash
$ git commit -m "Fixed severe production problem"
[hotfix-1.2.1 abbe5d6] Fixed severe production problem
5 files changed, 32 insertions(+), 17 deletions(-)
```
#### 3.3.2 Chiusura di un branch di hotfix
Una volta concluso, il branch deve essere mergiato sia sul master che sul develop. La procedura è analoga ai branch di release.
Mergiamo sul master:
```bash
$ git checkout master
Switched to branch 'master'
$ git merge --no-ff hotfix-1.2.1
Merge made by recursive.
(Summary of changes)
$ git tag -a 1.2.1
```
E sul develop:
```bash
$ git checkout develop
Switched to branch 'develop'
$ git merge --no-ff hotfix-1.2.1
Merge made by recursive.
(Summary of changes)
```
L'unica eccezione permessa a questo workflow è che **se esiste un branch di release mentre ho un branch di hotfix, quest'ultimo deve essere mergiato sul branch di release invece che sul develop**.

## 4. SourceTree e Git-flow
Questa parte dell'articolo riguarda SourceTree, un popolare client gratuito per git e mercurial.
Dalla versione 1.5 del progetto è presente un bottone chiamato "git flow" che offre una serie di comandi comodi per implementare quanto descritto nell'articolo precedente.
Infatti permette la creazione del branch di develop qualora non esistesse, ed inoltre fornisce un'interfaccia ad alto livello per creare feature, release e hotfix, con tutte le convenzioni indicate sopra, in maniera automatica.
Per approfondire questo discorso vedi [l'articolo direttamente dal blog di SourceTree](http://blog.sourcetreeapp.com/2012/08/01/smart-branching-with-sourcetree-and-git-flow/).