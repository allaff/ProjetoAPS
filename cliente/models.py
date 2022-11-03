from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    senha = models.CharField(max_length=6)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField(null=True)
    endereco = models.CharField(null=True)
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
      return self.nome