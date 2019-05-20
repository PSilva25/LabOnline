# Generated by Django 2.2.1 on 2019-05-13 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laboratorio', '0008_aluno_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='funcao',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='matricula',
            field=models.TextField(default='', unique=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]