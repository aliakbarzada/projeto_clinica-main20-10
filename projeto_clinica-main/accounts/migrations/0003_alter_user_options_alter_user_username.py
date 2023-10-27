import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Un nombre corto que se utilizará. para identificarlo de forma única en la plataforma.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Por favor proporcione un nombre de usuario válido. Este valor debe contener solo letras, números.y estos caracteres: @/./+/-/_.', 'invalido')], verbose_name='Usuario'),
        ),
    ]
