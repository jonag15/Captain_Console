from django.forms import ModelForm, widgets
from django.contrib.auth.models import User

from order.models import Order
from user.models import Card
#from user.models import Customer       #þarf að laga tengingu

class PersonalInfoOrder(ModelForm):
    class Meta:
        model = User
        exclude = [ 'id', 'last_login', 'date_joined', 'password', 'is_superuser', 'username', 'is_active', 'is_staff', 'groups', 'user_permissions' ]
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control', }),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'})
        }

class PaymentInfo(ModelForm):
    class Meta:
        model = Card
        exclude = []
        widgets = {
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'label':'blabla'}),
            'valid_month': widgets.NumberInput(attrs={'class': 'form-control'}),
            'valid_year': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'})
        }


def CreateOrder(request):
    class Meta:
        model = Order
        exclude = [ 'id', 'last_login', 'date_joined', 'password', 'is_superuser', 'username', 'is_active', 'is_staff', 'groups', 'user_permissions' ]
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control', }),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'})
        }