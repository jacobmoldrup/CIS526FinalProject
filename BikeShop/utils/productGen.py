from BikeShop.models import Companies, Cities, BikeShops, Products, BikeShops_Products
import random
from django.core.exceptions import ObjectDoesNotExist
companies ={
    'Giro': "123 Main st",
    'Bell': "456 West St",
    'FOX': "789 Tree St",
    'CamelBak': "147 Far St",
    'Dakine': "258 North St"
}
cityid=1

def makeProducts(fileName):
    city = Cities.objects.get(id= cityid)
    with open(fileName) as f:
        lines = f.read().splitlines()
    company = None
    for line in lines:
        split_line = line.split('  ')
        if (split_line[0] == 'company'):

            addr = companies[split_line[1]]
            company = Companies.objects.get_or_create(address= addr, name=split_line[1], city_id= city)
        else:
            split_line = line.split(', ')
            starting_bikeShop_id = 1
            ending_bikeshop_id = starting_bikeShop_id + 9
            num_to_Make = random.randint(1, 7)
            for insert in range(num_to_Make):

                bs_pk = random.randint(starting_bikeShop_id, ending_bikeshop_id)

                # this will be none unless it finds, in which case an exception should be caugh
                # and the function should return
                shop = None
                try:
                    shop = BikeShops.objects.get(id=bs_pk)
                except ObjectDoesNotExist:
                    print("Bike Shop was not found. Please take a look at line 35")

                product = Products.objects.get_or_create(name= split_line[0], price= split_line[1], thumbnail= split_line[2], company_code=company[0])

                BikeShops_Products.objects.update_or_create(bikeshop_id= shop, product_id= product[0])