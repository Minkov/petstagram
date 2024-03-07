from django import template

register = template.Library()


@register.filter
def placeholder(field, token):
    field.field.widget.attrs['placeholder'] = token
    return field
