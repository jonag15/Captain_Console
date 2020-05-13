import json
from django.http import JsonResponse
from django.shortcuts import render
from product.models import Product


# Create your views here.
def index(request):
    if request.method == 'POST':
        order_list = []
        order_json = json.loads(request.POST['orderList'])
        for id in order_json['paramName']:
            if id != None:
                order_list.append(id)
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.objects.productimage_set.first().image
        } for x in Product.objects.filter(pk__in = order_list)]
        return JsonResponse({'data': products})
    return render(request, 'order/index.html')


def payment(request):
    return render(request, 'order/payment.html')

def overview(request):
    if request.method == 'POST':
        order_list = []
        order_json = json.loads(request.POST['orderList'])
        for id in order_json['paramName']:
            order_list.append(id)
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
        } for x in Product.objects.filter(pk__in=order_list)]
        return JsonResponse({'data': products})
    return render(request, 'order/overview.html')