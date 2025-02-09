from user.models import Product, Producer
from django.forms import ModelForm, TextInput, NumberInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'price', 'producer', 'description', 'amount']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control'
            }),
            'category': TextInput(attrs={
                'class': 'form-control'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control'
            }),
            'producer': TextInput(attrs={
                'class': 'form-control'
            }),
            'description': TextInput(attrs={
                'class': 'form-control'
            }),
            'amount': NumberInput(attrs={
                'class': 'form-control'
            })
        }


class ProducerForm(ModelForm):
    class Meta:
        model = Producer
        fields = ['title', 'country', 'products', 'description', 'site', 'email', 'phone_numbers']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control'
            }),
            'country': TextInput(attrs={
                'class': 'form-control'
            }),
            'products': TextInput(attrs={
                'class': 'form-control'
            }),
            'description': TextInput(attrs={
                'class': 'form-control'
            }),
            'site': TextInput(attrs={
                'class': 'form-control'
            }),
            'email': TextInput(attrs={
                'class': 'form-control'
            }),
            'phone_numbers': TextInput(attrs={
                'class': 'form-control'
            })
        }
