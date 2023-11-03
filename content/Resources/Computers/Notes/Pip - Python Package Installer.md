---
tags:
  - Python
---
Il  PIP è il principale sistema di gestione dei pacchetti per Python.
Con PIP, gli sviluppatori possono installare, aggiornare e gestire librerie e pacchetti Python in modo semplice ed efficiente.
Con PIP, è possibile:

- Installare librerie e pacchetti Python da repository remoti o locali.
- Aggiornare librerie esistenti all'ultima versione.
- Rimuovere librerie che non sono più necessarie.
- Gestire l'ambiente virtuale (con `virtualenv`) per mantenere isolati i progetti Python.

Per le differenze con Conda vedi [[Conda#^a0d717|PIP Vs Conda]]
## Installazione di PIP

Se si sta usando una versione recente di Python (3.4 o successiva), PIP è già installato di default. È possibile verificare se PIP è installato eseguendo il seguente comando:

```bash
pip --version
```

Se PIP non è installato, è possibile farlo facilmente utilizzando il metodo appropriato per il sistema operativo in uso. Ad esempio, su molte distribuzioni Linux, è possibile utilizzare `apt` o `yum`, mentre su macOS è possibile utilizzare `brew` o `port`. Su Windows, è possibile utilizzare l'installer di Python.

## Utilizzo di PIP

Ecco alcune delle operazioni più comuni eseguite con PIP:

### 1. Installazione di una Libreria
Per installare una libreria o un pacchetto Python da PyPI (Python Package Index), utilizzare il comando `pip install` seguito dal nome del pacchetto:

```bash
pip install nome_pacchetto
```

Esempio:

```bash
pip install requests
```

### 2. Installazione di una Versione Specifica

È possibile specificare una versione specifica del pacchetto da installare. Ad esempio:

```bash
pip install nome_pacchetto==1.2.3
```

### 3. Aggiornamento di una Libreria

Per aggiornare una libreria alla sua ultima versione, utilizzare il comando `pip install --upgrade` seguito dal nome del pacchetto:

```bash
pip install --upgrade nome_pacchetto
```

### 4. Rimozione di una Libreria

Per rimuovere una libreria, utilizzare il comando `pip uninstall` seguito dal nome del pacchetto:

```bash
pip uninstall nome_pacchetto
```

### 5. Visualizzazione delle Librerie Installate

Per visualizzare un elenco delle librerie Python installate, è possibile utilizzare il comando `pip list`:

```bash
pip list
```

### 6. Creazione di un File Requirements

Un file requirements è un modo per elencare tutte le librerie necessarie per un progetto specifico. È possibile generare un file requirements a partire da un ambiente virtuale o da un progetto esistente utilizzando il comando `pip freeze`:

```bash
pip freeze > requirements.txt
```

### 7. Installazione di Librerie da un File Requirements

È possibile installare tutte le librerie elencate in un file requirements utilizzando il comando `pip install -r`:

```bash
pip install -r requirements.txt
```

### 8. Creazione di un Ambiente Virtuale

Un ambiente virtuale è un ambiente isolato in cui è possibile installare librerie specifiche per un progetto senza interferire con il sistema globale. Per creare un ambiente virtuale, utilizzare il modulo `venv`:

```bash
python -m venv nome_ambiente
```

Attivare l'ambiente virtuale (su Linux/macOS):

```bash
source nome_ambiente/bin/activate
```

### 9. Disattivazione di un Ambiente Virtuale

Per disattivare un ambiente virtuale, basta eseguire il comando:

```bash
deactivate
```

## 10. Uso di PIP in un Progetto

Quando si lavora su un progetto Python, è possibile specificare le librerie necessarie all'interno di un file `requirements.txt` e poi utilizzare PIP per installarle all'interno di un ambiente virtuale specifico per il progetto. Ciò consente di mantenere un ambiente pulito e isolato per ciascun progetto, con tutte le librerie richieste.

Ecco un esempio di come utilizzare PIP in un progetto:

1. Creare un ambiente virtuale per il progetto:

```bash
python -m venv venv
```

2. Attivare l'ambiente virtuale:

```bash
source venv/bin/activate
```

3. Creare un file `requirements.txt` con le librerie necessarie:

```
Flask==2.0.1
requests==2.26.0
```

4. Installare le librerie all'interno dell'ambiente virtuale:

```bash
pip install -r requirements.txt
```

5. Quando si è finito di lavorare sul progetto, disattivare l'ambiente virtuale:

```bash
deactivate
```

