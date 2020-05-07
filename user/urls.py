from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'user_index'),
    path('searchhistory/', views.search_history, name = 'search_history'),
]