# Generated by Django 3.2.5 on 2021-07-21 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0030_auto_20210721_2050'),
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
            field=models.FloatField(default=4.9),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='taxa_custodia',
            field=models.FloatField(default=8.9),
        ),
    ]
