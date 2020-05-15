import json
from datetime import date
from django.contrib.auth.decorators import login_required
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
from order.models import OrderStatus, DeliveryType
from product.models import Product
from order.models import Order, OrderedProducts
from django.views.decorators.csrf import csrf_protect, csrf_exempt
# Create your views here.
def index(request):
    if request.method == 'POST':
        order_list = []
        order_json = json.loads(request.POST['orderList'])
        for id in order_json['paramName']:
            if id != None:
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
@csrf_exempt        #Setti þetta inn vegna csrf villu
def overview(request):
    if request.method == 'POST':
        #print("Byrja")
        if 'orderList' in request.POST:
            #print("orderlist")
            order_list = []
            order_json = json.loads(request.POST['orderList'])
            for id in order_json['paramName']:
                if id != None:
                    order_list.append(id)
            products = [{
                'id': x.id,
                'name': x.name,
                'price': x.price,
            } for x in Product.objects.filter(pk__in=order_list)]
            return JsonResponse({'data': products})
        elif 'product_form' in request.POST:

            return complete(request)

        else:
            print('overveiw else í POST')
            return render(request, 'order/overview.html')
    else:
        print('Overview else')
        return render(request, 'order/overview.html')

#@login_required
def complete(request):
    if request.method == 'POST':
        order_json = json.loads(request.POST['product_form'])
        order = Order()
        for key, value in order_json.items():
            if key == 'total_price':
                order.total_price = value
                print("total price")
        order.order_status = OrderStatus(id=1)
        order.order_date = date.today()
        order.delivery = DeliveryType(id=2)
        print("rétt fyrir Order save")
        order.save()
        print("Order saved")
        order_id = order.id
        print("producr form byrjun")
        for key, value in order_json.items():
            if key != 'NaN' and value != 'NaN' and key != 'total_price':
                ordered_products = OrderedProducts()
                ordered_products.product_id = key
                ordered_products.quantity = value
                ordered_products.order_id = order_id
                ordered_products.save()
        print("product form")
        products = [{'test1': 2, 'test2': 3}]
        print('Er að fara return json response i complete')
        return JsonResponse({'data': products})

    else:
        print('Else í complete')
        return render(request, 'order/order_complete.html')


def customer_info(request):
    if request.method == 'POST':
        order_json_card = json.loads(request.POST['card_info'])
        customer = Customer()
        for key, value in order_json_card.items():
            if key == 'card_numer':
                customer.card_number = value
                print("card number")
            if key == 'valid_month':
                customer.valid_month = value
                print('month')
            if key == 'valid_year':
                customer.valid_year = value
                print('year')
            if key == 'cvc':
                customer.cvc = value

        order_json_info = json.loads(request.POST['user_info'])
        print("user info form byrjun")

        for key, value in order_json_info.items():
            if key == 'first_name':
                customer.first_name = value
            if key == 'last_name':
                customer.last_name = value
            if key == 'email':
                customer.mail = value
            if key == 'address':
                customer.address = value
            if key == 'zip_code':
                customer.zip_code = value
            if key == 'country':
                customer.country = value
        customer.save()
        print("customer saved")
        products = [{'test1': 2, 'test2': 3}]
        print('Er að fara return json response i complete')
        return JsonResponse({'data': products})
    else:
        print('Else í complete')
        return render(request, 'order/order_complete.html')