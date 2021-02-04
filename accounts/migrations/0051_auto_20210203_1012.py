# Generated by Django 3.1.5 on 2021-02-03 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_auto_20210203_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 10, 12, 1, 368635)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_contact',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_home',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 10, 12, 1, 368635)),
        ),
    ]
