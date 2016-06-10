from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.filter
def active_tag(context):
    if context:
        span = 'glyphicon-ok-sign green'
    else:
        span = 'glyphicon-minus-sign red'
    return mark_safe('<span class="glyphicon {}"></span>'.format(span))
