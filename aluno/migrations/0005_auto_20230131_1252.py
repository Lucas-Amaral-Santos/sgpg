# Generated by Django 3.2.16 on 2023-01-31 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_estadocivil_etnia'),
        ('aluno', '0004_alter_aluno_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='estado_civil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='config.estadocivil', verbose_name='Estado civil:'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='etnia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='config.etnia', verbose_name='Etnia:'),
        ),
    ]