Come indicato [qui](https://www.reddit.com/r/Piracy/wiki/megathread/) questi sono i passi necessari per avere la massima privacy sul proprio PC.

✔️ **Consigliato:** Usa Firefox + uBlock Origin.

Firefox è il miglior browser non basato su Chromium, e offre eccellenti funzionalità di sicurezza e privacy. Vanta inoltre la migliore compatibilità con uBlock Origin per bloccare efficacemente annunci pubblicitari e altri contenuti web dannosi.

✔️ **Consigliato:** Modifica le impostazioni DNS.

Il DNS può migliorare l'esperienza di navigazione aumentando la velocità e aggirando le restrizioni, poiché il tuo provider di servizi Internet (ISP) di solito offre un DNS predefinito più lento che potrebbe censurare i siti web in base alle proprie preferenze.
Tutorial:
1. Fai clic destro sull'icona della **Rete** o del **WiFi** nella barra delle applicazioni e fai clic sinistro su **Network and internet settings**.    
2. Seleziona la connessione che ti interessa
3. Clicca su **Properties** o **\[nome rete\] properties**    
4. Scorri verso il basso e clicca su **Edit** accanto a _DNS server assignment_.    
5. Apporta le seguenti modifiche:    
    - Cambia **Automatico (DHCP)** in **Manuale**.        
    - Attiva l'interruttore su **On** sotto **IPv4** per cambiare il server DNS.        
    - Inserisci nel campo **DNS preferito**: `9.9.9.9`        
    - Imposta **DNS over HTTPS** su _On (automatic template)_.
    - Inserisci nel campo **DNS alternativo**: `149.112.112.112`
    - Imposta **DNS over HTTPS** su _On (automatic template)_.
6. Clicca su **Salva**.
Per verificare che sia tutto ok aprire Powershell e scrivere
```
Resolve-DnsName -Type txt proto.on.quad9.net.
```
e si deve ottenere questo (importante che ci sia scritto `doh`).
```
Name                           Type   TTL   Section    NameHost
----                           ----   ---   -------    --------
proto.on.quad9.net             CNAME  60    Answer     doh
```

🧲 **Per il Torrenting:** Installa un client torrent affidabile come qBittorrent.

Il client torrent è un programma separato essenziale per scaricare file tramite file torrent, che è un metodo distinto dai download diretti.

🧲 **Per il Torrenting:** Configura una rete VPN come AirVPN o ProtonVPN.

La VPN migliora la privacy e la sicurezza online crittografando la connessione e mascherando l'indirizzo IP, rendendola ideale per il torrenting in quanto protegge la tua identità e consente l'accesso a contenuti con restrizioni.

🧲 **Per il Torrenting:** Collega (Bind) il client torrent all'interfaccia VPN.

Questo assicura che il torrenting avvenga solo quando la VPN è attiva, riducendo a zero le possibilità di una fuga dell'indirizzo IP. Per dettagli più approfonditi, consulta la nostra Guida su Torrenting + VPN.