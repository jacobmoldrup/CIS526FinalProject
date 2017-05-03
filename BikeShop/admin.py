from django.contrib import admin
from .models import BikeShops
from .models import Services
from .models import Bikes
from .models import Companies
from .models import CustomerServiceRequests
from .models import BikeShops_Bikes
from .models import BikeShops_Products
from .models import Products
from .models import Cities

# Register your models here.

admin.site.register(BikeShops)
admin.site.register(Services)
admin.site.register(Bikes)
admin.site.register(Companies)
admin.site.register(CustomerServiceRequests)
admin.site.register(BikeShops_Bikes)
admin.site.register(BikeShops_Products)
admin.site.register(Products)
admin.site.register(Cities)
