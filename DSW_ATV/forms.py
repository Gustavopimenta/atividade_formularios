from django import forms
from .models import Question, Fornecedor

class QuestionForm(forms.Form):
   question_text = forms.CharField(label="Enquete")

class FornecedorForm(forms.Form):
   model = Fornecedor
   fields = ['nome_fornecedor', 'cod_fornecedor']