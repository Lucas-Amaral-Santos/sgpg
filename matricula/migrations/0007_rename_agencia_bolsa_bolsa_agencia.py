# Generated by Django 3.2.16 on 2024-05-15 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0006_alter_bolsa_agencia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bolsa',
            old_name='agencia',
            new_name='bolsa_agencia',
        ),
    ]
