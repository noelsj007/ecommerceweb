# Generated by Django 3.1.5 on 2021-02-02 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_auto_20210202_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 18, 25, 27, 914341)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 18, 25, 27, 914341)),
        ),
    ]