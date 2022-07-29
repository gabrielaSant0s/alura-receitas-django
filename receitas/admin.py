from django.contrib import admin
from .models import Receita

# Register your models here.

# Isso faz com que os objetos do admin sejam melhor identificados


class ListandoReceitas(admin.ModelAdmin):
    # exibe esses atibrutos ao invés de object1, object2 e etc
    list_display = ('id', 'nome_receita', 'categoria')
    # deixa os atributos do objeto clicáveis
    list_display_links = ('id', 'nome_receita')
    # cria um campo de busca no admin q procura só as receitas por nome
    search_fields = ('nome_receita',)
    # cria um campo de filtro só com as categorias
    list_filter = ('categoria',)
    # cria paginação no caso tera 5 itens por pagina
    list_per_page = 5


# aqui passa a model e classes para o admin
admin.site.register(Receita, ListandoReceitas)
