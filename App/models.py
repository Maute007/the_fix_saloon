from django.db import models
from django.utils import timezone

class Product(models.Model):
    CHOICES = [
        ('0%', '0%'),
        ('25%', '25%'),
        ('50%', '50%'),
        ('75%', '75%'),
        ('100%', '100%'),
    ]
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Concluído', 'Concluído'),
        ('Entregue', 'Entregue'),
    ]
    
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    Tipo_De_trabalho = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100)
    valor_trabalho = models.CharField(max_length=100)
    valor_pago = models.CharField(max_length=100, null=True)
    sinal = models.CharField(verbose_name='Proporção', max_length=100, choices=CHOICES, editable=False)
    metodo_de_pagamento = models.CharField(max_length=100, null=True)
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    assunto = models.CharField(verbose_name='Descrição', max_length=800)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pendente')
    data_entrega = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if self.valor_trabalho and self.valor_pago:
            valor_trabalho = float(self.valor_trabalho)
            valor_pago = float(self.valor_pago)
            proporcao = (valor_pago / valor_trabalho) * 100

            if proporcao >= 100:
                self.sinal = '100%'
            elif proporcao >= 75:
                self.sinal = '75%'
            elif proporcao >= 50:
                self.sinal = '50%'
            else:
                self.sinal = '0%'
        
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'PRODUTOS'
