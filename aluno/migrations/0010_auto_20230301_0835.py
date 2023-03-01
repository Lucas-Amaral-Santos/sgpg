# Generated by Django 3.2.16 on 2023-03-01 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0008_statusoptions'),
        ('aluno', '0009_alter_aluno_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='sexo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='aluno_sexo', to='config.sexo', verbose_name='Sexo:'),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='config.statusoptions')),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='status',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.DO_NOTHING, related_name='aluno_status', to='aluno.status'),
            preserve_default=False,
        ),
    ]