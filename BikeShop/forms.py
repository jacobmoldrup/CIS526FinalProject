import datetime

from django import forms
from django.forms import fields

from .models import Services, BikeShops
from .models import CustomerServiceRequests


class ServiceRequestForm(forms.ModelForm):
    time_requested = forms.DateTimeField(initial=datetime.date.today)
    bike_vin = forms.CharField(max_length=10)
    class Meta:
        model = CustomerServiceRequests
        fields = ['service_id', 'bikeshop_id', 'time_requested']

class SearchForm(forms.Form):
    query = forms.CharField(label= 'Shop Search', max_length = 50)

