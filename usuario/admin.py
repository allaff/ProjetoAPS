from django.contrib import admin
from .models import Usuario

@admin.action(description='Ativar todos os cadastros selecionados')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=True)

@admin.action(description='Desativar todos os cadastros selecionados')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=False)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'senha', 'cpf', 'data_nascimento', 'telefone', 'endereco', 'ativo']
    list_filter = ['ativo', 'data_nascimento']
    search_fields = ['nome']
    actions = [ativar_todos, desativar_todos]

admin.site.register(Usuario, UsuarioAdmin)