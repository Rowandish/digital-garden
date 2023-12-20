---
tags:
  - Crypto
  - Definition
  - PublishedPosts
---


## Introduzione

Distributed Ledger significa letteralmente registro distribuito e, di fatto, è un database contenente delle **informazioni che è sincronizzato e distribuito in più nodi su una rete peer-to-peer, senza che vi sia un nodo o ente centrale che fa da garante**.
Ogni nodo possiede quindi una copia dell'intero database (l'informazione è quindi volutamente ridondante).
Quando un nodo effettua una modifica, tale modifica viene riflessa a tutti i nodi della rete qualora vengano rispettate le regole imposte dalla stessa rete. In italiano sarebbe più corretto definirli "libro mastro" in quanto il database contiene la lista delle transazioni effettuate dalla sua creazione ad oggi.

Questa tecnologia è il contrario del classico "Centralized ledger" dove ho un singolo database che contiene tutte le informazioni, database gestito da un ente centrale. Il fatto che il database sia unico e centralizzato è, di fatto, un single point of failure e permette a chi controlla il database (o a chi lo attacca) di gestire tutte le informazioni ivi contenute a piacimento.

Utilizzando quindi una tecnologia a registro distribuito non ho alcuna autorità centrale che autorizza e valida le transazioni ma il sistema si autosostiene peer-to-peer automaticamente.

## Algoritmi di consenso

La chiave per fa funzionare un distributed ledger è che vi deve essere una procedura, condivisa da tutti i nodi, per poter effettuare delle modifiche "autorizzate" al database. Questa procedura deve poter impedire a utenti malevoli di effettuare modifiche non autorizzate. Tale algoritmo è definito **algoritmo del consenso**, ed è la chiave sul funzionamento di ogni DLT.

I sistemi a DL si distinguono per tre caratteristiche fondamentali:

- Tipologia di rete
    - **Permissioned**: reti che possono avere una "proprietà"; quando un nuovo record viene aggiunto la sua approvazione è vincolata solo ad un numero limitato di attori, definiti trusted. E' possibile inoltre definire regole per l'accesso e la visibilità di tutti i dati;
    - **Permissionless**: reti senza una proprietà effettiva e sono quindi concepite per non poter essere controllabili e censurabili. Nessun ente può impedire una transazione una volta conquistato il consenso della rete.
- Meccanismo di consenso
    - [[Bitcoin#^ca85ef|Proof of Work]]
    - [[Proof of Stake (PoS)]]
    - Sistemi a votazione (tipica dei sistemi permissioned dove pochi nodi detengono il potere di modificare l'informazione)
    - [Hashgraph](https://en.wikipedia.org/wiki/Hashgraph)
- Struttura del registro
    - [[Blockchain]]:
    - Grafico diretto aciclico

## Blockchain

La blockchain è una tipologia di struttura del registro, in particolare esso è strutturato come una catena di blocchi contenenti le transazioni e il consenso è distribuito su tutti i nodi della rete. Il suo contenuto una volta scritto tramite un processo normato, non è più né modificabile né eliminabile, a meno di non invalidare l'intero processo.
