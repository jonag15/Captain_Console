from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'product_index'),
    path('info/', views.info_index, name = 'product_info'),

]