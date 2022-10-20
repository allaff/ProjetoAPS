from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .forms import UsuarioForm
from .models import Usuario


class ListaUsuarioView(ListView):
  model = Usuario
  queryset = Usuario.objects.all().order_by('nome')
  
class UsuarioCreateView(CreateView):
  model = Usuario
  form_class = UsuarioForm
  success_url = '/usuarios/'