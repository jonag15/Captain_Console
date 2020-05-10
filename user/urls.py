from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'user_index'),
    path('searchhistory/', views.search_history, name = 'search_history'),
    path('user_area/', views.user_area, name = 'user_area'),
    path('user_area/change_payment/', views.change_payment, name = 'change_payment'),



    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/picture/', views.picture, name='picture')
]

