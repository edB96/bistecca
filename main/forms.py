from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Deal
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Field, Row, Column, Submit
from django.urls import reverse_lazy

class DateInput(forms.DateInput):
    input_type = 'date'

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    role = forms.ChoiceField(choices=[('seller', 'Seller'), ('buyer', 'Buyer'), ('partner', 'Partner')])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

class AdeguataForm(forms.Form):
    idcard_fronte = forms.ImageField(label="Carta d'identita - Fronte")
    idcard_retro = forms.ImageField(label="Carta d'identita - Retro")
    ts_fronte = forms.ImageField(label="Tessera Sanitatia - Fronte")
    ts_retro = forms.ImageField(label="Tessera Sanitatia - Retro")
    data_emissione = forms.DateField(widget=DateInput)
    data_scadenza = forms.DateField(widget=DateInput)
    numero_documento = forms.CharField(max_length=20)
    comune_rilascio = forms.CharField(max_length=100)
    gdpr = forms.BooleanField(label='Dichiaro di aver preso visione dell\'informativa sulla privacy')

    class Meta:
        model = Deal
        fields = ('title', 'idcard_fronte','idcard_retro','ts_fronte','ts_retro','data_emissione', 
                  'data_scadenza', 'numero_documento', 'comune_rilascio')


class AnagraficaForm(forms.Form):
    nome_azienda = forms.CharField(max_length=100)
    data_costituzione = forms.DateField(widget=DateInput)
    p_iva = forms.CharField(max_length=11, min_length=11, label="Partita IVA")
    cf = forms.CharField(max_length=16, min_length=16, label="Codice Fiscale")
    
    sede_leg_citta = forms.CharField(max_length=50, label="Citt\u00E0")
    sede_leg_indirizzo = forms.CharField(max_length=50, label="Indirizzo")
    sede_leg_numero_civico = forms.CharField(max_length=50, label="Numero Civico")
    #sede_leg_cap = forms.CharField(max_length=50, label="CAP")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('add_deal_anagrafica')
        self.helper.form_method = 'GET'
    class Meta:
        model = Deal
        fields = ('nome_azienda', 'data_costituzione','p_iva','cf','sede_leg_citta', 
                  'sede_leg_indirizzo', 'sede_leg_numero_civico', 'sede_leg_cap')
