from django.db import connection
from BikeShop.models import BikeShops_Bikes, Companies_Bikes

# these will need to be populated with queries, some we can probably reuse from my other project

queryList ={
    'allShops': "select bs.name as NAME, bs.address as ADDR, c.name as CITY, c.state as STATE from BikeShop_bikeshops bs join BikeShop_cities c on bs.city_id_id = c.id",
    'findBikeAtShops': "select bikes.serialNumber, bikes.type, bikes.model, bikes.price, bikes.size, bikes.thumbnail, bikes.year, c.name as Company from BikeShop_bikeshops_bikes bsb join BikeShop_bikes bikes on bsb.bike_id_id = bikes.serialNumber join BikeShop_companies_bikes cb on cb.bike_id_id = bikes.serialNumber join BikeShop_companies c on c.code = cb.company_code_id where bsb.bikeshop_id_id = %s",
    'productsAtShop' : "select p.name, p.thumbnail,p.price, comp.name as Company from BikeShop_bikeshops_products bsp join BikeShop_products p on bsp.product_id_id = p.id join BikeShop_companies comp on comp.code = p.company_code_id where bsp.bikeshop_id_id = 3"
}
'''
EXAMPLE QUERY (requires exact spelling), could also search by company or other things here too
SELECT b.id as BID, b.model as BMOD, b.released as BREL, b.kind as BKIND, c.name as CNAME, c.id as CID FROM Bikes b
join Companies c on c.id = b.company_code
WHERE
b.model = %s
'''


# returns the results as a dictionary so you can grab by column name
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns,row))
        for row in cursor.fetchall()
    ]

# query type is a key in the QueryList dictionary, paramters are passed in
# from the view, and then inserted into the query
def makeQuery(queryType, params):

    with connection.cursor() as cursor:
        query = queryList[queryType]
        cursor.execute(query, params)
        results = dictfetchall(cursor)
    return results

# in some cases its best to return None vs throwing a DoesNotExist Exception
# Classmodel is the model name and this will grab one object.
def get_or_none(classmodel, pk):
    try:
        return classmodel.objects.get(pk)
    except classmodel.DoesNotExists:
        return None