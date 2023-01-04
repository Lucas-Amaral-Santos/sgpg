# Generated by Django 3.2.16 on 2023-01-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='estrangeiro',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='professor',
            name='tipo_docente',
            field=models.CharField(blank=True, choices=[('Permanente', 'Permanente'), ('Colaborador', 'Colaborador'), ('Coorientador', 'Coorientador'), ('Visitante', 'Visitante'), ('Pos Doutor', 'Pós Doutor')], max_length=100, null=True),
        ),
    ]