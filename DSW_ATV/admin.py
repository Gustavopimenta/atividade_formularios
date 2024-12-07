from django.contrib import admin
from .models import Produto

# Register your models here.
admin.site.register(Produto)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('cod_produto', 'nome_produto', 'preco', 'qntd_estoque', 'data_criacao')

    search_fields = ('cod_produto', 'nome')
    ordering = ('-data_criacao',)