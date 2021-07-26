# Generated by Django 3.2.5 on 2021-07-21 23:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0024_auto_20210721_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentacao',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='corretora.cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='cliente_ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='data_aplicacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='quantidade',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='taxa_adm',
            field=models.FloatField(default=4.9),
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='taxa_custodia',
            field=models.FloatField(default=8.9),
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='tipo',
            field=models.CharField(choices=[('A', 'Aplicação'), ('R', 'Resgate')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='total_aplicacao',
            field=models.FloatField(null=True),
        ),
    ]
