from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'order_index'),
    path('payment/', views.payment, name = 'order_payment'),
    path('payment/overview', views.overview, name = 'order_overview'),
    path('payment/overview/complete', views.overview , name='order_complete')
]