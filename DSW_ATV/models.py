from django.db import models
from .validators import validate_price, validate_stock, validate_code, validate_lenght

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=255, null=False, blank=False, verbose_name="Nome da Categoria")
    cod_categoria = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.nome_categoria

class Fornecedor(models.Model):
    nome_fornecedor = models.CharField(max_length=255, null=False, blank=False)
    cod_fornecedor = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.nome_fornecedor

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data publicada')

    def __str__(self):
        return self.question_text

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255, null=False, blank=False, validators=[validate_lenght])
    cod_produto = models.CharField(max_length=100, unique=True, blank=False, null=False, validators=[validate_code])
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price])
    qntd_estoque = models.IntegerField(null=False, blank=False, validators=[validate_stock])
    data_criacao = models.DateField(auto_now_add=True) 
    categorias = models.ManyToManyField(Categoria)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nome_produto
        