from django.db import models
from django.contrib.auth.models import User
from validation.validators import valida_cpf, valida_senha, valida_telefone

class Usuario(models.Model):
  nome = models.CharField(max_length=256)
  email = models.EmailField(max_length=256)
  senha = models.CharField(max_length=8, validators=[valida_senha], unique=True)
  cpf = models.IntegerField(validators=[valida_cpf], unique=True)
  data_nascimento = models.DateField(null=True)
  telefone = models.CharField(max_length=11, null=True, blank=True, validators=[valida_telefone])
  endereco = models.CharField(max_length=256, null=True, blank=True)
  ativo = models.BooleanField(default=True)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  image = models.ImageField(upload_to='images/', null=True)

  def __str__(self) -> str:
    return self.nome
  