# Generated by Django 3.2.5 on 2021-07-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0038_alter_movimentacao_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='taxa_adm',
            field=models.FloatField(blank=True, default=4.9),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='taxa_custodia',
            field=models.FloatField(blank=True, default=8.9),
        ),
    ]
