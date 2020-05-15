from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('searchhistory/', views.search_history, name = 'search_history'),
    path('admin-option/', views.admin_option, name='admin_option'),  # Admin view
    path('profile/', views.profile, name='profile'),
    path('profile/picture/', views.picture, name='picture'),
    path('profile/change_payment/', views.change_payment, name='change_payment'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('view_orders/', views.get_orders_to_choose_from, name='view_all_orders'),

]

