from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_main_page, name='post_main_page'),
    url(r'^Bikes$', views.view_all_bikes, name='view_all_bikes'),
    url(r'^request_service$', views.request_service, name='request_service'),
    url(r'^current_services', views.current_services, name='current_services'),
    url(r'^signup/$', views.signup, name='signup'),

]
