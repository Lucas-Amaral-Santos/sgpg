# Generated by Django 3.2.16 on 2024-05-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0004_auto_20240508_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolsa',
            name='agencia',
            field=models.CharField(max_length=200, verbose_name='Agência de Fomento:'),
        ),
    ]