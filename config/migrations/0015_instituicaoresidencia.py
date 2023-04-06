# Generated by Django 3.2.16 on 2023-03-23 12:26

import colorful.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0014_colegio'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstituicaoResidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao_residencia', models.CharField(max_length=200)),
                ('cor', colorful.fields.RGBColorField(default='#000000')),
            ],
        ),
    ]