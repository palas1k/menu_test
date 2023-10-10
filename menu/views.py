from django.shortcuts import render



def index(request):
    return render(request, 'menu/base_menu.html')


def check_url(request, menu_id):
    return render(request, 'menu/base_menu.html')
