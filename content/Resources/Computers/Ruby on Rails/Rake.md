---
tags:
  - Coding
  - RubyOnRails
---


Esempione: https://github.com/novelys/production_chain/blob/master/lib/production_chain/tasks/db.rake


Rake significa "ruby make" e sostituisce l'utility unix `make` e utilizza un `Rakefile` o un file `.rake` per costruire una lista di task da eseguire.
Con l'istruzione `rake --tasks` ottengo tutti i tak che posso eseguire su una determinata directory

##### 1.1 about
Fornisce informazioni generali sulla versione di Ruby, RubyGems, Rails e i suoi sottocomponenti...
```ruby
rake about
```
##### 1.2 assets
```ruby
rake assets:precompile # precompila gli assets
rake assets:clean # rimuove gli assets compilati
rake assets:clobber #elimina tutto il contenuto di public/assets

```
##### 1.3 db
```ruby
rake db:drop #droppa il DB
rake db:create #crea il DB
rake db:migrate #lancia le migration pendenti
rake db:seed #lancia il seed.rb
rake db:setup #crea il DB, lo schema e lo inizializza con i seed
rake db:reset #esegue il drop e il setup
rake db:schema:dump #aggiorna il file db/schema.rb
rake db:rollback #rollback dell'ultima migrazione
rake db:rollback STEP=3 # rollback delle ultime 3 migrazioni
rake db:migrate:redo #esegue un rollback e riesegue la migration
rake db:migrate:redo STEP=3 #analogo ma con 3 migration

```

##### 1.4 doc
```ruby
rake doc:app # documentazione per l'app in doc/app
rake doc:guides #guida per l'app in doc/guides
rake doc:rails # documentazione per l'API in doc/api
```
##### 1.5 notes
Cerca nel codice per dei commenti che cominciano con FIXME, OPTIMIZE o TODO e fornisce un output leggibile

##### 1.6 routes
elenco delle route
##### 1.7 tmp
La cartella tmp creata da Rails e dove vengono memorizzati file temporanei come le sessioni, PID o azioni in cache.
```ruby
rake tmp:cache:clear # clears tmp/cache.
rake tmp:sessions:clear # clears tmp/sessions.
rake tmp:sockets:clear # clears tmp/sockets.
rake tmp:clear # clears all the three: cache, sessions and sockets.
rake tmp:create # creates tmp directories for sessions, cache, sockets, and pids.
```

##### 1.8 stats
Elenco di varie statistiche del codice
##### 1.9 secret 
Fornisce una chiave pseudo casuale che può essere usata come tok

## Task personalizzati
I task personalizzati hanno estensione `.rake` e sono in `Rails.root/lib/tasks` e si possono creare con un generator nel seguente modo:
```ruby
rails generate task
```
#### Task che dipendono da altri
```ruby
task :turn_off_alarm do
puts "Turned off alarm. Would have liked 5 more minutes, though."
end

task :make_coffee do
cups = ENV["COFFEE_CUPS"] || 2
puts "Made #{cups} cups of coffee. Shakes are gone."
end

task :ready_for_the_day => [:turn_off_alarm, :make_coffee] do
puts "Ready for the day!"
end
```
Chiamando il task `ready_for_the_day` verranno chiamati tutti gli altri taks
```bash
=> rake ready_for_the_day
Turned off alarm. Would have liked 5 more minutes, though.
Made 5 cups of coffee. Shakes are gone.
Ready for the day!
```
Al task chiamato `make_coffee` posso passare parametri come **ENV**
```bash
=> rake COFFEE_CUPS=5 make_coffee
Made 5 cups of coffee. Shakes are gone.
```
#### Invocare un task dentro un altro
Uso il comando `invoke`
```ruby
task :make_coffee do
Rake::Task['morning:make_coffee'].invoke
puts "Ready for the rest of the day!"
end
```
#### parametri in ingresso
```ruby
task :task_name, [:arg_1] => [:pre_1, :pre_2] do |t, args|
end
```
#### namespace
```ruby
namespace :db do
desc "This task does nothing"
task :nothing do
end
end
```
Per esempio, vogliamo creare un task che invia una mail a tutti gli utenti che hanno un account che sta per scadere
```ruby
namespace :accounts do
desc "Email expiring accounts to let them know"
task :email_expiring => :environment do
date = ENV['from'] ? Date.parse(ENV['from']) : Date.today
Account.notify_expiring(date)
end
end
```