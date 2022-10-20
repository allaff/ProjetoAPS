from django.db import models


class Usuario(models.Model):
  nome = models.CharField(max_length=256)
  email = models.CharField(max_length=256)
  senha = models.CharField(max_length=6)
  cpf = models.CharField(max_length=11)
  telefone = models.CharField(max_length=9)
  ativo = models.BooleanField(default=True)
