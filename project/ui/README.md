# UI app

This app manages the UI and AJAX loading. At the moment this app only handles GET request for rendering pages and does not assist with AJAX POST, or any other AJAX functionality. This will most likely change.  

## BootStrap form fields

Bootstrap has special formating for HTML forms and From errors that do not play nicely out of the box with django. To fix this and have proper formated forms use these tamplate tags;

```html
{% load ui.bootstrap %}
<form method="POST">
	{% csrf_token %}

	{% boot_form_fields form %}
			
	<button class="btn btn-default">
		<span class="glyphicon glyphicon-share-alt"></span>
		Save
	</button>
</form>

``` 
`{% load ui.bootstrap %}` loads the bootstrap tags.
`{% boot_form_fields myForm %}` will render the field correctly and display all error messages in the proper stop. Demo this behavior with the login form, try to leave fields blank, and try to login with bad credentials.
 * where `form` is the form name passed to the template.

## middleware.py

This file is where all the magic happens. Each request is checked if its AJAX and sets `request.context_dict` dict to be have appropriate `base_template` value.

## Templates

The base templates for the whole project live here. The UI app can be a dependent for ever app that requires user interaction.

## request.context_dict

The `request.context_dict` is added prior to the views file being called. The object is the dictionary that will be sent to each view for rendering. Please add all values you need to send to the template like so;
```python

def get(self, request):
    request.context_dict['error'] = request.GET.get( 'error', None )
    request.context_dict['referer'] = request.GET.get( 'referer', '/' )
    request.context_dict['form'] = UserForm()
    return render( request, 'users/login.html', request.context_dict )
```

## Whats going on here?

When a request is sent to the server, the middleware.py file will check if its an ajax request. If it is then the base template file will be set to "ui/ajax.html" witch will only render the content for that page and not the whole page.This allows( with the help of history.pushState in JS ) for AJAX load calls to keep the same URL's, SEO and legacy support.

## How do i use it?

For this magic to work, the template file's for each page must be set correctly;

```html
{% extends base_template|default:"ui/base.html" %}

{% block title %}Login - {% endblock %}

{% block content %}
	<fieldset>

		<legend>Log in</legend>
		
		<form id="user_form" action="/users/login" method="post">
			<h2 class="error">{% if error %}{{ error }}{% endif %}</h2>

			{% csrf_token %}
			{{ form.as_p }}
			<input type="hidden" name="referer" value="{{ referer }}" >
			<input type="submit" value="log in" />
		</form>

	</fieldset>

{% endblock %}

{% block spa %}
<script>
	$( '#user_form' ).on( 'submit', function ( event ) {
		event.preventDefault();
		$.ajax( {
			url: $( this ).attr( 'action' ),
			type: $( this ).attr( 'method' ),
			data: $( this ).serializeObject(),
			success: function( data ){

				if( data.status === 'success' ){
					alert( 'yay' )
				}else{
					$( '#user_form' ).find( 'h2' ).html( 'Incorrent username or password' )
				}
				
			}
		} );
	} );
</script>
{% endblock %}
``` 
Lets break down the template above:

1. `{% extends base_template|default:"ui/base.html" %}`
	* This loads the template to extend from. If the `request.context_dict.base_tempalte` is set then it will be used. If not then the default value will be used. The behavior will change shortly, but dont worry about that, the rest of template is much more important.
2. `{% block title %}Login - {% endblock %}`
	* This is the title PREFIX portion of the page. Regardless if the call is AJAX or not, this sill pre-fix will be set.
	* This can be omitted for no title prefix.
3. `{% block content %} ...HTML... {% endblock %}`
	* The content HTML portion of the template lives here. Regardless if its AJAX call or not the say thing will be rendered as the content.
4. `{% block spa %} ...HTML or JS... {% endblock %}`
	* The block will only be loaded if the page is called from an AJAX call.
	* I do not like this behavior and am actively looking for a better way...


For the view.py files, see `request.context_dict` on this page.

## AJAX links

For a link to tiger a AJAX load call, it must be set up correcly.
```html
<a href="/users/login" class="ajax">Log in</a>
```

All this is needed is a regular HTML `<a href>` with a the class set to AJAX. When one of these links is clicked jQuery will stop the link from firing and do an AJAX to the reference( href attribute ) value for the HTML content to load and change the address's bar URL and page title to correct values to allow for proper history, bookmarking and URL sharing.
