# Generated by Django 5.1.4 on 2025-04-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='business',
            field=models.BooleanField(default=False),
        ),
    ]
