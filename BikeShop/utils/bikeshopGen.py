from BikeShop.models import BikeShops, Cities, Companies



# These methods will generate/regenerate all of the data for bike shops and companies

shops= [
    ['Daves Bike Shop', '221 Main St', 'Topeka'],
    ['Mountain Bikes', '1457 71st St', 'Denver'],
    ['Smith and Sons Bikes', '258 Bluemont St', 'Topeka'],
    ['Johns Wheels', '102 Main St', 'San Francisco'],
    ['Desert Wheels', '258 14th St', 'Austin'],
    ['Premium Bikes', '963 Johnson Rd', 'Boston'],
    ['Pro Bike Store', '249 23rd St', 'Austin'],
    ['Cycling Supply Store', '223 Main St', 'San Francisco'],
    ['Ultimate Biking Supplies', '500 Overton Rd', 'Boston'],
    ['Bikes For Everyone', '1478 12th St', 'Denver']
]


def insertBikeShops():
    for shop in shops:
        BikeShops.objects.update_or_create(name=shop[0], address=shop[1], city_id=Cities.objects.get(name=shop[2]))

    insertCompanies()




companies =[
    ['Specialized', '15130 Concord Circle', 'San Francisco'],
    ['Trek', '122 Main Street', 'Waterloo'],
    ['Giant', '3587 Old Conejo Road', 'Sacremento'],
    ['Santa Cruz', '2841 Mission Street', 'Sacremento'],
    ['Kona', '2455 Salashan Loop', 'Bend'],
    ['Yeti', '621 CORPORATE CIR., UNIT B', 'Denver'],
    ['Pivot', '1807 West Drake Drive', 'Phoenix'],
    ['Cannondale', '1234 W 2nd Street', 'Sacremento'],
    ['Rocky Mountain', '7894 Mountain Rd', 'Bend'],
    ['Transition', '1600 Carolina St', 'Bend'],
    ['Whyte USA', '4567 Bike St', 'Sacremento']
]

def insertCompanies():
    for company in companies:
        Companies.objects.update_or_create(name=company[0], address=company[1], city_id=Cities.objects.get(name=company[2]))