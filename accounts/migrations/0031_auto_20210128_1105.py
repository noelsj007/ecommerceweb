# Generated by Django 3.1.5 on 2021-01-28 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20210128_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_domain',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 11, 5, 9, 332679)),
        ),
    ]
