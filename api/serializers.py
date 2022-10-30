from rest_framework import serializers
from usuario.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    #email = EmailSerializer(many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'data_nascimento', 'senha', 'telefone', 'endereco', 'cpf', 'ativo']
