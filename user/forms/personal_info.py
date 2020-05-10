from django.forms import ModelForm, widgets
from django.contrib.auth.models import User

class PersonalInfo(ModelForm):
    class Meta:
        model = User
        exclude = [ 'id', 'last_login', 'date_joined', 'password', 'is_superuser', 'username', 'is_active', 'is_staff', 'groups', 'user_permissions' ]
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'})
        }