from dataclasses import fields

from django import forms

from .models import Usuario


class UsuarioForm(forms.ModelForm):
  class Meta:
    model = Usuario
    fields = ['nome', 'email','cpf','telefone', 'senha', 'ativo']