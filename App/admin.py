from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'telefone',
        'tipo_de_trabalho', 
        'quantidade',
        'valor_trabalho',
        'metodo_de_pagamento',
        'data_de_criacao',
        'assunto',
        'status',
        'data_entrega',
        'total_valor',
        
    ]

    search_fields = ['nome', 'telefone', 'tipo_de_trabalho', 'assunto']
    list_filter = ['status', 'metodo_de_pagamento', 'data_de_criacao']
    list_per_page = 25

    readonly_fields = [
        'nome',
        'telefone',
        'tipo_de_trabalho',
        'quantidade',
        'valor_trabalho',
        'metodo_de_pagamento',
        'data_de_criacao',
        'assunto',
        'status',
        'data_entrega',
        'total_valor',
        
    ]

admin.site.register(Product, ProductAdmin)

#Maute007.pythonanywhere.com