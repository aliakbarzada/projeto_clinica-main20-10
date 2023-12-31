# Generated by Django 4.0.1 on 2022-01-11 19:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import medicos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('rut', models.CharField(max_length=200, verbose_name='RUT')),
                ('telefono', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Su numero debe estar en este formato:                     '+99 99 9999-0000'.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Telefono')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicos', to='medicos.especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(help_text='Seleccione una fecha', validators=[medicos.models.validar_dia])),
                ('horario', models.CharField(choices=[('1', '07:00 a las 08:00'), ('2', '08:00 a las 09:00'), ('3', '09:00 a las 10:00'), ('4', '10:00 a las 11:00'), ('5', '11:00 a las 12:00')], max_length=10)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='medicos.medico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'unique_together': {('horario', 'dia')},
            },
        ),
    ]
