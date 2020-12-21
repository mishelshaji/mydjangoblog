from django import template

register = template.Library()

@register.filter('format_price')
def format_price(value):
    return float(value)