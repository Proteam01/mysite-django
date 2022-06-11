from django.shortcuts import render
from .models import Beer
from .forms import BeerForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def beer_list(request):
    beers = Beer.objects.all()
    context = {'beers': beers}
    return render(request, 'beer_list.html', context=context)

def new_beer(request):
    beer_form = BeerForm()
    context = {'beer_form': beer_form}
    return render(request,'beer_form.html',context=context)