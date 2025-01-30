from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, FornecedorForm, CategoriaForm, ProdutoForm
from .models import *

# CBV teste

from django.views.generic import ListView
from .models import Produto, Categoria, Fornecedor

class ProdutoListView(ListView):
    model = Produto
    template_name = "produtos/index.html"
    context_object_name = "produto"

class CategoriaListView(ListView):
    model = Categoria
    template_name = "produtos/listar_categoria"
    context_object_name = "categorias"

class FornecedorListView(ListView):
    model = Fornecedor
    template_name = "produtos/listar_fornecedores.html"
    context_object_name = "fornecedores"

def detalhes(request, pk):
    detalhes_produto = get_object_or_404(Produto, id=pk)
    context = {
        'produtos': detalhes_produto 
    }
    return render(request, 'detalhes_produtos.html', context)

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'cadastrar_categoria.html', {'form': form})

def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm()

    return render(request, 'cadastrar_fornecedor.html', {'form':form})

def cadastrar_produtos(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produto.html', {'form': form})