---
tags:
  - Coding
  - RubyOnRails
---


## Controller
Testano i metodi del controller, indipendentemente dal fatto che vengano chiamati o meno dal frontend.
In particolare si dedicano a testare il:
- **Rendering dei template**: `expect(response).to render_template(:new)`
- **Redirects**: `expect(response).to redirect_to(location)`
- **Varaibili di istanza**: verificare che il controller fornisca la variabile `@foo` corretta `expect(assigns(:foo)).to eq([foo]`
- **Cookie**: inviati alla risposta
- **Codice http di risposta**: `expect(response).to have_http_status(:created)`

##### Render_template
Disponbile in:
- **controller**
- **request**

```ruby
expect(subject).to render_template(:index)
expect(subject).to render_template("index")
expect(subject).to render_template("gadgets/index")
```
##### Redirect_to
Disponbile in:
- **controller**
- **request**
```ruby
it "redirects to widget_url(@widget)" do
expect(subject).to redirect_to(widget_url(assigns(:widget)))
end
it "redirects_to :action => :show" do
expect(subject).to redirect_to :action => :show,
:id => assigns(:widget).id
end
it "redirects_to(@widget)" do
expect(subject).to redirect_to(assigns(:widget))
end
it "redirects_to /widgets/:id" do
expect(subject).to redirect_to("/widgets/#{assigns(:widget).id}")
end
```

##### have_http_status
Disponbile in:
- **controller**
- **request**
- **feature**

```ruby
expect(response).to have_http_status(209)
expect(response).to have_http_status(:ok)
expect(response).to have_http_status(:error)
```

##### be_a_new
Accetta in ingresso una classe e fornisce ok se il soggetto è una istanza di tale classe. Posso concatenare anche il metodo `with` con il `be_a_new` per controllare gli attributi di tale classe.

```ruby
expect(foo).to be_a_new(Foo)
expect(foo).not_to be_a_new(String)
```
Nota bene che funziona con un oggetto che è una nuova istanza di classe (`Foo.ne`w) e non con un oggetto già creato (`Foo.create`)

## Request
Utili per testare un intero comportamento (routing e controller). Posso testare:
- Singola richiesta
- Multiple richieste su più controller
- Multiple richieste su più sessioni

Se si utilizzano i test di controller e ri route può non servire.

## Feature
Specificano test ad alto livello per testare una intera funzionalità di un applicativo. Navigano l'applicazione da pagine web (utilizzando capybara).
L'oggetto feature corrisponde al describe, lo scenario all'it.
Classi comode
### Navigazione
##### visit
Naviga in una pagina web (solo un parametro in ingresso, solo **GET**)
```ruby
visit "/widgets/new"
visit(post_comments_path(post))
```
##### current_path
Fornisce il path attuale.
```ruby
expect(current_path).to eq(post_comments_path(post))
```
### Cliccare link e bottoni
Capybara automaticamente segue il link, i redirect e submitta i form.
```ruby
click_link('id-of-link')
click_link('Link Text')
click_button('Save')
click_on('Link Text')
click_on('Button Value')
```
### Interagire con i form
```ruby
fill_in('First Name', with: 'John')
fill_in('Password', with: 'Seekrit')
fill_in('Description', with: 'Really Long Text...')
choose('A Radio Button')
check('A Checkbox')
uncheck('A Checkbox')
attach_file('Image', '/path/to/image.jpg')
select('Option', :from => 'Select Box')
```

### Verificare l'esistenza di elementi
```ruby
expect(page).to have_selector('table tr')
expect(page).to have_selector(:xpath, '//table/tr')

expect(page).to have_xpath('//table/tr')
expect(page).to have_css('table tr.foo')
expect(page).to have_content('foo')
expect(page).to have_button('foo')
```

### Trovare un elemento
Ho numerodi modi per trovare elementi nella pagina per manipolarli (i metodi find aspettano che l'elemento compaia nella pagina (aspettando conseguentmente tutte le chiamate AJAX), se l'elemento non appare lancia un errore).
```ruby
find_field('First Name').value
find_link('Hello', :visible => :all).visible?
find_button('Send').click

find(:xpath, "//table/tr").click
find("#overlay").find("h1").click
all('a').each { |a| a[:href] }
```
Gli oggetti che vengono trovati con il `find` possono essere poi concatenati ad altri metodi capybara:
```ruby
find('#navigation').click_link('Home')
expect(find('#navigation')).to have_button('Sign out')
```

### Scoping
Volendo testare solo una determinata sezione di una pagina, posso utilizzare il metodo `within` che accetta in ingresso un selettore CSS nel seguente modo:
```ruby
within("li#employee") do
fill_in 'Name', :with => 'Jimmy'
end
```

### Lavorare con le finestre
Talvolta il click dei pulsanti crea delle nuove finestre (per esempio il log in con facebook), che capybara dovrebbe gestire.
Assumiamo che ho il pulsante like di facebook che mi apre una nuova finestra. Il test avverrà nel seguente modo:
```ruby
facebook_window = window_opened_by do
click_button 'Like'
end
within_window facebook_window do
find('#login_email').set('a@example.com')
find('#login_password').set('qwerty')
click_button 'Submit'
end
```

### Debugging
E' possibile fare degli snapshot delle pagine elaborate da capybara per poterle guardare e trovare eventuali errori.
- `save_and_open_page`: Apri la pagina corrente
- `print page.html`: Fornisce la string del DOM attuale
- `page.save_screenshot('screenshot.png')`: salva uno screenshot della pagina
- `save_and_open_screenshot`: salva lo screenshot e lo apre

## View
Tendenzialmente inutili