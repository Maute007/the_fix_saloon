# Generated by Django 4.2.5 on 2024-01-04 10:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_product_sinal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Tipo_De_trabalho',
            new_name='tipo_de_trabalho',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sinal',
        ),
        migrations.AddField(
            model_name='product',
            name='numero_produtos_mes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='total_valor_mensal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='data_entrega',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantidade',
            field=models.IntegerField(verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='product',
            name='valor_pago',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='valor_trabalho',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.CreateModel(
            name='HistoricalTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.product')),
            ],
            options={
                'ordering': ['-data_registro'],
            },
        ),
    ]
