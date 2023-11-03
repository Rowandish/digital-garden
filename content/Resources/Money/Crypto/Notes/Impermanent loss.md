---
tags:
  - Crypto
  - Definition
---


![[impermanent-loss-chart-1024x575-1.webp]]

Fornendo liquidità a dei pool con due (o più) monete posso soffrire di **impermanent loss, che è una perdita ipotetica che viene calcolata in percentuale rispetto all'holdare i due asset** con la stessa proporzione (50/50).

La perdita è proporzionale alla volatilità ai due asset del pool tra loro, in particolare alla differenza in percentuale tra il prezzo dei due asset dal momento in cui metto liquidità al momento in cui la tolgo.

Per esempio se vado in un pool con due token, A e B. A vale 1 e B vale 100. Se quando ritiro la differenza tra i valori tra i 2 token è ancora 100 a 1 non ho impermanent loss. Per esempio se A vale 2 e B vale 200 e così via.

Qualora invece uno dei due token aumenti o diminuisca il suo prezzo mentre l'altro rimane costante ho impermanent loss.

Questo accade in quanto **lo smart contract vuole avere sempre nel pool il 50% della moneta A e il 50% della moneta B, quindi in caso, per esempio, di un drastico aumento di prezzo del token A lo smart contract andrà automaticamente a venderlo per comprare il token B in modo che la proporzione sia sempre 50 e 50**. Quando vado a ritirare i fondi lo smart contract mi fornirà sempre i token in proporzione 50 e 50, indipendentemente dalla loro variazione di valore.

Non ho impermanent loss con il lending, in quanto ho una sola moneta, oppure quando effettuo il pool di [[Stablecoin]], in quanto queste, per definizione, mantengono lo stesso valore nel tempo.

Un ulteriore modo per non avere impermanent loss sono i pool di token rappresentanti la stessa moneta, per esempio Luna con bLuna.

Ovviamente la perdita si realizza solo ed esclusivamente al momento del ritiro dei fondi, fino a quel momento la perdita è solo virtuale e non pratica.

Esistono vari siti che permettono di calcolare l'impermanent loss, uno di questi è: [https://decentyields.com/impermanent-loss-calculator](https://decentyields.com/impermanent-loss-calculator)