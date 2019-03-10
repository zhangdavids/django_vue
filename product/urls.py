from django.conf.urls import  url
from . import views

urlpatterns = [
    url('api/$', views.ProductView.as_view(), name='product'),
]