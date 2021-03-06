from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_login, name='logout'),
    url(r'^register/$', views.register, name='register'),
]