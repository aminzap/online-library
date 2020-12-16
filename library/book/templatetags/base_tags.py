import datetime
from django import template

register = template.Library()

@register.simple_tag
def title():
    return "My django blog"