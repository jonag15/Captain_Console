from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'product_index'),
    path('orderby=name', views.index_by_name, name = 'product_index_name'),
    path('orderby=price', views.index_by_price, name = 'product_index_price'),
    path('<int:id>', views.get_product_by_id, name = 'product_description'),
    path('<int:id>', views.get_products, name='product_info'),
    path('games/', views.get_all_games, name = 'product_games'),
    path('computers/', views.get_all_computers, name = 'product_computer'),
    path('accessory/', views.get_all_accessory, name = 'product_accessory'),
    path('spareparts/', views.get_all_spareparts, name = 'product_spareparts'),
    path('create-product', views.create_new_product, name='create_new_product'),
    path('delete-product/<int:id>', views.delete_product, name='delete_product'),
    path('update-product/<int:id>', views.update_product, name='update_product'),
    path('choose_product/', views.get_products_to_choose_from, name='choose_product_to_update'),
]