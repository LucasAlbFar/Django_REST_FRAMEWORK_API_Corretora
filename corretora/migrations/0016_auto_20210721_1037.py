# Generated by Django 3.2.5 on 2021-07-21 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0015_auto_20210721_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimentacao',
            name='total_ativo',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='valor_unitario',
        ),
    ]
