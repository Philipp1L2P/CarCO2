from django.urls import path
from carco2 import views

urlpatterns = [
    path('', views.carco2, name='carco2'),
]