# Generated by Django 3.0.5 on 2020-05-30 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200530_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bought_adpack',
            name='buying_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 30, 14, 8, 32, 294233)),
        ),
    ]
