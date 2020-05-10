from django.forms import ModelForm, widgets
from django.contrib.auth.models import User


class PersonalInfo(ModelForm):
    class Meta:
        model = User
        exclude = [ 'id' ]
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_login': widgets.TextInput(attrs={'class': 'form-control'})
        }