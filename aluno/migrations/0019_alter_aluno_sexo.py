# Generated by Django 3.2.16 on 2023-04-20 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0016_grau'),
        ('aluno', '0018_remove_aluno_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='sexo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='config.sexo', verbose_name='Sexo:'),
        ),
    ]
