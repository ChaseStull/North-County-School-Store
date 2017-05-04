from django.shortcuts import get_object_or_404, render
from .models import Item

from django.http import HttpResponseRedirect

from .forms import LoginForm

def index(request):
    return render(request, 'inventory/index.html', {'item_list': Item.objects.all()})


def detail(request, item_name):
    item = get_object_or_404(Item, item_name=item_name)
    return render(request, 'inventory/detail.html', {'item': item})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('../../')

    else:
        form = LoginForm()

    return render(request, 'inventory/login.html', {'form': form})