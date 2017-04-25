from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_main_page, name='post_main_page'),
]