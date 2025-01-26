from django import forms
from .models import Categoria, Fornecedor, Question, Produto

class QuestionForm(forms.Form):
   question_text = forms.CharField(label="Enquete")

class FornecedorForm(forms.ModelForm):
   class Meta:
      model = Fornecedor
      fields = ['nome_fornecedor', 'cod_fornecedor']
      widgets = {
         'nome_fornecedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do Fornecedor'}),
         'cod_fornecedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o código do Fornecedor'}),
      }

class CategoriaForm(forms.ModelForm):
   class Meta:
      model = Categoria
      fields = ['nome_categoria', 'cod_categoria']
      widgets = {
         'nome_categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o nome da Categoria'}),
         'cod_categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o codigo da Categoria'}),
      }

class ProdutoForm(forms.ModelForm):
   class Meta:
      model = Produto
      fields = ['nome_produto', 'cod_produto', 'descricao', 'preco', 'qntd_estoque', 'categorias', 'fornecedor']
      widgets = {
         'nome_produto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o nome da Categoria'}),
         'cod_produto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o codigo do produto'}),
         'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Informe a Descrição do produto'}),
         'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Informe o preço do produto', 'step': '0.01'}),
         'qntd_estoque': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Informe a quantidade em estoque'}),
         'categorias': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
         'fornecedor': forms.Select(attrs={'class': 'form-control'}),
      }