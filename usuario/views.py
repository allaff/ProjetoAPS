from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
#from .forms import UsuarioForm, RegistrationForm
from .forms import RegistrationForm
from .models import Usuario


def registrationView(request):
   context = {}
   if request.POST:
      form = RegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         email = form.cleaned_data.get('email')
         raw_password = form.cleaned_data.get('password1')
         account = authenticate(email=email, senha=raw_password)
         login(request, account)
         return redirect('home')
      else:
         context['registration_form'] = form
   else:
      form = RegistrationForm()
      context['registration_form'] = form
   return render(request, 'account/user_register.html', context)

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
  
  
# class UsuarioCreateView(CreateView):
#   model = Usuario
#   form_class = UsuarioForm
#   success_url = '/usuarios/'

#   def form_valid(self, form):
#      form.instance.usuario=self.request.user
#      return super().form_valid(form)

# class UsuarioUpdateView(UpdateView):
#     model = Usuario
#     form_class = UsuarioForm
#     success_url = '/usuarios/'
  
# class UsuarioDeleteView(DeleteView):
#    model = Usuario
#    success_url = '/usuarios/'
