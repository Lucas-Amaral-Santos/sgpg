# Generated by Django 3.2.16 on 2023-03-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0015_auto_20230324_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='portador_deficiencia_qual',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Qual deficiência:'),
        ),
    ]
