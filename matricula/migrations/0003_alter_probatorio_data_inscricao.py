# Generated by Django 3.2.16 on 2023-01-31 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0002_alter_probatorio_data_inscricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probatorio',
            name='data_inscricao',
            field=models.DateField(default=datetime.datetime(2023, 1, 31, 11, 30, 48, 769264)),
        ),
    ]