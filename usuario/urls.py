from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListaUsuarioView, UsuarioCreateView, UsuarioUpdateView,UsuarioDeleteView
from . import views

urlpatterns = [
    path('', login_required(ListaUsuarioView.as_view()), name='usuario.index'),
    path('novo/', login_required(UsuarioCreateView.as_view()), name='usuario.novo'),
    path('editar/<int:pk>/editar', login_required(UsuarioUpdateView.as_view()), name='usuario.editar'),
    path('excluir/<int:pk>/excluir', login_required(UsuarioDeleteView.as_view()), name='usuario.excluir'),
]