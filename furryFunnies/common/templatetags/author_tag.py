from django import template

from furryFunnies.author.models import Author

register = template.Library()


@register.simple_tag
def get_author():
    return Author.objects.first()