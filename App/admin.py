from django.contrib import admin
from django.utils import timezone
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'Tipo_De_trabalho', 'quantidade', 'valor_trabalho',
                    'valor_pago', 'get_status', 'get_sinal', 'metodo_de_pagamento', 'assunto', 'data_de_criacao')
    search_fields = ('id', 'nome', 'telefone', 'Tipo_De_trabalho')
    readonly_fields = ('id', 'nome', 'telefone', 'Tipo_De_trabalho', 'valor_trabalho', 'quantidade',
                       'sinal', 'assunto', 'data_de_criacao')

    def save_model(self, request, obj, form, change):
        if 'valor_pago' in form.changed_data:
            valor_trabalho = float(obj.valor_trabalho)
            valor_pago = float(obj.valor_pago) if obj.valor_pago else 0.0
            proporcao = (valor_pago / valor_trabalho) * 100
            obj.sinal = f'{proporcao:.2f}%'

        obj.save()

    def get_sinal(self, obj):
        if obj.sinal:
            return obj.sinal
        else:
            valor_trabalho = float(obj.valor_trabalho)
            valor_pago = float(obj.valor_pago) if obj.valor_pago else 0.0
            proporcao = (valor_pago / valor_trabalho) * 100
            return f'{proporcao:.2f}%'

    get_sinal.short_description = 'Proporção'

    def get_status(self, obj):
        return obj.status

    get_status.short_description = 'Status'

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj and obj.status == 'Entregue':
            fields.append('data_entrega')
        return fields

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj and obj.status == 'Entregue':
            readonly_fields += ('data_entrega',)
        return readonly_fields

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        obj = form.instance
        if obj.status == 'Entregue':
            obj.data_entrega = timezone.now()
            obj.save()


admin.site.register(Product, ProductAdmin)
