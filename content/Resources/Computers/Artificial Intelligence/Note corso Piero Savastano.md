Con Python è comodo usare ambienti virtuali, questi sono dei file nascosti all'interno del proprio progetto dove verranno installati pacchetti e dipendenze in modo da non sporcare l'ambiente di sistema ma che ogni progetto abbia il suo ambiente dedicato.
Su PyCharm quando creo un nuovo progetto clicco su `Custom environment -> Generate new -> Virtualenv` per generarne uno nuovo. tutti questi file saranno nella cartella nascosta `.venv` all'interno del progetto.
Per installare un pacchetto il modo più comodo è andare nel terminale di PyCharm e fare `pip install [Nome pacchetto]`.
Per sapere i pacchetti installati posso usare `pip freeze` e per creare il file `requirements.txt` posso fare `pip freeze > requirements.txt`.
