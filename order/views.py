from django.shortcuts import render
from django.contrib.auth.models import User
from user.forms.personal_info import PersonalInfo
from user.forms.personal_info import AddressInfo
from user.forms.payment_info import PaymentInfo
from user.models import Customer
from user.models import Card



# Create your views here.
def index(request):
    return render(request, 'order/index.html')


def payment(request):
    user = User.objects.filter(id=request.user.id).first()
    address = Customer.objects.filter(id=request.user.id).first()
    paymentInfo = Card.objects.filter(id=request.user.id).first()

    if request.method == 'POST':
        print('order/payment - POST')

    return render(request, 'order/payment.html', {
        'form': PersonalInfo(instance=user),
        'address': AddressInfo(instance=address),
        'carddetails': PaymentInfo(instance=paymentInfo)
    })