from django.shortcuts import render

from BikeShop.utils.cityGen import createCities
from BikeShop.utils.bikeshopGen import insertBikeShops
from BikeShop.utils.BikeDataGen import readFile

# Create your views here.
def post_main_page(request):
    # this can be commented out once your done with importing data
    fileName = "BikeShop/Raw_Data/Bike_Data.txt"

    # LOOK HERE
    # uncomment these lines for reading in Data
    #createCities()
    #insertBikeShops()
    #readFile(fileName)



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