# Generated by Django 3.1.5 on 2021-01-30 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_auto_20210130_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 30, 20, 24, 46, 863029)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_username',
            field=models.CharField(default='noel', max_length=100),
        ),
    ]