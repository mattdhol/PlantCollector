# Generated by Django 3.1.1 on 2020-11-10 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0006_water'),
    ]

    operations = [
        migrations.RenameField(
            model_name='water',
            old_name='water',
            new_name='drink',
        ),
    ]