from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_main_page, name='post_main_page'),
    url(r'^view_all_bikes', views.view_all_bikes, name='view_all_bikes'),
    url(r'^view_all_products', views.view_all_products, name='view_all_products'),
    url(r'^view_all_shops', views.view_all_shops, name='view_all_shops'),
    url(r'^view_shop_items/(?P<pk>\w+)/$', views.view_shop_items, name='view_shop_items'),

    url(r'^request_service$', views.request_service, name='request_service'),
    url(r'^current_services$', views.current_services, name='current_services'),
    url(r'^signup/$', views.signup, name='signup'),

]
