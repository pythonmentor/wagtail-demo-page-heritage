from .models import HomePage


def menu_items(request):
    return {
        "menu_items": HomePage.objects.live().in_menu().specific(),
    }
