# Generated by Django 3.1.1 on 2020-11-09 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0003_plant_amount_of_water'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='worth_buying',
            field=models.BooleanField(default=True),
        ),
    ]
