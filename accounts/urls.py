from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.home),
    path('pussy',views.wet),
]

