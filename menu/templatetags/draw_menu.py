from django import template

from menu.models import MenuCats

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = MenuCats.objects.prefetch_related('menu').get(name = menu_name)
    #menu = MenuCats.objects.filter(menu__name = menu_name).select_related('menu')
    request_data = context['request'].path
    if len(request_data)!=1:
        menu_id = int(request_data[1])
    else:
        menu_id = 0
    return {'menu': menu, 'selected': menu_id}