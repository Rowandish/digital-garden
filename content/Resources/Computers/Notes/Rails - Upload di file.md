---
tags:
  - Coding
  - RubyOnRails
---


Le gem principale per l'upload di file è `CarrierWave`
Per prima cosa è necessario creare un oggetto `Uploader`:
```ruby
rails generate uploader Avatar
```
che crea il seguente file
```ruby
class AvatarUploader < CarrierWave::Uploader::Base
storage :file
end
```
**CarrierWave** fornisce un metodo `store` per lo storage permanenete e un metodo `cache` per lo storage temporaneo.
Una volta ceh è stato definito un uploader come AvatarUploader, posso salvare un file (o reperirlo) con le seguenti istruzioni:
```ruby
uploader = AvatarUploader.new
uploader.store!(my_file)
uploader.retrieve_from_store!('my_file.png')
```

## Configurazione del model
Devo agginugere una colonna al model in cui voglio inserire l'uploader:
```ruby
add_column :users, :avatar, :string
```
e poi, nella dichiarazione del model, scrivo:
```ruby
class User < ActiveRecord::Base
mount_uploader :avatar, AvatarUploader
end
```
Ora posso memorizzare i file assegnandoli come attributi del model:
```ruby
u = User.new
u.avatar = params[:file]
u.save!
```

## Estensioni ammesse
Per poter permettere file solo con determinate estensioni basta aggiungere il metodo `extension_white_list` all'uploader
```ruby
def extension_white_list
%w(jpg jpeg gif png)
end
```

## Versioni per il file
Voglio poter permettere varie versioni dello stesso file, con caratteristiche diverse (un classico esempio sono le thumbnail).
Per esempio, vogliamo che un'immagine caricata non sia mai più larga di 800x800, inoltre creo automaticamente una thumb croppata a 200x200
Aggiorno l'uploader così:
```ruby
class MyUploader < CarrierWave::Uploader::Base
include CarrierWave::RMagick
process :resize_to_fit => [800, 800]
version :thumb do
process :resize_to_fill => [200,200]
end
end
```
Ottengo quindi:
```ruby
uploader = AvatarUploader.new
uploader.store!(my_file) # size: 1024x768
uploader.url # => '/url/to/my_file.png' # size: 800x600
uploader.thumb.url # => '/url/to/thumb_my_file.png' # size: 200x200
```
##### Versioni innestate
Posso anche innestare le versioni:
```ruby
class MyUploader < CarrierWave::Uploader::Base
version :animal do
version :human
version :monkey
version :llama
end
end
```
##### Versioni condizionali
Posso creare una versione di un file solo se il model (variabile `model`, riferita al model a cui l'uploader è riferito) soddisfa determinate caratteristiche
```ruby
class MyUploader < CarrierWave::Uploader::Base

version :human, :if => :is_human?
version :monkey, :if => :is_monkey?
version :banner, :if => :is_landscape?

protected

def is_human? picture
model.can_program?(:ruby)
end

def is_monkey? picture
model.favorite_food == 'banana'
end

def is_landscape? picture
image = MiniMagick::Image.open(picture.path)
image[:width] > image[:height]
end

end
```

## Mantenere un upload anche se la validazione fallisce
In alcune piattaforme, il file caricato scompare se la validazione del form di inserimento fallisce obbligando l'utente a ricaricare tutto. Questo comportamento è avitabile usando un campo hidden `avatar_cache` (assumendo che il nome dell'upload sia `avatar`) che verrà valorizzato con il file già caricato dall'utente senza che questo se ne accorga.
Posso inserire una thumnail, per esempio, per far capire all'utente che il file esiste ed è stato caricato correttamente
```html
<%= form_for @user, :html => {:multipart => true} do |f| %>
<p>
<label>My Avatar</label>
<%= image_tag(@user.avatar_url) if @user.avatar? %>
<%= f.file_field :avatar %>
<%= f.hidden_field :avatar_cache %>
</p>
<% end %>
```

## Rimuovere un file caricato
Posso o chiamare il metodo `remove_avatar!` da controller, oppure usare un checkbox di questo tipo nelle views:
```html
<%= form_for @user, :html => {:multipart => true} do |f| %>
<p>
<label>My Avatar</label>
<%= image_tag(@user.avatar_url) if @user.avatar? %>
<%= f.file_field :avatar %>
</p>

<p>
<label>
<%= f.check_box :remove_avatar %>
Remove avatar
</label>
</p>
<% end %>
```

## Caricare un file tramite un URL
```html
<%= form_for @user, :html => {:multipart => true} do |f| %>
<p>
<label>My Avatar URL:</label>
<%= image_tag(@user.avatar_url) if @user.avatar? %>
<%= f.text_field :remote_avatar_url %>
</p>
<% end %>
```

## Fornire un URL di default
Spesso, sopratutto con le immagini, conviene fornire un URL di defualt nel caso in cui l'utente non carichi nessun file. Per fornire un url di default da utilizzare posso usare il metodo default_url nell'uploader
```ruby
class MyUploader < CarrierWave::Uploader::Base
def default_url
"/images/fallback/" + [version_name, "default.png"].compact.join('_')
end
end
```

## Configurazioni
Per configurare CarrierWave basta creare il file `config/initializers/carrierwave.rb` e inserirvi config come questa di esempio:
```ruby
CarrierWave.configure do |config|
config.permissions = 0666
config.storage = :s3
end
```

## Test
Conviene testare utilizzando uno storage locale e non remoto, con la seguente configurazione:
```ruby
if Rails.env.test? or Rails.env.cucumber?
CarrierWave.configure do |config|
config.storage = :file
config.enable_processing = false
end
end
```

#### Rspec
CarrierWave possiede dei matcher rspec molto comodi, di seguito un esempio:
```ruby
require 'carrierwave/test/matchers'

describe MyUploader do
include CarrierWave::Test::Matchers

before do
MyUploader.enable_processing = true
@uploader = MyUploader.new(@user, :avatar)
@uploader.store!(File.open(path_to_file))
end

after do
MyUploader.enable_processing = false
end

context 'the thumb version' do
it "should scale down a landscape image to be exactly 64 by 64 pixels" do
@uploader.thumb.should have_dimensions(64, 64)
end
end

context 'the small version' do
it "should scale down a landscape image to fit within 200 by 200 pixels" do
@uploader.small.should be_no_larger_than(200, 200)
end
end

it "should make the image readable only to the owner and not executable" do
@uploader.should have_permissions(0600)
end
end
```

## Amazon S3
Per permettere il caricamento su S3 è necessaria la gem `fog`, devo fornire i `fog_credentials` e la `fog_directory` in un initializer (ricorda che la `fog_directory` deve essere creata prima)
Di seguito un esempio di configurazione per amazon S3:
```ruby
CarrierWave.configure do |config|
config.fog_credentials = {
:provider => 'AWS', # required
:aws_access_key_id => 'xxx', # required
:aws_secret_access_key => 'yyy', # required
:region => 'eu-west-1' # optional, defaults to 'us-east-1'
}
config.fog_directory = 'name_of_directory' # required
config.fog_host = 'https://assets.example.com' # optional, defaults to nil
config.fog_public = false # optional, defaults to true
config.fog_attributes = {'Cache-Control'=>'max-age=315576000'} # optional, defaults to {}
end
```
Nell'uploader devo settare lo storage a `:fog`:
```ruby
class AvatarUploader < CarrierWave::Uploader::Base
storage :fog
end
```
Per ottenere l'url del file memorizzato funziona in maniera trasparente il metodo `url` dell'`uploader` (`CarrierWave::Uploader#url`)

#### carrierwave-aws
Al posto di `fog` conviene usare [carrierwave-aws](https://github.com/sorentwo/carrierwave-aws) che è pensata solo per amazon, molto più leggera e versatile.


## Manipolare immagini
CarrierWave fornisce una semplice libreria di elaborazione immagini che permette di cambiarne il formato, ridimensionarle...
