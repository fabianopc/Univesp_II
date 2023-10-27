from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Endereco(models.Model):
    #cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return self.endereco

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Pizza(models.Model):
    nome = models.CharField(max_length=100)
    valor_p = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor P')
    valor_m = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor M')
    valor_g = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor G')
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    imagem = models.ImageField(upload_to='pizzas/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nome}"
    
class Pedido(models.Model):
    TIPOS_PAGAMENTO = (
        ('Dinheiro', 'Dinheiro'),
        ('Debito', 'Debito'),
        ('Credito', 'Credito'),
        ('Pix', 'Pix'),        
    )
    data_hora = models.DateTimeField()
    valor_total = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_pagamento = models.CharField(max_length=15, choices=TIPOS_PAGAMENTO)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='pedidos')
    
    def __str__(self):
        return f'{self.cliente} - {self.valor_total}'
    
class ItensPedido(models.Model):
    item_id = models.IntegerField()
    tipo_item = models.CharField(max_length=10)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=5, decimal_places=2)
    
    pizza = models.ForeignKey("Pizza", on_delete=models.CASCADE, related_name='ItensPedido')
    pedido = models.ForeignKey("Pedido", on_delete=models.CASCADE, related_name='ItensPedido')
        
    def __str__(self):
        return f'{self.item_id} {self.tipo_item} - {self.quantidade} {self.preco_unitario}, ({self.pedido}'