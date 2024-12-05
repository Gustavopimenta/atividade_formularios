from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255, null=False, blank=False)
    cod_produto = models.CharField(max_length=100, unique=True, blank=False, null=False)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    qntd_estoque = models.IntegerField(null=False, blank=False)
    data_criacao = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.nome_produto

