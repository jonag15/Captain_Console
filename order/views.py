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
    print("Byrja")
    if 'orderList' in request.POST:
        print("orderlist")
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
        print("product form")
        #order_json = json.loads(request.POST['product_form'])
        for item in 'product_form':
            order = Order()
            print("for loopa byrjuð")
            if item[0] == 'total_price':
                order.total_price = 1234 #item[1]
                print("total price")
            elif item[0] != 'NaN':
                print("item")
                order.total_price = 1234    #Hér var eitthvað sem var á villu
                order.order_status = OrderStatus(id=1) #Hér var eitthvað sem var á villu
                order.order_date = date.today()
                order.delivery = DeliveryType(id=2) #Hér var eitthvað sem var á villu
                #if order.is_valid():               # það var einhver villa hér, commentað út - Unnar 14.5
                print("rétt fyrir Order save")
                order.save()
                print("Order saved")
        order_id = order.id
        ordered_products = OrderedProducts()
        #products ={}
        for item in 'product_form':
            print("producr form byrjun")
            ordered_products.product = Product.objects.first()  #Hér var eitthvað sem var á villu
            ordered_products.quantity = 123 #Hér var eitthvað sem var á villu
            ordered_products.order = Order.objects.last()   #Hér var eitthvað sem var á villu
            print("Rétt fyrir products save")
            ordered_products.save()
            print("Orderer products saved")
            #products[key] = value
        #products = [{'test1': 2, 'test2': 3}]
        #return JsonResponse({'data': order_json})
        return render(request, 'order/order_complete.html', {
            'form': order
        })
    elif request.method == 'POST':
        return render(request, 'product/index.html')
    return render(request, 'order/overview.html')



#@login_required
def complete(request):
    # form_order = CreateOrder(data=request.POST)
    # if form_order.is_valid():
    #     form_order.save()
    #     return redirect('order_complete')
    return render(request, 'order/order_complete.html')

# def create_new_order(request):
#     if request.method == 'POST':
#         form_order = CreateOrder(data=request.POST)
#         if form_order.is_valid():
#             form_order.save()
#             form_user = PersonalInfoOrder(data=request.POST)
#             if form_user.is_valid():
#                 form_user.save()
#             #order_info = Order(image=request.POST['image'], product=product)
#             return redirect('order_complete')
#
#     return render(request, 'order/order_complete.html', {
#         'form_order': form_order
#     })
