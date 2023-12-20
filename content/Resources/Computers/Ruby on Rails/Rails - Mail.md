---
tags:
  - Coding
  - RubyOnRails
---


Esempio: https://github.com/csm123/puppify

Per inviare una mail è necessario creare un mailer con il seguente comando:
```ruby
$ bin/rails generate mailer UserMailer
create app/mailers/user_mailer.rb
create app/mailers/application_mailer.rb
invoke erb
create app/views/user_mailer
create app/views/layouts/mailer.text.erb
create app/views/layouts/mailer.html.erb
```
I mailer sono concettualmente simili ai controller.
### Mailer
Di seguito il template generato dal generator:
```ruby
class ApplicationMailer < ActionMailer::Base
default from: "from@example.com"
layout 'mailer'
end

class UserMailer < ApplicationMailer
end
```
I mailer hanno metodi chiamati `actions` e usano le viste per strutturare il contenuto della mail e inviarlo allo stesso modo per cui un controller genera un HTML e lo invia al client.
Creiamo un metodo nello `UserMailer` chiamato `welcome_email` che invia una mail di base ad un utente appena si registra:
```ruby
class UserMailer < ApplicationMailer
default from: 'notifications@example.com'

def welcome_email(user)
@user = user
@url = 'http://example.com/login'
mail(to: @user.email, subject: 'Welcome to My Awesome Site')
end
end
```
Questo metodo chiama la vista chiamata `welcome_email.html.erb` in `app/views/user_mailer/` che sarà il template HTML della mail.
Dato che non tutti i client preferiscono la mail HTML è possibile creare un altro template chiamato `welcome_email.text.erb` sempre in `app/views/user_mailer/` con una mail in formato testo.
In questo modo, quando viene chiamato il metodo `mail`, `ActionMailer` noterà i due template (`text` and `HTML`) e genererà una `multipart/alternative` email (la versione HTML e testo verranno inserite insieme, una dopo l'altra).

### Invio
ActionMailer è integrato con ActiveJob, quindi è semplice comunicare l'invio di una mail fuori dal ciclo richiesta-risposta, per esempio posso scrivere:
```ruby
if @user.save
UserMailer.welcome_email(@user).deliver_later
```
Attenzione che il metodo `deliver_later` mette in memoria che la mail deve essere inviata, ma per cominciare ad inviarle come job in background è necessario usare un **queueing backend (Sidekiq, Resque, etc) ?**.
Usando il metodo `deliver_now` la mail viene inviata immediatamente, questo comando è comodo se si vuole fare, per esempio, un `cronjob` come il seguente:
```ruby
class SendWeeklySummary
def run
User.find_each do |user|
UserMailer.weekly_summary(user).deliver_now
end
end
end
```
#### Inviare una mail a più destinatari
Per inviare una mail a più destinatari utilizzo l'attributo `:to` nella classe `AdminMailer`. Tale lista può essere un array di indirizzi email oppure una stringa in cui le mail sono separate da virgola, per esempio il seguente esempio invia una mail a tutti gli admin quando un nuovo utente si è registrato.
```ruby
class AdminMailer < ActionMailer::Base
default to: Proc.new { Admin.pluck(:email) },
from: 'notification@example.com'
def new_registration(user)
@user = user
mail(subject: "New User Signup: #{@user.email}")
end
end
```
Il seguente a tutti gli utenti correlati ad un determinato model in ingresso:
```ruby
class SendNewVideoInCategoryNotificationEmailsJob < ActiveJob::Base
queue_as :default

def perform(video)
category = video.category
subscribers = category.subscriptions.pluck(:user_id)
mail(...)
end
```

#### Inviare una mail con il nome del destinatario
Spesso è più bello vedere come destinatario il nome della persona invece che il suo indirizzo email: per farlo devo formattare l'indirizzo email nel formato: `"Full Name <email>"`.
```ruby
def welcome_email(user)
@user = user
email_with_name = %("#{@user.name}" <#{@user.email}>)
mail(to: email_with_name, subject: 'Welcome to My Awesome Site')
end
```

#### Utilizzare degli URL nelle mail
A differenza dei controller, l'istanza mailer non ha nessun contesto sulla richiesta di invio mail, conseguentemente, per generare degli url, devo fornire esplicitamente il parametro `:host`. Posso configurarlo in `config/application.rb` nel seguente modo:
```ruby
config.action_mailer.default_url_options = { host: 'example.com' }
```
Inoltre non posso usare alcun helper `*_path` all'interno di una mail (che danno il percorso relativo), ma devo utilizzare gli helper `*_url` (che danno il percorso assoluto).
Per esempio, invece di usare
```ruby
<%= link_to 'welcome', welcome_path %>
```
Devo usare
```ruby
<%= link_to 'welcome', welcome_url %>
```
Se uso l'helper chiamato url_for, devo impostare l'opzione only_path: false che assicura che vengano utilizzati url assoluti invece che url relativi (funziona solo se il parametro `:host` è stato configurato correttamente):
```ruby
<%= url_for(controller: 'welcome',
action: 'greeting',
only_path: false) %>
```

### Configurazioni
Affinchè le mail funzionino correttamente devo impostare le configurazioni del server SMTP di invio (attenzione: **mailchimp non invia le mail, serve solo per memorizzare gli indirizzi ed informazioni varie**).
In fase di test posso benissimo utilizzare gmail:

```ruby

config.action_mailer.default_url_options = { :host => 'example.com' }
config.action_mailer.delivery_method = :smtp
config.action_mailer.perform_deliveries = true
config.action_mailer.raise_delivery_errors = false
config.action_mailer.default :charset => "utf-8"
config.action_mailer.smtp_settings = {
address: "smtp.gmail.com",
port: 587,
domain: "example.com",
authentication: "plain",
enable_starttls_auto: true,
user_name: ENV["GMAIL_USERNAME"],
password: ENV["GMAIL_PASSWORD"]
}
```

Per testare in sviluppo conviene disabilitare l'invio effettivo di mail che invece verranno scritte in un file di log con la seguente configurazione:
```ruby
config.action_mailer.default_url_options = { :host => 'localhost:3000' }
config.action_mailer.delivery_method = :smtp
config.action_mailer.perform_deliveries = false
config.action_mailer.raise_delivery_errors = true
config.action_mailer.default :charset => "utf-8"
```

#### SendGrid
Per configurare **SendGrid** basta scrivere la seguente configurazione (in produzione)
```ruby
ActionMailer::Base.smtp_settings = {
:user_name => ENV['SENDGRID_USERNAME'],
:password => ENV['SENDGRID_PASSWORD'],
:domain => 'yourdomain.com',
:address => 'smtp.sendgrid.net',
:port => 587,
:authentication => :plain,
:enable_starttls_auto => true
}
```
Configurazione con Heroku:
```bash
heroku addons:create sendgrid:starter
heroku config:set SENDGRID_USERNAME=appXYZ@heroku.com
heroku config:set SENDGRID_PASSWORD=password
```
Ricorda di configurare le variabili globali anche nel file `.env`.

## Mailchimp

### Introduzione
Mailchimp è un servizio **non** per inviare mail, ma per gestire mailing list (con tutte le comodità del caso, disiscrizione inclusa).
Usando **mailchimp** quindi non ho il classico procedimento **pluck** (`Admin.pluck(:email)`) per capire a chi inviare la mail ma, grazie all'API fornita da Mailchimp, reperisco le liste di persone a cui inviare la mail direttamente da loro.

Per memorizzare indirizzi mail con mailchimp sono necessarie due informazioni
- API Key: per l'autenticazione
- List-Id: Id della lista che deve essere creata con mailchimp

Queste chiavi devono stare in delle variabili di ambiente al di fuori del codice, ottima la gem `dotenv-rails` in cui posso scrivere
```ruby
MAILCHIMP_API_KEY = "123123123123123"
MAILCHIMP_LIST_ID = "148b2f05c5"
```
Attenzione che mailchimp fornisce un solo API key per account, conseguentemente questo viene utilizzato sia in sviluppo che in produzione. Con questo scenario, ogni mail che invii in developmente andrà anche nella mailing list di produzione.
Per evitare questo o **non utilizzare mailchimp in sviluppo** (gmail) oppure utilizzare un secondo account per sviluppo.
Ricorda che quando eseguo un commit in **produzione, .env non funziona** e è encessario settare le variabili di ambiente di heroku direttamente da linea di comando.

### gibbon

Gibbon è un'interfaccia comoda per rails e le API di mailchimp.
Dopo averla installata (`gem "gibbon"`) è possibile configurarlo in `config/initializers/gibbon.rb` con
```ruby
Gibbon::API.api_key = ENV["MAILCHIMP_API_KEY"]
Gibbon::API.timeout = 15
Gibbon::API.throws_exceptions = true
puts "MailChimp API key: #{Gibbon::API.api_key}" # temporary
```
throws_exceptions a true significa che qualsiasi problema di invio mail verrà notificato: va bene in sviluppo ma non in produzione.

Per poter inviare una mail con MailChimp è necessario che la mail dell'interessato sia nella lista mailchimp e questa operazione richiede del tempo che non vogliamo far aspettare all'utente, con Rails 4.21 posso usare gli ActiveJob per eseguire dei task in background.
Il comando
```bash
bin/rails generate job subscribe_user_to_mailing_list
```
genera il seguente template:
```ruby
class SubscribeUserToMailingListJob < ActiveJob::Base
queue_as :default

def perform(*args)
end
end
```
Ora personalizziamo il job in modo tale che accetti un parametro utente e lanciamo l'API *gibbon* per *mailchimp*:
```ruby
class SubscribeUserToMailingListJob < ActiveJob::Base
queue_as :default

def perform(user)
gb = Gibbon::API.new
gb.lists.subscribe({:id => ENV["MAILCHIMP_LIST_ID"], :email => {:email => user.email}, :double_optin => false})
end
end
```
e nel model User creo un metodo in `after_create`.

```ruby
after_create :subscribe_user_to_mailing_list
private
def subscribe_user_to_mailing_list
SubscribeUserToMailingListJob.perform_later(self)
end
```
Quando un utente viene creato, se è presente connessione internet, verrà inviata la mail, altrimenti otterrò l'errore:
```ruby
getaddrinfo: nodename nor servername provided, or not know
```
### Aggiungere ulteriori informazioni alle mail
Il metodo come è ora invia solo la mail a mailChimp, è comodo invece che possa venire inviato anche l'username o altre comode informazioni, per fare questo devo andare nella sezione `Merge fields` nei settings della lista, ed aggiungere i parametri voluti (per esempio `FNAME` e `LNAME`).
Ora modifico il job in modo da inviare anche tali parametri a mailchimp
```ruby
def perform(user)
gb = Gibbon::API.new
gb.lists.subscribe({:id => ENV["MAILCHIMP_LIST_ID"], :email => {:email => user.email}, :merge_vars => {:FNAME => user.first_name, :LNAME => user.last_name}, :double_optin => false})
end
```