from django import forms
from django.db import models
from .models import *


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['ordered_by', 'shipping_address', 'mobile', 'email', 'payment_method']


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    

    class Meta:
        model = Customer
        fields = ['full_name', 'address', "username", "password", "email"]

    def clean_username(self):
        uname = self.cleaned_data["username"]
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("Customer with this username already exists")
        
        return uname


class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.TextInput())