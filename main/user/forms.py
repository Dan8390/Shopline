from django.forms import ModelForm, TextInput
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'surname', 'email', 'phone_number', 'country']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control'
            }),
            'password': TextInput(attrs={
                'class': 'form-control'
            }),
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'surname': TextInput(attrs={
                'class': 'form-control'
            }),
            'email': TextInput(attrs={
                'class': 'form-control'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control'
            }),
            'country': TextInput(attrs={
                'class': 'form-control'
            })
        }
