from django import template

register = template.Library()


@register.filter
def crypto(text):
    vogal = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 'u': '9'}
    for v in text:
        if v in vogal:
            text = text.replace(v, vogal[v])
    return text
