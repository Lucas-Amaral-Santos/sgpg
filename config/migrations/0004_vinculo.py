# Generated by Django 3.2.16 on 2023-01-31 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_estadocivil_etnia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vinculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vinculo', models.CharField(max_length=50)),
            ],
        ),
    ]
