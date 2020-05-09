from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'product_index'),
    path('orderby=name', views.index_by_name, name = 'product_index_name'),
    path('orderby=price', views.index_by_price, name = 'product_index_price'),
    path('<int:id>', views.get_product_by_id, name = 'product_description'),
    path('<int:id>', views.get_products, name='product_info'),
    path('games/', views.get_all_games, name = 'product_games'),
    path('create-product', views.create_new_product, name='create_new_product'),
]