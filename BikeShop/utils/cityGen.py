from BikeShop.models import Cities

City_list = {"Topeka":"KS", "Austin":"TX", "San Francisco":"CA", "Boston":"MA", "Denver":"CO", "Wichita":"KS", "Bend":"OR", "Waterloo":"WI", "Sacremento":"CA","Phoenix":"AZ" }




def createCities():
    for k,v in City_list.items():
        Cities.objects.update_or_create(name= k, state= v)
