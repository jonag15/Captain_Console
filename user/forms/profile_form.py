from django.forms import ModelForm, widgets
from user.models import UserImage
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = UserImage
        exclude = [ 'id', 'customer_id', 'customer' ]
        widgets = {
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }

