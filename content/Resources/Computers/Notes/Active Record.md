---
tags:
  - Coding
  - RubyOnRails
---


### find(id)
Cerca l’oggetto per la sua chiave primaria

| Sintassi | Query |
|--------|--------|
|`client = Client.find(10)`|`SELECT * FROM clients WHERE (clients.id = 10)`|
|`client = Client.find([1, 10])`|`SELECT * FROM clients WHERE (clients.id IN (1,10))`|

### take(n)

Limita i risultati della query a n elementi

| Sintassi | Query |
|--------|--------|
|`client = Client.take(2)`|`SELECT * FROM clients LIMIT 2`|

### first

Prende il primo elemento del record

| Sintassi | Query |
|--------|--------|
|`client = Client.first`|`SELECT * FROM clients ORDER BY clients.id ASC LIMIT 1`|
|`client = Client.first(3)`|`SELECT * FROM clients ORDER BY clients.id ASC LIMIT 3`|

### last

Prende i'ultimo elemento del record

| Sintassi | Query |
|--------|--------|
|`client = Client.last`|`SELECT * FROM clients ORDER BY clients.id DESC LIMIT 1`|
|`client = Client.last`|`SELECT * FROM clients ORDER BY clients.id DESC LIMIT 3`|

### find_by_string

Trova il primo record seguendo l’attributo indicato in string. 

| Sintassi | Query |
|--------|--------|
|`Client.find_by first_name:'Lifo'`|`Client.where(first_name:'Lifo').take`|

### find_each

Trova un insieme di record e fornisce ogni record come un model singolo. Questo e il metodo successivo sono da usare solo quando il numero di risultati è talmente grande che satura la ram. Altrimenti conviene usare il normale each


### find_in_batches

Trova un insieme di record e considera l’intero risultato come un array di modelli da considerare in blocco

### Where

Condizione where delle normali SQL, ritorna un array di ActiveRecord.

| Sintassi | Query |
|--------|--------|
|`Client.where("orders_count = ? AND locked = ?", params[:orders], false)`|Possibilità di aggiungere elementi alla condizione con il ?|
|`Client.where("created_at >= :start_date AND created_at <= :end_date",{start_date: params[:start_date], end_date:params[:end_date]})`|Parametri condizionali espliciti per una maggiore facilità di lettura|
|`Client.where(locked: true)`|Se locked è un attributo di Client, questa sintassi è la più consigliata per una maggiore leggibilità|
|`Client.where(created_at: (Time.now.midnight - 1.day)..Time.now.midnight)`|Posso specificare un range di valori tramite i ..|
|`Client.where(orders_count: [1,3,5])`|`SELECT * FROM clients WHERE (clients.orders_count IN (1,3,5))`|
|`Article.where.not(author: author)`|Esclusione. where con nessun parametro e concatenato subito il not|


### Order

Ordina i record ottenuti dal database

| Sintassi | Query |
|--------|--------|
|`Client.order(created_at: :desc)`|``|

### Select

Seleziona un sottoinsieme specifico di campi

| Sintassi | Query |
|--------|--------|
|`Client.select(:name)`|`SELECT name FROM clients`|

### Distinct

Rimuove i duplicati dalla query

| Sintassi | Query |
|--------|--------|
|`Client.select(:name).distinct`|`SELECT DISTINCT name FROM clients`|

### Limit

Specifica il numero di record che voglio ottenere

| Sintassi | Query |
|--------|--------|
|`Client.limit(5)`|`SELECT * FROM clients LIMIT 5`|

### Offset

Specifica il numero di record da skipper prima di cominciare a fornire risultati

| Sintassi | Query |
|--------|--------|
|`Client.limit(5).offset(30)`|`SELECT * FROM clients LIMIT 5 OFFSET 30`|

### Group

Raggruppa gli elementi di una query secondo un determinato parametro

| Sintassi | Query |
|--------|--------|
|`Order.select("date(created_at), sum(price)”).group("date(created_at)")`|Fornisce un array di oggetti Order, uno per ogni data di creazione dello stesso|
|`Order.group(:status).count # => { 'awaiting_approval' => 7, 'paid' => 12 }`|Fornisce il numero di elementi raggruppati secondo un determinato attributo del model|

### Having

Permette di selezionare delle condizioni da applicare al model raggruppato da GROUP BY

| Sintassi | Query |
|--------|--------|
|`Order.select("date(created_at), sum(price)”).group("date(created_at)").having("sum(price) > ?", 100)`|Fornisce un array di oggetti Order, uno per ogni data di creazione dello stesso ma solo quelli che hanno somma di prezzo maggiore di 100|

### Join

Solo nel caso di inner join (altrimenti usare Squeel) posso specificare il nome delle relazioni definite nel model come una shortcut 

|Classe| Sintassi | Query |
|--------|--------|--------|
|`Category has_many :articles`|`Category.joins(:articles)`|Fornisce un oggetto Category per tutte le categorie CON almeno un articolo (per avere anche quelle senza articoli fare un OUTER JOIN). Se più di un articolo ha la stessa categoria avrò risultati duplicati, se voglio risultati unici appendere la funzione .uniq|
|`Article belongs_to :category has_many :comments has_many tags`|`Article.joins(:category, :comments)`|Fornisce tutti gli articoli che hanno una categoria ed almeno un commento|
|`class Comment belongs_to :article has_one :guest class Guest belongs_to :comment`|`Article.joins(comments: :guest)`|Fornisce tutti gli articoli che hanno un commento fatto da un guest (notare che ho un solo parametro di ingresso)|
|`class Tag belongs_to :article`|`Category.joins(articles: [{ comments: :guest }, :tags])`|Fornisce tutte le categorie che hanno almeno un articolo con almeno un commento fatto da un guest e i tag dell’articolo in questione|

