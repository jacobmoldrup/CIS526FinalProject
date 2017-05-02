from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label= 'Shop Search', max_length = 50)