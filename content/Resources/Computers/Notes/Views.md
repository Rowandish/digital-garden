---
tags:
  - Coding
  - RubyOnRails
---


Le viste sono la visualizzazione HTML di quanto viene prodotto dal controller. Tipicamente esiste una vista per ogni azione (metodo) del controller.
L'HTML completo fornito al client sarà la composizione del file ERB associato all'azione del controller, del layout che lo contiene e di tutti i partial che questo referenzia.

## 1. Template, Partial e Layouts

### 1.1 Templates
Associati all'azione del controller, possono essere file .erb o .haml e contengono codice ruby che utilizza le variabili fornite dal controller.
Esempio con codice `erb`
```erb
<h1>Names of all the people</h1>
<% @people.each do |person| %>
Name: <%= person.name %><br>
<% end %>
```
Stesso codice con `haml`
```haml
%h1 Names of all the people
- @people.each do |person|
Name:
= person.name
```

### 1.2 Partials
Servono per suddividere il rendering in sottoparti richiamabili. Non sono associati a nessun controller e possono essere richiamati da più template con il comando `render`.
Se sono all'interno della stessa cartella di view posso scivere:
```erb
<%= render "menu" %>
```
che eseguità il rendere di un file chiamato `_menu.html.erb`.
Notare che i partial **devono cominciare con un _** per distinguerli dai template.
Se voglio utilizzare un partial da una altra cartella posso scrivere
```erb
<%= render "shared/menu" %>
```
#### 1.2.1 Passare variabili al partial
Quando eseguo il rendering di un partial, a questo viene passata, se esiste, una variabile con lo stesso nome del partial.
I seguenti due codici sono quindi equivalenti:
```erb
<%= render partial: "product" %>
<%= render partial: "product", locals: {product: @product} %>
```
#### 1.2.2 Iterare su collection di elementi
Spesso ho un partial per un singolo elemento e voglio eseguirne il rendering per una serie di elementi.
Il seguente codice:
```erb
<% @products.each do |product| %>
<%= render partial: "product", locals: { product: product } %>
<% end %>
```
Posso tradurlo i una singola linea di codice:
```erb
<%= render partial: "product", collection: @products %>
```
Che posso ulteriormente ridurre con:
```erb
<%= render @products %>
```
Nel caso in cui necessiti di avere un partial (divider, spacer) da inserire ad ogni rendering di partial di una collection, posso utilizzare l'attributo `spacer_partial` nel seguente modo:
```erb
<%= render partial: @products, spacer_template: "product_ruler" %>
```
Verrà quindi eseguito il render del `_product_ruler` partial tra ogni partial `_product`

### 1.3 Layouts
I layout possono essere utilizzati per renderizzare un template comune attorno ai risultati dei controller. Di solito un sito presenta una serie di layout di base, come quello per l'utente sloggato o loggato o altri utilizzi.

## 2. Helper
### 2.1 RecordTagHelper
Questo modulo fornisce un modo comodo per generare i tag a partire dagli oggetti forniti dal backend, con degli id e delle classi coerenti.
#### 2.1.1 content_tag_for
Crea un tag in relazione all'oggetto `ActiveRecord`.
Per esempio, dato un `@article` della classe Article posso fare:
```erb
<%= content_tag_for(:tr, @article, class: "frontpage") do %>
<td><%= @article.title %></td>
<% end %>
```
Che genera
```erb
<tr id="article_1234" class="article frontpage">
<td>Hello World!</td>
</tr>
```
Posso anche passare una collection di oggetti ActiveRecord:
```erb
<%= content_tag_for(:tr, @articles) do |article| %>
<td><%= article.title %></td>
<% end %>
```
Genera
```erb
<tr id="article_1234" class="article">
<td>Hello World!</td>
</tr>
<tr id="article_1235" class="article">
<td>Ruby on Rails Rocks!</td>
</tr>
```
#### 2.1.2 div_for
Analogo a `content_tag_for` ma crea un tag `div`.
#### 2.1.3 image_path
Fornisce il path dell'immagine negli asset
```ruby
image_path("edit.png") # => /assets/edit.png
```
#### 2.1.4 image_url
Fornisce l'url completo da un'immagine negli asset
```ruby
image_url("edit.png") # => http://www.example.com/assets/edit.png
```
#### 2.1.5 image_tag
Fornisce il tag html per una immagine negli asset
```ruby
image_tag("icon.png") # => <img src="/assets/icon.png" alt="Icon" />
```
#### 2.1.6 content_for
`content_for` memorizza un blocco di markup in una variabile in modo che possa essere utilizzato successivamente. Viene chiamato mediante il metodo `yield`.
Per esempio, assumiamo che abbiamo un layout standard, ma inoltre una pagina che richiede un Javascript che le altre pagine non necessitano. Possiamo utilizzare `content_for` per includere questo Javascript nella nostra pagina speciale senza modificare il resto del sito.
```erb
<head>
<title>Welcome!</title>
<%= yield :special_script %>
</head>
```
Che può essere richiamato nel seguente modo
```erb
<% content_for :special_script do %>
<script>alert('Hello!')</script>
<% end %>
```

#### 2.1.7 link_to
Crea un link per una determinata route.
Esempio:
```ruby
<% @books.each do |book| %>
<tr>
<td><%= book.title %></td>
<td><%= book.content %></td>
<td><%= link_to "Show", book %></td>
<td><%= link_to "Edit", edit_book_path(book) %></td>
<td><%= link_to "Remove", book, method: :delete, data: { confirm: "Are you sure?" } %></td>
</tr>
<% end %>
```

### 2.2 DateHelper
Vedi documentazione http://guides.rubyonrails.org/action_view_overview.html
### 2.3 DebugHelper
Fornisce un tag pre compilato con l'oggetto da controllare
```ruby
my_hash = {'first' => 1, 'second' => 'two', 'third' => [1,2,3]}
debug(my_hash)
```
Fornisce
```erb
<pre class='debug_dump'>---
first: 1
second: two
third:
- 1
- 2
- 3
</pre>
```
### 2.4 FormHelper
##### 2.4.1 form_for
Crea un form a partire da una istanza del model. Per esempio, assumiamo di avere un model Person e ne vogliamo creare una nuova istanza:

```ruby
<%= form_for @person, url: {action: "create"} do |f| %>
<%= f.text_field :first_name %>
<%= f.text_field :last_name %>
<%= submit_tag 'Create' %>
<% end %>
```
Creerà il seguente html:
```html
<form action="/people/create" method="post">
<input id="person_first_name" name="person[first_name]" type="text" />
<input id="person_last_name" name="person[last_name]" type="text" />
<input name="commit" type="submit" value="Create" />
</form>
```
a al controller arriverà l'oggetto seguente:
```json
{"action" => "create", "controller" => "people", "person" => {"first_name" => "William", "last_name" => "Smith"}}
```

##### 2.4.2 check_box
Fornisce una checkbox per accedere ad un atrributo booleano, eventualmente preselezionata in base al valore che tale oggetto ha nel model
```ruby
check_box("article", "validated")
```

##### 2.4.3 fields_for
analogo al form_for ma senza creare il tag form effettivo. Serve per specificare oggetti addizionali all'interno di un form
```html
<%= form_for @person, url: {action: "update"} do |person_form| %>
First name: <%= person_form.text_field :first_name %>
Last name : <%= person_form.text_field :last_name %>

<%= fields_for @person.permission do |permission_fields| %>
Admin? : <%= permission_fields.check_box :admin %>
<% end %>
<% end %>
```
##### 2.4.4 file_field
Fornisce un tag pe l'upload di file
```ruby
file_field(:user, :avatar)
```
##### 2.4.5 hidden_field
Fornisce un tag input hidden
```ruby
hidden_field(:user, :[[token]])
```
##### 2.4.6 label
fornisce un tag label
```
label(:article, :title)
```

##### 2.4.7 password_field
```ruby
password_field(:login, :pass)
```
##### 2.4.8 radio_button
```ruby
radio_button("article", "category", "rails")
radio_button("article", "category", "java")
```
##### 2.4.9 text_area
```ruby
text_area(:comment, :text, size: "20x30")
```
##### 2.4.10 text_field
```ruby
text_field(:article, :title)
```
##### 2.4.11 email_field
```ruby
email_field(:user, :email)
```
##### 2.4.12 url_field
```ruby
url_field(:user, :url)
```

### 2.5 FormOptionsHelper
Fornisce metodi per trasformare differenti tipi di container in insieme di tag **option**.
##### 2.5.1 collection_select
Ho un oggetto che ha una relazione di `belongs_to` ad un altro. Voglio creare un tag **select** con dei tag **option** per permettere di associarci l'oggetto padre.

Per esempio, assumiamo di avere l aseguente struttura
```ruby
class Article < ActiveRecord::Base
belongs_to :author
end

class Author < ActiveRecord::Base
has_many :articles
def name_with_initial
"#{first_name.first}. #{last_name}"
end
end
```
Assumimo di avere una istanza di `Article` (`@article`) e vogliamo associargli un autore.
Il seguente codice:
```ruby
collection_select(:article, :author_id, Author.all, :id, :name_with_initial, {prompt: true})
```
genera il seguente HTML (assumendo che `@article.author_id` sia uguale a 1). Ovviamente questo deve essere inserito in un form affinchè il giro funzioni.
```html
<select name="article[author_id]">
<option value="">Please select</option>
<option value="1" selected="selected">D. Heinemeier Hansson</option>
<option value="2">D. Thomas</option>
<option value="3">M. Clark</option>
</select>

```
##### 2.5.2 collection_radio_buttons
Analogo al metodo sopra ma creando dei **radio button** invece dei **select-option**
```ruby
collection_radio_buttons(:article, :author_id, Author.all, :id, :name_with_initial)
```
Fornisce
```html
<input id="article_author_id_1" name="article[author_id]" type="radio" value="1" checked="checked" />
<label for="article_author_id_1">D. Heinemeier Hansson</label>
<input id="article_author_id_2" name="article[author_id]" type="radio" value="2" />
<label for="article_author_id_2">D. Thomas</label>
<input id="article_author_id_3" name="article[author_id]" type="radio" value="3" />
<label for="article_author_id_3">M. Clark</label>
```
##### 2.5.3 collection_check_boxes
Analogo a sopra ma con degli input type checkbox
##### 2.5.4 option_groups_from_collection_for_select
Raggruppa gli oggetti in degli optgroup. Vedi documentazione se necessario
##### 2.5.5 options_for_select
Accetta un container (hash, array, enum...) e fornisce una lista di tag option
```ruby
options_for_select([ "VISA", "MasterCard" ])
```
##### 2.5.6 options_from_collection_for_select
Fornisce una lista di option a partire da una istanza di un oggetto ActiveRecord in cui l'attributo del tag è `text_method` e il valore è `value_method`
```ruby
options_from_collection_for_select(collection, value_method, text_method, selected = nil)
```
```ruby
options_from_collection_for_select(@people, "id", "name")
```
##### 2.5.7 select
Crea un tag select e una serie di tag option in esso contenuti per l'oggetto fornito
```ruby
select("article", "person_id", Person.all.collect {|p| [ p.name, p.id ] }, {include_blank: true})
```
Se `@article.person_id = 1` il risultato sarà:
```html
<select name="article[person_id]">
<option value=""></option>
<option value="1" selected="selected">David</option>
<option value="2">Sam</option>
<option value="3">Tobias</option>
</select>
```