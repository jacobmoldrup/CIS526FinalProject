from django.db import models
from django.utils import timezone

# Create your models here.


class BikeShops(models.Model):
    name = models.TextField(max_length=40)
    address = models.TextField(max_length=50)
    city_id = models.ForeignKey(Cities, on_delete=models.CASCADE)


class Cities(models.Model):
    name = models.TextField(max_length=40)
    state = models.TextField(max_length=20, unique=True)


class Companies(models.Model):
    code = models.IntegerField(primary_key = True)
    name = models.TextField(max_length=40)
    address = models.TextField(max_length=50)
    city_id = models.ForeignKey(Cities, on_delete=models.CASCADE)


class Bikes(models.Model):
    type = models.TextField(max_length=40)
    company_code = models.ForeignKey(Companies, on_delete=models.CASCADE)
    model = models.TextField(max_length=40)
    year = models.IntegerField


class Companies_Bikes(models.Model):
    company_code = models.ForeignKey(primary_key=True)
    bike_id = models.ForeignKey(primary_key=True)


class BikeShops_Bikes(models.Model):
    bikeshop_id = models.ForeignKey(BikeShops, primary_key=True)
    bike_id = models.ForeignKey(Bikes, primary_key=True)
    price = models.FloatField()


class Services(models.Model):
    price = models.FloatField()
    estimated_finish = models.DateTimeField()
    description = models.TextField(max_length=100)
    bike_id = models.ForeignKey(Bikes)
    scheduled_start_date = models.DateTimeField()


class Products(models.Model):
    name = models.TextField(max_length=40)
    company_code = models.ForeignKey(Companies)
    description = models.TextField(max_length=100)


class BikeShops_Products(models.Model):
    bikeshop_id = models.ForeignKey(BikeShops, primary_key=True)
    product_id = models.ForeignKey(Products, primary_key=True)
    price = models.FloatField()


class Companies_Products(models.Model):
    company_id = models.ForeignKey(Companies, primary_key=True)
    product_id = models.ForeignKey(Products, primary_key=True)


class People(models.Model):
    first_name = models.TextField(max_length=40)
    last_name = models.TextField(max_length=40)
    address = models.TextField(max_length=40)
    city_id = models.ForeignKey(Cities, on_delete=models.CASCADE)
    class Meta:
        abstract = True


class Employees(People):
    person_id = models.ForeignKey(People, primary_key=True, on_delete=models.CASCADE)
    bikeshop_id = models.ForeignKey(BikeShops)
    title = models.TextField(max_length=40)
    salery = models.FloatField()


class Customer(People):
    person_id = models.ForeignKey(People, primary_key=True, on_delete=models.CASCADE)
    email = models.TextField(max_length=50)


class ShopEmployees(models.Model):
    person_id = models.ForeignKey(Employees, primary_key=True, on_delete=models.CASCADE)
    bike_shop_id = models.ForeignKey(BikeShops, primary_key=True, on_delete=models.CASCADE)


class CustomerServiceRequests(models.Model):
    person_id = models.ForeignKey(Customer, primary_key=True, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, primary_key=True)
    bikeshop_id = models.ForeignKey(BikeShops, on_delete=models.CASCADE)
    bike_id = models.ForeignKey(Bikes, primary_key=True)


class BikeShopServices(models.Model):
    bikeshop_id = models.ForeignKey(BikeShops, primary_key=True, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, primary_key=True)


class Customer_Bikes(models.Model):
    person_id = models.ForeignKey(Customer, primary_key=True, on_delete=models.CASCADE)
    bike_id = models.ForeignKey(Bikes, primary_key=True, on_delete=models.CASCADE)



