# Generated by Django 3.2.5 on 2021-07-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(default='0', max_length=11),
        ),
    ]