from django.urls import path

from .views import ListaUsuarioView, UsuarioCreateView

urlpatterns = [
    path('', ListaUsuarioView.as_view(), name='usuario.index'),
    path('novo/', UsuarioCreateView.as_view(), name='usuario.novo')
]
