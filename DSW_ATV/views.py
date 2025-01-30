from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, FornecedorForm, CategoriaForm, ProdutoForm
from .models import *

def index(request):
    produto = Produto.objects.all()
    context = {
        'produto': produto
    }
    return render(request, 'index.html', context)

def detalhes(request, pk):
    detalhes_produto = get_object_or_404(Produto, id=pk)
    context = {
        'produtos': detalhes_produto 
    }
    return render(request, 'detalhes_produtos.html', context)

def listar_categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'listar_categorias.html', context)

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'cadastrar_categoria.html', {'form': form})

def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    context = {
        'fornecedores': fornecedores
        }
    return render(request, 'listar_fornecedores.html', context)

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