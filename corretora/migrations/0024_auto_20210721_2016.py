# Generated by Django 3.2.5 on 2021-07-21 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0023_auto_20210721_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimentacao',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='cliente_ip',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='data_aplicacao',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='quantidade',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='taxa_adm',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='taxa_custodia',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='total_aplicacao',
        ),
    ]
