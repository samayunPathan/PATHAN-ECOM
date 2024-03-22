from django import template

register = template.Library()
@register.inclusion_tag("core_app/menu.html")


def menu():
    return {}