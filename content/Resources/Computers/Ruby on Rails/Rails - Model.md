---
tags:
  - Coding
  - RubyOnRails
---


## 1. Convenzioni
- **Tabelle**: nome plurale con gli underscore che separano le parole
- **Model**: sinfolari con la prima lettera di ogni parola in maiuscolo
- **Chiavi esterne**: `singularized_table_name_id` (esempi `item_id`, `order_id`)

| Model / Class | Table / Schema |
|--------|--------|
|Article|articles|
|LineItem|line_items|
|Deer|deers|
|Mouse|mice|
|Person|people|

## 2. CRUD
#### 2.1 Creazione
Gli oggetti ActiveRecord possono essere creati da un hash (metodo create) oppure posso istanziarli e settare i loro attributi successivamente.
Le seguenti istruzioni sono analoghe
##### 2.1.1 New

```ruby
user = User.new
user.name = "David"
user.occupation = "Code Artist"
user.save
```

##### 2.1.2 Create
```ruby
user = User.create(name: "David", occupation: "Code Artist")
```

#### 2.2 Lettura
```ruby
users = User.all
user = User.first
david = User.find_by(name: 'David')
users = User.where(name: 'David', occupation: 'Code Artist').order(created_at: :desc)
```

#### 2.3 Aggiornamento
Una volta che ho trovato un oggetto, posso aggiornarne gli attributi per poi salvarlo su DB.
```ruby
user = User.find_by(name: 'David')
user.name = 'Dave'
user.save
```
Un modo veloce per eseguire tale operazione è il seguente (esegue già il save)
```ruby
user = User.find_by(name: 'David')
user.update(name: 'Dave')
```
Per aggiornare tutti i record è possibile utilizzare la seguente istruzione
```ruby
user = User.find_by(name: 'David')
user.destroy
```
#### 2.4 Eliminazione
```ruby
user = User.find_by(name: 'David')
user.destroy
```

## 3 Controlli
Con ActivRecord è possibile eseguire dei controlli sui dati **prima** che questi vengano scritti sul database (quindi non vengono lanciate con il metodo `new` ma con il metodo `create` (oppure dopo un quasiasi metodo `save`))

#### 1. Errori
Per verificare che un particolare oggetto abbia o meno superato le validazioni posso usare la funzione `errors[:attribute]` che fornisce un array per tutti gli errori di tale attributo. Deve essere lanciato **dopo** che le validazioni sono partite
```ruby
class Person < ActiveRecord::Base
validates :name, presence: true
end
>> p = Person.new
>> p.errors.messages
>> p.errors.messages
```

### 2.Validazioni

#### 2.1 acceptance
Valida se un **checkbox è stato selezionato quando un form è stato submittato**. Può essere lanciato anche su un attributo che non esiste direttamente nel DB, in tal caso verrà creato un attributo virtuale.
Può essere utilizzato principalmente se l'utente deve accettare i terms of service, confermare la lettura di un qualche testo io simili.
```ruby
class Person < ActiveRecord::Base
validates :terms_of_service, acceptance: true
end
```
#### 2.2 validates_associated
Da utilizzare quando il model ha delle associazioni con altri model che devono essere validate. Quando viene lanciato il save il metodo `valid?` viene chiamato su tutti gli oggetti associati.
```ruby
class Library < ActiveRecord::Base
has_many :books
validates_associated :books
end
```
#### 2.3 confirmation
Da usare quando ho due campi di testo e voglio che entrambi contengano lo stesso valore. Questa validazione crea un attributo virtuale il cui nome è il nome del campo che deve essere conrfermato con un _confirmation alla fine.
Per esempio, se voglio confermare la mail, opero di conseguenza:
```ruby
class Person < ActiveRecord::Base
validates :email, confirmation: true
validates :email_confirmation, presence: true
end
<%= text_field :person, :email %>
<%= text_field :person, :email_confirmation %>
```
#### 2.4 Exclusion
Controlla che l'attributo non sia contenuto in un determinato insieme
```ruby
class Account < ActiveRecord::Base
validates :subdomain, exclusion: { in: %w(www us ca jp) }
end
```
#### 2.5 format
Controlla che l'attributo faccia il match con una espressione regolare
```ruby
class Product < ActiveRecord::Base
validates :legacy_code, format: { with: /\A[a-zA-Z]+\z/,
message: "only allows letters" }
end
```
Se sostituisco il `:with` con il `:without` chiedo che non esegua il match con la regexp.

#### 2.6 inclusion
Controlla che gli attributi siano inclusi in un determinato insieme
```ruby
class Coffee < ActiveRecord::Base
validates :size, inclusion: { in: %w(small medium large),
message: "%{value} is not a valid size" }
end
```

#### 2.7 length
```ruby
class Person < ActiveRecord::Base
validates :name, length: { minimum: 2 }
validates :bio, length: { maximum: 500 }
validates :password, length: { in: 6..20 }
validates :registration_number, length: { is: 6 }
end
```

#### 2.8 numericality
Controlla che l'attributo in questione abbia solo numeri (integer o float). Se voglio solo interi devo aggiungere l'opzione `:only_integer` a true.
```ruby
class Player < ActiveRecord::Base
validates :points, numericality: true
validates :games_played, numericality: { only_integer: true }
end
```

#### 2.9 presence
Controlla che gli attributi indicati **non siano vuoti**.
```ruby
class Person < ActiveRecord::Base
validates :name, :login, :email, presence: true
end
```
Nel caso in cui voglia verificare la presenza di una associazione devo eseguire il seguente codice:
```ruby
class LineItem < ActiveRecord::Base
belongs_to :order
validates :order, presence: true
end
class Order < ActiveRecord::Base
has_many :line_items, inverse_of: :order
end
```
Nel caso in cui voglia validare la presenza di un campo booleano devo eseguire il seguente trucco (in quando `false.blank?` fornisce `true`)
```ruby
validates :boolean_field_name, presence: true
validates :boolean_field_name, inclusion: { in: [true, false] }
validates :boolean_field_name, exclusion: { in: [nil] }
```
#### 2.10 abscence
Verifica che gli attributi indicati siano vuoti
```ruby
class Person < ActiveRecord::Base
validates :name, :login, :email, absence: true
end
```
#### 2.11 uniqueness
Controlla che l'attributo indicato sia l'unico presente su database. **Deve** essere associato ad un vincolo di unicità anche su DB.
```ruby
class Account < ActiveRecord::Base
validates :email, uniqueness: true
end
```

### 3 Validazioni condizionali
Talvolta conviene validare un attributo solo se una determinata condizione è soddisfatta.
```ruby
class Order < ActiveRecord::Base
validates :card_number, presence: true, if: :paid_with_card?

def paid_with_card?
payment_type == "card"
end
end
```
Posso anche usare una stringa a cui sarà fatto l'`eval`.
```ruby
class Person < ActiveRecord::Base
validates :surname, presence: true, if: "name.nil?"
end
```
#### 3.1 Raggruppare istruzioni condizionali
```ruby
class User < ActiveRecord::Base
with_options if: :is_admin? do |admin|
admin.validates :password, length: { minimum: 10 }
admin.validates :email, presence: true
end
end
```

#### 4. Visualizzare gli errori nelle view
Non esistono degli helper prefatti, tendenzialmente si può eseguire una strittura del genere
```erb
<% if @article.errors.any? %>
<div id="error_explanation">
<h2><%= pluralize(@article.errors.count, "error") %> prohibited this article from being saved:</h2>

<ul>
<% @article.errors.full_messages.each do |msg| %>
<li><%= msg %></li>
<% end %>
</ul>
</div>
<% end %>
```

## 4. Callback
Posso associare del codice che deve essere lanciato ad un determinato momento nella vita di un oggetto.
### 4.1 Implementazione
Posso definire la callback con due modalità, o come metodo o come blocco.
##### Metodo
```ruby
class User < ActiveRecord::Base
validates :login, :email, presence: true

before_validation :ensure_login_has_a_value

protected
def ensure_login_has_a_value
if login.nil?
self.login = email unless email.blank?
end
end
end
```
##### Blocco
```ruby
class User < ActiveRecord::Base
validates :login, :email, presence: true

before_create do
self.name = login.capitalize if name.blank?
end
end
```
Di seguite sono elencate tutte le possibili callback disponbili:
#### Creazione
- `before_validation`
- `after_validation`
- `before_save`
- `around_save`
- `before_create`
- `around_create`
- `after_create`
- `after_save`
- `after_commit/after_rollback`

#### Aggiornamento
- `before_validation`
- `after_validation`
- `before_save`
- `around_save`
- `before_update`
- `around_update`
- `after_update`
- `after_save`
- `after_commit/after_rollback`

#### Eliminazione
- `before_destroy`
- `around_destroy`
- `after_destroy`
- `after_commit/after_rollback`

## 5. Migrazioni
Le migrazioni sono utilizzate per gestire lo schema effettivo del DB e i suoi cambiamenti. Le migrazioni sono memorizzate in file e eseguite mediante il comando `rake`.
