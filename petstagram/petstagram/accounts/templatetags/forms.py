from django import template

register = template.Library()


@register.filter
def placeholder(form_field, text):
    form_field.field.widget.attrs['placeholder'] = text
    return form_field


@register.filter
def form_field_class(form_field, className):
    default_classname = form_field.field.widget.attrs.get('class', '')
    form_field.field.widget.attrs['class'] = default_classname + ' ' + className
    return form_field
