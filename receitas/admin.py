from django.contrib import admin
from .models import Receita

# Register your models here.

# Isso faz com que os objetos do admin sejam melhor identificados


class ListandoReceitas(admin.ModelAdmin):
    # exibe esses atibrutos ao invés de object1, object2 e etc
    list_display = ('id', 'nome_receita', 'categoria')
    # deixa os atributos do objeto clicáveis
    list_display_links = ('id', 'nome_receita')


admin.site.register(Receita, ListandoReceitas)
