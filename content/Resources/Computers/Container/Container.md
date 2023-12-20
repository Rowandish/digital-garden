---
tags:
  - PublishedPosts
---
## Introduzione

Nel modo tradizionale di sviluppo le applicazioni giravano su un determinato server utilizzando tutte le risorse che questo metteva a disposizione. Lanciando _n_ applicazioni sullo stesso server c'è il rischio che una utilizzi le risorse togliendole dalle altre applicazioni.

Per risolvere questo problema sono state inventate le Macchine Virtuali, che permettono di avere delle astrazioni dell'hardware fisico del server in quanto ho _n_ VM sullo stesso server ognuna con il suo sistema operativo e hardware assegnato.

Risolvo quindi il problema del fatto che una applicazione possa impattare le altre sullo stesso server.

I container portano l'astrazione ad un livello ancora maggiore: **==oltre ad astrarre l'hardware sottostante astraggono anche il sistema operativo==**. In questo modo i container offrono lo stesso livello di isolamento, scalabilità e facilità di gestione di una VM ma senza l'overhead di portarsi dietro un sistema operativo: in questo modo risultano leggere e molto più portabili di una VM.

==**La cointanerizzazione (_containerization_ in inglese) è il processo per cui viene "impacchettato" del codice e soprattutto delle sue dipendenze in modo che possa funzionare su ogni infrastruttura.**==

Il codice viene sviluppato su uno specifico ambiente di sviluppo (distro, dipendenze installate…); quando questo viene spostato in un nuovo ambiente è facile avere errori o bug in quanto l'ambiente non è lo stesso e i pacchetti possono o non esistere o avere comportamenti diversi.

La _containerization_ elimina il problema unendo il codice con un relativo file che ne specifica eventuali file di configurazione, librerie e dipendenze.

==In questo modo il software è all'interno di un "container" che lo rende indipendente dal sistema operativo o, in generale, dall'ambiente in cui viene lanciato e conseguentemente portable e bug-free==.

La _containerization_ permette di quindi di scrivere una applicazione una sola volta e poi poterla farla girare ovunque, con tutti i vantaggi del caso.

## Virtualization e Containerization

Spesso i container sono paragonati alle macchine virtuali (VM) in quanto entrambi permettono di lanciare varie tipologie di software (basati su Windows o Linux) di essere lanciati su un determinato ambiente.

**La virtualizzazione permette che più sistemi operativi e software possano girare contemporaneamente su un singolo PC**, per esempio su un singolo server posso far girare varie VM con sistemi operativi diversi o diverse versioni dello stesso.

Ogni applicazione e i suoi relativi file, librerie, dipendenze e sistema operativo sono impacchettati in una VM. Per fare questo anche l'hardware fisico viene virtualizzato e incapsulato nella VM.

Come descritto nell'introduzione la _containerization_ utilizza un approccio diverso: ==**oltre a virtualizzare l'hardware sottostante i container virtualizzano anche il sistema operativo** in modo che ho sì un pacchetto con tutto il software e le sue dipendenze ma senza una copia dell'SO==.

L'assenza di questo ultimo porta ai container ad essere leggeri, veloci e flessibili.

## Docker

Dato che il container non possiede copie del sistema operativo (a differenza di una VM) deve girare sul sistema operativo della piattaforma dove risiede: su questo ultimo deve invece essere installato un **_runtime engine_ che è l'applicazione che permette di far comunicare il container con questo**.

**Il _runtime engine_ più famoso è [Docker](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi8-Myo6tL2AhXBvKQKHQA_B18QFnoECBEQAQ&url=https%3A%2F%2Fwww.docker.com%2F&usg=AOvVaw3p9e1qPvdfjCrUwPYAhUlS)**, sistema open source del 2013 utilizzato in tutto il mondo.

E' formato da:
* **Dockerfile**: file che descrive le dipendenze
* **Image**: snapshot di una installazione, è effettivamente l'installer che contiene tutti i file
* **Container**: parte dall'immagine ma possono averne tanti a partire dalla stessa image, sono le installazioni. Ogni container è isolato e non sa dell'esistenza delle altre. 

## Container image

Quando un container viene lanciato, utilizza un proprio file system indipendente dal file system del sistema. Questo file system interno è fornito dal _container image_ che conseguentemente deve contenere tutto ciò che è necessario all'applicazione per funzionare quindi tutte le sue dipendenze, file di configurazione, script, binari e così via.

L'immagine inoltre contiene anche altre configurazioni del container come le variabili d'ambiente, i comandi da lanciare e eventuali altri metadata.

Per poter fornire questa sorta di "file system interno" Docker utilizza una versione estesa del comando [[chroot]] in quanto questo ultimo non permette di fornire il grado di isolamento del file system delle container image.

## Vantaggi

La _containerization_ offre numerosi vantaggi agli sviluppatori:

- **Portabilità**: un container è un pacchetto software che è indipendente dal sistema operativo e conseguentemente può girare su qualsiasi sistema e piattaforma;
- **Velocità**: i containers sono strumenti leggeri e veloci in quanto non c'è alcun sistema operativo da bootare; il delivery è semplice ed immediato;
- **Isolamento**: ogni container gira indipendentemente dagli altri eventuali container e un fail su uno non influenza gli altri.
- **Sicurezza**: il fatto che i container sono isolati tra di loro permette di ridurre gli effetti di un eventuale codice malevolo.

## Quando usare i container

I container possono essere usati per diversi utilizzi, vediamo i principali:

- **Microservizi**: essendo piccoli e leggeri sono perfetti per costruire una architettura a microservizi dove l'applicazione è formata da molti piccoli servizi "_loosely coupled"_ quindi dall'accoppiamento minimo;
- **DevOps**: Il termine DevOps è una combinazione di "_Development_" (sviluppo) e "_Operations_" (operazioni) che rappresenta un insieme di idee e procedure per fornire servizi efficienti e di alta qualità utilizzano infrastrutture moderne e applicazioni cloud native. La combinazione di una architettura a microservizi utilizzando container è la base per i team che utilizzano la modalità _DevOps_ per sviluppare e lanciare i propri software.
- **Multicloud**: dato che un container può girare ovunque, da un server ad un laptop a un servizio cloud sono ideali per scenari _multicloud_ dove le aziende lavorano sia con i propri data-center insieme a servizi cloud sulla rete;
- **Refactor e modernizzazione**: quando si ha una applicazione legacy che si vuole portare sul cloud spesso il primo passo e containerizzarla.

## Container orchestration - Kubernetes

Per concludere l'articolo un accenno a come gestire numerosi container in una architettura moderna basata sul cloud.

Con l'aumentare della complessità del sistema si dovrà gestire la centinaia di container diversi: per farlo al meglio si utilizzano software di _container orchestration_ che hanno lo scopo di gestire tutto il ciclo di vita, le risorse, il load balancing e quant'altro di una serie di container.

[Kubernetes](https://kubernetes.io/it/) è un progetto open source di google del 2014 che è la piattaforma di _container orchestration_ più famosa, ormai è infatti diventato uno standard.

Kubernetes è un software per l'automazione del deployment, scalabilità, e gestione di applicativi in containers.

Tramite dei file YAML che descrivono la configurazione desiderata dei container, Kubernetes gestisce lo stato dei container, il deploy, il reboot in caso di fail, il load balancing, lo scaling, il deploy e così via.
