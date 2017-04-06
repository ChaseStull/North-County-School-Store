from django.shortcuts import get_object_or_404, render
from .models import Item


def index(request):
    return render(request, 'inventory/index.html', {'item_list': Item.objects.all()})


def detail(request, item_name):
    item = get_object_or_404(Item, item_name=item_name)
    return render(request, 'inventory/detail.html', {'item': item})
