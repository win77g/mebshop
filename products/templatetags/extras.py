from django import template

register = template.Library()

@register.filter()
def values(items, attributes):
    return [getattr(i, attributes) for i in items]


@register.filter()
def distinct(items):
    return set(items)


@register.filter()
def qs_distinct(qs, attributes):
    fields = map(str.strip, attributes.split(','))
    return qs.order_by(*fields).distinct(*fields)

