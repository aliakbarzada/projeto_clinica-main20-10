# Generated by Django 4.0.1 on 2023-10-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0003_alter_especialidad_nombre_alter_medico_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
    ]
