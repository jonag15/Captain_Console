from django.forms import ModelForm, widgets
from product.models import Product
from django import forms

class ProductCreateForm(ModelForm):
    #image = forms.CharField(widgets=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nafn'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Verð/kr'}),
            'description': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lýsing á vöru'},),
            'quantity': widgets.NumberInput(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }
