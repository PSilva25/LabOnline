# Generated by Django 2.2.1 on 2019-05-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0010_remove_aluno_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horarios_laboratorio',
            name='aluno',
            field=models.TextField(default=''),
        ),
    ]
