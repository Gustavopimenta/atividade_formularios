import re
from django.core.exceptions import ValidationError

def validate_price(value):
    if value <= 0:
        raise ValidationError('O preço do Produto não pode ser 0')
    
def validate_stock(stock):
    if stock <= 0:
        raise ValidationError('O estoque não pode ser 0')
    
def validate_code(code):
    if not re.match(r'^[a-zA-Z0-9]+$', code):
        raise ValidationError('O código deverá apenas conter Letras e Números')
    
def validate_lenght(carac):
    if len(carac) < 3:
        raise ValidationError('O minimo de caracteres é 3')