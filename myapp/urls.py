from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('add_book', views.add_book, ),
    url('show_books', views.show_books, ),
    ]