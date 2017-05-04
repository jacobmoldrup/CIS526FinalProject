from django import forms
from django.forms import fields

from .models import Services, BikeShops
from .models import CustomerServiceRequests


class ServiceRequestForm(forms.ModelForm):
    services = forms.ModelChoiceField(queryset=Services.objects.all())
    bikeshops = forms.ModelChoiceField(queryset=BikeShops.objects.all())
    time_requested = forms.DateTimeField()
    class Meta:
        model = CustomerServiceRequests
        fields = ['bike_vin']
