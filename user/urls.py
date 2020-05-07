from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'user_index'),
    path('searchhistory/', views.search_history, name = 'search_history'),
    path('new_user/', views.new_user, name = 'new_user'),
    path('user_area/', views.user_area, name = 'user_area'),
    path('user_area/change_payment/', views.change_payment, name = 'change_payment'),
]

