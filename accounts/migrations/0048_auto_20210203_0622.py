# Generated by Django 3.1.5 on 2021-02-03 00:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_auto_20210202_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 6, 22, 17, 646546)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_domain',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 6, 22, 17, 646546)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_selected',
            field=models.TextField(default=False),
        ),
    ]
