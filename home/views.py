from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.datetime_safe import date

from product.models import Product, SearchHistory
from django.http import JsonResponse
# Create your views here.
def index(request):
    context = {'products': Product.objects.all()}
    if 'search_filter' in request.GET:
<<<<<<< HEAD
        redirect('product_index', request)
    return render(request, 'home/index.html', context)


def redirecter(request):
    redirect('product_index')
=======
        redirect('/product/', request.GET)
    return render(request, 'home/index.html')
>>>>>>> dfb52ecd19f3c519b5a6cb563195c0514338281b
