from django import template

register = template.Library()

@register.simple_tag
def current_user():
	return request.user