from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Deal

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    role = forms.ChoiceField(choices=[('seller', 'Seller'), ('buyer', 'Buyer'), ('partner', 'Partner')])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')


class DealForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    image = forms.URLField(required=False)

    class Meta:
        model = Deal
        fields = ('title', 'description', 'price', 'image')
