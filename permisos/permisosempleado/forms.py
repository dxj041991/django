from django import forms
from .models import Empleado
class AutorForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombreCompleto','fechaDesde','fechaHasta','numeroDias']