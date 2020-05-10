from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'order_index'),
    path('payment/', views.payment, name = 'order_payment')
]