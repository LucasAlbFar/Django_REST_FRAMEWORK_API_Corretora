# Generated by Django 3.2.5 on 2021-07-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corretora', '0048_rename_tipo_aplicacao_movimentacao_tipo_transacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentacao',
            name='tipo_ativo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
