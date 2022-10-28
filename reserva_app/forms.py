from django import forms
from reserva_app.models import reserva

class FormReserva(forms.ModelForm):
    class Meta:
        model= reserva
        fields='__all__'