from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from user.models import Address

class PersonalInfo(ModelForm):
    class Meta:
        model = User
        exclude = [ 'id', 'last_login', 'date_joined', 'password', 'is_superuser', 'username', 'is_active', 'is_staff', 'groups', 'user_permissions' ]
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control', }),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'})
        }

class AddressInfo(ModelForm):
    class Meta:
        model = Address   #breytti hér
        exclude = [ 'user' ]
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.NumberInput(attrs={'class': 'form-control'})
        }