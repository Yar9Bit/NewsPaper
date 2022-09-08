from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    words = ['fuck', 'ass']
    if value in words:
        return 'Цензура'
    else:
        return value
