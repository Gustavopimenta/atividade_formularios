from django.urls import path
from DSW_ATV import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:question_id>', views.detalhes, name='detail'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
]
