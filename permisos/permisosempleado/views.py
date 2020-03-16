from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def listarEmpelado (request):
    empleado = Empleado.objects.all()
    return render(request, 'reporte_ausencias.html', {'empleado': empleado})