from django import template

from petstagram.main.models import Profile

register = template.Library()


@register.simple_tag()
def has_profile():
    return Profile.objects.count() > 0
