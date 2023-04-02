from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Deal
from django.forms.widgets import SelectDateWidget

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    role = forms.ChoiceField(choices=[('seller', 'Seller'), ('buyer', 'Buyer'), ('partner', 'Partner')])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')


class DealForm(forms.Form):
    title = forms.CharField(max_length=100)
    idcard_fronte = forms.ImageField(label="Carta d'identita - Fronte")
    idcard_retro = forms.ImageField(label="Carta d'identita - Retro")
    ts_fronte = forms.ImageField(label="Tessera Sanitatia - Fronte")
    ts_retro = forms.ImageField(label="Tessera Sanitatia - Retro")
    data_emissione = forms.DateField(widget=SelectDateWidget)
    data_scadenza = forms.DateField(widget=SelectDateWidget)
    numero_documento = forms.CharField(max_length=20)
    comune_rilascio = forms.CharField(max_length=100)

    class Meta:
        model = Deal
        fields = ('title', 'idcard_fronte','idcard_retro','ts_fronte','ts_retro','data_emissione', 
                  'data_scadenza', 'numero_documento', 'comune_rilascio')
