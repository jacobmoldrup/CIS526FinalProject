from django.shortcuts import render
from BikeShop.models import BikeShops
from BikeShop.utils.query import makeQuery

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

# Create your views here.
def post_main_page(request):
    # this can be commented out once your done with importing data
    #fileName = "BikeShop/Raw_Data/Bike_Data.txt"
    fileName = "BikeShop/Raw_Data/products_data.txt"

    # LOOK HERE
    # uncomment these lines for reading in Data
    #createCities()
    #insertBikeShops()
    #readFile(fileName)

    makeProducts(fileName)



    return render(request, 'Layout/index.html', {})

def login(request):
    return render(request,'pages/login.html',{})

def bikes(request):
    return render(request,'pages/bikes.html',{})

def services(request):
    return render(request,'pages/services.html',{})
def favorites(request):
    return render(request, 'pages/favorites.html', {})

def cart(request):
    return render(request, 'pages/cart.html',{})

def bikes_at_shops(pk, request):

    bikes = makeQuery('findBikeAtShops', [pk])
    shop = BikeShops.objects.get(id = pk)

    return render(request, 'pages/shopBikes.html', {'bikes': bikes, 'shop': shop})

def all_shops(request):
    type = 'allShops'
    shops = makeQuery(type, [])
    return render(request, 'pages/shops.html', {'shops':shops})