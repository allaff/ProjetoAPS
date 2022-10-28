from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
from .forms import UsuarioForm
from .models import Usuario


class ListaUsuarioView(ListView):
  model = Usuario
  queryset = Usuario.objects.all().order_by('nome')

  def get_queryset(self):
      queryset = super().get_queryset()
      queryset = queryset.filter(usuario=self.request.user)
      filtro_nome = self.request.GET.get('nome') or None

      if(filtro_nome):
         queryset = queryset.filter(nome__contains=filtro_nome)
      return queryset
  
  
class UsuarioCreateView(CreateView):
  model = Usuario
  form_class = UsuarioForm
  success_url = '/usuarios/'

  def form_invalid(self, form):
     form.instance.usuario=self.request.user
     return super().form_invalid(form)

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = '/usuarios/'
  
class UsuarioDeleteView(DeleteView):
   model = Usuario
   success_url = '/usuarios/'
