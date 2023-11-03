---
tags:
  - Coding
  - RubyOnRails
---


Active Job è un framework per dichiarare dei job e farli andare in background; tutto quello che può essere diviso in piccole unità di lavoro da far eseguire in differita rispetto all'utente, può essere fatto con gli Active Job.
ActiveJob è un framework che sta sopra gli effettivi motori che fanno partire i job, come Delayed Job e Resque in modo da non dover preoccuparsi della differenza tra le varie possibilità.
## Creare un job
Active Job fornisce un generatore per creare i job:
```bash
$ bin/rails generate job guests_cleanup
create app/jobs/guests_cleanup_job.rb
```
Posso creare un job che viene lanciato su una specirfica coda:
```bash
$ bin/rails generate job guests_cleanup --queue urgent
```

## Mettere in coda un job
##### Il job viene eseguito appena la coda è libera
```ruby
MyJob.perform_later record
```
##### Il job verrà eseguito domani a mezzogiorno
```ruby
MyJob.set(wait_until: Date.tomorrow.noon).perform_later(record)
```
##### Il job verrà eseguito fra una settimana
```ruby
MyJob.set(wait: 1.week).perform_later(record)
```

## Backend per gestire le code di processi
Esistono vari gestori di job in coda (Sidekiq, Resque, Delayed Job...) per utilizzarli, dopo averne installato la gem, basta andare nelle configurazioni
```ruby
module YourApp
class Application < Rails::Application
config.active_job.queue_adapter = :sidekiq
end
end
```

## Code
Molti gestori permettono multiple code e posso assegnare che un job sia su una specifica coda:
```ruby
class GuestsCleanupJob < ActiveJob::Base
queue_as :low_priority
#....
end
```
E' possibile inserire una stringa che sia un prefisso al nome di tutte le code:
```ruby
class Application < Rails::Application
config.active_job.queue_name_prefix = Rails.env
end
```
Ora quindi con il comando `queue_as :low_priority` metterà il job nella coda `production_low_priority` in produzione e `staging_low_priority` in staging.

Posso passare anche un block al comando queue_as, come nel seguente esempio:
```ruby
queue_as do
video = self.arguments.first
if video.owner.premium?
:premium_videojobs
else
:videojobs
end
end
```
Ovviamente poi è necessario configurare coloro che lanciano i job perchè "ascoltino" le code con il nome corretto.

## Callback
Posso lanciare delle callback mentre il job sta per essere lanciato, le callback disponibili sono:
- `before_enqueue`
- `around_enqueue`
- `after_enqueue`
- `before_perform`
- `around_perform`
- `after_perform`

## Exceptions
ActiveJob fornisce un modo comodo per gestire le eccezioni che si possono verificare durante il lancio del job:
```ruby
class GuestsCleanupJob < ActiveJob::Base
queue_as :default

rescue_from(ActiveRecord::RecordNotFound) do |exception|
end

def perform
end
end
```