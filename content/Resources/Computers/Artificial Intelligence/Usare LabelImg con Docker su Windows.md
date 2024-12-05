L'obiettivo è lanciare `labelimg` su Windows usando [[Docker]] in modo da evitare tutti i problemi di dipendenza e avere un ambiente uguale per tutti.
Per prima cosa è necessario creare un `Dockerfile`:
```dockerfile
# Usa una base leggera con Python e Conda
FROM continuumio/miniconda3:latest

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Installa dipendenze di sistema
RUN apt-get update && apt-get install -y \
    pyqt5-dev-tools \
    libgl1-mesa-glx \
    && apt-get clean

# Copia i file necessari nella directory del container
COPY . /app

# Crea un ambiente Conda per LabelImg
RUN conda install -y pyqt=5 && \
    conda install -y -c anaconda lxml

# Compila le risorse di LabelImg
RUN pyrcc5 -o libs/resources.py resources.qrc

# Imposta un volume per le immagini
VOLUME /data

# Specifica il comando per eseguire LabelImg
ENTRYPOINT ["python", "labelImg.py"]
CMD ["/data/image.png", "/data/classes.txt"]
```

Nella stessa cartella dove si trova il `Dockerfile` mettere il contenuto della repository di `labelimg`.
Modificare il file `labelimg\data\predefined_classes.txt` con le classi predefinite che si pensa di utilizzare, per esempio:
```
0
1
2
```

Ora costruiamo l'immagine Docker:
```bash
docker build -t labelimg .
```
Una volta costruita l'immagine possiamo eseguirne il container. Se le immagini che voglio utilizzare sono in un path locale, tale path dovrà essere montato come volume facendo in modo che punti alla cartella `/data` all'interno del container.
E' necessario che la cartella contenente le immagini di cui voglio fare il labelling contenga un file `classes.txt` con indicate le classi dei file separati da `\n`.
Su Windows non è scontato lanciare finestre grafiche all'interno di Container in quanto sono ambienti virtualizzati. Per risolvere è necessario installare `VcXsrv` indicando come opzioni:
* Multiple windows
* Start no client
* Abilita "Disable access control"

Infine posso avviare `labelimg` con il comando:
   ```bash
   docker run -it --rm -e DISPLAY=host.docker.internal:0 -v C:/path/immagini/locali:/data labelimg   
   ```