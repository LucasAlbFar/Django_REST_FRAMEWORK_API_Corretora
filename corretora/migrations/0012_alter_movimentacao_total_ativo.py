# Generated by Django 3.2.5 on 2021-07-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0011_alter_movimentacao_total_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='total_ativo',
            field=models.FloatField(),
        ),
    ]
