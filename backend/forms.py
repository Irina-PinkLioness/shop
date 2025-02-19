from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Product, Order


class ProductForm(forms.ModelForm):
    def clean_price(self):
        value =self.cleaned_data['price']
        if value < 0:
            raise ValidationError('Not valid')
        return value

    class Meta:
        model = Product
        fields = ['name','category','description','price','stock']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','quantity', 'total_price', 'customer']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

