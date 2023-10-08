from django import template
from django.shortcuts import get_object_or_404

from menu.models import MenuCats

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html')
def draw_menu(menu_name=None):
    if not menu_name:
        pass
    else:
        menu = MenuCats.objects.get(name = menu_name)
    return {'menu': menu}
