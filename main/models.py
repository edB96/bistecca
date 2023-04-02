from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role


class Deal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='nessuno')
    idcard_fronte = models.ImageField(verbose_name="Carta d'identita - Fronte", upload_to='images/idcards/fronte')
    idcard_retro = models.ImageField(verbose_name="Carta d'identita - Retro", upload_to='images/idcards/retro')
    ts_fronte = models.ImageField(verbose_name="Tessera Sanitatia - Fronte", upload_to='images/TS/fronte')
    ts_retro = models.ImageField(verbose_name="Tessera Sanitatia - Retro", upload_to='images/TS/retro')
    data_emissione = models.DateField(default=datetime.now())
    data_scadenza = models.DateField(default=datetime.now())
    numero_documento = models.CharField(max_length=20)
    comune_rilascio = models.CharField(max_length=100)

    def __str__(self):
        return self.title