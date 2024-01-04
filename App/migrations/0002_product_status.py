# Generated by Django 4.2.5 on 2024-01-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Concluído', 'Concluído'), ('Entregue', 'Entregue')], default='Pendente', max_length=100),
        ),
    ]
