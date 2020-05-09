from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'user_index'),
    path('searchhistory/', views.search_history, name = 'search_history'),
    path('user_area/', views.user_area, name = 'user_area'),
    path('user_area/change_payment/', views.change_payment, name = 'change_payment'),
    path('admin-option/', views.admin_option, name='admin_option'),#Admin view
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]

