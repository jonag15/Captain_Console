from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.datetime_safe import date

from product.models import Product, SearchHistory
from django.http import JsonResponse
# Create your views here.

#def FourError(request, exception):
#    return render(request, '404NotFound.html')


#def FiveError(request, exception):
#    return render(request, '500.html')


def index(request):
    context = {'products': Product.objects.all()}
    if 'search_filter' in request.GET:
        redirect('product_index', request)
    return render(request, 'home/index.html', context)