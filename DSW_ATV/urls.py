from django.urls import path
from DSW_ATV import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detalhes, name='detail'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
    path('cadastrar_fornecedor/', views.cadastrar_fornecedor, name='cadastrar_fornecedores'),
    path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('cadastrar_produtos/', views.cadastrar_produtos, name='cadastrar_produto'),
]
