import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from order.forms.personal_info_order import PersonalInfoOrder, CreateOrder
from order.models import Customer
from user.forms.personal_info import PersonalInfo
from user.forms.personal_info import AddressInfo
from user.forms.payment_info import PaymentInfo

#from user.models import Customer

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


  #
    #     print('order/payment - POST')
    #
    # return render(request, 'order/payment.html', {
    #     'form': PersonalInfo(instance=user),
    #     'address': AddressInfo(instance=address),
    #     'carddetails': PaymentInfo(instance=paymentInfo)
    # })




def create_new_order(request):
    if request.method == 'POST':
        form_order = CreateOrder(data=request.POST)
        if form_order.is_valid():
            form_order.save()
            form_user = PersonalInfoOrder(data=request.POST)
            if form_user.is_valid():
                form_user.save()
            #order_info = Order(image=request.POST['image'], product=product)
            return redirect('order_complete')


    return render(request, 'order/order_complete.html', {
        'form_order': form_order
    })