# Generated by Django 3.1.3 on 2020-11-27 01:10

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.generate_random_codes, max_length=8, unique=True),
        ),
    ]
