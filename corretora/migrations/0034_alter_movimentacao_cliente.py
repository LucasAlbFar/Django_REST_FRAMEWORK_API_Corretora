# Generated by Django 3.2.5 on 2021-07-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0033_auto_20210721_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='cliente',
            field=models.IntegerField(),
        ),
    ]