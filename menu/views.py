from django.shortcuts import render

from menu.models import MenuCats


def index(request):
    menu = MenuCats.objects.all()
    return render(request, 'menu/base_menu.html', context={'menu': menu})

def check_url(request, int):
    return render(request, 'menu/check.html')
