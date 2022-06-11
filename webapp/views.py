from django.shortcuts import redirect, render
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
    if request.method == 'POST':
        beer_form = BeerForm(request.POST)
        if beer_form.is_valid():
            print('valid form')
            beer_form.save()
            return redirect(to='beer_list')
        else:
            context = {'beer_form': beer_form}
            return render(request,'beer_form.html',context=context)         

    context = {'beer_form': beer_form}
    return render(request,'beer_form.html',context=context)