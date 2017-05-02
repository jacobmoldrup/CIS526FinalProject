from django.db import models
from django.utils import timezone


# Create your models here.

class Cities(models.Model):
    name = models.TextField(max_length=40)
    state = models.TextField(max_length=20)

    def __str__(self):
        return self.name + ' ' + self.state

    class Meta:
        unique_together = ('name', 'state')


class BikeShops(models.Model):
    name = models.TextField(max_length=40)
    address = models.TextField(max_length=50)
    city_id = models.ForeignKey('Cities', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('city_id', 'address', 'name')


class Companies(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.TextField(max_length=40)
    address = models.TextField(max_length=50)
    city_id = models.ForeignKey('Cities', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'address', 'city_id')


class Bikes(models.Model):

    #https: // docs.djangoproject.com / en / 1.11 / ref / models / fields /
    XSMALL = 1
    SMALL = 2
    MEDIUM = 3
    LARGE = 4
    XLARGE = 5
    BIKE_SIZE_CHOICES =(
        (XSMALL, 'Extra Small'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (XLARGE, 'Extra Large'),
    )
    size = models.IntegerField(
        choices= BIKE_SIZE_CHOICES,
        default= MEDIUM,
    )
    price = models.FloatField(default= 2450)
    type = models.TextField(max_length=40)
    model = models.TextField(max_length=40)
    year = models.IntegerField()
    serialNumber = models.AutoField(primary_key = True)
    thumbnail = models.ImageField(upload_to= 'bikes_pics/')


class Companies_Bikes(models.Model):
    company_code = models.ForeignKey('Companies')
    bike_id = models.ForeignKey('Bikes')

    class Meta:
        unique_together= ('company_code', 'bike_id')

# django does not support multi-column primary keys so delcaring them Unique together and then having django create
# an autoincremented primary key will have to do.
class BikeShops_Bikes(models.Model):
    bikeshop_id = models.ForeignKey('BikeShops')
    bike_id = models.ForeignKey('Bikes')

    class Meta:
        unique_together = ('bikeshop_id', 'bike_id')


class Services(models.Model):
    price = models.FloatField()
    estimated_finish = models.DateTimeField()
    description = models.TextField(max_length=100)
    bike_id = models.ForeignKey('Bikes')
    scheduled_start_date = models.DateTimeField()

    class Meta:
        unique_together = ('bike_id', 'scheduled_start_date')


class Products(models.Model):
    name = models.TextField(max_length=40)
    company_code = models.ForeignKey('Companies')
    thumbnail = models.ImageField(upload_to='images/')
    price = models.TextField()

class BikeShops_Products(models.Model):
    bikeshop_id = models.ForeignKey('BikeShops')
    product_id = models.ForeignKey('Products')

    class Meta:
        unique_together= ('bikeshop_id', 'product_id')



class People(models.Model):
    first_name = models.TextField(max_length=40)
    last_name = models.TextField(max_length=40)
    address = models.TextField(max_length=40)
    city_id = models.ForeignKey('Cities')

    # class Meta:
    #     abstract = True


class Employees(People):
    bikeshop_id = models.ForeignKey('BikeShops')
    title = models.TextField(max_length=40)
    salery = models.FloatField()


class Customer(People):
    email = models.TextField(max_length=50)



class ShopEmployees(models.Model):
    person_id = models.ForeignKey('Employees',  on_delete=models.CASCADE)
    bike_shop_id = models.ForeignKey('BikeShops',  on_delete=models.CASCADE)

    class Meta:
        unique_together=('person_id', 'bike_shop_id')


class CustomerServiceRequests(models.Model):
    person_id = models.ForeignKey('Customer',  on_delete=models.CASCADE)
    service_id = models.ForeignKey('Services' )
    bikeshop_id = models.ForeignKey('BikeShops', on_delete=models.CASCADE)
    bike_id = models.ForeignKey('Bikes')
    time_requested = models.DateTimeField()

    class Meta:
        unique_together = ('time_requested', 'bike_id', 'person_id', 'service_id')


class BikeShopServices(models.Model):
    bikeshop_id = models.ForeignKey('BikeShops',  on_delete=models.CASCADE)
    service_id = models.ForeignKey('Services', )

    class Meta:
        unique_together=('bikeshop_id', 'service_id')

class Customer_Bikes(models.Model):
    person_id = models.ForeignKey('Customer',  on_delete=models.CASCADE)
    bike_id = models.ForeignKey('Bikes',  on_delete=models.CASCADE)

    class Meta:
        unique_together=('person_id', 'bike_id')
