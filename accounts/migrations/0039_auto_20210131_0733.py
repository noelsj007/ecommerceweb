# Generated by Django 3.1.5 on 2021-01-31 02:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_auto_20210131_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 31, 7, 33, 12, 640685)),
        ),
    ]
