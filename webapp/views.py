from django.shortcuts import redirect, render, get_object_or_404
from .models import Beer
from .forms import BeerForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def home(request):
    return render(request, 'index.html')

@login_required()
def beer_list(request):
    beers = Beer.objects.all()
    context = {'beers': beers}
    return render(request, 'beer_list.html', context=context)

@login_required()
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

@login_required()
def edit_beer(request, beer_id):
    beer = get_object_or_404(Beer, id=beer_id)
    if request.method == 'POST':
        beer_form = BeerForm(request.POST,instance=beer)
        if beer_form.is_valid():
            beer_form.save()
            return redirect(to='beer_list')
        else:
            context = {'beer_form': beer_form}

    beer_form = BeerForm(instance=beer)
    context = {'beer_form': beer_form}
    return render(request,'beer_form.html',context=context)
    
@login_required()
def delete_beer(request, beer_id):
    beer = get_object_or_404(Beer, id=beer_id)
    beer.delete()
    return redirect(to='beer_list')

@login_required()
def search_beer(request): 
    if request.method == 'POST':
        search_beer = request.POST['search_beer']
        beer_list = Beer.objects.filter( name__contains = search_beer )
        context = {'beers': beer_list}
        return render(request, 'beer_list.html', context=context)