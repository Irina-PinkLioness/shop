from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    return f"${value}"

@register.simple_tag
def copyright():
    return "&copy; 2025 SUNSHINE"