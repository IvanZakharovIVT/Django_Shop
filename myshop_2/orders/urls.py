from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^order_list/$', views.order_list, name='order_list'),
    url(r'^order_items/(?P<id>\d+)$', views.order_items, name='order_items'),
]