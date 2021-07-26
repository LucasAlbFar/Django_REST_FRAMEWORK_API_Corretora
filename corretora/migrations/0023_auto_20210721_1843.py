# Generated by Django 3.2.5 on 2021-07-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0022_alter_movimentacao_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='quantidade',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='taxa_adm',
            field=models.FloatField(default=5.9),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='taxa_custodia',
            field=models.FloatField(default=9.9),
        ),
    ]