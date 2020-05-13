import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from user.forms.personal_info import PersonalInfo
from user.forms.personal_info import AddressInfo
from user.forms.payment_info import PaymentInfo
from user.models import Address
from user.models import Card
from product.models import Product


# Create your views here.
def index(request):
    if request.method == 'POST':
        order_list = []
        order_json = json.loads(request.POST['orderList'])
        for id in order_json['paramName']:
            order_list.append(id)
        products = [ {
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(pk__in=order_list) ]
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