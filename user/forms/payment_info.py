from django.forms import ModelForm, widgets
from user.models import Card

class PaymentInfo(ModelForm):
    class Meta:
        model = Card
        exclude = [ 'user' ]
        widgets = {
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'label':'blabla'}),
            'valid_month': widgets.NumberInput(attrs={'class': 'form-control'}),
            'valid_year': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'})
        }


