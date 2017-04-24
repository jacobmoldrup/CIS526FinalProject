from django.shortcuts import render

from BikeShop.utils.cityGen import createCities
from BikeShop.utils.bikeshopGen import insertBikeShops
from BikeShop.utils.BikeDataGen import readFile

# Create your views here.
def post_main_page(request):
    fileName = "BikeShop/Raw_Data/Bike_Data.txt"

    #createCities()
    #insertBikeShops()
    readFile(fileName)



    return render(request, 'Layout/index.html', {})
