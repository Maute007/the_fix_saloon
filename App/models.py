from django.db import models
from django.utils import timezone
from django.db.models import Sum

class Product(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Concluído', 'Concluído'),
        ('Entregue', 'Entregue'),
    ]

    nome = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    tipo_de_trabalho = models.CharField(max_length=100, verbose_name="Tipo de trabalho")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    valor_trabalho = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_de_pagamento = models.CharField(max_length=100, null=True)
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    assunto = models.CharField(verbose_name='Descrição do trabalho', max_length=800)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pendente')
    data_entrega = models.DateTimeField(null=True, blank=True)

    # Novos campos para armazenar totais e dados mensais
    total_valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_valor_mensal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    numero_produtos_mes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Atualizar totais e número de produtos mensais antes de salvar
        if self.data_de_criacao:
            self.atualizar_totais_mensais()
        super().save(*args, **kwargs)

    def atualizar_totais_mensais(self):
        # Calcular totais mensais e número de produtos do mês
        mes_atual = self.data_de_criacao.month
        ano_atual = self.data_de_criacao.year
        produtos_mes = Product.objects.filter(data_de_criacao__month=mes_atual, data_de_criacao__year=ano_atual)
        
        totais_mensais = produtos_mes.aggregate(
            total_valor_mensal=Sum('valor_trabalho'),
            numero_produtos_mes=Sum(1),
            total_valor=Sum('valor_trabalho')
        )

        self.numero_produtos_mes = totais_mensais['numero_produtos_mes']
        self.total_valor_mensal = totais_mensais['total_valor_mensal']
        self.total_valor = totais_mensais['total_valor']

