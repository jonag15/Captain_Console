from django.shortcuts import render, get_object_or_404
from product.models import Product
from product.models import ProductImage

# products = [
#     {'name': 'TÃ¶lvuleikur 1', 'price': 1000},
#     {'name': 'TÃ¶lvuleikur 2', 'price': 1000},
#     {'name': 'TÃ¶lvuleikur 3', 'price': 1000},
#     {'name': 'LeikjatÃ¶lva 1', 'price': 5000},
#     {'name': 'LeikjatÃ¶lva 2', 'price': 5000},
#
# ]

# Create your views here.
def index(request):
    context = {'products': Product.objects.all()}
    return render(request, 'product/index.html', context)

def index_by_name(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context)

def index_by_price(request):
    context = {'products': Product.objects.all().order_by('price')}
    return render(request, 'product/index.html', context)


# def info_index(request):
#    context = {'products': Product.objects.all()}
#    return render(request, 'product/info.html', context)

# /product/1
def get_product_by_id(request, id):
   context = {'products': Product.objects.all()}
   return render(request, 'product/info.html',  {
       'product': get_object_or_404(Product, pk=id)
   })

def get_all_games(request):
    context = {'products': Product.objects.all()}
    return

#Get all products
def get_products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'product/single_product.html', context)