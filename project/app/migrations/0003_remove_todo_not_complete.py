# Generated by Django 4.0.5 on 2022-06-04 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_todo_status_todo_complete_todo_not_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='Not_Complete',
        ),
    ]