# Generated by Django 3.2.5 on 2021-07-22 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0045_movimentacao_valor_unitario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ativo',
            old_name='valor_unitario',
            new_name='preco_mercado',
        ),
    ]
