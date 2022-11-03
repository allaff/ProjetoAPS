from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UsuarioSerializer

from usuario.models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('nome')
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        usuarios = super().get_queryset()
        usuarios = usuarios.filter(usuario=self.request.user)
        return usuarios
    