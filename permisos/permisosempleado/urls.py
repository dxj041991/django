from django.urls import path
from .views import *
urlpatterns = [
path ('listar_empleado/', listarEmpelado, name = 'listar_empleado'),


]