# Generated by Django 3.2.5 on 2021-07-21 01:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0013_auto_20210720_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentacao',
            name='data_aplicacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
