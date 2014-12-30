from django import template

register = template.Library()

# http://vanderwijk.info/blog/adding-css-classes-formfields-in-django-templates/
@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.inclusion_tag( "ui/_boot_form_fields.html" )
def boot_form_fields( form ):
	return { 'form' : form }