from django.shortcuts import render, redirect
from .forms import QuestionForm, FornecedorForm
from .models import *

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question()
            question.question_text = form.clearned_data['question_text']
            question.pub_date = datetime.datetime.now()
            form.save()
            return HTTPResponseRedirect(reverse('index'))
    else:
        form = QuestionForm()
    return render(request, 'create.html', {'form':form})

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
            return(redirect('listar_fornecedores'))
    else:
        form = FornecedorForm()

    return render(request, 'cadastrar_fornecedor.html', {'form':form})