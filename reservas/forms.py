from dataclasses import fields
from django import forms
from reservas.models import Reserva



class Form_reserva(forms.ModelForm):
    class Meta:
        model   = Reserva
        fields = '__all__'