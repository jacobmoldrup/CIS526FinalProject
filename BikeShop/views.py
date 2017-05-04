
import json

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from BikeShop.models import BikeShops, Cities
from BikeShop.utils.query import makeQuery
from BikeShop.forms import SearchForm
from BikeShop.utils.cityGen import createCities
from BikeShop.utils.bikeshopGen import insertBikeShops
from BikeShop.utils.BikeDataGen import readFile
from BikeShop.utils.productGen import makeProducts

from BikeShop.utils.cityGen import createCities
from BikeShop.utils.bikeshopGen import insertBikeShops
from BikeShop.utils.BikeDataGen import readFile
from BikeShop.utils.cityGen import createCities
from BikeShop.utils.bikeshopGen import insertBikeShops
from BikeShop.utils.BikeDataGen import readFile
from .models import Bikes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.
def post_main_page(request):
    # this can be commented out once your done with importing data
    #fileName = "BikeShop/Raw_Data/Bike_Data.txt"
    #fileName = "BikeShop/Raw_Data/products_data.txt"

    # LOOK HERE
    # uncomment these lines for reading in Data
    #createCities()
    #insertBikeShops()
    #readFile(fileName)

    #makeProducts(fileName)



    return render(request, 'Layout/index.html', {})

def login(request):
    return render(request,'pages/login.html',{})

def bikes(request):
    mybikes = makeQuery('allBikes', [])
    return render(request, 'pages/bikes.html', {'bikes': mybikes})

@login_required
def services(request):
    return render(request, 'pages/services.html', {})


def items_at_shops(pk, request):
    bikes = makeQuery('findBikeAtShops', [pk])
    products = makeQuery('productsAtShop', [pk])
    shop = BikeShops.objects.get(id=pk)
    return render(request, 'pages/products.html', {'bikes': bikes, 'products': products, 'shop':shop } )

def bikes_at_shops(pk, request):
    bikes = makeQuery('findBikeAtShops', [pk])
    shop = BikeShops.objects.get(id=pk)

    return render(request, 'pages/shopBikes.html', {'bikes': bikes, 'shop': shop})


def all_shops(request):
    type = 'allShops'
    shops = makeQuery(type, [])
    return render(request, 'pages/shops.html', {'shops': shops})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def findShop(request):
    form = SearchForm(request.GET)
    shops = None
    if form.is_valid():
        searchField = form.cleaned_data['shop_search']

        cities = Cities.objects.filter(name= searchField)
        if cities == []:
            return 404
        shops = BikeShops.objects.filter(city_id= cities.id)
        if shops == []:
            return 404
    return render(request, 'pages/findSHop.html', {'shops': shops} )



def bikes_at_shops(pk, request):

    bikes = makeQuery('findBikeAtShops', [pk])
    shop = BikeShops.objects.get(id = pk)

    return render(request, 'pages/shopBikes.html', {'bikes': bikes, 'shop': shop})



def getBike(request):
    bike_id = None
    if request.Method == "GET":
        bike_id = request.GET['bike_id']

    if bike_id:
        bike = makeQuery('singleBike', [bike_id])
        json_data = json.dumps(bike)
       # return HttpResponse(json_data, content_type="application/json")
