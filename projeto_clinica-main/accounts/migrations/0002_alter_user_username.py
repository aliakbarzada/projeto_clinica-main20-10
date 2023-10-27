import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Un nombre corto que se utilizará para identificarlo de manera única en la plataforma.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Introduzca un nombre de usuario válido. Este valor debe contener solo letras, números y caracteres: @/./+/-/_.', 'invalid')], verbose_name='Usuário'),
        ),
    ]
