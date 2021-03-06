# Generated by Django 3.2.5 on 2021-07-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0052_auto_20210723_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='taxa_adm',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='taxa_custodia',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='total_aplicacao',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='total_investido',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='valor_unitario',
            field=models.FloatField(),
        ),
    ]
