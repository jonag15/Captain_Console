from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home_index'),
    path('product', views.redirecter, name = 'rederecter')
]