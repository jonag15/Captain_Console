from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from django import forms

from order.models import Order, OrderedProducts
from user.models import Card


class PersonalInfoOrder(ModelForm):
    class Meta:
        model = User
        exclude = [ 'id']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control' }),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'Country'})
        }

class PaymentInfo(ModelForm):
    class Meta:
        model = Card
        exclude = ['id']
        widgets = {
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'label':'blabla'}),
            'valid_month': widgets.NumberInput(attrs={'class': 'form-control'}),
            'valid_year': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'})
        }


def CreateOrder(request):
    class Meta:
        model = OrderedProducts
        exclude = ['id']
        widgets = {
            'product': widgets.TextInput(attrs={'class': 'Product'}),
            'quantity': widgets.NumberInput(attrs={'class': 'form-control'}),
            'order' : widgets.NumberInput(attrs={'class': 'Order'})
        }