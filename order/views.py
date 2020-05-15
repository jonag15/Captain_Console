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
    if 'product_form' in request.POST:
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
        return render(request.GET, 'order_complete', {
            #'order': Order(order),
            #'ordered_product': OrderedProducts(OrderedProducts.objects.get(id= order_id))

        })
        #products = [{'test1': 2, 'test2': 3}]
        #return render(request, 'order/order_complete.html')
        #return JsonResponse({'data': products})
        #complete(request)


        #return redirect('order_complete')
        #return render(request, 'product/order_complete.html', {})

        # products = [{'test1': 2, 'test2': 3}]
        #
        # return JsonResponse({'data': products})
        #return render(request, 'order/order_complete.html') #, {
        #     'form': order,
        #     'form_product': ordered_products
        # })
    # elif request.method == 'POST':
    #     return render(request, 'product/index.html')
    else:

        return render(request, 'order/overview.html')



#@login_required
# def complete(request):
#     order_json = json.loads(request.POST['product_form'])
#     order = Order()
#     for key, value in order_json.items():
#         if key == 'total_price':
#             order.total_price = value
#             print("total price")
#     order.order_status = OrderStatus(id=1)
#     order.order_date = date.today()
#     order.delivery = DeliveryType(id=2)
#     print("rétt fyrir Order save")
#     order.save()
#     print("Order saved")
#     order_id = order.id
#     print("producr form byrjun")
#     for key, value in order_json.items():
#         if key != 'NaN' and value != 'NaN' and key != 'total_price':
#             ordered_products = OrderedProducts()
#             ordered_products.product_id = key
#             ordered_products.quantity = value
#             ordered_products.order_id = order_id
#             ordered_products.save()
#     print("product form")
#
#     products = [{'test1': 2, 'test2': 3}]
#
#
#
#     return JsonResponse({'data': products})
#     #return redirect('order_complete')

