# Generated by Django 3.2.16 on 2023-01-31 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_vinculo'),
        ('aluno', '0005_auto_20230131_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabalho',
            name='tipo_vinculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='config.vinculo', verbose_name='Tipo de Vínculo:'),
        ),
    ]