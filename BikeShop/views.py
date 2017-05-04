from datetime import timezone

from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404

from BikeShop.forms import ServiceRequestForm
from BikeShop.models import BikeShops, CustomerServiceRequests
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
from .models import Bikes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def post_main_page(request):
    # this can be commented out once your done with importing data
    # fileName = "BikeShop/Raw_Data/Bike_Data.txt"
    # fileName1 = "BikeShop/Raw_Data/products_data.txt"
    #
    # # LOOK HERE
    # # uncomment these lines for reading in Data
    # createCities()
    # insertBikeShops()
    # readFile(fileName)
    #
    # makeProducts(fileName1)



    return render(request, 'Layout/index.html', {})


def view_all_bikes(request):
    bikes = Bikes.objects.all()
    return render(request, 'pages/bikes.html', {'bikes': bikes})



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

@login_required
def request_service(request):
    form = ServiceRequestForm()
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user_id = request.user
            service_request.save()
            return redirect('/')
    else:
        form = ServiceRequestForm()
    return render(request, 'pages/request_services.html', {'form': form})

@login_required
def current_services(request):
    # get current user service requests
    return render(request, 'pages/current_services.html')
