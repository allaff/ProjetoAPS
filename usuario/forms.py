from dataclasses import fields

from django import forms

from .models import Usuario


class UsuarioForm(forms.ModelForm):
  data_nascimento = forms.DateField(widget=forms.TextInput(attrs={"type":"date"}))
  class Meta:
    model = Usuario
    fields = ['nome', 'email', 'data_nascimento', 'senha', 'telefone', 'endereco', 'cpf', 'ativo']