from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

from django import forms

from .models import Usuario

class RegistrationForm(UserCreationForm):
  email = forms.EmailField(max_length=100, help_text="Campo obrigatório. Digite um endereço de e-mail válido")
  class Meta:
    model = Usuario
    fields = ('email', 'nome', 'password1', 'password2')
    
# class UsuarioForm(forms.ModelForm):
#   data_nascimento = forms.DateField(widget=forms.TextInput(attrs={"type":"date"}))

#   image = forms.ImageField(label='Imagem', required=False)
#   class Meta:
#     model = Usuario
#     fields = ['nome', 'email', 'data_nascimento', 'senha', 'telefone', 'endereco', 'cpf', 'ativo', 'image']