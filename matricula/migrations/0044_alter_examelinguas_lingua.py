# Generated by Django 3.2.16 on 2023-05-25 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0017_linguas'),
        ('matricula', '0043_alter_probatorio_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examelinguas',
            name='lingua',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='exame_linguas', to='config.linguas'),
        ),
    ]
