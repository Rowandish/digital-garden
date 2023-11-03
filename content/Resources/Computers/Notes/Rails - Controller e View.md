---
tags:
  - Coding
  - RubyOnRails
---


Di seguito la descrizione di come interconnettere i controller con le viste.
## 1. Creare risposte
Dal punto di vista del controller, esistono tre modi per creare una risposta HTTP:
- **render**: crea un risposta completa da inviare al browser
- **redirect_to**: invia un status code HTTP di redirect
- **head**: crea una risposta che consiste nel solo header HTTP

## 1.1 render
Di seguito vengono elencati tutti i metodi per renderizzare la stessa vista
```ruby
render :edit
render action: :edit
render "edit"
render "edit.html.erb"
render action: "edit"
render action: "edit.html.erb"
render "books/edit"
render "books/edit.html.erb"
render template: "books/edit"
render template: "books/edit.html.erb"
render "/path/to/rails/app/views/books/edit"
render "/path/to/rails/app/views/books/edit.html.erb"
render file: "/path/to/rails/app/views/books/edit"
render file: "/path/to/rails/app/views/books/edit.html.erb"
```

#### 1.1.1 Render di un template dello stesso controller 
Voglio renderizzare la vista che corrisponde a un template **differente nello stesso controller**. In questo caso basta indicare il nome della vista.
```ruby
def update
@book = Book.find(params[:id])
if @book.update(book_params)
redirect_to(@book)
else
render :edit
end
end
```
Se l'aggiornamento fallisce, verrà renderizzata la vista `edit.html.erb` appartenente allo stesso controller.
#### 1.1.2 Rendere di un template di un altro controller
Il metodo render accetta anche un path assoluto (relativo ad app/views)
```ruby
render "products/show"
```

#### 1.1.3 render JSON
Invece di chiamare una vista e fornire il risultato di quella, fornisce direttamente il JSON indicato (già serializzato)
```ruby
render json: @product
```

#### 1.1.4 Opzioni del metodo render
Esistono quattro possibili opzioni:
- `content_type`
- `layout`
- `location`
- `status`

##### content_type
Modifica il content-type della risposta. Di default è text/html (o application/json se si utilizza l'opzione :json) ma volendo posso cambiarla nel seguente modo
```ruby
render file: filename, content_type: "application/rss"
```
##### layout
La vista di default viene visualizzata come parte del layout corrente. Se voglio specificare un layout diverso specifico posso scrivere:
```ruby
render layout: "special_layout"
```
##### location
Modifica l'header HTTP location:
```ruby
render xml: photo, location: photo_url(photo)
```

##### status
Di default lo status code HTTP è 200 (ok), ma posso modificarlo nel seguente modo:
```ruby
render status: 500
render status: :forbidden
```
## 1.2 redirect_to
Indica al browser di inviare una nuova richiesta per un url completamente differente. Per esempio per andare all'url delle foto basta un:
```ruby
redirect_to photos_url
```
Posso chiamarwe il redirect_to con quasiasi parametro che potre usare con un `link_to` o `url_for`

### 1.2.1 Differenza tra il render e il redirect_to
Si è portati a pensare che il redirect_to sia una specie di render più potente, come un goto. Ovviamente non è così.
Il trucco vi è che il render non fa eseguire un redirect al browser, banalmente chiama la view associata ad un particolare metodo del controller (**senza** eseguirlo).
Segue l'esempio:
```ruby
def index
@books = Book.all
end

def show
@book = Book.find_by(id: params[:id])
if @book.nil?
render action: "index"
end
end
```
Se `@book` risulta `nil`, viene eseguito un `render` a `index`, ma solo alla sua vista (il codice `@books = Book.all` **non viene eseguito**), conseguentemente se in tale vista viene richiesta la variabile `@books` questa risulterà `nil`.
E' possibile risolvere la cosa sostituendo il `render action: "index"` con un `redirect_to action: :index`, ma questo risulterebbe molto lento: il frontend fa due chiamate al server invece di una.
la soluzione migliore è invece la seguente:
```ruby
def index
@books = Book.all
end

def show
@book = Book.find_by(id: params[:id])
if @book.nil?
@books = Book.all
flash.now[:alert] = "Your book was not found"
render "index"
end
end
```
in questo modo utilizzo il metodo render andando a fornire la vista della variabile `@books` richiesta.