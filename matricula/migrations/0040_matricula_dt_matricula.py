# Generated by Django 3.2.16 on 2023-04-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0039_auto_20230420_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='dt_matricula',
            field=models.DateField(default='1970-01-01', verbose_name='Data de Matrícula:'),
            preserve_default=False,
        ),
    ]