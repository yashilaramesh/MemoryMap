# Generated by Django 5.1.5 on 2025-04-07 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0002_memory_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memory',
            name='user',
        ),
    ]
