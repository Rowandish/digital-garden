---
tags:
  - Dometrain
---

Questa nota prende a piene mani dal corso [Cloud Fundamentals: AWS Services for C# Developers](https://courses.dometrain.com/courses/take/cloud-fundamentals-aws-services-for-csharp-developers).

## Introduzione

Amazon Web Services (AWS) è una piattaforma cloud leader che offre oltre 200 servizi completi per il calcolo, lo storage, il networking, il machine learning e altro ancora.

### Piani gratuiti
1. **Prova gratuita (free trial)**: Questo piano è disponibile per determinati servizi AWS e consente agli utenti di accedere a funzionalità premium per un periodo limitato, di solito 30 o 60 giorni.
2. **12 mesi gratuito (12 months free)**: Questo piano offre accesso gratuito a diversi servizi AWS per i primi 12 mesi dall'iscrizione.
3. **Sempre gratuito (always free)**: questo piano include servizi e risorse che rimangono gratuiti per sempre, indipendentemente dalla durata dell'account.
### Autenticazione

#### Root user
Esiste la possibilità di autenticare il PC come root, quindi qualsiasi azione che viene da tale PC viene effettuata senza chiedere le credenziali come admin (qualsiasi Console Application non necessiterà quindi di alcuna autenticazione).
Questa è la soluzione più comoda ma non è una best practice; può essere utilizzata temporaneamente durante lo sviluppo.
Per farlo fare i seguenti passaggi:
* AWS Console -> Access keys -> Create Access Key
* Scaricare la CLI di AWS
* `aws configure`
* Scrivere l'Access Key ID, il Secret Access Key, la region di riferimento e l'output format (json)

## Servizi
* [[SQS]]
* [[SNS]]
* [[DynamoDB]]
* [[S3]]
* [[Secrets Manager]]
* [[Lambda]]

