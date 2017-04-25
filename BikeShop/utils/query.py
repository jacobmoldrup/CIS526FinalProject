from django.db import connection
from BikeShop.models import BikeShops_Bikes, Companies_Bikes

# these will need to be populated with queries, some we can probably reuse from my other project

queryList ={

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