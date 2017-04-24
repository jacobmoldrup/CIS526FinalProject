from BikeShop.models import Companies, Bikes, Companies_Bikes, BikeShops, BikeShops_Bikes
from enum import Enum
import random
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist



class Size(Enum):
    S = 1
    M = 2
    L = 3
    XL = 4



def readFile(fileName):


    with open(fileName) as f:
        lines = f.read().splitlines()

    company = None
    for line in lines:

        # try to split first
        split_line = line.split('  ')
        if (split_line[0] == 'company'):
            company = Companies.objects.get(name=split_line[1])

        else:
            split_line = line.split(', ')


            # If adding doesn't work change these next few lines
            # This number may change if you delete items from BikeShops
            # run this in python shell to see the id
            # python manage.py shell
            # from BikeShop.models import BikeShops
            # BikeShops.objects.all().values()
            starting_bikeShop_id = 1
            ending_bikeshop_id = starting_bikeShop_id +9
            num_to_Make = random.randint(1, 10)
            for insert in range( num_to_Make):
                size = random.randint(1,5)
                bs_pk = random.randint(starting_bikeShop_id, ending_bikeshop_id)

                # this will be none unless it finds, in which case an exception should be caugh
                # and the function should return
                shop = None
                try:
                    shop = BikeShops.objects.get(id= bs_pk)
                except ObjectDoesNotExist:
                    print("Bike Shop was not found. Please take a look at line 35")

                print(int(split_line[2]))
                print(int(split_line[3]))
                bike = Bikes.objects.get_or_create(model=split_line[0], type=split_line[1], price=int(split_line[2]), year=int(split_line[3]), thumbnail=split_line[4], size= size)

                Companies_Bikes.objects.update_or_create(company_code= company, bike_id=bike[0])

                BikeShops_Bikes.objects.update_or_create(bikeshop_id= shop, bike_id= bike[0])




