from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_main_page, name='post_main_page'),
    url(r'^Bikes$', views.view_all_bikes, name='view_all_bikes'),
    url(r'^Services$', views.services, name='services'),
    url(r'^signup/$', views.signup, name='signup'),

]
