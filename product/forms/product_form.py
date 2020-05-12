from django.forms import ModelForm, widgets
from product.models import Product
from django import forms


class ProductCreateForm(ModelForm):
    #image = forms.CharField(widgets=forms.TextInput(attrs={'class': 'form-control'}))
    #image = widgets.TextInput(attrs={'class': 'form-control'})
    image = forms.CharField(required=True)
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nafn'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Verð/kr'}),
            'description': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lýsing á vöru'}, ),
            'quantity': widgets.NumberInput(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'category': forms.Select(attrs={'class': 'ProductType'}),
            'status': forms.Select(attrs={'class': 'ProductStatus'}),
            'sub_type': forms.Select(attrs={'class': 'ProductSubTypes'}),
            'age_limit': forms.Select(attrs={'class': 'ProductAgeLimit'}),
            'manufacturer' : forms.Select(attrs={'class': 'ProductManufacturer'}),

        }


class ProductUpdateForm(ModelForm):
    #image = forms.CharField(widgets=forms.TextInput(attrs={'class': 'form-control'}))
    #image = forms.TextInput(attrs={'class': 'form-control'})
    image = forms.CharField(required=True)
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nafn'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Verð/kr'}),
            'description': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lýsing á vöru'}, ),
            'quantity': widgets.NumberInput(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'category': forms.Select(attrs={'class': 'ProductType'}),
            'status': forms.Select(attrs={'class': 'ProductStatus'}),
            'sub_type': forms.Select(attrs={'class': 'ProductSubTypes'}),
            'age_limit': forms.Select(attrs={'class': 'ProductAgeLimit'}),
            'manufacturer' : forms.Select(attrs={'class': 'ProductManufacturer'}),

        }