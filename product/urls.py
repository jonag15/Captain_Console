from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'product_index'),  #All products shown
    path('orderby=name', views.index_by_name, name = 'product_index_name'), #All product orderby name
    path('orderby=price', views.index_by_price, name = 'product_index_price'), #All product orderby price
    path('<int:id>', views.get_product_by_id, name = 'product_description'),
    path('<int:id>', views.get_products, name='product_info'),
    path('games/', views.get_all_games, name = 'product_games'),
    path('games/orderby=name', views.games_by_name, name = 'games_by_name'),
    path('games/orderby=price', views.games_by_price, name = 'games_by_price'),
    path('computers/', views.get_all_computers, name = 'product_computer'),
    path('computers/orderby=name', views.computers_by_name, name = 'computers_by_name'),
    path('computers/orderby=price', views.computers_by_price, name = 'computers_by_price'),

    path('accessory/', views.get_all_accessory, name = 'product_accessory'),
    path('accessory/orderby=name', views.accessory_by_name, name = 'accessory_by_name'),
    path('accessory/orderby=price', views.accessory_by_price, name = 'accessory_by_price'),
    path('spareparts/', views.get_all_spareparts, name = 'product_spareparts'),
    path('spareparts/orderby=name', views.spareparts_by_name, name = 'spareparts_by_name'),
    path('spareparts/orderby=price', views.spareparts_by_price, name = 'spareparts_by_price'),
    path('create-product', views.create_new_product, name='create_new_product'),
    path('delete-product/<int:id>', views.delete_product, name='delete_product'),
    path('update-product/<int:id>', views.update_product, name='update_product'),
    path('choose_product/', views.get_products_to_choose_from, name='choose_product_to_update'),
]