# Generated by Django 3.1.5 on 2021-01-30 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_auto_20210130_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_username',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 30, 20, 23, 29, 191735)),
        ),
    ]
