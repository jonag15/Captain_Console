from django.forms import ModelForm, widgets
from user.models import UserImage
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = UserImage
        exclude = [ 'id', 'user' ]
        widgets = {
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }

