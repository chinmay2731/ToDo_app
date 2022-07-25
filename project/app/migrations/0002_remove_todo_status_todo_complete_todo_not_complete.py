# Generated by Django 4.0.4 on 2022-06-01 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
        migrations.AddField(
            model_name='todo',
            name='Complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='Not_Complete',
            field=models.BooleanField(default=False),
        ),
    ]
