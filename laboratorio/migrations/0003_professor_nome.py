# Generated by Django 2.2.1 on 2019-05-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_auto_20190511_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='nome',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
