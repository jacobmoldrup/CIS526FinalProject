from django.contrib import admin
from .models import Customer
from .models import BikeShops
from .models import Employees
from .models import Services
from .models import Bikes
from .models import Companies
from .models import Customer_Bikes
from .models import CustomerServiceRequests
from .models import BikeShops_Bikes
from .models import BikeShops_Products
from .models import BikeShopServices
from .models import People
from .models import Products
from .models import Cities
from .models import ShopEmployees

# Register your models here.

admin.site.register(Customer)
admin.site.register(BikeShops)
admin.site.register(Employees)
admin.site.register(Services)
admin.site.register(Bikes)
admin.site.register(Companies)
admin.site.register(Customer_Bikes)
admin.site.register(CustomerServiceRequests)
admin.site.register(BikeShops_Bikes)
admin.site.register(BikeShops_Products)
admin.site.register(BikeShopServices)
admin.site.register(People)
admin.site.register(Products)
admin.site.register(Cities)
admin.site.register(ShopEmployees)

