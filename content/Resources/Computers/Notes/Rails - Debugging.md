---
tags:
  - Coding
  - RubyOnRails
---


## Viste
Un metodo grezzo per il debugging è printare nelle viste gli oggetti a cui far riferimento, per far ciò esistono due metodi
```ruby
<%= debug @article %>
```

##### debug
Fornisce un tag `<pre>` che renderizzerò l'oggetto usando come formato YAML. 

##### inspect
utile per visualizzare i valori degli oggetti, specialmente hash o array
```ruby
<%= [1, 2, 3, 4, 5].inspect %>
```

## File di log
Può essere utile inoltre salvare informazioni in file di log in runtime, Rails crea dei file di log separati per ogni ambiente.
Nel file ci configurazione dell'ambiente scrivere
```ruby
Rails.logger = Logger.new(STDOUT)
```
verrà scritto un log nella cartella `Rails.root/log/`.

#### Log level
Ad ogni print del log viene associato un livello, i livelli disponbili sono `:debug`, `:info`, `:warn`, `:error`, `:fatal`
Di default, tutti i log sono di livello `:debug` ma è possibile cambiarlo inserendo questa config nell'initializer dell'ambiente.
```ruby
config.log_level = :warn
```

### Scrivere nel log
Per scrivere nel logo posso usare la funzione `logger` in un *controller*, *model* o *mailer*.
```ruby
logger.debug "Person attributes hash: #{@person.attributes.inspect}"
logger.info "Processing the request..."
logger.fatal "Terminating application, raised unrecoverable error!!!"
```

## Byebug
Byebug è una gem che permette di inserire breakpoint nel codice e conseguentemente utilizzare un debugger per risolvere i problemi.
Utilizzando il metodo byebug viene lanciata una shell `byebug` interattiva.
```ruby
class PeopleController < ApplicationController
def new
byebug
@person = Person.new
end
end
```
Quando verrà chiamato tale metodo tutto verrà bloccato e, nella finestra di terminale dove ho lanciato il server, comparirà la shell `byebug`