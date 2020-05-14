from django.shortcuts import render
from django.shortcuts import redirect
from product.models import Product
from django.http import JsonResponse
# Create your views here.
def index(request):
    context = {'products': Product.objects.all()}
    if 'search_filter' in request.GET:
        redirect('product_index', request)
    return render(request, 'home/index.html', context)


def redirecter(request):
    redirect('product_index')