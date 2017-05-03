from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_main_page, name='post_main_page'),
    url(r'^Bikes$', views.bikes, name='bikes'),
    url(r'^SignIn$', views.login, name='login'),
    url(r'^Services$', views.services, name='services'),
    url(r'^Favorites$', views.favorites, name='favorites'),
    url(r'^Cart$',views.cart,name='cart'),
    url(r'^bike/$', views.getBike, name='bike'),



]
