from django import template
from .. import models

register = template.Library()

@register.simple_tag
def title():
    return "My django blog"
@register.inclusion_tag("book/partial/nav.html")
def category_nav():
    return {
        "category": models.Category.objects.filter(status=True)
    }

